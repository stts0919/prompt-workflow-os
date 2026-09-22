# Contributing

Thanks for helping grow `prompt-workflow-os`. This document covers the three
contribution paths and the things that will fail CI.

## Before you start

Run the validator from the repo root:

```bash
bash tests/validate.sh
```

A clean run prints `VALIDATION PASSED — 0 issues`. Anything else must be fixed
before opening a PR. CI runs the same script on every push.

## Three contribution paths

### 1. Add or change a workflow

The 100 workflows are generated from a canonical content map in
[`scripts/generate_workflows.py`](scripts/generate_workflows.py). Hand-editing
files under `workflows/` works for one-offs but they will be regenerated on the
next validator run.

- **Adding a workflow**: edit the `WORKFLOWS` dict in `generate_workflows.py`,
  pick a free `id` (001–100, currently all taken), set `category`, and provide
  the 11 field blocks (`aliases`, `triggers`, `input_types`, `output_types`,
  `requires`, `produces`, `related`, `playbooks`, `mode_support`, body sections,
  `handoff_text`). The template lives at
  [`templates/WORKFLOW_TEMPLATE.md`](templates/WORKFLOW_TEMPLATE.md).
- **Editing a workflow**: prefer editing the entry in `generate_workflows.py`
  and letting the validator regenerate the file. If you only need a typo fix,
  edit the rendered file directly and add a note in the PR description.
- **Adding a `localization:` block**: see
  [`LOCALIZATION_OVERRIDES`](scripts/generate_workflows.py) — only workflows
  in this dict get explicit `default_style_profile`, `locale_override`, and
  `editing_intensity`. `scripts/apply_localization.py` is the verifier.

### 2. Add or change a locale

`zh-TW` is the reference implementation. Future locales must match the
structure in [`shared/locales/`](shared/locales/) without weakening it. See
[`shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md`](shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md)
for what each new locale pack needs.

A new locale pack is five files plus a vocabulary / profiles / checklist:
`shared/locales/<code>/` with `README.md`,
`LOCALE_ROUTING_RULES.md`, `LOCALE_STYLE_PROFILE_SCHEMA.md`,
`LOCALE_TERM_GLOSSARY_SCHEMA.md`, and `LOCALE_QUALITY_CHECKLIST_SCHEMA.md`,
followed by the actual `shared/<CODE>_*.md` content. The reference example is
[`shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md`](shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md).

Never claim that the localization layer bypasses AI detection, removes
watermarks, or proves human authorship. Editorial rewriting improves clarity,
naturalness, and tone; it does not do those other things.

### 3. Improve the router, shared rules, or tests

- **Router**: [`router/AI_ROUTER.md`](router/AI_ROUTER.md) is the canonical
  routing surface. Cases A–D cover the four input/output language
  combinations. Changes here affect how every workflow gets selected.
- **Shared rules**: [`shared/MULTILINGUAL_RULES.md`](shared/MULTILINGUAL_RULES.md),
  [`shared/FACT_INFERENCE_RULES.md`](shared/FACT_INFERENCE_RULES.md),
  [`shared/OUTPUT_FORMATS.md`](shared/OUTPUT_FORMATS.md),
  [`shared/QUALITY_CHECKLISTS.md`](shared/QUALITY_CHECKLISTS.md),
  [`shared/SOURCE_AND_CITATION_RULES.md`](shared/SOURCE_AND_CITATION_RULES.md).
- **Evaluation cases**: use
  [`templates/EVALUATION_CASE_TEMPLATE.md`](templates/EVALUATION_CASE_TEMPLATE.md)
  and add files under `tests/router-cases/`, `tests/language-cases/`, or
  `tests/workflow-cases/`. The CI does not yet grade cases automatically; the
  harness at [`tests/_evaluations/`](tests/_evaluations/) is operator-driven.

## Things that will fail CI

- A workflow count that is not exactly 100.
- A workflow ID outside `001–100` or a duplicated ID.
- A workflow slug mismatch (`scripts/generate_workflows.py` and the
  frontmatter `slug:` must agree).
- A missing human-readable section from the required list in
  `templates/WORKFLOW_TEMPLATE.md`.
- A missing required frontmatter field.
- A broken Markdown link (the validator does not currently strip `#fragment`,
  so links to anchors must use the full path only).
- Recorded JSONL under `tests/_evaluations/results/` — those stay operator-local
  and must not be committed (`.gitignore` already covers this).

## Code style

- Python: 3.10+ syntax. Run `python3 -m py_compile scripts/*.py` before
  pushing; CI also does a syntax sanity check.
- Markdown: relative links only. No `[[wiki]]` syntax. Single H1 per file.
- English for repository metadata, instruction files, code comments. User-facing
  output mirrors the user's language.

## Releases

The repo uses [Semantic Versioning](https://semver.org/). A change that adds a
new workflow, a new shared rule, or a new locale pack is a minor bump (1.x.0).
A change that only fixes structure, typos, or links is a patch bump (1.0.x).
Maintainers cut tags from `main` after CI is green.

## Code of conduct

Be kind. Disagreements are fine; rudeness is not. The maintainers make the
final call on what lands; the goal is a useful, well-documented library that
helps real users, not a maximalist reference.