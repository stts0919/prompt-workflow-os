# Style Profiles — `en-GB` (English — United Kingdom)

> Source-of-truth file for the `en-GB` style profiles. Lives under
> `shared/locales/en-GB/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for British English.
Each profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile uses:

- **Code**: identifier.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: UK.
- **`punctuation_notes`**: spacing, marks, conventions.
- **`common_pitfalls`**: patterns the layer avoids.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `en-gb-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: you.
- **`formality`**: medium.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: single quotes for direct speech (UK
  convention); straight ASCII quotes in technical; periods usually
  omitted from abbreviations.
- **`common_pitfalls`**:
  - US buzzword leakage ("delve into", "synergy", "circle back").
  - US idioms ("take a rain check", "touch base").
  - US spelling (organization, color, modeled).
- **`exemplar`**: We build enterprise software for [industry]. Our
  customers typically see [outcome] within [timeframe].

## 2. `en-gb-linkedin-professional`

- **Channel**: LinkedIn posts / comments.
- **`second_person`**: you.
- **`formality`**: medium-high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: em-dash for asides; line breaks between
  paragraphs.
- **`common_pitfalls`**:
  - "Thrilled to announce" US-style cliché.
  - Excessive hashtags.
  - US spelling leakage.
- **`exemplar`**: Delighted to share that I've joined XYZ as Head of
  Marketing. Looking forward to building with this team — we have a
  strong product and a clear path to [outcome].

## 3. `en-gb-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: you.
- **`formality`**: low.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: short sentences; emoji OK sparingly;
  British humour (dry, ironic) acceptable.
- **`common_pitfalls`**:
  - Over-long posts.
  - Engagement bait.
  - US slang that doesn't carry across.
- **`exemplar`**: Spent six months waiting on [tool] to ship
  [feature]. Built my own in a fortnight. Sometimes you have to
  DYI.

## 4. `en-gb-email-professional`

- **Channel**: B2B email.
- **`second_person`**: Dear [Name], (formal) / Hi [Name], (casual).
- **`formality`**: high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: clear subject line; signature block with
  name / title / company / phone / website.
- **`common_pitfalls`**:
  - Too direct / blunt (UK prefers polite hedging).
  - "Dear Sir / Madam" cliché (acceptable in formal letter, not
    email).
  - Vague sign-offs.
- **`exemplar**:
  ```text
  Subject: Introduction from [Company] — potential collaboration

  Dear [Name],

  I hope this finds you well. I'm writing from [Company], where we
  help [target audience] with [specific outcome]. I've followed your
  work at [their company] with great interest.

  Would you be open to a 15-minute call in the coming weeks to explore
  whether there might be a fit?

  Kind regards,

  [Your name]
  [Title]
  [Company]
  ```

## 5. `en-gb-formal-letter`

- **Channel**: formal letters (legal, government, business).
- **`second_person`**: Dear [Name], (named) / Dear Sir / Madam,
  (unnamed).
- **`formality`**: very high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: address block top-right; date below;
  recipient's address left; salutation with comma; sign-off
  "Yours sincerely," (named) / "Yours faithfully," (unnamed);
  signature above typed name.
- **`common_pitfalls`**:
  - Wrong sign-off (sincerely vs faithfully).
  - Colon after salutation (UK uses comma).
  - Casual language leaking into formal context.
- **`exemplar**:
  ```text
  [Sender's address]

  [Date]

  [Recipient's address]

  Dear Mr Smith,

  Thank you for your letter of [date] regarding [subject]. I am writing
  to [purpose].

  [Body paragraphs]

  I look forward to hearing from you.

  Yours sincerely,

  [Signature]
  [Typed name]
  [Title]
  ```

## 6. `en-gb-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: you.
- **`formality`**: medium.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text is action + outcome.
- **`common_pitfalls`**:
  - "Revolutionary" / "disruptive" / "game-changing" exaggeration.
  - Multiple CTAs.
  - Missing social proof.
- **`exemplar`**: **Headline:** [Outcome] for [audience] in
  [timeframe]. **Subhead:** [One-line how]. **CTA:** Start free
  trial →

## 7. `en-gb-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: you.
- **`formality`**: medium.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: polite empathy first, action second;
  specific timeline; open invitation.
- **`common_pitfalls`**:
  - "We apologise for any inconvenience this may have caused"
    (UK spelling: "apologise"; but avoid the cliché).
  - Defensive tone.
  - No specific next step or timeline.
- **`exemplar**:
  ```text
  Hello [Name],

  Thank you for getting in touch. I'm sorry to hear about the trouble
  with your order [#12345].

  I've initiated a full refund, which should appear back on your
  original payment method within 5-7 working days.

  Please let me know if there's anything else I can help with.

  Kind regards,
  [Agent name]
  ```

## 8. `en-gb-long-form-article`

- **Channel**: blog posts, long articles.
- **`second_person`**: you / the reader.
- **`formality`**: medium-high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: short paragraphs (3-5 sentences); H2 / H3
  structure; pull quotes; citations as hyperlinks.
- **`common_pitfalls`**:
  - "In conclusion" / "to summarise" filler endings.
  - Generic intro without hook.
  - Unsupported statistics.
- **`exemplar`**: Most teams hit the same wall: [problem]. After
  working with [N] teams over the past year, I've seen three
  patterns that separate those who solve it from those who don't.

## 9. `en-gb-business-consulting`

- **Channel**: consulting reports, strategic documents, internal memos.
- **`second_person`**: not used (internal).
- **`formality`**: high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: numbered lists; data tables; clear
  recommendations.
- **`common_pitfalls`**:
  - "Synergy" / "leverage" / "circle back" US buzzword leakage.
  - Recommendations without data support.
  - Missing "Recommendation" or "Next step" sections.
- **`exemplar`**: Based on Q3 data and a survey of 47 enterprise
  customers, retention dropped by 4.2 percentage points compared
  with Q2. **Recommendation:** invest £200K in onboarding
  improvements by the end of Q4. **Next step:** review the proposed
  budget with finance by 15 November.

## 10. `en-gb-finance-formal`

- **Channel**: financial reports, regulatory disclosures, investment
  summaries.
- **`second_person`**: not used (formal audience).
- **`formality`**: very high.
- **`locale`**: United Kingdom.
- **`punctuation_notes`**: precise figures; "£" before amount; date
  DD/MM/YYYY.
- **`common_pitfalls`**:
  - Promising returns without "Past performance is not a reliable
    indicator of future results" disclaimer.
  - Rounding figures to mislead.
  - Citing non-FCA-compliant sources for regulated content.
- **`exemplar`**: The fund returned 8.2% in 2024, 5.1% in 2025, and
  -1.3% year-to-date as of 22/09/2026. Past performance is not a
  reliable indicator of future results. Suitable for investors with
  [risk profile] over a [minimum horizon].

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `en-gb-friendly-professional` |
| content | LinkedIn | `en-gb-linkedin-professional` |
| content | Twitter / X | `en-gb-twitter-casual` |
| content | long-form | `en-gb-long-form-article` |
| business | email | `en-gb-email-professional` |
| business | formal letter | `en-gb-formal-letter` |
| business | sales / landing | `en-gb-landing-page-clear` |
| business | financial | `en-gb-finance-formal` |
| research | report | `en-gb-business-consulting` |
| any | customer support | `en-gb-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.