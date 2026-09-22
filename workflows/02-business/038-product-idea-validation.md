---
id: "038"
slug: "product-idea-validation"
title: "Validate a Product Idea"
category: "business"
aliases:
  - idea validation
  - validate idea
  - test demand
triggers:
  - validate my idea
  - test demand
  - is this idea worth it
  - validate a product
input_types:
  - idea
  - customer
  - market
output_types:
  - validation plan
  - experiments
requires:
  - idea summary
  - customer profile
  - market context
produces:
  - validation plan
  - experiment designs
  - success criteria
related:
  - customer-interview
  - pricing-strategy
  - mvp-scope
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



# 038 — Validate a Product Idea

## What is this?

Plan 2–4 low-cost experiments (interviews, smoke-tests, prototypes, landing pages) with explicit success criteria and decision rules.

## Why use it?

Most products fail from not from engineering but from lack of demand. Cheap experiments reduce risk before heavy investment.

## When should I use it?

- You have a new product or feature concept.
- You're deciding between two directions.

## When should I not use it?

- You're scoping the build — use mvp-scope (039) after validation.

## What should I prepare?

- Idea summary.
- Customer profile.
- Market context.

## How does the AI help me?

1. Confirm idea and riskiest assumption.
2. Design 2–4 experiments with success criteria.
3. Sequence cheap before expensive.
4. Define go / no-go rules.

## What will I get?

- Validation plan.
- Experiments.
- Go / no-go rules.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-interview](../02-business/032-customer-interview.md)
- [pricing-strategy](../02-business/041-pricing-strategy.md)
- [mvp-scope](../02-business/039-mvp-scope.md)

## Recommended next steps

- mvp-scope (039)
- pricing-strategy (041)

---

## AI specification

```text
purpose: "Design experiments to test demand and desirability."
required_inputs:
  - idea summary
  - customer profile
  - market context
optional_inputs:
  - budget
  - timeline
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're scoping the build — use mvp-scope (039) after validation."
workflow:
  - "1. Confirm idea and riskiest assumption."
  - "2. Design 2–4 experiments with success criteria."
  - "3. Sequence cheap before expensive."
  - "4. Define go / no-go rules."
output_contract:
  - "validation plan"
  - "experiment designs"
  - "success criteria"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: validation_plan
    description: ordered experiments
  - key: go_no_go_rules
    description: decision thresholds
```