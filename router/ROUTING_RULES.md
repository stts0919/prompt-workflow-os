# Routing Rules

Selection tables that the AI router applies after classification.

## 1. Goal classification

| Goal verb (user)                                         | Workflow slug                                                                 | Category       |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- |
| "I need content ideas / blog topics / video ideas"       | `content-idea-generation` (001)                                                | content        |
| "Help me write an article / post"                        | `article-draft` (007) and `article-outline` (006)                              | content        |
| "Rewrite / shorten / improve my draft"                   | `article-rewrite` (008) and `content-editing` (009)                            | content        |
| "Summarize this document / paper / chapter"              | `document-summary` (058) or `content-summary` (010)                           | research/content |
| "Translate this content"                                 | `translation-localization` (027)                                               | content        |
| "Repurpose this into LinkedIn / Twitter / email / carousel" | `content-repurposing` (028)                                                 | content        |
| "Create a podcast / presentation"                        | `podcast-interview` (018) or `presentation-story` (019)                        | content        |
| "I want to understand my competitors"                    | `competitor-analysis` (034)                                                   | business       |
| "I want to validate an online course / product"          | `product-idea-validation` (038) and `customer-persona` (031)                  | business       |
| "Define my target customer / ICP"                        | `customer-persona` (031)                                                      | business       |
| "Improve my pricing"                                     | `pricing-strategy` (041)                                                      | business       |
| "Write a sales page / landing page"                      | `sales-page` (043)                                                            | business       |
| "Build an email sequence"                                | `email-sequence` (046)                                                        | business       |
| "Plan a campaign / product launch"                       | `campaign-plan` (045)                                                         | business       |
| "Decide between A and B"                                 | `business-decision` (052) or `decision-memo` (069)                             | business/research |
| "Help me understand this research"                       | `web-research-synthesis` (057) or `research-plan` (055)                       | research       |
| "Fact check this"                                        | `fact-check` (064)                                                            | research       |
| "Turn this into a brief"                                 | `executive-brief` (070)                                                       | research       |
| "Help me plan my week / tasks"                           | `weekly-plan` (074) or `task-breakdown` (072)                                  | workflow       |
| "Build a SOP / checklist"                                | `sop-builder` (080) or `checklist-builder` (081)                               | workflow       |
| "I have failing code"                                    | `debugging` (094)                                                             | technical      |
| "Explain this code"                                      | `code-explanation` (092)                                                      | technical      |
| "Review my code"                                         | `code-review` (095)                                                           | technical      |
| "Design a system / API / schema"                         | `system-design` (100), `api-integration` (099), `schema-design` (098)         | technical      |
| "Design a better prompt"                                 | `prompt-designer` (089) or `prompt-improvement` (090)                         | technical      |
| "Build an AI agent task"                                 | `agent-task-spec` (091)                                                       | technical      |

If multiple matches apply, prefer the longest playbook chain only when the user signals a complete end-to-end goal. Otherwise pick the single smallest workflow.

## 1.5 zh-TW localization activation

When the conversation language is Traditional Chinese, the user explicitly requests `zh-TW` or a Taiwan-targeted deliverable, attach the layer reference and choose a style profile.

```text
conversation_language is zh-TW | requested_locale == Taiwan → activate localization layer
conversation_language is zh-HK | requested_locale == Hong Kong → honor user request, do not apply zh-TW by default
conversation_language is zh-CN | requested_locale == Mainland   → honor user request, do not apply zh-TW by default

default_zh_style_profile selection (when localization active):
  category content  → zh-tw-friendly-professional or platform-specific profile
  category business  → zh-tw-business-consulting, zh-tw-sales-clear, or zh-tw-landing-page-clear
  category research  → zh-tw-research-precise or zh-tw-technical-clear
  category workflow  → zh-tw-sop-direct
  category technical → zh-tw-agent-spec-precise or zh-tw-technical-clear
  customer support or reply        → zh-tw-customer-support
  Threads posts                    → zh-tw-threads-insightful
  Instagram captions               → zh-tw-instagram-casual
  LinkedIn posts                   → zh-tw-linkedin-professional
  long-form articles               → zh-tw-long-form-article
  default fallback                 → zh-tw-conversational-help

editing_intensity default per output type:
  reserved code / ID / brand name spans → none
  structured technical output           → light
  default user-facing output             → standard
  legal / medical / financial / security / compliance / regulated   → strict_precision
```

## 2. Input type routing

| Input type                  | Default first action                                              |
| --------------------------- | ----------------------------------------------------------------- |
| prompt only                 | Ask 1–2 clarifying questions per [CLARIFICATION_PROTOCOL.md](CLARIFICATION_PROTOCOL.md) |
| one short document          | Read in full, then map to a single workflow                       |
| one long document / report  | `document-summary` first, then a downstream workflow              |
| multiple documents          | `classification` (061), then fan-out per bucket                   |
| transcript                  | `meeting-summary` (059) or `podcast-interview` (018)              |
| dataset / CSV / JSON        | `data-exploration` (096), then `data-analysis` (097)               |
| code snippet                | `code-explanation` (092), then `code-review` (095) / `debugging` (094) |
| codebase                    | `system-design` (100) for architecture map, or `code-review` for spot checks |
| vague goal statement        | `customer-persona` (031) / `research-question` (054)              |

## 3. Output type routing

| Desired output             | Default workflow(s)                                              |
| -------------------------- | ---------------------------------------------------------------- |
| publishable article        | `article-outline` (006) → `article-draft` (007) → `content-editing` (009) → `content-quality-review` (029) |
| short-form post            | `social-post` (012)                                              |
| short video                | `video-hook` (016) → `short-video-script` (015)                  |
| carousel / slides          | `carousel` (014)                                                 |
| newsletter                 | `newsletter` (011)                                               |
| presentation               | `presentation-story` (019) → `video-storyboard` (017)             |
| decision memo              | `decision-memo` (069)                                            |
| executive brief            | `executive-brief` (070)                                          |
| sales page                 | `sales-page` (043)                                               |
| email sequence             | `email-sequence` (046)                                           |
| weekly plan                | `weekly-plan` (074)                                              |
| project plan               | `project-plan` (076)                                             |
| SOP                        | `sop-builder` (080)                                              |
| schema                     | `schema-design` (098)                                            |
| system / architecture map  | `system-design` (100)                                            |
| agent task spec            | `agent-task-spec` (091)                                          |

## 4. Stage routing

| Stage              | Lean toward                                                 |
| ------------------ | ------------------------------------------------------------ |
| exploratory        | research / planning workflows                                |
| material in hand   | summary / analysis workflows                                 |
| drafting           | creation / outline workflows                                 |
| refining           | editing / rewriting / translation / quality review            |
| publishing         | repurposing / distribution / channel-specific creation        |

## 5. Conflict rules

- `quick mode` and missing required input → ask one round of clarifications then proceed with labeled assumptions.
- `recommend mode` and ambiguous goal → return a ranked candidate list and stop.
- Strict verification need + no source list → state that external verification is required before drawing conclusions.
- Conflicting playbooks → prefer the playbook that minimizes total workflow count and ends with the user's stated deliverable.
- Multiple candidate workflows inside one playbook → run them in declared order; allow skipping on user confirmation.

## 6. Skip heuristics

- If the user already produced an artifact matching the desired output, skip the planning workflow and only refine.
- If the input is one short document under ~3,000 words, skip `document-summary` and proceed directly to the consuming workflow.
- If the deliverable is a brief one-paragraph answer, skip all multi-step chains.
