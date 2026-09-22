# Style Profiles — `vi-VN` (Vietnamese — Vietnam)

> Source-of-truth file for the `vi-VN` style profiles. Lives under
> `shared/locales/vi-VN/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for Vietnamese. Each
profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile uses:

- **Code**: identifier.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: punctuation conventions.
- **`common_pitfalls`**: patterns the layer avoids.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `vi-vn-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: Anh / Chị (peers); Quý vị (formal).
- **`formality`**: medium.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: full-width punctuation; diacritics
  mandatory; no space between Vietnamese words and punctuation.
- **`common_pitfalls`**:
  - 「chúng tôi xin thông báo」 excessive formality.
  - 「rất」「cực kỳ」「vô cùng」 excessive intensifiers.
  - Missing diacritics (looks unprofessional).
- **`exemplar`**: Chúng tôi phát triển phần mềm cho ngành [industry].
  Khách hàng thường thấy [outcome] trong vòng [timeframe].

## 2. `vi-vn-email-formal`

- **Channel**: business email (formal).
- **`second_person`**: Anh / Chị [Name] / Kính gửi.
- **`formality`**: very high.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: full-width punctuation; formal opener
  Kính gửi; closer Trân trọng.
- **`common_pitfalls`**:
  - Dropping to informal mid-email.
  - 「xin được phép」 / 「chúng tôi xin」 formal clichés.
  - 「kính thư」 letter cliché.
- **`exemplar**:
```text
Kính gửi Anh / Chị [Name],

Tôi là [Tên] đến từ [Công ty]. Chúng tôi hoạt động trong lĩnh vực
[industry] và đã phục vụ hơn [số] khách hàng trên toàn Việt Nam.

Anh / Chị có thể dành 15 phút trong vài tuần tới để chúng ta thảo luận
không?

Cảm ơn Anh / Chị đã quan tâm.

Trân trọng,

[Tên]
[Chức danh]
[Công ty]
[Liên hệ]
```

## 3. `vi-vn-email-casual`

- **Channel**: casual / internal email.
- **`second_person`**: Anh / Chị / Bạn.
- **`formality`**: medium.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: full-width punctuation; no formal opener;
  polite but not ceremonial.
- **`common_pitfalls`**:
  - Over-formality in internal communication.
  - Casual particles (nhé / nè) leaking in.
- **`exemplar`**: Chào [Name], bạn có thể xác nhận [topic] giúp mình
  không? Cảm ơn trước nhé.

## 4. `vi-vn-zalo-casual`

- **Channel**: Zalo messages (dominant in Vietnam).
- **`second_person`**: bạn / [name] + anh/chị/em.
- **`formality`**: low.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: short messages; emoji OK; casual
  particles.
- **`common_pitfalls`**:
  - Over-formality in chat.
  - Long paragraphs.
- **`exemplar`**: Ok! Mai 14h gặp nhé 👍 Đừng trễ!

## 5. `vi-vn-facebook-casual`

- **Channel**: Facebook posts / comments.
- **`second_person`**: bạn / mọi người.
- **`formality`**: low.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: short + emoji + occasional casual
  particles.
- **`common_pitfalls`**:
  - Over-formality kills engagement.
  - Excessive hashtags.
- **`exemplar`**: Cuối cùng thì tool này cũng ra tính năng mới! Cuối
  cùng mình tự làm trong 2 tuần vẫn nhanh hơn. DIY is the best. ✨

## 6. `vi-vn-linkedin-professional`

- **Channel**: LinkedIn posts / comments.
- **`second_person`**: Anh / Chị / Quý vị.
- **`formality`**: medium-high.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: em-dash for asides; line breaks between
  paragraphs.
- **`common_pitfalls`**:
  - "Thrilled to announce" English cliché.
  - Casual particles (nhé / nè) leaking in.
- **`exemplar`**: Rất vui khi chia sẻ rằng tôi đã gia nhập XYZ với
  vị trí Head of Marketing. Tôi mong được cùng xây dựng những điều
  tuyệt vời với đội ngũ.

## 7. `vi-vn-business-document`

- **Channel**: formal business documents (proposals, contracts).
- **`second_person`**: Anh / Chị / Quý Công ty.
- **`formality`**: very high.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: full-width; structured headings; data
  tables; numbered lists.
- **`common_pitfalls`**:
  - Missing required disclosures.
  - Numbers without units.
- **`exemplar`**: Đề xuất này khuyến nghị triển khai [product] như
  giải pháp cho [problem]. Triển khai dự kiến mang lại [outcome],
  với thời gian hoàn vốn [period].

## 8. `vi-vn-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: Anh / Chị / Quý khách.
- **`formality`**: high.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: empathy first, action second; specific
  timeline.
- **`common_pitfalls`**:
  - 「Chúng tôi rất tiếc về sự bất tiện」 cliché without specifics.
  - Defensive tone.
  - No specific next step.
- **`exemplar**:
```text
Xin chào Anh / Chị [Tên],

Chúng tôi rất tiếc về sự bất tiện mà Anh / Chị đã gặp.
Chúng tôi đã ghi nhận vấn đề của Anh / Chị về [vấn đề].

[Hành động cụ thể đã thực hiện]

[Hành động] sẽ được hoàn tất trong [thời gian] ngày làm việc.

Đừng ngần ngại liên hệ nếu có bất kỳ điều gì khác chúng tôi có thể
hỗ trợ.

Trân trọng,
[Tên nhân viên]
[Công ty]
[Liên hệ]
```

## 9. `vi-vn-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: Anh / Chị.
- **`formality`**: medium.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text action + outcome.
- **`common_pitfalls`**:
  - 「Cách mạng」 / 「đột phá」 exaggeration.
  - Multiple CTAs.
  - Missing social proof (số liệu / đánh giá).
- **`exemplar`**: **Tiêu đề:** [Outcome] cho [audience] trong
  [timeframe]. **Mô tả:** [One-line how]. **CTA:** Bắt đầu miễn phí →

## 10. `vi-vn-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: bạn / mọi người.
- **`formality`**: low.
- **`locale`**: Vietnam.
- **`punctuation_notes`**: short sentences; emoji OK; casual
  particles.
- **`common_pitfalls`**:
  - Over-long posts.
  - Engagement bait.
- **`exemplar`**: Đợi 6 tháng tool mới ra tính năng. Tự làm trong 2
  tuần xong. DIY quá.

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `vi-vn-friendly-professional` |
| content | Twitter / X | `vi-vn-twitter-casual` |
| content | Facebook | `vi-vn-facebook-casual` |
| content | Zalo | `vi-vn-zalo-casual` |
| business | email (formal) | `vi-vn-email-formal` |
| business | email (casual) | `vi-vn-email-casual` |
| business | LinkedIn | `vi-vn-linkedin-professional` |
| business | proposal / contract | `vi-vn-business-document` |
| business | sales / landing | `vi-vn-landing-page-clear` |
| any | customer support | `vi-vn-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.