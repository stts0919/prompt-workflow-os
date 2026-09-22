---
id: "051"
slug: "retention-plan"
title: "Design a Retention Plan"
category: "business"
aliases:
  - retention
  - churn
  - customer retention
triggers:
  - retention
  - churn plan
  - reduce churn
  - keep customers
input_types:
  - product
  - current churn signals
  - customer segments
output_types:
  - retention plan
  - trigger matrix
requires:
  - product
  - current churn signals
  - segments
produces:
  - retention plan
  - trigger-based actions
  - measurement plan
related:
  - customer-journey
  - customer-feedback-analysis
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



# 051 — Design a Retention Plan

## What is this?

Build a retention plan with key churn signals, trigger-based actions, and a measurement approach (e.g., cohort retention curves).

## Why use it?

Retention compounds. A small improvement in churn is worth more than aggressive acquisition.

## When should I use it?

- You're noticing churn or downgrade signals.
- You want to launch a habit / loyalty feature.

## When should I not use it?

- You're optimizing acquisition only — use marketing-funnel (044).

## What should I prepare?

- Product context.
- Current churn or downgrade signals.
- Segments.

## How does the AI help me?

1. Confirm inputs.
2. Map churn triggers.
3. Design trigger-based actions.
4. Define measurement.

## What will I get?

- Trigger matrix.
- Action playbook.
- Measurement plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-journey](../02-business/050-customer-journey.md)
- [customer-feedback-analysis](../02-business/033-customer-feedback-analysis.md)
- [email-sequence](../02-business/046-email-sequence.md)

## Recommended next steps

- customer-feedback-analysis (033)
- email-sequence (046)

---

## AI specification

```text
purpose: "Reduce churn with a trigger-based retention plan."
required_inputs:
  - product
  - current churn signals
  - segments
optional_inputs:
  - interview notes
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're optimizing acquisition only — use marketing-funnel (044)."
workflow:
  - "1. Confirm inputs."
  - "2. Map churn triggers."
  - "3. Design trigger-based actions."
  - "4. Define measurement."
output_contract:
  - "retention plan"
  - "trigger-based actions"
  - "measurement plan"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: trigger_matrix
    description: triggers and matching actions
  - key: measurement_plan
    description: cohort or NPS tracking
```