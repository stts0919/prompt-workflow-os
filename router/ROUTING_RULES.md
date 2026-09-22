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
conversation_language is zh-TW | requested_locale == Taiwan → activate zh-TW localization layer
conversation_language is zh-HK | requested_locale == Hong Kong → honor user request, do not apply zh-TW by default
conversation_language is zh-CN | requested_locale == Mainland   → honor user request, do not apply zh-TW by default; activate zh-CN layer (see 1.6)
user explicitly requests 繁體中文 / zh-TW / 台灣               → activate zh-TW regardless of input
user explicitly requests 簡體中文 / zh-CN / 大陸 / Mainland       → activate zh-CN regardless of input

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

## 1.6 zh-CN localization activation

When the conversation language is Simplified Chinese, the user explicitly
requests `zh-CN` or a Mainland-China-targeted deliverable, attach the layer
reference and choose a style profile from
[`../shared/locales/zh-CN/STYLE_PROFILES.md`](../shared/locales/zh-CN/STYLE_PROFILES.md).

```text
conversation_language is zh-CN | requested_locale == Mainland → activate zh-CN localization layer
conversation_language is zh-CN | requested_locale == Taiwan    → honor zh-CN form but ask one short clarification; default to zh-TW
conversation_language is zh-TW | requested_locale == Mainland → ask one short clarification; user likely meant zh-CN
user explicitly requests 簡體中文 / zh-CN / 大陸 / Mainland → activate zh-CN regardless of input

default_zh_cn_style_profile selection (when zh-CN layer active):
  category content  → zh-cn-friendly-professional or platform-specific profile
  category business → zh-cn-business-consulting, zh-cn-landing-page-clear, or zh-cn-email-professional
  category research → zh-cn-thought-leadership or zh-cn-business-consulting
  category workflow → zh-cn-friendly-professional
  category technical→ zh-cn-friendly-professional
  customer support or reply        → zh-cn-customer-support
  公众号 / 知乎 long-form           → zh-cn-thought-leadership
  微博 short post                  → zh-cn-weibo-casual
  小红书 lifestyle                 → zh-cn-xiaohongshu-lifestyle
  抖音 script                      → zh-cn-douyin-script
  哔哩哔哩 / B 站 script           → zh-cn-bilibili-script
  default fallback                 → zh-cn-friendly-professional

editing_intensity defaults follow the same rules as zh-TW:
  reserved code / ID / brand name spans → none
  structured technical output           → light
  default user-facing output            → standard
  legal / medical / financial / security / compliance / regulated → strict_precision
```

Conflict resolution between `zh-TW` and `zh-CN` is decided first by the user's
explicit instruction, second by the requested output language, third by the
target market, fourth by the input language. When all four conflict (rare),
the router asks one short clarification.

## 1.7 yue-Hant-HK localization activation

When the conversation language is Traditional Chinese, Cantonese vocabulary
is detected, or the user explicitly names Hong Kong / a HK city as the target
market, attach the yue-Hant-HK layer reference and choose a style profile from
[`../shared/locales/yue-Hant-HK/STYLE_PROFILES.md`](../shared/locales/yue-Hant-HK/STYLE_PROFILES.md).

```text
conversation_language is TC + Cantonese vocabulary detected        → activate yue-Hant-HK
requested_locale == Hong Kong (explicit)                            → activate yue-Hant-HK
conversation_language is TC + requested_locale unspecified          → ask one short clarification; default to zh-TW (more channels covered)
user explicitly requests 「香港」「HK」「Cantonese」「廣東話」         → activate yue-Hant-HK

default_yue_hk_style_profile selection:
  category content  → yue-hk-facebook-friendly or yue-hk-long-form-article
  category business → yue-hk-email-professional or yue-hk-business-consulting
  category research → yue-hk-business-consulting
  category workflow → yue-hk-business-consulting
  category technical→ yue-hk-business-consulting
  customer support or reply        → yue-hk-customer-support
  WhatsApp / Telegram / Signal      → yue-hk-chat-casual
  Facebook comment                  → yue-hk-facebook-casual
  Facebook post (long)              → yue-hk-facebook-friendly
  Instagram caption                 → yue-hk-instagram-casual
  LIHKG forum                       → yue-hk-lihkg-style
  LinkedIn                          → yue-hk-linkedin-professional
  legal / compliance                → yue-hk-legal-formal
  default fallback                  → yue-hk-friendly-professional
```

Cantonese 口語 (食、飲、嘅、喺、唔、搞掂、唔該) is acceptable in casual
channels (chat, Facebook comment, LIHKG) but must be excluded from formal
channels (legal, email, business consulting). The writing rules section E.3
documents which vocabulary is safe.

## 1.8 en-US and en-GB localization activation

When the user requests output in English, attach an English locale layer.
For unspecified "English" requests, default to `en-US` because most global
English training data and most users default to US conventions. Switch to
`en-GB` when the user explicitly names the UK or uses UK spellings
(`organisation`, `colour`, `behaviour`).

```text
requested_locale == English + US signal (or unspecified)            → activate en-US
requested_locale == English + UK signal                             → activate en-GB
UK spellings in user input (organisation / colour / behaviour)      → likely en-GB; ask if ambiguous
user explicitly requests "British English" / "UK English"            → activate en-GB

default_en_us_style_profile selection (en-US layer active):
  category content  → en-us-friendly-professional
  category business → en-us-email-professional or en-us-landing-page-clear
  category research → en-us-business-consulting
  category workflow → en-us-business-consulting
  category technical→ en-us-friendly-professional
  customer support or reply        → en-us-customer-support
  LinkedIn                          → en-us-linkedin-professional
  Twitter / X                       → en-us-twitter-casual
  Reddit                            → en-us-reddit-casual
  marketing email                   → en-us-email-marketing
  default fallback                  → en-us-friendly-professional

default_en_gb_style_profile selection (en-GB layer active):
  category content  → en-gb-friendly-professional
  category business → en-gb-email-professional or en-gb-formal-letter
  category research → en-gb-business-consulting
  category workflow → en-gb-business-consulting
  category technical→ en-gb-friendly-professional
  customer support or reply        → en-gb-customer-support
  LinkedIn                          → en-gb-linkedin-professional
  Twitter / X                       → en-gb-twitter-casual
  marketing email                   → en-gb-email-professional
  formal letter                     → en-gb-formal-letter
  financial / regulatory            → en-gb-finance-formal
  default fallback                  → en-gb-friendly-professional
```

For both English locales, editing_intensity follows the same rules as
zh-TW / zh-CN.

## 1.9 ja-JP, ko-KR, id-ID, vi-VN localization activation

Activate the corresponding locale pack when the user requests output in
Japanese, Korean, Indonesian, or Vietnamese (or explicitly names the target
market). When the input contains characters of the locale's script, the
router activates the layer without asking.

```text
conversation_language is ja-JP / ko-KR / id-ID / vi-VN → activate that locale's layer
requested_locale == Japan / South Korea / Indonesia / Vietnam → activate that locale's layer
locale pack's characters appear in user input           → activate that locale's layer
user explicitly requests that language                  → activate that locale's layer

editing_intensity: same rules as zh-TW / zh-CN / en-US (none / light /
standard / strict_precision; auto-escalate for regulated content).

default style profile selection (all four locales):
  general professional        → <locale>-friendly-professional
  email (formal / business)   → <locale>-email-formal
  email (casual / internal)   → <locale>-email-casual
  long-form article           → <locale>-long-form-article
  business document / proposal→ <locale>-business-document
  customer support            → <locale>-customer-support
  sales / landing             → <locale>-landing-page-clear

Locale-specific channel overrides:
  ja-JP Twitter / X            → ja-jp-twitter-casual
  ja-JP LINE                   → ja-jp-line-casual
  ja-JP note.com long-form     → ja-jp-long-form-article
  ko-KR Twitter / X            → ko-kr-twitter-casual
  ko-KR Naver blog             → ko-kr-naver-blog
  ko-KR KakaoTalk              → ko-kr-kakao-casual
  id-ID Twitter / X            → id-id-twitter-casual
  id-ID Instagram              → id-id-instagram-casual
  id-ID WhatsApp               → id-id-whatsapp-casual
  id-ID LinkedIn               → id-id-linkedin-professional
  vi-VN Zalo                   → vi-vn-zalo-casual
  vi-VN Facebook               → vi-vn-facebook-casual
  vi-VN LinkedIn               → vi-vn-linkedin-professional
  vi-VN Twitter / X            → vi-vn-twitter-casual
```

Each locale's full profile list lives in
`shared/locales/<locale>/STYLE_PROFILES.md`. The router's role is to pick
the most appropriate profile given the workflow category, channel hint,
and target market.

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
