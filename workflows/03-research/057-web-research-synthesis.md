---
id: "057"
slug: "web-research-synthesis"
title: "Synthesize Web Research"
category: "research"
aliases:
  - research summary
  - synthesize
  - research synthesis
triggers:
  - research this online
  - what does the web say
  - synthesize findings
input_types:
  - topic
  - questions
output_types:
  - synthesis
  - source list
requires:
  - topic or question
  - recency sensitivity
produces:
  - synthesis
  - source list
  - verification log
related:
  - research-question
  - source-evaluation
  - fact-check
playbooks:
  - research-before-a-decision
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-tw-research-precise
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 057 — Synthesize Web Research

## What is this?

Read public sources, summarize findings by sub-question, and produce a synthesis with a source list and a verification log.

## Why use it?

Today's web is flooded with content. A synthesis separates signal from noise and tells the user what is solid and what is contested.

## When should I use it?

- You need current information on a topic.
- You're preparing for a decision and want to scan the landscape.

## When should I not use it?

- You have one document — use document-summary (058).
- You need to defend a specific claim — use fact-check (064).

## What should I prepare?

- Topic or question.
- Recency sensitivity.
- Output length.

## How does the AI help me?

1. Confirm inputs.
2. Pull current sources.
3. Group by sub-question.
4. Note disagreements and gaps.
5. Output the synthesis with sources.

## What will I get?

- Synthesis.
- Source list.
- Verification log.
- Next-workflow suggestion: fact-check (064) or evidence-matrix (065).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [research-question](../03-research/054-research-question.md)
- [source-evaluation](../03-research/056-source-evaluation.md)
- [fact-check](../03-research/064-fact-check.md)

## Recommended next steps

- fact-check (064)
- evidence-matrix (065)

---

## AI specification

```text
purpose: "Synthesize current public information on a topic."
required_inputs:
  - topic or question
  - recency sensitivity
optional_inputs:
  - authoritative sources preferred
  - regions
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You have one document — use document-summary (058)."
  - "You need to defend a specific claim — use fact-check (064)."
workflow:
  - "1. Confirm inputs."
  - "2. Pull current sources."
  - "3. Group by sub-question."
  - "4. Note disagreements and gaps."
  - "5. Output the synthesis with sources."
output_contract:
  - "synthesis"
  - "source list"
  - "verification log"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: synthesis
    description: topic synthesis
  - key: source_list
    description: cited sources with URL and date
```