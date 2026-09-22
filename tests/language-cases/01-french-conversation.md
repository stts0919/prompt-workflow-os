# Language Case — French Conversation

## Setup

- Mode: `guide`.
- Detected language: French.

## Input

> Lis le START.md de ce dépôt et aide-moi à valider mon idée d'entreprise en ligne. Je ne sais pas si les gens achèteront.

## Expected behavior

- Reply in French.
- Select `customer-persona` (031) or `product-idea-validation` (038).
- Preserve `START.md`, `customer-persona`, all workflow IDs in English.
- Run the same flow as `tests/router-cases/01-vague-product-idea.md`.

## Expected questions (in French)

1. "À qui destines-tu cette offre, et quel problème résout-elle ?"
2. "Quelle preuve as-tu que ce problème existe aujourd'hui ?"

## Failure conditions

- Replying in English when the user wrote French.
- Translating workflow IDs to French.
- Inventing the customer.
