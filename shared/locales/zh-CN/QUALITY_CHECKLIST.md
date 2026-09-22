# Quality Checklist — Simplified Chinese (`zh-CN`, Mainland China)

> Source-of-truth file for the `zh-CN` quality checklist. Lives under `shared/locales/zh-CN/` per the architecture in [`../README.md`](../README.md).

The `zh-CN` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list the AI should run on every
  protected-spans-respecting draft.
- **Layer 2** — a human-readable editorial review checklist for the operator
  to apply when the deliverable is high-stakes (publishing, regulated
  content, customer-facing).

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2 has no
blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output to the user. Block on any failure.

1. **字符**：输出是简体中文。除非引用原文，否则不夹繁体字。
2. **术语**：参考 [TERM_GLOSSARY.md](TERM_GLOSSARY.md)；台湾 / 港澳词已
   替换为大陆词；用户已登记的术语未覆盖。
3. **受保护内容**：代码、ID、URL、品牌名、引用、数字、单位、货币、日期
   未被改写。
4. **标点**：全角中文标点；中英数字之间留空格；不出现半角中英夹杂。
5. **段落**：段落开头不写空格；标题层级清晰；列点格式统一。
6. **AI-pattern reduction**：
   - 不连续三个相似结构句子。
   - 无「综上所述」「非常感谢」「希望对您有所帮助」等程式化表达。
   - 无「赋能 / 抓手 / 闭环」等空泛流行语堆砌（除非用户或场景明确要求）。
7. **政治 / 监管敏感表达**：默认中性事实性表述；不主动写未经证实的数据。
8. **频道匹配**：所选 style profile 与目标频道一致。
9. **编辑强度匹配**：`editing_intensity` 与 workflow 前置声明一致；
   法律 / 医疗 / 金融 / 安全 / 合规内容使用 `strict_precision`。
10. **语言边界**：当用户最终交付物是英文 / 日文 / 韩文等非中文语言时，
    `zh-CN` 层完全不加载。

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables. Each item has a severity.

### Structure & clarity

- [ ] **核心信息一句话可见**：读者扫一眼标题 / 首段能看出本文要解决的问题。
- [ ] **段落逻辑连贯**：段间过渡自然，不突然跳主题。
- [ ] **小标题层级一致**：H2 / H3 / H4 不混用。
- [ ] **列点格式统一**：要么全用「1.」，要么全用「-」，不混用。
- [ ] **引用 / 数据可追溯**：所有数据点都有来源或标注「数据来源待确认」。

### Language & tone

- [ ] **频道声音一致**：语气与目标平台匹配（公众号 vs 小红书 vs B 站）。
- [ ] **避免机器味**：没有明显的「AI 写」标志（三段式排比、空洞总结、
      程式化开头结尾）。
- [ ] **术语一致**：同一概念在全文用同一表达，不混用。
- [ ] **口语 / 书面匹配**：场景需要口语时保留自然感；正式场景替换为书面表达。

### Audience fit

- [ ] **预设读者画像准确**：能告诉我是写给谁的（年龄、城市、职业、消费偏好）。
- [ ] **读者能采取具体动作**：结尾有明确的「下一步」。
- [ ] **不冒犯目标读者**：避免刻板印象、政治敏感、地域歧视。

### Compliance & safety

- [ ] **无 AI 检测绕过声明**：本文未声称「绕过 AI 检测」「删除水印」「证明人类撰写」。
- [ ] **监管 / 合规表述准确**：医疗效果、金融承诺、疗效声称等场景有合规表述。
- [ ] **品牌 / 商标保护**：品牌名、商标、产品名未做非授权改写。

### Output format

- [ ] **格式与 channel 匹配**：公众号长文 / 微博短文 / 小红书 emoji 等。
- [ ] **图片 / 视频位标注**：需要素材的地方明确标注「[此处插图]」。
- [ ] **CTA 明确**：销售 / 转化场景有清晰行动召唤。

### Before-and-after spot checks (high-stakes)

When the deliverable is publishing-grade, run 3+ before/after checks:

1. **AI-pattern reduction**:
   - Before: 「首先…其次…再次…最后…」
   - After: 按重要性或逻辑顺序重排，移除机械连接词。
2. **Terminology flip**:
   - Before: 「這個軟件超好用」
   - After: 「这个软件非常好用」（大陆词 + 简体 + 标点修正）。
3. **Channel voice**:
   - Before: 「本报告分析了 XX 的市场表现，认为…」 （公文化）
   - After (for 公众号 / 知乎): 「我们看了 XX 在大陆的市场表现，发现…」 （更接近思考者口吻）。

## How to apply

- **Layer 1** runs every turn (the AI applies it before showing output).
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated (legal, medical, financial, security),
  - the operator requests it (e.g. before publishing).
- A deliverable is **acceptable** when Layer 1 is 100% AND Layer 2 has no
  blocking failure (most Layer 2 items are advisory, not blocking).

## When to return partial output

The AI should return partial output (with a short note) when:

- it cannot fully verify a fact claim (Layer 2 数据可追溯 fails) — return the
  deliverable with `[待核实]` markers;
- the user explicitly requested a deliverable in a conflicting channel
  (e.g. asked for a 公眾號 article but in 微博 voice) — return a single
  channel's version and note the conflict;
- the editing intensity escalates automatically (e.g. workflow default is
  `standard` but the content is regulated) — explain the auto-escalation in
  one line.

---

## Layer 2 extended before-and-after examples

(精选 5 条代表性范例。每条 channel 都覆盖，全套范例参考
[WRITING_RULES.md](WRITING_RULES.md) 的 Section I。)

### E.1 friendly-professional

- **Before**: 「希望您能喜欢这个产品。」
- **After**: 「我们觉得你可以试试这个产品；如果有任何问题，随时告诉我们。」

### E.2 business-consulting

- **Before**: 「我们觉得这个方案非常好，可以颠覆市场。」
- **After**: 「根据 2024-2025 年的市场数据，该方案在 [细分市场] 有 30%
  的成本优势。建议在 Q1 先做小范围试点，验证转化率后再扩大。」

### E.3 weibo-casual

- **Before**: 「今天天气真好，我决定出门走走。大家也一起吧。」
- **After**: 「北京今天终于放晴了☀️ 出门遛弯走起～姐妹们今天出门了吗？
  #我的周末日常#」

### E.4 xiaohongshu-lifestyle

- **Before**: 「这个品牌的护肤品我用了一段时间，效果不错。」
- **After**: 「姐妹们！这个[品牌]精华我已经空瓶 3 罐了🧴 之前肌肤状态
  很糟糕，[痛点]，[现在的状态]✨ 缺点是有点小贵，但[正向价值]～真心
  推荐！」

### E.5 customer-support

- **Before**: 「非常抱歉给您带来不便，我们会尽快处理。」
- **After**: 「您好，关于您反馈的 [具体问题]，我们已经记录。请您方便时
  发送订单号，我们会在 24 小时内为您处理。再次为带来的不便道歉。」

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable switches between Simplified and Traditional characters
   mid-paragraph — implies the locale layer failed to load.
2. The deliverable uses 「亲」 「家人们」 「姐妹们」 in a B2B email — wrong
   channel voice.
3. The deliverable claims a percentage or ranking without a source — even
   for friendly-professional contexts.
4. The deliverable translates a brand name (e.g. 「苹果公司」 for Apple) —
   brand names stay as-is.
5. The deliverable uses 大陆简体但 with 港澳俚语 (e.g. 「食字」「搞掂」) —
   either go full 大陆 or full 港澳，不混用。