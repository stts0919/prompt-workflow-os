---
id: "043"
slug: "sales-page"
title: "Create a Sales Page"
category: "business"
aliases:
  - landing page
  - sales letter
  - product page copy
triggers:
  - sales page
  - landing page
  - product page
  - long-form sales letter
input_types:
  - offer
  - audience
  - tone
output_types:
  - sales page
requires:
  - offer card
  - audience
  - tone reference
produces:
  - sales page copy
  - section-by-section outline
related:
  - offer-design
  - value-proposition
  - case-study
playbooks: []
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-tw-landing-page-clear
  locale_style_profile_overrides:
    zh-TW: zh-tw-sales-clear
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 043 — Create a Sales Page

## What is this?

Produce a long-form sales page: headline, sub-headline, problem, promise, proof, offer, guarantee, call to action, FAQ.

## Why use it?

A sales page without structure scatters attention. The classic sections carry the reader from skepticism to action.

## When should I use it?

- You're launching a paid offer.
- Your landing page is under-converting.

## When should I not use it?

- You want a quick landing page — use a simpler structure with cta-design (021).

## What should I prepare?

- Offer card.
- Audience.
- Tone and proof.

## How does the AI help me?

1. Confirm inputs.
2. Write each section.
3. Insert proof and FAQs.
4. Close with a strong CTA.

## What will I get?

- Section-by-section outline.
- Sales page copy.
- Sample CTA.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [offer-design](../02-business/037-offer-design.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [case-study](../01-content/025-case-study.md)

## Recommended next steps

- content-quality-review (029)
- email-sequence (046)

---

## AI specification

```text
purpose: "Create a structured sales page from an offer brief."
required_inputs:
  - offer card
  - audience
  - tone reference
optional_inputs:
  - testimonials
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a quick landing page — use a simpler structure with cta-design (021)."
workflow:
  - "1. Confirm inputs."
  - "2. Write each section."
  - "3. Insert proof and FAQs."
  - "4. Close with a strong CTA."
output_contract:
  - "sales page copy"
  - "section-by-section outline"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: sales_page
    description: sectioned page copy
  - key: cta
    description: closing call to action
```