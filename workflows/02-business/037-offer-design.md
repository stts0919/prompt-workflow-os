---
id: "037"
slug: "offer-design"
title: "Design an Offer"
category: "business"
aliases:
  - offer
  - product offer
  - service offer
  - package
triggers:
  - design an offer
  - package
  - what to sell
  - bundling
input_types:
  - offer
  - audience
  - pricing constraints
output_types:
  - offer card
  - pricing tiers
requires:
  - underlying product or service
  - audience
  - pricing constraints
produces:
  - offer card
  - pricing tiers
  - guarantee or risk-reversal
related:
  - pricing-strategy
  - value-proposition
  - sales-page
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



# 037 — Design an Offer

## What is this?

Combine features, deliverables, pricing tiers, bonuses, and a guarantee into a single offer card. The card should be readable in 60 seconds.

## Why use it?

Most offers underperform because they bury the outcome. A well-designed offer aligns price, value, and risk reversal.

## When should I use it?

- You're launching a paid product or service.
- Your conversion is low even though traffic is good.

## When should I not use it?

- You only need pricing logic — use pricing-strategy (041).

## What should I prepare?

- Product or service.
- Audience.
- Pricing constraints.

## How does the AI help me?

1. Confirm inputs.
2. Build a tiered offer card.
3. Add bonuses and guarantee.
4. Suggest price-test variations.

## What will I get?

- Tiered offer card.
- Bonuses and guarantee.
- Price-test variations.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [pricing-strategy](../02-business/041-pricing-strategy.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [sales-page](../02-business/043-sales-page.md)

## Recommended next steps

- pricing-strategy (041)
- sales-page (043)

---

## AI specification

```text
purpose: "Package a service or product into a clear offer."
required_inputs:
  - underlying product or service
  - audience
  - pricing constraints
optional_inputs:
  - competitor pricing
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need pricing logic — use pricing-strategy (041)."
workflow:
  - "1. Confirm inputs."
  - "2. Build a tiered offer card."
  - "3. Add bonuses and guarantee."
  - "4. Suggest price-test variations."
output_contract:
  - "offer card"
  - "pricing tiers"
  - "guarantee or risk-reversal"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: offer_card
    description: tiered offer summary
  - key: guarantee
    description: risk-reversal options
```