---
id: "015"
slug: "short-video-script"
title: "Write a Short-Form Video Script"
category: "content"
aliases:
  - reels script
  - tiktok script
  - shorts script
  - short video script
triggers:
  - reels script
  - tiktok script
  - shorts script
  - short video
  - vertical video script
input_types:
  - topic
  - hook
  - platform
  - target length
output_types:
  - video script
  - shot list
  - caption draft
requires:
  - topic
  - hook idea
  - platform and length (15s/30s/60s/90s)
produces:
  - video script
  - shot list
  - caption draft
  - CTA draft
related:
  - video-hook
  - video-storyboard
  - social-post
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



# 015 — Write a Short-Form Video Script

## What is this?

Write a video script with the opening hook, the body beats, and the closing CTA. Include on-screen text, voice-over, and shot direction.

## Why use it?

Short video rewards tight structure. A scripted arc beats improvised rambling every time.

## When should I use it?

- You're scripting a Reel, TikTok, or Short.
- You have a hook idea but not the body.

## When should I not use it?

- You only need hooks — use video-hook (016).
- You're producing a long video — use video-storyboard (017).

## What should I prepare?

- Topic and angle.
- Target length.
- Platform conventions.

## How does the AI help me?

1. Confirm hook, length, platform.
2. Write the arc beats.
3. Add on-screen text, voice-over, and shot notes.
4. Draft the caption.

## What will I get?

- Video script.
- Shot list.
- Caption draft.
- Suggested next workflow: video-storyboard (017).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [video-hook](../01-content/016-video-hook.md)
- [video-storyboard](../01-content/017-video-storyboard.md)
- [social-post](../01-content/012-social-post.md)

## Recommended next steps

- video-storyboard (017)

---

## AI specification

```text
purpose: "Write a short-form video script tuned to platform, length, and audience."
required_inputs:
  - topic
  - hook idea
  - platform and length (15s/30s/60s/90s)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need hooks — use video-hook (016)."
  - "You're producing a long video — use video-storyboard (017)."
workflow:
  - "1. Confirm hook, length, platform."
  - "2. Write the arc beats."
  - "3. Add on-screen text, voice-over, and shot notes."
  - "4. Draft the caption."
output_contract:
  - "video script"
  - "shot list"
  - "caption draft"
  - "CTA draft"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: script
    description: the video script
  - key: shots
    description: ordered shot notes
```