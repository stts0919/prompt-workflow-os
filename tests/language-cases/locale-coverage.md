# Locale Coverage Test Cases

Lightweight coverage of all 8 v1.2 locales. Each case verifies:

- The router activates the right locale pack.
- The output language matches the requested locale.
- The relevant style profile is selected.
- The protected content (workflow IDs) is preserved.

Full localization test suites live in
`tests/language-cases/zh-tw-localization-cases.md` (35 cases) and
`tests/language-cases/zh-cn-localization-cases.md` (35 cases). The
cases below are router-level smoke tests, not full localization
audits.

---

## 1. yue-Hant-HK — Hong Kong Traditional Chinese

- **User request:** 幫我用廣東話口吻寫一個 WhatsApp 短訊，通知客戶他的訂單已寄出。
- **Requested output language:** zh-HK (Traditional Chinese, HK
  colloquial acceptable).
- **Target market:** Hong Kong.
- **Expected locale:** yue-Hant-HK.
- **Expected style profile:** `yue-hk-chat-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate yue-Hant-HK layer; allow
  Cantonese vocab (寄出 → 已寄出 / 已 send 咗); preserve workflow IDs.
- **Protected content:** order number, customer name.
- **Failure conditions:**
  - Reply in zh-TW form (e.g. 「您的訂單」) — HK prefers 「您嘅訂單」
    in formal, but Cantonese 「你嗰張 order」is acceptable in chat.
  - Reply in zh-CN (Simplified characters).

## 2. yue-Hant-HK — LIHKG forum-style

- **User request:** 用 LIHKG 風格寫一段關於新餐廳的評價，約 100 字。
- **Requested output language:** zh-HK.
- **Target market:** Hong Kong.
- **Expected locale:** yue-Hant-HK.
- **Expected style profile:** `yue-hk-lihkg-style`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate yue-Hant-HK; allow Cantonese
  forum slang (巴打 / 絲打 / 食字); preserve restaurant name.
- **Protected content:** restaurant name, address.
- **Failure conditions:**
  - Overly formal writing (LIHKG 受眾會覺得造作).
  - Mix with zh-TW / zh-CN forms inappropriately.

## 3. yue-Hant-HK — formal letter

- **User request:** 幫我寫一封正式信給客戶，解釋服務條款的修改。
- **Requested output language:** zh-HK.
- **Target market:** Hong Kong.
- **Expected locale:** yue-Hant-HK.
- **Expected style profile:** `yue-hk-email-professional`.
- **Expected editing intensity:** strict_precision (legal context).
- **Expected router behavior:** Activate yue-Hant-HK; reject Cantonese
  口語 (食、搞掂); use Standard Written Chinese for legal register.
- **Protected content:** company name, legal references, dates.
- **Failure conditions:**
  - Cantonese 口語 leaking into formal letter.
  - Mix with zh-TW / zh-CN forms.

## 4. en-US — LinkedIn post

- **User request:** Help me write a LinkedIn post announcing I just
  joined a new company as Head of Marketing.
- **Requested output language:** en-US.
- **Target market:** United States.
- **Expected locale:** en-US.
- **Expected style profile:** `en-us-linkedin-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate en-US; US spelling
  (`organization`, not `organisation`); polite US LinkedIn register.
- **Protected content:** company name, role title.
- **Failure conditions:**
  - UK spelling leakage (organisation, behaviour, colour).
  - "Thrilled to announce" US-cliché overuse.

## 5. en-US — Twitter / X casual

- **User request:** Write a short Twitter post about a new feature
  shipped today.
- **Requested output language:** en-US.
- **Target market:** United States.
- **Expected locale:** en-US.
- **Expected style profile:** `en-us-twitter-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate en-US; under X character
  limit; emoji OK sparingly.
- **Protected content:** feature name, link.
- **Failure conditions:**
  - Reply in UK spelling.
  - Over-long posts.

## 6. en-GB — formal letter

- **User request:** Draft a formal letter to a UK supplier about a
  contract amendment.
- **Requested output language:** en-GB.
- **Target market:** United Kingdom.
- **Expected locale:** en-GB.
- **Expected style profile:** `en-gb-formal-letter`.
- **Expected editing intensity:** strict_precision.
- **Expected router behavior:** Activate en-GB; UK spellings
  (`organisation`, `behaviour`); "Yours sincerely," for named
  recipient; polite hedging.
- **Protected content:** supplier name, contract reference.
- **Failure conditions:**
  - US spelling leakage.
  - "Yours faithfully" with named recipient (should be "sincerely").

## 7. en-GB — LinkedIn (UK style)

- **User request:** LinkedIn post about my new role at a UK fintech.
- **Requested output language:** en-GB.
- **Target market:** United Kingdom.
- **Expected locale:** en-GB.
- **Expected style profile:** `en-gb-linkedin-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate en-GB; UK spellings; "Delighted
  to share" preferred over "Thrilled to".
- **Protected content:** company name.
- **Failure conditions:**
  - US spelling leakage.

## 8. ja-JP — formal email (keigo)

- **User request:** 日本の取引先に、製品リリースのご案内メールを書いて
  ください。
- **Requested output language:** ja-JP.
- **Target market:** Japan.
- **Expected locale:** ja-JP.
- **Expected style profile:** `ja-jp-email-formal`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate ja-JP; very high keigo
  (拝啓 / 敬具); polite opener / closer.
- **Protected content:** product name, company name, dates.
- **Failure conditions:**
  - Casual register leaking in (ね / よ particles).
  - です / ます mixed with だ / である.
  - Missing 敬具 closer after 拝啓 opener.

## 9. ja-JP — Twitter / X casual

- **User request:** Twitter に投稿する短い開発日誌を書いて。
- **Requested output language:** ja-JP.
- **Target market:** Japan.
- **Expected locale:** ja-JP.
- **Expected style profile:** `ja-jp-twitter-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate ja-JP; casual register with
  sentence-ending particles (ね / よ); contractions OK.
- **Protected content:** tool name.
- **Failure conditions:**
  - 敬語 leaking into casual post.
  - Over-formality kills engagement.

## 10. ko-KR — formal business email

- **User request:** 한국 거래처에 신제품 출시 안내 이메일을 작성해 주세요.
- **Requested output language:** ko-KR.
- **Target market:** South Korea.
- **Expected locale:** ko-KR.
- **Expected style profile:** `ko-kr-email-formal`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate ko-KR; 합쇼체 throughout; polite
  opener; signature block.
- **Protected content:** company name, product name.
- **Failure conditions:**
  - 반말체 leaking into formal email.
  - Mixed 합쇼체 / 해요체.

## 11. ko-KR — Naver blog

- **User request:** 네이버 블로그에 올릴 IT 주제 글 1500자 써 주세요.
- **Requested output language:** ko-KR.
- **Target market:** South Korea.
- **Expected locale:** ko-KR.
- **Expected style profile:** `ko-kr-naver-blog`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate ko-KR; long-form with H2 / H3
  structure; pull quotes.
- **Protected content:** brand names, citations.
- **Failure conditions:**
  - 합쇼체 leaking into casual blog.
  - Generic intro without hook.

## 12. id-ID — WhatsApp casual

- **User request:** Tolong tulis pesan WhatsApp singkat untuk konfirmasi
  janji temu besok.
- **Requested output language:** id-ID.
- **Target market:** Indonesia.
- **Expected locale:** id-ID.
- **Expected style profile:** `id-id-whatsapp-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate id-ID; informal register
  (`kamu` acceptable in chat); emoji OK.
- **Protected content:** appointment time, location.
- **Failure conditions:**
  - Over-formal `Anda` (you, formal) when casual context.
  - Reply in English.

## 13. id-ID — LinkedIn (ID style)

- **User request:** Tulisan LinkedIn tentang pencapaian profesional
  terbaru saya.
- **Requested output language:** id-ID.
- **Target market:** Indonesia.
- **Expected locale:** id-ID.
- **Expected style profile:** `id-id-linkedin-professional`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate id-ID; formal register
  (`Anda`); achievement-focused.
- **Protected content:** company name, role.
- **Failure conditions:**
  - Casual `kamu` / `aku` leaking into professional post.
  - English slang overuse.

## 14. vi-VN — Zalo casual

- **User request:** Viết tin nhắn Zalo ngắn cho đồng nghiệp về lịch họp
  team tuần sau.
- **Requested output language:** vi-VN.
- **Target market:** Vietnam.
- **Expected locale:** vi-VN.
- **Expected style profile:** `vi-vn-zalo-casual`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate vi-VN; casual register;
  particles (nhé / nha) OK; diacritics mandatory.
- **Protected content:** meeting time, location.
- **Failure conditions:**
  - Missing diacritics (unprofessional).
  - Over-formality in chat.

## 15. vi-VN — formal email

- **User request:** Soạn email chính thức gửi khách hàng về hợp đồng mới.
- **Requested output language:** vi-VN.
- **Target market:** Vietnam.
- **Expected locale:** vi-VN.
- **Expected style profile:** `vi-vn-email-formal`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate vi-VN; formal opener (Kính
  gửi); closer (Trân trọng); full diacritics; Anh / Chị address.
- **Protected content:** contract reference, client name.
- **Failure conditions:**
  - Missing diacritics.
  - Casual pronouns (bạn / mình) leaking in.

## 16. Cross-locale — user input contains Traditional Chinese

- **User request:** 幫我寫一份 README.md for my GitHub project
  (input is in Traditional Chinese).
- **Requested output language:** not specified by user (input suggests
  zh-TW or zh-HK).
- **Target market:** unspecified.
- **Expected locale:** default to zh-TW when ambiguous (most
  channels covered).
- **Expected style profile:** `zh-tw-friendly-professional` (or
  cross-compatible `zh-cn-friendly-professional` if workflow declares
  it).
- **Expected editing intensity:** standard.
- **Expected router behavior:** Default to zh-TW; ask if ambiguous.
  Preserve GitHub project name verbatim.
- **Protected content:** GitHub URL, project name.
- **Failure conditions:**
  - Output in Simplified Chinese (zh-CN) when input is Traditional.

## 17. Cross-locale — user requests English without locale

- **User request:** Write a press release about our Series A funding.
- **Requested output language:** English (no locale specified).
- **Target market:** unspecified.
- **Expected locale:** en-US (default for unspecified English).
- **Expected style profile:** `en-us-friendly-professional` or
  `en-us-business-consulting`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Default to en-US; do not assume UK
  unless spelling / region signal present.
- **Protected content:** company name, funding amount, date.
- **Failure conditions:**
  - Switching to UK spelling (en-GB) without user signal.
  - Adding date format DD/MM/YYYY (UK convention) when en-US default.

## 18. Cross-locale — Cantonese vocabulary in input

- **User request:** 我想用廣東話口吻寫一篇關於 [topic] 的文。（Cantonese
  markers in input: 「嘅」「喺」「食字」.）
- **Requested output language:** Traditional Chinese.
- **Target market:** Hong Kong (implied by Cantonese).
- **Expected locale:** yue-Hant-HK.
- **Expected style profile:** `yue-hk-facebook-friendly` or
  `yue-hk-long-form-article`.
- **Expected editing intensity:** standard.
- **Expected router behavior:** Activate yue-Hant-HK when Cantonese
  vocabulary detected in input; allow Cantonese 口語 in casual
  registers; preserve technical terms.
- **Protected content:** topic, brand names.
- **Failure conditions:**
  - Stripping Cantonese vocab (loses user signal).
  - Defaulting to zh-TW (loses Cantonese context).