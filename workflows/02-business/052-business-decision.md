---
id: "052"
slug: "business-decision"
title: "Make a Business Decision"
category: "business"
aliases:
  - business decision
  - strategic decision
  - go or no-go
triggers:
  - should we
  - go or no-go
  - business decision
  - make a call
input_types:
  - decision
  - options
  - criteria
output_types:
  - decision memo
requires:
  - decision statement
  - options considered
  - decision criteria
produces:
  - decision memo
  - trade-off table
  - next steps
related:
  - decision-memo
  - risk-stress-test
  - scenario-planning
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



# 052 — Make a Business Decision

## What is this?

Produce a decision memo with the decision statement, criteria, options, trade-offs, recommendation, and next steps.

## Why use it?

Most bad strategic decisions were never written down. A memo forces clarity and survives group-think.

## When should I use it?

- A major decision sits with leadership.
- You want to defend the call later.

## When should I not use it?

- The decision needs research first — use research-before-a-decision playbook.

## What should I prepare?

- Decision statement.
- Options considered.
- Decision criteria.

## How does the AI help me?

1. Confirm inputs.
2. Frame the decision.
3. Compare options against criteria.
4. Recommend with conditions.

## What will I get?

- Decision memo.
- Trade-off table.
- Recommendation.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [decision-memo](../03-research/069-decision-memo.md)
- [risk-stress-test](../02-business/053-risk-stress-test.md)
- [scenario-planning](../03-research/068-scenario-planning.md)

## Recommended next steps

- risk-stress-test (053)
- decision-memo (069)

---

## AI specification

```text
purpose: "Structure a strategic business decision before committing."
required_inputs:
  - decision statement
  - options considered
  - decision criteria
optional_inputs:
  - research sources
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The decision needs research first — use research-before-a-decision playbook."
workflow:
  - "1. Confirm inputs."
  - "2. Frame the decision."
  - "3. Compare options against criteria."
  - "4. Recommend with conditions."
output_contract:
  - "decision memo"
  - "trade-off table"
  - "next steps"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: decision_memo
    description: structured decision
  - key: trade_offs
    description: trade-off table
```