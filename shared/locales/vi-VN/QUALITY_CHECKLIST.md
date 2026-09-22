# Quality Checklist — `vi-VN` (Vietnamese — Vietnam)

> Source-of-truth file for the `vi-VN` quality checklist. Lives under
> `shared/locales/vi-VN/` per the architecture in
> [`../README.md`](../README.md).

The `vi-VN` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list.
- **Layer 2** — a human-readable editorial review checklist.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output. Block on any failure.

1. **Diacritics**: full diacritics throughout (except for established
   brand names without diacritics, e.g. "Vinamilk", "Viettel").
2. **Pronouns**: appropriate family-based pronoun (Anh / Chị / Bác /
   Cô / Ông / Bà).
3. **Register 一貫性**: formal vs informal pronoun not mixed
   mid-document.
4. **Punctuation**: full-width `,` `.`; sentence-ending period
   mandatory.
5. **Spacing**: no space between Vietnamese words and punctuation;
   space between Vietnamese and English.
6. **Loanwords**: English tech terms used per established forms;
   brand names stay English.
7. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
8. **Channel voice**: profile matches channel.
9. **AI-pattern reduction**:
   - No 「chúng tôi xin thông báo」 / 「xin được phép」 excessive
     formality.
   - No 「rất」「cực kỳ」「vô cùng」 excessive intensifiers.
   - No 「kính thư」 formal letter cliché in modern email.
   - No mixed formal / informal pronouns in same document.
10. **Editing intensity**: matches workflow declaration; legal /
    medical / financial / security / compliance uses `strict_precision`.

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables.

### Structure & clarity

- [ ] **Core message visible**: takeaway in title / opening sentence.
- [ ] **Paragraph logic**: smooth transitions.
- [ ] **Heading hierarchy**: H2 / H3 / H4 consistent.
- [ ] **List format**: numbered or bulleted consistently.
- [ ] **Citations**: every data point has a source.

### Language & tone

- [ ] **Channel voice**: matches platform (Zalo vs Facebook vs
      Email vs LinkedIn).
- [ ] **Register**: appropriate for the channel and recipient.
- [ ] **No machine tells**: avoids excessive formality, intensifier
      overuse, formulaic openers.
- [ ] **Loanword consistency**: English terms used consistently.

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
      include required disclosures.
- [ ] **Brand / trademark**: brand names not altered.
- [ ] **Privacy**: Nghị định 13/2023/NĐ-CP (Vietnamese Personal Data
      Protection Decree) compliance for personal data references.

### Output format

- [ ] **Format matches channel**: email subject + body + sign-off.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When publishing-grade, run 3+ before/after checks:

1. **Diacritics**:
   - Before: "VN" or "Viet Nam" without diacritics.
   - After: "Việt Nam" with full diacritics.
2. **AI-pattern reduction**:
   - Before: 「chúng tôi xin thông báo」「rất」 formality / intensifier
     stacking.
   - After: rewrite to direct phrasing.
3. **Register consistency**:
   - Before: mixed "Anh/Chị" with "tôi" / "bạn" in same document.
   - After: consistent pronoun choice throughout.

## How to apply

- **Layer 1** runs every turn.
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated,
  - the operator requests it.

## When to return partial output

Return partial output (with a short note) when:

- it cannot fully verify a fact claim — return with `[cần xác minh]`
  markers;
- the user requested a conflicting channel — return one channel's
  version and note the conflict;
- the editing intensity auto-escalates — explain in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable omits diacritics in formal / professional content
   — PUEBI-equivalent compliance broken.
2. The deliverable uses casual pronouns (bạn / mình) in formal
   business email — register broken.
3. The deliverable claims a percentage without source or sample size.
4. The deliverable uses 「kính thư」 / 「xin được phép」 formal letter
   clichés in modern email context.
5. The deliverable uses 「chúng ta」 (we inclusive) in a business
   letter where 「chúng tôi」 (we exclusive) is correct.