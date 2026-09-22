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

### Changed

- `tests/_evaluations/` switched from fully gitignored to "track the harness, ignore only the recorded JSONL". Recorded model outputs may contain private / sensitive content and must not be committed.
- `tests/README.md` case-count table refreshed (15 router / 11 language / 11 workflow) and a new "Operator-driven evaluation harness" section added pointing at the harness.
- 29 high-traffic Taiwan workflows (11 content, 12 business, 6 research) gain explicit `localization:` frontmatter blocks via `LOCALIZATION_OVERRIDES` in `scripts/generate_workflows.py`. Other workflows inherit the category default documented in `templates/WORKFLOW_TEMPLATE.md`. `scripts/apply_tw_localization.py` is now a verifier that the CI runs to prevent drift between the override map and the rendered frontmatter.
- `.github/workflows/validate.yml` runs the new `apply_tw_localization.py` verifier on every push and PR.
