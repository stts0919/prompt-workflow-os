# Agent instructions — prompt-workflow-os

This file is for AI models and human contributors working on this repository.

## Purpose

Maintain a human-readable and AI-routable library of 100 prompt workflows plus a router, playbooks, indexes, shared rules, templates, and evaluation cases.

## Authoring rules

1. Every workflow lives in exactly one Markdown file under `workflows/`.
2. Use English kebab-case file names and stable 3-digit numeric IDs (`001`–`100`).
3. Category folder names use the leading zero prefix (`01-content`, `02-business`, …). Canonical frontmatter `category:` is unprefixed (`content`, `business`, `research`, `workflow`, `technical`).
4. Every workflow contains both a human-readable guide and a compact AI specification.
5. Never use tool-specific wiki link syntax (`[[ ]]`). Always use relative Markdown links.
6. Update [indexes/05-all-100-workflows.md](indexes/05-all-100-workflows.md) when adding, renaming, or removing a workflow.
7. Preserve backward-compatible IDs and slugs whenever possible.
8. Workflows must be distinct: do not duplicate a workflow under a different name. When you add a new workflow, define the boundary against the closest existing one.

## Workflow structure (required)

Each workflow file must contain both layers below.

### Layer 1 — Human-readable guide

Sections in this order:

1. `# NNN — Title` heading
2. `## What is this?`
3. `## Why use it?`
4. `## When should I use it?`
5. `## When should I not use it?`
6. `## What should I prepare?`
7. `## How does the AI help me?`
8. `## What will I get?`
9. `## How to start`
10. `## Related workflows`
11. `## Recommended next steps`

Write concretely. Give at least one named example situation and a sketched output.

### Optional localization metadata

Workflows that frequently produce user-facing Traditional Chinese content can include:

```yaml
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile:
  zh_tw_style_profile:
  zh_tw_editing_intensity:
```

See `templates/WORKFLOW_TEMPLATE.md` for the full schema and selection guidance. Localization metadata is optional; absence triggers a category-based default.

### Layer 2 — Compact AI specification

YAML frontmatter must include all of:

```yaml
id: "NNN"
slug: "kebab-case-slug"
title: "Human Title"
category: "content" | "business" | "research" | "workflow" | "technical"
aliases: []
triggers: []
input_types: []
output_types: []
requires: []
produces: []
related: []
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
handoff: []
```

Plus a `text` instruction block with the keys: `purpose`, `required_inputs`, `optional_inputs`, `ask_if_missing`, `do_not_use_when`, `workflow`, `output_contract`, `quality_rules`, `handoff`.

## Quality rules

1. Do not claim current facts without sources or verification.
2. Separate facts, assumptions, and recommendations when relevant.
3. Ask only for information that materially affects output quality.
4. Include an explicit output contract per workflow.
5. Define a clear next-step recommendation per workflow.
6. Never invent sources, statistics, or user context.
7. Never bundle more than two clarifying questions in a single turn.

## Language rules

Internal instructions remain English. User-facing output mirrors the user's language by default. Never translate code, URLs, file paths, IDs, JSON keys, or commands unless explicitly asked.

When the conversation language is Traditional Chinese or the deliverable targets readers in Taiwan, the AI must load the Taiwan Traditional Chinese localization layer:

- `shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md`
- `shared/ZH_TW_TERM_GLOSSARY.md`
- `shared/ZH_TW_STYLE_PROFILES.md`
- `shared/ZH_TW_QUALITY_CHECKLIST.md`

Editorial rewriting improves clarity, naturalness, and tone. It does not prove human authorship, does not remove watermarks, and does not evade AI detection. If the user asks for those outcomes, follow `router/FALLBACK_RULES.md` and explain the boundary plainly.

For non-zh-TW Chinese variants (Hong Kong, Mainland, international), the user may override. The override is recorded in the context ledger. Future locale packs (zh-CN, yue-Hant-HK, en-US, en-GB, ja-JP, ko-KR, id-ID, vi-VN) plug into the same architecture described in `shared/locales/`.

## Frontmatter conventions

- `slug` matches the filename minus the leading `NNN-` prefix.
- `category` is one of: `content`, `business`, `research`, `workflow`, `technical`.
- `triggers` are short phrases the router will match against a user request.
- `requires` lists required inputs in human terms.
- `produces` lists outputs in human terms.
- `related` lists workflow slugs that share handoff data.
- `playbooks` lists playbook slugs that include this workflow.
- `mode_support` enumerates which of `guide | quick | recommend` apply.
- `language_support.input` is `auto-detect`. `language_support.output` is `mirror-user-language` unless constrained.
- `handoff` lists the keys that flow downstream to `related` workflows.

## Validation

Before any release:

1. Run `tests/validate.sh`.
2. Confirm `VALIDATION_REPORT.md` shows zero failures.
3. Confirm every workflow appears in `indexes/05-all-100-workflows.md`.
4. Confirm every cross-link uses relative Markdown syntax and resolves.
