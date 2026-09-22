---
id: "031"
slug: "customer-persona"
title: "Define Target Customer"
category: "business"
aliases:
  - persona
  - icp
  - ideal customer profile
  - buyer persona
triggers:
  - who is my customer
  - icp
  - target persona
  - buyer persona
input_types:
  - product or service
  - existing customer signals
  - market
output_types:
  - persona card
  - jobs-to-be-done
requires:
  - product or service summary
  - any existing customer signals
  - target market
produces:
  - persona card
  - jobs-to-be-done
  - anti-persona
related:
  - customer-interview
  - value-proposition
  - competitor-analysis
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
  default_style_profile: zh-tw-business-consulting
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 031 — Define Target Customer

## What is this?

Produce a persona card with jobs-to-be-done, context, pains, gains, and an anti-persona. The card is concrete enough to brief a copywriter or sales team.

## Why use it?

Marketing fails when it targets "everyone". A persona makes it possible to choose channels, messages, and trade-offs.

## When should I use it?

- You're targeting a new segment.
- Your messaging gets no traction.

## When should I not use it?

- You have rich qualitative interviews — synthesize them first with customer-feedback-analysis (033).

## What should I prepare?

- Product or service summary.
- Existing customer signals (sales notes, support tickets, reviews).
- Market scope.

## How does the AI help me?

1. Confirm product and market.
2. Build a persona card (demographics, jobs, pains, gains).
3. Add an anti-persona.
4. Verify against existing signals.

## What will I get?

- Persona card.
- Jobs-to-be-done list.
- Anti-persona.
- Next-workflow suggestion: customer-interview (032).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-interview](../02-business/032-customer-interview.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [competitor-analysis](../02-business/034-competitor-analysis.md)

## Recommended next steps

- customer-interview (032)
- value-proposition (036)

---

## AI specification

```text
purpose: "Define a target customer based on jobs, context, pains, and desired outcomes."
required_inputs:
  - product or service summary
  - any existing customer signals
  - target market
optional_inputs:
  - competitors
  - pricing
  - sales notes
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You have rich qualitative interviews — synthesize them first with customer-feedback-analysis (033)."
workflow:
  - "1. Confirm product and market."
  - "2. Build a persona card (demographics, jobs, pains, gains)."
  - "3. Add an anti-persona."
  - "4. Verify against existing signals."
output_contract:
  - "persona card"
  - "jobs-to-be-done"
  - "anti-persona"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: persona
    description: persona card with jobs, pains, gains
  - key: anti_persona
    description: who is not the target
```