# Quality Checklist — `ko-KR` (Korean — South Korea)

> Source-of-truth file for the `ko-KR` quality checklist. Lives under
> `shared/locales/ko-KR/` per the architecture in
> [`../README.md`](../README.md).

The `ko-KR` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list.
- **Layer 2** — a human-readable editorial review checklist.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output. Block on any failure.

1. **Register 一貫性**: 합쇼체 / 해요체 / 반말체 not mixed mid-document.
2. **Punctuation**: full-width `,` `.`; sentence-ending period
   mandatory.
3. **Quotes**: 「」 for primary; 『』 for nested.
4. **Spacing**: no space between Korean characters and punctuation;
   ASCII space between Korean and English.
5. **Loanwords**: English terms transliterated per established Hangul
   forms; brand names stay English.
6. **Honorifics**: 님 for polite, 씨 for peers; avoid ~さん (Japanese).
7. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
8. **Channel voice**: profile matches channel.
9. **AI-pattern reduction**:
   - No 「~라고 생각합니다」「~라고 할 수 있습니다」 hedge stacking.
   - No 「매우」「정말」「아주」 excessive intensifiers.
   - No 「바쁘신 중에」 formal letter cliché leaking into casual.
   - No mixed 합쇼체 / 해요체 / 반말체 in same document.
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

- [ ] **Channel voice**: matches platform (Naver blog vs KakaoTalk vs
      Email).
- [ ] **Register level**: appropriate for the channel and recipient.
- [ ] **No machine tells**: avoids hedge stacking, intensifier
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
      include required disclosures (자본시장법 / 금융소비자보호법 for
      finance).
- [ ] **Brand / trademark**: brand names not altered.
- [ ] **Privacy**: 개인정보보호법 compliance for personal data
      references.

### Output format

- [ ] **Format matches channel**: email subject + body + sign-off;
      formal document with proper opening.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When publishing-grade, run 3+ before/after checks:

1. **Register consistency**:
   - Before: mixed 합쇼체 / 해요체 in same email.
   - After: consistent register throughout.
2. **AI-pattern reduction**:
   - Before: 「~라고 생각합니다」「매우」「아주」 hedge / intensifier
     stacking.
   - After: rewrite to direct phrasing.
3. **Loanword consistency**:
   - Before: GitHub / 깃허브 mixing in same document.
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

- it cannot fully verify a fact claim — return with `[확인 필요]`
  markers;
- the user requested a conflicting channel — return one channel's
  version and note the conflict;
- the editing intensity auto-escalates — explain in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable mixes 합쇼체 / 해요체 / 반말체 mid-document —
   register broken.
2. The deliverable uses 「바쁘신 중에」 in a casual chat — formal
   letter cliché leakage.
3. The deliverable claims a percentage without source or sample size
   — research / statistics discipline broken.
4. The deliverable uses 「당신」 for a formal business audience — too
   direct, prefer 귀하.
5. The deliverable uses ~さん (Japanese) — Korean is ~님 / ~씨.