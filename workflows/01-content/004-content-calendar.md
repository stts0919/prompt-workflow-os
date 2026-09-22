---
id: "004"
slug: "content-calendar"
title: "Plan a Content Calendar"
category: "content"
aliases:
  - editorial calendar
  - publishing calendar
  - schedule posts
triggers:
  - plan a calendar
  - editorial calendar
  - when to publish
  - publishing schedule
input_types:
  - channels
  - posting frequency
  - backlog or theme
output_types:
  - calendar table
  - themes per week
  - production milestones
requires:
  - channels (blog, LinkedIn, X, newsletter, etc.)
  - cadence
  - content backlog or pillars
produces:
  - rolling N-week calendar
  - theme-per-week summary
  - production milestones
related:
  - topic-prioritization
  - content-pillar-design
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



# 004 — Plan a Content Calendar

## What is this?

Lay out a calendar (typically 4–8 weeks) with date, channel, format, theme, owner, and status. It mixes pillar content, repurposed posts, and reactive opportunities.

## Why use it?

A calendar turns a backlog into shipping velocity. Without dates, nothing gets published consistently.

## When should I use it?

- You have ideas but no shipping rhythm.
- Your publishing output dropped off.
- You're coordinating multiple channels or contributors.

## When should I not use it?

- You have no backlog yet — start with content-idea-generation (001) or topic-prioritization (005).
- You need a launch plan, not a steady calendar — use campaign-plan (045).

## What should I prepare?

- Channels to publish on.
- Cadence (e.g., 3 posts a week).
- Backlog or pillars.

## How does the AI help me?

1. Confirm channels, cadence, and timeframe.
2. Distribute backlog across dates and channels.
3. Reserve 20% of slots for reactive or trending topics.
4. Output a calendar table with owners and themes.

## What will I get?

- Calendar table.
- Themes per week.
- Production milestones (draft dates, review dates).
- Suggested next workflow: content-quality-review (029).

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [topic-prioritization](../01-content/005-topic-prioritization.md)
- [content-pillar-design](../01-content/002-content-pillar-design.md)
- [content-repurposing](../01-content/028-content-repurposing.md)

## Recommended next steps

- topic-prioritization (005)
- content-quality-review (029)

---

## AI specification

```text
purpose: "Build a rolling content calendar with concrete dates, channels, and themes."
required_inputs:
  - channels (blog, LinkedIn, X, newsletter, etc.)
  - cadence
  - content backlog or pillars
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You have no backlog yet — start with content-idea-generation (001) or topic-prioritization (005)."
  - "You need a launch plan, not a steady calendar — use campaign-plan (045)."
workflow:
  - "1. Confirm channels, cadence, and timeframe."
  - "2. Distribute backlog across dates and channels."
  - "3. Reserve 20% of slots for reactive or trending topics."
  - "4. Output a calendar table with owners and themes."
output_contract:
  - "rolling N-week calendar"
  - "theme-per-week summary"
  - "production milestones"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: calendar
    description: dated calendar slots per channel
  - key: themes
    description: theme summary per week
```