---
id: "018"
slug: "podcast-interview"
title: "Plan a Podcast Interview"
category: "content"
aliases:
  - podcast prep
  - interview questions
  - guest interview prep
triggers:
  - podcast prep
  - interview questions
  - guest interview
  - talk show prep
input_types:
  - guest
  - topic
  - show tone
output_types:
  - interview brief
  - questions
  - follow-ups
requires:
  - guest profile
  - topic
  - show tone and audience
produces:
  - interview brief
  - questions sequenced by arc
  - follow-ups
  - call-to-action
related:
  - presentation-story
  - short-video-script
  - audience-message-map
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



# 018 — Plan a Podcast Interview

## What is this?

Build a one-page brief, an arc of 8–14 questions, follow-ups, and a closing CTA — all in service of an engaging interview that serves the listener.

## Why use it?

Most podcast interviews meander. A pre-built arc and follow-ups keep the conversation on track without feeling scripted.

## When should I use it?

- You're hosting a guest.
- You're preparing to be interviewed.

## When should I not use it?

- You're running an internal team meeting — use meeting-agenda (078).
- You're speaking without an audience Q&A — use presentation-story (019).

## What should I prepare?

- Guest profile and bio.
- Topic and key angles.
- Show tone.

## How does the AI help me?

1. Confirm tone and audience.
2. Draft an interview brief (5 bullets).
3. Sequence 8–14 questions by arc.
4. Add follow-ups and a closing CTA.

## What will I get?

- Interview brief.
- Sequenced questions.
- Follow-ups.
- Closing CTA.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [presentation-story](../01-content/019-presentation-story.md)
- [short-video-script](../01-content/015-short-video-script.md)
- [audience-message-map](../01-content/003-audience-message-map.md)

## Recommended next steps

- meeting-notes (079)
- content-repurposing (028)

---

## AI specification

```text
purpose: "Prepare a podcast interview: brief, sequenced questions, follow-ups, and CTA."
required_inputs:
  - guest profile
  - topic
  - show tone and audience
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're running an internal team meeting — use meeting-agenda (078)."
  - "You're speaking without an audience Q&A — use presentation-story (019)."
workflow:
  - "1. Confirm tone and audience."
  - "2. Draft an interview brief (5 bullets)."
  - "3. Sequence 8–14 questions by arc."
  - "4. Add follow-ups and a closing CTA."
output_contract:
  - "interview brief"
  - "questions sequenced by arc"
  - "follow-ups"
  - "call-to-action"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: interview_brief
    description: the brief and question arc
  - key: follow_ups
    description: list of follow-up questions
```