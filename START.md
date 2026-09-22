# START — entry point

## Copy-and-paste prompt

```
Read this repository's START.md and help me with this:

[Describe what you want to achieve naturally.]
```

You can add a mode hint in the same message:

- `Guide me.` — step-by-step discovery with confirmations.
- `Quick mode.` — execute now with labeled assumptions.
- `Recommend.` — propose a workflow or workflow chain first.

## What this is

This repository is a library of 100 prompt workflows. You do not need to memorize prompts, choose IDs, or browse categories.

## What the AI does

1. Detects your language from the latest meaningful message.
2. Reads the request and classifies it by goal, stage, input type, desired output, complexity, urgency, verification need, current-information need, and experience level.
3. Maintains a compact context ledger (see [router/CONTEXT_LEDGER.md](router/CONTEXT_LEDGER.md)).
4. Asks only one or two high-value questions per turn when context is missing — never more than five before recommending a path.
5. Selects the smallest sufficient workflow or workflow chain.
6. Explains the selection in plain language when useful.
7. Executes the workflow's compact AI specification.
8. Distinguishes verified facts, user-provided facts, assumptions, inferences, and recommendations.
9. Quality-reviews the output before delivery.
10. Suggests the next useful workflow.

## Interaction contract

- **No silent assumptions.** When the AI makes a non-trivial assumption, it labels it as such.
- **No invented facts.** Sources, numbers, and citations must be real or labeled as unverified.
- **No forced interview.** Quick mode skips low-risk questions.
- **No category browsing.** The user is never asked to choose a category.
- **No tool-specific links.** The repository uses relative Markdown links only.

## Operating rules

| Rule                                  | Where defined                                  |
| ------------------------------------- | ---------------------------------------------- |
| Detect user language, reply in kind   | [shared/MULTILINGUAL_RULES.md](shared/MULTILINGUAL_RULES.md) |
| Separate fact, inference, recommendation | [shared/FACT_INFERENCE_RULES.md](shared/FACT_INFERENCE_RULES.md) |
| Output structure                      | [shared/OUTPUT_FORMATS.md](shared/OUTPUT_FORMATS.md) |
| Quality checklist                     | [shared/QUALITY_CHECKLISTS.md](shared/QUALITY_CHECKLISTS.md) |
| Source & citation rules               | [shared/SOURCE_AND_CITATION_RULES.md](shared/SOURCE_AND_CITATION_RULES.md) |
| Routing state machine                 | [router/AI_ROUTER.md](router/AI_ROUTER.md)     |
| Selection tables                      | [router/ROUTING_RULES.md](router/ROUTING_RULES.md) |
| How to ask                            | [router/CLARIFICATION_PROTOCOL.md](router/CLARIFICATION_PROTOCOL.md) |
| Context ledger                        | [router/CONTEXT_LEDGER.md](router/CONTEXT_LEDGER.md) |
| Fallback when nothing matches         | [router/FALLBACK_RULES.md](router/FALLBACK_RULES.md) |
| Taiwan Traditional Chinese localization | [shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md](shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md) |
| zh-TW term glossary                   | [shared/ZH_TW_TERM_GLOSSARY.md](shared/ZH_TW_TERM_GLOSSARY.md) |
| zh-TW style profiles                  | [shared/ZH_TW_STYLE_PROFILES.md](shared/ZH_TW_STYLE_PROFILES.md) |
| zh-TW quality checklist               | [shared/ZH_TW_QUALITY_CHECKLIST.md](shared/ZH_TW_QUALITY_CHECKLIST.md) |
| Locale architecture (future locales)  | [shared/locales/README.md](shared/locales/README.md) |

## Quick reference for AI

After reading START.md:

1. Read [router/AI_ROUTER.md](router/AI_ROUTER.md).
2. Use [indexes/05-all-100-workflows.md](indexes/05-all-100-workflows.md) as the workflow catalog.
3. Read the chosen workflow file only after selection.
4. If user attaches a playbook, read the matching file in [playbooks/](playbooks/).
5. Never claim facts you cannot verify; label all assumptions.
