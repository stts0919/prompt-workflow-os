---
id: "096"
slug: "data-exploration"
title: "Explore a Dataset"
category: "technical"
aliases:
  - explore data
  - data exploration
  - EDA
triggers:
  - explore this data
  - eda
  - what's in this dataset
input_types:
  - dataset
output_types:
  - exploration report
requires:
  - dataset (path or sample)
  - exploration goal
produces:
  - summary stats
  - distributions
  - anomalies
  - questions
related:
  - data-analysis
  - data-extraction
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



# 096 — Explore a Dataset

## What is this?

Run structured EDA: shape, types, missing values, distributions, correlations, anomalies, and 5 questions worth answering next.

## Why use it?

Most analyses skip exploration and produce fragile findings. EDA grounds the rest of the analysis.

## When should I use it?

- You just received a dataset.
- You want to know what's in it before modeling.

## When should I not use it?

- You're answering a specific question — use data-analysis (097).

## What should I prepare?

- Dataset.
- Exploration goal.

## How does the AI help me?

1. Confirm dataset and goal.
2. Run EDA.
3. Surface anomalies.
4. List next questions.

## What will I get?

- Summary stats.
- Distributions.
- Anomalies.
- 5 next questions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [data-analysis](../05-technical/097-data-analysis.md)
- [data-extraction](../03-research/060-data-extraction.md)

## Recommended next steps

- data-analysis (097)

---

## AI specification

```text
purpose: "Run structured EDA on a dataset."
required_inputs:
  - dataset (path or sample)
  - exploration goal
optional_inputs:
  - columns of interest
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're answering a specific question — use data-analysis (097)."
workflow:
  - "1. Confirm dataset and goal."
  - "2. Run EDA."
  - "3. Surface anomalies."
  - "4. List next questions."
output_contract:
  - "summary stats"
  - "distributions"
  - "anomalies"
  - "questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: eda_report
    description: exploration findings
  - key: anomalies
    description: anomalies and warnings
```