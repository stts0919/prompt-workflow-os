---
id: "041"
slug: "pricing-strategy"
title: "Design Pricing Strategy"
category: "business"
aliases:
  - pricing
  - price
  - monetization pricing
triggers:
  - pricing
  - how to price
  - pricing tiers
  - monetization
input_types:
  - offer
  - market
  - constraints
output_types:
  - pricing strategy
  - tier logic
requires:
  - offer
  - market willingness to pay
  - business model constraints
produces:
  - pricing strategy
  - tier table
  - test plan
related:
  - offer-design
  - value-proposition
  - business-model
playbooks:
  - validate-a-business-idea
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



# 041 — Design Pricing Strategy

## What is this?

Propose 2–3 pricing models (good-better-best, usage, tiered) with rationale, a tier table, and a price-test plan.

## Why use it?

Pricing changes margin more than any other lever. A pricing strategy defends the choice and the trade-offs.

## When should I use it?

- You're launching a paid offer.
- Your pricing feels arbitrary.

## When should I not use it?

- You only need a headline price — use offer-design (037).

## What should I prepare?

- Offer summary.
- Market willingness to pay signals.
- Business model constraints.

## How does the AI help me?

1. Confirm inputs.
2. Generate 2–3 pricing models.
3. Build a tier table.
4. Define a price-test plan.

## What will I get?

- Pricing models.
- Tier table.
- Price-test plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [offer-design](../02-business/037-offer-design.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [business-model](../02-business/042-business-model.md)

## Recommended next steps

- sales-page (043)
- marketing-funnel (044)

---

## AI specification

```text
purpose: "Develop pricing options and validation steps."
required_inputs:
  - offer
  - market willingness to pay
  - business model constraints
optional_inputs:
  - competitor pricing
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a headline price — use offer-design (037)."
workflow:
  - "1. Confirm inputs."
  - "2. Generate 2–3 pricing models."
  - "3. Build a tier table."
  - "4. Define a price-test plan."
output_contract:
  - "pricing strategy"
  - "tier table"
  - "test plan"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: pricing_models
    description: candidate pricing strategies
  - key: tier_table
    description: tiers with rationale
```