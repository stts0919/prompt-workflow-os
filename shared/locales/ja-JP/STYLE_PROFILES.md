# Style Profiles — `ja-JP` (Japanese — Japan)

> Source-of-truth file for the `ja-JP` style profiles. Lives under
> `shared/locales/ja-JP/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for Japanese. Each
profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile uses:

- **Code**: identifier.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: Japan.
- **`punctuation_notes`**: punctuation conventions.
- **`common_pitfalls`**: patterns the layer avoids.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `ja-jp-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: あなた / 貴社 (formal) / あなた (less formal).
- **`formality`**: medium.
- **`locale`**: Japan.
- **`punctuation_notes`**: 全角 punctuation 「、」「。」「」」;
  no space between Japanese characters and punctuation; English
  brand names stay English.
- **`common_pitfalls`**:
  - 「〜と思われます」「〜と言えるでしょう」 excessive hedge stacking.
  - 「非常に」「大変」 excessive intensifiers.
  - Mixing です / ます with だ / である in same document.
- **`exemplar`**: 私たちは、[業界]向けのエンタープライズソフトウェアを
  開発しています。

## 2. `ja-jp-email-formal`

- **Channel**: business email (formal).
- **`second_person`**: 貴社 / 貴殿.
- **`formality`**: very high.
- **`locale`**: Japan.
- **`punctuation_notes`**: 全角 punctuation; 拝啓 opener;
  敬具 closer; very high keigo throughout.
- **`common_pitfalls`**:
  - Dropping to casual register mid-email.
  - 「お忙しいところ」 overuse in opener.
  - 「なるほど」 / 「確かに」 agreement markers (too casual).
- **`exemplar**:
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

## 3. `ja-jp-email-casual`

- **Channel**: casual / internal email.
- **`second_person`**: あなた / みなさん.
- **`formality`**: medium.
- **`locale`**: Japan.
- **`punctuation_notes`**: full-width punctuation; no 拝啓 / 敬具;
  polite but not ceremonial.
- **`common_pitfalls`**:
  - Over-formality (slows down internal communication).
  - Casual particles (ね / よ) leaking in.
- **`exemplar`**: お疲れ様です。[件名]について、ご確認をお願いします。
  [詳細]。質問があれば、気軽に聞いてください。

## 4. `ja-jp-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: あなた / 皆さん.
- **`formality`**: low.
- **`locale`**: Japan.
- **`punctuation_notes`**: casual punctuation; sentence-ending
  particles OK (ね、よ); contractions OK (〜てる、〜ちゃう).
- **`common_pitfalls`**:
  - Keigo leaking into casual post.
  - Excess formality kills engagement.
  - Excess emoji.
- **`exemplar`**: 半年待ったツールがやっと新機能出してくれた✨
  でも結局自分で2週間で作った方が早かった。DIY 最高。

## 5. `ja-jp-line-casual`

- **Channel**: LINE messages.
- **`second_person`**: あなた / [name] + さん.
- **`formality`**: low.
- **`locale`**: Japan.
- **`punctuation_notes`**: short messages; emoji OK; line breaks
  optional; casual particles.
- **`common_pitfalls`**:
  - Over-formality in chat (awkward).
  - Mixing English / Japanese awkwardly.
- **`exemplar`**: 了解！明日 14 時に集合ね👍 遅れないで！

## 6. `ja-jp-long-form-article`

- **Channel**: note.com / blog long-form.
- **`second_person`**: あなた / 読者.
- **`formality`**: medium-high.
- **`locale`**: Japan.
- **`punctuation_notes`**: full-width punctuation; structured with
  H2 / H3; pull quotes.
- **`common_pitfalls`**:
  - "結論から言いますと" cliché opener.
  - 「〜と思われる」 excessive hedging.
  - 「お忙しいところ」 / 「ご多忙のところ」 formal letter clichés
    leaking in.
- **`exemplar`**: 多くのチームが同じ壁にぶつかります：[問題]。過去
  1年間で[N]チームと仕事をしてきましたが、解決できたチームと
  できなかったチームを分かつ3つのパターンが見えてきました。

## 7. `ja-jp-business-document`

- **Channel**: formal business documents (proposals, contracts).
- **`second_person`**: 貴社 / 貴殿.
- **`formality`**: very high.
- **`locale`**: Japan.
- **`punctuation_notes`**: full-width; structured headings; data
  tables; numbered lists.
- **`common_pitfalls`**:
  - Dropping keigo mid-document.
  - Missing 「以上」 closer.
  - Numbers without units.
- **`exemplar`**: 本提案書では、[課題]に対する解決策として、
  [製品名]の導入を推奨いたします。導入により[効果]が見込まれ、
  投資回収期間は[期間]と試算いたします。

## 8. `ja-jp-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: お客様 / [name] 様.
- **`formality`**: high.
- **`locale`**: Japan.
- **`punctuation_notes`**: polite empathy first; specific action
  with timeline; apologetic register.
- **`common_pitfalls`**:
  - 「ご不便をおかけしており申し訳ございません」 cliché without
    specifics.
  - Defensive tone.
  - Missing apology for confirmed error.
- **`exemplar**:
```text
[お客様名] 様

このたびは、ご不便をおかけしており申し訳ございません。
お問い合わせいただいた[内容]について、確認いたしましたので
ご報告いたします。

[具体的な対応内容]

[具体的な所要時間]以内に対応させていただきます。
進捗があり次第、改めてご連絡いたします。

ご不明な点がございましたら、お気軽にお問い合わせください。

[担当者名]
[会社名]
[連絡先]
```

## 9. `ja-jp-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: あなた.
- **`formality`**: medium.
- **`locale`**: Japan.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text action + outcome.
- **`common_pitfalls`**:
  - 「革命的」 / 「画期的」 / 「業界初」 exaggeration.
  - Multiple CTAs.
  - Missing social proof (数値 / 事例).
- **`exemplar`**: **見出し:** [期間]で[成果]を。
  **サブ見出し:** [一行での説明]。**CTA:** 無料トライアルを
  始める →

## 10. `ja-jp-finance-formal`

- **Channel**: financial reports, regulatory disclosures.
- **`second_person`**: not used (formal audience).
- **`formality`**: very high.
- **`locale`**: Japan.
- **`punctuation_notes`**: precise figures; 全角 digit in formal;
  currency format `¥100` (no space).
- **`common_pitfalls`**:
  - Promising returns without 「過去の運用実績は将来の運用成果を
    保証するものではない」 disclaimer.
  - Rounding figures to mislead.
  - Missing required disclosures (金融商品取引法 準拠).
- **`exemplar`**: 当ファンドの運用実績は、2024年8.2%、2025年5.1%、
  2026年9月22日時点で年初来-1.3%です。過去の運用実績は将来の運用
  成果を保証するものではなく、[リスク許容度]の投資家向けです。

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `ja-jp-friendly-professional` |
| content | Twitter / X | `ja-jp-twitter-casual` |
| content | LINE | `ja-jp-line-casual` |
| content | note.com | `ja-jp-long-form-article` |
| business | email (formal) | `ja-jp-email-formal` |
| business | email (casual) | `ja-jp-email-casual` |
| business | proposal / contract | `ja-jp-business-document` |
| business | sales / landing | `ja-jp-landing-page-clear` |
| research | report | `ja-jp-business-document` |
| business | financial | `ja-jp-finance-formal` |
| any | customer support | `ja-jp-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.