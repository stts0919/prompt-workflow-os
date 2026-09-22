---
id: "019"
slug: "presentation-story"
title: "Build a Presentation Narrative"
category: "content"
aliases:
  - keynote structure
  - talk narrative
  - pitch deck story
triggers:
  - presentation
  - keynote
  - talk structure
  - pitch deck story
input_types:
  - topic
  - audience
  - length
output_types:
  - narrative arc
  - section beats
  - opening and closing
requires:
  - topic
  - audience profile
  - talk length
produces:
  - narrative arc
  - section beats
  - opening and closing
related:
  - presentation-story
  - storytelling
  - video-storyboard
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



# 019 — Build a Presentation Narrative

## What is this?

Design the narrative arc: opening hook, tension, payoff, call to action. Lay out section-by-section beats the speaker can deliver.

## Why use it?

Presentations fail when they recite information instead of telling a story. A clear arc gives the speaker something to land.

## When should I use it?

- You're preparing a talk or pitch.
- Your deck reads like a report and you need a story.

## When should I not use it?

- You only need the visual side — use video-storyboard (017).
- You're leading a meeting, not a presentation — use meeting-agenda (078).

## What should I prepare?

- Topic and audience.
- Length.
- One-line core message.

## How does the AI help me?

1. Confirm audience and length.
2. Draft the narrative arc.
3. Lay out section beats.
4. Write the opening hook and the closing call to action.

## What will I get?

- Narrative arc.
- Section beats.
- Opening and closing copy.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [presentation-story](../01-content/019-presentation-story.md)
- [storytelling](../01-content/024-storytelling.md)
- [video-storyboard](../01-content/017-video-storyboard.md)

## Recommended next steps

- video-storyboard (017)
- presentation-story → storytelling (024)

---

## AI specification

```text
purpose: "Build the narrative structure for a presentation or talk."
required_inputs:
  - topic
  - audience profile
  - talk length
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only need the visual side — use video-storyboard (017)."
  - "You're leading a meeting, not a presentation — use meeting-agenda (078)."
workflow:
  - "1. Confirm audience and length."
  - "2. Draft the narrative arc."
  - "3. Lay out section beats."
  - "4. Write the opening hook and the closing call to action."
output_contract:
  - "narrative arc"
  - "section beats"
  - "opening and closing"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: arc
    description: narrative arc summary
  - key: section_beats
    description: ordered beats per section
```