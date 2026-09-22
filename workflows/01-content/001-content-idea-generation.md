---
id: "001"
slug: "content-idea-generation"
title: "Generate Content Ideas"
category: "content"
aliases:
  - blog ideas
  - content ideas
  - video ideas
  - post ideas
  - topic ideas
triggers:
  - need topics
  - ran out of ideas
  - what should I post
  - give me ideas
  - brainstorm content
input_types:
  - topic or domain
  - audience description
  - business goal
output_types:
  - idea list
  - angles
  - hooks
requires:
  - topic or domain
  - target audience
  - high-level goal (educate, sell, build authority)
produces:
  - prioritized idea list
  - angles per idea
  - opening hooks for top ideas
related:
  - content-pillar-design
  - topic-prioritization
  - audience-message-map
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



# 001 — Generate Content Ideas

## What is this?

Produce a structured set of content ideas for a topic, audience, and goal. Each idea is paired with an angle, an opening hook, and a fitness note so you can pick what to publish next.

## Why use it?

Most content stalls because the backlog is shallow or repetitive. A short, ranked backlog with explicit angles prevents rehashed posts and keeps the editorial calendar full.

## When should I use it?

- You're staring at a blank content calendar.
- Your niche feels saturated and you want fresh angles.
- You have a topic but no idea which slice of the audience to address first.

## When should I not use it?

- You already have a backlog that needs filtering — use topic-prioritization (005) instead.
- You're producing one specific artifact — go straight to article-outline (006), social-post (012), or short-video-script (015).
- You want strategic guidance on what to be about — use content-pillar-design (002).

## What should I prepare?

- Topic or domain — be specific ("B2B SaaS pricing"), not vague ("marketing").
- Target audience — jobs-to-be-done or one-line persona.
- Goal — educate, drive sign-ups, build authority, nurture, sell.

## How does the AI help me?

1. Restate the goal in one sentence and confirm the audience and channel.
2. Generate 15–25 distinct ideas across angles (contrarian, beginner, advanced, story, data, comparison).
3. Score each idea on audience fit, novelty, and production cost.
4. Provide an opening hook for the top 5 ideas.
5. Suggest the next workflow: article-outline (006) for the chosen idea.

## What will I get?

- A prioritized idea table with score and angle.
- A short hook for each of the top 5 ideas.
- Assumptions about audience and goal.
- One next-workflow suggestion.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [content-pillar-design](../01-content/002-content-pillar-design.md)
- [topic-prioritization](../01-content/005-topic-prioritization.md)
- [audience-message-map](../01-content/003-audience-message-map.md)

## Recommended next steps

- article-outline (006)
- topic-prioritization (005)

---

## AI specification

```text
purpose: "Turn a vague topic into a prioritized backlog of distinct content ideas."
required_inputs:
  - topic or domain
  - target audience
  - high-level goal (educate, sell, build authority)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You already have a backlog that needs filtering — use topic-prioritization (005) instead."
  - "You're producing one specific artifact — go straight to article-outline (006), social-post (012), or short-video-script (015)."
  - "You want strategic guidance on what to be about — use content-pillar-design (002)."
workflow:
  - "1. Restate the goal in one sentence and confirm the audience and channel."
  - "2. Generate 15–25 distinct ideas across angles (contrarian, beginner, advanced, story, data, comparison)."
  - "3. Score each idea on audience fit, novelty, and production cost."
  - "4. Provide an opening hook for the top 5 ideas."
  - "5. Suggest the next workflow: article-outline (006) for the chosen idea."
output_contract:
  - "prioritized idea list"
  - "angles per idea"
  - "opening hooks for top ideas"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: selected_idea
    description: the idea chosen by the user for further development
  - key: audience
    description: confirmed audience description
  - key: goal
    description: confirmed content goal
```