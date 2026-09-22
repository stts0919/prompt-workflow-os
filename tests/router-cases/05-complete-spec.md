# Router Case — Complete Spec for an AI Agent

## Setup

- Mode: `quick`.
- Language: English.

## Input

> Build me an AI agent that takes a product description and returns:
> 1) three different positioning statements,
> 2) a competitor matrix against [named competitors],
> 3) a draft value proposition.
> Acceptance: each output is valid JSON. No external API calls. Single Python file.

## Expected routing

`agent-task-spec` (091) → confirm spec → `code-generation` (093) → `code-review` (095).

Inputs are complete. Execute in `quick` mode with no clarifying questions, but state explicit assumptions about the JSON schema and the competitor list size.

## Expected output

- A precise agent task spec.
- A Python file with tests for the schema.
- A short code review with severity-tagged issues.

## Failure conditions

- Asking clarifying questions when the spec is already complete.
- Producing code without tests.
- Skipping the review step.
