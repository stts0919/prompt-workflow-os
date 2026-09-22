---
id: "017"
slug: "video-storyboard"
title: "Create a Video Storyboard"
category: "content"
aliases:
  - storyboard
  - shot list
  - scene plan
triggers:
  - storyboard
  - shot list
  - scene plan
  - visual plan for video
input_types:
  - script or outline
  - platform
output_types:
  - scene-by-scene storyboard
  - shot notes
requires:
  - video script or outline
  - platform and length
produces:
  - scene-by-scene storyboard
  - shot notes
  - transition notes
related:
  - short-video-script
  - presentation-story
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



# 017 — Create a Video Storyboard

## What is this?

Build a storyboard that maps each scene to a shot, an on-screen text overlay, a voice-over line, and a transition.

## Why use it?

A storyboard reveals pacing problems before you film. It also makes editing predictable.

## When should I use it?

- You have a script and want to film efficiently.
- You want to brief an editor.

## When should I not use it?

- You're scripting for the first time — start with short-video-script (015).
- You're producing audio-only — use podcast-interview (018).

## What should I prepare?

- Video script or outline.
- Platform and length.
- Visual style or brand references.

## How does the AI help me?

1. Read the script and identify scenes.
2. Map each scene to a shot, on-screen text, and transition.
3. Flag pacing risks (too slow / too fast).
4. Suggest locations, props, or B-roll.

## What will I get?

- Scene-by-scene storyboard.
- Shot, text, transition notes per scene.
- Pacing flags.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [short-video-script](../01-content/015-short-video-script.md)
- [presentation-story](../01-content/019-presentation-story.md)

## Recommended next steps

- content-quality-review (029)

---

## AI specification

```text
purpose: "Translate a video script into scenes, shots, text overlays, and transitions."
required_inputs:
  - video script or outline
  - platform and length
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're scripting for the first time — start with short-video-script (015)."
  - "You're producing audio-only — use podcast-interview (018)."
workflow:
  - "1. Read the script and identify scenes."
  - "2. Map each scene to a shot, on-screen text, and transition."
  - "3. Flag pacing risks (too slow / too fast)."
  - "4. Suggest locations, props, or B-roll."
output_contract:
  - "scene-by-scene storyboard"
  - "shot notes"
  - "transition notes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: storyboard
    description: ordered scenes with shots and transitions
```