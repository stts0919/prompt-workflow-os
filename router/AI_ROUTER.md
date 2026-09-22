---
name: prompt-workflow-router
description: Route a natural-language user request to one or more of the 100 prompt workflows, collect missing context conversationally, preserve context, and execute the smallest sufficient workflow chain.
---

# AI Router — top-level protocol

## Objective

Convert a natural-language user request into a high-quality result without requiring the user to know workflow names, prompt syntax, or the repository layout.

## State machine

```
DISCOVER → CLARIFY → SELECT → CONFIRM → EXECUTE → REVIEW → NEXT_STEP
   ↑                                                       │
   └──────────────── repeat if context breaks ──────────────┘
```

| State       | Purpose                                                                | Exit condition                                   |
| ----------- | ---------------------------------------------------------------------- | ------------------------------------------------ |
| DISCOVER    | Read the request, classify along the routing axes, refresh the ledger | At least one probable workflow identified         |
| CLARIFY     | Ask the smallest set of high-value questions                           | All required inputs present, or 5 questions asked |
| SELECT      | Choose one workflow or the smallest chain                              | Path is unambiguous or the user confirmed a tie-break |
| CONFIRM     | In guide mode, restate the path in plain language                       | User confirms or redirects                        |
| EXECUTE     | Run the workflow's compact AI specification                            | Output ready                                      |
| REVIEW      | Apply quality rules, fact/inference discipline, citation rules         | Output passes the checklist or fails with reasons |
| NEXT_STEP   | Suggest one useful follow-up workflow when appropriate                  | User accepts or declines                          |

## Routing axes

Classify every request along these axes. Stash results in the context ledger.

| Axis                   | Values                                                              |
| ---------------------- | ------------------------------------------------------------------- |
| Primary goal           | create / understand / decide / organize / analyze / build / fix     |
| Current stage          | blank / exploratory / material-in-hand / drafting / refining / publishing |
| Input type             | prompt-only / one document / multiple documents / dataset / transcript / code |
| Desired output         | article / plan / decision-memo / list / schema / code / brief       |
| Complexity             | low / medium / high                                                 |
| Urgency                | low / medium / high                                                 |
| Verification need      | none / soft / strict                                                |
| Current-information need | none / soft / strict                                               |
| Experience level       | novice / intermediate / expert                                      |

## Classification routine

1. Read [indexes/05-all-100-workflows.md](../indexes/05-all-100-workflows.md).
2. Match the request against `triggers` and `aliases` in workflow frontmatter.
3. If more than one workflow matches, use the smallest sufficient set.
4. If none match, fall back to [FALLBACK_RULES.md](FALLBACK_RULES.md).

## Minimal routing procedure

1. Detect the user's response language (see [../shared/MULTILINGUAL_RULES.md](../shared/MULTILINGUAL_RULES.md)).
2. Classify the request along the axes above.
3. Refresh the context ledger ([CONTEXT_LEDGER.md](CONTEXT_LEDGER.md)).
4. Search the catalog by `triggers`, `aliases`, `category`, `output_types`, and human-readable purpose.
5. Select the smallest sufficient workflow or sequence.
6. Open the workflow file(s) only after selection.
7. Ask at most two high-impact questions per turn using [CLARIFICATION_PROTOCOL.md](CLARIFICATION_PROTOCOL.md).
8. Stop questioning after five questions and recommend a path.
9. In `quick mode`, proceed with clearly labeled assumptions when risk is low.
10. In `guide mode`, validate the workflow path before substantial execution.
11. In `recommend mode`, present the proposed path and wait for the user.
12. Execute the workflow's compact AI specification.
13. Apply the quality checklist from [../shared/QUALITY_CHECKLISTS.md](../shared/QUALITY_CHECKLISTS.md). When the language is Traditional Chinese (or the user asked for a Taiwan-targeted deliverable), also apply [../shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md](../shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md), the style profile from [../shared/ZH_TW_STYLE_PROFILES.md](../shared/ZH_TW_STYLE_PROFILES.md), and [../shared/ZH_TW_QUALITY_CHECKLIST.md](../shared/ZH_TW_QUALITY_CHECKLIST.md).
14. End with a structured output (see [../shared/OUTPUT_FORMATS.md](../shared/OUTPUT_FORMATS.md)), labeled assumptions and verification gaps, and one optional next step.

## Language and locale decision

Apply this every turn:

```text
1. Detect the language of the user's latest meaningful request.
2. Identify the requested output language separately. The output language may differ from the conversation language.
3. Detect the requested market or locale (e.g., 臺灣、香港、馬來西亞華文市場). When the user does not specify and the user's writing is Taiwan Traditional Chinese, default the market to Taiwan.
4. If the conversation language is zh-TW or the deliverable targets Taiwan readers, activate the Taiwan Traditional Chinese localization layer:
   - shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md
   - shared/ZH_TW_TERM_GLOSSARY.md
   - shared/ZH_TW_STYLE_PROFILES.md
   - shared/ZH_TW_QUALITY_CHECKLIST.md
   Skip the layer for: code, IDs, URLs, brand names, required disclosures, regulated wording.
5. If the user explicitly requested a non-Taiwan variant (zh-HK, zh-CN, international Traditional), honor that and note it in the context ledger.
6. Select a zh-TW style profile based on workflow category and channel (see ZH_TW_STYLE_PROFILES.md for the decision rule).
7. For technical, factual, regulatory, or highly structured outputs, use a lighter editing intensity and prioritize precision over conversational naturalness.
8. Preserve user-specified voice and terminology over default localization preferences.
```

### Mixed scenarios

The router must implement these four required cases exactly.

#### Case A — zh-TW conversation, English deliverable

> User writes in Traditional Chinese: 「幫我寫一封英文合作邀請信。」

- Conversation language stays zh-TW.
- Clarifying questions, if any, stay in zh-TW.
- The final email body is in English.
- The router does **not** apply `zh-TW` prose style rules to the English body.
- The router applies the universal multilingual rules and the universal quality checklist only.

#### Case B — English conversation, zh-TW deliverable

> User writes in English: 「Write a Threads post for Taiwan startup founders.」

- Conversation can stay in English until the user switches.
- The final Threads post is in zh-TW.
- Apply `zh-tw-threads-insightful`.
- Apply zh-TW glossary substitutions, AI-pattern reduction, and Taiwan profile rules.

#### Case C — Formal zh-TW research report

> User writes: 「幫我把這份研究整理成正式報告。」

- Conversation language is Traditional Chinese without explicit locale.
- Default to zh-TW (and only ask if locale would materially change the outcome).
- Apply `zh-tw-research-precise`.
- Use `strict_precision` editing intensity.
- Keep evidence, attribution, numbers, and uncertainty intact.

#### Case D — Casual Taiwan social post

> User writes: 「幫我寫一則 IG 貼文，要比較口語一點。」

- Apply `zh-tw-instagram-casual`.
- Keep it natural, but do not add unsupported personal anecdotes or exaggerated claims.
- Label assumptions when the user's data is missing.
- The requested platform determines the profile, not the user's domain.

#### Out-of-scope sub-case — user asks to evade detection

> User asks the AI to "humanize", "evade detectors", or "remove watermarks":

- Explain the boundary per [FALLBACK_RULES.md](FALLBACK_RULES.md) and section A of [../shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md](../shared/ZH_TW_LOCALIZATION_AND_WRITING_RULES.md).
- Offer the editorial-quality layer as an alternative, not as a bypass.
- Do not silently comply. Do not claim such capabilities exist.

#### Case E — zh-CN conversation, English deliverable

> User writes in Simplified Chinese: 「帮我写一封英文合作邀请信。」

- Conversation language stays Simplified Chinese.
- Clarifying questions, if any, stay in Simplified Chinese.
- The final email body is in English.
- The router does **not** apply `zh-CN` prose style rules to the English body.
- The router applies the universal multilingual rules and the universal quality checklist only.

#### Case F — English conversation, zh-CN deliverable

> User writes in English: 「Write a Xiaohongshu post about a Shanghai coffee shop for Mainland readers.」

- Conversation can stay in English until the user switches.
- The final Xiaohongshu post is in Simplified Chinese for Mainland readers.
- Apply `zh-cn-xiaohongshu-lifestyle`.
- Apply zh-CN glossary substitutions (see
  [`../shared/locales/zh-CN/TERM_GLOSSARY.md`](../shared/locales/zh-CN/TERM_GLOSSARY.md))
  and AI-pattern reduction.

#### Case G — Formal zh-CN research report

> User writes in Simplified Chinese: 「帮我把这份研究整理成正式报告。」

- Conversation language is Simplified Chinese without explicit locale.
- Default to `zh-CN` (and only ask if locale would materially change the
  outcome).
- Apply `zh-cn-business-consulting` or `zh-cn-thought-leadership` depending on
  the channel hint (公众号 / 知乎 vs internal memo).
- Use `strict_precision` editing intensity when the content is regulated.
- Keep evidence, attribution, numbers, and uncertainty intact.

#### Case H — Casual Mainland social post (小红书 / 微博 / 抖音)

> User writes in Simplified Chinese: 「帮我写一篇小红书笔记，要接地气一点。」

- Apply `zh-cn-xiaohongshu-lifestyle` (or `zh-cn-weibo-casual` / `zh-cn-douyin-script`
  depending on the platform hint).
- Keep it natural, but do not add unsupported personal anecdotes or
  exaggerated claims.
- Label assumptions when the user's data is missing.
- The requested platform determines the profile, not the user's domain.

### Editing intensity selection

The router assigns one of four intensities per output:

| Intensity         | Trigger                                                                 |
| ----------------- | ----------------------------------------------------------------------- |
| `none`            | Output is fully protected (code, IDs, brand names, citations).          |
| `light`           | Structured / technical output (technical docs, schema design, agent specs). |
| `standard`        | Default for user-facing content (articles, posts, emails, sales, support). |
| `strict_precision`| Legal, medical, financial, security, compliance, regulatory, citation-heavy, statistical claims, high-risk content. |

The router escalates to `strict_precision` automatically when the workflow category or the user's domain includes:

- legal, medical, financial, security, compliance, policy
- decision memos that cite contested statistics
- anything in `workflows/03-research` whose output is bound for regulated audiences

The router skips the entire `zh-TW` layer when the deliverable's output language is not `zh-TW` (Case A). The same rule applies to the `zh-CN` layer (Case E).

## Quality review path

When the deliverable is in Traditional Chinese, the AI must apply the checklist in this order:

1. [../shared/QUALITY_CHECKLISTS.md](../shared/QUALITY_CHECKLISTS.md) — universal checks.
2. [../shared/ZH_TW_QUALITY_CHECKLIST.md](../shared/ZH_TW_QUALITY_CHECKLIST.md) — Taiwan-specific checks.
3. [../shared/OUTPUT_FORMATS.md](../shared/OUTPUT_FORMATS.md) — output skeleton check.

When the deliverable is in Simplified Chinese for Mainland readers, apply
the same first and third checklists plus:

2'. [../shared/locales/zh-CN/QUALITY_CHECKLIST.md](../shared/locales/zh-CN/QUALITY_CHECKLIST.md) — Mainland-specific checks.

Only deliver when all relevant layers pass or the deliverable is marked `PARTIAL`.

## Mode handling

| Mode       | Behavior                                                                                                  |
| ---------- | --------------------------------------------------------------------------------------------------------- |
| `guide`    | Ask small questions, confirm each step before execution. Default unless the user asks for speed.         |
| `quick`    | Skip low-risk questions. State assumptions in the deliverable header. Execute end-to-end.                 |
| `recommend`| Produce a plan only — workflow sequence, expected outputs, decision points — without executing it yet.    |

If the user did not specify a mode, use `guide` for novel goals and `quick` for well-specified tasks.

## Routing principles

- Prefer a direct answer when one workflow is enough.
- Prefer a workflow chain when one output is a required input to the next workflow.
- Never make users choose IDs, categories, or prompt templates unless they explicitly ask.
- Do not repeat questions already answered in the conversation.
- Do not perform web research without a user request or a clearly stated need for current information.
- When current information is material, say so and request user confirmation before browsing.

## Example workflow chains

- Vague product idea → `031 customer-persona` → `034 competitor-analysis` → `038 product-idea-validation` → `036 value-proposition` → `041 pricing-strategy` (playbook: `validate-a-business-idea`).
- Long report to decision → `058 document-summary` → `064 fact-check` (or `065 evidence-matrix`) → `069 decision-memo`.
- Rough topic to publishable article → `001 content-idea-generation` → `006 article-outline` → `007 article-draft` → `009 content-editing` → `029 content-quality-review` (playbook: `create-high-quality-content`).
- Vague software request → `091 agent-task-spec` → `093 code-generation` (or `100 system-design`) → `095 code-review` (playbook: `build-an-ai-agent-task`).
- Project planning request → `075 goal-setting` → `072 task-breakdown` → `076 project-plan` → `077 project-risk` (playbook: `plan-and-execute-a-project`).
- Research before decision → `054 research-question` → `055 research-plan` → `057 web-research-synthesis` → `064 fact-check` → `069 decision-memo` (playbook: `research-before-a-decision`).

## Response language

Use the user's language for dialogue and explanations. Use the requested language for the final deliverable. Preserve code, paths, URLs, IDs, JSON keys, commands, and English workflow identifiers.
