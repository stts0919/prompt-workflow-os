"""Regression check for `prompt_builder.LANGUAGE_FILES` and
`extract_locale_code`. Run from the repo root:

    python3 tests/_evaluations/runs/2026-Q3-smoke/check_paths.py

This catches two classes of bugs that have already shipped in v1.x:

1. LANGUAGE_FILES paths that are not anchored at REPO_ROOT (e.g. a
   stray `../../` prefix on one locale that breaks the layer load).
2. `extract_locale_code` failing to recognise a locale code, which
   causes the layer to be silently skipped.

The check exits non-zero if any locale fails to load. Add new locales
to `LOCALES_TO_CHECK` below when expanding the manifest.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent.parent.parent
EVAL_DIR = HERE.parent.parent
sys.path.insert(0, str(EVAL_DIR))

import prompt_builder  # noqa: E402

# (case_file, case_index, expected_locale_code)
LOCALES_TO_CHECK = [
    ("tests/language-cases/zh-tw-localization-cases.md", 0, "zh-TW"),
    ("tests/language-cases/zh-cn-localization-cases.md", 3, "zh-CN"),
    ("tests/language-cases/locale-coverage.md", 0, "yue-Hant-HK"),
    ("tests/language-cases/locale-coverage.md", 3, "en-US"),
    ("tests/language-cases/locale-coverage.md", 5, "en-GB"),
    ("tests/language-cases/locale-coverage.md", 7, "ja-JP"),
    ("tests/language-cases/locale-coverage.md", 9, "ko-KR"),
    ("tests/language-cases/locale-coverage.md", 11, "id-ID"),
    ("tests/language-cases/locale-coverage.md", 13, "vi-VN"),
]


def main() -> int:
    failed = 0
    for case_file, idx, expected in LOCALES_TO_CHECK:
        try:
            built = prompt_builder.build_prompt(case_file, case_index=idx)
        except Exception as e:
            print(f"  ✗ {case_file} #{idx + 1}: build failed — {e}")
            failed += 1
            continue
        actual_code = built["locale_code"]
        prompt_chars = len(built["prompt"])
        if actual_code != expected:
            print(f"  ✗ {case_file} #{idx + 1}: locale_code = {actual_code!r}, expected {expected!r}")
            failed += 1
            continue
        # A real loaded layer adds tens of thousands of characters. A
        # bare case text + system prompt is ~1.5 KB.
        if prompt_chars < 5000:
            print(f"  ✗ {case_file} #{idx + 1}: prompt only {prompt_chars} chars — "
                  f"layer for {expected} probably failed to load")
            failed += 1
            continue
        print(f"  ✓ {expected:14s}  {prompt_chars:6d} chars")

    print()
    if failed:
        print(f"FAILED — {failed} locale(s) did not load correctly.")
        print("Common causes:")
        print("  - LANGUAGE_FILES path has a stray `../../` prefix that")
        print("    does not resolve from REPO_ROOT.")
        print("  - extract_locale_code does not match the locale code.")
        return 1
    print("OK — all locales load their LANGUAGE_FILES layer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
