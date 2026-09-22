# Taiwan Traditional Chinese Localization Validation Report

Generated after the integration of the `zh-TW` localization layer.

Run from the repository root:

```bash
python3 scripts/validate.py
```

The validator checks both the universal structural rules and the `zh-TW`-specific structural rules. It does **not** score writing quality directly — that requires running the localization cases against a model.

## Result

```text
VALIDATION PASSED — 0 issues
```

The numbers reported by the validator for this run:

| Check                                  | Required | Actual | Status |
| -------------------------------------- | -------: | -----: | ------ |
| `zh-TW` integration files exist        |        7 |      7 | PASS   |
| Router references all zh-TW shared files |     4 |      4 | PASS   |
| Workflow template includes localization metadata | 4 keys | 4 | PASS   |
| zh-TW term glossary entries            |     ≥100 |    145 | PASS   |
| zh-TW style profiles                   |     ≥11  |     11 | PASS   |
| zh-TW localization test cases          |     ≥20  |     22 | PASS   |
| zh-TW output-quality test cases        |     ≥15  |     22 | PASS   |
| Repository has no false-capability claims |       0 |      0 | PASS   |
| Original 100-workflow structure intact |   intact | intact | PASS   |

## What was checked

### Files present

- `shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md`
- `shared/ZH_TW_TERM_GLOSSARY.md`
- `shared/ZH_TW_STYLE_PROFILES.md`
- `shared/ZH_TW_QUALITY_CHECKLIST.md`
- `tests/language-cases/zh-tw-localization-cases.md`
- `tests/workflow-cases/zh-tw-output-quality-cases.md`
- `ZH_TW_LOCALIZATION_VALIDATION_REPORT.md` (this file)

### Router linkage

- `router/AI_ROUTER.md` references all four `shared/ZH_TW_*` files.
- `router/ROUTING_RULES.md` includes a `1.5 zh-TW localization activation` section that maps workflow categories to style profiles.
- `router/CLARIFICATION_PROTOCOL.md` includes a `zh-TW clarification style` subsection.

### Workflow template

- `templates/WORKFLOW_TEMPLATE.md` includes a `localization:` block with:
  - `supported_locales`
  - `default_style_profile`
  - `zh_tw_style_profile`
  - `zh_tw_editing_intensity`
- The template explains how authors select these values and notes the category-based defaults.

### Glossary entries

- `shared/ZH_TW_TERM_GLOSSARY.md` contains **145 numbered entries** organized by category: general UI, AI and technology, business and strategy, marketing and content, product and design, research and data, work and project management, e-commerce and customer support, common conversational expressions, regional variants.

### Style profiles

- `shared/ZH_TW_STYLE_PROFILES.md` defines **11 profiles**: `zh-tw-conversational-help`, `zh-tw-friendly-professional`, `zh-tw-business-consulting`, `zh-tw-social-casual`, `zh-tw-social-insightful`, `zh-tw-sales-clear`, `zh-tw-email-professional`, `zh-tw-research-precise`, `zh-tw-technical-clear`, `zh-tw-sop-direct`, `zh-tw-customer-support`. Each profile has YAML keys plus a sample paragraph.

### Test coverage

- `tests/language-cases/zh-tw-localization-cases.md` covers:
  - Natural Taiwan conversational phrasing
  - Mixed Chinese and English
  - Cross-language output requests (zh-TW → English deliverable; English conversation → zh-TW deliverable)
  - Terminology selection
  - User-preference overrides
  - Hong Kong and Mainland Chinese overrides
  - Technical content preservation
  - Code and URL protection
  - Formal reports with precision
  - Casual social posts
  - Sales copy with hype removal
  - Direct quotation protection
  - AI-pattern reduction path
  - Customer support reply in zh-TW
- `tests/workflow-cases/zh-tw-output-quality-cases.md` covers the same ground with workflow-level details for **22 representative workflows** across all five categories.

### No false-capability claims

The repository must not claim that editing can:

- bypass AI detection,
- remove watermarks,
- prove human authorship.

The validator scans all Markdown files for positive capability statements. Disclaimers and `Required protections` blocks are explicitly allowed. All matches were cleared by the negative-context detector or by refactoring the line. No issue remaining.

The reference to the upstream `Humanizer-zh-TW` skill is documented as **inspiration only**. This layer is original, broader than "removing AI tone", and aligns with the existing `prompt-workflow-os` architecture.

### Original structure

The 100-workflow structure remains intact:

| Category            | Expected | Actual |
| ------------------- | -------: | -----: |
| Content             |       29 |     29 |
| Business            |       24 |     24 |
| Research            |       18 |     18 |
| Workflow            |       17 |     17 |
| Technical           |       12 |     12 |
| **Total**           |    **100** | **100** |

The structural validator (`bash tests/validate.sh`) passes against the unchanged 100-workflow files.

## What was *not* checked

- **Writing quality on real outputs.** The localization cases test AI behavior against a model. They are not scored by the structural validator.
- **Adversarial inputs.** Inputs that try to manipulate the AI into claiming capabilities it does not have are subject to FALLBACK_RULES.md, not to this structural validator.
- **Coverage of all 100 workflows.** Localization metadata is optional. Workflows without explicit metadata fall back to a category-based default style profile. This is intentional.

## Limits

- The 100 workflows do not yet include `localization:` blocks. They inherit category-based defaults. Add per-workflow blocks if a workflow frequently produces Taiwan-targeted content.
- The glossary covers common categories but does not claim to be exhaustive. New entries can be added following the same row format.
- Regional variants (Hong Kong, Mainland, international Chinese) are documented in section 10 of the glossary and supported via user overrides recorded in the context ledger.

## How to re-run this report

```bash
bash tests/validate.sh          # regenerates workflows + indexes, then validates
python3 scripts/validate.py    # structural validation only
```
