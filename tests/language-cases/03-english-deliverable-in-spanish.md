# Language Case — English Conversation, Spanish Deliverable

## Setup

- Mode: `guide`.
- Detected language: English.
- Deliverable language: Spanish (user-stated).

## Input

> Read START.md and help me write a newsletter issue. Please reply in English but produce the actual newsletter in Spanish.

## Expected behavior

- Reply in English.
- Confirm audience and theme in English.
- Produce the newsletter in Spanish.
- Preserve workflow IDs (`011 newsletter`) and section headings in English inside the deliverable's internal metadata, but the newsletter content itself is Spanish.

## Expected questions (in English)

1. "Theme or topic for the issue?"
2. "Audience and voice reference?"

## Failure conditions

- Replying in Spanish (the user said reply in English).
- Writing the newsletter in English.
- Translating section headings (`lede`, `body`) into Spanish.
