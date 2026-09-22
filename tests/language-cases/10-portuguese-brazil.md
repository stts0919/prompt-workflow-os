# Language Case — Brazilian Portuguese

## Setup

- Mode: `guide`.
- Detected language: Brazilian Portuguese.

## Input

> Leia o START.md e me ajude com um decision-memo. Estou decidindo se lanço o produto no Brasil primeiro ou nos EUA.

## Expected behavior

- Reply in Brazilian Portuguese.
- Run `decision-memo` (069) — possibly via `business-decision` (052) first.
- Preserve English workflow slugs.

## Expected questions

1. "Quais critérios de decisão importam mais (tamanho do mercado, encaixe do produto, risco, time-to-revenue)?"
2. "Que evidências você já tem ou precisa搜集?"

## Failure conditions

- Replying in European Portuguese or English.
- Inventing market numbers.
- Skipping the criteria question.
