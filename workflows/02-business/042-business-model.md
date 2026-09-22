---
id: "042"
slug: "business-model"
title: "Design a Business Model"
category: "business"
aliases:
  - business model canvas
  - bmc
  - revenue model
triggers:
  - business model
  - how do we make money
  - revenue model
  - business model canvas
input_types:
  - offer
  - customer
  - channels
output_types:
  - business model canvas
requires:
  - offer
  - customer
  - channels
  - cost structure hints
produces:
  - business model canvas
  - alternate models
related:
  - pricing-strategy
  - value-proposition
  - offer-design
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



# 042 — Design a Business Model

## What is this?

Produce a business model canvas (segments, value props, channels, relationships, revenue, costs, etc.) plus one alternate model.

## Why use it?

Most pitch decks describe what the product does, not how it makes money. A business model makes the economics visible.

## When should I use it?

- You're starting or pivoting a business.
- Investors or partners ask how money flows.

## When should I not use it?

- You only need pricing — use pricing-strategy (041).

## What should I prepare?

- Offer.
- Customer segments.
- Channels.

## How does the AI help me?

1. Confirm inputs.
2. Build a canvas.
3. Add an alternate model.
4. Highlight weakest assumptions.

## What will I get?

- Business model canvas.
- Alternate model.
- Weakest-assumption list.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [pricing-strategy](../02-business/041-pricing-strategy.md)
- [value-proposition](../02-business/036-value-proposition.md)
- [offer-design](../02-business/037-offer-design.md)

## Recommended next steps

- pricing-strategy (041)
- offer-design (037)

---

## AI specification

```text
purpose: "Map value creation, delivery, and revenue logic."
required_inputs:
  - offer
  - customer
  - channels
  - cost structure hints
optional_inputs:
  - competitor models
  - regulation
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need pricing — use pricing-strategy (041)."
workflow:
  - "1. Confirm inputs."
  - "2. Build a canvas."
  - "3. Add an alternate model."
  - "4. Highlight weakest assumptions."
output_contract:
  - "business model canvas"
  - "alternate models"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: business_model_canvas
    description: 9-block canvas
  - key: alternate_model
    description: backup model
```