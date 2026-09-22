# Quality Checklist — `ja-JP` (Japanese — Japan)

> Source-of-truth file for the `ja-JP` quality checklist. Lives under
> `shared/locales/ja-JP/` per the architecture in
> [`../README.md`](../README.md).

The `ja-JP` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list.
- **Layer 2** — a human-readable editorial review checklist.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output. Block on any failure.

1. **Keigo 一貫性**: 敬語 levels don't mix mid-document. If opener is
   拝啓, closer must be 敬具 and body uses 謙譲語 / 丁寧語.
2. **句読点**: 全角 comma `、`and period `。`; sentence-ending period
   mandatory.
3. **Quotes**: 「」 for primary; 『』 for nested.
4. **Spacing**: no space between Japanese characters and punctuation;
   ASCII space between Japanese and English.
5. **Loanwords**: English terms transliterated per established
   katakana forms; brand names stay English.
6. **Honorifics**: さん for polite, 様 for formal; くん / ちゃん only
   in casual / familiar contexts.
7. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
8. **Channel voice**: profile matches channel.
9. **AI-pattern reduction**:
   - No 「〜と思われます」「〜と言えるでしょう」 hedge stacking.
   - No 「非常に」「大変」 excessive intensifiers.
   - No 「お忙しいところ」 formal letter cliché leaking into casual.
   - No mixed です/ます with だ/である in same document.
10. **Editing intensity**: matches workflow declaration; legal /
    medical / financial / security / compliance uses `strict_precision`.

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables.

### Structure & clarity

- [ ] **Core message visible**: takeaway in title / opening sentence.
- [ ] **Paragraph logic**: smooth transitions, no abrupt topic shifts.
- [ ] **Heading hierarchy**: H2 / H3 / H4 consistent.
- [ ] **List format**: numbered (一二三) or bulleted consistent.
- [ ] **Citations**: every data point has a source.

### Language & tone

- [ ] **Channel voice**: matches platform (formal email vs LINE vs
      note.com).
- [ ] **Keigo level**: appropriate for the channel and recipient.
- [ ] **No machine tells**: avoids excessive hedge stacking,
      intensifier overuse, formulaic openers.
- [ ] **Loanword consistency**: English terms used consistently
      (katakana or English, not mixed).

### Audience fit

- [ ] **Reader profile**: writer can describe who they are writing
      for (industry / role / seniority).
- [ ] **Reader action**: closing provides a clear next step.
- [ ] **No offense**: avoids stereotypes, regional bias, political
      bias.

### Compliance & safety

- [ ] **No detection-bypass claims**: text does not claim
      "undetectable", "human-proof", "watermark-free".
- [ ] **Regulatory accuracy**: medical, financial, efficacy claims
      include required disclosures (e.g. 金融商品取引法 for finance).
- [ ] **Brand / trademark**: brand names not altered.
- [ ] **Privacy**: 個人情報保護法 compliance for personal data
      references.

### Output format

- [ ] **Format matches channel**: email subject + body + sign-off;
      formal document with proper opening / closing.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When publishing-grade, run 3+ before/after checks:

1. **Keigo level**:
   - Before: mixed です/ます with だ/である in same email.
   - After: consistent register throughout.
2. **AI-pattern reduction**:
   - Before: 「〜と思われます」「〜と言えるでしょう」「非常に」
     hedge / intensifier stacking.
   - After: rewrite to direct phrasing.
3. **Loanword consistency**:
   - Before: GitHub / ギットハブ mixing in same document.
   - After: pick one form and use consistently.

## How to apply

- **Layer 1** runs every turn.
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated,
  - the operator requests it.

## When to return partial output

Return partial output (with a short note) when:

- it cannot fully verify a fact claim — return with `[要確認]`
  markers;
- the user requested a conflicting channel — return one channel's
  version and note the conflict;
- the editing intensity auto-escalates — explain in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable mixes です/ます with だ/である mid-document —
   keigo level broken.
2. The deliverable opens with 拝啓 but closes without 敬具 — formal
   letter convention broken.
3. The deliverable claims a percentage without source or sample size
   — research / statistics discipline broken.
4. The deliverable uses 「お忙しいところ」 in a casual chat — formal
   letter cliché leakage.
5. The deliverable uses くん / ちゃん for a non-familiar recipient —
   register / relationship inappropriate.