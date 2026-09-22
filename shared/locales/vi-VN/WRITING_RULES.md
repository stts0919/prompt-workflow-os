# Writing Rules — `vi-VN` (Vietnamese — Vietnam)

> Source-of-truth file for the `vi-VN` writing rules. Lives under
> `shared/locales/vi-VN/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in
Vietnamese for Vietnam readers. Covers diacritics, pronouns,
loanwords, and channel-specific tone.

Does not cover:

- Other regional Vietnamese variants (Northern / Central / Southern
  accent differences in speech; we use the standard written form).
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `vi-VN` layer when **all** hold:

1. User requested output in Vietnamese, **or** explicitly named
   Vietnam as target market, **or** the input contains Vietnamese
   text.
2. Selected workflow's `localization.supported_locales` includes
   `vi-VN`, or category default applies.

When the user explicitly says "thân mật" (informal) or "trang
trọng" (formal), respect the explicit register.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Vietnamese | Vietnamese | Vietnam | Load `vi-VN`. |
| English | Vietnamese | Vietnam | Load `vi-VN`. |
| Vietnamese | English | any | Skip vi-VN; use en-US / en-GB. |

## D. Protected content

Same as other locale layers.

## E. Vietnamese language guidance

### E.1 Diacritics

Full diacritics are standard for all professional / formal writing:

- `Việt Nam` (with diacritics), not `Viet Nam`.
- `tiếng Việt` (with diacritics), not `tieng Viet`.
- Diacritics matter for meaning: `ch` vs `tr` vs `gi` / `r` / `d` can
  change meaning. Verify each word's diacritics.

Omitting diacritics is acceptable only in:

- SMS / informal chat (rare; most Vietnamese typing apps support
  diacritics).
- Brand names that established themselves without diacritics
  (e.g. "Vinamilk", "Viettel" — established forms).
- Code identifiers / URLs.

### E.2 Pronouns

Vietnamese has a rich family-based pronoun system that signals
relationship and respect:

- Anh: older brother / male peer.
- Chị: older sister / female peer.
- Em: younger sibling / younger peer.
- Ông: grandfather / elderly male.
- Bà: grandmother / elderly female.
- Cô: aunt (father's sister) / female teacher.
- Bác: uncle / aunt (parents' older sibling) / elder peer.
- Chú: uncle (father's younger brother).
- Anh / chị: common business address for peers.

Default to formal address in business contexts:

- "Anh / chị [Name]" for peers.
- "Bác / cô [Name]" for elders.
- "Ông / bà [Name]" for much older or executive.

Avoid `tôi` (I, formal but cold) in casual contexts; use `mình`
(we / me, casual inclusive) or `tôi` (formal exclusive).

### E.3 Punctuation

- Full-width punctuation: `,` `.` `?` `!` `;` `:`.
- Quotes: `" "` for direct speech; `'` for nested.
- Sentence-ending period mandatory.
- No space between Vietnamese words and punctuation (e.g. 「Xin
  chào.」 not 「Xin chào .」).
- Space between Vietnamese and English (e.g. 「GitHub repository」).

### E.4 Numbers, dates, currency

- Currency: `₫` (đồng) before number with space (e.g. `100.000 ₫`).
  Use `VND` in international contexts.
- Date: `22/09/2026` (DD/MM/YYYY, common); `22 tháng 9 năm 2026` (long
  form); `2026-09-22` (ISO, technical).
- Time: `14:30` (24-hour); `2:30 chiều` (12-hour + sáng / trưa /
  chiều / tối).
- Numbers: `.` thousand separator (Vietnamese uses period, like
  German / Indonesian); `,` decimal separator.
- Phone: `+84 24 1234 5678` (Hanoi landline); `+84 91 234 5678`
  (mobile).

### E.5 Loanwords

Common English tech terms in Vietnamese:

- software (English preserved)
- hardware (English preserved)
- máy tính (computer)
- internet (English preserved)
- email / thư điện tử (both common; thư điện tử official)
- trang web (website)
- ứng dụng (application) / app (English preserved)
- tải xuống / download (both common)
- tải lên / upload (similar)
- tệp / file (both common)
- dữ liệu / data (both common)
- máy chủ (server)
- khách hàng (client)
- AI (English preserved)
- họp / meeting (both common)

Default to English when both are acceptable.

### E.6 Honorifics and titles

- Ông / bà + name: for elders, executives.
- Anh / chị + name: for peers.
- Bác / cô / chú + name: for various family-derived elder addresses.
- Job titles: Giám đốc (Director), Trưởng phòng (Department Head),
  Quản lý (Manager).

### E.7 Casual register

Common particles:

- "nhé": soft assertion / request. 「Nhớ nhé」「Đi nhé」
- "nha": same as "nhé" (southern dialect more common).
- "đó": tag / emphasis. 「Vậy đó」
- "thôi": limit / "that's all". 「Chỉ vậy thôi」
- "rồi": completed / "already". 「Xong rồi」
- "nè": pointing / "here". 「Đây nè」
- "á / vậy á": surprise. 「Vậy á?」

Avoid these in business / formal writing.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| Email (business) | `vi-vn-email-formal` | Formal, kính gửi / trân trọng |
| Email (casual) | `vi-vn-email-casual` | Friendly, less formal |
| Zalo | `vi-vn-zalo-casual` | Short messages, casual |
| Facebook | `vi-vn-facebook-casual` | Mixed, casual |
| LinkedIn (VN) | `vi-vn-linkedin-professional` | Achievement-focused |
| Twitter / X | `vi-vn-twitter-casual` | Short, casual |
| Business document | `vi-vn-business-document` | Very formal, structured |
| Customer support | `vi-vn-customer-support` | Empathetic, specific action |
| Sales / landing | `vi-vn-landing-page-clear` | Headline, CTA |
| General professional | `vi-vn-friendly-professional` | Polite default fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locales, plus:

- Avoid 「chúng tôi xin thông báo」 / 「xin được phép」 excessive
  formality.
- 「rất」「cực kỳ」「vô cùng」 excessive intensifiers.
- 「trên đây」「dưới đây」 letter cliché pointing.
- 「kính thư」 formal letter cliché in modern email.

## H. Editing intensity rules

Same as other locales.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** Công ty chúng tôi làm phần mềm.

**After:** Chúng tôi phát triển phần mềm cho ngành [industry].

### I.2 Intensity: standard, channel: email-formal

**Before:** Hãy dùng sản phẩm của chúng tôi.

**After:**
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

### I.3 Intensity: light, channel: translation

**Before (English):** "Welcome to our service. Please feel free to
contact us if you have any questions."

**After:** Chào mừng Anh / Chị đến với dịch vụ của chúng tôi. Đừng
ngần ngại liên hệ nếu có bất kỳ câu hỏi nào.

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** Hầu hết người dùng thích sản phẩm này.

**After:** Theo khảo sát người dùng năm 2025 (n=1.247, độ tin cậy 95%),
78% người được hỏi cho biết họ ưa thích [sản phẩm] hơn [sản phẩm đối
thủ]. Kết quả áp dụng cho tiểu mẫu [nhân khẩu học].

### I.5 Intensity: standard, channel: customer-support

**Before:** Xin lỗi về sự bất tiện. Chúng tôi sẽ xử lý sớm.

**After:**
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

## K. Safety boundaries

Same as other locale layers.

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — Loanword handling, business
  terms, platform terms.
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles.
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — Quality gate.
- [`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md) —
  core schema.
- [`../zh-TW/README.md`](../zh-TW/README.md) — reference
  structure.

## M. Citations

Editorial principles borrowed from Vietnamese style guides (Quy tắc
đặt câu tiếng Việt, Ngữ pháp tiếng Việt, Hội đồng Quốc gia về
Chính tả). Specific citations TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.