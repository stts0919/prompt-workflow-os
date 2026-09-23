"""AI evaluation harness — build prompts from test cases and write stub records.

Usage:

    # Manual (paste into a chat UI; this is the only supported path)
    python3 harness.py build-prompt tests/language-cases/zh-tw-localization-cases.md --case 1 \
        --output /tmp/case-01-prompt.txt

    # Build stub JSONL for a batch (one stub row per case, empty response)
    python3 harness.py run-batch \
        --model gpt-6-sol \
        --cases-glob 'tests/language-cases/zh-tw-localization-cases.md' \
        --run-id 2026-Q3/gpt-6-sol

    # Compare across models (after at least two runs are filled in)
    python3 harness.py compare \
        --runs 2026-Q3/gpt-6-sol,2026-Q3/claude-opus-5,2026-Q3/gemini-3.8-flash \
        --out tests/_evaluations/results/2026-Q3/_compare.md

The harness does **not** call any model itself — neither via API nor via any
other means. Operators evaluate prompts through their own chat subscription
(ChatGPT Plus / Pro, Claude Free / Pro / Max, Gemini AI Pro / Ultra, etc.)
and paste the response back into the JSONL. See
`./operators/manual.md` for the full protocol. The project scope explicitly
excludes API integration; see `shared/MODELS_OF_RECORD.md` § "Architecture".

Reasons the harness never calls a model:

1. The project scope is subscription-only — no API key handling exists
   anywhere in the codebase.
2. Models and surfaces change frequently; the harness stays model-agnostic.
3. The recommended surface is the chat UI (paste-into-UI), so a scripted
   API client would not match the recommended workflow anyway.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from schema import EvalResult, RubricScore  # noqa: E402
import prompt_builder  # noqa: E402


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def cmd_build_prompt(args: argparse.Namespace) -> int:
    """Build a single prompt and write to a file (or stdout)."""
    case_path = args.cases_glob
    total = prompt_builder.count_cases(case_path)
    if args.case_number is None:
        if total != 1:
            print(
                f"{case_path} has {total} cases; pass --case N (1..{total})",
                file=sys.stderr,
            )
            return 2
        case_index = 0
    else:
        if args.case_number < 1 or args.case_number > total:
            print(f"--case must be 1..{total}; got {args.case_number}", file=sys.stderr)
            return 2
        case_index = args.case_number - 1

    built = prompt_builder.build_prompt(case_path, case_index=case_index)
    text = (
        f"<!-- case_id: {built['case_id']} -->\n"
        f"<!-- case_kind: {built['case_kind']} -->\n"
        f"<!-- locale: {built['locale']} -->\n"
        f"<!-- locale_code: {built['locale_code']} -->\n\n"
        f"{built['prompt']}\n"
    )

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"wrote prompt to {args.output}")
    else:
        sys.stdout.write(text)
    return 0


def discover_cases(glob: str) -> list[str]:
    """Expand a glob into a list of case file paths."""
    base = prompt_builder.REPO_ROOT
    paths = sorted(str(p.relative_to(base)) for p in base.glob(glob))
    return paths


def cmd_run_batch(args: argparse.Namespace) -> int:
    """Build prompts for every case and write a stub JSONL per kind.

    The operator runs the prompts (manually or via their own API call), then
    fills in the response fields. The stub file documents the schema.
    """
    case_paths = discover_cases(args.cases_glob)
    run_dir = HERE / "results" / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    per_kind_files: dict[str, list] = {}
    total = 0
    for case_path in case_paths:
        n = prompt_builder.count_cases(case_path)
        for case_index in range(n):
            built = prompt_builder.build_prompt(case_path, case_index=case_index)
            kind = built["case_kind"]
            per_kind_files.setdefault(kind, []).append(built)
            total += 1

    written: list[str] = []
    for kind, items in per_kind_files.items():
        out_path = run_dir / f"{kind}-cases.jsonl"
        with out_path.open("w", encoding="utf-8") as f:
            for built in items:
                result = EvalResult(
                    run_id=args.run_id,
                    case_id=built["case_id"],
                    case_path=built["case_path"],
                    case_kind=kind,
                    model_id=args.model,
                    model_version=args.model_version,
                    timestamp=utc_now(),
                    prompt=built["prompt"],
                    response="",  # operator fills in
                    locale_actual="",
                    profile_actual="",
                    editing_intensity_actual="",
                    protected_content_preserved=True,
                    failure_conditions_triggered=[],
                    rubric=RubricScore(),
                    notes="stub — operator must fill response and rubric",
                )
                f.write(json.dumps(result.to_dict(), ensure_ascii=False) + "\n")
        written.append(str(out_path.relative_to(HERE)))

    for w in written:
        print(f"wrote stub to {w}")
    print(f"total prompts: {total}")
    print("operator workflow:")
    print(f"  1. for each case_id, paste the prompt at `prompt` into the model.")
    print(f"  2. paste the response into `response`.")
    print(f"  3. score per `tests/_evaluations/rubric.md` and fill `rubric`.")
    print(f"  4. update `locale_actual`, `profile_actual`, `editing_intensity_actual`.")
    print(f"  5. note any `failure_conditions_triggered` from the case file.")
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    """Produce a markdown comparison across runs."""
    runs = args.runs.split(",")
    cases: dict[str, dict[str, float]] = {}

    for run_id in runs:
        run_dir = HERE / "results" / run_id
        if not run_dir.exists():
            print(f"missing run dir: {run_dir}", file=sys.stderr)
            continue
        model = run_id.split("/")[-1]
        for jsonl in sorted(run_dir.glob("*.jsonl")):
            with jsonl.open(encoding="utf-8") as f:
                for line in f:
                    row = json.loads(line)
                    cid = row["case_id"]
                    score = row.get("rubric_average", 0.0)
                    cases.setdefault(cid, {})[model] = score

    if not cases:
        print("no cases to compare", file=sys.stderr)
        return 1

    models = sorted({m for c in cases.values() for m in c})
    lines: list[str] = []
    lines.append(f"# Compare: {', '.join(runs)}\n")
    lines.append(f"Generated at: {utc_now()}\n")
    header = "| case_id | " + " | ".join(models) + " |"
    sep = "| --- |" + (" --- |" * len(models))
    lines.append(header)
    lines.append(sep)
    for cid in sorted(cases):
        row = "| " + cid + " | " + " | ".join(
            f"{cases[cid].get(m, ''):.2f}" if cases[cid].get(m) else "" for m in models
        ) + " |"
        lines.append(row)
    lines.append("")
    out = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"wrote comparison to {args.out}")
    else:
        sys.stdout.write(out)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="prompt-workflow-os evaluation harness")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("build-prompt", help="build a single prompt")
    p1.add_argument("cases_glob", help="test file path or glob")
    p1.add_argument("--case", type=int, default=None, dest="case_number",
                    help="1-based case number within the glob")
    p1.add_argument("--output", help="write prompt here (default stdout)")
    p1.set_defaults(func=cmd_build_prompt)

    p2 = sub.add_parser("run-batch", help="build all prompts and write a stub JSONL")
    p2.add_argument("--cases-glob", required=True, dest="cases_glob")
    p2.add_argument("--run-id", required=True, help="e.g. 2026-Q3/gpt-6-sol")
    p2.add_argument("--model", required=True, help="e.g. gpt-6-sol")
    p2.add_argument("--model-version", default="", dest="model_version")
    p2.set_defaults(func=cmd_run_batch)

    p3 = sub.add_parser("compare", help="compare rubric averages across runs")
    p3.add_argument("--runs", required=True,
                    help="comma-separated run ids (e.g. 2026-Q3/gpt-6-sol,2026-Q3/claude-opus-5)")
    p3.add_argument("--out", help="output path (default stdout)")
    p3.set_defaults(func=cmd_compare)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
