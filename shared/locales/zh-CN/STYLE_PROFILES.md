# Style Profiles — Simplified Chinese (`zh-CN`, Mainland China)

> Source-of-truth file for the `zh-CN` style profiles. Lives under `shared/locales/zh-CN/` per the architecture in [`../README.md`](../README.md).

Ten style profiles cover the canonical channels for Mainland Chinese. Each
profile is a fixed schema: name, channel, second-person policy, formality,
sensitivity, punctuation notes, common pitfalls, and an exemplar phrase.

## How to choose a profile

The router picks based on the workflow's `category`, the requested output
`channel`, the audience, and the editing intensity. See "How to choose a
profile" at the bottom of this file.

## Schema

Each profile below uses this schema:

- **Code**: identifier used in workflow frontmatter and harness output.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: which audience this profile is for.
- **`punctuation_notes`**: spacing, marks, and conventions specific to this
  profile.
- **`common_pitfalls`**: patterns the layer avoids in this profile.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `zh-cn-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: 「你」or「您」 depending on formality; default 「你」
  for neutral, 「您」 for customer-facing or formal B2G.
- **`formality`**: medium.
- **`locale`**: Mainland China.
- **`punctuation_notes`**: 全角中文标点；中英数字之间留空格；段落开头不写
  空格。
- **`common_pitfalls`**:
  - 「亲爱的用户」等过度客套。
  - 「非常好」「非常不错」等空洞修饰。
  - 「希望对您有所帮助」等程式化结尾。
- **`exemplar`**: 我们正在筹备暑期活动，预计参加人数 60 人左右，想优化
  一下报到流程。

## 2. `zh-cn-business-consulting`

- **Channel**: 战略文档、商业顾问报告、内部决策备忘录。
- **`second_person`**: 不直接称呼读者；「我们」「团队」「公司」为主。
- **`formality`**: high.
- **`locale`**: Mainland China business audience.
- **`punctuation_notes`**: 全角中文标点；列点用「1.」「2.」而非「-」；
  强调用粗体或「**」不滥用。
- **`common_pitfalls`**:
  - 「赋能」「抓手」「闭环」等空泛流行语堆砌。
  - 「我们认为…我们建议…」过度主观。
  - 数据不标来源。
- **`exemplar`**: 根据 2025 年公开财报与第三方调研，该业务在大陆市场的
  复购率约为 38%，低于行业均值（45%）。建议在 Q 4 调整定价梯度并加强
  留存运营。

## 3. `zh-cn-thought-leadership`

- **Channel**: 微信公众号 长文 / 知乎专栏 / 行业洞察报告。
- **`second_person`**: 「你」 直接称呼；偶尔「我们」表共同立场。
- **`formality`**: medium-high.
- **`locale`**: Mainland China professional / executive readers.
- **`punctuation_notes`**: 段落清晰；小标题用「一、」「二、」或粗体；引用
  用「」或引用块；不滥用 emoji。
- **`common_pitfalls`**:
  - 「内卷」「躺平」等流行语作为论证基础（应作为现象描述，不作为论点）。
  - 学术化堆砌但无原创洞察。
  - 标题党 + 正文无实质。
- **`exemplar`**: 过去三年，AI 把内容生产的边际成本压到了接近零。但成本
  的下降不意味着价值的下沉；相反，读者对「低成本内容」的容忍度正在快速
  降低。这一变化，决定了未来一年内容从业者的分水岭。

## 4. `zh-cn-weibo-casual`

- **Channel**: 微博 短贴。
- **`second_person`**: 「你」 「我」 「姐妹们」 「兄弟们」 等口语化称呼。
- **`formality`**: low.
- **`locale`**: Mainland China general public.
- **`punctuation_notes`**: 短句；emoji 适度（每段不超过 2-3 个）；话题标签
  用 `#xxx#` 而非英文 `#xxx`。
- **`common_pitfalls`**:
  - 过度营销口吻。
  - 长段落（微博字数限制 2000，但读者注意力 ≤ 140 字）。
  - 立场化措辞导致封号风险。
- **`exemplar`**: 今天北京下雪了🌨️ 出门第一件事就是找咖啡☕ 姐妹们有没有
  同款仪式感？#我的冬日续命清单# #城市生活#

## 5. `zh-cn-xiaohongshu-lifestyle`

- **Channel**: 小红书笔记。
- **`second_person`**: 「姐妹们」「家人们」「宝宝们」 直接对话感。
- **`formality`**: low.
- **`locale`**: Mainland China lifestyle audience (predominantly female,
  18-40).
- **`punctuation_notes`**: 标题通常含 emoji；正文 300–800 字；段落短；
  关键词加粗（如品牌名）。
- **`common_pitfalls`**:
  - 过度标题党（「震惊！」「必看！」）。
  - 假测评（编造的使用感）。
  - 商业导流违反平台规则（笔记里贴二维码、外链）。
- **`exemplar`**: 姐妹们冲！这个[品牌]真的是今年秋冬的本命🧡 我之前一直用
  [竞品]，但是[痛点]真的劝退。换了这个之后[具体改变]✨ 唯一的缺点是价格
  有点贵，但是[正向价值]。真心推荐给[目标人群]～

## 6. `zh-cn-douyin-script`

- **Channel**: 抖音 短视频脚本。
- **`second_person`**: 「你」 直接对话；旁白用「他/她」第三人。
- **`formality`**: low.
- **`locale`**: Mainland China general short-video audience.
- **`punctuation_notes`**: 时间轴标注（0-3s / 3-8s / ...）；分镜清楚；
  字幕与画外音分开标注。
- **`common_pitfalls`**:
  - 前 3 秒没钩子（完播率低）。
  - 节奏过慢或信息密度过高。
  - 涉及敏感词、平台违禁内容（医疗效果、金融承诺等）。
- **`exemplar`**:
  ```text
  [0-3s 钩子]
  画面：主角拿起产品特写
  旁白：「这个东西我只用了 7 天，但是…」

  [3-10s 痛点]
  画面：使用前后对比
  旁白：「之前 [痛点描述]，现在 [效果描述]」

  [10-25s 细节]
  ...

  [25-30s CTA]
  画面：产品链接
  字幕：「点击购物车看看，姐妹们冲！」
  ```

## 7. `zh-cn-bilibili-script`

- **Channel**: 哔哩哔哩 中长视频脚本 / 知识区 / 测评区。
- **`second_person`**: 「大家」「各位观众」 中性称呼。
- **`formality`**: medium.
- **`locale`**: Mainland China knowledge / interest audience.
- **`punctuation_notes`**: 时间轴 + 章节标题（如「00:30 开箱」）；适度
  弹幕梗（「下次一定」「AWSL」）；不用滥用。
- **`common_pitfalls`**:
  - 念稿感太强（缺乏互动）。
  - 知识点错误（知识区观众敏感）。
  - 商业内容未明确标注。
- **`exemplar`**: 今天给大家带来 [产品/话题] 的深度测评。我们会从
  [维度1]、[维度2]、[维度3] 三个角度来分析。如果你也在纠结要不要
  [行动]，那这期视频一定要看完。

## 8. `zh-cn-email-professional`

- **Channel**: 商务邮件、客户沟通、内部通知。
- **`second_person`**: 「您」 默认；收件人为平级或上级时使用。
- **`formality`**: high.
- **`locale`**: Mainland China business / institutional audience.
- **`punctuation_notes`**: 称呼顶格；正文段落清晰；结尾敬语规范；签名
  块完整。
- **`common_pitfalls`**:
  - 「亲爱的」「您好！」 在正式邮件中过度使用。
  - 段落堆砌无分段。
  - 结尾无具体动作（请对方做什么、何时回复）。
- **`exemplar`**:
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

## 9. `zh-cn-landing-page-clear`

- **Channel**: 落地页 / 销售页 / 增长页。
- **`second_person`**: 「你」 直接对话；「我们」 表公司立场。
- **`formality`**: medium.
- **`locale`**: Mainland China conversion-oriented readers.
- **`punctuation_notes`**: 标题大字号；段落短；CTA 按钮清晰；证据块
  （数字、用户证言）独立呈现。
- **`common_pitfalls`**:
  - 「颠覆」「革命」 等夸张词。
  - 缺少证据（只喊口号）。
  - CTA 不明确（「了解更多」不如「立即领取 7 天试用」）。
- **`exemplar`**:
  ```text
  [标题]
  30 天，让你的内容生产效率翻倍。

  [副标题]
  AI 帮你把 80% 的重复工作自动化，让你专注真正重要的创意。

  [痛点 → 方案 → 证据 → CTA]
  ...

  [CTA 按钮]
  立即免费试用 →

  [社会证据]
  已有 12,000+ 团队在使用。
  ```

## 10. `zh-cn-customer-support`

- **Channel**: 客服回复、售后沟通、退换货处理。
- **`second_person`**: 「您」 必须；体现尊重。
- **`formality`**: medium.
- **`locale`**: Mainland China customer-facing audience.
- **`punctuation_notes`**: 共情段（一句）；解释段（一到两句）；行动段
  （明确步骤）；结尾一句问询是否解决。
- **`common_pitfalls`**:
  - 程式化开头（「非常感谢您的反馈」）。
  - 推卸责任。
  - 没有具体动作让用户执行。
- **`exemplar`**:
  ```text
  您好，

  非常抱歉给您带来了不好的体验。关于您提到的 [问题]，我们已经记录并
  提交到相关部门。根据我们的售后政策，这种情况可以为您 [解决方案]。

  请您方便时回复订单号，我们会在 24 小时内为您处理。

  再次为带来的不便道歉。请问还有其他可以帮您的吗？
  ```

---

## How to choose a profile

Decision table (used by the router):

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general professional | `zh-cn-friendly-professional` |
| content | 公众号 / 知乎 | `zh-cn-thought-leadership` |
| content | 微博 | `zh-cn-weibo-casual` |
| content | 小红书 | `zh-cn-xiaohongshu-lifestyle` |
| content | 抖音脚本 | `zh-cn-douyin-script` |
| content | B 站脚本 | `zh-cn-bilibili-script` |
| business | general strategy | `zh-cn-business-consulting` |
| business | sales / landing page | `zh-cn-landing-page-clear` |
| business | email outreach | `zh-cn-email-professional` |
| research | research report | `zh-cn-business-consulting` or `zh-cn-thought-leadership` |
| workflow | SOP / docs | `zh-cn-friendly-professional` |
| technical | technical writing | `zh-cn-friendly-professional` |
| any | customer support | `zh-cn-customer-support` |

User's explicit channel hint always overrides the default. Workflows may
also declare a `localization.default_style_profile` in their frontmatter;
that takes precedence over the category default but yields to explicit
channel hints.