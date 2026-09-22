---
id: "069"
slug: "decision-memo"
title: "Write a Decision Memo"
category: "research"
aliases:
  - decision memo
  - decision document
  - recommendation memo
triggers:
  - decision memo
  - recommendation
  - decide this
input_types:
  - decision
  - options
  - evidence
output_types:
  - decision memo
requires:
  - decision statement
  - options
  - evidence or criteria
produces:
  - decision memo
  - options table
  - next steps
related:
  - executive-brief
  - evidence-matrix
  - business-decision
playbooks:
  - research-before-a-decision
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



# 069 — Write a Decision Memo

## What is this?

Write a 1–2 page memo: decision, criteria, options, recommendation, trade-offs, next steps, and open questions.

## Why use it?

Most decisions are made on the back of imprecise arguments. A memo forces clarity, criteria, and trade-offs.

## When should I use it?

- A strategic decision needs written support.
- You want to brief executives.

## When should I not use it?

- You only need a one-page summary — use executive-brief (070).

## What should I prepare?

- Decision statement.
- Options.
- Evidence.

## How does the AI help me?

1. Confirm inputs.
2. Frame decision.
3. Compare options.
4. Recommend with conditions.
5. List next steps and risks.

## What will I get?

- Decision memo.
- Options table.
- Recommendation.
- Next steps and risks.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [executive-brief](../03-research/070-executive-brief.md)
- [evidence-matrix](../03-research/065-evidence-matrix.md)
- [business-decision](../02-business/052-business-decision.md)

## Recommended next steps

- executive-brief (070)
- scenario-planning (068)

---

## AI specification

```text
purpose: "Produce a decision-ready memo with options, criteria, and recommendation."
required_inputs:
  - decision statement
  - options
  - evidence or criteria
optional_inputs:
  - stakeholders
  - risks
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a one-page summary — use executive-brief (070)."
workflow:
  - "1. Confirm inputs."
  - "2. Frame decision."
  - "3. Compare options."
  - "4. Recommend with conditions."
  - "5. List next steps and risks."
output_contract:
  - "decision memo"
  - "options table"
  - "next steps"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: decision_memo
    description: 1–2 page memo
  - key: recommendation
    description: chosen option
```