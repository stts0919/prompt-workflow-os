---
id: "091"
slug: "agent-task-spec"
title: "Spec an AI Agent Task"
category: "technical"
aliases:
  - agent spec
  - task spec
  - agent task
triggers:
  - agent task
  - spec an agent
  - ai agent brief
input_types:
  - task
  - agent capabilities
output_types:
  - agent task spec
requires:
  - task
  - agent capabilities
  - acceptance criteria
produces:
  - agent task spec
  - non-goals
  - evaluation plan
related:
  - prompt-designer
  - code-generation
  - system-design
playbooks:
  - build-an-ai-agent-task
mode_support:
  - guide
  - quick
  - recommend
language_support:
  input: auto-detect
  output: mirror-user-language
localization:
  supported_locales:
    - en
    - zh-TW
  default_style_profile: zh-cn-friendly-professional
  locale_style_profile_overrides:
    zh-TW:
  editing_intensity: strict_precision
handoff:
  - key: context
    description: "summary of upstream context"
---



# 091 — Spec an AI Agent Task

## What is this?

Write an agent task spec: objective, inputs, outputs, acceptance criteria, non-goals, tool access, and an evaluation plan.

## Why use it?

Vague agent briefs produce inconsistent behavior. A precise spec is the difference between useful automation and a demo.

## When should I use it?

- You're setting up an agent task.
- You're briefing a build for an agent.

## When should I not use it?

- You're generating code — use code-generation (093) or system-design (100).

## What should I prepare?

- Task description.
- Agent capabilities.
- Acceptance criteria.

## How does the AI help me?

1. Confirm inputs.
2. Define objective and inputs.
3. Specify outputs and acceptance criteria.
4. State non-goals.
5. Define tool access and evaluation plan.

## What will I get?

- Agent task spec.
- Non-goals.
- Evaluation plan.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [prompt-designer](../05-technical/089-prompt-designer.md)
- [code-generation](../05-technical/093-code-generation.md)
- [system-design](../05-technical/100-system-design.md)

## Recommended next steps

- code-generation (093)
- system-design (100)

---

## AI specification

```text
purpose: "Produce a precise AI agent task specification."
required_inputs:
  - task
  - agent capabilities
  - acceptance criteria
optional_inputs:
  - tools
  - budget
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're generating code — use code-generation (093) or system-design (100)."
workflow:
  - "1. Confirm inputs."
  - "2. Define objective and inputs."
  - "3. Specify outputs and acceptance criteria."
  - "4. State non-goals."
  - "5. Define tool access and evaluation plan."
output_contract:
  - "agent task spec"
  - "non-goals"
  - "evaluation plan"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: agent_spec
    description: structured agent brief
  - key: acceptance_criteria
    description: success criteria
```