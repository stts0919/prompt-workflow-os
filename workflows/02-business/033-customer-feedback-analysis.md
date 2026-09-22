---
id: "033"
slug: "customer-feedback-analysis"
title: "Analyze Customer Feedback"
category: "business"
aliases:
  - feedback analysis
  - thematic analysis
  - review analysis
triggers:
  - analyze feedback
  - thematic analysis
  - review themes
  - feedback summary
input_types:
  - feedback transcripts or texts
output_types:
  - thematic report
  - quotes per theme
requires:
  - feedback corpus (transcripts, reviews, tickets)
produces:
  - thematic report
  - quotes per theme
  - recommendations
related:
  - customer-interview
  - customer-persona
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



# 033 — Analyze Customer Feedback

## What is this?

Group feedback into themes, count frequency, surface representative quotes, and propose 2–3 actions.

## Why use it?

Without structure, customer feedback is just complaining. With themes and counts, it becomes a roadmap input.

## When should I use it?

- You have 5+ interviews or 50+ tickets.
- You need to brief product or marketing on what customers say.

## When should I not use it?

- You have only one interview — read it directly with customer-interview (032).

## What should I prepare?

- Feedback corpus.
- Optional: research goal or segmentation.

## How does the AI help me?

1. Read the corpus.
2. Code themes.
3. Count frequency and surface quotes.
4. Recommend 2–3 actions.

## What will I get?

- Thematic report.
- Quotes per theme.
- Action recommendations.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [customer-interview](../02-business/032-customer-interview.md)
- [customer-persona](../02-business/031-customer-persona.md)

## Recommended next steps

- customer-persona (031)
- positioning (035)

---

## AI specification

```text
purpose: "Classify feedback and identify recurring patterns."
required_inputs:
  - feedback corpus (transcripts, reviews, tickets)
optional_inputs:
  - research goal
  - segments
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You have only one interview — read it directly with customer-interview (032)."
workflow:
  - "1. Read the corpus."
  - "2. Code themes."
  - "3. Count frequency and surface quotes."
  - "4. Recommend 2–3 actions."
output_contract:
  - "thematic report"
  - "quotes per theme"
  - "recommendations"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: themes
    description: themes with counts and quotes
  - key: recommendations
    description: 2–3 prioritized actions
```