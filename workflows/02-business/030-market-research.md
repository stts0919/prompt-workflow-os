---
id: "030"
slug: "market-research"
title: "Plan Market Research"
category: "business"
aliases:
  - market research
  - research plan
  - market intel
triggers:
  - research the market
  - market research plan
  - industry overview
  - size the market
input_types:
  - market
  - research goal
  - existing knowledge
output_types:
  - research plan
  - key questions
  - source list
requires:
  - market or industry
  - research goal
  - existing knowledge gaps
produces:
  - research plan
  - key questions
  - suggested sources
related:
  - research-plan
  - competitor-analysis
  - customer-interview
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



# 030 — Plan Market Research

## What is this?

Build a research plan that names the questions, the methods, the sources, and the timeline. It clarifies what is in scope and what to skip.

## Why use it?

Most market research drowns the reader in facts and skips the questions. A plan makes the research answer real decisions.

## When should I use it?

- You're entering a new market or category.
- A leadership question needs evidence-based support.
- A consultant or agency needs a clear brief.

## When should I not use it?

- You need quick competitive intel — use competitor-analysis (034).
- You need to talk to customers — use customer-interview (032).

## What should I prepare?

- Market or industry.
- Decision the research must support.
- Existing knowledge and known gaps.

## How does the AI help me?

1. Confirm decision and audience.
2. List 5–9 research questions ranked by impact.
3. Pick methods (web research, interviews, surveys, datasets).
4. Suggest primary sources.
5. Output a one-page research plan.

## What will I get?

- One-page research plan.
- Ranked research questions.
- Suggested sources.
- Next-workflow suggestion: web-research-synthesis (057).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [research-plan](../03-research/055-research-plan.md)
- [competitor-analysis](../02-business/034-competitor-analysis.md)
- [customer-interview](../02-business/032-customer-interview.md)

## Recommended next steps

- web-research-synthesis (057)
- customer-interview (032)

---

## AI specification

```text
purpose: "Design a focused market-research approach."
required_inputs:
  - market or industry
  - research goal
  - existing knowledge gaps
optional_inputs:
  - timeline
  - budget
  - audience for the research output
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You need quick competitive intel — use competitor-analysis (034)."
  - "You need to talk to customers — use customer-interview (032)."
workflow:
  - "1. Confirm decision and audience."
  - "2. List 5–9 research questions ranked by impact."
  - "3. Pick methods (web research, interviews, surveys, datasets)."
  - "4. Suggest primary sources."
  - "5. Output a one-page research plan."
output_contract:
  - "research plan"
  - "key questions"
  - "suggested sources"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: research_plan
    description: ranked questions, methods, sources
  - key: decision_context
    description: the decision the research must inform
```