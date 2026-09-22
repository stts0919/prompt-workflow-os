# Shared Style Profile Schema

> Resolves SPEC.md open question 4. Both `shared/locales/zh-TW/STYLE_PROFILES.md`
> and `shared/locales/zh-CN/STYLE_PROFILES.md` carry style profiles that
> describe how the layer rewrites prose for a given channel. The two packs
> agree on a **core schema** but extend it with locale-specific fields that
> capture differences that matter in one audience and not the other.

## Why a shared schema

Several `zh-tw-*` profiles have near-equivalents in `zh-cn-*`
(`friendly-professional`, `business-consulting`, `email-professional`,
`landing-page-clear`, …). The voices are distinct — Taiwan and Mainland
writing diverge on tone, formality, and platform conventions — but the
**shape** of a profile is the same. A shared schema:

- Lets a workflow declare a profile by code (`zh-tw-friendly-professional`
  vs `zh-cn-friendly-professional`) and the router can fall back gracefully
  when the locale layer does not implement a specific profile.
- Lets a future locale pack implement the core schema first, then add
  locale-specific fields as needed.
- Makes automated tooling (the harness, an auto-scorer, a profile
  catalogue) possible.

## Core schema

Every profile declares:

| Field | Type | Required | Purpose |
| --- | --- | :-: | --- |
| `id` | string | yes | Stable identifier. Use `<locale>-<name>` (e.g. `zh-tw-friendly-professional`). |
| `locale` | string | yes | Which audience this profile serves (e.g. `Taiwan`, `Mainland China`). |
| `channel` | string | yes | Where the profile applies (e.g. `email`, `xiaohongshu`, `linkedin`, `general`). |
| `formality` | enum | yes | `high` / `medium` / `low`. |
| `second_person_policy` | string | yes | How to address the reader (e.g. 「你」 vs 「您」, 「姐妹们」 vs 「家人们」, formal vs direct). |
| `punctuation_notes` | string | yes | Spacing, marks, and conventions specific to this profile. |
| `avoid` | list | yes | Patterns the layer avoids (e.g. 程式化結尾, 三段式排比, AI 模式). |
| `exemplar` | string | yes | A short paragraph in the profile's voice. |

## Locale-specific extensions

A locale pack may add fields that the core schema does not require.
Existing locale-specific fields:

### `zh-TW` extension fields

Used in [`zh-TW/STYLE_PROFILES.md`](zh-TW/STYLE_PROFILES.md):

| Field | Why it is zh-TW-specific |
| --- | --- |
| `best_for` | Surfaces which workflows and audiences the profile suits. |
| `tone` | The overall affective tone (warmer / cooler / playful). The Mainland pack handles this in the exemplar instead. |
| `directness` | How directly the profile states conclusions. Taiwan audiences accept a wider range than Mainland B2B contexts. |
| `sentence_rhythm` | Long/medium/short sentence preference. Taiwan social media favors short; Taiwan B2B favors medium. |
| `first_person_policy` | 「我們」 vs 「本公司」 vs 「敝公司」 vs no first person. Each variant carries a different politeness weight. |
| `rhetorical_question_policy` | Whether to use rhetorical questions to engage readers (Threads yes, B2B report no). |
| `evidence_standard` | What counts as sufficient evidence (anecdote / statistic / citation). |
| `preferred_patterns` | Sentence patterns to prefer (e.g. opening with a concrete number vs opening with a thesis). |
| `ending_style` | How to close (CTA / soft close / question / nothing). |

### `zh-CN` extension fields

Used in [`zh-CN/STYLE_PROFILES.md`](zh-CN/STYLE_PROFILES.md):

| Field | Why it is zh-CN-specific |
| --- | --- |
| `common_pitfalls` | A flat list of patterns to avoid (Mainland-specific clichés like 「赋能」, 「抓手」, 「闭环」). The Taiwan pack captures this in `avoid` plus separate `tone` and `directness` notes. |

### Adding a new field to either pack

1. Add the field with one or two example values in the existing profile
   that uses it most heavily.
2. Update this document's extension table.
3. If the field is locale-neutral, propose moving it to the core schema.
4. New locale packs can ignore locale-specific fields; the core schema is
   the floor.

## How the router selects a profile

The router's profile-selection logic is in
[`ROUTING_RULES.md`](LOCALE_ROUTING_RULES.md). It looks at:

1. The workflow's `localization.default_style_profile` (if declared).
2. The workflow's `localization.locale_style_profile_overrides.<locale>`
   (per-locale override).
3. The category default if neither is set.
4. The channel hint from the user's request.

When the locale layer is active and the requested profile is missing from
the active pack, the router falls back to the locale's generic professional
profile (`<locale>-friendly-professional`) and emits a one-line note to the
operator.

## Compatibility notes

- Pre-v1.1.0 profiles in `zh-TW/STYLE_PROFILES.md` (the legacy
  `shared/ZH_TW_STYLE_PROFILES.md`) used 14 fields. v1.1.0 brings them
  into the core schema where possible; the 9 extension fields above remain
  valid in `zh-TW` but are ignored by `zh-CN`.
- Pre-v1.1.0 profiles in `zh-CN/STYLE_PROFILES.md` already followed this
  shape (the `common_pitfalls` field maps directly to `avoid`; the
  exemplar maps directly). The mapping is documented above.
- New profiles added to either pack should declare at least the 8 core
  fields. Locale-specific fields are optional.

Last revised 2026-09-22.