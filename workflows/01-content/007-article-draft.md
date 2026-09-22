---
id: "007"
slug: "article-draft"
title: "Draft an Article"
category: "content"
aliases:
  - write an article
  - draft post
  - long-form draft
triggers:
  - write the article
  - draft the post
  - give me a draft
  - compose the article
input_types:
  - outline or brief
  - voice guide
  - word count target
output_types:
  - first draft
requires:
  - outline or brief
  - target length
  - voice guide or sample
produces:
  - complete first draft
  - open assumptions
  - fact flags
related:
  - article-outline
  - article-rewrite
  - content-editing
  - content-quality-review
playbooks:
  - create-high-quality-content
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



# 007 — Draft an Article

## What is this?

Convert an outline into a full draft that hits the target length and voice. Flag every place where a fact needs verification.

## Why use it?

Outlines without drafts don't ship. The AI handles the mechanical writing so the user spends energy editing, not typing.

## When should I use it?

- You have an outline and want to draft.
- You have a brief with audience and angle and want a fast draft.

## When should I not use it?

- You don't have an outline — start with article-outline (006).
- You're revising an existing draft — use article-rewrite (008).

## What should I prepare?

- Outline or brief.
- Target word count.
- Voice guide or sample paragraphs.

## How does the AI help me?

1. Confirm the voice and length.
2. Draft section by section.
3. Insert `[fact-check]` flags where claims need verification.
4. End with a short Assumptions section.

## What will I get?

- Complete first draft.
- Inline fact-check flags.
- Assumptions section.
- Suggested next workflow: content-editing (009).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [article-outline](../01-content/006-article-outline.md)
- [article-rewrite](../01-content/008-article-rewrite.md)
- [content-editing](../01-content/009-content-editing.md)
- [content-quality-review](../01-content/029-content-quality-review.md)

## Recommended next steps

- content-editing (009)
- content-quality-review (029)

---

## AI specification

```text
purpose: "Produce a complete first draft from a confirmed outline or brief."
required_inputs:
  - outline or brief
  - target length
  - voice guide or sample
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You don't have an outline — start with article-outline (006)."
  - "You're revising an existing draft — use article-rewrite (008)."
workflow:
  - "1. Confirm the voice and length."
  - "2. Draft section by section."
  - "3. Insert `[fact-check]` flags where claims need verification."
  - "4. End with a short Assumptions section."
output_contract:
  - "complete first draft"
  - "open assumptions"
  - "fact flags"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: draft
    description: complete draft text
  - key: fact_check_flags
    description: inline markers where verification is required
```