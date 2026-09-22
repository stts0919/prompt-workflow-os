---
id: "010"
slug: "content-summary"
title: "Summarize Content"
category: "content"
aliases:
  - summarize
  - summary
  - tldr
  - shorten
triggers:
  - summarize this
  - give me a summary
  - shorten this
  - tldr
input_types:
  - content (article, video transcript, document)
output_types:
  - summary
  - key takeaways
requires:
  - content to summarize
  - reader and use case
produces:
  - summary tailored to reader
  - 5 key takeaways
  - one-paragraph synopsis
related:
  - document-summary
  - article-draft
  - content-repurposing
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



# 010 — Summarize Content

## What is this?

Read the supplied content and produce a summary sized to a specific reader and use case. Default to a one-paragraph synopsis plus 5 takeaways. Adjust when the user specifies.

## Why use it?

Reading time is expensive. Summaries let the user decide quickly whether to dive deeper, and they feed into other workflows.

## When should I use it?

- You're deciding whether to read an article or watch a video.
- You need a brief for a meeting.
- You want to repurpose the core of someone else's piece.

## When should I not use it?

- You're summarizing a long internal document — use document-summary (058) for richer structure.
- You're rebuilding the article — use article-rewrite (008).

## What should I prepare?

- Content to summarize.
- Reader (you, your team, executives, etc.).
- Use case (decision prep, briefing, newsletter).

## How does the AI help me?

1. Read the content.
2. Identify the central claim and supporting points.
3. Write a synopsis, then 5 takeaways, then a "why this matters" line.
4. Flag any factual claim that needs verification.

## What will I get?

- One-paragraph synopsis.
- 5 key takeaways.
- Why-it-matters line.
- Suggested next workflow based on use case.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [document-summary](../03-research/058-document-summary.md)
- [article-draft](../01-content/007-article-draft.md)
- [content-repurposing](../01-content/028-content-repurposing.md)

## Recommended next steps

- article-rewrite (008)
- content-repurposing (028)

---

## AI specification

```text
purpose: "Summarize content for a specific reader and use case."
required_inputs:
  - content to summarize
  - reader and use case
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're summarizing a long internal document — use document-summary (058) for richer structure."
  - "You're rebuilding the article — use article-rewrite (008)."
workflow:
  - "1. Read the content."
  - "2. Identify the central claim and supporting points."
  - "3. Write a synopsis, then 5 takeaways, then a "why this matters" line."
  - "4. Flag any factual claim that needs verification."
output_contract:
  - "summary tailored to reader"
  - "5 key takeaways"
  - "one-paragraph synopsis"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: summary
    description: tailored summary text
  - key: takeaways
    description: bullet takeaways
```