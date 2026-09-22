---
id: "065"
slug: "evidence-matrix"
title: "Build an Evidence Matrix"
category: "research"
aliases:
  - evidence matrix
  - weight evidence
  - claim evidence table
triggers:
  - evidence matrix
  - compare evidence
  - weight the evidence
input_types:
  - claims and evidence
output_types:
  - evidence matrix
requires:
  - claims
  - evidence items
  - criteria
produces:
  - claim × evidence matrix
  - weighted score per claim
related:
  - fact-check
  - decision-memo
  - reasoning-audit
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



# 065 — Build an Evidence Matrix

## What is this?

Build a matrix of claims × evidence pieces. Weight the evidence and score each claim. Identify the most and least supported claims.

## Why use it?

Decisions become defensible when the evidence behind them is visible. A matrix makes that visible.

## When should I use it?

- You're supporting or rejecting a strategic hypothesis.
- You're comparing two courses of action.

## When should I not use it?

- You want to verify one claim — use fact-check (064).

## What should I prepare?

- Claims.
- Evidence items.
- Criteria.

## How does the AI help me?

1. Build the matrix.
2. Apply weights.
3. Score claims.
4. Highlight outliers.

## What will I get?

- Evidence matrix.
- Weighted scores.
- Outlier claims.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [fact-check](../03-research/064-fact-check.md)
- [decision-memo](../03-research/069-decision-memo.md)
- [reasoning-audit](../03-research/066-reasoning-audit.md)

## Recommended next steps

- decision-memo (069)
- reasoning-audit (066)

---

## AI specification

```text
purpose: "Map claims to evidence and weight them."
required_inputs:
  - claims
  - evidence items
  - criteria
optional_inputs:
  - weighting
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want to verify one claim — use fact-check (064)."
workflow:
  - "1. Build the matrix."
  - "2. Apply weights."
  - "3. Score claims."
  - "4. Highlight outliers."
output_contract:
  - "claim × evidence matrix"
  - "weighted score per claim"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: matrix
    description: claim × evidence grid
  - key: scores
    description: weighted scores per claim
```