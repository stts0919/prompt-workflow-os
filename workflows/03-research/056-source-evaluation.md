---
id: "056"
slug: "source-evaluation"
title: "Evaluate a Source"
category: "research"
aliases:
  - source check
  - credibility
  - rate the source
triggers:
  - is this reliable
  - check this source
  - evaluate this article
input_types:
  - source link or text
output_types:
  - credibility assessment
requires:
  - source link or text
  - decision context
produces:
  - credibility assessment
  - bias flags
related:
  - fact-check
  - web-research-synthesis
  - research-question
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



# 056 — Evaluate a Source

## What is this?

Score the source on credibility (authorship, evidence, incentives) and relevance (recency, fit to the question). Flag known biases.

## Why use it?

Basing decisions on weak sources produces weak decisions. A structured evaluation surfaces issues you would otherwise skim past.

## When should I use it?

- You're about to cite a source in a decision document.
- You suspect a source is biased.

## When should I not use it?

- You're fact-checking specific claims — use fact-check (064).

## What should I prepare?

- Source link or text.
- Decision context.

## How does the AI help me?

1. Confirm inputs.
2. Score credibility.
3. Score relevance.
4. Flag bias risks.
5. Recommend how to use the source.

## What will I get?

- Credibility assessment.
- Relevance assessment.
- Bias flags.
- Usage recommendation.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [fact-check](../03-research/064-fact-check.md)
- [web-research-synthesis](../03-research/057-web-research-synthesis.md)
- [research-question](../03-research/054-research-question.md)

## Recommended next steps

- fact-check (064)
- evidence-matrix (065)

---

## AI specification

```text
purpose: "Evaluate the credibility and relevance of a source."
required_inputs:
  - source link or text
  - decision context
optional_inputs:
  - author
  - publication
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're fact-checking specific claims — use fact-check (064)."
workflow:
  - "1. Confirm inputs."
  - "2. Score credibility."
  - "3. Score relevance."
  - "4. Flag bias risks."
  - "5. Recommend how to use the source."
output_contract:
  - "credibility assessment"
  - "bias flags"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: credibility_score
    description: numeric credibility score with rationale
  - key: bias_flags
    description: list of detected biases
```