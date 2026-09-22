# Style Profiles — `en-US` (English — United States)

> Source-of-truth file for the `en-US` style profiles. Lives under
> `shared/locales/en-US/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for US English. Each
profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile below uses:

- **Code**: identifier used in workflow frontmatter and harness output.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: which audience this profile serves.
- **`punctuation_notes`**: spacing, marks, and conventions specific to
  this profile.
- **`common_pitfalls`**: patterns the layer avoids in this profile.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `en-us-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: you (default).
- **`formality`**: medium.
- **`locale`**: United States.
- **`punctuation_notes`**: ASCII straight quotes for technical writing;
  curly quotes acceptable in narrative; periods inside abbreviation
  (Mr., St., Dr.).
- **`common_pitfalls`**:
  - "delve into", "synergy", "circle back to" buzzword stacking.
  - "It's important to note that" filler phrases.
  - Three consecutive "we believe / we think / we suggest" structures.
- **`exemplar`**: We build enterprise software for [industry]. Our
  customers typically see [outcome] within [timeframe].

## 2. `en-us-linkedin-professional`

- **Channel**: LinkedIn posts / comments.
- **`second_person`**: you / the reader.
- **`formality`**: medium-high.
- **`locale`**: United States.
- **`punctuation_notes`**: ASCII straight quotes; em-dash for asides;
  line breaks between paragraphs.
- **`common_pitfalls`**:
  - "Thrilled to announce" cliché.
  - Humble-brag tone.
  - Excessive hashtags (#).
  - Emoji on professional posts (US LinkedIn prefers no emoji).
- **`exemplar`**: Excited to share that I've joined XYZ as Head of
  Marketing. Looking forward to building with this team — we have a
  strong product and a clear path to [outcome].

## 3. `en-us-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: you.
- **`formality`**: low.
- **`locale`**: United States.
- **`punctuation_notes`**: short sentences; emoji OK sparingly; thread
  numbering (1/, 2/) for multi-post.
- **`common_pitfalls`**:
  - Over-long posts (X character limit).
  - Engagement bait ("RT if you agree").
  - Hashtag stuffing (> 3 hashtags).
- **`exemplar`**: Spent 6 months waiting on [tool] to ship [feature].
  Built my own in 2 weeks. Sometimes you have to DIY.

## 4. `en-us-reddit-casual`

- **Channel**: Reddit comments / posts.
- **`second_person`**: you / OP.
- **`formality`**: medium-low.
- **`locale`**: United States.
- **`punctuation_notes`**: paragraphs OK; bold for emphasis (markdown);
  no excessive emoji.
- **`common_pitfalls`**:
  - Marketing voice (Reddit users detect and downvote).
  - Fake personal anecdotes.
  - Link-dropping without context.
- **`exemplar`**: I had this exact problem last year. Here's what
  worked for me: [specific steps]. YMMV depending on your setup.

## 5. `en-us-email-professional`

- **Channel**: B2B email.
- **`second_person`**: Hi [Name] (casual) / Dear [Name] (formal).
- **`formality`**: high.
- **`locale`**: United States.
- **`punctuation_notes`**: clear subject line; ASCII quotes; signature
  block with name / title / company / phone / website.
- **`common_pitfalls`**:
  - "Dear Sir / Madam" (overly formal for most US contexts).
  - Burying the ask in the body (US email: ask first, context after).
  - Vague sign-offs ("Let me know").
- **`exemplar**:
  ```text
  Subject: Quick question about [topic]

  Hi [Name],

  Saw your team's recent post on [topic]. We built [product] that
  addresses the exact problem you described — specifically [outcome].

  Open to a 15-minute call this week?

  Best,
  [Your name]
  [Title]
  [Company]
  ```

## 6. `en-us-email-marketing`

- **Channel**: B2C / newsletter email.
- **`second_person`**: you.
- **`formality`**: medium.
- **`locale`**: United States.
- **`punctuation_notes`**: subject line is the headline; preview text
  matters; clear CTA button text.
- **`common_pitfalls`**:
  - Click-bait subject lines that don't match body.
  - Multiple CTAs competing for attention.
  - All-caps or excessive punctuation in subject.
- **`exemplar`**: **Subject:** [Number] [outcome] our customers got
  in [timeframe]. **Preview:** Here's how. **CTA:** See the case
  studies →

## 7. `en-us-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: you (direct).
- **`formality`**: medium.
- **`locale`**: United States.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text is action + outcome.
- **`common_pitfalls`**:
  - "Revolutionary" / "disruptive" / "game-changing" exaggeration.
  - Multiple CTAs.
  - Missing social proof (numbers / testimonials).
- **`exemplar`**: **Headline:** [Outcome] for [audience] in
  [timeframe]. **Subhead:** [One-line how]. **CTA:** Start free
  trial →

## 8. `en-us-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: you / the customer.
- **`formality`**: medium.
- **`locale`**: United States.
- **`punctuation_notes`**: empathy first, action second; specific
  timeline; open invitation for follow-up.
- **`common_pitfalls`**:
  - "We apologize for any inconvenience this may have caused"
    (over-formal cliché).
  - Defensive tone.
  - No specific next step or timeline.
- **`exemplar**:
  ```text
  Hi [Name],

  Sorry for the trouble. I've initiated a full refund for order
  [#12345]. You'll see it back on your original payment method within
  5-7 business days.

  Let me know if anything else comes up.

  Best,
  [Agent name]
  ```

## 9. `en-us-long-form-article`

- **Channel**: blog posts, long articles.
- **`second_person`**: you / the reader.
- **`formality`**: medium-high.
- **`locale`**: United States.
- **`punctuation_notes`**: short paragraphs (3-5 sentences); H2 / H3
  structure; pull quotes for emphasis; citation as hyperlinks.
- **`common_pitfalls`**:
  - "In conclusion" / "to summarize" filler endings.
  - Generic intro without a hook.
  - Unsupported statistics.
- **`exemplar`**: Most teams hit the same wall: [problem]. After
  working with [N] teams over the past year, I've seen three patterns
  that separate those who solve it from those who don't.

## 10. `en-us-business-consulting`

- **Channel**: consulting reports, strategic documents, internal memos.
- **`second_person`**: not used (internal audience).
- **`formality`**: high.
- **`locale`**: United States.
- **`punctuation_notes`**: numbered lists; data tables; clear
  recommendations; "Recommendation:" prefix.
- **`common_pitfalls`**:
  - "Synergy" / "leverage" / "circle back" buzzword stacking.
  - Recommendations without data support.
  - Missing "Recommendation" or "Next step" sections.
- **`exemplar`**: Based on Q3 data and a survey of 47 enterprise
  customers, retention dropped 4.2 percentage points compared to Q2.
  **Recommendation:** invest $200K in onboarding improvements by
  end of Q4. **Next step:** review the proposed budget with finance
  by Nov 15.

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `en-us-friendly-professional` |
| content | LinkedIn | `en-us-linkedin-professional` |
| content | Twitter / X | `en-us-twitter-casual` |
| content | Reddit | `en-us-reddit-casual` |
| content | long-form | `en-us-long-form-article` |
| business | email | `en-us-email-professional` |
| business | marketing email | `en-us-email-marketing` |
| business | sales / landing | `en-us-landing-page-clear` |
| research | report | `en-us-business-consulting` |
| any | customer support | `en-us-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.