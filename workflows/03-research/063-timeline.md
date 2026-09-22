---
id: "063"
slug: "timeline"
title: "Build a Timeline"
category: "research"
aliases:
  - timeline
  - chronology
  - history
triggers:
  - timeline
  - chronology
  - history of
  - build a timeline
input_types:
  - events or sources
output_types:
  - timeline
requires:
  - events list or sources
  - time range
produces:
  - timeline
  - key inflection points
related:
  - document-summary
  - knowledge-map
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



# 063 — Build a Timeline

## What is this?

Read the sources and produce a timeline of events, each with date, summary, and source. Highlight inflection points.

## Why use it?

Timelines turn dense history into a story. They also expose patterns that are invisible in prose.

## When should I use it?

- You're preparing a history section.
- You're analyzing how a field evolved.

## When should I not use it?

- You need scenario planning — use scenario-planning (068).

## What should I prepare?

- Events or sources.
- Time range.

## How does the AI help me?

1. Confirm inputs.
2. Read sources.
3. Order events.
4. Highlight inflection points.

## What will I get?

- Timeline.
- Inflection points.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [document-summary](../03-research/058-document-summary.md)
- [knowledge-map](../03-research/062-knowledge-map.md)

## Recommended next steps

- document-summary (058)
- knowledge-map (062)

---

## AI specification

```text
purpose: "Order events into a clear timeline with inflection points."
required_inputs:
  - events list or sources
  - time range
optional_inputs:
  - significance
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You need scenario planning — use scenario-planning (068)."
workflow:
  - "1. Confirm inputs."
  - "2. Read sources."
  - "3. Order events."
  - "4. Highlight inflection points."
output_contract:
  - "timeline"
  - "key inflection points"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: timeline
    description: ordered events
  - key: inflection_points
    description: notable turning points
```