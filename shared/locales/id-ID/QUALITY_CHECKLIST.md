# Quality Checklist — `id-ID` (Indonesian — Indonesia)

> Source-of-truth file for the `id-ID` quality checklist. Lives under
> `shared/locales/id-ID/` per the architecture in
> [`../README.md`](../README.md).

The `id-ID` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list.
- **Layer 2** — a human-readable editorial review checklist.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output. Block on any failure.

1. **PUEBI spelling**: official 2015 spelling rules applied; no
   pre-2015 EYD hyphens (e.g. `memakai` not `memakai`).
2. **Register 一貫性**: formal (Anda / kami) vs informal (kamu / kita)
   not mixed mid-document.
3. **Punctuation**: full-width `,` `.`; sentence-ending period
   mandatory.
4. **Quotes**: `" "` for direct speech; inline emphasis.
5. **Spacing**: no space between Indonesian words and punctuation;
   space between Indonesian and English.
6. **Loanwords**: English tech terms used per established forms;
   brand names stay English.
7. **Honorifics**: Bapak / Ibu for polite; Saudara for gender-neutral
   formal.
8. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
9. **Channel voice**: profile matches channel.
10. **AI-pattern reduction**:
    - No 「dengan ini kami memberitahukan」 excessive formality.
    - No 「sangat」「amat」「sekali」 excessive intensifiers.
    - No 「demikianlah」 / 「akhir kata」 letter closing clichés.
11. **Editing intensity**: matches workflow declaration; legal /
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

- [ ] **Channel voice**: matches platform (WhatsApp vs Instagram vs
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
- [ ] **Privacy**: UU PDP (Undang-Undang Perlindungan Data Pribadi)
      compliance for personal data references.

### Output format

- [ ] **Format matches channel**: email subject + body + sign-off.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When publishing-grade, run 3+ before/after checks:

1. **Register consistency**:
   - Before: `Anda` in one paragraph, `kamu` in the next.
   - After: consistent formal `Anda` throughout.
2. **AI-pattern reduction**:
   - Before: 「dengan ini kami memberitahukan」「sangat sekali」
     formality / intensifier stacking.
   - After: rewrite to direct phrasing.
3. **PUEBI spelling**:
   - Before: `memakai` (old EYD hyphen).
   - After: `memakai` (PUEBI).

## How to apply

- **Layer 1** runs every turn.
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated,
  - the operator requests it.

## When to return partial output

Return partial output (with a short note) when:

- it cannot fully verify a fact claim — return with `[perlu verifikasi]`
  markers;
- the user requested a conflicting channel — return one channel's
  version and note the conflict;
- the editing intensity auto-escalates — explain in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable mixes formal `Anda` with informal `kamu` in the
   same document.
2. The deliverable uses pre-2015 EYD hyphens — PUEBI compliance broken.
3. The deliverable claims a percentage without source or sample size.
4. The deliverable uses 「akhir kata」 / 「demikianlah」 letter
   closing clichés in modern business email.
5. The deliverable uses `Rp 100000` (no separator) for currency
   amounts — should be `Rp 100.000` per Indonesian convention.