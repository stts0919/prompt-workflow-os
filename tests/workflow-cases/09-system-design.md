# Workflow Case — System Design

## Setup

- Mode: `guide`.
- Workflow: `system-design` (100).

## Input

- Functional requirements: a customer support email classification pipeline.
- Non-functional: 99th-percentile latency under 2s for 1k requests/min, multi-region, monthly cost ceiling.
- Constraints: existing Postgres + OpenAI API, small team (3 engineers).

## Expected output

A system design covering:

- Architecture (queue, classifier service, Postgres, cache).
- Components and responsibilities.
- Data flow.
- Trade-offs (cost vs latency, accuracy vs speed).
- Open questions.

## Verification

- Trade-offs are explicit, not glossed.
- Open questions are listed (e.g., prompt strategy, evaluation cadence).
- Cost estimates include a sensitivity note.
- Reliability plan addresses retries and queue depth.

## Failure conditions

- Producing only a diagram without trade-offs.
- Inventing infrastructure components the user does not have.
- Skipping non-functional requirements.
