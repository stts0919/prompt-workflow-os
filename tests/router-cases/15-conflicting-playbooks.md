# Router Case — Conflicting Playbook Signals

## Setup

- Mode: `guide`.
- Language: English.

## Input

> I have an idea I want to validate. I also want to write a launch article for it.

## Expected routing

Two plays conflict slightly. Prefer the smallest sufficient chain: `validate-a-business-idea` playbook for validation, then start `create-high-quality-content` once the offer is validated. Ask 1–2 alignment questions rather than running both in parallel.

## Expected questions

1. "Do you want to validate before drafting the article, or work in parallel?"
2. "Audience and channel for the article?"

## Failure conditions

- Running both playbooks simultaneously.
- Skipping the validation entirely because the user also wants content.
- Producing both an article and a validation plan without asking which comes first.
