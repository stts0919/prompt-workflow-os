---
id: "090"
slug: "prompt-improvement"
title: "Improve an Existing Prompt"
category: "technical"
aliases:
  - improve prompt
  - tune prompt
  - prompt audit
triggers:
  - improve my prompt
  - tune this prompt
  - audit this prompt
input_types:
  - prompt
  - issues
output_types:
  - improved prompt
  - change summary
requires:
  - prompt text
  - failing or weak examples
produces:
  - improved prompt
  - rationale
  - test cases
related:
  - prompt-designer
  - code-review
  - debugging
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



# 090 — Improve an Existing Prompt

## What is this?

Identify failure modes, propose a rewrite, and explain each change. Provide new test cases targeting the failures.

## Why use it?

Most prompt regressions come from unclear instructions or missing constraints. A targeted rewrite fixes them.

## When should I use it?

- A prompt works but feels inconsistent.
- The model often misses a constraint.

## When should I not use it?

- You're starting a new prompt — use prompt-designer (089).

## What should I prepare?

- Prompt text.
- Failing examples.

## How does the AI help me?

1. Diagnose failure modes.
2. Propose rewrite.
3. Explain changes.
4. Add test cases.

## What will I get?

- Improved prompt.
- Change rationale.
- New test cases.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [prompt-designer](../05-technical/089-prompt-designer.md)
- [code-review](../05-technical/095-code-review.md)
- [debugging](../05-technical/094-debugging.md)

## Recommended next steps

- prompt-designer (089)
- code-review (095)

---

## AI specification

```text
purpose: "Diagnose and improve an existing prompt."
required_inputs:
  - prompt text
  - failing or weak examples
optional_inputs:
  - evaluation criteria
  - constraints
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're starting a new prompt — use prompt-designer (089)."
workflow:
  - "1. Diagnose failure modes."
  - "2. Propose rewrite."
  - "3. Explain changes."
  - "4. Add test cases."
output_contract:
  - "improved prompt"
  - "rationale"
  - "test cases"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: improved_prompt
    description: new prompt text
  - key: change_log
    description: rationale per change
```