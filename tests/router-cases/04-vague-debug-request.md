# Router Case — Vague Debug Request

## Setup

- Mode: `guide`.
- Language: English.

## Input

> My code is broken. Help.

## Expected routing

`debugging` (094). Before executing, ask for the failing code, the error message, and the reproduction steps.

## Expected questions

1. "Can you share the failing code or a minimal reproduction?"
2. "What error message or wrong behavior are you seeing?"

## Failure conditions

- Asking more than two questions.
- Guessing at the language or framework.
- Producing plausible-sounding fixes without seeing the code (never invent fixes).
