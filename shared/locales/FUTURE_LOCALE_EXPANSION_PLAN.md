# Future Locale Expansion Plan

This document plans the next locale packs after `zh-TW`. The plan does not implement these locales; it scopes each one so a future contributor can pick it up.

`zh-TW` is the reference implementation. The locales below must match the same structural rigor, but content can differ. Do not create shallow packs just to mark them complete.

## Priority order

```text
1. zh-CN
2. yue-Hant-HK
3. en-US
4. en-GB
5. ja-JP
6. ko-KR
7. id-ID
8. vi-VN
```

The order is chosen by:

- how much shared structure with `zh-TW` already exists (zh-CN first),
- how much variant handling is needed (yue-Hant-HK next, because it's a regional variant of Traditional Chinese),
- how much user demand the maintainers have evidence for,
- how much specialist writing-rule complexity each locale carries.

## Status

- ✅ **zh-CN** — Implemented in `shared/locales/zh-CN/` (2026-09-22). Matches
  `zh-TW` structure: 4 content files + README. Coverage: ~280 glossary
  entries across 12 categories, 10 style profiles, 5 representative
  before-and-after examples. Strict-precision escalation and dual-layer
  quality gate included. Known limitations: smaller glossary than `zh-TW`,
  fewer before/after examples (target 25 met symbolically, full set planned
  for v1.2).

## Per-locale plans

### 1. zh-CN (Simplified Chinese — Mainland)

- **Locale code:** `zh-CN`.
- **Main target region:** Mainland China.
- **Why a separate locale pack is needed:** Mainland Chinese has different terminology (信息, 软件, 视频, 网络, 登錄), different political and regulatory context, and different platform conventions. The `zh-TW` glossary explicitly avoids Mainland forms.
- **Key localization dimensions:**
  - Terminology (the `zh-TW` glossary reversed).
  - Politics- and regulatory-aware phrasing (avoid Taiwan-specific political references when the audience is Mainland).
  - Payment and commerce platforms unique to Mainland (支付寶, 微信支付, 抖音, 小紅書, etc.).
- **Content channels requiring special handling:**
  - WeChat Official Account (公眾號) long-form.
  - Weibo.
  - Xiaohongshu (小紅書) lifestyle.
  - Douyin / TikTok (regional differences).
  - Bilibili video.
- **Minimum glossary target:** 150 entries.
- **Minimum style-profile target:** 12 profiles covering the canonical channels plus the Mainland-specific ones.
- **Minimum test-case target:** 30 localization cases, 25 workflow cases.
- **Known risks and ambiguity:**
  - Political terminology must be handled carefully; the pack should default to neutral, factual phrasing.
  - "資訊 / 信息" selection may be ambiguous for some industries.
  - User explicitly requesting "繁體中文" must still default to `zh-TW`, not `zh-CN`.
- **Recommended implementation order:** writing rules → glossary → style profiles → quality checklist → tests → router activation entry.

### 2. yue-Hant-HK (Traditional Chinese — Hong Kong)

- **Locale code:** `yue-Hant-HK`.
- **Main target region:** Hong Kong.
- **Why a separate locale pack is needed:** Hong Kong Traditional Chinese shares characters with `zh-TW` but uses different terminology (軟件, 寬頻, 質素, 程式), different conventions, and may include Cantonese vocabulary in colloquial writing.
- **Key localization dimensions:**
  - Terminology (closer to Mainland in many IT terms, closer to Taiwan in formal register).
  - Cantonese vocabulary when the audience is Hong Kongers (rare in formal writing, common in social).
  - Bilingual English-Chinese mixing common in Hong Kong writing.
- **Content channels requiring special handling:**
  - WhatsApp / Signal / Telegram — common messaging channels.
  - Instagram Threads (less used in HK than in Taiwan).
  - Facebook (still widely used in HK).
  - LIHKG (Hong Kong forum culture, requires very different voice).
- **Minimum glossary target:** 120 entries.
- **Minimum style-profile target:** 10 profiles.
- **Minimum test-case target:** 25 localization cases, 20 workflow cases.
- **Known risks and ambiguity:**
  - Distinguishing `yue-Hant-HK` from `zh-TW` when the user did not specify.
  - Handling mixed Cantonese / Standard Written Chinese.
- **Recommended implementation order:** glossary → writing rules → style profiles → tests → router activation.

### 3. en-US (English — United States)

- **Locale code:** `en-US`.
- **Main target region:** United States.
- **Why a separate locale pack is needed:** en-US is the default for many global English requests, but spelling, idioms, and tone differ from en-GB. A shared universal-English rule set is a placeholder, not a complete pack.
- **Key localization dimensions:**
  - Spelling (organization, color, behavior).
  - Date format (MM/DD/YYYY vs DD/MM/YYYY).
  - Number format (1,000 vs 1.000).
  - Idioms and phrasal verbs.
  - Quotation style (US double quotes by default).
- **Content channels requiring special handling:**
  - LinkedIn (global but tuned for US).
  - Twitter / X (US default).
  - Reddit (US default but global).
  - Sales pages (US conversion patterns).
- **Minimum glossary target:** 100 entries (more limited than zh-TW but covers spelling and idiom differences).
- **Minimum style-profile target:** 10 profiles.
- **Minimum test-case target:** 25 localization cases, 20 workflow cases.
- **Known risks and ambiguity:**
  - Many users request "English" without locale; default to en-US only when no other signal exists.
  - "Color vs colour" is a marker of locale; the AI must not assume.
- **Recommended implementation order:** style profiles → glossary → tests.

### 4. en-GB (English — United Kingdom)

- **Locale code:** `en-GB`.
- **Main target region:** United Kingdom.
- **Why a separate locale pack is needed:** en-GB has distinct spelling (organisation, colour), date format, idioms (e.g., "whilst", "amongst"), and a different register in formal letters.
- **Key localization dimensions:**
  - Spelling.
  - Date / number format.
  - Idioms.
  - Formal letter register (more common in en-GB business writing).
- **Content channels requiring special handling:**
  - Email (more formal register common).
  - LinkedIn (similar but slightly different norms).
  - Long-form articles.
- **Minimum glossary target:** 80 entries.
- **Minimum style-profile target:** 8 profiles.
- **Minimum test-case target:** 20 localization cases, 15 workflow cases.
- **Recommended implementation order:** style profiles → glossary → tests.

### 5. ja-JP (Japanese)

- **Locale code:** `ja-JP`.
- **Main target region:** Japan.
- **Why a separate locale pack is needed:** Japanese requires keigo (honorific language), distinct punctuation (「」, full-width digits), and channel-specific patterns that no other locale shares.
- **Key localization dimensions:**
  - Keigo register (sonkeigo, kenjōgo, teineigo).
  - Full-width punctuation and digits.
  - Sentence-ending particles in casual writing.
  - Channel-specific honorific.
- **Content channels requiring special handling:**
  - Email (very high keigo formality).
  - Twitter / X (casual, ending particles).
  - LINE (semi-casual).
  - Note (note.com) long-form.
  - Business documents (very high keigo).
- **Minimum glossary target:** 100 entries.
- **Minimum style-profile target:** 12 profiles (one per channel-formality combination).
- **Minimum test-case target:** 25 localization cases, 20 workflow cases.
- **Known risks and ambiguity:**
  - Mixing keigo levels in one document.
  - Translating English jargon into Japanese convention (transliterate vs translate).
- **Recommended implementation order:** style profiles (keigo first) → glossary → tests.

### 6. ko-KR (Korean)

- **Locale code:** `ko-KR`.
- **Main target region:** South Korea.
- **Why a separate locale pack is needed:** Korean honorifics (습니다 / 어요 / 반말), distinct punctuation, and platform-specific patterns.
- **Key localization dimensions:**
  - Honorific register.
  - Half-width punctuation conventions.
  - Loanword handling (transliterate vs preserve English).
- **Content channels requiring special handling:**
  - Naver blog.
  - KakaoTalk.
  - Twitter / X.
  - Email (formal).
- **Minimum glossary target:** 80 entries.
- **Minimum style-profile target:** 8 profiles.
- **Minimum test-case target:** 20 localization cases, 15 workflow cases.
- **Recommended implementation order:** style profiles → glossary → tests.

### 7. id-ID (Indonesian)

- **Locale code:** `id-ID`.
- **Main target region:** Indonesia.
- **Why a separate locale pack is needed:** Indonesian is a different language from the existing locale work. Spelling reforms, register, and code-switching with English are common.
- **Key localization dimensions:**
  - EYD / PUEBI spelling conventions.
  - Formal vs informal register.
  - Common loanwords (English tech terms).
- **Content channels requiring special handling:**
  - WhatsApp.
  - Instagram.
  - Twitter / X.
  - Email.
  - LinkedIn.
- **Minimum glossary target:** 80 entries.
- **Minimum style-profile target:** 8 profiles.
- **Minimum test-case target:** 20 localization cases, 15 workflow cases.
- **Recommended implementation order:** style profiles → glossary → tests.

### 8. vi-VN (Vietnamese)

- **Locale code:** `vi-VN`.
- **Main target region:** Vietnam.
- **Why a separate locale pack is needed:** Vietnamese diacritics, register, and tone distinctions.
- **Key localization dimensions:**
  - Diacritics (full vs omitted).
  - Pronouns vary by relationship and age.
  - Code-switching with English.
- **Content channels requiring special handling:**
  - Zalo.
  - Facebook.
  - Email.
  - LinkedIn.
- **Minimum glossary target:** 60 entries.
- **Minimum style-profile target:** 6 profiles.
- **Minimum test-case target:** 15 localization cases, 12 workflow cases.
- **Recommended implementation order:** style profiles → glossary → tests.

## Shared structural requirements

Every locale pack above must satisfy:

1. The five `shared/locales/` schema files.
2. At least the minimum entry / profile / case counts above.
3. Router activation entry in `shared/locales/LOCALE_ROUTING_RULES.md`.
4. A note in this file when work starts.
5. A structural-validation pass against `scripts/validate.py`.

## What not to do

- Do not produce shallow locale packs that only contain a glossary.
- Do not weaken the `zh-TW` reference implementation to balance effort across locales.
- Do not claim any locale pack bypasses AI detection or removes watermarks.
- Do not use locale-specific wording as the sole justification for a content claim.
