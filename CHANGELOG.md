# Changelog

All notable changes to this repository will be documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [1.0.0] — 2026-09-22

### Added

- Initial public release of `prompt-workflow-os`.
- Exactly 100 workflow files distributed as 29 content / 24 business / 18 research / 17 workflow / 12 technical.
- Two-layer workflow format: human-readable guide plus compact AI specification with `id`, `slug`, `category`, `aliases`, `triggers`, `input_types`, `output_types`, `requires`, `produces`, `related`, `playbooks`, `mode_support`, `language_support`.
- Router stack: `AI_ROUTER.md`, `ROUTING_RULES.md`, `CLARIFICATION_PROTOCOL.md`, `CONTEXT_LEDGER.md`, `FALLBACK_RULES.md`.
- Shared rule set: `MULTILINGUAL_RULES.md`, `FACT_INFERENCE_RULES.md`, `OUTPUT_FORMATS.md`, `QUALITY_CHECKLISTS.md`, `SOURCE_AND_CITATION_RULES.md`.
- Authoring templates: `WORKFLOW_TEMPLATE.md`, `PLAYBOOK_TEMPLATE.md`, `EVALUATION_CASE_TEMPLATE.md`.
- Six index files under `indexes/`.
- Five end-to-end playbooks under `playbooks/`.
- 35 evaluation cases under `tests/`.
- Validation script and `VALIDATION_REPORT.md`.
- MIT License.

### Changed

- Replaces earlier single-template workflow bodies with workflow-specific guidance.
- Relative Markdown links only — no tool-specific wiki syntax.

### Notes

- Repository is content-complete as of this version. Future versions will preserve backward-compatible IDs and slugs.

## [Unreleased]

### Added

- GitHub Actions CI at `.github/workflows/validate.yml` with three jobs: `validate` (runs `bash tests/validate.sh` on push / PR / manual), `pr-comment` (upserts a status comment on PRs), and `release-readiness` (flags tag-vs-HEAD drift and placeholder-author commits).
- AI evaluation harness under `tests/_evaluations/`: `harness.py` with `build-prompt` / `run-batch` / `compare` subcommands, `prompt_builder.py` (splits multi-case files on `## N.` headings), `schema.py` (`EvalResult` / `RubricScore` dataclasses), `rubric.md` (5-dimension rubric, acceptance ≥ 4.0 average and no dimension < 3), `operators/manual.md` (paste-into-UI protocol) and `operators/api.md` (SDK pattern). Recorded JSONL files stay operator-local.
- Cross-language Humanizer references in `shared/locales/research/HUMANIZER_REFERENCES.md` with timestamps and per-locale recency hints (en / zh-TW / zh-CN / ko / ru / multilingual / en-editorial). The corresponding zh-TW writing rules cite `kevintsai1202/Humanizer-zh-TW` as editorial inspiration only.
- Three new locales documented in `shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md`: zh-CN, yue-Hant-HK, en-US, en-GB, ja-JP, ko-KR, id-ID, vi-VN. zh-TW remains the reference implementation.
- `README.md` CI / release / license badges at the top, plus `CONTRIBUTING.md` covering three contribution paths (workflow / locale / router-shared-tests), CI failure modes, and the version-bump convention.

### Changed

- `tests/_evaluations/` switched from fully gitignored to "track the harness, ignore only the recorded JSONL". Recorded model outputs may contain private / sensitive content and must not be committed.
- `tests/README.md` case-count table refreshed (15 router / 11 language / 11 workflow) and a new "Operator-driven evaluation harness" section added pointing at the harness.
- 29 high-traffic Taiwan workflows (11 content, 12 business, 6 research) gain explicit `localization:` frontmatter blocks via `LOCALIZATION_OVERRIDES` in `scripts/generate_workflows.py`. Other workflows inherit the category default documented in `templates/WORKFLOW_TEMPLATE.md`. `scripts/apply_localization.py` is now a verifier that the CI runs to prevent drift between the override map and the rendered frontmatter.
- `.github/workflows/validate.yml` runs the new `apply_localization.py` verifier on every push and PR.
- **`zh-CN` locale pack** under `shared/locales/zh-CN/`: 4 content files (WRITING_RULES, TERM_GLOSSARY, STYLE_PROFILES, QUALITY_CHECKLIST) + README; ~280 glossary entries across 12 categories; 10 style profiles covering Mainland channels (公众号 / 微博 / 小红书 / 抖音 / 哔哩哔哩 / 知乎); 5 representative before-and-after examples. `shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md` marks zh-CN as **Implemented** (2026-09-22).
- Router updated: `router/AI_ROUTER.md` adds Cases E–H (zh-CN conversation + English deliverable; English conversation + zh-CN deliverable; formal zh-CN report; casual Mainland social post). `router/ROUTING_RULES.md` adds section 1.6 for `zh-CN` activation rules and style profile selection. Quality review path now branches to the zh-CN checklist when the deliverable is Simplified Chinese.
- 35 zh-CN localization cases at `tests/language-cases/zh-cn-localization-cases.md` covering Mainland terminology, channels, cross-strait disambiguation, and brand-name preservation.
- 12 more high-traffic workflows (7 workflow + 5 technical) gain `localization:` blocks using `zh-cn-friendly-professional` as the cross-compatible default — these workflows serve both zh-TW and zh-CN audiences. `LOCALIZATION_OVERRIDES` and the verifier now cover 41 workflows across all five categories.
- **`shared/MODELS_OF_RECORD.md`** documents the canonical model IDs, release dates, context windows, and pricing for the OpenAI GPT-5.6 / GPT-6 family, Anthropic Claude 5 family (Sonnet 5, Opus 5, Fable 5.1), and Google Gemini 3.8 Flash — verified 2026-09-22 against the vendors' own pages. The model IDs used in the harness (`gpt-5.6-luna` / `gpt-6-astra` / `claude-opus-5` / `claude-fable-5-1` / `gemini-3.8-flash`) now point at this file as the single source of truth.
- Corrected `gemini-flash-3.8` → `gemini-3.8-flash` (the official Google API ID order) across `tests/_evaluations/*` and `tests/README.md`. Renamed the placeholder result directory accordingly.
- Harness parser now handles both case formats: the `- **Field:** value` bullet layout used by multi-case files (e.g. `tests/language-cases/zh-tw-localization-cases.md`) and the H2-section layout used by single-case files (e.g. `tests/workflow-cases/01-*.md`, `tests/router-cases/01-*.md`). Before this fix, single-case files produced empty prompt bodies and operator runs were useless; now they carry the case's Setup / Input / Expected Output / Verification / Failure Conditions content.
- `scripts/validate.py` `check_links` now strips the fragment portion before resolving a Markdown link target, so anchor-only links no longer get falsely flagged as missing.
- Renamed `scripts/apply_tw_localization.py` → `scripts/apply_localization.py`. The verifier already covered zh-CN entries; the old name was a leftover from the Taiwan-only origin. Updated all references in CI, CONTRIBUTING.md, SPEC.md, and CHANGELOG.md.
- **`zh-TW` locale pack migrated to subdirectory.** The four content files moved from `shared/ZH_TW_*.md` to `shared/locales/zh-TW/` with shorter filenames matching the `zh-CN` convention (`WRITING_RULES.md`, `TERM_GLOSSARY.md`, `STYLE_PROFILES.md`, `QUALITY_CHECKLIST.md`); plus a new `README.md` entry point. Brings zh-TW into structural parity with `zh-CN` and resolves SPEC.md open question 1. Every reference across the repository was rewritten. `scripts/validate.py`'s `zh_tw_files` list and router reference check now point at the new subdirectory paths.
- **`zh-CN` locale pack expanded.** `shared/locales/zh-CN/WRITING_RULES.md` Section I (before-and-after examples) grew from 5 to 25 examples, covering all 10 style profiles (`friendly-professional` / `business-consulting` / `thought-leadership` / `weibo-casual` / `xiaohongshu-lifestyle` / `douyin-script` / `bilibili-script` / `email-professional` / `landing-page-clear` / `customer-support`) and all three editing intensities (`light` / `standard` / `strict_precision`).
- **Thin auto-scorer (`tests/_evaluations/auto_scorer.py`).** Three deterministic checks (`language_check`, `banned_phrase_check`, `protected_span_check`) that run without reading the model output for nuance. Writes a `<input>.auto-verdict.jsonl` next to the source JSONL; never overwrites the operator's `rubric` scores. Resolves SPEC.md open question 2.
- **Shared style profile schema** (`shared/locales/SHARED_STYLE_PROFILE_SCHEMA.md`). 8 core fields both `zh-TW` and `zh-CN` style profiles implement, plus locale-specific extension fields documented per pack. New locale packs implement the core first; locale-specific fields are optional. Resolves SPEC.md open question 4.
- **SPEC.md open question 3 resolved.** Keep `editing_intensity` per-workflow for v1.x; the router already auto-escalates to `strict_precision` for regulated content. Channel-specific overrides would expand the schema without solving a problem the maintainers have evidence for. Revisit if per-channel failures start showing up in `tests/_evaluations/results/` baselines.
- **All 4 SPEC.md open questions are now resolved.** See [`SPEC.md`](SPEC.md) § "Resolved open questions" for the full rationale.
- **Five additional locale packs** (`FUTURE_LOCALE_EXPANSION_PLAN.md` priorities 2-8):
  - `yue-Hant-HK` (Traditional Chinese — Hong Kong, with Cantonese 口語 handling)
  - `en-US` (English — United States)
  - `en-GB` (English — United Kingdom, with formal letter register)
  - `ja-JP` (Japanese, with full keigo system: sonkeigo / kenjōgo / teineigo)
  - `ko-KR` (Korean, with 합쇼체 / 해요체 / 반말체 register)
  - `id-ID` (Indonesian, with PUEBI 2015 spelling)
  - `vi-VN` (Vietnamese, with full diacritics and family-based pronouns)
- All 8 locale packs now follow the subdirectory pattern under
  `shared/locales/<code>/`. Each pack has 4 content files + README
  matching the `zh-TW` / `zh-CN` structural rigor.
- `router/ROUTING_RULES.md` adds section 1.7 (yue-Hant-HK), 1.8
  (en-US / en-GB), 1.9 (ja-JP / ko-KR / id-ID / vi-VN) covering
  activation rules and default style-profile selection per locale.
- `tests/_evaluations/prompt_builder.py` `LANGUAGE_FILES` map now
  points at all 8 locale packs. Harness loads the correct layer for
  any case whose expected_locale resolves to one of these codes.
- `tests/language-cases/locale-coverage.md` adds 18 router-level
  smoke tests covering all 8 locales (1-3 cases per locale + 3
  cross-locale cases). Full localization suites remain at
  `zh-tw-localization-cases.md` (35 cases) and
  `zh-cn-localization-cases.md` (35 cases).
- `shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md` status table
  marks all 8 locales as **Implemented** as of 2026-09-22.
