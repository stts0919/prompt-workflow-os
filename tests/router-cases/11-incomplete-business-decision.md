# Router Case — Incomplete Inputs for a Business Decision

## Setup

- Mode: `guide`.
- Language: English.

## Input

> Should we enter the European market?

## Expected routing

`business-decision` (052) → `research-before-a-decision` playbook. The decision statement is provided; criteria, options, evidence are not.

## Expected questions

1. "What decision criteria matter most (size, fit, risk, time-to-revenue)?"
2. "What evidence do we already have or need to gather?"

## Failure conditions

- Producing a recommendation without criteria.
- Inventing market size numbers.
- Skipping the playbook entirely.
