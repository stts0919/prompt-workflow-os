---
id: "005"
slug: "topic-prioritization"
title: "Prioritize Content Topics"
category: "content"
aliases:
  - rank topics
  - topic scoring
  - decide what to write
triggers:
  - which topic first
  - rank my ideas
  - score my backlog
  - what to write next
input_types:
  - topic list
  - scoring criteria
output_types:
  - ranked list
  - scoring table
  - recommended top 3
requires:
  - list of topics or ideas
  - scoring criteria (audience fit, novelty, effort, business value)
produces:
  - ranked list
  - scoring breakdown
  - top-3 recommendation with rationale
related:
  - content-idea-generation
  - content-calendar
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



# 005 — Prioritize Content Topics

## What is this?

Apply a transparent scoring rubric to every topic. Surface the top 3 with rationale, and call out the bottom of the list so it can be cut.

## Why use it?

Backlogs grow faster than publishing capacity. Without explicit scoring, pet topics win and high-leverage ones starve.

## When should I use it?

- You have a backlog but no shipping decision.
- Your team disagrees on priority.
- You want to defend cuts in a backlog.

## When should I not use it?

- You don't have a backlog — start with content-idea-generation (001).
- You need to ship a single urgent thing — skip prioritization.

## What should I prepare?

- Topic list (5–30 items).
- Scoring criteria (e.g., audience fit, novelty, ease, business value).
- Optional weighting for each criterion.

## How does the AI help me?

1. Confirm scoring criteria and weights.
2. Score each topic transparently.
3. Output the ranked list with rationale per topic.
4. Recommend top 3 to feed into article-outline (006).

## What will I get?

- Ranked list.
- Scoring table.
- Top-3 recommendation.
- Suggested next workflow: article-outline (006).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-idea-generation](../01-content/001-content-idea-generation.md)
- [content-calendar](../01-content/004-content-calendar.md)

## Recommended next steps

- article-outline (006)

---

## AI specification

```text
purpose: "Score and rank a backlog of topics so the next piece is the highest-leverage one."
required_inputs:
  - list of topics or ideas
  - scoring criteria (audience fit, novelty, effort, business value)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You don't have a backlog — start with content-idea-generation (001)."
  - "You need to ship a single urgent thing — skip prioritization."
workflow:
  - "1. Confirm scoring criteria and weights."
  - "2. Score each topic transparently."
  - "3. Output the ranked list with rationale per topic."
  - "4. Recommend top 3 to feed into article-outline (006)."
output_contract:
  - "ranked list"
  - "scoring breakdown"
  - "top-3 recommendation with rationale"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: ranked_topics
    description: ranked list with scores
  - key: scoring_rubric
    description: criteria and weights
```