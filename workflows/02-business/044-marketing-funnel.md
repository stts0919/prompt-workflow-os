---
id: "044"
slug: "marketing-funnel"
title: "Design a Marketing Funnel"
category: "business"
aliases:
  - funnel
  - marketing funnel
  - tofu mofu bofu
  - customer journey funnel
triggers:
  - marketing funnel
  - funnel design
  - tofu mofu bofu
  - customer journey funnel
input_types:
  - offer
  - audience
  - channels
output_types:
  - funnel map
  - stage definitions
requires:
  - offer
  - audience
  - channels
produces:
  - funnel map
  - stage definitions
  - content per stage
related:
  - audience-message-map
  - campaign-plan
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



# 044 — Design a Marketing Funnel

## What is this?

Lay out a funnel (awareness, consideration, decision, retention) with stage definitions, content ideas per stage, and key metrics.

## Why use it?

Funnels clarify who sees what content at what moment. They make conversion problems attributable to a stage.

## When should I use it?

- You're building a campaign from scratch.
- Conversion is uneven and you don't know why.

## When should I not use it?

- You want a one-time launch — use campaign-plan (045).

## What should I prepare?

- Offer.
- Audience segments.
- Channels.

## How does the AI help me?

1. Confirm inputs.
2. Lay out stages.
3. Add content per stage.
4. Add metrics per stage.

## What will I get?

- Funnel map.
- Stage definitions.
- Content ideas per stage.
- Metrics per stage.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [audience-message-map](../01-content/003-audience-message-map.md)
- [campaign-plan](../02-business/045-campaign-plan.md)
- [email-sequence](../02-business/046-email-sequence.md)

## Recommended next steps

- campaign-plan (045)
- email-sequence (046)

---

## AI specification

```text
purpose: "Map the funnel from first contact to customer."
required_inputs:
  - offer
  - audience
  - channels
optional_inputs:
  - awareness stage
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a one-time launch — use campaign-plan (045)."
workflow:
  - "1. Confirm inputs."
  - "2. Lay out stages."
  - "3. Add content per stage."
  - "4. Add metrics per stage."
output_contract:
  - "funnel map"
  - "stage definitions"
  - "content per stage"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: funnel_map
    description: stage definitions and metrics
  - key: stage_content
    description: content ideas per stage
```