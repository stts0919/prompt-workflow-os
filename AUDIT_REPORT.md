# Audit Report — prompt-workflow-os

This audit precedes the second zh-TW localization pass. The previous pass delivered a working baseline (see `ZH_TW_LOCALIZATION_VALIDATION_REPORT.md`). This audit records what already exists, what is missing for the new spec, and the recommended implementation order.

## 1. Repository tree summary

Top-level layout (after previous work):

```text
ChatGPT-100-Prompts-Workflow/
├── README.md
├── START.md
├── AGENTS.md
├── LICENSE
├── CHANGELOG.md
├── AUDIT_REPORT.md             ← this file
├── VALIDATION_REPORT.md
├── ZH_TW_LOCALIZATION_VALIDATION_REPORT.md
├── indexes/                    (6 files)
├── router/                     (5 files)
├── workflows/                 (100 files; 29+24+18+17+12)
├── playbooks/                  (5 + README)
├── shared/                     (5 base + 4 zh-TW + scripts)
│   ├── MULTILINGUAL_RULES.md
│   ├── FACT_INFERENCE_RULES.md
│   ├── OUTPUT_FORMATS.md
│   ├── QUALITY_CHECKLISTS.md
│   ├── SOURCE_AND_CITATION_RULES.md
│   ├── shared/locales/zh-TW/WRITING_RULES.md
│   ├── shared/locales/zh-TW/TERM_GLOSSARY.md
│   ├── shared/locales/zh-TW/STYLE_PROFILES.md
│   └── shared/locales/zh-TW/QUALITY_CHECKLIST.md
├── templates/                  (3 files)
├── tests/                      (README + 35 cases + 22 zh-tw localization + 22 zh-tw output quality)
└── scripts/                    (generate + validate)
```

File counts are verified by `scripts/validate.py`. The 100-workflow structure is intact.

## 2. Existing zh-TW-related files

| File                                                    | Status |
| ------------------------------------------------------- | ------ |
| `shared/locales/zh-TW/WRITING_RULES.md`        | Exists (381 lines). 7 sections + 15 before-and-after examples. Needs to grow to ≥25 examples and add `second_person_policy` / `punctuation_notes` style guidance. |
| `shared/locales/zh-TW/TERM_GLOSSARY.md`                         | Exists (236 lines). 145 entries across 10 categories. Needs to grow to ≥150 entries and add 3 categories: education / learning, finance / metrics, social media platforms. |
| `shared/locales/zh-TW/STYLE_PROFILES.md`                        | Exists (371 lines). 11 profiles. Needs to grow to ≥15 profiles (split social, add Threads / Instagram / LinkedIn / landing page / long-form / agent spec). |
| `shared/locales/zh-TW/QUALITY_CHECKLIST.md`                     | Exists (124 lines). Already has both AI-readable and human-readable layers. Tighten to match new spec exactly. |
| `tests/language-cases/zh-tw-localization-cases.md`      | Exists. 22 cases. Needs to grow to ≥30. |
| `tests/workflow-cases/zh-tw-output-quality-cases.md`     | Exists. 22 cases. Needs to grow to ≥25. |
| `ZH_TW_LOCALIZATION_VALIDATION_REPORT.md`               | Exists. Re-run after expansion. |
| `ZH_TW_IMPLEMENTATION_VALIDATION_REPORT.md`             | Missing. Will be created after expansion. |

## 3. Existing multilingual and localization files

| File                                | State                                                |
| ----------------------------------- | ---------------------------------------------------- |
| `shared/MULTILINGUAL_RULES.md`      | Updated with Chinese-variant rules (items 11–17).    |
| `shared/QUALITY_CHECKLISTS.md`      | Updated with localization section.                   |
| `router/AI_ROUTER.md`               | Updated with language / locale decision procedure.   |
| `router/ROUTING_RULES.md`           | Updated with `1.5 zh-TW localization activation`.    |
| `router/CLARIFICATION_PROTOCOL.md`  | Updated with `zh-TW clarification style`.            |
| `templates/WORKFLOW_TEMPLATE.md`    | Updated with `localization:` block. Schema needs to support `locale_style_profile_overrides` per spec. |
| `AGENTS.md`                         | Updated with zh-TW activation guidance.              |
| `README.md`                         | Updated with zh-TW localization note.                |
| `START.md`                          | Updated with zh-TW rule entry points.                |

## 4. Existing router behavior and locale logic

The router currently:

1. Detects the user's input language.
2. Detects the requested output language separately.
3. Detects a locale hint when present.
4. Defaults to `zh-TW` when Traditional Chinese is requested without locale.
5. Loads `shared/ZH_TW_*` files only when relevant.
6. Selects a style profile by category.
7. Records the choice in the context ledger.

Gaps against the new spec:

- The router should document the four required scenarios explicitly (Cases A–D).
- The router should expose `editing_intensity` per workflow and per content type.
- The router should detect "high-precision" categories (legal, financial, medical, security, compliance, data, research, citations) and force `strict_precision`.

## 5. Existing tests

| Area                | Files | Cases |
| ------------------- | ----: | ----: |
| router-cases        |    15 |    15 |
| language-cases      |    10 |    10 |
| workflow-cases      |    10 |    10 |
| zh-tw-localization  |     1 |    22 (target ≥30) |
| zh-tw-output-quality|     1 |    22 (target ≥25) |
| **Total**           |    37 |    79 |

## 6. Missing zh-TW requirements (vs new spec)

| Requirement                                   | Current | Target | Status |
| --------------------------------------------- | ------: | -----: | ------ |
| Glossary entries                              |     145 | ≥150  | -5 |
| Glossary categories                           |     10  |     13 | -3 (education / learning, finance / metrics, social media platforms) |
| Style profiles                                |     11  | ≥15   | -4 |
| Style profile schema fields                   | partial | full schema with `locale`, `second_person_policy`, `punctuation_notes` | partial |
| ZH_TW_LOCALIZATION_AND_WRITING_RULES examples |     15  | ≥25   | -10 |
| Channel tone guidance sections                |   partial | 15 channels | partial |
| Editing-intensity rules                       |   partial | explicit ruleset | partial |
| ZH-TW localization cases                      |     22  | ≥30   | -8 |
| ZH-TW workflow cases                          |     22  | ≥25   | -3 |
| Test case schema (Request, Locale, Profile, Intensity, Router behavior, Protections, Failure) | partial | full | partial |
| Shared locale architecture (`shared/locales/`) | 0 files | 5 files | -5 |
| Future locale expansion plan                  | missing | 1 file | -1 |
| `locale_style_profile_overrides` in workflow template | uses `zh_tw_style_profile` | new schema | needs update |
| `ZH_TW_IMPLEMENTATION_VALIDATION_REPORT.md`   | missing | required | -1 |

## 7. Duplicate or conflicting language rules

The validator and the file structure both treat `shared/MULTILINGUAL_RULES.md` as the canonical multilingual source. `shared/locales/zh-TW/WRITING_RULES.md` is a Taiwan-specific implementation that defers to the multilingual rules.

Conflict candidates to watch:

- `shared/MULTILINGUAL_RULES.md` says "Default to zh-TW when Traditional Chinese is unspecified." `shared/locales/zh-TW/WRITING_RULES.md` repeats the rule. This is consistent. Keep both, but ensure they don't drift.
- `shared/QUALITY_CHECKLISTS.md` lists "Localization checks"; `shared/locales/zh-TW/QUALITY_CHECKLIST.md` is more specific. Both are needed. Verify cross-link.
- `templates/WORKFLOW_TEMPLATE.md` currently has `zh_tw_style_profile`. The new spec wants `locale_style_profile_overrides.zh-TW`. The migration plan: support both keys, prefer the new one, fall back to the old one for backward compatibility.

## 8. Broken or missing relative links

`scripts/validate.py` walks every `.md` file and resolves relative links. The current run reports zero broken links. After expanding the locale architecture and re-running, all links must still resolve.

## 9. Incomplete workflow metadata

The 100 workflows use the canonical frontmatter set:

```yaml
id, slug, title, category, aliases, triggers, input_types, output_types,
requires, produces, related, playbooks, mode_support, language_support, handoff
```

Missing pieces relative to the new spec:

- Optional `localization` block: not yet present in any of the 100 files. By design — it is optional. After the new template supports `locale_style_profile_overrides`, the router will fall back to category defaults.
- `language_support.output` is `mirror-user-language` for all 100 files. This is correct: per-workflow output language is a runtime decision.

The 100-workflow structure remains intact and is not modified by this pass.

## 10. Recommended implementation order

Strict priority order from the new spec:

1. **Phase 1 — Audit.** This file.
2. **Phase 2 — zh-TW as the reference locale.**
   - 2A. Expand `shared/locales/zh-TW/WRITING_RULES.md` to ≥25 examples + channel-tone table for 15 channels + editing-intensity rules.
   - 2B. Expand `shared/locales/zh-TW/TERM_GLOSSARY.md` to ≥150 entries across 13 categories.
   - 2C. Expand `shared/locales/zh-TW/STYLE_PROFILES.md` to ≥15 profiles with the full schema (locale, second_person_policy, punctuation_notes).
   - 2D. Refresh `shared/locales/zh-TW/QUALITY_CHECKLIST.md` with both layers explicitly labeled.
   - 2E. Expand `tests/language-cases/zh-tw-localization-cases.md` to ≥30 cases with the full case schema.
   - 2F. Expand `tests/workflow-cases/zh-tw-output-quality-cases.md` to ≥25 cases.
3. **Phase 3 — Router integration.** Update `AI_ROUTER.md`, `ROUTING_RULES.md`, `CLARIFICATION_PROTOCOL.md`, `MULTILINGUAL_RULES.md`, `QUALITY_CHECKLISTS.md`, `WORKFLOW_TEMPLATE.md`, `START.md`, `AGENTS.md`, `README.md`. Cover the four Cases A–D.
4. **Phase 4 — Locale architecture.** Create `shared/locales/` with 5 documents: README, LOCALE_ROUTING_RULES, LOCALE_STYLE_PROFILE_SCHEMA, LOCALE_TERM_GLOSSARY_SCHEMA, LOCALE_QUALITY_CHECKLIST_SCHEMA.
5. **Phase 5 — Future locale expansion plan.** Create `shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md` covering zh-CN, yue-Hant-HK, en-US, en-GB, ja-JP, ko-KR, id-ID, vi-VN with the per-locale plan structure.
6. **Validation.** Update `scripts/validate.py` thresholds and produce `ZH_TW_IMPLEMENTATION_VALIDATION_REPORT.md`.

The 100-workflow structure is preserved untouched throughout.
