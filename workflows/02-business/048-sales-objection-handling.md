---
id: "048"
slug: "sales-objection-handling"
title: "Handle Sales Objections"
category: "business"
aliases:
  - objections
  - objection handling
  - sales rebuttal
triggers:
  - objection
  - sales objection
  - they said no
  - rebuttal
input_types:
  - objection
  - context
output_types:
  - response variants
  - redirect to next step
requires:
  - objection text
  - context (offer, stage, customer)
produces:
  - response variants
  - disqualification note
  - next-step suggestion
related:
  - cold-outreach
  - sales-page
  - retention-plan
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



# 048 — Handle Sales Objections

## What is this?

For each objection, produce a short response that acknowledges, reframes, and offers a concrete next step. Add a disqualification note when the objection signals a bad fit.

## Why use it?

Arguing with objections triggers more resistance. Acknowledging and reframing keeps the conversation alive.

## When should I use it?

- You're preparing for sales calls.
- A prospect raised an objection in writing.

## When should I not use it?

- You're losing customers after purchase — use retention-plan (051).

## What should I prepare?

- Objection text.
- Context of the deal.

## How does the AI help me?

1. Confirm objection and context.
2. Classify (price, trust, fit, timing).
3. Produce 2 response variants.
4. Suggest a next step.

## What will I get?

- Objection classification.
- 2 response variants.
- Next-step suggestion.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [cold-outreach](../02-business/047-cold-outreach.md)
- [sales-page](../02-business/043-sales-page.md)
- [retention-plan](../02-business/051-retention-plan.md)

## Recommended next steps

- retention-plan (051)
- cold-outreach (047)

---

## AI specification

```text
purpose: "Draft responses to common sales objections without arguing."
required_inputs:
  - objection text
  - context (offer, stage, customer)
optional_inputs:
  - history of the conversation
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're losing customers after purchase — use retention-plan (051)."
workflow:
  - "1. Confirm objection and context."
  - "2. Classify (price, trust, fit, timing)."
  - "3. Produce 2 response variants."
  - "4. Suggest a next step."
output_contract:
  - "response variants"
  - "disqualification note"
  - "next-step suggestion"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: classification
    description: objection category
  - key: response_variants
    description: response options
```