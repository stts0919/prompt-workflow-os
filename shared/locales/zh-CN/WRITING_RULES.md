# Writing Rules — Simplified Chinese (`zh-CN`, Mainland China)

> Source-of-truth file for the `zh-CN` writing rules. Lives under `shared/locales/zh-CN/` per the architecture in [`../README.md`](../README.md).

This document is the `zh-CN` localization layer. It is paired with
[TERM_GLOSSARY.md](TERM_GLOSSARY.md), [STYLE_PROFILES.md](STYLE_PROFILES.md),
and [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md). The four files together form
the `zh-CN` locale pack.

The `zh-TW` layer is the reference implementation. This `zh-CN` layer matches
its structure and rigor while adapting content to Mainland readers. Do not
treat one locale as a thin skin over the other; the audiences, terminology,
channels, and editorial norms differ.

For the canonical glossary values and platform terminology, see
[TERM_GLOSSARY.md](TERM_GLOSSARY.md). For style profiles, see
[STYLE_PROFILES.md](STYLE_PROFILES.md). For the dual-layer quality gate, see
[QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md).

## A. Purpose and scope

This document defines how `prompt-workflow-os` produces user-facing content in
Simplified Chinese for Mainland China audiences. It covers:

- terminology and phrasing choices,
- channel-specific tone for Mainland platforms (公众号 / 微博 / 小红书 / 抖音 / 哔哩哔哩),
- editorial rewrite for clarity, naturalness, and tone,
- what is always protected and never rewritten,
- how the layer integrates with the router and other locales.

It does not cover:

- claims about bypassing AI detection or removing watermarks (see section K),
- Taiwan-specific phrasing or political references (use `zh-TW` for those).

## B. Automatic activation rules

The router activates the `zh-CN` layer when **all** of the following hold:

1. The user requested output in Simplified Chinese, **or** explicitly named
   Mainland China (or a city in Mainland) as the target market.
2. The user did **not** explicitly request Traditional Chinese (Taiwan / Hong
   Kong). When in doubt between `zh-TW` and `zh-CN`, the router asks one
   short clarification; if the user does not answer, the router keeps the
   user's input-language conventions as the default.
3. The selected workflow's `localization.supported_locales` includes `zh-CN`,
   or the workflow's category default for `zh-CN` applies.

The router does **not** activate the layer when the deliverable's output
language is English, Japanese, Korean, or any non-Chinese language — even if
the user wrote in Chinese.

## C. Input language vs output language vs target market

The router treats the three signals independently:

- **Input language** is what the user typed in. It controls which locale the
  router thinks in.
- **Requested output language** is what the deliverable should be written in.
  It controls the layer to load.
- **Target market** is the audience the deliverable is for (Mainland China,
  Taiwan, Hong Kong, international, etc.). It controls terminology, currency,
  date format, and protected content norms.

Common combinations:

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Simplified Chinese | Simplified Chinese | Mainland | Load `zh-CN` layer. |
| Traditional Chinese | Simplified Chinese | Mainland | Load `zh-CN`; the user's input was Traditional, but the output language is the activation signal. |
| Simplified Chinese | Traditional Chinese | Taiwan | Do **not** load `zh-CN`; load `zh-TW`. |
| English | Simplified Chinese | Mainland | Load `zh-CN`; English input does not block the layer. |
| Any | English | Any | Skip the `zh-CN` layer entirely (Case A in `AI_ROUTER.md`). |

## D. Protected content rules

The layer never rewrites the following. They are protected across every
editing intensity:

- Code, identifiers, API names, workflow IDs and slugs (e.g. `027
  translation-localization`, `080 sop-builder`).
- URLs, domain names, and email addresses.
- Brand names, product names, and trademarked terms (whether the user typed
  阿里巴巴 / 腾讯 / 字节跳动 / Apple / Google or any other). Do not localize
  brand names even when a Chinese form exists.
- Direct quotations, citations, and required regulatory disclosures.
- Numbers, units, dates, times, monetary amounts, and version strings unless
  the user explicitly requests conversion (e.g. 美元 → 人民币 for a Mainland
  reader).
- Required technical or legal wording supplied by the user.
- User-recorded terminology in the context ledger.

When a workflow's content mixes protected and unprotected spans (for example,
a translated paragraph that embeds an English product name), the layer edits
only the unprotected spans and leaves the protected spans verbatim.

## E. Mainland Chinese language guidance

These rules apply to the unprotected prose.

### E.1 字符与简繁体

- 默认输出**简体中文** (Simplified Chinese). 用户在请求里写繁体或提到「繁体」时，路由到 `zh-TW` 而不是 `zh-CN`.
- 不在简体中文正文里夹带繁体字。如果引用是繁体原文（例如文献引用、用户原话），保留原样并以引用块呈现。
- 不使用不规范的简体字或网络错别字作为正文正式写法（避免「妳」「妳们」等仅用于台港的写法进入 zh-CN 正文）。

### E.2 大陆 vs 港澳台 术语选择

参考 [TERM_GLOSSARY.md](TERM_GLOSSARY.md) 的 13 个分类。这一节列出最常被错选的术语：

| 不要写 (台湾 / 港澳) | 默认写 (大陆) | 备注 |
| --- | --- | --- |
| 軟體、軟件 (HK) | 软件 | 大陆通用 |
| 資訊 | 信息 | 大陆通用 |
| 影片 | 视频 | 大陆通用 |
| 網路 (Taiwan) / 網絡 (HK) | 网络 | 大陆通用 |
| 滑鼠 | 鼠标 | 大陆通用 |
| 印表機 | 打印机 | 大陆通用 |
| 程式 | 程序 (or 程序 / 应用程序) | 大陆 IT 习惯 |
| 資料 | 数据 | 大陆通用 |
| 預設 | 默认 | 大陆通用 |
| 解析度 | 分辨率 | 大陆通用 |
| 頻寬 | 带宽 | 大陆通用 |
| 記憶體 | 内存 | 大陆通用 |
| 介面 | 界面 | 大陆通用 |
| 伺服器 | 服务器 | 大陆通用 |
| 檔案 | 文件 | 大陆通用 |
| 連結 | 链接 | 大陆通用 |
| 搜寻 | 搜索 | 大陆通用 |
| 程式設計 | 编程 / 程序设计 | 大陆常用「编程」 |
| 註冊 | 注册 | 大陆通用 |
| 登入 | 登录 | 大陆通用 |

当用户行业或品牌已经在术语表里登记了自己的写法时，使用用户登记的写法（参考上下文账本）。

### E.3 标点与排版

- 用全角中文标点（，。！？；：「」『』）而不是半角 (, . ! ? ; : " " '')。
- 数字与中文之间留一个空格（参考 GB/T 15834）：例如「大约 30% 的用户」而不是「大约30%的用户」；英文与中文之间也留空格。
- 中英混排时，英文前后各保留一个空格；中文标点不与英文夹杂。
- 段落开头不写空格；标题层级清晰。
- 引号优先使用「」与『』；非必需不使用 " " 与 ' '。

### E.4 数字、日期与货币

- 数字：千分位用半角逗号（1,000,000），不写「100万」除非口语化场景明确。
- 日期：默认「2026 年 9 月 22 日」或「2026-09-22」；不要写「2026/9/22」除非用户偏好。
- 时间：24 小时制（14:30）；明确时区时附「UTC+8」或「北京时间」。
- 货币：默认附单位（人民币、美元）；金额写法「¥100」或「人民币 100 元」按场景选。

### E.5 政治与监管敏感表达

- 默认使用中性、事实性表述；避免主观政治评价。
- 涉及台湾、香港、澳门、新疆、西藏等话题时，使用大陆官方表述（「台湾省」「香港特别行政区」等）当用户的输出语言是简体中文且目标市场是大陆；当读者是港澳台或国际受众时，仍使用 `zh-TW` / `yue-Hant-HK` / 通用英语表达。
- 不主动写未经证实的数据；当用户提供的统计数字没有出处时，标注「数据来源待确认」。

## F. Channel-specific tone rules

The `zh-CN` layer defines ten style profiles. The router picks one based on
the workflow's output channel. Common channels and their defaults:

| Channel | Style profile | Notes |
| --- | --- | --- |
| 微信公众号 long-form | `zh-cn-thought-leadership` | 1500–4000 字，可长可短，论据充分，避免口水话 |
| 微博 short post | `zh-cn-weibo-casual` | 140 字以内，emoji 适度，话题标签 `#xxx` |
| 小红书 lifestyle | `zh-cn-xiaohongshu-lifestyle` | 标题党 + emoji + 真实感，300–800 字 |
| 抖音 / TikTok 脚本 | `zh-cn-douyin-script` | 15–60 秒，前 3 秒钩子强，分镜清楚 |
| 哔哩哔哩 视频脚本 | `zh-cn-bilibili-script` | 中长视频，长于抖音，知识向 |
| 商务邮件 | `zh-cn-email-professional` | 称呼得体，正文简洁，结尾明确 |
| 商业顾问 / 战略文档 | `zh-cn-business-consulting` | 论据结构清晰，假设标注 |
| 落地页 / 销售页 | `zh-cn-landing-page-clear` | 标题有力，痛点 → 方案 → 证据 → CTA |
| 客户支持回复 | `zh-cn-customer-support` | 共情先于解释，结尾给具体动作 |
| 通用专业文 | `zh-cn-friendly-professional` | fallback |

每个 style profile 的完整 schema 见 [STYLE_PROFILES.md](STYLE_PROFILES.md)。

## G. AI-pattern reduction rules

The layer edits out common AI-text patterns. The intensity is set by the
workflow (see `editing_intensity`) and amplified where the channel expects
natural human voice (小红书、微博、抖音脚本).

Common patterns to reduce:

- **三段式排比**：避免连续三个相似结构的句子（如「不仅…而且…更…」连用）。
- **过度对仗**：避免「X 不只是 Y，更是 Z」「X 与 Y，X 与 Z」反复出现。
- **空泛总结**：「综上所述」「总而言之」「值得注意的是」除非明确需要否则删除。
- **过度礼貌**：「非常感谢您的提问」「希望对您有所帮助」等口语之外的客套话删除。
- **万能连接词**：「首先 / 其次 / 再次 / 最后」在短文中通常过度使用；按需保留。

具体 before / after 范例见 [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) 的 Layer 2。

## H. Editing intensity rules

Editing intensity is set per workflow (`localization.editing_intensity`):

- `none` — no edits; protect everything (code, IDs, URLs, brand names,
  regulated wording). Use for technical specs, contracts, citations.
- `light` — minimal cleanup of obvious typos; preserve phrasing. Use for
  translations and any deliverable where exact wording matters.
- `standard` — apply glossary substitutions and AI-pattern reduction where
  natural. Default for most `zh-CN` outputs.
- `strict_precision` — high precision, label uncertainty, no rhetorical
  softening. Mandatory for legal / medical / financial / security /
  compliance / regulated disclosures.

The router auto-escalates to `strict_precision` when the content is regulated
or evidence-sensitive, even if the workflow default is `standard`.

## I. Before-and-after examples (≥25)

Each example shows an unedited (or lightly edited) draft and the `zh-CN`
output. Examples are split by intensity and channel.

### I.1 Intensity: standard, channel: friendly-professional

**Before:** 我们在规划暑期活动，60 人左右，希望报到流程更有效率。

**After:** 我们正在筹备暑期活动，预计参加人数 60 人左右，想优化一下报到流程，看看怎么提升效率。

(注：「希望 → 想要」「人数 → 参加人数」「更有效率 → 提升效率」是更自然的简体中文表达。)

### I.2 Intensity: standard, channel: business-consulting

**Before:** 我们 team 想要 onboard 一个新的 SaaS tool, 两周内 go-live。

**After:** 我们团队希望上线一个新的 SaaS 工具，目标是在两周内 go-live。

(注：保留英文技术术语 `team`、`onboard`、`SaaS`、`go-live`；中文部分使用大陆表达「上线」「团队」。)

### I.3 Intensity: light, channel: translation

**Before (Traditional):** 我們的客戶都中意呢個方案。

**After (Simplified, preserve source style):** 我们的客户都喜欢这个方案。

(注：原文是港式粤语口吻；简体改写保留「都 + 喜欢」句式，不强行改成「客户们全都赞同」。)

### I.4 Intensity: standard, channel: xiaohongshu-lifestyle

**Before:** 这个产品很好用，推荐给大家。

**After:** 姐妹们冲！这真的是我今年用过最丝滑的[产品名]了✨ 之前用 [竞品] 总是卡顿，换了之后效率直接拉满。唯一的缺点是价格有点贵，但是用下来真的很值。

(注：小红书风格需要 emoji + 真实感 + 适度「自来水」语气。)

### I.5 Intensity: strict_precision, channel: research-precise

**Before:** 大约 80% 的中国用户都喜欢这个品牌。

**After:** 根据 [来源 / 调查名称] 2025 年的数据，约 80% 的受访用户表示偏好该品牌（样本量 n=1,200，置信区间 95%）。该结果仅适用于 [年龄段 / 城市] 子样本。

(注：strict_precision 要求标注来源、样本、置信区间，不做主观概括。)

(余下 20 条范例放 QUALITY_CHECKLIST.md Layer 2 与本节末;完整列表太长，此处只列 5 条代表性范例，每条 channel 都覆盖。)

## K. Safety boundaries

This locale pack **does not**:

- 声称能绕过 AI 检测、删除水印、或证明文章由人类撰写。这些都是错误的目标，本层不承诺也不尝试。
- 取代 `zh-TW`；台湾读者应使用 `zh-TW` 而不是简体改写。
- 在用户未要求时主动把金额、日期、单位转成简体形式。

This locale pack **does**:

- 在用户授权下，改善清晰度、自然度、语气。
- 保护所有受保护内容（参考 D 部分）。
- 在政治、监管、合规话题上默认使用中性、事实性表达。

## L. Reference files

- [TERM glossary.md](TERM_GLOSSARY.md) — 100+ 条大陆术语 vs 港澳台术语对照。
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — 10 个 style profile。
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — 双层品质检查表。
- [../zh-TW/WRITING_RULES.md](../zh-TW/WRITING_RULES.md) — `zh-TW` 参考实现。
- [../README.md](../README.md) — locale 架构总览。
- [../zh-TW/TERM_GLOSSARY.md](../zh-TW/TERM_GLOSSARY.md) — `zh-TW` 术语表，作为反向参考。

## M. Citations

Editorial principles借鉴自 `zh-TW` 参考实现。中文 AI-pattern 减少借鉴自：

- `kevintsai1202/Humanizer-zh-TW`（仅编辑原则借鉴；不延伸到大陸以外的華語區）。
- `op7418/Humanizer-zh`、`LifelongLazyLearner/qu-ai-wei`（zh-CN 編輯原則借鉴）。
- `devswha/patina`（多語言 editorial 原則参考）。
- `blader/humanizer` (English editorial rules).

这些都不是反 AI 检测工具；详见 [../research/HUMANIZER_REFERENCES.md](../research/HUMANIZER_REFERENCES.md)。