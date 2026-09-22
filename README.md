# 100 ChatGPT Prompt Workflows

[![CI](https://github.com/stts0919/prompt-workflow-os/actions/workflows/validate.yml/badge.svg)](https://github.com/stts0919/prompt-workflow-os/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/tag/stts0919/prompt-workflow-os?label=release&sort=semver)](https://github.com/stts0919/prompt-workflow-os/releases)
[![License](https://img.shields.io/github/license/stts0919/prompt-workflow-os)](LICENSE)

> You do not need to memorize prompts, browse categories, or copy templates.
> Share this repository with an AI, describe what you want, and the AI selects the right workflow for you.

## What this repository is

This is a Markdown-first library of **100 reusable prompt workflows** across five categories:

| #  | Category            | Coverage                                                                          |
| -- | ------------------- | --------------------------------------------------------------------------------- |
| 01 | Content             | articles, posts, videos, newsletters, stories, presentations, rewriting, localization, quality review |
| 02 | Business            | customers, competitors, positioning, validation, pricing, campaigns, sales, retention, strategic choices |
| 03 | Research            | source evaluation, summaries, fact checks, evidence, scenarios, decisions          |
| 04 | Workflow            | tasks, projects, meetings, SOPs, documentation, automation, learning, self-review |
| 05 | Technical           | prompts, agents, code, debugging, data, APIs, schemas, system design              |

It is **not** a list of disconnected prompts. It is a connected system with:

- a **router** that detects your goal, language, and stage, then selects the smallest sufficient workflow chain,
- **100 workflow cards** that pair a human-readable guide with a compact AI specification,
- **playbooks** that connect multiple workflows into end-to-end outcomes,
- **shared rules** for language, fact-handling, output formats, quality checklists, and citations,
- a **Taiwan Traditional Chinese (`zh-TW`) localization layer** (the reference implementation) that improves clarity, naturalness, and tone for Taiwan readers without claiming human authorship, watermark removal, or AI-detection evasion,
- a **locale architecture** in [shared/locales/README.md](shared/locales/README.md) that documents how future locale packs (zh-CN, yue-Hant-HK, en-US, en-GB, ja-JP, ko-KR, id-ID, vi-VN) will plug in without weakening the `zh-TW` reference implementation.

## How to use it

Share this repo with any AI that can read files, then say:

```
Read this repository's START.md and help me with this:
[describe your goal naturally]
```

The AI should detect your language, ask only the most useful questions, pick the right workflow, and execute.

### Three interaction modes

You can append a mode hint at any time:

- `Guide me.` — step-by-step discovery, with confirmation before each major move.
- `Quick mode.` — execute with reasonable stated assumptions when the risk is low.
- `Recommend.` — propose a workflow or workflow chain before starting.

You do not need to know workflow IDs or category names. The router chooses for you.

## How the router works

State flow: **DISCOVER → CLARIFY → SELECT → CONFIRM → EXECUTE → REVIEW → NEXT_STEP**

The router classifies each request by primary goal, current stage, input type, desired output, complexity, urgency, verification need, current-information need, and experience level. It keeps a compact context ledger and asks at most one or two high-value questions per turn. If sufficient context already exists, it executes immediately.

Full router specification:

- [router/AI_ROUTER.md](router/AI_ROUTER.md) — top-level protocol
- [router/ROUTING_RULES.md](router/ROUTING_RULES.md) — selection tables
- [router/CLARIFICATION_PROTOCOL.md](router/CLARIFICATION_PROTOCOL.md) — how to ask
- [router/CONTEXT_LEDGER.md](router/CONTEXT_LEDGER.md) — running context schema
- [router/FALLBACK_RULES.md](router/FALLBACK_RULES.md) — handling unknowns

## Repository layout

```
prompt-workflow-os/
├── README.md                 ← this file
├── START.md                  ← copy-paste entry point
├── AGENTS.md                 ← authoring & behavior rules for AI and humans
├── LICENSE
├── CHANGELOG.md
│
├── indexes/
│   ├── 00-start-here.md
│   ├── 01-by-goal.md
│   ├── 02-by-problem.md
│   ├── 03-by-input.md
│   ├── 04-by-output.md
│   └── 05-all-100-workflows.md
│
├── router/                   ← how the AI selects workflows
├── workflows/                ← the 100 workflow cards
├── playbooks/                ← connected workflow sequences
├── shared/                   ← reusable rules and schemas
├── templates/                ← authoring templates
└── tests/                    ← router / language / workflow cases
```

## Two layers in every workflow

Each workflow file contains:

1. **Human-readable guide** — what it is, why use it, when to use it (and when not to), what to prepare, how the AI helps, what you will receive, related workflows, and recommended next steps.
2. **Compact AI specification** — YAML frontmatter and a short instruction block. AI models read this layer for low-token, deterministic execution.

You can read either layer. AI execution prefers the second layer for token efficiency.

## Known limitations

- Not every AI product auto-loads a linked GitHub repository. Some products require you to paste the file contents manually or use a connected workspace.
- Models have token limits. For very large inputs, consider splitting the request or attaching summaries.
- This repository does not include live web search or proprietary data. When current information matters, the AI will tell you verification is needed.
- The system is intentionally framework-free: no servers, no databases, no plugins to install.
- The Taiwan Traditional Chinese layer is an editorial quality layer. It does not prove human authorship, remove watermarks, or evade AI detection. See [shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md](shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md).

## Contributing or extending

Read [AGENTS.md](AGENTS.md) for the authoring rules. Each new workflow must:

- have a unique 3-digit ID (`001`–`100`),
- follow [templates/WORKFLOW_TEMPLATE.md](templates/WORKFLOW_TEMPLATE.md),
- produce a discoverable entry in [indexes/05-all-100-workflows.md](indexes/05-all-100-workflows.md).

To propose a new playbook, follow [templates/PLAYBOOK_TEMPLATE.md](templates/PLAYBOOK_TEMPLATE.md). To add evaluation cases, use [templates/EVALUATION_CASE_TEMPLATE.md](templates/EVALUATION_CASE_TEMPLATE.md).

## Language behavior

Internal specifications are in English. The AI must detect your language and reply in it unless you request another output language. Code, URLs, file paths, IDs, JSON keys, and commands are preserved unchanged.

When the conversation is in Traditional Chinese (or the deliverable targets readers in Taiwan), the AI applies the [Taiwan Traditional Chinese localization rules](shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md), the [zh-TW term glossary](shared/ZH_TW_TERM_GLOSSARY.md), a [style profile](shared/ZH_TW_STYLE_PROFILES.md) chosen by content type, and the [zh-TW quality checklist](shared/ZH_TW_QUALITY_CHECKLIST.md). Editorial rewriting improves clarity and naturalness; it does not promise human authorship, does not remove watermarks, and does not evade AI detectors.

For Hong Kong, Mainland, or international Chinese variants, the user can override the default by stating their preferred locale in the request.

## License

Released under the MIT License — see [LICENSE](LICENSE).
