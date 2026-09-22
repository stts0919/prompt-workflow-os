---
id: "097"
slug: "data-analysis"
title: "Answer a Question with Data"
category: "technical"
aliases:
  - analyze data
  - answer with data
  - data analysis
triggers:
  - answer with data
  - analyze the data
  - what does the data show
input_types:
  - dataset
  - question
output_types:
  - analysis
requires:
  - dataset
  - question
  - audience
produces:
  - answer with evidence
  - caveats
  - next questions
related:
  - data-exploration
  - data-extraction
  - decision-memo
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



# 097 — Answer a Question with Data

## What is this?

Plan the analysis, run it, and report the answer with caveats. Surface what's not in the data.

## Why use it?

Most "data answers" are guesses. A planned analysis that says what it can and can't conclude earns trust.

## When should I use it?

- You have a specific business question and clean data.
- You're preparing a chart or table for a decision.

## When should I not use it?

- You don't yet know the dataset — use data-exploration (096) first.

## What should I prepare?

- Dataset.
- Question.
- Audience.

## How does the AI help me?

1. Confirm question.
2. Plan analysis.
3. Run it.
4. Report answer + caveats.
5. Suggest next questions.

## What will I get?

- Answer with evidence.
- Caveats.
- Next questions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [data-exploration](../05-technical/096-data-exploration.md)
- [data-extraction](../03-research/060-data-extraction.md)
- [decision-memo](../03-research/069-decision-memo.md)

## Recommended next steps

- decision-memo (069)

---

## AI specification

```text
purpose: "Answer a specific question with data."
required_inputs:
  - dataset
  - question
  - audience
optional_inputs:
  - hypothesis
  - control variables
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You don't yet know the dataset — use data-exploration (096) first."
workflow:
  - "1. Confirm question."
  - "2. Plan analysis."
  - "3. Run it."
  - "4. Report answer + caveats."
  - "5. Suggest next questions."
output_contract:
  - "answer with evidence"
  - "caveats"
  - "next questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: answer
    description: structured answer
  - key: caveats
    description: known limitations
```