---
id: "040"
slug: "product-roadmap"
title: "Create a Product Roadmap"
category: "business"
aliases:
  - roadmap
  - product plan
  - release plan
triggers:
  - product roadmap
  - release plan
  - what to build when
input_types:
  - product
  - strategy
  - constraints
output_types:
  - time-phased roadmap
requires:
  - product
  - strategy
  - team capacity
produces:
  - time-phased roadmap
  - themes per horizon
  - trade-off notes
related:
  - mvp-scope
  - goal-setting
  - task-breakdown
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



# 040 — Create a Product Roadmap

## What is this?

Group initiatives into horizons (now / next / later) and call out the trade-offs. Each horizon has a theme and 2–4 initiatives.

## Why use it?

Roadmaps without trade-offs are wish lists. Naming what you won't do is what makes a roadmap executable.

## When should I use it?

- You finished MVP scope and need to plan the next 6–12 months.
- Stakeholders want a single page showing what's coming.

## When should I not use it?

- You only need a sprint plan — use task-breakdown (072) or project-plan (076).

## What should I prepare?

- Product state.
- Strategy.
- Team capacity.

## How does the AI help me?

1. Confirm horizons (now / next / later).
2. Group themes per horizon.
3. List 2–4 initiatives each.
4. Add trade-off notes.

## What will I get?

- Time-phased roadmap.
- Trade-off notes.
- Next-workflow suggestion: project-plan (076).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [mvp-scope](../02-business/039-mvp-scope.md)
- [goal-setting](../04-workflow/075-goal-setting.md)
- [task-breakdown](../04-workflow/072-task-breakdown.md)

## Recommended next steps

- project-plan (076)
- task-breakdown (072)

---

## AI specification

```text
purpose: "Prioritize product work across time horizons."
required_inputs:
  - product
  - strategy
  - team capacity
optional_inputs:
  - priorities
  - dependencies
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a sprint plan — use task-breakdown (072) or project-plan (076)."
workflow:
  - "1. Confirm horizons (now / next / later)."
  - "2. Group themes per horizon."
  - "3. List 2–4 initiatives each."
  - "4. Add trade-off notes."
output_contract:
  - "time-phased roadmap"
  - "themes per horizon"
  - "trade-off notes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: roadmap
    description: horizon-grouped initiatives
  - key: trade_offs
    description: notes on what was deferred
```