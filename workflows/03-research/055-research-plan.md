---
id: "055"
slug: "research-plan"
title: "Plan a Research Project"
category: "research"
aliases:
  - research plan
  - study plan
  - investigation plan
triggers:
  - research plan
  - study plan
  - how to research this
input_types:
  - research questions
  - constraints
output_types:
  - research plan
requires:
  - research questions
  - constraints (time, budget, tools)
produces:
  - research plan
  - method selection
  - timeline
related:
  - research-question
  - web-research-synthesis
  - evidence-matrix
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



# 055 — Plan a Research Project

## What is this?

Build a research plan with methods, source list, timeline, and decision-ready output format.

## Why use it?

Without a plan, research meanders and over-runs. A plan commits to methods and a deadline.

## When should I use it?

- You're starting a multi-day research project.
- You're scoping research for a client or stakeholder.

## When should I not use it?

- You only need a quick study — use web-research-synthesis (057).

## What should I prepare?

- Research questions.
- Constraints.

## How does the AI help me?

1. Confirm inputs.
2. Pick methods per question.
3. List primary sources.
4. Build a timeline.
5. Specify the output.

## What will I get?

- Research plan.
- Method selection.
- Timeline.
- Output spec.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [research-question](../03-research/054-research-question.md)
- [web-research-synthesis](../03-research/057-web-research-synthesis.md)
- [evidence-matrix](../03-research/065-evidence-matrix.md)

## Recommended next steps

- web-research-synthesis (057)
- evidence-matrix (065)

---

## AI specification

```text
purpose: "Plan a research project: methods, sources, timeline, deliverables."
required_inputs:
  - research questions
  - constraints (time, budget, tools)
optional_inputs:
  - primary sources
  - audience for the output
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need a quick study — use web-research-synthesis (057)."
workflow:
  - "1. Confirm inputs."
  - "2. Pick methods per question."
  - "3. List primary sources."
  - "4. Build a timeline."
  - "5. Specify the output."
output_contract:
  - "research plan"
  - "method selection"
  - "timeline"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: research_plan
    description: methods, sources, timeline
  - key: output_spec
    description: what the research will produce
```