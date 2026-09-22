---
id: "053"
slug: "risk-stress-test"
title: "Stress-Test a Plan Against Risks"
category: "business"
aliases:
  - risk test
  - pre-mortem
  - stress test a plan
triggers:
  - risk check
  - pre-mortem
  - stress test this plan
  - what could go wrong
input_types:
  - plan
  - risks
output_types:
  - risk register
  - mitigations
requires:
  - plan summary
  - known risks
produces:
  - risk register
  - mitigations
  - owner suggestions
related:
  - business-decision
  - project-risk
  - scenario-planning
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



# 053 — Stress-Test a Plan Against Risks

## What is this?

Generate a risk register with risk statements, likelihood, impact, score, mitigations, and owners. Include at least one pre-mortem scenario.

## Why use it?

Plans fail in ways you didn't prepare for. Stress-testing converts vague worry into mitigable risks.

## When should I use it?

- Before committing to a major plan.
- When a stakeholder asks "what could go wrong?"

## When should I not use it?

- You're planning long-range scenarios — use scenario-planning (068).

## What should I prepare?

- Plan summary.
- Known risks.

## How does the AI help me?

1. Confirm inputs.
2. Generate a risk register.
3. Run a pre-mortem.
4. Recommend mitigations.

## What will I get?

- Risk register.
- Pre-mortem notes.
- Mitigations.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [business-decision](../02-business/052-business-decision.md)
- [project-risk](../04-workflow/077-project-risk.md)
- [scenario-planning](../03-research/068-scenario-planning.md)

## Recommended next steps

- business-decision (052)
- project-risk (077)

---

## AI specification

```text
purpose: "Identify, score, and mitigate risks in a plan."
required_inputs:
  - plan summary
  - known risks
optional_inputs:
  - stakeholders
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're planning long-range scenarios — use scenario-planning (068)."
workflow:
  - "1. Confirm inputs."
  - "2. Generate a risk register."
  - "3. Run a pre-mortem."
  - "4. Recommend mitigations."
output_contract:
  - "risk register"
  - "mitigations"
  - "owner suggestions"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: risk_register
    description: ranked risks with mitigations
  - key: pre_mortem
    description: pre-mortem narrative
```