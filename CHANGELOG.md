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
