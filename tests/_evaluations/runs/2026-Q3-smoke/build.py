"""Build stub JSONL files for the 2026-Q3 smoke eval round.

For each model listed in `cases.json`, this script:

1. Reads the case manifest.
2. For each case, calls `prompt_builder.build_prompt`.
3. Writes a stub JSONL per model under
   `tests/_evaluations/results/2026-Q3/smoke/<model>/smoke-cases.jsonl`.

Each stub row carries the prompt but an empty `response` field. The
operator runs each prompt against the real model via their own chat
subscription (ChatGPT / Claude.ai / Gemini) and pastes the response
back into the same row. Operator also fills `rubric` per
`tests/_evaluations/rubric.md`.

The project does not use any model API; see
`../../../../shared/MODELS_OF_RECORD.md` § "Architecture".

Usage:

    # build stubs for all models in the manifest
    python3 build.py

    # build stubs for one model only
    python3 build.py --model gpt-6-sol

    # dry-run: print prompt statistics, do not write files
    python3 build.py --dry-run

The script never calls any model API. It only builds prompts and writes
JSONL files.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# File lives at tests/_evaluations/runs/2026-Q3-smoke/build.py, so:
#   HERE         = tests/_evaluations/runs/2026-Q3-smoke/
#   HERE.parent   = tests/_evaluations/runs/
#   HERE.parent.parent = tests/_evaluations/
#   HERE.parent.parent.parent = tests/
#   HERE.parent.parent.parent.parent = repo root
HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent.parent.parent
EVAL_DIR = HERE.parent.parent  # tests/_evaluations/
sys.path.insert(0, str(EVAL_DIR))

from prompt_builder import build_prompt  # noqa: E402
from schema import EvalResult, RubricScore  # noqa: E402

CASES_FILE = HERE / "cases.json"
RESULTS_BASE = REPO_ROOT / "tests" / "_evaluations" / "results" / "2026-Q3" / "smoke"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_manifest() -> dict:
    return json.loads(CASES_FILE.read_text(encoding="utf-8"))


def build_one(case_spec: dict) -> dict:
    """Build a single prompt + metadata dict from one case spec."""
    built = build_prompt(case_spec["case_file"], case_index=case_spec["case_index"])
    return {
        "smoke_id": case_spec["id"],
        "case_file": case_spec["case_file"],
        "case_index": case_spec["case_index"],
        "locale_expected": case_spec["locale"],
        "profile_expected": case_spec["profile"],
        "notes": case_spec.get("notes", ""),
        "prompt_chars": len(built["prompt"]),
        "case_id": built["case_id"],
        "case_kind": built["case_kind"],
        "case_path": built["case_path"],
        "prompt": built["prompt"],
    }


def write_model_stub(model: str, items: list[dict]) -> Path:
    out_dir = RESULTS_BASE / model
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "smoke-cases.jsonl"
    ts = utc_now()
    with out_path.open("w", encoding="utf-8") as f:
        for it in items:
            result = EvalResult(
                run_id=f"2026-Q3/smoke/{model}",
                case_id=it["smoke_id"],
                case_path=it["case_path"],
                case_kind=it["case_kind"],
                model_id=model,
                model_version="",
                timestamp=ts,
                prompt=it["prompt"],
                response="",
                locale_actual="",
                profile_actual="",
                editing_intensity_actual="",
                protected_content_preserved=True,
                failure_conditions_triggered=[],
                rubric=RubricScore(),
                notes=f"smoke round — {it['locale_expected']} / {it['profile_expected']}. {it['notes']}".strip(),
            )
            f.write(json.dumps(result.to_dict(), ensure_ascii=False) + "\n")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build smoke eval stub JSONLs.")
    parser.add_argument("--model", help="only build for this model (default: all in manifest)")
    parser.add_argument("--dry-run", action="store_true",
                        help="print prompt statistics only; do not write files")
    args = parser.parse_args()

    manifest = load_manifest()
    models = [args.model] if args.model else manifest["models"]
    case_specs = manifest["cases"]

    print(f"Building prompts for {len(case_specs)} cases × {len(models)} models")
    print(f"Output base: {RESULTS_BASE}")
    print()

    built_items: list[dict] = []
    for spec in case_specs:
        try:
            item = build_one(spec)
        except Exception as e:
            print(f"  ✗ {spec['id']}: build failed — {e}", file=sys.stderr)
            return 1
        print(f"  ✓ {spec['id']:20s}  {spec['locale']:14s}  "
              f"{item['prompt_chars']:6d} chars")
        built_items.append(item)

    if args.dry_run:
        print()
        print("Dry run — no files written.")
        return 0

    print()
    written: list[Path] = []
    for model in models:
        out = write_model_stub(model, built_items)
        written.append(out)
        print(f"wrote {len(built_items)} stub rows to {out.relative_to(REPO_ROOT)}")

    print()
    print("Operator workflow:")
    print("  1. Open each JSONL row at the file paths above.")
    print("  2. Paste `prompt` into your chat subscription UI")
    print("     (ChatGPT / Claude.ai / Gemini — no API).")
    print("  3. Paste `response` back into the same row.")
    print("  4. Fill `rubric` per tests/_evaluations/rubric.md (5 dimensions).")
    print("  5. Update `locale_actual`, `profile_actual`,")
    print("     `editing_intensity_actual` from the response.")
    print("  6. Note any `failure_conditions_triggered` from the case file.")
    print("  7. Run: python3 tests/_evaluations/auto_scorer.py "
          "tests/_evaluations/results/2026-Q3/smoke/<model>/smoke-cases.jsonl")
    print("  8. Compare across models with:")
    print("       python3 tests/_evaluations/harness.py compare \\")
    print("         --runs 2026-Q3/smoke/gpt-6-sol,2026-Q3/smoke/gpt-6-luna,"
          "2026-Q3/smoke/claude-opus-5,2026-Q3/smoke/gemini-3.8-flash")
    return 0


if __name__ == "__main__":
    sys.exit(main())
