# Language Case — Japanese Conversation

## Setup

- Mode: `quick`.
- Detected language: Japanese.

## Input

> リポジトリのSTART.mdを読んで、手短にcontent-editingで私の下書きを校閲してください。

## Expected behavior

- Reply in Japanese.
- Run `content-editing` (009) — the user named the workflow explicitly.
- Preserve workflow slug `content-editing` in English.

## Expected output

A short editorial review in Japanese with severity-tagged issues.

## Failure conditions

- Replying in English.
- Translating "content-editing" to "コンテンツ編集".
- Asking clarifying questions about which workflow to use when named.
