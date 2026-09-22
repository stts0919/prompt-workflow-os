# Locale Routing Rules

How the router decides which locale pack to load.

## Activation matrix

```text
conversation_language == zh-TW (or detects Taiwan Traditional Chinese)
  AND requested_locale == Taiwan OR unspecified Traditional Chinese
  → activate zh-TW pack
  → default style profile by workflow category
  → default editing intensity: standard; escalate to strict_precision for legal/medical/financial/security/compliance

conversation_language == zh-TW
  AND requested_locale == Hong Kong
  → honor user request; do NOT apply zh-TW glossary by default
  → activate zh-HK pack if it exists; else reply in zh-HK friendly form

conversation_language == zh-CN (Simplified Chinese)
  AND requested_locale == Mainland China
  → honor user request; activate zh-CN pack if it exists

conversation_language == yue-Hant-HK
  → activate yue-Hant-HK pack if it exists; else reply in zh-HK friendly form

conversation_language == en-US
  → activate en-US pack if it exists; else default to universal English rules

conversation_language == en-GB
  → activate en-GB pack if it exists; else default to universal English rules

conversation_language == ja-JP
  → activate ja-JP pack if it exists

conversation_language == ko-KR
  → activate ko-KP pack if it exists

conversation_language == id-ID
  → activate id-ID pack if it exists

conversation_language == vi-VN
  → activate vi-VN pack if it exists

locale pack missing for requested locale
  → use universal multilingual + quality rules only
  → record missing-locale in context ledger
  → notify the user briefly that the locale-specific pack is not yet available
```

## Mixed-language inputs

When the input language is unclear or mixed:

1. Detect the dominant script (Hant / Hans / Kana / Hangul / Latin).
2. If Hant with Cantonese vocabulary, prefer `yue-Hant-HK`.
3. If Hant without Cantonese vocabulary, default to `zh-TW` unless the user indicates another locale.
4. If mixed Hant + Hans, ask one short clarification.
5. If Latin with the user supplying locale hints (e.g., 「請用香港中文」), honor the locale.

## Output language vs locale

The router distinguishes:

- **Output language**: the language of the deliverable.
- **Locale**: the conventions, terminology, and culture of the deliverable.

For most requests, output language and locale match. When they differ (Case A in the router spec), the locale layer applies only to the locale's primary language. An English email body is not subject to `zh-TW` prose rules even when the conversation language is Traditional Chinese.

## Style profile selection (zh-TW example)

When the locale layer is active, the router chooses a style profile by reading this in order:

1. `localization.locale_style_profile_overrides[locale]` from the workflow file.
2. Platform / channel inference (Threads → `zh-tw-threads-insightful`).
3. Workflow category default (research → `zh-tw-research-precise`).
4. Fallback: `zh-tw-conversational-help`.

Future locales should follow the same priority order.

## Editing intensity selection

```text
content type                   → intensity
----------------------------------------
protected spans (code, IDs,
  brand names, citations)     → none
structured technical output    → light
default user-facing content    → standard
legal / medical / financial /
  security / compliance /
  citation-heavy statistical  → strict_precision
```

The router can override based on user instruction (e.g., "be very careful about numbers" → `strict_precision`).

## Locale override recording

Whenever the user explicitly overrides a locale decision (e.g., 「用香港中文」), record:

- the explicit locale,
- the time of the override,
- the context (per-user override vs per-conversation override).

The router honors the override for the duration of the conversation. Per-user overrides are out of scope for this scaffold.
