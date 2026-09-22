---
id: "021"
slug: "cta-design"
title: "Design Calls to Action"
category: "content"
aliases:
  - call to action
  - cta copy
  - cta design
  - next action prompt
triggers:
  - call to action
  - what should they do next
  - cta
  - next button
input_types:
  - context (article, email, post)
  - intended action
  - audience
output_types:
  - CTA variants
  - rationale
requires:
  - context
  - intended action
  - audience
produces:
  - CTA variants tuned to context
  - rationale
  - placement suggestions
related:
  - social-post
  - newsletter
  - email-sequence
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
handoff:
  - key: context
    description: "summary of upstream context"
---



# 021 — Design Calls to Action

## What is this?

Generate CTA variants tuned to context (article, email, post, landing page). Include button text, micro-copy, and placement suggestions.

## Why use it?

Even engaged readers stall without a clear next step. A weak CTA is the most common reason content under-converts.

## When should I use it?

- You're publishing any content that needs the reader to act.
- Your current CTAs are bland or generic.

## When should I not use it?

- You're building a full landing page — use sales-page (043).
- You're building an automated sequence — use email-sequence (046).

## What should I prepare?

- Context (where the CTA lives).
- Intended action.
- Audience.

## How does the AI help me?

1. Confirm context and intended action.
2. Generate CTA variants across tones.
3. Recommend placement and micro-copy.
4. Suggest a test plan (A/B variant ideas).

## What will I get?

- CTA variants.
- Placement suggestions.
- Test plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [social-post](../01-content/012-social-post.md)
- [newsletter](../01-content/011-newsletter.md)
- [email-sequence](../02-business/046-email-sequence.md)

## Recommended next steps

- content-quality-review (029)
- email-sequence (046)

---

## AI specification

```text
purpose: "Design context-appropriate calls to action that move readers to the next step."
required_inputs:
  - context
  - intended action
  - audience
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're building a full landing page — use sales-page (043)."
  - "You're building an automated sequence — use email-sequence (046)."
workflow:
  - "1. Confirm context and intended action."
  - "2. Generate CTA variants across tones."
  - "3. Recommend placement and micro-copy."
  - "4. Suggest a test plan (A/B variant ideas)."
output_contract:
  - "CTA variants tuned to context"
  - "rationale"
  - "placement suggestions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: cta_variants
    description: CTA options
  - key: placement
    description: placement suggestions
```