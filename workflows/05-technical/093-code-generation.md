---
id: "093"
slug: "code-generation"
title: "Generate Code"
category: "technical"
aliases:
  - write code
  - implement
  - code generation
triggers:
  - write this code
  - implement this
  - generate code
input_types:
  - task spec
output_types:
  - code
requires:
  - task spec (objective, inputs, outputs)
  - language and constraints
  - acceptance criteria
produces:
  - code
  - tests
  - usage notes
related:
  - code-review
  - debugging
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
handoff:
  - key: context
    description: "summary of upstream context"
---



# 093 — Generate Code

## What is this?

Read the spec and produce code with tests, edge-case handling, and usage notes.

## Why use it?

Generated code without a spec is brittle. A spec makes the generation testable and the code auditable.

## When should I use it?

- You have a small task spec and want code.
- You're scripting a one-off.

## When should I not use it?

- You're designing architecture — use system-design (100).
- You don't yet have a spec — use agent-task-spec (091) first.

## What should I prepare?

- Task spec.
- Language and constraints.
- Acceptance criteria.

## How does the AI help me?

1. Confirm spec.
2. Generate code.
3. Add tests.
4. Note edge cases.
5. Provide usage notes.

## What will I get?

- Code.
- Tests.
- Usage notes.
- Edge cases.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [code-review](../05-technical/095-code-review.md)
- [debugging](../05-technical/094-debugging.md)
- [system-design](../05-technical/100-system-design.md)

## Recommended next steps

- code-review (095)
- debugging (094)

---

## AI specification

```text
purpose: "Generate code that satisfies a task spec."
required_inputs:
  - task spec (objective, inputs, outputs)
  - language and constraints
  - acceptance criteria
optional_inputs:
  - style guide
  - test framework
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're designing architecture — use system-design (100)."
  - "You don't yet have a spec — use agent-task-spec (091) first."
workflow:
  - "1. Confirm spec."
  - "2. Generate code."
  - "3. Add tests."
  - "4. Note edge cases."
  - "5. Provide usage notes."
output_contract:
  - "code"
  - "tests"
  - "usage notes"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: code
    description: generated code
  - key: tests
    description: test coverage
```