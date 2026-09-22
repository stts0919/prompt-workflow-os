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

(余下 20 条范例列在下方，覆盖每个 channel 与每个 intensity 等级。)

### I.6 Intensity: standard, channel: friendly-professional (introduction)

**Before:** 我们公司是做软件开发的。

**After:** 我们公司专注于软件开发。

(注：「是做 → 专注于」从陈述句升级为定位句，去掉「的」字让句子更干净。)

### I.7 Intensity: standard, channel: business-consulting (recommendation)

**Before:** 我们觉得这个方案非常好，可以颠覆市场。

**After:** 根据 2024–2025 年的市场数据，该方案在 [细分市场] 有 30% 的成本优势。建议在 Q1 先做小范围试点，验证转化率后再扩大。

(注：去掉「颠覆」夸张词；用「建议 + 试点」框架，给出可执行的下一步。)

### I.8 Intensity: standard, channel: thought-leadership (公众号 / 知乎)

**Before:** 内卷太严重了，大家都躺平了。

**After:** 过去三年，「内卷」从一个学术用语变成了日常吐槽。问题在于：当我们用「内卷」概括所有高强度竞争时，也抹平了其中真实存在的结构性差异。这一变化，决定了未来一年内容从业者必须重新定义自己的位置。

(注：thought-leadership 不堆叠流行语；用「变化 → 决定」句式建立论证深度。)

### I.9 Intensity: standard, channel: weibo-casual (happy tone)

**Before:** 今天天气真好，我决定出门走走。大家也一起吧。

**After:** 北京今天放晴了☀️ 出门遛弯走起～姐妹们今天出门了吗？#我的周末日常#

(注：微博受字数限制 + 需要话题标签；emoji 适度。)

### I.10 Intensity: standard, channel: weibo-casual (commentary)

**Before:** 现在的电视剧越来越难看了。

**After:** 最近的剧真的是剧越来越剧了……大家最近在追啥？求安利！

(注：保留「真的是剧」的口语化重复；用反问结尾引发评论。)

### I.11 Intensity: standard, channel: xiaohongshu-lifestyle (review)

**Before:** 这个品牌的护肤品我用了一段时间，效果不错。

**After:** 姐妹们！这个 [品牌] 精华我已经空瓶 3 罐了🧴 之前肌肤状态很糟糕，[痛点描述]，[现在的状态描述]✨ 缺点是有点小贵，但 [正向价值]。真心推荐给 [目标人群]～

(注：小红书风格需要 emoji + 真实感 + 适度「自来水」语气。)

### I.12 Intensity: standard, channel: xiaohongshu-lifestyle (tutorial)

**Before:** 教大家如何收纳衣柜。

**After:** 整理衣柜的姐妹看过来👀 我之前也是 [痛点]，后来试了这个 [方法/工具]，真的省了 60% 的空间！步骤很简单：1️⃣ [第一步] 2️⃣ [第二步] 3️⃣ [第三步]。赶紧试试吧～

(注：步骤用数字 emoji 视觉切分；结尾带行动召唤。)

### I.13 Intensity: standard, channel: douyin-script (15s hook)

**Before:** 介绍一款产品。

**After:**
```text
[0-3s 钩子]
画面：主角拿起产品特写
旁白：「这个东西我只用了 7 天，但是…」

[3-10s 痛点]
画面：使用前后对比
旁白：「之前 [痛点描述]，现在 [效果描述]」

[10-15s CTA]
画面：产品链接
字幕：「点击购物车看看，姐妹们冲！」
```

(注：抖音脚本前 3 秒钩子决定 70% 完播率；分镜必须清楚。)

### I.14 Intensity: standard, channel: douyin-script (30s educational)

**Before:** 解释一个概念。

**After:**
```text
[0-3s 钩子]
旁白：「99% 的人都搞错了 [概念]。」
画面：错误示范 + 大字「❌」

[3-10s 拆解]
旁白：「其实正确的理解是 [正确解释]。」
画面：正确示范 + 大字「✅」

[10-25s 细节]
旁白：[3 个具体要点]

[25-30s CTA]
旁白：「关注我，下集讲 [下一话题]。」
画面：关注按钮动画
```

(注：教育类抖音用「错误 → 正确 → 细节」三段式；CTA 引向下一集，提高账号粘性。)

### I.15 Intensity: standard, channel: bilibili-script (中长视频)

**Before:** 介绍一个新的开发工具。

**After:**
```text
00:00 开场
今天给大家带来 [工具名] 的深度测评。我们会从 [维度1]、[维度2]、[维度3] 三个角度来分析。

00:30 安装与上手
[具体安装步骤、配置要求]

06:00 核心功能实测
[具体功能、对比其他工具]

12:00 优缺点总结
[优点清单 + 缺点清单]

18:00 结论
如果你也在 [目标场景]，可以考虑入手。

视频内字幕：使用清晰的章节标题；弹幕梗适度（「AWSL」「下次一定」）。
```

(注：B 站用户对技术细节敏感；时长 5–20 分钟；必须明确告知结论。)

### I.16 Intensity: standard, channel: email-professional (商务邮件)

**Before:** 张总你好。我们的方案做好了。你看看。

**After:**
```text
张总：

您好。

关于 [项目] 的下一步安排，附件是我们的方案初稿。请您过目，如方便，
建议本周五（10 月 4 日）下午 3 点前电话沟通一次，确认落地节奏。

期待您的反馈。

王明
XX 公司
138-xxxx-xxxx
```

(注：商务邮件要求称呼得体、段落清晰、结尾具体动作。)

### I.17 Intensity: standard, channel: email-professional (内部通知)

**Before:** 大家好，明天开会。

**After:**
```text
各位：

明天（10 月 4 日 周三）下午 2 点在 3 楼会议室开 [会议主题]，预计 60 分钟。
议程：

1. [议题 1] — 负责人：[姓名]，30 分钟
2. [议题 2] — 负责人：[姓名]，20 分钟
3. Q&A

请提前阅读附件中的 [文档名]，并准备好相关数据。

谢谢。
[姓名]
```

(注：内部通知需要完整议程 + 负责人 + 时长，让收件人提前知道是否需要准备。)

### I.18 Intensity: standard, channel: landing-page-clear (SaaS 落地页)

**Before:** 我们做了一个软件，可以颠覆你的工作方式。

**After:**
```text
[标题]
30 天，让你的内容生产效率翻倍。

[副标题]
AI 帮你把 80% 的重复工作自动化，让你专注真正重要的创意。

[痛点]
- 每天花 3 小时手动整理素材
- 内容质量不稳定
- 跨平台分发耗时

[方案]
我们的工具用 AI 自动 [具体功能]，让你 [具体收益]。

[证据]
「用了 3 个月，我们的内容产出效率提高了 2.4 倍。」— XX 公司 内容主管
已有 12,000+ 团队在使用。

[CTA 按钮]
立即免费试用 →
```

(注：落地页禁止夸张词（「颠覆」「革命」），必须有具体证据和明确 CTA。)

### I.19 Intensity: standard, channel: landing-page-clear (B2C 落地页)

**Before:** 我们的产品很好，快来买。

**After:**
```text
[标题]
告别 [痛点场景描述]。

[副标题]
[产品名] 帮 [目标人群] 在 [使用场景] 中 [具体收益]。

[社会证据]
- 已有 50,000+ 用户
- 评分 4.8/5.0（基于 8,200 条评价）

[CTA 按钮]
限时 7 天试用，0 元 →
```

(注：B2C 落地页强调社会证据 + 低门槛试用；CTA 文案必须具体到动作 + 时限。)

### I.20 Intensity: standard, channel: customer-support (退款)

**Before:** 抱歉给您带来不便，我们会尽快处理。

**After:**
```text
您好，

关于您反馈的 [具体问题]，我们已经记录并提交到售后部门。
根据我们的售后政策，这种情况可以为您 [具体方案：全额退款 / 部分退款 / 换货]。

请您方便时回复订单号 [订单号格式示例]，我们会在 24 小时内为您处理。
再次为带来的不便道歉。请问还有其他可以帮您的吗？
```

(注：客服回复必须有共情 + 具体方案 + 具体动作；结尾问询是否还有其他问题。)

### I.21 Intensity: standard, channel: customer-support (产品咨询)

**Before:** 您好，您的问题我们已收到。

**After:**
```text
您好，

关于您咨询的 [产品功能]，具体说明如下：

- [要点 1]
- [要点 2]
- [要点 3]

如果您需要进一步演示，可以预约我们的产品顾问。时间：工作日 9:00–18:00。
预约链接：[链接]

请问还有其他问题吗？
```

(注：客服回复产品咨询要把要点列清楚 + 提供进一步行动；不要简单回复「已收到」。)

### I.22 Intensity: strict_precision, channel: research-precise (法规)

**Before:** 大多数情况下，我们的做法是合规的。

**After:** 根据 [法规名称] 第 [X] 条，[具体行为] 应 [具体要求]。本方案在 [具体条件] 下符合该条款的要求；若 [条件变化]，需 [后续动作]。本结论仅基于截至 2026 年 9 月 22 日可公开查阅的法规文本，法规更新需以最新文本为准。

(注：法规相关内容必须引用条款 + 说明适用范围 + 标注截止日期。)

### I.23 Intensity: strict_precision, channel: research-precise (投资)

**Before:** 这个投资产品的预期收益很高。

**After:**
- 历史年化收益率：2023 年 12.5%、2024 年 8.2%、2025 年 -1.3%。
- 过往业绩不预示未来表现。
- 主要风险：[风险 1]、[风险 2]、[风险 3]。
- 适合投资者画像：[流动性需求] / [风险承受等级] / [投资期限]。

(注：投资产品描述必须列历史数据 + 风险提示 + 投资者画像，禁止只讲收益。)

### I.24 Intensity: light, channel: friendly-professional (代码相关)

**Before:** 这个 bug 是因为没考虑并发情况。

**After:** 这个 bug 的根本原因是 [函数名] 在并发场景下未加锁。当 [触发条件] 时，多个 goroutine 会同时修改 [变量]，导致 [后果]。

修复方案：用 [锁类型] 保护临界区，参考 [文件路径:行号] 的现有用法。

(注：技术文档要求点明「根因 → 触发条件 → 后果 → 修复」四步。)

### I.25 Intensity: strict_precision, channel: business-consulting (战略)

**Before:** 我们应该进入东南亚市场。

**After:**
- **机会**：东南亚 6 国 2024 年总人口 6.7 亿，互联网用户 4.5 亿，电商市场年增长率 18%。
- **风险**：本地化成本高（语言 6 种、支付 4 种）、竞争激烈（Shopee / Lazada 已占主导）、法规差异大。
- **建议**：先以新加坡为试点（市场规模小但购买力高、监管清晰），验证产品适配度后再扩展。
- **下一步**：组建 3 人东南亚专班，Q4 完成市场调研，Q1 启动新加坡试点。

(注：战略建议必须分「机会 / 风险 / 建议 / 下一步」四块，禁止只给结论。)

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