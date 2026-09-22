# Changelog

All notable changes to this repository will be documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned

- First operator-driven smoke eval round using the `tests/_evaluations/`
  harness against `gpt-5.6-luna`, `claude-opus-5`, and `gemini-3.8-flash`.
- GitHub Release for `v1.2.0` once a smoke-round result set is committed.
- SPEC.md deferred item: per-channel `editing_intensity` overrides,
  revisited only after per-channel failure evidence exists.

## [1.2.0] — 2026-09-22

The "all 8 locales live" release.

### Added

- **Five additional locale packs** beyond `zh-TW` / `zh-CN`:
  - `yue-Hant-HK` (Traditional Chinese — Hong Kong, with Cantonese 口語
    handling and LIHKG forum-style profile)
  - `en-US` (English — United States)
  - `en-GB` (English — United Kingdom, with formal letter register)
  - `ja-JP` (Japanese, with full keigo system: sonkeigo / kenjōgo /
    teineigo)
  - `ko-KR` (Korean, with 합쇼체 / 해요체 / 반말체 register)
  - `id-ID` (Indonesian, with PUEBI 2015 spelling)
  - `vi-VN` (Vietnamese, with full diacritics and family-based pronouns)
- All 8 locale packs now follow the subdirectory pattern under
  `shared/locales/<code>/`. Each pack has 4 content files + README matching
  the `zh-TW` / `zh-CN` structural rigor.
- `tests/language-cases/locale-coverage.md` adds 18 router-level smoke tests
  covering all 8 locales (1–3 cases per locale + 3 cross-locale cases).
  Full localization suites remain at `zh-tw-localization-cases.md`
  (35 cases) and `zh-cn-localization-cases.md` (35 cases).
- `shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md` status table marks all
  8 locales as **Implemented** as of 2026-09-22.

### Changed

- `router/ROUTING_RULES.md` adds section 1.7 (`yue-Hant-HK`), 1.8
  (`en-US` / `en-GB`), and 1.9 (`ja-JP` / `ko-KR` / `id-ID` / `vi-VN`)
  covering activation rules and default style-profile selection per locale.
- `tests/_evaluations/prompt_builder.py` `LANGUAGE_FILES` map now points at
  all 8 locale packs. The harness loads the correct layer for any case whose
  `expected_locale` resolves to one of these codes.
- `README.md` language section lists all 8 locale packs and points readers
  at the shared schema, routing rules, and expansion plan.

## [1.1.0] — 2026-09-22

The "structure + zh-CN + evidence-base" release.

### Added

- **`zh-CN` locale pack** under `shared/locales/zh-CN/`: 4 content files
  (WRITING_RULES, TERM_GLOSSARY, STYLE_PROFILES, QUALITY_CHECKLIST) +
  README; ~280 glossary entries across 12 categories; 10 style profiles
  covering Mainland channels (公众号 / 微博 / 小红书 / 抖音 / 哔哩哔哩 /
  知乎). 25 before-and-after examples covering all 10 style profiles and
  all 3 editing intensities (`light` / `standard` / `strict_precision`).
- **`shared/MODELS_OF_RECORD.md`** documents canonical model IDs, release
  dates, context windows, and pricing for OpenAI GPT-5.6 / GPT-6 family,
  Anthropic Claude 5 family (Sonnet 5, Opus 5, Fable 5.1), and Google
  Gemini 3.8 Flash — verified 2026-09-22.
- **`SPEC.md`** — design rationale with 6 non-goals, 6 design principles,
  architecture diagram, 4 contracts, versioning rules, and a "what we
  don't measure" section.
- **`CONTRIBUTING.md`** — three contribution paths (workflow / locale /
  router-shared-tests), CI failure modes, versioning convention.
- **Thin auto-scorer** at `tests/_evaluations/auto_scorer.py`. Three
  deterministic checks (`language_check`, `banned_phrase_check`,
  `protected_span_check`) that never overwrite operator's `rubric` scores.
- **Shared style profile schema** at
  `shared/locales/SHARED_STYLE_PROFILE_SCHEMA.md`. 8 core fields both
  `zh-TW` and `zh-CN` style profiles implement, plus locale-specific
  extension fields documented per pack.
- 35 zh-CN localization cases at
  `tests/language-cases/zh-cn-localization-cases.md` covering Mainland
  terminology, channels, cross-strait disambiguation, and brand-name
  preservation.
- 12 more high-traffic workflows (7 workflow + 5 technical) gain
  `localization:` blocks using `zh-cn-friendly-professional` as the
  cross-compatible default. `LOCALIZATION_OVERRIDES` and the verifier now
  cover **41 workflows** across all five categories.

### Changed

- **All 4 SPEC.md open questions are now resolved.** See [`SPEC.md`](SPEC.md)
  § "Resolved open questions" for the full rationale.
- `router/AI_ROUTER.md` adds Cases E–H (zh-CN conversation + English
  deliverable; English conversation + zh-CN deliverable; formal zh-CN
  report; casual Mainland social post).
- `router/ROUTING_RULES.md` adds section 1.6 for `zh-CN` activation rules
  and style profile selection. Quality review path now branches to the
  zh-CN checklist when the deliverable is Simplified Chinese.
- `scripts/validate.py` `check_links` now strips the fragment portion
  before resolving a Markdown link target, so anchor-only links no longer
  get falsely flagged as missing.
- Renamed `scripts/apply_tw_localization.py` → `scripts/apply_localization.py`.
  The verifier already covered zh-CN entries; the old name was a leftover
  from the Taiwan-only origin.
- **zh-TW locale pack migrated to subdirectory.** The four content files
  moved from `shared/ZH_TW_*.md` to `shared/locales/zh-TW/` with shorter
  filenames matching the `zh-CN` convention; plus a new `README.md` entry
  point. Brings zh-TW into structural parity with `zh-CN`.

### Fixed

- Harness parser now handles both case formats: the `- **Field:** value`
  bullet layout used by multi-case files and the H2-section layout used
  by single-case files. Before this fix, single-case files produced empty
  prompt bodies; now they carry Setup / Input / Expected Output /
  Verification / Failure Conditions content.
- Corrected `gemini-flash-3.8` → `gemini-3.8-flash` (the official Google
  API ID order) across `tests/_evaluations/*` and `tests/README.md`.

## [1.0.1] — 2026-09-22

The "CI + harness + Humanizer + first localization blocks" hotfix.

### Added

- **GitHub Actions CI** at `.github/workflows/validate.yml` with three
  jobs: `validate` (runs `bash tests/validate.sh` on push / PR / manual),
  `pr-comment` (upserts a status comment on PRs), and `release-readiness`
  (flags tag-vs-HEAD drift and placeholder-author commits).
- **AI evaluation harness** under `tests/_evaluations/`: `harness.py` with
  `build-prompt` / `run-batch` / `compare` subcommands, `prompt_builder.py`,
  `schema.py` (`EvalResult` / `RubricScore` dataclasses), `rubric.md`
  (5-dimension rubric, acceptance ≥ 4.0 average and no dimension < 3),
  `operators/manual.md` (paste-into-UI protocol), `operators/api.md`
  (SDK pattern). Recorded JSONL files stay operator-local.
- **Cross-language Humanizer references** in
  `shared/locales/research/HUMANIZER_REFERENCES.md` with timestamps and
  per-locale recency hints (en / zh-TW / zh-CN / ko / ru / multilingual /
  en-editorial). The corresponding zh-TW writing rules cite
  `kevintsai1202/Humanizer-zh-TW` as editorial inspiration only — not for
  AI-detection bypass.
- 29 high-traffic Taiwan workflows (11 content, 12 business, 6 research)
  gain explicit `localization:` frontmatter blocks via `LOCALIZATION_OVERRIDES`
  in `scripts/generate_workflows.py`. Other workflows inherit the category
  default documented in `templates/WORKFLOW_TEMPLATE.md`.
- `README.md` CI / release / license badges at the top, plus
  `CONTRIBUTING.md` covering three contribution paths.

### Changed

- `tests/_evaluations/` switched from fully gitignored to "track the
  harness, ignore only the recorded JSONL". Recorded model outputs may
  contain private / sensitive content and must not be committed.
- `tests/README.md` case-count table refreshed and a new "Operator-driven
  evaluation harness" section added.

## [1.0.0] — 2026-09-22

### Added

- Initial public release of `prompt-workflow-os`.
- Exactly 100 workflow files distributed as 29 content / 24 business /
  18 research / 17 workflow / 12 technical.
- Two-layer workflow format: human-readable guide plus compact AI
  specification with `id`, `slug`, `category`, `aliases`, `triggers`,
  `input_types`, `output_types`, `requires`, `produces`, `related`,
  `playbooks`, `mode_support`, `language_support`.
- Router stack: `AI_ROUTER.md`, `ROUTING_RULES.md`, `CLARIFICATION_PROTOCOL.md`,
  `CONTEXT_LEDGER.md`, `FALLBACK_RULES.md`.
- Shared rule set: `MULTILINGUAL_RULES.md`, `FACT_INFERENCE_RULES.md`,
  `OUTPUT_FORMATS.md`, `QUALITY_CHECKLISTS.md`, `SOURCE_AND_CITATION_RULES.md`.
- Authoring templates: `WORKFLOW_TEMPLATE.md`, `PLAYBOOK_TEMPLATE.md`,
  `EVALUATION_CASE_TEMPLATE.md`.
- Six index files under `indexes/`.
- Five end-to-end playbooks under `playbooks/`.
- 35 evaluation cases under `tests/`.
- Validation script and `VALIDATION_REPORT.md`.
- MIT License.

### Notes

- Repository is content-complete as of this version. Future versions will
  preserve backward-compatible IDs and slugs.
