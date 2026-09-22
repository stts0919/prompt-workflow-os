---
id: "092"
slug: "code-explanation"
title: "Explain Code"
category: "technical"
aliases:
  - explain code
  - what does this code do
  - code walkthrough
triggers:
  - explain this code
  - what does this code do
  - walk me through this
input_types:
  - code
output_types:
  - code explanation
requires:
  - code snippet or repo pointer
  - audience level
produces:
  - layered explanation
  - diagram suggestion
  - open questions
related:
  - code-review
  - code-generation
  - system-design
playbooks: []
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
  editing_intensity: light
handoff:
  - key: context
    description: "summary of upstream context"
---



# 092 — Explain Code

## What is this?

Produce a layered explanation: one-sentence summary, control flow, data flow, edge cases, and a deeper dive for the curious.

## Why use it?

Most code explanations are too dense for newcomers and too shallow for experienced engineers. Layered explanations serve both.

## When should I use it?

- You're learning a new codebase.
- You're documenting legacy code.

## When should I not use it?

- You want bugs caught — use code-review (095) or debugging (094).

## What should I prepare?

- Code.
- Audience level.

## How does the AI help me?

1. Confirm code and audience.
2. One-sentence summary.
3. Control flow and data flow.
4. Edge cases.
5. Deeper dive pointer.

## What will I get?

- Layered explanation.
- Diagram suggestion.
- Open questions.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [code-review](../05-technical/095-code-review.md)
- [code-generation](../05-technical/093-code-generation.md)
- [system-design](../05-technical/100-system-design.md)

## Recommended next steps

- code-review (095)
- system-design (100)

---

## AI specification

```text
purpose: "Explain code in a layered way for the chosen audience."
required_inputs:
  - code snippet or repo pointer
  - audience level
optional_inputs:
  - focus areas
  - background
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You want bugs caught — use code-review (095) or debugging (094)."
workflow:
  - "1. Confirm code and audience."
  - "2. One-sentence summary."
  - "3. Control flow and data flow."
  - "4. Edge cases."
  - "5. Deeper dive pointer."
output_contract:
  - "layered explanation"
  - "diagram suggestion"
  - "open questions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: explanation
    description: layered walkthrough
  - key: diagram
    description: visual aid suggestion
```