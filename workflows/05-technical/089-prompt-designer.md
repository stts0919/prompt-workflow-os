---
id: "089"
slug: "prompt-designer"
title: "Design a Prompt from Scratch"
category: "technical"
aliases:
  - prompt design
  - design a prompt
  - system prompt
triggers:
  - design a prompt
  - system prompt
  - write a prompt for
  - new prompt
input_types:
  - task
  - model constraints
output_types:
  - prompt
requires:
  - task description
  - model or system constraints
  - examples
produces:
  - prompt
  - rationale
  - test cases
related:
  - prompt-improvement
  - agent-task-spec
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



# 089 — Design a Prompt from Scratch

## What is this?

Build a prompt with role, inputs, instructions, output format, constraints, and 3 example test cases.

## Why use it?

First-draft prompts are vague and brittle. Structured prompts document the intent and stay portable.

## When should I use it?

- You're building a prompt for a new workflow.
- You're handing a prompt to teammates or contractors.

## When should I not use it?

- You already have a prompt and want to improve it — use prompt-improvement (090).

## What should I prepare?

- Task description.
- Model or system constraints.
- Examples.

## How does the AI help me?

1. Confirm task and constraints.
2. Draft a structured prompt.
3. Add 3 test cases.
4. Document rationale.

## What will I get?

- Prompt.
- Rationale.
- 3 test cases.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [prompt-improvement](../05-technical/090-prompt-improvement.md)
- [agent-task-spec](../05-technical/091-agent-task-spec.md)
- [debugging](../05-technical/094-debugging.md)

## Recommended next steps

- prompt-improvement (090)

---

## AI specification

```text
purpose: "Design a prompt from scratch with explicit structure and rationale."
required_inputs:
  - task description
  - model or system constraints
  - examples
optional_inputs:
  - evaluation criteria
  - tone
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You already have a prompt and want to improve it — use prompt-improvement (090)."
workflow:
  - "1. Confirm task and constraints."
  - "2. Draft a structured prompt."
  - "3. Add 3 test cases."
  - "4. Document rationale."
output_contract:
  - "prompt"
  - "rationale"
  - "test cases"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: prompt
    description: structured prompt
  - key: test_cases
    description: example inputs and expected outputs
```