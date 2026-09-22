# Quality Checklist — `en-US` (English — United States)

> Source-of-truth file for the `en-US` quality checklist. Lives under
> `shared/locales/en-US/` per the architecture in
> [`../README.md`](../README.md).

The `en-US` quality gate is two layers:

- **Layer 1** — a compact, machine-checkable list the AI should run on
  every protected-spans-respecting draft.
- **Layer 2** — a human-readable editorial review checklist for the
  operator to apply when the deliverable is high-stakes.

A deliverable is acceptable when **Layer 1 passes 100%** and **Layer 2
has no blocking failure**.

---

## Layer 1 — Compact AI-readable checklist

Run before showing output to the user. Block on any failure.

1. **Spelling**: US spellings throughout (`organization`, `color`, `center`,
   etc.). See [TERM_GLOSSARY.md](TERM_GLOSSARY.md) section 1.
2. **Dates**: `MM/DD/YYYY` in business contexts, `YYYY-MM-DD` in
   technical.
3. **Currency**: `$` symbol before number; no space between (`$100`,
   not `$ 100`).
4. **Quotation marks**: double quotes `" "` for direct speech;
   straight ASCII quotes in technical writing.
5. **Honorifics**: `Mr.` / `Ms.` / `Mrs.` / `Dr.` with period.
6. **Protected content**: code, IDs, URLs, brand names, citations,
   numbers, units, currency, dates not rewritten.
7. **Channel voice**: profile matches channel (LinkedIn / Twitter /
   Reddit / email / landing / support).
8. **AI-pattern reduction**:
   - No "delve into", "synergy", "leverage" buzzword stacking.
   - No "It's important to note that", "in conclusion" filler.
   - No "we believe / we think / we suggest" three-times-in-a-row.
   - No over-formal hedges ("It might be argued that").
9. **Editing intensity**: matches workflow declaration; legal /
   medical / financial / security / compliance uses `strict_precision`.
10. **Output language**: when the user requested English output, do not
    slip into Chinese (or vice versa for Chinese requests).

## Layer 2 — Human-readable editorial review checklist

Run by the operator on high-stakes deliverables. Each item has a
severity.

### Structure & clarity

- [ ] **Core message visible**: reader sees the takeaway in title /
  opening sentence.
- [ ] **Paragraph logic**: smooth transitions, no abrupt topic shifts.
- [ ] **Heading hierarchy**: H2 / H3 / H4 consistent.
- [ ] **List format**: numbered or bulleted consistently.
- [ ] **Citations**: every data point has a source.

### Language & tone

- [ ] **Channel voice**: matches platform (LinkedIn vs Twitter vs
      Reddit vs email).
- [ ] **No "machine" tells**: avoids three-paragraph parallel structure,
      hollow summary, formulaic openers.
- [ ] **US English**: spelling, idioms, register consistent throughout.
- [ ] **Direct asks**: US business writing leads with the ask; avoid
      burying the question.

### Audience fit

- [ ] **Reader profile**: writer can describe who they are writing
      for (US / global / industry / role).
- [ ] **Reader action**: closing provides a clear next step.
- [ ] **No offense**: avoids stereotypes, regional bias, political
      bias.

### Compliance & safety

- [ ] **No detection-bypass claims**: text does not claim "undetectable",
      "human-proof", "watermark-free".
- [ ] **Regulatory accuracy**: medical, financial, efficacy claims
      include required disclosures.
- [ ] **Brand / trademark**: brand names not altered.

### Output format

- [ ] **Format matches channel**: Twitter short, LinkedIn
      achievement-focused, email has subject + body + sign-off.
- [ ] **Image / video placeholders**: marked when needed.
- [ ] **CTA**: sales / conversion has clear action.

### Before-and-after spot checks (high-stakes)

When the deliverable is publishing-grade, run 3+ before/after checks:

1. **US spelling**:
   - Before: "The organisation has realised..." (UK spelling).
   - After: "The organization has realized..." (US spelling).
2. **AI-pattern reduction**:
   - Before: "We believe X. We think Y. We suggest Z." (three
     consecutive).
   - After: rewrite to avoid repetition; vary sentence structures.
3. **Direct ask**:
   - Before: US email with ask buried in the third paragraph.
   - After: ask in the first paragraph; context follows.

## How to apply

- **Layer 1** runs every turn.
- **Layer 2** runs when:
  - the workflow is high-traffic or publishes to a public channel,
  - the editing intensity is `strict_precision`,
  - the deliverable is regulated (legal, medical, financial, security),
  - the operator requests it.
- A deliverable is **acceptable** when Layer 1 is 100% AND Layer 2 has no
  blocking failure.

## When to return partial output

The AI should return partial output (with a short note) when:

- it cannot fully verify a fact claim (Layer 2 數據可追溯 fails) — return
  the deliverable with `[to verify]` markers;
- the user explicitly requested a deliverable in a conflicting channel
  (e.g. asked for a Reddit casual but in LinkedIn professional voice) —
  return a single channel's version and note the conflict;
- the editing intensity escalates automatically — explain the
  auto-escalation in one line.

---

## Edge cases the operator should escalate

These patterns look minor but indicate systemic drift. Treat as
`strict_precision`:

1. The deliverable switches between US and UK spellings in the same
   paragraph — implies the locale layer failed to load.
2. The deliverable uses "Let's table this" in a UK audience — opposite
   meaning (UK "table" means bring up for discussion; US "table" means
   defer).
3. The deliverable claims a percentage or ranking without a source.
4. The deliverate transliterates a brand name (e.g. "the Goog") — brand
   names stay as-is.
5. The deliverate uses "football" for soccer in a US audience — UK
   "football" = soccer, US "soccer" = soccer.