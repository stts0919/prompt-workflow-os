# Quality Checklists

Apply before delivering any non-trivial output.

## Universal checks

- [ ] Output language matches the user's language unless a deliverable language was specified.
- [ ] All required inputs satisfied, or the AI stated labeled assumptions.
- [ ] No fabricated facts, numbers, sources, or quotes.
- [ ] Sources used are real and reachable; URL included when relevant.
- [ ] Verified facts, user-provided facts, assumptions, inferences, and recommendations are clearly labeled when the output mixes them.
- [ ] Output respects all stated constraints (tone, length, must-include, must-avoid).
- [ ] One suggested next step is provided when useful; none when the task is finished.
- [ ] All cross-references use relative Markdown links.

## Localization checks

- [ ] When the conversation language is Traditional Chinese or the deliverable targets Taiwan readers, the [Taiwan Traditional Chinese quality checklist](locales/zh-TW/QUALITY_CHECKLIST.md) is applied in addition to this checklist.
- [ ] Output does not claim human authorship, watermark removal, or AI detection evasion as a result of editing.
- [ ] For zh-TW output, regional terminology is context-appropriate (see [locales/zh-TW/TERM_GLOSSARY.md](locales/zh-TW/TERM_GLOSSARY.md)).
- [ ] Protected content (code, IDs, URLs, brand names, required disclosures) is unchanged.

## Per category

### Articles and posts

- [ ] The lede answers the reader's primary question.
- [ ] Headings scan as a clear outline.
- [ ] Sources for factual claims are cited or flagged as unverified.
- [ ] Tone matches the brand voice guide (if provided).
- [ ] Call to action is appropriate to the stage.
- [ ] For zh-TW output, the chosen [style profile](locales/zh-TW/STYLE_PROFILES.md) is applied consistently.

### Business deliverables

- [ ] Target customer is concrete.
- [ ] Each option compared has explicit trade-offs.
- [ ] Pricing or numbers include a sensitivity note when applicable.
- [ ] Recommendations include at least one alternative.

### Research deliverables

- [ ] Every fact is labeled with its source or marked unverified.
- [ ] Counter-arguments are surfaced for any opinionated conclusion.
- [ ] Confidence level is stated where appropriate.
- [ ] Verification gaps are listed when sources are incomplete.
- [ ] For zh-TW research output, `zh-tw-research-precise` profile is applied.

### Project / workflow deliverables

- [ ] Each task has a clear owner slot (or named placeholders).
- [ ] Risks and dependencies are explicitly listed.
- [ ] Acceptance criteria are testable.
- [ ] Timeline is realistic and flexible (room for unknowns).
- [ ] For zh-TW SOP output, `zh-tw-sop-direct` profile is applied with imperative voice.

### Technical deliverables

- [ ] Code compiles or at least the syntax is consistent.
- [ ] Acceptance criteria and non-goals are present.
- [ ] Edge cases are noted (empty input, large input, partial failure).
- [ ] Migration or rollback plan is included for database / schema changes.
- [ ] For zh-TW technical output, `zh-tw-technical-clear` profile is applied.

### Customer support replies

- [ ] The actual issue is acknowledged.
- [ ] A concrete next action is named.
- [ ] An escalation or fallback path is provided when relevant.
- [ ] No fabricated compensation, promises, or policy statements.
- [ ] For zh-TW support replies, `zh-tw-customer-support` profile is applied.
- [ ] Editing intensity matches content type: `standard` for user-facing; `light` for structured technical; `strict_precision` for legal / medical / financial / security / compliance / citation-heavy content.
- [ ] Style profile selection matches channel: Threads → `zh-tw-threads-insightful`; Instagram → `zh-tw-instagram-casual`; LinkedIn → `zh-tw-linkedin-professional`; landing page → `zh-tw-landing-page-clear`; long-form article → `zh-tw-long-form-article`; agent spec → `zh-tw-agent-spec-precise`.

## Failure handling

If any check fails and the issue cannot be resolved in-line, return the deliverable with the heading:

```
PARTIAL — see issues below
```

followed by:

- What was produced
- What was skipped
- Why it was skipped
- What the user can supply to finish

When the failing item is localization or writing quality for zh-TW, also note which checklist item failed and link to [locales/zh-TW/QUALITY_CHECKLIST.md](locales/zh-TW/QUALITY_CHECKLIST.md).
