# Style Profiles — `yue-Hant-HK` (Traditional Chinese — Hong Kong)

> Source-of-truth file for the `yue-Hant-HK` style profiles. Lives
> under `shared/locales/yue-Hant-HK/` per the architecture in
> [`../README.md`](../README.md).

11 style profiles cover the canonical channels for Hong Kong
Traditional Chinese. Each profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md):
id, locale, channel, formality, second_person_policy,
punctuation_notes, avoid, exemplar. Locale-specific extension fields
where useful.

## Schema

Each profile below uses this schema:

- **Code**: identifier used in workflow frontmatter and harness output.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: which audience this profile is for.
- **`punctuation_notes`**: spacing, marks, and conventions specific to
  this profile.
- **`common_pitfalls`**: patterns the layer avoids in this profile.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `yue-hk-chat-casual`

- **Code**: `yue-hk-chat-casual`.
- **Channel**: WhatsApp / Signal / Telegram messaging.
- **`second_person`**: 你 / 你哋 (direct).
- **`formality`**: low.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 全角中文 + 半角英數；中英之間留空格；emoji 適度。
- **`common_pitfalls`**:
  - 過度客套（避免「不好意思打擾您」這類正式用語）。
  - 程式化結尾（避免「如有問題請隨時告訴我」）。
  - 中英夾雜時空格不一致。
- **`exemplar`**: 我已經 send 咗個 file 俾你，記得 check 吓。有問題隨時講聲。

## 2. `yue-hk-facebook-casual`

- **Code**: `yue-hk-facebook-casual`.
- **Channel**: Facebook comment replies.
- **`second_person`**: 你 / 你哋.
- **`formality`**: low.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 短句；emoji 1-3 個；保留 HK Facebook 常見 emoji 風格。
- **`common_pitfalls`**:
  - 立場化措辭（容易引起 FB 戰文文化）。
  - 長段落（FB comment 受眾注意力低）。
- **`exemplar`**: 我用過！真心幾好用，唔似得之前嗰個會 lag 👌

## 3. `yue-hk-facebook-friendly`

- **Code**: `yue-hk-facebook-friendly`.
- **Channel**: Facebook post (long-form, public page).
- **`second_person`**: 你 / 各位 / 朋友.
- **`formality`**: medium.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 段落清晰；標點用「」與『』。
- **`common_pitfalls`**:
  - 過度行銷（FB 受眾對廣告警覺）。
  - 標題黨與內文不符。
- **`exemplar`**: 好消息！我哋嘅 [產品名] 終於返貨啦，今次仲加咗 [新功能]。即刻去下面 link 了解啦 👇

## 4. `yue-hk-instagram-casual`

- **Code**: `yue-hk-instagram-casual`.
- **Channel**: Instagram captions.
- **`second_person`**: 你.
- **`formality`**: low.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 短 + emoji + hashtags。
- **`common_pitfalls`**:
  - 太多 hashtags（IG 算法會降權）。
  - 完全無 emoji 會失去 IG 風格。
- **`exemplar`**: ☕️ 今日去咗 [店名]，latte 拉花真係好靚 📸 推薦畀鍾意 cafe 嘅朋友！

## 5. `yue-hk-lihkg-style`

- **Code**: `yue-hk-lihkg-style`.
- **Channel**: LIHKG forum (討論區).
- **`second_person`**: 你 / 巴打 / 絲打.
- **`formality`**: low to medium-low.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: LIHKG 風格 — 短句；顏文字；強烈個人聲音；適度粗俗詞可接受。
- **`common_pitfalls`**:
  - 過度正式（LIHKG 受眾會覺得造作）。
  - 政治敏感內容（HK 環境高度敏感）。
- **`exemplar`**: 我覺得今次 [事件] 真係 [個人觀點]，巴打點睇？

## 6. `yue-hk-linkedin-professional`

- **Code**: `yue-hk-linkedin-professional`.
- **Channel**: LinkedIn posts / comments.
- **`second_person`**: 您 / 你 / 各位.
- **`formality`**: high.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 中英夾雜常見；段落清晰；避免太口語。
- **`common_pitfalls`**:
  - 「我哋」過度口語（LinkedIn 偏正式）。
  - 過度 emoji。
  - 過度謙虛（「小弟不才」之類）。
- **`exemplar`**: 過去五年，我哋公司專注於 [行業]，服務超過 200 家中港客戶。今年希望能與更多業界朋友交流合作機會。

## 7. `yue-hk-email-professional`

- **Code**: `yue-hk-email-professional`.
- **Channel**: 商業 email.
- **`second_person`**: 您 (formal).
- **`formality`**: high.
- **`locale`**: Hong Kong.
- **`punctuation_notes`**: 頂格稱呼；段落清晰；簽名塊完整。
- **`common_pitfalls`**:
  - 「您好嗎?」開頭（Cantonese 寒暄但偏鬆，正式 email 用「您好」）。
  - 缺乏具體行動。
- **`exemplar`**:
  ```text
  王先生：

  您好。

  關於 [項目] 的下一步安排，建議本週三（10 月 7 日）下午 3 點在 [地點 / Zoom]
  開會討論。附件是初版方案，請過目。

  期待您的回覆。

  順頌商祺。

  Mary Chan
  [公司名稱]
  [電話]
  ```

## 8. `yue-hk-business-consulting`

- **Code**: `yue-hk-business-consulting`.
- **Channel**: 商業顧問報告、戰略文件、內部決策備忘。
- **`second_person`**: 內部 — 不用「您」/「你」。
- **`formality`**: high.
- **`locale`**: Hong Kong business.
- **`punctuation_notes`**: 全形中文標點；列點用「1.」「2.」；避免 Cantonese 口語。
- **`common_pitfalls`**:
  - 「我哋覺得⋯」「我哋建議⋯」主觀措辭。
  - 數據不標來源。
  - Cantonese 口語混入正式書面。
- **`exemplar`**: 根據 2025 年公開財報與第三方研究，目標市場在 2025 Q4 增長 12.5%，建議增加 15% 行銷預算以維持市佔率。

## 9. `yue-hk-legal-formal`

- **Code**: `yue-hk-legal-formal`.
- **Channel**: 法律 / 合規文件、合約條款、政策文件。
- **`second_person`**: 正式 — 不用口語或「您」以外的稱呼。
- **`formality`**: very high.
- **`locale`**: Hong Kong legal.
- **`punctuation_notes`**: 全形中文標點；引法例用「第 X 章」「條例編號」。
- **`common_pitfalls`**:
  - Cantonese 口語（食、搞掂、嘅、喺）。
  - 翻譯錯誤的法例章節。
  - 缺乏「根據」或「茲」開頭。
- **`exemplar`**: 根據香港法例第 [X] 章 [法規名稱] 第 [Y] 條的規定，訂約雙方同意遵守以下條款。

## 10. `yue-hk-customer-support`

- **Code**: `yue-hk-customer-support`.
- **Channel**: 客戶支援、售後、退換貨。
- **`second_person`**: 您 (formal).
- **`formality`**: medium.
- **`locale`**: Hong Kong customer-facing.
- **`punctuation_notes`**: 共情段（一句）；解釋段（一到兩句）；行動段（明確步驟）。
- **`common_pitfalls`**:
  - 程式化開頭（「非常感謝您的來信」）。
  - 推卸責任。
  - 缺乏具體動作。
- **`exemplar`**:
  ```text
  您好，

  抱歉造成不便。關於您提出的 [問題]，我們已經記錄並將個案升級處理。
  請您方便時提供訂單編號，我們會在 24 小時內回覆。

  請問還有其他可以協助的嗎？
  ```

## 11. `yue-hk-long-form-article`

- **Code**: `yue-hk-long-form-article`.
- **Channel**: 長文 / 文章 / 雜誌文章。
- **`second_person`**: 你 / 讀者.
- **`formality`**: medium-high.
- **`locale`**: Hong Kong readers.
- **`punctuation_notes`**: 全形中文標點；段落清晰；小標題用「一、」「二、」。
- **`common_pitfalls`**:
  - 流行語堆疊（「內卷」「躺平」當主論述基礎）。
  - 學術化但無原創洞察。
  - 標題黨 + 內文空洞。
- **`exemplar`**: 過去五年，香港的共享辦公空間從 [年份] 年的 [數字] 個激增到 [年份] 年的 [數字] 個，背後反映了創業文化的結構性轉變⋯⋯

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | WhatsApp / Telegram | `yue-hk-chat-casual` |
| content | Facebook comment | `yue-hk-facebook-casual` |
| content | Facebook post | `yue-hk-facebook-friendly` |
| content | Instagram | `yue-hk-instagram-casual` |
| content | LIHKG forum | `yue-hk-lihkg-style` |
| content | 長文 / 雜誌 | `yue-hk-long-form-article` |
| business | email | `yue-hk-email-professional` |
| business | LinkedIn | `yue-hk-linkedin-professional` |
| business | 顧問 / 報告 | `yue-hk-business-consulting` |
| business | sales / landing | `yue-hk-linkedin-professional` |
| business | legal / compliance | `yue-hk-legal-formal` |
| research | research report | `yue-hk-business-consulting` |
| workflow | SOP / docs | `yue-hk-business-consulting` |
| technical | technical writing | `yue-hk-business-consulting` |
| any | customer support | `yue-hk-customer-support` |

User's explicit channel hint always overrides the default. Workflows
may also declare a `localization.default_style_profile` in their
frontmatter.