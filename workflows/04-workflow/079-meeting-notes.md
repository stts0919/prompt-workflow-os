---
id: "079"
slug: "meeting-notes"
title: "Take Meeting Notes"
category: "workflow"
aliases:
  - meeting notes
  - note-taking
  - minutes
triggers:
  - take notes
  - meeting minutes
  - capture this meeting
input_types:
  - meeting context
  - agenda
output_types:
  - meeting notes
requires:
  - agenda or goal
  - transcript or rough notes
produces:
  - meeting notes
  - decisions
  - action items
related:
  - meeting-agenda
  - meeting-summary
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



# 079 — Take Meeting Notes

## What is this?

Produce notes: agenda items, decisions, action items (who/what/when), and open questions.

## Why use it?

Most meeting notes are unusable later. Structured notes give the absent a place to start and the present a record.

## When should I use it?

- You're taking notes live.
- You want to summarize notes after a meeting.

## When should I not use it?

- You only have a transcript — use meeting-summary (059).

## What should I prepare?

- Agenda.
- Live or rough notes.

## How does the AI help me?

1. Confirm agenda.
2. Capture per-item summary.
3. Pull out decisions and action items.
4. Note open questions.

## What will I get?

- Meeting notes.
- Decisions.
- Action items.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [meeting-agenda](../04-workflow/078-meeting-agenda.md)
- [meeting-summary](../03-research/059-meeting-summary.md)
- [task-breakdown](../04-workflow/072-task-breakdown.md)

## Recommended next steps

- task-breakdown (072)
- project-plan (076)

---

## AI specification

```text
purpose: "Turn a meeting into actionable notes with decisions and owners."
required_inputs:
  - agenda or goal
  - transcript or rough notes
optional_inputs:
  - attendees
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You only have a transcript — use meeting-summary (059)."
workflow:
  - "1. Confirm agenda."
  - "2. Capture per-item summary."
  - "3. Pull out decisions and action items."
  - "4. Note open questions."
output_contract:
  - "meeting notes"
  - "decisions"
  - "action items"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: notes
    description: meeting notes
  - key: action_items
    description: who / what / when
```