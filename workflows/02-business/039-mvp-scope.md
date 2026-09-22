---
id: "039"
slug: "mvp-scope"
title: "Define MVP Scope"
category: "business"
aliases:
  - mvp
  - minimum viable product
  - scope cut
  - v1 scope
triggers:
  - mvp
  - minimum viable
  - cut scope
  - v1 scope
input_types:
  - product idea
  - validation results
  - constraints
output_types:
  - MVP scope card
  - non-goals
requires:
  - product idea
  - validation results
  - constraints (time, team, money)
produces:
  - MVP scope card
  - non-goals list
  - success criteria
related:
  - product-idea-validation
  - product-roadmap
  - agent-task-spec
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



# 039 — Define MVP Scope

## What is this?

Cut a long wish list into the smallest scope that could still produce learning or value. Explicitly list what is not in scope.

## Why use it?

MVPs that try to be MRPs (minimally respectable products) rarely ship. A ruthless scope accelerates learning.

## When should I use it?

- You finished idea validation.
- Your team keeps adding features.

## When should I not use it?

- You don't have validation yet — use product-idea-validation (038) first.

## What should I prepare?

- Product idea and validation results.
- Constraints.

## How does the AI help me?

1. List candidate features.
2. Rank by learning value per cost.
3. Cut to MVP scope.
4. Enumerate non-goals.

## What will I get?

- MVP scope card.
- Non-goals list.
- Success criteria.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [product-idea-validation](../02-business/038-product-idea-validation.md)
- [product-roadmap](../02-business/040-product-roadmap.md)
- [agent-task-spec](../05-technical/091-agent-task-spec.md)

## Recommended next steps

- product-roadmap (040)
- agent-task-spec (091)

---

## AI specification

```text
purpose: "Define the smallest viable scope for an experiment or product."
required_inputs:
  - product idea
  - validation results
  - constraints (time, team, money)
optional_inputs:
  - tech stack
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You don't have validation yet — use product-idea-validation (038) first."
workflow:
  - "1. List candidate features."
  - "2. Rank by learning value per cost."
  - "3. Cut to MVP scope."
  - "4. Enumerate non-goals."
output_contract:
  - "MVP scope card"
  - "non-goals list"
  - "success criteria"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: mvp_scope
    description: in-scope features
  - key: non_goals
    description: explicit out-of-scope list
```