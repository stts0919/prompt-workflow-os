# Writing Rules — `ko-KR` (Korean — South Korea)

> Source-of-truth file for the `ko-KR` writing rules. Lives under
> `shared/locales/ko-KR/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in
Korean for South Korea readers. Covers honorific register,
punctuation, loanword handling, and channel-specific conventions.

Does not cover:

- North Korean language conventions.
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `ko-KR` layer when **all** hold:

1. User requested output in Korean, **or** explicitly named South Korea
   as target market, **or** the input contains Korean characters.
2. Selected workflow's `localization.supported_locales` includes
   `ko-KR`, or category default applies.

When the user explicitly says 존댓말 / formal, honor the explicit
register.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Korean | Korean | South Korea | Load `ko-KR`. |
| English | Korean | South Korea | Load `ko-KR`. |
| Korean | English | any | Skip ko-KR; use en-US / en-GB. |

## D. Protected content

Same as other locale layers.

## E. Korean language guidance

### E.1 Honorific register

Three main levels:

- **합쇼체 (-습니다 / -입니다)**: most formal; for business, official,
  formal letters. Default for first contact with unknown seniority.
- **해요체 (-어요 / -여요 / -이에요)**: polite casual; for daily
  business, customer support, internal email. Default for most
  professional content.
- **반말체 (-다 / -야 / -어)**: plain / intimate; for friends, family,
  very casual chat, Naver blog comments.

NEVER mix registers mid-document. Default to 해요체 for most
professional writing. Reserve 합쇼체 for explicitly formal contexts
(letters, contracts, official documents).

### E.2 Punctuation

- Full-width comma `,` and period `.`.
- Quotes: 「」 for primary; 『』 for nested (rare).
- Colon: `:` (half-width), common in lists.
- Question / exclamation: `?` `!` (half-width).
- No space between Korean characters and punctuation (e.g. 「안녕하세요.」
  not 「안녕하세요 .」).
- Space between Korean and English (e.g. 「GitHub 리포지토리」).

### E.3 Numbers, dates, currency

- Currency: `₩` symbol before number; no space (e.g. `₩10,000`).
  Use `KRW` in international contexts.
- Date: `2026년 9월 22일` (kanji-like, common); `2026. 9. 22.` (period
  form); `2026-09-22` (ISO, technical).
- Time: `오후 2시 30분` (12-hour with AM/PM); `14:30` (24-hour,
  common).
- Numbers: comma separator for thousands (`10,000`); 만 / 억 for large
  numbers (`1만`, `100억`).
- Phone: `010-1234-5678` (mobile); `02-1234-5678` (Seoul landline).

### E.4 Loanwords (English → Hangul)

Common English terms transliterated to Hangul.

- 컴퓨터 (computer), 인터넷 (internet), 이메일 (email), 소프트웨어
  (software), 데이터 (data), 서버 (server), 클라이언트 (client).
- Established loanwords use Hangul; brand names stay English.
- Loanword conventions vary by generation: older Koreans use Hangul
  transliteration; younger Koreans often prefer English directly.

### E.5 Honorifics and titles

- さん: NOT used in Korean. Use 씨 or 님.
- 씨 (ssi): informal respectful (between peers).
- 님 (nim): formal respectful (for customers, executives, officials).
- 선생님 (seonsaengnim): teachers, doctors, lawyers, politicians.
- 사장님 (sajangnim): CEO (formal); 회장님 (hoejangnim): chairman.
- 부장 (bujang) / 차장 (chajang) / 과장 (gwajang) / 대리 (daeri): job
  titles (often with 님 in polite contexts).

### E.6 Casual register

Sentence-ending forms:

- ~요 / ~어요: polite casual, default.
- ~네 / ~군: agreement / realization. 「맞네」「좋군」
- ~지: explanation / question. 「맞지」「가자」
- ~잖아: reminder. 「그렇잖아」
- ~아 / ~어 / ~야: intimate casual.
- Avoid mixing polite / plain in same paragraph.

Casual contractions (chat only):

- ~하고 있어 → ~하고 있어 (formal) / ~하고 있어 (casual same)
- ~거든: explanation
- ~는 거야 / ~는 거지: emphasis

Avoid these in business / formal writing.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| Email (business) | `ko-kr-email-formal` | 합쇼체, formal opener |
| Email (casual) | `ko-kr-email-casual` | 해요체, friendly |
| Twitter / X | `ko-kr-twitter-casual` | 짧게, casual |
| Naver blog | `ko-kr-naver-blog` | Long-form, structured |
| KakaoTalk | `ko-kr-kakao-casual` | Short messages, casual |
| Business document | `ko-kr-business-document` | Very formal, structured |
| Customer support | `ko-kr-customer-support` | Polite, specific action |
| Sales / landing | `ko-kr-landing-page-clear` | Headline-driven, CTA |
| Long-form article | `ko-kr-long-form-article` | Structured, citation-aware |
| General professional | `ko-kr-friendly-professional` | Polite, default fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locales, plus:

- Avoid 「~라고 생각합니다」「~라고 할 수 있습니다」 excessive
  hedge stacking.
- 「매우」「정말」「아주」 excessive intensifiers.
- 「바쁘신 중에」 formal letter cliché.
- 「감사합니다」「수고하셨습니다」 overuse.

## H. Editing intensity rules

Same as other locales.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** 저희 회사는 소프트웨어 개발을 합니다.

**After:** 저희는 [업종] 분야 엔터프라이즈 소프트웨어를 개발하고 있습니다.

### I.2 Intensity: standard, channel: email-formal

**Before:** 저희 회사의 서비스를 사용해 주세요.

**After:**
```text
[회사명] [이름] 드림.

안녕하세요.
[회사명] [이름]입니다.
저희는 [대상 고객]에게 [특정 결과]를 제공하는 [회사명]입니다.
귀사의 최근 활동을 큰 관심으로 지켜보고 있었습니다.

향후 몇 주 내에 15분 정도 통화하실 의향이 있으신지 궁금합니다.
함께할 수 있는지 확인해 보고 싶습니다.

감사합니다.

[이름]
[직함]
[회사명]
[연락처]
```

### I.3 Intensity: light, channel: translation

**Before (English):** "Welcome to our service. Please feel free to
contact us if you have any questions."

**After:** 저희 서비스에 오신 것을 환영합니다. 궁금한 점이 있으시면
편하게 연락 주세요.

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** 대부분의 사용자가 이 제품을 좋아합니다.

**After:** 2025년 사용자 설문조사 (n=1,247, 95% 신뢰구간)에 따르면,
응답자의 78%가 [경쟁 제품]보다 [제품]을 선호한다고 답했습니다.
결과는 [인구통계학적] 하위 표본에 적용됩니다.

### I.5 Intensity: standard, channel: customer-support

**Before:** 불편을 드려 죄송합니다. 곧 처리하겠습니다.

**After:**
```text
[고객명] 님,

불편을 드려 죄송합니다.
문의하신 [내용]에 대해 확인하여 보고드립니다.

[구체적인 대응 내용]

[구체적인 소요 시간] 이내에 처리해 드리겠습니다.

기타 문의 사항이 있으시면 편하게 연락 주세요.

[담당자 이름]
[회사명]
[연락처]
```

## K. Safety boundaries

Same as other locale layers.

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — Loanword handling, business /
  platform terms.
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles.
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — Quality gate.
- [`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md) —
  core schema.
- [`../zh-TW/README.md`](../zh-TW/README.md) — reference
  structure.

## M. Citations

Editorial principles borrowed from Korean style guides (표준 한국어
대사전, 국립국어원 한국어 문법, 매체별 가이드라인). Specific citations
TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.