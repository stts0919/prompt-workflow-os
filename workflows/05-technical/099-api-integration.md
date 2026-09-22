---
id: "099"
slug: "api-integration"
title: "Design an API Integration"
category: "technical"
aliases:
  - api integration
  - integrate with api
  - third-party api
triggers:
  - integrate an api
  - third-party api
  - build an integration
input_types:
  - provider
  - use case
output_types:
  - integration plan
requires:
  - provider and use case
  - constraints (auth, rate limits, latency)
produces:
  - integration plan
  - auth and rate-limit handling
  - error handling
  - tests
related:
  - system-design
  - schema-design
  - code-review
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



# 099 — Design an API Integration

## What is this?

Produce an integration plan: auth, rate-limit handling, retries, idempotency, error handling, logging, tests, and observability.

## Why use it?

Most integrations break at the corners: rate limits, retries, partial failures. A plan closes the corners early.

## When should I use it?

- You're integrating with a third-party API.
- You're rebuilding an existing integration that's flaky.

## When should I not use it?

- You're designing whole-system architecture — use system-design (100).

## What should I prepare?

- Provider.
- Use case.
- Constraints.

## How does the AI help me?

1. Confirm use case.
2. Map provider endpoints.
3. Define auth and rate-limit handling.
4. Define retries, idempotency, error handling.
5. Specify tests and observability.

## What will I get?

- Integration plan.
- Auth and rate-limit handling.
- Error handling.
- Tests.

## How to start

Open a conversation with any AI that can read this repository and say:

```
Read this repository's START.md and help me with this:

[describe what you want — your goal, topic, audience, and any constraints]
```


## Related workflows

- [system-design](../05-technical/100-system-design.md)
- [schema-design](../05-technical/098-schema-design.md)
- [code-review](../05-technical/095-code-review.md)

## Recommended next steps

- code-generation (093)
- code-review (095)

---

## AI specification

```text
purpose: "Plan an API integration with predictable error handling."
required_inputs:
  - provider and use case
  - constraints (auth, rate limits, latency)
optional_inputs:
  - data shape
  - environments
ask_if_missing:
  - "What is the desired outcome and who is it for?"
  - "Any constraints on tone, length, or required terminology?"
do_not_use_when:
  - "You're designing whole-system architecture — use system-design (100)."
workflow:
  - "1. Confirm use case."
  - "2. Map provider endpoints."
  - "3. Define auth and rate-limit handling."
  - "4. Define retries, idempotency, error handling."
  - "5. Specify tests and observability."
output_contract:
  - "integration plan"
  - "auth and rate-limit handling"
  - "error handling"
  - "tests"
quality_rules:
  - "Mirror the user's language unless another output language is requested."
  - "Do not invent facts, sources, numbers, or user context."
  - "Use current-source verification only when recency is material."
  - "Label assumptions and verification gaps explicitly."
handoff:
handoff:
  - key: integration_plan
    description: structured plan
  - key: error_strategy
    description: retries and idempotency
```