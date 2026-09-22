# Quality Checklist — `en-GB` (English — United Kingdom)

> Source-of-truth file for the `en-GB` quality checklist. Lives under
> `shared/locales/en-GB/` per the architecture in
> [`../README.md`](../README.md).

The `en-GB` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list the AI should run on
  every protected-spans-respecting draft.
- **Layer 2** — a human-readable editorial review checklist for the
  operator to apply when the deliverable is high-stakes.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output. Block on any failure.

1. **Spelling**: UK spellings throughout (`organisation`, `colour`,
   `centre`, `modelled`). See [TERM_GLOSSARY.md](TERM_GLOSSARY.md)
   section 1.
2. **Dates**: `DD/MM/YYYY` in business contexts; `YYYY-MM-DD` in
   technical.
3. **Currency**: `£` symbol before number; no space between
   (`£100`, not `£ 100`).
4. **Quotation marks**: single quotes `' '` for direct speech (UK
   convention); straight ASCII quotes in technical writing.
5. **Honorifics**: `Mr` / `Mrs` / `Dr` / `Prof` typically without
   period (UK convention).
6. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
7. **Channel voice**: profile matches channel (LinkedIn / Twitter /
   email / formal letter / landing / support).
8. **AI-pattern reduction**:
   - No US buzzword leakage ("delve into", "synergy", "circle back").
   - No "It's important to note that", "in conclusion" filler.
   - No US idioms ("take a rain check", "touch base", "circle back").
   - No over-formal hedge stacking.
9. **Editing intensity**: matches workflow declaration; legal /
   medical / financial / security / compliance uses `strict_precision`.
10. **Output language**: when the user requested English output, do not
    slip into Chinese (or vice versa).

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables.

### Structure & clarity

- [ ] **Core message visible**: takeaway in title / opening sentence.
- [ ] **Paragraph logic**: smooth transitions.
- [ ] **Heading hierarchy**: H2 / H3 / H4 consistent.
- [ ] **List format**: numbered or bulleted consistently.
- [ ] **Citations**: every data point has a source.

### Language & tone

- [ ] **Channel voice**: matches platform.
- [ ] **UK register**: spelling, idioms, hedging consistent
      throughout.
- [ ] **Polite hedging** where appropriate (UK business prefers
      indirect phrasing in formal contexts).
- [ ] **No machine tells**: avoids three-paragraph parallel
      structure, hollow summary, formulaic openers.

### Audience fit

- [ ] **Reader profile**: writer can describe who they are writing
      for (UK industry / role).
- [ ] **Reader action**: closing provides a clear next step.
- [ ] **No offense**: avoids stereotypes, regional bias, political
      bias.

### Compliance & safety

- [ ] **No detection-bypass claims**: text does not claim
      "undetectable", "human-proof", "watermark-free".
- [ ] **Regulatory accuracy**: medical, financial, efficacy claims
      include required disclosures ("Past performance is not a
      reliable indicator of future results" for finance).
- [ ] **Brand / trademark**: brand names not altered.
- [ ] **FCA compliance** (where applicable): UK financial services
      content follows FCA conduct rules.

### Output format

- [ ] **Format matches channel**: email subject + body + sign-off;
      formal letter address blocks.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When publishing-grade, run 3+ before/after checks:

1. **UK spelling**:
   - Before: "The organization has realized..." (US spelling).
   - After: "The organisation has realised..." (UK spelling).
2. **AI-pattern reduction**:
   - Before: "delve into the synergy of..." (US buzzwords).
   - After: rewrite to plain UK English.
3. **Polite hedging**:
   - Before: blunt US-style ask ("Send me the file by Friday").
   - After: UK polite form ("Would it be possible to send the file
     by Friday? Thank you.").

## How to apply

- **Layer 1** runs every turn.
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated,
  - the operator requests it.
- A deliverable is **acceptable** when Layer 1 is 100% AND Layer 2 has
  no blocking failure.

## When to return partial output

Return partial output (with a short note) when:

- it cannot fully verify a fact claim — return with `[to verify]`
  markers;
- the user requested a conflicting channel — return one channel's
  version and note the conflict;
- the editing intensity auto-escalates — explain in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable switches between UK and US spellings mid-paragraph
   — implies the locale layer failed to load.
2. The deliverable uses US idiom in a UK audience — "take a rain
   check" / "touch base" should be replaced with UK equivalents or
   removed.
3. The deliverable claims a percentage or ranking without a source.
4. The deliverable uses "Yours faithfully" with a named recipient
   (should be "Yours sincerely") — UK formal letter convention
   broken.
5. The deliverable uses "football" for soccer in a US audience
   context (where this locale is en-GB, this is correct; flag
   only if cross-locale mixing).