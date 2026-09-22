---
id: "013"
slug: "thread-series"
title: "Create a Thread or Series"
category: "content"
aliases:
  - twitter thread
  - x thread
  - linkedin carousel as text
  - post series
  - narrative series
triggers:
  - thread
  - x thread
  - post series
  - carousel as text
input_types:
  - core idea
  - platform
  - number of posts
output_types:
  - post-by-post outline
  - first post variants
requires:
  - core idea
  - platform and conventions
  - target post count
produces:
  - post-by-post outline
  - post 1 hooks
  - call-to-action in final post
related:
  - social-post
  - carousel
  - article-outline
playbooks: []
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
  default_style_profile: zh-tw-threads-insightful
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 013 — Create a Thread or Series

## What is this?

Lay out an ordered series of posts that reads as one narrative. Each post stands alone but the sequence compounds. First and last posts are emphasized because they drive reach and conversion.

## Why use it?

A single post rarely has space to teach or persuade. A series lets a creator deliver value, build trust, and prompt action.

## When should I use it?

- You want to teach a short course on a platform.
- You have a complex story to tell in segments.

## When should I not use it?

- You only need one post — use social-post (012).
- Your content is slide-driven — use carousel (014).

## What should I prepare?

- Core idea.
- Target platform.
- Number of posts.

## How does the AI help me?

1. Plan the arc (setup → development → payoff).
2. Write a one-line beat per post.
3. Draft post 1 with hook variants.
4. Draft the closing post with CTA.
5. Hand off post bodies for the user to expand.

## What will I get?

- Post-by-post outline.
- Post 1 hook variants.
- Closing post with CTA.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [social-post](../01-content/012-social-post.md)
- [carousel](../01-content/014-carousel.md)
- [article-outline](../01-content/006-article-outline.md)

## Recommended next steps

- social-post (012)
- content-repurposing (028)

---

## AI specification

```text
purpose: "Turn a single idea into a multi-post thread or series tuned to platform conventions."
required_inputs:
  - core idea
  - platform and conventions
  - target post count
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need one post — use social-post (012)."
  - "Your content is slide-driven — use carousel (014)."
workflow:
  - "1. Plan the arc (setup → development → payoff)."
  - "2. Write a one-line beat per post."
  - "3. Draft post 1 with hook variants."
  - "4. Draft the closing post with CTA."
  - "5. Hand off post bodies for the user to expand."
output_contract:
  - "post-by-post outline"
  - "post 1 hooks"
  - "call-to-action in final post"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: series_outline
    description: ordered beats per post
  - key: post_1_hooks
    description: alternative openers
```