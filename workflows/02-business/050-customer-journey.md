---
id: "050"
slug: "customer-journey"
title: "Map the Customer Journey"
category: "business"
aliases:
  - journey map
  - customer journey
  - touchpoints
triggers:
  - customer journey
  - touchpoints
  - journey map
  - user journey
input_types:
  - customer
  - stages
  - channels
output_types:
  - journey map
requires:
  - customer profile
  - stages
  - channels
produces:
  - journey map (stages × touchpoints)
  - pain points
  - moments of truth
related:
  - marketing-funnel
  - retention-plan
  - audience-message-map
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



# 050 — Map the Customer Journey

## What is this?

Produce a journey map: stages × touchpoints, with emotions, pain points, and moments of truth. Identify quick wins and structural fixes.

## Why use it?

A journey map makes moments of truth obvious. It also removes finger-pointing between teams because the journey is shared.

## When should I use it?

- You want to improve onboarding, conversion, or retention.
- Different teams disagree on where problems happen.

## When should I not use it?

- You only need a funnel for conversion — use marketing-funnel (044).

## What should I prepare?

- Customer profile.
- Stages (awareness, consideration, etc.).
- Channels.

## How does the AI help me?

1. Confirm inputs.
2. Build the map.
3. Identify pain points and moments of truth.
4. Recommend quick wins.

## What will I get?

- Journey map.
- Pain points.
- Moments of truth.
- Quick wins.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [marketing-funnel](../02-business/044-marketing-funnel.md)
- [retention-plan](../02-business/051-retention-plan.md)
- [audience-message-map](../01-content/003-audience-message-map.md)

## Recommended next steps

- retention-plan (051)
- marketing-funnel (044)

---

## AI specification

```text
purpose: "Map the customer journey across stages and touchpoints."
required_inputs:
  - customer profile
  - stages
  - channels
optional_inputs:
  - existing journey map
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a funnel for conversion — use marketing-funnel (044)."
workflow:
  - "1. Confirm inputs."
  - "2. Build the map."
  - "3. Identify pain points and moments of truth."
  - "4. Recommend quick wins."
output_contract:
  - "journey map (stages × touchpoints)"
  - "pain points"
  - "moments of truth"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: journey_map
    description: stages and touchpoints
  - key: moments_of_truth
    description: critical interactions
```