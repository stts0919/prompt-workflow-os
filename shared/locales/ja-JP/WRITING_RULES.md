# Writing Rules — `ja-JP` (Japanese — Japan)

> Source-of-truth file for the `ja-JP` writing rules. Lives under
> `shared/locales/ja-JP/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in
Japanese for Japan readers. Covers keigo (honorific language),
punctuation, loanword handling, and channel-specific register.

Does not cover:

- Classical Japanese (文語 / bungo).
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `ja-JP` layer when **all** hold:

1. User requested output in Japanese, **or** explicitly named Japan as
   target market, **or** the input contains Japanese characters.
2. Selected workflow's `localization.supported_locales` includes
   `ja-JP`, or category default applies.

When the user explicitly says 敬語 (keigo), 丁寧 (polite), or
タメ口 (casual), respect the explicit register.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Japanese | Japanese | Japan | Load `ja-JP`. |
| English | Japanese | Japan | Load `ja-JP`. |
| Japanese | English | any | Skip ja-JP; use en-US / en-GB. |

## D. Protected content

Same as other locale layers:

- Code, identifiers, URLs, brand names.
- Direct quotations, citations, regulatory disclosures.
- Numbers, units, currency, dates.
- Required technical or legal wording.

## E. Japanese language guidance

### E.1 Keigo (honorific language)

Three layers, often combined:

- **Sonkeigo (尊敬語)**: respect for the other party's actions.
  Example: 言う → おっしゃる, 行く → いらっしゃる.
- **Kenjōgo (謙譲語)**: humility for one's own (or in-group's)
  actions. Example: 言う → 申す, 行く → 参る.
- **Teineigo (丁寧語)**: polite verb endings. Example: 食べる →
  食べます, 行く → 行きます.

Most business writing uses `desu / masu` form (丁寧体) combined with
kenjōgo for self-reference and sonkeigo for the recipient's actions.

Casual writing (Twitter, LINE, friends) drops keigo and uses だ / である
form (常体) plus sentence-ending particles (ね、よ、かな).

NEVER mix keigo levels mid-document. If the document opens with
「拝啓」 (formal opener), it must close with 「敬具」 (formal
opener's matching closer), and the body uses 謙譲語 for self /
丁寧語 for recipient.

### E.2 Punctuation

- Full-width punctuation: 「、」comma, 「。」period.
- Quotes: 「」 for primary, 『』 for nested.
- Avoid Western commas `,` and periods `.` in body text (technical
  documents may use ASCII for code / numbers).
- Sentence-ending period is mandatory (Japanese convention).
- No space between Japanese characters and punctuation (e.g.
  「日本語を勉強します。」, not 「日本語を勉強します。 」).

### E.3 Numbers, dates, currency

- Currency: `¥100` (no space) for yen. `USD 100` or `100ドル` for
  US dollars. `100ユーロ` for euros. No space between number and
  円 (¥100).
- Date: `2026年9月22日` (kanji form, most common); `2026/09/22` (slash
  form, technical); `2026-09-22` (ISO, technical only).
- Time: `14時30分` (kanji, common); `14:30` (24-hour, technical /
  formal).
- Numbers: 全角 (full-width) digits `１２３` in formal; 半角 (half-width)
  `123` in technical / business common. Comma separator for thousands:
  `1,000`, `1,000,000`.
- Counter words (助数詞) matter: 一人 (one person), 二人 (two people),
  一本 (one long thin thing), 一枚 (one flat thing). Use the right
  counter for the noun.

### E.4 Loanwords (katakana)

- Established loanwords use katakana: コーヒー (coffee), コンピュータ
  (computer), ダウンロード (download).
- Brand names keep their English form: Apple, Google, GitHub.
- Mixed-script: 「GitHub リポジトリ」 is common (English brand +
  Japanese noun).
- Avoid transliterating every English term; preserve English when
  the user uses English in the source.

### E.5 Honorifics and titles

- さん: most common honorific (gender-neutral, polite).
- 様 / さま: more formal than さん (used in formal letters).
- 先生 / せんせい: for teachers, doctors, lawyers, politicians.
- 社長 / 部長 / 課長: job titles, often with さん in polite contexts.
- Avoid くん / ちゃん outside very casual contexts; reserved for
  children / very close relationships.

### E.6 Casual register

Sentence-ending particles:

- ね: agreement-seeking, soft assertion. 「いいね」「そうだね」
- よ: emphasis / new information. 「いいよ」「行くよ」
- かな / かしら: uncertainty / wondering. 「どうしようかな」
- わ: feminine / literary softener. 「行くわ」
- ぞ / ぜ: masculine emphatic. 「行くぞ」(plain)
- や: dialect / casual. 「行くや」(Kansai)

Casual contractions (rougher register, only in chat):

- 〜ている → 〜てる
- 〜てしまう → 〜ちゃう
- 〜ておく → 〜とく
- 〜なくてはいけない → 〜なくちゃいけない

Avoid these in business / formal writing.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| Email (business) | `ja-jp-email-formal` | Very high keigo, 拝啓 / 敬具, polite openings |
| Email (casual) | `ja-jp-email-casual` | Polite but shorter, no 拝啓 |
| Twitter / X | `ja-jp-twitter-casual` | Sentence-ending particles, contractions OK |
| LINE | `ja-jp-line-casual` | Short messages, emojis OK, casual particles |
| note.com long-form | `ja-jp-long-form-article` | Polite, structured, narrative |
| Business document | `ja-jp-business-document` | Very high keigo, formal register |
| Customer support | `ja-jp-customer-support` | Polite, specific action, apologetic |
| Sales / landing | `ja-jp-landing-page-clear` | Headline-driven, evidence, CTA |
| General professional | `ja-jp-friendly-professional` | Polite, default fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locales, plus:

- Avoid 「〜と思われます」「〜と言えるでしょう」 excessive hedge
  stacking.
- 「〜することができます」 passive voice (often wordy); prefer
  「〜できます」or active voice.
- 「非常に」「大変」 excessive intensifiers.
- 「お忙しいところ」 overuse in openings (formal letter cliché).
- 「なるほど」「確かに」 agreement markers used as fillers.

## H. Editing intensity rules

Same as other locales:

- `none` — protect everything.
- `light` — minimal cleanup.
- `standard` — apply glossary + AI-pattern reduction.
- `strict_precision` — high precision, mandatory for legal / medical /
  financial / security / compliance.

The router auto-escalates to `strict_precision` for regulated content.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** 私達の会社はソフトウェア開発をします。

**After:** 私たちは、[業界]向けのエンタープライズソフトウェアを開発しています。

### I.2 Intensity: standard, channel: email-formal

**Before:** 私たちの会社のサービスを使ってください。

**After:**
```text
拝啓

時下ますますご清栄のこととお慶び申し上げます。
貴社ますますご発展のこととお喜び申し上げます。

[株式会社名]の[氏名]と申します。
このたびは、[製品 / サービス]のご案内を差し上げたく、
ご連絡いたしました。

[本文]

ご検討いただけますと幸いです。
ご不明な点がございましたら、お気軽にお問い合わせください。

敬具

[氏名]
[役職]
[株式会社名]
[連絡先]
```

### I.3 Intensity: light, channel: translation

**Before (English):** "Welcome to our service. Please feel free to
contact us if you have any questions."

**After:** 私たちのサービスへようこそ。ご質問がございましたら、
お気軽にお問い合わせください。

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** 多くの人がこの製品を好きです。

**After:** 2025年のユーザー調査（n=1,247、95%信頼区間）によると、
回答者の78%が[競合製品]よりも[製品]を希望すると回答しました。
結果は[人口統計学的]サブサンプルに適用されます。

### I.5 Intensity: standard, channel: customer-support

**Before:** 不便をかけてすみません。すぐに処理します。

**After:**
```text
[お客様名] 様

このたびは、ご不便をおかけしており申し訳ございません。
お問い合わせいただいた[内容]について、確認いたしましたので
ご報告いたします。

[具体的な対応内容]

[具体的な所要時間]以内に対応させていただきます。

ご不明な点がございましたら、お気軽にお問い合わせください。

[担当者名]
[会社名]
[連絡先]
```

## K. Safety boundaries

Same as other locale layers:

- Does not claim to bypass AI detection, remove watermarks, or prove
  human authorship.
- Does not silently convert currency or units.
- Does not override user-recorded terminology.
- Default to neutral, factual phrasing on regulatory / political
  topics.

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — Loanword handling, katakana
  conventions, business terms.
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles.
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — Quality gate.
- [`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md) —
  core schema.
- [`../zh-TW/README.md`](../zh-TW/README.md) — reference
  structure.

## M. Citations

Editorial principles borrowed from Japanese style guides (NHK 放送
用語, 記者ハンドブック, 共同通信社 表記Guidelines). Specific
citations TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.