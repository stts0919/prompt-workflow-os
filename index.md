# prompt-workflow-os

> 100 ChatGPT Prompt Workflows.
> Describe what you want. The AI finds the right workflow, asks only what matters, and helps you complete the task.

This repository is a Markdown-first, AI-routable library of **100 prompt workflows** plus a router, playbooks, indexes, shared rules, templates, and evaluation cases.

## Get started

1. **Open this repo with any AI that can read files**, or paste the files you need.
2. **Tell the AI to read [START.md](START.md).**
3. **Describe what you want in natural language.** Examples:
   - *「I want to validate an online course idea.」*
   - *「I have a messy meeting transcript.」*
   - *「Help me understand my competitors.」*
   - *「I have code that is failing.」*
4. **The AI detects your language**, asks 1–2 high-value questions, picks the right workflow, and executes.

The user never has to memorize a workflow name.

## Three interaction modes

- **Guide me** — step-by-step discovery with confirmation before each major move.
- **Quick mode** — execute with labeled assumptions when the risk is low.
- **Recommend** — propose a workflow or workflow chain before starting.

## Five categories

| Category                                  | Count | What it covers |
| ----------------------------------------- | ----: | -------------- |
| [Content creation & communication](indexes/01-by-goal.md) | 29 | articles, posts, videos, newsletters, stories, presentations, rewriting, localization, quality review |
| [Business, marketing & customer growth](indexes/01-by-goal.md) | 24 | customers, competitors, positioning, validation, pricing, campaigns, sales, retention, strategic choices |
| [Research, analysis & decision making](indexes/01-by-goal.md) | 18 | source evaluation, summaries, fact checks, evidence, scenarios, decisions |
| [Planning, operations & self-management](indexes/01-by-goal.md) | 17 | tasks, projects, meetings, SOPs, documentation, automation, learning, self-review |
| [AI, code & data](indexes/01-by-goal.md) | 12 | prompts, agents, code, debugging, data, APIs, schemas, system design |
| **Total** | **100** | |

## Browse

- [By goal](indexes/01-by-goal.md) — when you know the outcome.
- [By problem](indexes/02-by-problem.md) — when you have a known pain.
- [By input](indexes/03-by-input.md) — when you already have material.
- [By output](indexes/04-by-output.md) — when you know the artifact you need.
- [All 100 workflows](indexes/05-all-100-workflows.md) — the complete list.

## How the router works

State flow: **DISCOVER → CLARIFY → SELECT → CONFIRM → EXECUTE → REVIEW → NEXT_STEP**

The router classifies each request by primary goal, current stage, input type, desired output, complexity, urgency, verification need, current-information need, and experience level. It keeps a compact context ledger and asks at most one or two high-value questions per turn. If sufficient context already exists, it executes immediately.

## Localization

This repo includes a [Taiwan Traditional Chinese (`zh-TW`) localization layer](shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md) with:

- a 156-entry context-sensitive term glossary,
- 15 style profiles (Threads, Instagram, LinkedIn, Email, Sales, Landing, Article, Research, Tech, SOP, Agent spec, Support, etc.),
- a two-layer quality checklist,
- 65 test cases.

Editorial rewriting improves clarity, naturalness, and tone. It does not prove human authorship, does not remove watermarks, and does not evade AI detection.

Future locale packs ([zh-CN, yue-Hant-HK, en-US, en-GB, ja-JP, ko-KR, id-ID, vi-VN](shared/locales/FUTURE_LOCALE_EXPANSION_PLAN.md)) plug into the same architecture.

## For contributors

- Read [AGENTS.md](AGENTS.md) for the authoring rules.
- Add a workflow following [templates/WORKFLOW_TEMPLATE.md](templates/WORKFLOW_TEMPLATE.md).
- Add a playbook following [templates/PLAYBOOK_TEMPLATE.md](templates/PLAYBOOK_TEMPLATE.md).
- Add an evaluation case following [templates/EVALUATION_CASE_TEMPLATE.md](templates/EVALUATION_CASE_TEMPLATE.md).
- Run `bash tests/validate.sh` before any commit.

## License

Released under the MIT License — see [LICENSE](LICENSE).
