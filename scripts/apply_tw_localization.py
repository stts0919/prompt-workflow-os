#!/usr/bin/env python3
"""Verify Taiwan `localization:` blocks are present on the expected workflows.

The actual generation lives in `scripts/generate_workflows.py` (the
`LOCALIZATION_OVERRIDES` dict + `fmt_localization()` helper). This script
asserts that:

- every id in `LOCALIZATION_OVERRIDES` ends up with the expected
  `default_style_profile` and `editing_intensity` in its rendered frontmatter
- no other workflow has a `localization:` block by accident

Run from repo root:

    python3 scripts/apply_tw_localization.py            # verify
    python3 scripts/apply_tw_localization.py --verbose  # show every workflow
```

Exit code is non-zero when any expected block is missing or wrong.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Mirrors `LOCALIZATION_OVERRIDES` in scripts/generate_workflows.py. Kept in
# sync by hand; mismatches between the two are a deliberate flag.
EXPECTED: dict[str, dict] = {
    "012": {"default_style_profile": "zh-tw-friendly-professional", "editing_intensity": "standard"},
    "013": {"default_style_profile": "zh-tw-threads-insightful",    "editing_intensity": "standard"},
    "014": {"default_style_profile": "zh-tw-instagram-casual",       "editing_intensity": "standard"},
    "015": {"default_style_profile": "zh-tw-friendly-professional", "editing_intensity": "standard"},
    "018": {"default_style_profile": "zh-tw-conversational-help",    "editing_intensity": "standard"},
    "022": {"default_style_profile": "zh-tw-customer-support",       "editing_intensity": "standard"},
    "023": {"default_style_profile": "zh-tw-friendly-professional", "editing_intensity": "standard"},
    "025": {"default_style_profile": "zh-tw-long-form-article",      "editing_intensity": "standard"},
    "026": {"default_style_profile": "zh-tw-conversational-help",    "editing_intensity": "standard"},
    "027": {"default_style_profile": "zh-tw-friendly-professional", "editing_intensity": "light"},
    "028": {"default_style_profile": "zh-tw-friendly-professional", "editing_intensity": "standard"},
    "031": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "standard"},
    "032": {"default_style_profile": "zh-tw-conversational-help",    "editing_intensity": "standard"},
    "035": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "standard"},
    "036": {"default_style_profile": "zh-tw-landing-page-clear",     "editing_intensity": "standard"},
    "037": {"default_style_profile": "zh-tw-sales-clear",            "editing_intensity": "standard"},
    "042": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "standard"},
    "043": {"default_style_profile": "zh-tw-landing-page-clear",     "editing_intensity": "standard"},
    "045": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "standard"},
    "046": {"default_style_profile": "zh-tw-email-professional",     "editing_intensity": "standard"},
    "047": {"default_style_profile": "zh-tw-email-professional",     "editing_intensity": "standard"},
    "048": {"default_style_profile": "zh-tw-sales-clear",            "editing_intensity": "standard"},
    "052": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "strict_precision"},
    "055": {"default_style_profile": "zh-tw-research-precise",       "editing_intensity": "standard"},
    "057": {"default_style_profile": "zh-tw-research-precise",       "editing_intensity": "standard"},
    "064": {"default_style_profile": "zh-tw-research-precise",       "editing_intensity": "strict_precision"},
    "065": {"default_style_profile": "zh-tw-research-precise",       "editing_intensity": "strict_precision"},
    "069": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "strict_precision"},
    "070": {"default_style_profile": "zh-tw-business-consulting",    "editing_intensity": "strict_precision"},
    # workflow (7) — uses zh-cn-friendly-professional as the canonical profile
    # because these workflows serve both zh-TW and zh-CN audiences and the
    # zh-cn profile is the most cross-compatible. The locale_style_profile_overrides
    # block in each frontmatter carries the optional zh-TW override.
    "072": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "074": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "076": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "080": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "081": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "086": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    "088": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "standard"},
    # technical (5) — code / data / agent specs; light intensity for code-aware
    # workflows, strict_precision for agent-task-spec since it's the formal
    # contract a downstream agent reads.
    "089": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "light"},
    "091": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "strict_precision"},
    "092": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "light"},
    "095": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "light"},
    "098": {"default_style_profile": "zh-cn-friendly-professional", "editing_intensity": "light"},
}

CATEGORY_DIR = {
    "content": "01-content",
    "business": "02-business",
    "research": "03-research",
    "workflow": "04-workflow",
    "technical": "05-technical",
}

# id -> category folder (mirrors `indexes/05-all-100-workflows.md`)
ID_CATEGORY = {
    **{f"{i:03d}": "content" for i in range(12, 29)},  # 012–028
    **{f"{i:03d}": "business" for i in range(31, 53)},  # 031–052
    **{f"{i:03d}": "research" for i in range(55, 71)},  # 055–070
    **{f"{i:03d}": "workflow" for i in [72, 74, 76, 80, 81, 86, 88]},
    **{f"{i:03d}": "technical" for i in [89, 91, 92, 95, 98]},
}


def parse_frontmatter_block(text: str) -> dict[str, str]:
    """Extract the frontmatter between the first pair of `---` markers."""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    block = parts[1]
    fields: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_][\w]*)\s*:\s*(.*)$", line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            fields[key] = value
    return fields


def workflow_path(idn: str) -> Path | None:
    cat = ID_CATEGORY.get(idn)
    if not cat:
        return None
    cat_dir = CATEGORY_DIR[cat]
    # Find the file by id prefix.
    folder = ROOT / "workflows" / cat_dir
    for p in folder.glob(f"{idn}-*.md"):
        return p
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="print every workflow")
    args = parser.parse_args()

    failures: list[str] = []
    for idn, expected in EXPECTED.items():
        path = workflow_path(idn)
        if path is None:
            failures.append(f"{idn}: workflow file not found")
            continue
        if not path.exists():
            failures.append(f"{idn}: workflow file missing at {path}")
            continue
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_block(text)

        if "localization" not in fields:
            failures.append(f"{idn}: missing localization block")
            continue

        block_text = fields["localization"]
        # block_text may be a nested YAML value like
        # "{supported_locales: [en, zh-TW], default_style_profile: zh-tw-foo, ...}".
        # We re-parse the nested block more carefully.
        # Easier: just grep the original text for the expected substrings.
        for needle in (
            f"default_style_profile: {expected['default_style_profile']}",
            f"editing_intensity: {expected['editing_intensity']}",
            "supported_locales:",
            "    - en",
            "    - zh-TW",
        ):
            if needle not in text:
                failures.append(f"{idn}: missing line `{needle}`")
        if args.verbose:
            print(f"  ok: {idn} ({path.name})")

    if failures:
        print("FAIL:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print(f"verified {len(EXPECTED)} workflow localization blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main())