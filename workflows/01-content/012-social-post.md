---
id: "012"
slug: "social-post"
title: "Create a Social Post"
category: "content"
aliases:
  - social media post
  - linkedin post
  - twitter post
  - x post
  - instagram caption
triggers:
  - write a post
  - linkedin post
  - tweet
  - instagram caption
  - social post
input_types:
  - topic
  - platform
  - voice
output_types:
  - post copy
  - hashtag suggestions
requires:
  - topic or hook
  - platform (X, LinkedIn, Instagram, etc.)
  - voice guide
produces:
  - platform-aware post
  - alternative versions
  - hashtag suggestions
related:
  - thread-series
  - video-hook
  - content-repurposing
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
  default_style_profile: zh-tw-friendly-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 012 — Create a Social Post

## What is this?

Write a platform-aware social post with a strong hook, clear structure, and a soft call to action. Adapt length and tone to the platform's norms.

## Why use it?

Posts that ignore platform norms underperform. The same message must be reframed for X, LinkedIn, Instagram, etc.

## When should I use it?

- You're publishing one post.
- You're testing an angle quickly.

## When should I not use it?

- You want a multi-post narrative — use thread-series (013).
- You want a carousel — use carousel (014).

## What should I prepare?

- Topic or hook.
- Platform.
- Voice reference.

## How does the AI help me?

1. Confirm platform and audience.
2. Generate a hook (first line / first 7 words).
3. Write the post adapting length and structure.
4. Suggest hashtag or mention conventions.
5. Provide 1–2 alternate versions.

## What will I get?

- Platform-aware post.
- 1–2 alternate versions.
- Hashtag / mention suggestions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [thread-series](../01-content/013-thread-series.md)
- [video-hook](../01-content/016-video-hook.md)
- [content-repurposing](../01-content/028-content-repurposing.md)

## Recommended next steps

- thread-series (013)
- content-quality-review (029)

---

## AI specification

```text
purpose: "Create a single social post adapted to platform, audience, and voice."
required_inputs:
  - topic or hook
  - platform (X, LinkedIn, Instagram, etc.)
  - voice guide
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want a multi-post narrative — use thread-series (013)."
  - "You want a carousel — use carousel (014)."
workflow:
  - "1. Confirm platform and audience."
  - "2. Generate a hook (first line / first 7 words)."
  - "3. Write the post adapting length and structure."
  - "4. Suggest hashtag or mention conventions."
  - "5. Provide 1–2 alternate versions."
output_contract:
  - "platform-aware post"
  - "alternative versions"
  - "hashtag suggestions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: post_copy
    description: the social post text
  - key: platform
    description: target platform
```