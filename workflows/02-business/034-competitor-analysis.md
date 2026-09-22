---
id: "034"
slug: "competitor-analysis"
title: "Analyze Competitors"
category: "business"
aliases:
  - competitive analysis
  - competition
  - competitors
triggers:
  - competitors
  - competitive landscape
  - who competes with me
  - competitor analysis
input_types:
  - offer
  - customer
  - competitor list
output_types:
  - landscape map
  - comparison table
  - gaps
requires:
  - offer
  - customer
  - market
  - known competitors
produces:
  - landscape map
  - comparison table
  - gap analysis
related:
  - positioning
  - customer-persona
  - value-proposition
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



# 034 — Analyze Competitors

## What is this?

Build a competitor landscape using a comparison table (audience, features, pricing, messaging) and a gaps section that highlights whitespace.

## Why use it?

Defensibility is built on contrast. A clear comparison surfaces differentiation that an internal team takes for granted.

## When should I use it?

- You're entering a new market.
- Your messaging feels undifferentiated.

## When should I not use it?

- You need continuous tracking — set up a recurring process with marketing-funnel (044).

## What should I prepare?

- Offer summary.
- Customer profile.
- Known competitor list or URLs.

## How does the AI help me?

1. Confirm offer and customer.
2. Build a comparison table.
3. Map positioning quadrants.
4. Identify gaps and whitespace.

## What will I get?

- Comparison table.
- Positioning quadrants.
- Whitespace and gap notes.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [positioning](../02-business/035-positioning.md)
- [customer-persona](../02-business/031-customer-persona.md)
- [value-proposition](../02-business/036-value-proposition.md)

## Recommended next steps

- positioning (035)
- value-proposition (036)

---

## AI specification

```text
purpose: "Compare direct, indirect, and substitute competitors."
required_inputs:
  - offer
  - customer
  - market
  - known competitors
optional_inputs:
  - competitor URLs
  - positioning notes
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You need continuous tracking — set up a recurring process with marketing-funnel (044)."
workflow:
  - "1. Confirm offer and customer."
  - "2. Build a comparison table."
  - "3. Map positioning quadrants."
  - "4. Identify gaps and whitespace."
output_contract:
  - "landscape map"
  - "comparison table"
  - "gap analysis"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: comparison_table
    description: competitor matrix
  - key: whitespace
    description: gaps and white-space opportunities
```