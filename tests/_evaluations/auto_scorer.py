"""Thin auto-scorer for the AI evaluation harness.

This is a guardrail, not a replacement for human scoring. It applies three
obvious checks that can run deterministically without reading the model
output for nuance:

1. **language_check** — the response's main content language matches the
   requested output language (or one of the acceptable alternatives).
2. **banned_phrase_check** — none of the case's failure-condition strings
   appear in the response verbatim. (This is coarse; failure conditions
   are often paraphrased, so a hit is a strong signal but a miss is not a
   clean pass.)
3. **protected_span_check** — every protected span (when the case
   declares them in `fields.protected_content`) appears verbatim in the
   response.

The scorer writes a verdict file at
`<input>.auto-verdict.jsonl` so the human operator can quickly see what
needs a closer look. It never overwrites the operator's `rubric` scores.

Run from repo root:

    python3 tests/_evaluations/auto_scorer.py \
        tests/_evaluations/results/2026-Q3/gpt-5.6-luna/language-cases.jsonl

Optional flags:

    --summary-only    print only the per-case flags without re-writing a file
    --strict          treat any FAIL as an error (non-zero exit code)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

# A minimal language detector. Good enough for the three checks we run; not a
# general-purpose library.
_CJK_RE = re.compile(r"[\u3400-\u9fff]")
_LATIN_RE = re.compile(r"[A-Za-z]")
_TRAD_HINTS = re.compile(r"[\u4e3b\u65b0\u6700\u96fb\u8cc7\u8a0a\u8b80\u8d77\u9078\u898b\u983b\u904b\u904b\u5165]")
_SIMP_HINTS = re.compile(r"[主讯电读选频运运入]")


def detect_script(text: str) -> str:
    """Return `zh-TW`, `zh-CN`, `en`, or `mixed` for the dominant script of `text`.

    Heuristic, not authoritative. Good enough for the auto-scorer's
    obvious-failure detection.
    """
    if not text or not text.strip():
        return "unknown"
    has_cjk = bool(_CJK_RE.search(text))
    has_latin = bool(_LATIN_RE.search(text))
    if has_cjk and not has_latin:
        return _classify_cjk(text)
    if has_latin and not has_cjk:
        return "en"
    return "mixed"


def _classify_cjk(text: str) -> str:
    # Look for characters that are most likely to appear in one variant.
    tw_score = len(_TRAD_HINTS.findall(text))
    cn_score = len(_SIMP_HINTS.findall(text))
    if tw_score == 0 and cn_score == 0:
        # Fall back to script shape: Traditional forms often include
        # specific radicals (e.g. 臺 vs 台). Without distinctive hits we
        # default to zh-CN because most Chinese-language training data is
        # Simplified-dominant.
        return "zh-CN"
    if tw_score > cn_score:
        return "zh-TW"
    return "zh-CN"


def check_language(response: str, expected_locale: str) -> tuple[bool, str]:
    """Did the response use the expected language?

    Auto-scorer only flags *obvious* failures. It distinguishes CJK vs Latin;
    it does NOT try to disambiguate zh-TW from zh-CN (a heuristic that
    misclassifies more often than not). Disambiguating the two is the
    human scorer's job per `rubric.md`.
    """
    if not response.strip():
        return False, "empty response"
    detected = detect_script(response)
    expected = expected_locale.strip().lower()
    if not expected:
        return True, f"no expected locale specified; detected {detected}"
    if expected.startswith("zh") or expected == "yue-hant-hk":
        # Either Traditional or Simplified Chinese — both are acceptable
        # for an obvious-failure check. Human scorer judges 繁 vs 简.
        return detected.startswith("zh") or detected in {"mixed", "yue-Hant-HK"}, \
            f"expected Chinese, detected {detected}"
    if expected.startswith("en"):
        return detected in {"en", "mixed"}, f"expected English, detected {detected}"
    return True, f"unknown expected locale '{expected_locale}'; detected {detected}"


def check_banned_phrases(response: str, failure_conditions: list[str]) -> tuple[bool, str]:
    """Did the response include any failure-condition text verbatim?

    Failure conditions are written in Chinese, so a hit is a strong
    signal — but a miss is not a clean pass (the model can paraphrase
    a failure condition without reusing the wording).
    """
    if not failure_conditions:
        return True, "no failure conditions defined"
    hits = [c for c in failure_conditions if c and c in response]
    if hits:
        return False, f"matched {len(hits)} failure-condition text(s) verbatim: {hits[:3]}"
    return True, "no failure-condition text matched verbatim"


def check_protected_spans(response: str, protected_content: str) -> tuple[bool, str]:
    """Did the response preserve the protected content verbatim?

    `protected_content` may be a single string or a list of strings;
    the parser keeps it as a string for the auto-scorer.
    """
    if not protected_content:
        return True, "no protected content declared"
    # Split on common separators so a multi-span declaration is checked.
    spans = [s.strip() for s in re.split(r"[\n;]+", protected_content) if s.strip()]
    if not spans:
        return True, "no protected content declared"
    missing = [s for s in spans if s not in response]
    if missing:
        return False, f"{len(missing)}/{len(spans)} protected span(s) missing"
    return True, f"all {len(spans)} protected span(s) present"


# ---------------------------------------------------------------------------
# Record-level verdict
# ---------------------------------------------------------------------------

@dataclass
class AutoVerdict:
    case_id: str
    case_path: str
    language_check: dict = field(default_factory=dict)
    banned_phrase_check: dict = field(default_factory=dict)
    protected_span_check: dict = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return all(
            c.get("passed", False)
            for c in (self.language_check, self.banned_phrase_check, self.protected_span_check)
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "case_id": self.case_id,
            "case_path": self.case_path,
            "passed": self.passed,
            "language_check": self.language_check,
            "banned_phrase_check": self.banned_phrase_check,
            "protected_span_check": self.protected_span_check,
        }


def parse_protected_content(fields: dict[str, Any]) -> str:
    """Pull protected_content out of the case's parsed fields.

    The case file schema marks protected content under several possible
    labels depending on the case author. We check the canonical one first,
    then fall back to common alternatives.
    """
    return (
        fields.get("protected_content")
        or fields.get("protected_spans")
        or fields.get("protected")
        or ""
    )


def auto_score(record: dict[str, Any]) -> AutoVerdict:
    fields = record.get("fields") or {}
    expected_locale = fields.get("expected_locale") or ""
    failure_conditions = fields.get("failure_conditions") or []
    if isinstance(failure_conditions, str):
        failure_conditions = [failure_conditions]

    return AutoVerdict(
        case_id=record.get("case_id", ""),
        case_path=record.get("case_path", ""),
        language_check=dict(zip(("passed", "reason"), check_language(record.get("response", ""), expected_locale))),
        banned_phrase_check=dict(zip(("passed", "reason"), check_banned_phrases(record.get("response", ""), failure_conditions))),
        protected_span_check=dict(zip(("passed", "reason"), check_protected_spans(record.get("response", ""), parse_protected_content(fields)))),
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl", help="Path to the JSONL record file (one record per case)")
    parser.add_argument("--summary-only", action="store_true", help="print summary only; do not write a verdict file")
    parser.add_argument("--strict", action="store_true", help="exit non-zero if any case fails")
    args = parser.parse_args()

    src = Path(args.jsonl)
    if not src.exists():
        print(f"missing: {src}", file=sys.stderr)
        return 2

    records: list[dict[str, Any]] = []
    with src.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    verdicts = [auto_score(r) for r in records]

    # Per-case output.
    failed = 0
    for v in verdicts:
        marker = "PASS" if v.passed else "FAIL"
        if not v.passed:
            failed += 1
        print(f"  [{marker}] {v.case_id}")
        for check_name in ("language_check", "banned_phrase_check", "protected_span_check"):
            check = getattr(v, check_name)
            note = check.get("reason", "")
            status = "ok" if check.get("passed") else "FAIL"
            print(f"           {check_name:>20}: {status:>4}  {note}")

    # Summary.
    total = len(verdicts)
    passed = total - failed
    print()
    print(f"summary: {passed}/{total} passed, {failed}/{total} failed")

    if not args.summary_only:
        out = src.with_suffix(".jsonl").with_name(src.stem + ".auto-verdict.jsonl")
        with out.open("w", encoding="utf-8") as f:
            for v in verdicts:
                f.write(json.dumps(v.to_dict(), ensure_ascii=False) + "\n")
        print(f"verdict file: {out}")

    return 1 if (failed and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())