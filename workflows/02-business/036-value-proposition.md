---
id: "036"
slug: "value-proposition"
title: "Create a Value Proposition"
category: "business"
aliases:
  - value prop
  - vp
  - value proposition canvas
triggers:
  - value proposition
  - value prop
  - why us
  - benefits
input_types:
  - offer
  - customer
  - pains and gains
output_types:
  - value proposition canvas
  - headline value prop
requires:
  - offer
  - customer profile
  - pains and gains
produces:
  - value proposition canvas
  - headline value prop
  - supporting statements
related:
  - positioning
  - sales-page
  - customer-persona
playbooks:
  - validate-a-business-idea
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
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 036 — Create a Value Proposition

## What is this?

Produce a value proposition canvas (jobs, pains, gains; products, pain relievers, gain creators) and a single headline that combines customer, value, and differentiator.

## Why use it?

A value prop is more than a tagline — it is a structured promise that matches what the customer wants.

## When should I use it?

- You're launching a new product.
- Your landing pages under-convert.

## When should I not use it?

- You only need a tagline — use headline-generation (020).

## What should I prepare?

- Offer summary.
- Customer pains and gains.

## How does the AI help me?

1. Build the canvas.
2. Draft a headline value prop.
3. Add supporting statements.
4. Sanity-check against the persona.

## What will I get?

- Value proposition canvas.
- Headline value prop.
- Supporting statements.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [positioning](../02-business/035-positioning.md)
- [sales-page](../02-business/043-sales-page.md)
- [customer-persona](../02-business/031-customer-persona.md)

## Recommended next steps

- sales-page (043)
- mvp-scope (039)

---

## AI specification

```text
purpose: "Map customer jobs, pains, gains, and offer value."
required_inputs:
  - offer
  - customer profile
  - pains and gains
optional_inputs:
  - existing value prop
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a tagline — use headline-generation (020)."
workflow:
  - "1. Build the canvas."
  - "2. Draft a headline value prop."
  - "3. Add supporting statements."
  - "4. Sanity-check against the persona."
output_contract:
  - "value proposition canvas"
  - "headline value prop"
  - "supporting statements"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: value_prop_canvas
    description: jobs/pains/gains map
  - key: headline_value_prop
    description: headline statement
```