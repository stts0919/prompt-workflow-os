---
id: "026"
slug: "comment-response"
title: "Draft Comment Responses"
category: "content"
aliases:
  - reply
  - comment reply
  - public response
triggers:
  - reply to comment
  - respond publicly
  - draft a reply
  - comment response
input_types:
  - comment text
  - tone
  - context
output_types:
  - response variant(s)
requires:
  - comment or question
  - tone (warm, neutral, firm)
  - context (post, video, etc.)
produces:
  - response variants
  - rationale per variant
related:
  - faq-creation
  - social-post
  - brand-voice-guide
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
  default_style_profile: zh-tw-conversational-help
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: standard
handoff:
  - key: context
    description: "summary of upstream context"
---



# 026 — Draft Comment Responses

## What is this?

Draft one to three response variants calibrated to tone and context. Flag comments that should escalate or be ignored.

## Why use it?

Public replies shape how others see your brand. A polite, useful reply builds trust; a defensive one erodes it.

## When should I use it?

- You're responding to comments on posts or videos.
- You're facing a sensitive public question.

## When should I not use it?

- You're writing a private email — use newsletter (011) or email-sequence (046).
- The question needs legal or compliance review — escalate.

## What should I prepare?

- Comment text.
- Tone.
- Context (post, article, etc.).

## How does the AI help me?

1. Classify the comment (question, complaint, agreement, troll).
2. Recommend a response strategy.
3. Draft 1–3 variants.
4. Flag comments that should be escalated.

## What will I get?

- Response variants.
- Strategy per variant.
- Escalation flag if relevant.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [faq-creation](../01-content/022-faq-creation.md)
- [social-post](../01-content/012-social-post.md)
- [brand-voice-guide](../01-content/023-brand-voice-guide.md)

## Recommended next steps

- faq-creation (022)

---

## AI specification

```text
purpose: "Draft useful replies to public comments or questions."
required_inputs:
  - comment or question
  - tone (warm, neutral, firm)
  - context (post, video, etc.)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're writing a private email — use newsletter (011) or email-sequence (046)."
  - "The question needs legal or compliance review — escalate."
workflow:
  - "1. Classify the comment (question, complaint, agreement, troll)."
  - "2. Recommend a response strategy."
  - "3. Draft 1–3 variants."
  - "4. Flag comments that should be escalated."
output_contract:
  - "response variants"
  - "rationale per variant"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: responses
    description: response variants
```