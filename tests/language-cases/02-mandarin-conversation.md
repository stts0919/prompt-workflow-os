# Language Case — Mandarin Chinese Conversation

## Setup

- Mode: `guide`.
- Detected language: Mandarin Chinese (Simplified).

## Input

> 请阅读 START.md，并帮我做一个产品验证。我有一个针对小企业的 SaaS 想法。

## Expected behavior

- Reply in Mandarin.
- Select `customer-persona` (031) then `product-idea-validation` (038).
- Keep workflow IDs / slugs / paths in English.
- Mirror user's language unless a deliverable language is requested.

## Expected questions (in Mandarin)

1. "目标客户是谁？他们的核心痛点是什么？"
2. "你有任何关于这个问题存在的证据吗？"

## Failure conditions

- Replying in English.
- Translating "customer-persona" to "客户画像".
- Skipping the validation step.
