---
id: "045"
slug: "campaign-plan"
title: "Plan a Campaign"
category: "business"
aliases:
  - campaign
  - launch plan
  - marketing campaign
triggers:
  - campaign plan
  - launch plan
  - marketing campaign
input_types:
  - goal
  - audience
  - channels
output_types:
  - campaign plan
  - timeline
  - assets list
requires:
  - campaign goal
  - audience
  - channels
  - timeline
produces:
  - campaign plan
  - channel mix
  - asset list
  - timeline
related:
  - marketing-funnel
  - email-sequence
  - content-calendar
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



# 045 — Plan a Campaign

## What is this?

Build a campaign plan with objectives, audience, channel mix, asset list, timeline, and measurement plan.

## Why use it?

Campaigns without a plan collapse into ad-hoc execution. A simple plan makes the team aligned and accountable.

## When should I use it?

- You're launching a product or feature.
- You want a one-time push for a promotion.

## When should I not use it?

- You need a steady-state calendar — use content-calendar (004).

## What should I prepare?

- Campaign goal.
- Audience.
- Channels and timeline.

## How does the AI help me?

1. Confirm goal, audience, channels.
2. Pick the channel mix.
3. List assets per channel.
4. Timeline with milestones.
5. Measurement plan.

## What will I get?

- Campaign plan.
- Asset list.
- Timeline.
- Measurement plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [marketing-funnel](../02-business/044-marketing-funnel.md)
- [email-sequence](../02-business/046-email-sequence.md)
- [content-calendar](../01-content/004-content-calendar.md)

## Recommended next steps

- email-sequence (046)
- content-calendar (004)

---

## AI specification

```text
purpose: "Plan a multi-channel campaign for a defined period."
required_inputs:
  - campaign goal
  - audience
  - channels
  - timeline
optional_inputs:
  - budget
  - assets
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You need a steady-state calendar — use content-calendar (004)."
workflow:
  - "1. Confirm goal, audience, channels."
  - "2. Pick the channel mix."
  - "3. List assets per channel."
  - "4. Timeline with milestones."
  - "5. Measurement plan."
output_contract:
  - "campaign plan"
  - "channel mix"
  - "asset list"
  - "timeline"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: campaign_plan
    description: asset list and timeline
  - key: measurement_plan
    description: KPIs and tracking
```