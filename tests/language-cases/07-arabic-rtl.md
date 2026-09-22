# Language Case — Arabic Conversation (RTL)

## Setup

- Mode: `guide`.
- Detected language: Arabic.

## Input

> اقرأ START.md وساعدني في كتابة بريد إلكتروني تسلسلي (email-sequence) لإطلاق منتجي.

## Expected behavior

- Reply in Arabic.
- Run `email-sequence` (046).
- Preserve the workflow ID `046` and slug `email-sequence` in English.
- Section headings can be in Arabic.

## Expected questions

1. "ما هو المنتج ومن هي الفئة المستهدفة؟"
2. "كم عدد الرسائل التي تريدها، وما هي النبرة؟"

## Failure conditions

- Replying in English.
- Translating workflow names.
- Forgetting to ask about audience.
