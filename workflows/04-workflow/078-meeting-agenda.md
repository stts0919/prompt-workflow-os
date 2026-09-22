---
id: "078"
slug: "meeting-agenda"
title: "Build a Meeting Agenda"
category: "workflow"
aliases:
  - agenda
  - meeting agenda
  - meeting prep
triggers:
  - meeting agenda
  - agenda
  - meeting prep
input_types:
  - meeting goal
  - attendees
output_types:
  - meeting agenda
requires:
  - meeting goal
  - attendees or roles
  - time budget
produces:
  - agenda
  - pre-read list
  - decision points
related:
  - meeting-notes
  - podcast-interview
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



# 078 — Build a Meeting Agenda

## What is this?

Produce an agenda with time boxes per item, decision points, who is responsible for each, and a pre-read list.

## Why use it?

Meetings without agendas turn into status reports. Tight agendas force decisions and respect time.

## When should I use it?

- You're scheduling a meeting.
- Past meetings have run over or ended without decisions.

## When should I not use it?

- You're hosting a podcast — use podcast-interview (018).

## What should I prepare?

- Meeting goal.
- Attendees.
- Time budget.

## How does the AI help me?

1. Confirm inputs.
2. Build agenda.
3. Add time boxes.
4. Mark decisions.
5. Add pre-read list.

## What will I get?

- Agenda.
- Pre-read list.
- Decisions list.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [meeting-notes](../04-workflow/079-meeting-notes.md)
- [podcast-interview](../01-content/018-podcast-interview.md)

## Recommended next steps

- meeting-notes (079)

---

## AI specification

```text
purpose: "Build a tight meeting agenda that ends on time with clear decisions."
required_inputs:
  - meeting goal
  - attendees or roles
  - time budget
optional_inputs:
  - pre-read
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're hosting a podcast — use podcast-interview (018)."
workflow:
  - "1. Confirm inputs."
  - "2. Build agenda."
  - "3. Add time boxes."
  - "4. Mark decisions."
  - "5. Add pre-read list."
output_contract:
  - "agenda"
  - "pre-read list"
  - "decision points"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: agenda
    description: agenda with time boxes
  - key: pre_read
    description: required pre-reading
```