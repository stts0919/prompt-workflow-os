# Language Case — Language Switch Mid-Conversation

## Setup

- Mode: `guide`.

## Input (turn 1)

> Por favor, ayúdame con un competitor analysis.

## Input (turn 2, language switch to English)

> Switch to English please. We need it by tomorrow.

## Expected behavior

- Turn 1: Reply in Spanish.
- Turn 2: Detect the new dominant language is English. Reply in English from this turn onward.
- Continue running the same workflow (`competitor-analysis`, 034) with the new context.

## Failure conditions

- Continuing in Spanish after the switch.
- Restarting the workflow from scratch.
- Apologizing excessively instead of just switching.
