# Style Profiles — `ko-KR` (Korean — South Korea)

> Source-of-truth file for the `ko-KR` style profiles. Lives under
> `shared/locales/ko-KR/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for Korean. Each
profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile uses:

- **Code**: identifier.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: South Korea.
- **`punctuation_notes`**: punctuation conventions.
- **`common_pitfalls`**: patterns the layer avoids.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `ko-kr-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: 귀사 / 귀하 (formal); 당신 (informal, often
  avoided).
- **`formality`**: medium.
- **`locale`**: South Korea.
- **`punctuation_notes`**: full-width `,` `.`; no space between Korean
  characters and punctuation; space between Korean and English.
- **`common_pitfalls`**:
  - 「~라고 생각합니다」「~라고 할 수 있습니다」 hedge stacking.
  - 「매우」「정말」「아주」 excessive intensifiers.
  - Mixing 합쇼체 / 해요체 / 반말체 mid-document.
- **`exemplar`**: 저희는 [업종] 분야 엔터프라이즈 소프트웨어를 개발하고
  있습니다.

## 2. `ko-kr-email-formal`

- **Channel**: business email (formal).
- **`second_person`**: 귀사 / 귀하.
- **`formality`**: very high (합쇼체).
- **`locale`**: South Korea.
- **`punctuation_notes`**: full-width punctuation; formal opener
  pattern; signature block.
- **`common_pitfalls`**:
  - Dropping to 해요체 mid-email.
  - 「바쁘신 중에」 formal letter cliché overuse.
  - 「감사합니다」「수고하셨습니다」 overuse.
- **`exemplar**:
```text
[회사명] [이름] 드림.

안녕하십니까.
[회사명]의 [이름]입니다.
저희는 [대상 고객]에게 [특정 결과]를 제공하는 [회사명]입니다.
귀사의 최근 활동을 큰 관심으로 지켜보고 있었습니다.

향후 몇 주 내에 15분 정도 통화하실 의향이 있으신지 묻고자 합니다.
함께할 수 있는지 확인해 보고 싶습니다.

감사합니다.

[이름]
[직함]
[회사명]
[연락처]
```

## 3. `ko-kr-email-casual`

- **Channel**: casual / internal email.
- **`second_person`**: 귀하 (less formal) / 당신 (informal).
- **`formality`**: medium (해요체).
- **`locale`**: South Korea.
- **`punctuation_notes`**: full-width punctuation; no formal opener;
  polite but not ceremonial.
- **`common_pitfalls`**:
  - Over-formality in internal communication.
  - Casual particles (네 / 지) leaking into professional email.
- **`exemplar`**: 수고하셨습니다. [제목] 관련해서 확인 부탁드립니다.
  [세부 사항]. 질문 있으시면 편하게 물어봐 주세요.

## 4. `ko-kr-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: 당신 / 여러분.
- **`formality`**: low.
- **`locale`**: South Korea.
- **`punctuation_notes`**: short sentences; emoji OK; ㅋㅋ / ㅎㅎ OK.
- **`common_pitfalls`**:
  - 합쇼체 leaking into casual post.
  - Excessive formality kills engagement.
  - Excessive hashtags.
- **`exemplar`**: 6개월 기다린 툴이 드디어 신기능 출시했음✨
  근데 결국 2주만에 직접 만드는 게 더 빨랐음. DIY 최고.

## 5. `ko-kr-naver-blog`

- **Channel**: Naver blog (long-form).
- **`second_person`**: 여러분 / 독자.
- **`formality`**: medium-high.
- **`locale`**: South Korea.
- **`punctuation_notes`**: full-width punctuation; structured with
  H2 / H3; pull quotes.
- **`common_pitfalls`**:
  - 「결론적으로 말하면」 cliché opener.
  - Excessive hedge stacking.
  - Formal letter clichés leaking in.
- **`exemplar`**: 많은 팀이 같은 벽에 부딪힙니다: [문제]. 지난 1년
  동안 [N]개 팀과 일하면서, 해결한 팀과 해결하지 못한 팀을 가르는
  세 가지 패턴이 보입니다.

## 6. `ko-kr-kakao-casual`

- **Channel**: KakaoTalk messages.
- **`second_person`**: 너 / [name] + 님.
- **`formality`**: low.
- **`locale`**: South Korea.
- **`punctuation_notes`**: short messages; emoji OK; casual
  particles; ㅋㅋ OK.
- **`common_pitfalls`**:
  - Over-formality in chat (awkward).
  - Mixing polite / plain awkwardly.
- **`exemplar`**: 알겠어! 내일 14시에 보자 👍 늦지 마!

## 7. `ko-kr-business-document`

- **Channel**: formal business documents (proposals, contracts).
- **`second_person`**: 귀사 / 귀하.
- **`formality`**: very high (합쇼체).
- **`locale`**: South Korea.
- **`punctuation_notes`**: full-width; structured headings; data
  tables; numbered lists.
- **`common_pitfalls`**:
  - Dropping 합쇼체 mid-document.
  - Numbers without units.
  - Missing required disclosures.
- **`exemplar`**: 본 제안서에서는 [문제]에 대한 해결책으로 [제품명]의
  도입을 권장합니다. 도입 시 [효과]가 예상되며, 투자 회수 기간은
  [기간]으로 산출됩니다.

## 8. `ko-kr-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: 고객님 / [name] 님.
- **`formality`**: high (합쇼체 or polite 해요체).
- **`locale`**: South Korea.
- **`punctuation_notes`**: polite empathy first; specific action with
  timeline; apologetic register.
- **`common_pitfalls`**:
  - 「불편을 드려 죄송합니다」 cliché without specifics.
  - Defensive tone.
  - Missing apology for confirmed error.
- **`exemplar**:
```text
[고객명] 님,

불편을 드려 죄송합니다.
문의하신 [내용]에 대해 확인하여 보고드립니다.

[구체적인 대응 내용]

[구체적인 소요 시간] 이내에 처리해 드리겠습니다.
진척 사항이 있으면 다시 연락드리겠습니다.

기타 문의 사항이 있으시면 편하게 연락 주세요.

[담당자 이름]
[회사명]
[연락처]
```

## 9. `ko-kr-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: 당신.
- **`formality`**: medium.
- **`locale`**: South Korea.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text action + outcome.
- **`common_pitfalls`**:
  - 「혁신적인」 / 「업계 최초」 exaggeration.
  - Multiple CTAs.
  - Missing social proof (숫자 / 사례).
- **`exemplar`**: **헤드라인:** [기간] 안에 [성과]를. **서브헤드라인:**
  [한 줄 설명]. **CTA:** 무료 체험 시작하기 →

## 10. `ko-kr-finance-formal`

- **Channel**: financial reports, regulatory disclosures.
- **`second_person`**: not used (formal audience).
- **`formality`**: very high.
- **`locale`**: South Korea.
- **`punctuation_notes`**: precise figures; ₩ before amount;
  date format YYYY. M. D. or ISO.
- **`common_pitfalls`**:
  - Promising returns without 「과거 운용 실적은 미래 운용 성과를
    보장하는 것이 아닙니다」 disclaimer.
  - Rounding figures to mislead.
  - Missing required disclosures (자본시장법 / 금융소비자보호법).
- **`exemplar`**: 당 펀드의 운용 실적은 2024년 8.2%, 2025년 5.1%,
  2026년 9월 22일 기준으로 연초 대비 -1.3%입니다. 과거 운용 실적은
  미래 운용 성과를 보장하는 것이 아니며, [위험 허용도]의 투자자
  적합합니다.

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `ko-kr-friendly-professional` |
| content | Twitter / X | `ko-kr-twitter-casual` |
| content | Naver blog | `ko-kr-naver-blog` |
| content | KakaoTalk | `ko-kr-kakao-casual` |
| business | email (formal) | `ko-kr-email-formal` |
| business | email (casual) | `ko-kr-email-casual` |
| business | proposal / contract | `ko-kr-business-document` |
| business | sales / landing | `ko-kr-landing-page-clear` |
| research | report | `ko-kr-business-document` |
| business | financial | `ko-kr-finance-formal` |
| any | customer support | `ko-kr-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.