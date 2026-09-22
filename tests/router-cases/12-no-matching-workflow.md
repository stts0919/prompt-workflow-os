# Router Case — No Matching Workflow

## Setup

- Mode: `guide`.
- Language: English.

## Input

> Plan my wedding.

## Expected routing

No exact match. Use `fallback-rules` (router/FALLBACK_RULES.md). Pick the closest workflows: `goal-setting` (075), `task-breakdown` (072), `project-plan` (076), `weekly-plan` (074). State explicitly which parts fall outside the repository's domain and offer a fallback plan.

## Expected output

A small playbook-style summary using the closest workflows, plus a note that wedding planning exceeds the library's core purpose.

## Failure conditions

- Refusing the request entirely.
- Pretending a workflow matches.
- Forcing the request into `create-high-quality-content` because it's about "events".
