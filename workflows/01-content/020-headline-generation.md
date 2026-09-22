---
id: "020"
slug: "headline-generation"
title: "Generate Headlines"
category: "content"
aliases:
  - headlines
  - titles
  - subject lines
  - headline ideas
triggers:
  - headline
  - title ideas
  - subject line
  - click-worthy title
input_types:
  - content summary
  - audience
  - channel
output_types:
  - headline variants
  - rationale
requires:
  - content summary or angle
  - audience
  - channel
produces:
  - ranked headline variants
  - rationale per headline
related:
  - video-hook
  - social-post
  - article-outline
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



# 020 — Generate Headlines

## What is this?

Produce multiple headline variants across styles (curiosity, benefit, contrarian, how-to, numeric). Rank them and explain why each should or shouldn't be picked.

## Why use it?

The headline is the most leveraged sentence in any piece. Even a great article can be flattened by a weak title.

## When should I use it?

- You're publishing an article, post, or email and need a title.
- You want to A/B test multiple options.

## When should I not use it?

- You're writing a full article — start with article-outline (006).

## What should I prepare?

- Content summary.
- Audience.
- Channel (search, social, email).

## How does the AI help me?

1. Confirm summary, audience, and channel.
2. Generate 15+ variants across styles.
3. Rank the top 5 with rationale.
4. Note channels where each variant fits best.

## What will I get?

- 15+ headline variants.
- Top-5 recommendation with rationale.
- Channel notes per headline.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [video-hook](../01-content/016-video-hook.md)
- [social-post](../01-content/012-social-post.md)
- [article-outline](../01-content/006-article-outline.md)

## Recommended next steps

- article-outline (006)
- social-post (012)

---

## AI specification

```text
purpose: "Generate and rank headlines for articles, posts, and subject lines."
required_inputs:
  - content summary or angle
  - audience
  - channel
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're writing a full article — start with article-outline (006)."
workflow:
  - "1. Confirm summary, audience, and channel."
  - "2. Generate 15+ variants across styles."
  - "3. Rank the top 5 with rationale."
  - "4. Note channels where each variant fits best."
output_contract:
  - "ranked headline variants"
  - "rationale per headline"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: headlines
    description: ranked headline variants
  - key: chosen_headline
    description: user-selected headline
```