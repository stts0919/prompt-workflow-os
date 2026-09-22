# Localization Cases — zh-CN (≥30)

These cases exercise the Mainland Simplified Chinese localization layer at the
language level. Each case uses the standard schema:

- **User request**
- **Requested output language**
- **Target market**
- **Expected locale**
- **Expected style profile**
- **Expected editing intensity**
- **Expected router behavior**
- **Protected content**
- **Failure conditions**

User-facing behavior should match
[../../shared/locales/zh-CN/WRITING_RULES.md](../../shared/locales/zh-CN/WRITING_RULES.md)
and pass
[../../shared/locales/zh-CN/QUALITY_CHECKLIST.md](../../shared/locales/zh-CN/QUALITY_CHECKLIST.md).

---

## 1. Natural Mainland conversation

- **User request:** 「最近在规划暑期活动，学生人数大概 60 人，想知道报到流程有没有效率提升的方法。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Load zh-CN layer. Ask at most one clarifying question. Suggest SOP / process-review workflows.
- **Protected content:** Workflow IDs (`080 sop-builder`) stay in English.
- **Failure conditions:**
  - Replying in English or in Taiwan-only Chinese (繁體).
  - Using 台湾词汇 (資訊, 軟體, 影片) for Mainland audience.
  - Overwriting 「报到流程」 with 「簽到流程」.

## 2. Mixed Chinese-English request

- **User request:** 「我们 team 想要 onboard 一个新的 SaaS tool, 希望能在两周内 go-live。请帮我规划。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Reply in zh-CN. Preserve English terms (`team`, `onboard`, `SaaS`, `go-live`).
- **Protected content:** English technical terms stay English.
- **Failure conditions:**
  - Translating every English term.
  - Translating into Traditional Chinese (繁體).

## 3. User asks for English output from a zh-CN conversation

- **User request (turn 1):** 「请帮我写一封 cold email 给美国潜在客户。」
- **User request (turn 2):** 「请用英文写。」
- **Requested output language:** English (final deliverable).
- **Target market:** United States (recipient).
- **Expected locale:** zh-CN for clarification, English for deliverable.
- **Expected style profile:** N/A — English deliverable uses universal rules.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Continue conversation in zh-CN. Produce email body in English. Do not apply zh-CN prose rules to the English body.
- **Protected content:** Email body preserved in English. Workflow IDs preserved in English.
- **Failure conditions:**
  - Producing the email body in zh-CN.
  - Treating English output as a translation exercise.

## 4. 小红书 lifestyle post

- **User request:** 「帮我写一篇小红书笔记，介绍我新买的咖啡机。要真实感强一点。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-xiaohongshu-lifestyle`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** 300–800 字 with emoji, conversational tone, 「姐妹们」 / 「家人们」 address.
- **Protected content:** Brand name of the 咖啡机 stays in its official form.
- **Failure conditions:**
  - Tone that reads like a 公文 document.
  - Missing emoji entirely.
  - Including a fake personal anecdote the user didn't provide.

## 5. 公众号 long-form article

- **User request:** 「帮我写一篇 2000 字的公众号文章，主题是 AI 对内容行业的冲击。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-thought-leadership`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** 1500–4000 字 long-form with clear sections, data cited or marked as assumption.
- **Protected content:** User-supplied data and sources.
- **Failure conditions:**
  - Buzzword-heavy opener with no substance.
  - Hallucinated statistics without 「数据来源待确认」 markers.
  - Slogan-style ending.

## 6. 微博 short post

- **User request:** 「帮我写一条微博，介绍一下今天的天气和心情。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-weibo-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Under 200 characters (or split into multiple posts); use `#话题#` and 1-3 emoji.
- **Protected content:** User-supplied personal context.
- **Failure conditions:**
  - Going over the 微博 length limit.
  - Tone that's too formal / corporate.
  - Missing hashtags when the platform expects them.

## 7. 抖音 short video script

- **User request:** 「帮我写一个 30 秒的抖音脚本，介绍一款新产品。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-douyin-script`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Time-axis marked `[0-3s]` etc.; strong hook in the first 3 seconds.
- **Protected content:** Brand name of the new product.
- **Failure conditions:**
  - Weak opening that fails to hook viewers.
  - Missing time-axis markers.
  - Promising medical / financial efficacy that isn't substantiated.

## 8. 哔哩哔哩 中长视频 script

- **User request:** 「帮我写一个 5 分钟的 B 站视频脚本，介绍一款新的开发工具。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-bilibili-script`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Chapter markers (e.g. `00:30 开箱`), concise but explanatory.
- **Protected content:** Tool name, version numbers.
- **Failure conditions:**
  - Reading like a script that doesn't acknowledge viewers.
  - Wrong technical details that the 知识区 audience will catch.

## 9. Business email to a Mainland client

- **User request:** 「帮我给王总写一封邮件，告诉他项目延期一周。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-email-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** 「王总：」salutation; clear paragraphs; specific new deadline; ask for confirmation.
- **Protected content:** Recipient name, project name.
- **Failure conditions:**
  - 「亲爱的」 opening for a senior executive.
  - Vague new deadline.
  - No request for confirmation at the end.

## 10. Cross-strait terminology flip

- **User request:** 「把这段台湾文案改写成大陆版本：『這款軟體支援高速下載，畫質超清晰，使用介面友善。』」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Replace 軟體 → 软件, 介面 → 界面, 畫質 → 画质. Convert 繁體 → 简体.
- **Protected content:** Brand name if any.
- **Failure conditions:**
  - Leaving any 繁體 character in the output.
  - Translating 「軟體」 as 「软件」 but leaving 「介面」 unchanged.

## 11. Customer support reply

- **User request:** 「客户投诉我们的快递 5 天还没到，帮我写一封回复。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-customer-support`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Empathetic opening; clear apology; specific action (e.g. 「24 小时内回复订单号」).
- **Protected content:** Order number, customer name if provided.
- **Failure conditions:**
  - Defensive tone.
  - 「非常感谢您的反馈」 cliche.
  - No concrete next step.

## 12. User explicitly requests 繁體中文 — must NOT route to zh-CN

- **User request:** 「帮我写一篇文章，要用繁体中文写，给台湾读者看。」
- **Requested output language:** zh-TW.
- **Target market:** Taiwan.
- **Expected locale:** zh-TW.
- **Expected style profile:** `zh-tw-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Load zh-TW layer, not zh-CN. Even though the conversation is in Simplified Chinese, the user's explicit instruction wins.
- **Protected content:** N/A.
- **Failure conditions:**
  - Outputting Simplified Chinese.
  - Using Mainland terminology.

## 13. User explicitly requests 简体 / 大陆 — must NOT route to zh-TW

- **User request:** 「帮我写一篇文章，用简体中文写，给大陆读者看。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Load zh-CN layer. Even if conversation is in Traditional, the explicit output-language request wins.
- **Protected content:** N/A.
- **Failure conditions:**
  - Outputting Traditional Chinese.
  - Using Taiwan terminology.

## 14. B2B 商业顾问 report

- **User request:** 「帮我们团队写一份 Q4 战略建议，关于要不要进入东南亚市场。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Structure with 「现状 / 选项 / 建议」 sections; data cited or marked as assumption; concrete next actions.
- **Protected content:** Internal data and team context.
- **Failure conditions:**
  - 「赋能」「抓手」 buzzword stacking.
  - Subjective recommendations without data.
  - Missing the 「下一步」 section.

## 15. 落地页 / 销售页

- **User request:** 「帮我写一个 SaaS 工具的落地页，目标用户是大陆中小企业主。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-landing-page-clear`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** 标题 + 副标题 + 痛点 → 方案 → 证据 → CTA; clear CTA button text.
- **Protected content:** Brand name, product name.
- **Failure conditions:**
  - Vague CTA like 「了解更多」.
  - Missing evidence section.
  - 「颠覆」「革命」 exaggeration.

## 16. Translation: English to Simplified Chinese

- **User request:** 「Translate this English paragraph into Simplified Chinese: 'This release introduces three new APIs and deprecates two legacy endpoints. See the migration guide for details.'」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Translate naturally. Use 「停止维护」 or 「不再支持」 for `deprecates`. Preserve API names and URLs.
- **Protected content:** API names, URLs, version numbers.
- **Failure conditions:**
  - Literal translation 「弃用」 that breaks Mainland product jargon.
  - Changing version numbers.

## 17. Translation: Traditional Chinese to Simplified Chinese

- **User request:** 「把这段繁中改写成简体：『我們的客戶都中意呢個方案。』」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** light.
- **Expected router behavior:** Convert to 「我们的客户都喜欢这个方案」. Preserve the original sentence structure (light editing, not full rewrite).
- **Protected content:** None.
- **Failure conditions:**
  - Leaving any 繁體 character.
  - Fully rewriting the sentence into a different structure.

## 18. Cantonese vocabulary in a 简体 request

- **User request:** 「我想要整返個新嘅 logo。」 (Cantonese vocabulary in a Simplified-looking request)
- **Requested output language:** zh-CN (default).
- **Target market:** Mainland China (default).
- **Expected locale:** zh-CN; ask one short clarification.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Detect Cantonese vocabulary (整, 嘅, 嘅). Ask: 「你希望用简体 / 繁體 / 廣東話口吻？」Default to zh-CN form if user confirms.
- **Protected content:** None.
- **Failure conditions:**
  - Treating Cantonese vocabulary as Mainland speech.
  - Silently rewriting to fully Mainland without asking.

## 19. Avoiding AI-pattern cliches

- **User request:** 「帮我写一段我们产品的介绍。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Avoid 「首先 / 其次 / 最后」 triad. Avoid 「赋能 / 闭环」 buzzwords. Be concrete.
- **Protected content:** Product name, real features.
- **Failure conditions:**
  - 「首先...其次...再次...最后」 opening.
  - Stacking buzzwords without specifics.
  - 「希望对您有所帮助」 closing.

## 20. Strict precision: regulated financial claim

- **User request:** 「把这个投资产品的预期收益整理成摘要给客户看。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Cite source for every data point. Mark inferences. Do not soften regulatory risk warnings.
- **Protected content:** Numbers, regulatory disclosures.
- **Failure conditions:**
  - Omitting source attribution.
  - Softening 「风险提示」.
  - Promising returns without 「过往业绩不预示未来表现」 disclaimer.

## 21. Strict precision: medical context

- **User request:** 「帮我把这份血糖管理记录整理成摘要给医生看。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Preserve all numbers exactly. Mark any inferences. Do not interpret medical data.
- **Protected content:** All numbers, units, patient context.
- **Failure conditions:**
  - Modifying any number.
  - Adding medical interpretation not supported by the data.

## 22. Brand name preservation

- **User request:** 「帮我写一篇介绍 Apple Vision Pro 的知乎专栏。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-thought-leadership`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Brand name stays as `Apple Vision Pro` (or `Apple Vision Pro` if mixing Chinese); do not translate as 「苹果视觉 Pro」.
- **Protected content:** Brand name.
- **Failure conditions:**
  - Translating 「Apple」 to 「苹果公司」 in a brand context.
  - Translating 「Vision Pro」.

## 23. Code / identifier preservation

- **User request:** 「帮我写一段文档介绍我们的 agent。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** light.
- **Expected router behavior:** Keep workflow IDs in English (`091 agent-task-spec`). Keep code / API names verbatim.
- **Protected content:** Workflow IDs, code identifiers.
- **Failure conditions:**
  - Translating `agent-task-spec` to 「智能体任务规格」 inside an identifier context.

## 24. Numbers, units, and currency preservation

- **User request:** 「帮我整理这份营收数据：营收 1,500,000 元，增长率 12.5%。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Keep numbers exactly. Format with commas (`1,500,000`) and unit (`元` or `人民币`). Do not convert to 「150 万」 unless the user asks.
- **Protected content:** All numbers, units.
- **Failure conditions:**
  - Converting 1,500,000 元 to 150 万元 without asking.
  - Modifying the growth rate.

## 25. Mixed-script avoidance

- **User request:** 「写一段自我介绍。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Output is fully Simplified Chinese. No 繁體 characters appear (unless quoted).
- **Protected content:** None.
- **Failure conditions:**
  - Mixing 繁體 / 简体 within a single paragraph.
  - Using 繁體-only characters like 「資」「軟」「網」 instead of 「资」「软」「网」.

## 26. Avoiding excessive politeness cliches

- **User request:** 「帮我写一段客户感谢邮件。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-email-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Avoid 「非常感谢您的支持」 cliche opening. Be specific about what you're thanking for.
- **Protected content:** Customer name, specific contribution.
- **Failure conditions:**
  - 「亲爱的」 opening for a B2B recipient.
  - Generic 「非常感谢」 without specifics.

## 27. Currency and date format

- **User request:** 「帮我整理这份跨境电商财报。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Keep currency units as provided. Do not silently convert USD to CNY. Date format: 「2026 年 9 月 22 日」 or 「2026-09-22」.
- **Protected content:** Currency, dates, amounts.
- **Failure conditions:**
  - Silently converting USD to CNY without a stated exchange rate.
  - Using a different date format than the source.

## 28. Long-form zh-CN thought leadership

- **User request:** 「帮我写一篇 2000 字的知乎专栏，谈 AI Agent 的下一阶段。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-thought-leadership`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Build a 1,500–2,500 字 article with a clear arc. Cite real data or label as assumption. End with a takeaway.
- **Protected content:** User's actual argument (must be supplied or labeled).
- **Failure conditions:**
  - Generic AI-style introduction.
  - Ending with a slogan.

## 29. Casual × formal mix (channel conflict)

- **User request:** 「帮我写一个朋友圈文案，要正式一点但又不要太死板。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional` (between weibo-casual and business-consulting).
- **Expected editing intensity:** standard.
- **Expected router behavior:** Lean toward professional but allow 1-2 emojis and a personal voice.
- **Protected content:** None.
- **Failure conditions:**
  - Going fully casual (over-emojis).
  - Going fully formal (corporate jargon).

## 30. Output language is English — skip zh-CN layer

- **User request (in English):** 「Write a Xiaohongshu-style post for me in English.」 (Note: the user explicitly says English.)
- **Requested output language:** English.
- **Target market:** Mainland / international.
- **Expected locale:** None — zh-CN layer skipped.
- **Expected style profile:** N/A — English deliverable.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Despite the platform hint (Xiaohongshu), the user's output language is English, so zh-CN prose rules do not apply. Universal English quality rules apply.
- **Protected content:** English body.
- **Failure conditions:**
  - Trying to apply zh-CN writing rules to an English body.
  - Translating the body to Chinese without the user asking.

## 31. zh-CN user asks for 「不绕弯子」

- **User request:** 「帮我写个版本，直接说重点，别绕。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Strip 「综上所述」「值得注意的是」等 cliches. Front-load the answer. Bullet-point where appropriate.
- **Protected content:** None.
- **Failure conditions:**
  - Adding unnecessary throat-clearing.
  - 「首先 / 其次 / 最后」 structure when a flat list would do.

## 32. Avoiding fabrication of personal experience

- **User request:** 「帮我写一段对新人的欢迎词。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Use the team's voice. Do not invent personal anecdotes like 「我刚加入时也…」
- **Protected content:** Team voice.
- **Failure conditions:**
  - Fabricating 「我刚加入时…」 story.
  - Adding 「记得我第一次…」 without user input.

## 33. Auto-escalate editing intensity for compliance content

- **User request:** 「帮我写一份给客户的隐私政策摘要。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-business-consulting`.
- **Expected editing intensity:** strict_precision (auto-escalated).
- **Expected router behavior:** Even if the workflow default is `standard`, escalate to `strict_precision` because the content is regulated (privacy policy).
- **Protected content:** Specific legal wording, citations to PIPL (个人信息保护法).
- **Failure conditions:**
  - Using `standard` intensity.
  - Softening compliance language.

## 34. Local platform citation (小红书 笔记)

- **User request:** 「帮我引用小红书的一个笔记作为案例来源。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-thought-leadership`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Cite the 小红书 note by author handle and date. Mark if the note is the only source.
- **Protected content:** Author name, note URL, date.
- **Failure conditions:**
  - Hallucinating a quote from the note.
  - Failing to mark the source as a single-platform observation.

## 35. Honoring user-recorded terminology

- **User request:** (follow-up) 「以后用『智能体』，不要用『代理』。」
- **Requested output language:** zh-CN.
- **Target market:** Mainland China.
- **Expected locale:** zh-CN.
- **Expected style profile:** `zh-cn-friendly-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Record 「智能体」 as the user's preferred term in the context ledger. Use 「智能体」 consistently in subsequent outputs.
- **Protected content:** User-recorded terminology.
- **Failure conditions:**
  - Continuing to use 「代理」.
  - Mixing 「智能体」 and 「代理」 interchangeably.