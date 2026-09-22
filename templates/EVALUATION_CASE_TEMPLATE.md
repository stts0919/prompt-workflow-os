# Evaluation Case Template

Use this template for any test case under `tests/`.

---

## Test ID

`tests/<area>/<NN-slug>.md`

`<area>` is one of: `router-cases`, `language-cases`, `workflow-cases`.

## Title

Short, descriptive. e.g. "Router Case — Vague Product Idea".

## Setup (optional)

- Mode: `guide | quick | recommend`
- Language: declared by user (when relevant)
- Required inputs supplied or withheld

## Input

The literal user message (or first message in a small dialogue). Quote it.

## Expected routing

- State the workflows the router should select, in order.
- State the playbook if one applies.
- State expected clarifications (if any), and at what point they stop.

## Expected questions

- List the clarifying questions the AI should ask, or write `none` for quick mode.

## Expected output

What the deliverable should contain. A short bullet list is enough.

## Failure conditions

Be explicit. Each one must be observable.

- The AI invents facts / sources / numbers / quotes.
- The AI over-interviews (>2 questions per turn, >5 total).
- The AI under-interviews (skips a critical clarification).
- The AI picks the wrong workflow.
- The AI adds forbidden content.
- The AI produces inconsistent labels (mixes fact and inference).
- The AI delivers output in the wrong language.

## Notes

Anything the reviewer should know (mode, edge cases, why this case matters).
