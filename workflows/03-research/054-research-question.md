---
id: "054"
slug: "research-question"
title: "Define Research Questions"
category: "research"
aliases:
  - research questions
  - questions to research
triggers:
  - research question
  - what should we ask
  - what do we need to know
input_types:
  - topic
  - goal
output_types:
  - question list
  - decision relevance
requires:
  - topic
  - research goal
produces:
  - ranked question list
  - decision relevance per question
related:
  - research-plan
  - web-research-synthesis
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



# 054 — Define Research Questions

## What is this?

Produce a ranked list of research questions, each annotated with why the answer matters for the decision.

## Why use it?

Most research is unfocused because the questions were never written down. Defining questions first turns research from a chore into an answer-finding mission.

## When should I use it?

- You're commissioning research.
- You're starting an investigation and need focus.

## When should I not use it?

- You're planning the research method itself — use research-plan (055).

## What should I prepare?

- Topic.
- Research goal.

## How does the AI help me?

1. Confirm the decision context.
2. Brainstorm candidate questions.
3. Rank by decision relevance.
4. Drop low-value questions.

## What will I get?

- Ranked research question list.
- Decision relevance per question.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [research-plan](../03-research/055-research-plan.md)
- [web-research-synthesis](../03-research/057-web-research-synthesis.md)

## Recommended next steps

- research-plan (055)

---

## AI specification

```text
purpose: "Frame the questions a piece of research must answer."
required_inputs:
  - topic
  - research goal
optional_inputs:
  - audience
  - timeline
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're planning the research method itself — use research-plan (055)."
workflow:
  - "1. Confirm the decision context."
  - "2. Brainstorm candidate questions."
  - "3. Rank by decision relevance."
  - "4. Drop low-value questions."
output_contract:
  - "ranked question list"
  - "decision relevance per question"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: research_questions
    description: ranked list with rationale
```