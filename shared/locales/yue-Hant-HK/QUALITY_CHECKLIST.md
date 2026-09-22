# Quality Checklist — `yue-Hant-HK` (Traditional Chinese — Hong Kong)

> Source-of-truth file for the `yue-Hant-HK` quality checklist. Lives
> under `shared/locales/yue-Hant-HK/` per the architecture in
> [`../README.md`](../README.md).

The `yue-Hant-HK` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list the AI should run on
  every protected-spans-respecting draft.
- **Layer 2** — a human-readable editorial review checklist for the
  operator to apply when the deliverable is high-stakes (publishing,
  regulated content, customer-facing).

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output to the user. Block on any failure.

1. **字符**：輸出是繁體中文（HK variant）。除非引用原文，不混入簡體字。
2. **術語**：參考 [TERM_GLOSSARY.md](TERM_GLOSSARY.md)；HK 偏好形式已
   採用；用戶已登記術語未覆蓋。
3. **Cantonese 口語**：僅在 casual / colloquial channel 使用；formal
   channel 沒有 Cantonese 口語。
4. **Bilingual mixing**：中英夾雜時空格一致；formal channel 偏好
   monolingual。
5. **受保護內容**：代碼、ID、URL、品牌名、引用、數字、單位、貨幣、日期
   未被改寫。
6. **標點**：全形中文標點；中英之間留空格；段落開頭不寫空格。
7. **AI-pattern reduction**：
   - 不連續三個相似結構句子。
   - 無「綜上所述」「非常感謝」「希望對您有所幫助」等程式化表達。
   - 無 Cantonese 口語混入 formal channel。
8. **政治 / 監管敏感表達**：使用中性、實質性表述；不主動涉入中港台政治
   議題（除非用戶明確要求）。
9. **頻道匹配**：所選 style profile 與目標頻道一致。
10. **編輯強度匹配**：`editing_intensity` 與 workflow 前置聲明一致；法
    律 / 醫療 / 金融 / 安全 / 合規內容使用 `strict_precision`。

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables. Each item has a
severity.

### Structure & clarity

- [ ] **核心信息一句話可見**：讀者掃一眼標題 / 首段能看出本文要解決的問題。
- [ ] **段落邏輯連貫**：段間過渡自然，不突然跳主題。
- [ ] **小標題層級一致**：H2 / H3 / H4 不混用。
- [ ] **列點格式統一**：要么全用「1.」，要么全用「-」，不混用。
- [ ] **引用 / 數據可追溯**：所有數據點都有來源或標注「數據來源待確認」。

### Language & tone

- [ ] **頻道聲音一致**：語氣與目標平台匹配（WhatsApp vs Facebook vs
      LinkedIn vs legal document）。
- [ ] **Cantonese 口語使用得當**：casual channel 有口語；formal channel 沒
      有口語。
- [ ] **Bilingual 混合一致**：如果 source 混合，output 也混合；如果 source
      monolingual，output 也 monolingual。
- [ ] **避免機器味**：沒有明顯的「AI 寫」標誌（三段式排比、空洞總結、
      程式化開頭結尾）。
- [ ] **術語一致**：同一概念在全文用同一表達，不混用。

### Audience fit

- [ ] **預設讀者畫像準確**：能告訴我是寫給誰的（年齡、城市、行業、消費偏好）。
- [ ] **讀者能採取具體動作**：結尾有明確的「下一步」。
- [ ] **不冒犯目標讀者**：避免刻板印象、政治敏感、地域歧視。

### Compliance & safety

- [ ] **無 AI 檢測繞過聲明**：本文未聲稱「繞過 AI 檢測」「刪除浮水印」「證明人類撰寫」。
- [ ] **監管 / 合規表述準確**：醫療效果、金融承諾、療效聲稱等場景有合規表述。
- [ ] **品牌 / 商標保護**：品牌名、商標、產品名未做非授權改寫。
- [ ] **HK 法律參照準確**：法律文件引用的法例章節、條文編號準確。

### Output format

- [ ] **格式與 channel 匹配**：WhatsApp 短訊、Facebook 長文、LinkedIn 專
      業、legal 嚴謹。
- [ ] **圖片 / 視頻位標注**：需要素材的地方明確標注「[此處插圖]」。
- [ ] **CTA 明確**：銷售 / 轉化場景有清晰行動召喚。

### Before-and-after spot checks (high-stakes)

When the deliverable is publishing-grade, run 3+ before/after checks:

1. **Cantonese 口語使用得當**：
   - Before: 正式 legal 文件含「我哋」「搞掂」 — fail。
   - After: 改成「本公司」「完成」。
2. **術語翻轉**：
   - Before: 「這套 software 很好用」 — 混用語境。
   - After (HK email): 「這套軟件很好用」 — 統一使用 HK 形式。
3. **Bilingual 混合**：
   - Before: WhatsApp 訊息純中文（不自然）。
   - After: 「記得 check 吓個 file，send 俾我」 — 自然 HK 風格。

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

- it cannot fully verify a fact claim (Layer 2 數據可追溯 fails) — return
  the deliverable with `[待核實]` markers;
- the user explicitly requested a deliverable in a conflicting channel
  (e.g. asked for a legal document but in WhatsApp voice) — return a
  single channel's version and note the conflict;
- the editing intensity escalates automatically (e.g. workflow default is
  `standard` but the content is regulated) — explain the auto-escalation
  in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable switches between Traditional and Simplified
   characters mid-paragraph — implies the locale layer failed to load.
2. The deliverable uses Cantonese 口語 in a B2B email — wrong channel
   voice.
3. The deliverable claims a percentage or ranking without a source —
   even for friendly-professional contexts.
4. The deliverate translates a brand name (e.g. 「蘋果公司」 for
   Apple) — brand names stay as-is.
5. The deliverate mixes `zh-TW` style references (台灣用語) when the
   audience is HK — HK has different IT vocabulary than Taiwan.