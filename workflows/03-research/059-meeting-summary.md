---
id: "059"
slug: "meeting-summary"
title: "Summarize a Meeting Transcript"
category: "research"
aliases:
  - meeting notes
  - transcript summary
  - meeting recap
triggers:
  - summarize this meeting
  - meeting transcript
  - what was decided
input_types:
  - transcript or notes
output_types:
  - meeting summary
  - action items
requires:
  - transcript or notes
  - audience for the summary
produces:
  - meeting summary
  - decisions
  - action items
  - open questions
related:
  - meeting-notes
  - decision-memo
  - task-breakdown
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



# 059 — Summarize a Meeting Transcript

## What is this?

Read the transcript and produce a structured summary: decisions, action items, open questions, and brief context for absent teammates.

## Why use it?

Without a structured summary, meetings forget themselves. Action items lose owners and deadlines drift.

## When should I use it?

- You have a meeting transcript or detailed notes.
- You missed a meeting and need a recap.

## When should I not use it?

- You're turning notes into an internal memo — use meeting-notes (079).

## What should I prepare?

- Transcript or notes.
- Audience (full team, execs).

## How does the AI help me?

1. Read the transcript.
2. Extract decisions, actions, open questions.
3. Surface disagreements.
4. Write a short context recap.

## What will I get?

- Decisions list.
- Action items (who/what/when).
- Open questions.
- Context recap.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [meeting-notes](../04-workflow/079-meeting-notes.md)
- [decision-memo](../03-research/069-decision-memo.md)
- [task-breakdown](../04-workflow/072-task-breakdown.md)

## Recommended next steps

- task-breakdown (072)
- decision-memo (069)

---

## AI specification

```text
purpose: "Turn a meeting transcript into a usable summary."
required_inputs:
  - transcript or notes
  - audience for the summary
optional_inputs:
  - agenda
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're turning notes into an internal memo — use meeting-notes (079)."
workflow:
  - "1. Read the transcript."
  - "2. Extract decisions, actions, open questions."
  - "3. Surface disagreements."
  - "4. Write a short context recap."
output_contract:
  - "meeting summary"
  - "decisions"
  - "action items"
  - "open questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: decisions
    description: decision list
  - key: action_items
    description: who / what / when
```