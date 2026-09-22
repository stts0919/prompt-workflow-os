---
id: "009"
slug: "content-editing"
title: "Edit for Clarity"
category: "content"
aliases:
  - copy edit
  - editorial pass
  - clarity edit
  - proofread
triggers:
  - edit this
  - clean up
  - proofread
  - tighten prose
  - clarity pass
input_types:
  - draft
  - editing goal
output_types:
  - edited draft
  - edit notes
requires:
  - draft
  - editing goal (clarity, brevity, voice, accuracy)
produces:
  - edited draft
  - inline edit notes
  - open questions
related:
  - article-draft
  - article-rewrite
  - content-quality-review
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



# 009 — Edit for Clarity

## What is this?

Apply a multi-pass edit: structure, sentence-level clarity, concision, voice, and accuracy. Return an edited draft with inline edit notes and a short list of open questions for the author.

## Why use it?

First drafts are usually bloated, redundant, or meandering. A focused editorial pass turns a draft into publishable prose.

## When should I use it?

- A draft is in good shape but reads rough.
- You want an outside perspective without a full rewrite.

## When should I not use it?

- The structure is broken — start with article-outline (006).
- You need to change angle or audience — use article-rewrite (008).

## What should I prepare?

- Draft.
- Editing goal.
- Voice reference (optional).

## How does the AI help me?

1. Diagnose structural issues first.
2. Edit sentence by sentence for clarity and concision.
3. Flag factual claims requiring verification.
4. Output the edited draft plus a short edit-notes block.

## What will I get?

- Edited draft.
- Edit notes block (issues caught + how they were fixed).
- Open questions for the author.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [article-draft](../01-content/007-article-draft.md)
- [article-rewrite](../01-content/008-article-rewrite.md)
- [content-quality-review](../01-content/029-content-quality-review.md)

## Recommended next steps

- content-quality-review (029)

---

## AI specification

```text
purpose: "Run a focused editorial pass that improves clarity, structure, concision, and accuracy."
required_inputs:
  - draft
  - editing goal (clarity, brevity, voice, accuracy)
optional_inputs:
  - example or sample
  - tone guide
  - verification needs
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "The structure is broken — start with article-outline (006)."
  - "You need to change angle or audience — use article-rewrite (008)."
workflow:
  - "1. Diagnose structural issues first."
  - "2. Edit sentence by sentence for clarity and concision."
  - "3. Flag factual claims requiring verification."
  - "4. Output the edited draft plus a short edit-notes block."
output_contract:
  - "edited draft"
  - "inline edit notes"
  - "open questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: edited_draft
    description: draft after editing
  - key: edit_notes
    description: list of edits made and open questions
```