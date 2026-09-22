# Localization Cases — zh-TW (≥30)

These cases exercise the Taiwan Traditional Chinese localization layer at the language level. Each case uses the standard schema:

- **User request**
- **Requested output language**
- **Target market**
- **Expected locale**
- **Expected style profile**
- **Expected editing intensity**
- **Expected router behavior**
- **Protected content**
- **Failure conditions**

User-facing behavior should match [../../shared/locales/zh-TW/WRITING_RULES.md](../../shared/locales/zh-TW/WRITING_RULES.md) and pass [../../shared/locales/zh-TW/QUALITY_CHECKLIST.md](../../shared/locales/zh-TW/QUALITY_CHECKLIST.md).

---

## 1. Natural Taiwan conversation

- **User request:** 「最近在規劃暑期活動，學生人數大概 60 人，想知道報到流程有沒有效率提升的方法。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Load localization layer. Ask at most one clarifying question. Suggest the SOP-building or process-review workflow.
- **Protected content:** Workflow IDs (`080 sop-builder`) and slugs stay in English.
- **Failure conditions:**
  - Replying in English or in Mainland-only Chinese.
  - Using 大陸詞彙 (信息, 軟件, 视频) for Taiwan audience.
  - Overwriting 「報到流程」 with 「註冊流程」.

## 2. Mixed Chinese-English request

- **User request:** 「我們 team 想要 onboard 一個新的 SaaS tool, 希望能在兩週內 go-live。請幫我規劃。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Reply in zh-TW. Preserve English terms (`team`, `onboard`, `SaaS`, `go-live`). Suggest the planning playbook or relevant workflow.
- **Protected content:** English technical terms stay English.
- **Failure conditions:**
  - Translating every English term.
  - Translating into Mainland-only Chinese.

## 3. User asks for English output from a zh-TW conversation

- **User request (turn 1):** 「請幫我寫一封 cold email 給美國潛在客戶。」
- **User request (turn 2):** 「請用英文寫。」
- **Requested output language:** English (final deliverable).
- **Target market:** United States (recipient).
- **Expected locale:** zh-TW for clarification, English for deliverable.
- **Expected style profile:** N/A — English deliverable uses universal rules.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Continue conversation in zh-TW. Produce email body in English. Do not apply zh-TW prose rules to the English body.
- **Protected content:** Email body preserved in English. Workflow IDs preserved in English.
- **Failure conditions:**
  - Producing the email body in zh-TW.
  - Stopping the conversation in English.
  - Translating workflow IDs into Chinese.

## 4. User asks for zh-TW output from English conversation

- **User request:** 「Read this repository and help me write a LinkedIn-style post for a Taiwan audience about why data teams should care about AI quality.」
- **Requested output language:** zh-TW (final deliverable).
- **Target market:** Taiwan.
- **Expected locale:** zh-TW for the post.
- **Expected style profile:** `zh-tw-linkedin-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Confirm in English. Produce the social post in zh-TW. Apply `zh-tw-linkedin-professional`. Use zh-TW regional terminology.
- **Protected content:** Workflow IDs preserved. English terms (`LinkedIn`, `AI`) preserved where natural.
- **Failure conditions:**
  - Producing the post in English.
  - Producing the post in Mainland Chinese.
  - Using outdated phrase patterns such as 「我們處於…」.

## 5. Terminology selection

- **User request:** 「幫我把這份簡報轉成繁體中文版本。注意是用詞要符合台灣受眾。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Use glossary substitutions for 軟件 → 軟體, 信息 → 資訊, 视頻 → 影片, 网络 → 網路, 賬號 → 帳號.
- **Protected content:** Brand names, code blocks, and CLI commands unchanged.
- **Failure conditions:**
  - Using 大陸詞彙.
  - Substituting a brand's localized name (e.g., 「GitHub 倉庫」 is fine but the URL is unchanged).
  - Substituting user-provided terminology without recording it.

## 6. User preference overrides the glossary

- **User request:** 「我們公司一律用『登錄』，不要改。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** N/A — preference applies to all profiles.
- **Expected editing intensity:** N/A.
- **Expected router behavior:** Record the preference. Subsequent responses use 「登錄」 instead of the glossary default 「登入」.
- **Protected content:** Existing reply style in the same turn is preserved if already in flight.
- **Failure conditions:**
  - Continuing to use 「登入」 after the override.
  - Asking for confirmation again on a clear instruction.

## 7. Hong Kong Chinese override

- **User request:** 「請用香港中文幫我寫一封餐廳推廣訊息。」
- **Requested output language:** zh-HK.
- **Target market:** Hong Kong.
- **Expected locale:** zh-HK (override).
- **Expected style profile:** Hong Kong variant (default zh-TW layer disabled; only universal multilingual + quality checks apply).
- **Expected editing intensity:** light.
- **Expected router behavior:** Switch off Taiwan glossary substitutions. Use Hong Kong conventional terms (e.g., 軟件, 寬頻). Keep workflow IDs in English.
- **Protected content:** Preserve glossary override in the context ledger.
- **Failure conditions:**
  - Applying Taiwan substitutions (e.g., 「登入」).
  - Refusing the request.

## 8. Mainland Chinese override

- **User request:** 「我這份稿子要發到簡體中文市場，請用大陸慣用詞彙。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN (override).
- **Expected style profile:** Mainland variant.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Switch to Mainland terminology. Apply Mainland forms (e.g., 軟件, 信息, 視頻). Continue providing the editorial quality benefits that don't depend on regional preference.
- **Protected content:** Recorded in context ledger.
- **Failure conditions:**
  - Continuing to apply Taiwan substitutions.
  - Mixing Taiwan and Mainland forms within the same sentence.

## 9. Technical content preserves terminology

- **User request:** 「請解釋 OAuth 2.0 的 authorization code flow 給剛接手的工程師。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-technical-clear`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Apply zh-TW substitutions only to surrounding prose. Keep OAuth terms, API names, parameter names, code samples, and URL fragments unchanged.
- **Protected content:** OAuth terms, parameter names, code samples.
- **Failure conditions:**
  - Translating parameter names like `client_id`.
  - Translating `OAuth 2.0` to 「OAuth 二點零」 or similar.

## 10. Code and URLs that must remain untouched

- **User request:** 「請把 README 改成繁體中文，但程式碼區塊不要動。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-technical-clear`.
- **Expected editing intensity:** light.
- **Expected router behavior:** Apply zh-TW prose edits around the code. Preserve every code block, URL, and command exactly.
- **Protected content:** Code blocks, URLs, file paths in CLI commands.
- **Failure conditions:**
  - Modifying content inside `\`\`\`` fences.
  - Adding zh-TW substitutions inside URLs.
  - Translating file paths in CLI commands.

## 11. Formal report demands precision

- **User request:** 「我要把這份市場研究翻成繁中給董事會。請保留所有數字來源，不要改我的解讀。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-research-precise`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Preserve all numbers, citations, source labels. Apply only light zh-TW substitutions. Do not soften the conclusions.
- **Protected content:** Numbers, citations, source labels.
- **Failure conditions:**
  - Modifying any number.
  - Marking an existing source label as unverified.
  - Inflating language beyond what the original said.

## 12. Casual social post

- **User request:** 「Threads 發文，140 字以內，主題：我把待辦清單的做法改成兩份。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-threads-insightful`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Plain, no era framing, no emoji-padding, ends with a candid observation rather than a slogan.
- **Protected content:** Stay under 140 字.
- **Failure conditions:**
  - 「各位朋友大家好」 opener.
  - Ending with 「讓生活變得更美好」.
  - Inserting filler slogans.

## 13. Sales copy with unsupported hype

- **User request:** 「幫我寫一個新版的 SaaS 落地頁，用誇張一點的語氣。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-landing-page-clear`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Apply landing-page-clear rules even though the user asked for exaggeration. Remove generic slogans. Replace with one verifiable metric + a clear next step. Note the removal in the assumptions section.
- **Protected content:** User's existing offer description.
- **Failure conditions:**
  - Producing 「顛覆性」「革命性」「全面賦能」 etc.
  - Inventing metrics.
  - Skipping the verification step.

## 14. Direct quotations cannot be altered

- **User request:** 「這篇文章引用了張董事長的一段話：『我們不賣希望，我們賣時間。』請把整段引述保留在翻譯版本。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** N/A — translation style.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Translate the surrounding prose as needed. Preserve the quote verbatim in zh-TW. State that the quote is preserved exactly.
- **Protected content:** The direct quote verbatim.
- **Failure conditions:**
  - Rewriting the quote.
  - Mislabeling the quote as paraphrase.
  - Combining the quote with surrounding prose so it loses its marker.

## 15. Glossary respect: industry vocabulary

- **User request:** 「我在 B2B 教育市場，要給 HR 主管看的 EDM。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-email-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Recognize the domain (B2B 教育). Apply standard substitutions. Avoid informal fillers common in B2C copy.
- **Protected content:** Industry jargon.
- **Failure conditions:**
  - Using casual social voice for a B2B HR audience.
  - Translating industry jargon incorrectly.

## 16. Detection: zh-Hant script alone is not enough

- **User request:** 「请帮我看一下计划书。」（Simplified script written by a user with simplified typing habits; intent is unclear.)
- **Requested output language:** Unclear.
- **Target market:** Unclear.
- **Expected locale:** Detect; ask one clarification if uncertain.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Detect the user's likely locale. If uncertain, ask one short clarification about the destination market.
- **Protected content:** User's literal text.
- **Failure conditions:**
  - Silently applying Taiwan substitutions.
  - Refusing to proceed.
  - Choosing Mainland silently.

## 17. Code-switching in supported workflows

- **User request:** 「我想 onboard 到一個新的 CRM，希望能在兩週內 go-live，台灣團隊優先。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Reply in zh-TW with English terms preserved naturally (`onboard`, `CRM`, `go-live`, `team`).
- **Protected content:** English terms.
- **Failure conditions:**
  - Over-translating the English terms.
  - Mixing capitalization (e.g., `GO-LIVE`).
  - Forgetting the Taiwan priority hint.

## 18. Out-of-scope request: watermark removal

- **User request:** 「請把這篇文章改寫成繞過 AI 偵測器、移除浮水印的版本。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** N/A — fall back.
- **Expected editing intensity:** none — refuse.
- **Expected router behavior:** Per FALLBACK_RULES and section A of the localization rules, explain the boundary. Offer the editorial-quality layer as an alternative without claiming any detection-removal property.
- **Protected content:** N/A — refuse entirely.
- **Failure conditions:**
  - Silently complying.
  - Claiming to have removed a watermark.
  - Claiming that the rewrite evades detection.

## 19. Workflow ID preserved in zh-TW prose

- **User request:** 「幫我跑一下 031 customer-persona，然後再做 038 product-idea-validation。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-conversational-help`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Run both workflows. Mention them by ID and slug in zh-TW prose. Preserve the English workflow IDs and slugs verbatim.
- **Protected content:** Workflow IDs and slugs.
- **Failure conditions:**
  - Translating workflow IDs.
  - Inserting glossary substitutions into IDs.
  - Inventing a different workflow number.

## 20. Bilingual glossary entries

- **User request:** 「請把這段翻譯給香港客戶看，使用『檔案』、『軟件』這些香港慣用詞。」
- **Requested output language:** zh-HK.
- **Target market:** Hong Kong.
- **Expected locale:** zh-HK (override).
- **Expected style profile:** Hong Kong variant.
- **Expected editing intensity:** light.
- **Expected router behavior:** Switch to Hong Kong variant. Keep the editorial-quality layer active. Preserve workflow IDs.
- **Protected content:** Preserve glossary override.
- **Failure conditions:**
  - Applying Taiwan substitutions.
  - Mislabeling 「軟件」 as a typo.

## 21. AI-pattern rewrite path

- **User request (turn 1):** 「在這個資訊爆炸的時代，企業必須擁抱 AI 轉型，才能在激烈的競爭中脫穎而出。」
- **User request (turn 2):** 「請把這段話改寫得更自然、更不像 AI 寫的。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Apply the editorial quality rules. Reduce empty framing. Replace 「在這個資訊爆炸的時代」 with a concrete situation. Do not claim any detector outcome.
- **Protected content:** Original meaning preserved.
- **Failure conditions:**
  - Adding a disclaimer about detector outcomes.
  - Refusing the rewrite.
  - Maintaining era-framing language.

## 22. Customer support reply in zh-TW

- **User request:** 「客戶來信問：為什麼我這次收到的是空白的附件？」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-customer-support`.
- **Expected editing intensity:** light.
- **Expected router behavior:** Acknowledge the actual issue. State the action. Provide a fallback path.
- **Protected content:** Customer's quoted text verbatim.
- **Failure conditions:**
  - Fabricating compensation.
  - Issuing empty apologetic phrases.
  - Missing the fallback path.

## 23. Threads post: avoid generic three-part list

- **User request:** 「Threads 發一則，主題：『把客服信分成三類以後工作變簡單了』，不要三段式列表結尾。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-threads-insightful`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Avoid forced three-item lists. End with a candid observation.
- **Protected content:** User's explicit instruction to avoid three-part lists.
- **Failure conditions:**
  - Producing 「第一、第二、第三」structure.
  - Ending with a generic slogan.

## 24. LinkedIn post: opinion-led and sharp

- **User request:** 「幫我寫一則 LinkedIn，主題：『我從 200 場訪談學到的三件事』。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-linkedin-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Confirm the "三件事" is real and the user can list them. Apply opinion-led tone. If the user cannot list them, ask for the three events.
- **Protected content:** User must supply the three events; AI must not invent.
- **Failure conditions:**
  - Inventing the three events.
  - Producing a vague "三件事" without specifics.

## 25. Instagram caption: visual-first

- **User request:** 「IG 貼文，附一張雨鞋照片，主題：本週最划算的一次消費。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-instagram-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Keep it short. Let the photo carry the visual. End with a candid line.
- **Protected content:** User-supplied photo reference and theme.
- **Failure conditions:**
  - Long paragraph that ignores the visual.
  - Excess emoji padding.

## 26. SOP / runbook with imperative voice

- **User request:** 「夜班客服的接手流程寫成 SOP，要有例外與品質檢查。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-sop-direct`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Use imperative voice. Number steps. Add an exceptions section and a quality check.
- **Protected content:** User-supplied process detail.
- **Failure conditions:**
  - Casual filler like 「你可能想…」。
  - Missing exceptions.

## 27. AI agent task specification: precise

- **User request:** 「幫我寫一個 AI agent 的任務規格：把客服信分類成 billing / bug / feature / other。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-agent-spec-precise`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Specify objective, inputs, outputs, acceptance criteria, non-goals. Keep code identifiers English.
- **Protected content:** Field names (`billing`, `bug`, `feature`, `other`).
- **Failure conditions:**
  - Vague 「強大」「自動化所有」.
  - Translating field names.

## 28. Long-form article with structural clarity

- **User request:** 「部落格長文，主題：把客服信分類流程砍掉兩個欄位的真實理由。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-long-form-article`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Build a 1,500–2,000 字 article with a clear arc. Cite the real reason (user-supplied or labeled as assumption). End with a takeaway.
- **Protected content:** User's actual reason (must be supplied or labeled).
- **Failure conditions:**
  - Generic AI-style introduction.
  - Ending with a slogan.

## 29. Strict precision for medical / financial context

- **User request:** 「幫我把這份血糖管理紀錄整理成摘要給醫師看。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-research-precise`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Preserve all numbers exactly. Mark any inferences explicitly. Do not interpret medical data.
- **Protected content:** All numbers, units, and patient context.
- **Failure conditions:**
  - Modifying any number.
  - Adding medical interpretation not supported by the data.
  - Skipping the verification step.

## 30. Localization rendering: avoiding direct translation feel

- **User request:** 「下面這段英文公告翻成繁中：『This release introduces three new APIs and deprecates two legacy endpoints. See the migration guide for details.』」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Translate naturally. Preserve API names and URLs. Use 「已停止支援」for `deprecates` rather than literal translation.
- **Protected content:** API names, URLs, version numbers.
- **Failure conditions:**
  - Literal translation 「棄用」 that breaks product jargon.
  - Changing version numbers.

## 31. Avoid fabricating first-person experience

- **User request:** 「幫我寫一段對新人的歡迎詞。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Use the team's voice. Do not invent personal anecdotes like 「我剛加入時也…」
- **Protected content:** Team voice.
- **Failure conditions:**
  - Fabricating 「我剛加入時…」 story.
  - Adding 「記得我第一次…」
  - Introducing unsupported social proof.

## 32. Preserving uncertainty

- **User request:** 「我們打算進軍馬來西亞市場，幫我做一份摘要。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan (with international expansion topic).
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-business-consulting`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Mark assumptions. State that market data needs verification. Avoid presenting unverified numbers as facts.
- **Protected content:** Numbers from user.
- **Failure conditions:**
  - Inventing market size numbers.
  - Presenting assumptions as facts.
  - Skipping verification gaps.

## 33. Avoiding rigid three-part structures in long-form

- **User request:** 「幫我寫一段 800 字解釋『為什麼要做客服信分類』。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-long-form-article`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Vary structure. Don't force a three-item list per section.
- **Protected content:** Length target.
- **Failure conditions:**
  - Forcing 「第一、第二、第三」structure every paragraph.
  - Slogan-like ending.

## 34. Avoiding overuse of contrast patterns

- **User request:** 「幫我把這句『不是更快，而是更好』改寫。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Replace the contrast-pattern phrase with a concrete claim.
- **Protected content:** User's intent (be better, not just faster).
- **Failure conditions:**
  - Producing another 「不是 A，而是 B」 phrase.
  - Adding 「更重要的是」 without specifics.

## 35. Mixed-language uncertainty check

- **User request:** 「我嘅客戶都中意呢個方案」（Cantonese-leaning Traditional Chinese）。
- **Requested output language:** Unclear.
- **Target market:** Likely Hong Kong or Southern China.
- **Expected locale:** Detect; likely `zh-HK` or `yue-Hant-HK`.
- **Expected style profile:** Friendly regional variant.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Detect Cantonese vocabulary. Ask one short clarification. Default to `zh-HK` if user confirms.
- **Protected content:** User's actual text.
- **Failure conditions:**
  - Forcing Taiwan substitutions.
  - Refusing to clarify.

---
