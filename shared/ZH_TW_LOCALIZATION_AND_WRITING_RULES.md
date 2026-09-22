---
id: zh-tw-localization-rules
title: "Taiwan Traditional Chinese Localization and Writing Rules"
applies_when:
  - user writes primarily in Traditional Chinese used in Taiwan
  - user requests zh-TW, Taiwan Traditional Chinese, Taiwanese wording
  - deliverable targets readers in Taiwan
  - traditional Chinese is requested without naming another locale
out_of_scope:
  - watermarking, provenance, AI detection, authorship claims
companion_files:
  - ZH_TW_TERM_GLOSSARY.md
  - ZH_TW_STYLE_PROFILES.md
  - ZH_TW_QUALITY_CHECKLIST.md
version: 2.0.0
---

# Taiwan Traditional Chinese Localization and Writing Rules

This document is the integration point for the Taiwan Traditional Chinese (`zh-TW`) localization layer in `prompt-workflow-os`. The `zh-TW` implementation is the reference implementation; future locale packs must satisfy this file's structure even if their content differs.

## A. Purpose and scope

The layer exists for one reason: when a user writes in Traditional Chinese — or asks for an output that will be read in Taiwan — the AI should reply and write in language that is natural, clear, context-appropriate, and free of mechanical translation patterns.

What this layer **does**:

- Improves clarity, naturalness, cultural fit, and editorial quality.
- Selects regionally preferred terminology from [ZH_TW_TERM_GLOSSARY.md](ZH_TW_TERM_GLOSSARY.md).
- Adapts tone and structure to workflow type, audience, and channel via [ZH_TW_STYLE_PROFILES.md](ZH_TW_STYLE_PROFILES.md).
- Reduces generic AI writing patterns and unsupported hype.
- Runs a structured review against [ZH_TW_QUALITY_CHECKLIST.md](ZH_TW_QUALITY_CHECKLIST.md) before delivery.

What this layer **does not do**:

- It does not prove human authorship.
- It does not remove or verify watermarks, provenance, or AI detection signals.
- It is not positioned as a way to evade AI detectors, bypass content provenance, or fabricate identity.

If the user asks for the above outcomes, follow [../router/FALLBACK_RULES.md](../router/FALLBACK_RULES.md) and explain the boundary plainly. Do not silently comply. Do not claim such capabilities exist after editing.

## B. Automatic activation rules

Activate this rule set when **any** of the following is true:

1. The user's latest meaningful request is primarily in Traditional Chinese used in Taiwan.
2. The user explicitly requests `zh-TW`, Taiwan Traditional Chinese, Taiwanese wording, or Traditional Chinese for Taiwan.
3. The requested deliverable targets readers in Taiwan (e.g., a Taiwanese marketing email, a Taiwan customer-support reply, a Taipei product launch announcement).
4. The user asks for `繁體中文` without naming another locale, unless context indicates Hong Kong or another region.

When Traditional Chinese is requested without a locale, **default to `zh-TW`** and only ask a clarification question if the locale would materially change the deliverable.

Activate a **lighter editing intensity** when the output is:

- Research reports and decision memos.
- Business strategy and consulting deliverables.
- SOPs, technical specifications, or documentation.
- Data analysis or schema designs.

Activate **`strict_precision`** when the output is:

- Legal, medical, financial, security, compliance, or policy content.
- Anything that cites statistics, regulatory text, or third-party studies as decision-critical evidence.
- Code, configuration, or any output where exact preservation matters.

For both lighter and strict outputs, prioritize precision and explicit uncertainty over conversational naturalness.

## C. Input language vs output language vs target market

Three distinct signals must be detected each turn:

| Signal         | Example                                                |
| -------------- | ------------------------------------------------------ |
| Input language | The user wrote in Traditional Chinese.                 |
| Output language | The user asked for the deliverable in English.        |
| Target market  | The user asked for "a Taiwanese product launch post". |

Apply `zh-TW` prose style only when the output language (or target market) is `zh-TW`. Do not apply `zh-TW` rules to an English email body even when the user wrote the conversation in Traditional Chinese.

If the user did not specify the output language and the deliverable's natural language matches the input language, treat them as the same. If unclear, ask one short clarification.

## D. Protected content rules

Never rewrite by default:

- Code (programming languages, configuration files).
- Commands (shell, CLI, deployment).
- API names and HTTP method names.
- URLs.
- File paths.
- IDs (workflow IDs like `031 customer-persona`, JSON keys, schema field names).
- Tables that contain factual data.
- Dates, numbers, units, and currencies.
- Direct quotes.
- Citations and bibliographic references.
- Legal disclaimers and required disclosures.
- Product names and brand names.
- User-provided terminology.
- Workflow identifiers and slugs.

If prose surrounds protected content, only the prose is rewritten. Examples:

- `031 customer-persona` is preserved even when the surrounding paragraph is translated.
- A `curl https://api.example.com/v1/jobs ...` line stays verbatim.
- A quote like `"我們不賣希望，我們賣時間"` stays verbatim inside a paragraph that is otherwise revised.

## E. Taiwan language guidance

Substitutions are **context-sensitive**. The glossary in [ZH_TW_TERM_GLOSSARY.md](ZH_TW_TERM_GLOSSARY.md) documents preferred forms and acceptable alternatives.

Illustrative subset:

| Concept | Preferred zh-TW | Common Mainland form |
| --- | --- | --- |
| information | 資訊 | 信息 |
| video | 影片 | 視頻 |
| software | 軟體 | 軟件 |
| folder | 資料夾 | 文件夾 |
| account | 帳號 | 賬號 |
| account (formal product) | 帳戶 | 賬戶 |
| user (formal) | 使用者 | 用戶 |
| quality | 品質 | 質量 |
| interface | 介面 | 界面 |
| network | 網路 | 網絡 |
| print (verb) | 列印 | 打印 |
| save (file) | 儲存 | 保存 |
| login (verb) | 登入 | 登錄 |
| register (verb) | 註冊 | 注冊 |
| message | 訊息 | 消息 |
| reply (verb) | 回覆 | 回复 |
| marketing | 行銷 | 營銷 |
| optimization | 最佳化 | 優化 |
| optimization (alt.) | 改善 / 調整 / 改進 | 優化 |

Substitutions are **not** forced when:

- The user provides their own terminology.
- Industry vocabulary differs (e.g., 數位 in education marketing is fine; 數位化 in B2B SaaS is also acceptable).
- Direct quotes must remain unchanged.
- The destination is Hong Kong, Mainland, or international Chinese (use the requested variant).
- A brand name or required disclosure dictates spelling.

When uncertain, ask one short clarification. When the user prefers a specific form, record it in the context ledger and use it consistently.

## F. Channel-specific tone rules

Each row links to the dedicated style profile. The router chooses the profile based on workflow category, audience, and channel.

| # | Channel                          | Profile                                  | Tone             | Directness | Casualness | Evidence |
| - | -------------------------------- | ---------------------------------------- | ---------------- | ---------- | ---------- | -------- |
| 1 | Conversational AI assistance     | `zh-tw-conversational-help`              | Friendly plain   | Medium     | Medium     | Light    |
| 2 | Friendly professional            | `zh-tw-friendly-professional`            | Warm professional| Medium-high| Low-medium | Medium   |
| 3 | Business consulting              | `zh-tw-business-consulting`              | Analytical       | High       | Low        | High     |
| 4 | Threads post (insightful)        | `zh-tw-threads-insightful`               | Considered sharp | High       | Medium     | Medium   |
| 5 | Instagram caption                | `zh-tw-instagram-casual`                 | Casual vivid     | Medium-low | High       | Light    |
| 6 | LinkedIn post                    | `zh-tw-linkedin-professional`            | Considered sharp | High       | Low-medium | Medium   |
| 7 | B2B email                        | `zh-tw-email-professional`               | Respectful brief | High       | Low        | High     |
| 8 | Sales copy                       | `zh-tw-sales-clear`                      | Confident plain  | High       | Low        | Medium   |
| 9 | Landing page                     | `zh-tw-landing-page-clear`               | Outcome-led      | High       | Low        | Medium   |
| 10 | Long-form article              | `zh-tw-long-form-article`                | Considered       | Medium-high| Low-medium | Medium   |
| 11 | Research summary / report        | `zh-tw-research-precise`                 | Formal           | High       | Low        | Strict   |
| 12 | Technical docs                  | `zh-tw-technical-clear`                  | Technical terse  | Very high  | Low        | Strict   |
| 13 | SOP / runbook                   | `zh-tw-sop-direct`                       | Procedural       | Very high  | Low        | Strict   |
| 14 | AI agent task specification      | `zh-tw-agent-spec-precise`               | Specification    | Very high  | Low        | Strict   |
| 15 | Customer support reply           | `zh-tw-customer-support`                 | Warm solution    | High       | Medium     | High     |

Per-profile detail (tone, formality, sentence rhythm, first-person policy, rhetorical-question policy, evidence standard, common phrases to avoid, preferred patterns, ending style) is in [ZH_TW_STYLE_PROFILES.md](ZH_TW_STYLE_PROFILES.md).

## G. AI-pattern reduction rules

Editorial rules, not detector-evasion rules. The goal is competent-human-editor voice.

Patterns to reduce or remove:

1. **Empty era framing.** 「在這個資訊爆炸的時代」carries no information. Cut unless context genuinely requires it.
2. **Generic opening claims.** 「在現今的 X 領域中…」as the lead-in. Replace with the concrete situation.
3. **Generic importance framing.** 「這非常重要。」Show why, or remove.
4. **Unsupported hype.** Adjectives without evidence — 「徹底改變」,「完美解決」,「顛覆性」. Replace with concrete specifics.
5. **Forced contrast.** 「不只是 X，更是 Y.」Use only when contrast is the point.
6. **Repeated three-item lists.** Triadic lists are fine when meaningful; chains of three for the sake of three are not. Vary the structure.
7. **Excessive connectives.** 「此外」,「另外」,「更進一步地」,「值得注意的是」 at the start of every paragraph. Use when needed; drop when not.
8. **Excessive rhetorical questions.** A single setup question can be useful; a paragraph of them is not.
9. **Uniform sentence rhythm.** When every sentence has the same length, structure, and clause weight, rewrite for variety.
10. **Corporate abstraction.** 「賦能」,「生態系」,「全方位」 outside a specific operational meaning.
11. **Generic slogan-like endings.** 「讓 X 變得更好」 as a closer. End with the next concrete action or specific takeaway.
12. **Excessive "you can".** Avoid showing a capability every other sentence.
13. **Excessive "not only … but also".** Once per piece, at most.
14. **Repeated "the key is / 重點在於".** Use only when naming a specific key.
15. **Overexplaining obvious steps.** If the user is competent, skip the basics. If unsure, ask.
16. **Repeating the user's question before answering.** Get to the point.
17. **Fake personal anecdotes.** Never invent 「我曾經…」,「我的經驗是…」,「很多客戶都告訴我…」. Fabricated lived experience is forbidden.
18. **Fake social proof.** No invented 「已有 3,000 位用戶」unless the user supplied the number.
19. **Turning uncertainty into certainty.** If the AI is uncertain, label it (假設 / 推論 / 估計 / 待驗證). Do not launder into a confident claim.
20. **Pure enumerations without judgment.** When listing options, also pick a default or trade-off.
21. **Mirror symmetry.** 「無論是 A 還是 B，都需要…」overuse. Vary sentence openings.
22. **Form-letter apologies.** 「非常感謝您的耐心」,「我們深感抱歉」 without naming the actual problem and action.

Limits:

- Do not make writing artificially casual. Match the workflow's register.
- Do not strip useful structure from reports, SOPs, or instructional materials.
- Do not remove technical content in service of style.

## H. Editing intensity rules

The router selects an intensity per output:

| Intensity         | When to use | What it means |
| ----------------- | ----------- | -------------- |
| `none`            | Output is fully protected (code, IDs, brand names, citations). | Apply no prose edits. |
| `light`           | Technical docs, factual reports, schema design, structured business analysis, agent specs. | Only fix clear AI tells (uniform rhythm, opening filler). Preserve structure and content. |
| `standard`        | User-facing content: articles, posts, emails, sales pages, customer support. | Apply glossary, AI-pattern reduction, profile rules, ending-style guidance. |
| `strict_precision`| Legal, medical, financial, security, compliance, regulatory, citation-heavy, statistical claims, high-risk content. | Prioritize precision and explicit uncertainty. Apply minimal stylistic edits. Mark every claim with `[fact]` / `[inference]` / `[assumption]` / `[recommendation]`. |

The router escalates to `strict_precision` automatically for these workflow categories:

- Legal, medical, financial, security, compliance, policy.
- Decision memos that cite contested statistics.
- Anything in `workflows/03-research` whose output is bound for regulated audiences.

## I. Before-and-after examples (≥25)

Each example pairs a weaker AI-leaning version with a revised Taiwan-friendly version. The "why" focuses on the specific editorial move.

### Example 1 — Router follow-up question

**Before:** 「請問您能否提供更多細節以便我更好地為您服務？」

**After:** 「我需要先確認一件事：這份報告是要給董事會看，還是給業務團隊內部用？因為兩種的篇幅和語氣會差很多。」

**Why:** Asks for the high-impact decision (audience) instead of generic "more detail". Names why the answer changes the output.

### Example 2 — Workflow explanation

**Before:** 「這個強大的工作流程將會帶領您進入一個全新的世界，徹底改變您處理任務的方式。」

**After:** 「這個流程用三步把一份長文件變成決策摘要：先用 `058 文件摘要` 壓成結構化摘要，再用 `064 事實查核` 標記需要驗證的句子，最後用 `069 決策備忘錄` 整理出選項、利弊與建議。」

**Why:** Names the steps, what each does, and the skip rule. No adjectives carrying no information. Workflow IDs preserved in English.

### Example 3 — Business analysis

**Before:** 「這是一個充滿機會的市場。我們的公司擁有顛覆性的技術和全方位的解決方案，能夠徹底改變客戶體驗。」

**After:** 「這個市場 2023 年的規模約為 12 億美元，年增 8%，主要成長來自三個區隔：中小企業的 SaaS 採購、零售 POS 整合、教育端的學習平台。我們目前的方案覆蓋前兩個區隔，第三個尚未進入。」

**Why:** Replaces hype with one verifiable number and three concrete segments. Defines what the company covers and where it does not. Lets the reader judge.

### Example 4 — Consulting recommendation

**Before:** 「根據我的深入分析，我強烈建議貴公司應該立即採取行動。」

**After:** 「根據你提供的三個假設情境，我的建議是先把 A 路線跑 30 天，理由有兩點：(1) 投入成本只有 B 路線的 35%；(2) 你能從這 30 天拿到可比較的真實數據，用來決定是否升級到 B。如果 30 天後指標不達標，再討論是否完全放棄。」

**Why:** Names the data input, the criteria, and the alternative. Provides a verifiable next step and a fallback rule.

### Example 5 — Threads post (insightful)

**Before:** 「在這個資訊爆炸的時代，我們都渴望找到方向。」

**After:** 「重新整理待辦清單時，把「今天要做什麼」分成「今天可以完成什麼」兩份。貼一份在螢幕前，一份留給自己。第一份通常長 5 倍，第二份才是會真的消失的。」

**Why:** Opens with a concrete method. Ends with a candid observation. No motivational padding.

### Example 6 — Instagram caption

**Before:** 「✨ 大家好～今天來分享超棒的小技巧！讓生活變得更美好！💕」

**After:** 「本週最划算的一次消費：一雙 1,200 元的雨鞋，把我從『濕襪子悲劇』裡救出來三次。如果你也常被午後雷陣雨突襲，這筆帳很划算。」

**Why:** Drops decorative emoji and motivational language. Names the specific observation, the price, and the trigger condition. Reads like a person.

### Example 7 — LinkedIn post

**Before:** 「今天我想分享一個重要的觀點，這對我們行業來說具有深遠的意義。」

**After:** 「大家都以為新創的瓶頸是找到客戶，其實是建立『拒絕』的流程。沒有清楚的拒絕話術，sales 會把每位 lead 都當成機會；等真有人來買時，流程已經分不清楚誰是誰。如果你只接過五個客戶，現在還不需要拒絕話術。超過 50 個，就不能不寫。」

**Why:** Opens with the contrarian observation. Closes with the concrete threshold (5 vs 50 customers). No padding.

### Example 8 — Email (B2B)

**Before:** 「您好，我是來自 XX 公司的小明。在這個充滿機會的時代，希望與您共創美好未來。」

**After:** 「陳經理您好，我是 XX 公司的張怡安。看到你們最近導入了新一版的內部知識庫，想了解一下目前最頭痛的環節是哪一塊。我手上有一個針對內部搜尋準確率的做法，週四下午三點半小時方便嗎？」

**Why:** Brief, names a concrete observation about the recipient, states a specific offer and time slot.

### Example 9 — Sales copy

**Before:** 「我們的革命性產品將徹底改變您的工作方式。透過 AI 賦能的智慧引擎，享受無與倫比的效率提升。」

**After:** 「每月花 6 小時整理客戶回信？我們的做法把這段時間壓到 1.5 小時，且整段流程仍由你的客服主管覆核。下面 12 分鐘的示範走過一遍真實案例，看完再決定要不要約試用。」

**Why:** Replaces abstractions with the time spent, the time saved, the verification path, the demo length, and the explicit next step.

### Example 10 — Landing page

**Before:** 「我們提供全方位的解決方案，能夠幫助企業在數位時代取得成功。」

**After:** 「把客服信件從每週 6 小時壓到 1.5 小時，整段流程由你的客服主管覆核，不需要改你既有的信件平台。三分鐘示範會走過一封真實投訴信的處理過程，下面可以看更多客戶的真實使用前後比較。」

**Why:** Replaces 「全方位」 with three concrete dimensions (time, oversight, no-platform-change). Adds demo length, link to evidence, and trust signal.

### Example 11 — Product description

**Before:** 「我們的產品是一款顛覆性的創新解決方案，採用最先進的 AI 技術，提供無與倫比的使用者體驗。」

**After:** 「這個 App 把客戶來信自動分成『問題』、『退款』、『合作』三類，每封都會附上建議的回覆方向。分類模型只在你的歷史信件上訓練，不會拿去餵其他客戶。」

**Why:** Describes what the product does. Ends with one trust signal (data isolation).

### Example 12 — Research finding

**Before:** 「研究證實，我們的方法可以顯著提升用戶體驗。這是一個重大的突破，具有深遠的意義。」

**After:** 「在 47 位受測者中，使用新版介面的那一組完成核心任務的中位時間由 4.2 分鐘降到 2.6 分鐘（小樣本，未達統計顯著，建議再做一輪 200 人測試）。錯誤率由 18% 降到 9%。」

**Why:** Names sample size, effect, and the verification gap. Avoids marketing tone.

### Example 13 — Report conclusion

**Before:** 「總結來說，本研究取得了重要的成果，具有重要的參考價值。」

**After:** 「本研究在三家會計事務所的導入結果顯示，每週信件處理時間由 5.8 小時降到 1.6 小時（n=12）。在兩個小型補習班導入時，效益不顯著（小於 5%），可能因為這類用戶的信件樣本較少。建議擴大樣本後再驗證。」

**Why:** Replaces generic 「重要」with concrete effect size, sample, and a structural caveat. Names what the next verification should test.

### Example 14 — Project plan

**Before:** 「我們精心打造了一個全方位的專案計畫，旨在賦能團隊在各個層面實現突破。」

**After:** 「這個 6 週的目標是把『通知中心』從被動推播改成可訂閱。週 1 完成內容模型；週 2 完成遷移腳本；週 3-4 上線 beta；週 5 收集數據；週 6 決定要不要擴大。每個階段結束前要交付一段錄影 demo。」

**Why:** Names the actual scope, the weekly deliverables, and what each phase produces.

### Example 15 — Meeting summary

**Before:** 「本次會議大家討論得非常深入，並取得了多項共識。」

**After:** 「會議結論：下週一前由 Amy 把 CRM 欄位從 22 個縮到 8 個；週三 review；上線日改成 9 月 17 日；行銷確認不再 push 9 月初那段早鳥價。開放問題：客服是否要同步接手新的『退訂』按鈕？要等 Evan 週四回覆後再決定。」

**Why:** Replaces vague 「深入」「共識」 with named decisions, owners, deadlines, and one open question.

### Example 16 — Customer support reply

**Before:** 「非常感謝您的寶貴意見，我們會虛心接受並努力改進。」

**After:** 「收到了，這次寄出的版本確實少了附件，我再寄一次給你。附件就是上一封信裡提到的對照表。如果你打開還是空白請再回信，我直接請倉庫重寄。」

**Why:** Acknowledges the actual failure, names the action, offers a fallback.

### Example 17 — Community announcement

**Before:** 「我們非常高興地宣布，將為大家帶來全新的體驗，讓每一位用戶都能感受到我們的用心。」

**After:** 「提醒：9 月 3 日（一）凌晨 1:00-3:00 系統維護，期間 API、儀表板、webhook 都會暫停。9 月 2 日下午六點之後下載的報表，請在維護完成後重新整理。」

**Why:** Replaces announcement-with-no-info with maintenance window, what's affected, and a concrete action for users.

### Example 18 — SOP instruction

**Before:** 「首先，讓我們一起深入了解這個強大的功能。這個步驟非常關鍵。」

**After:** 「1. 開啟『自動回覆』分頁。2. 將『啟用時段』設定為 09:00-18:00。3. 選擇『客服類』→『付款問題』範本。4. 預覽後送出。例外：若客服主管要求夜間啟用，需填寫『加班核准單』後重複步驟 2。品質檢查：每日 18:00 系統自動產生當日啟用報表。」

**Why:** Imperative, numbered, with an exception path and a quality check at the end.

### Example 19 — Technical explanation

**Before:** 「OAuth 是一個非常強大且革命性的授權框架，能夠讓開發者輕鬆整合第三方登入。」

**After:** 「OAuth 2.0 的 authorization code flow 有四個角色：resource owner（使用者）、client（你的應用）、authorization server、resource server。重點是 client **永遠拿不到**使用者的密碼，它只拿到一個短期的 access token，並用這個 token 去 resource server 換資料。」

**Why:** Removes marketing tone. Lists the four roles. Highlights the security-critical fact (client never sees the password).

### Example 20 — AI agent task specification

**Before:** 「請打造一個超強的 AI agent，能夠自動化所有任務。」

**After:** 「目標：寫一個 Python 腳本，給定一段 `support_emails.json`（包含 `id`、`subject`、`body`、`received_at`），輸出 `classifications.json`（每封信加上 `category` ∈ {billing, bug, feature, other} 與 `confidence` ∈ [0, 1]）。Acceptance：所有信件都有分類，confidence 平均 ≥ 0.7，且類別分布不要全部都落在 billing。Non-goals：不串接實際信件 API；不做多語分類；不處理附件。」

**Why:** Names objective, inputs, outputs, acceptance criteria, and non-goals. No vague 「超強」「自動化所有」.

### Example 21 — Headline rewrite

**Before:** 「顛覆時代來臨：AI 將徹底改變你的工作」

**After:** 「這 12 個判斷，幫你決定要不要把客服信件外包給 AI」

**Why:** Replaces vague 「顛覆時代」 with a specific scope (12 judgments) and a concrete decision the reader can make.

### Example 22 — CTA rewrite

**Before:** 「立即行動，立即購買，立即改變！」

**After:** 「先看 12 分鐘的示範影片；看完再決定要不要約 30 分鐘試用。」

**Why:** Replaces three identical imperatives with a low-friction first step and a concrete follow-up.

### Example 23 — FAQ answer

**Before:** 「Q: 你們的方案安全嗎？A: 當然！我們採用最先進的加密技術，提供全方位的安全保障。」

**After:** 「Q: 資料你們怎麼存放？A: 存在 AWS 東京區（ap-northeast-1），不上雲以外的環境，也不會拿去訓練自家或其他客戶的模型。合約條款可以看這份：\<link\>。」

**Why:** Replaces reassurance with one verifiable fact and a pointer to the contract.

### Example 24 — Newsletter lede

**Before:** 「在這個充滿不確定性的時代，這一期的內容將會為您帶來全新的視角。」

**After:** 「這個月我們調整了三件事：客服信分類的判定欄位從 5 個減到 3 個，理由、與踩到的坑都在第一段。中段是一個客戶的真實回饋，最後是這週讀了什麼。」

**Why:** Names what changed and what each section does. Lets the reader decide whether to read.

### Example 25 — Press release / announcement

**Before:** 「我們極其榮幸地宣布，將隆重推出劃時代的全新產品系列。」

**After:** 「公告：9 月 17 日上線新版的『可訂閱通知中心』。Beta 期間目前有 47 家中小企業在試用。對外功能：(1) 使用者可選訂閱主題；(2) 預設為關閉、不強推；(3) API 端可直接調整訂閱狀態。對開發者：可下載 mock data 提前整合。」

**Why:** Replaces ceremonial language with date, scope, current usage, three concrete capabilities, and a developer hook.

### Example 26 — Threads follow-up

**Before:** 「感謝大家的支持，我們會繼續努力！」

**After:** 「昨天那則 Threads 收到 12 則留言，意外的是其中 4 則都是會計師事務所的 PM 提出來的。下次我想單獨做一則給 B2B 服務業 PM 的內容。如果你也是，留言跟我說你最煩的工作流程是哪一段。」

**Why:** Replaces gratitude with concrete signal from yesterday's post. Asks one specific question that primes the next post.

### Example 27 — Newsletter closing

**Before:** 「感謝您的閱讀，讓我們一起攜手共創美好未來！」

**After:** 「下週四寄出下一期，會整理這次信件分類的 8 個客戶回饋摘要。如果你不想再收到，可以直接點這裡取消訂閱。」

**Why:** Names the next send, gives a preview, and provides a clear opt-out.

## J. Router integration rules

When activating this layer, the router must:

1. Detect the user's input language.
2. Detect the requested output language separately.
3. Detect the requested target market or locale separately.
4. Default unspecified Traditional Chinese to `zh-TW`.
5. Load this file plus glossary, profiles, and quality checklist only when relevant.
6. Select a profile based on workflow category, channel, audience, formality, and evidence sensitivity.
7. Choose editing intensity (`none` / `light` / `standard` / `strict_precision`).
8. Apply glossary substitutions only to non-protected prose.
9. Skip the layer entirely when the deliverable's output language is not `zh-TW`.
10. Record the activation decision and chosen profile in the context ledger.

## K. Safety boundaries

- The layer never claims to bypass AI detection, remove watermarks, or prove human authorship.
- The layer never invents personal anecdotes, customer testimonials, or regionally specific statistics.
- The layer refuses to comply silently when the user asks for the above outcomes; it explains the boundary per [../router/FALLBACK_RULES.md](../router/FALLBACK_RULES.md).

## L. Reference files

- [ZH_TW_TERM_GLOSSARY.md](ZH_TW_TERM_GLOSSARY.md)
- [ZH_TW_STYLE_PROFILES.md](ZH_TW_STYLE_PROFILES.md)
- [ZH_TW_QUALITY_CHECKLIST.md](ZH_TW_QUALITY_CHECKLIST.md)
- [../tests/language-cases/zh-tw-localization-cases.md](../tests/language-cases/zh-tw-localization-cases.md)
- [../tests/workflow-cases/zh-tw-output-quality-cases.md](../tests/workflow-cases/zh-tw-output-quality-cases.md)
- [../shared/locales/README.md](../shared/locales/README.md) — locale architecture reference.
- [../shared/locales/research/HUMANIZER_REFERENCES.md](../shared/locales/research/HUMANIZER_REFERENCES.md) — cross-language editorial reference list.

## M. Citations

The `zh-TW` layer uses [`kevintsai1202/Humanizer-zh-TW`](https://github.com/kevintsai1202/Humanizer-zh-TW) as editorial inspiration only. We do **not** cite it for any detector-evasion or watermark-removal capability. The full cross-language editorial reference list — including the language-by-language first-look references and the explicit exclusion list for anti-detection bypass tools — is at [../shared/locales/research/HUMANIZER_REFERENCES.md](../shared/locales/research/HUMANIZER_REFERENCES.md).
