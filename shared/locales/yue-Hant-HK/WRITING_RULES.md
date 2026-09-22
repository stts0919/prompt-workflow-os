# Writing Rules — `yue-Hant-HK` (Traditional Chinese — Hong Kong)

> Source-of-truth file for the `yue-Hant-HK` writing rules. Lives under
> `shared/locales/yue-Hant-HK/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in
Traditional Chinese for Hong Kong readers. Covers HK terminology,
Cantonese vocabulary handling, bilingual mixing, and channel-specific
tone.

It does not cover:

- Claims about bypassing AI detection or removing watermarks (see
  section K).
- Taiwan-specific phrasing or political references (use `zh-TW`).
- Mainland-specific political or regulatory phrasing (use `zh-CN`).

## B. Automatic activation rules

The router activates the `yue-Hant-HK` layer when **all** hold:

1. User requested output in Traditional Chinese, **or** explicitly named
   Hong Kong / a HK district as target market.
2. User did not explicitly request Simplified Chinese (Mainland) or
   Taiwan-specific phrasing.
3. Selected workflow's `localization.supported_locales` includes
   `yue-Hant-HK`, or category default applies.

If the user explicitly says 「繁體中文」 without further qualification,
default to `zh-TW` (more channels covered). Use `yue-Hant-HK` only when
Hong Kong is explicitly named or implied (Cantonese vocabulary, HK
place names, HK-specific platform).

## C. Input language vs output language vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Cantonese-leaning TC | TC | HK | Load `yue-Hant-HK`; allow Cantonese vocab. |
| Standard TC | TC | HK | Load `yue-Hant-HK`; default to Standard Written Chinese. |
| Standard TC | TC | Taiwan | Load `zh-TW` (not yue-Hant-HK). |
| English | TC | HK | Load `yue-Hant-HK` for clarification, output language TC. |
| Any | EN | HK | Skip yue-Hant-HK layer; use en-US or en-GB based on user signal. |

## D. Protected content

Same rules as `zh-TW` and `zh-CN`:

- Code, identifiers, URLs, brand names.
- Direct quotations, regulatory disclosures.
- Numbers, units, currency, dates.
- Required technical or legal wording supplied by user.
- Bilingual mix: when source mixes Chinese and English, preserve the
  mix verbatim on protected spans.

## E. Hong Kong language guidance

### E.1 Characters

- Output is **Traditional Chinese** (繁體字). Same character set as
  `zh-TW`. User explicitly requesting 簡體 routes to `zh-CN` instead.
- HK uses 「的」 vs 「嘅」 interchangeably. Default to 「的」 for formal
  writing; 「嘅」 only in dialogue / casual.
- 香港 / 港 / Hong Kong: never rewrite the city name (港 vs 香港 is
  stylistic, both acceptable).

### E.2 HK vs Taiwan vs Mainland terminology

See [TERM_GLOSSARY.md](TERM_GLOSSARY.md) for the 60+ entry table. The
most common differences:

| Avoid (Taiwan / Mainland) | Default (HK) | 備註 |
| --- | --- | --- |
| 軟體 (Taiwan) / 软件 (Mainland) | 軟件 | HK IT convention |
| 程式 (Taiwan) / 程序 (Mainland) | 程式 | HK convention (same as Taiwan) |
| 寬頻 | 寬頻 | HK specific term |
| 影片 (TW) / 视频 (CN) | 影片 | HK matches TW |
| 網際網路 (Taiwan formal) | 互聯網 | HK convention |
| 介面 (Taiwan) / 界面 (Mainland) | 介面 | HK matches Taiwan |
| 滑鼠 (Taiwan) / 鼠标 (Mainland) | 滑鼠 | HK matches Taiwan |
| 質素 | 質素 | HK common; Taiwan uses 品質 |
| 巴士 | 巴士 | HK common |
| 巴士站 | 巴士站 | HK; Taiwan uses 公車站 |
| 捷運 (Taiwan) | 地鐵 | HK convention |
| 電郵 | 電郵 | HK convention |
| 互聯網 | 互聯網 | HK; Taiwan uses 網路 / 網際網路 |

When the user industry or brand has registered a specific form, use
that form (per context ledger).

### E.3 Cantonese vocabulary (口語)

Cantonese vocabulary is acceptable in casual channels (WhatsApp,
Facebook comments, LIHKG), rare in formal documents.

Common Cantonese cues:
- 嘅 (possessive particle) instead of 的 in casual writing.
- 喺 (location) instead of 在 in casual writing.
- 食 (eat) instead of 吃 in casual writing.
- 飲 (drink) — common in HK casual.
- 唔 (not) instead of 不 in casual writing.
- 睇 (look/watch) instead of 看 in casual writing.
- 攞 (take) instead of 拿 in casual writing.
- 點解 (why) instead of 為什麼 in casual writing.
- 邊度 (where) instead of 哪裡 in casual writing.
- 搞掂 (done / settled) — common HK colloquial.
- 食字 (use a word as a pun) — common in HK internet culture.
- 唔該 (please / thanks) — HK courtesy term, very common.
- 老闆 / 闆娘 — common HK workplace address.
- 食字 / 食字 — HK internet slang.
- 老細 (boss) — HK Cantonese.

Use these ONLY when the channel hint or the user's input signals casual
register. In formal documents (legal, financial, regulatory), do not use.

### E.4 Bilingual mixing

HK writing commonly mixes Chinese and English in the same sentence:

- 「記得 check 吓個 file」
- 「send 個 email 俾我」
- 「下晝三點開個 meeting」

When the user's input mixes, preserve the mix. When generating from
scratch, use the mix only if the channel hints casual (Facebook
comments, WhatsApp, LIHKG). For formal channels (LinkedIn, email),
prefer monolingual.

### E.5 Punctuation

- Default to full-width TC punctuation: 「」『』、。，；：？！。
- HK formal often uses English double quotes " " for emphasis; this is
  acceptable in bilingual contexts.
- Use 「」 for direct speech in formal writing; " " for inline emphasis
  in casual / English-mixed.

### E.6 Numbers, dates, currency

- Currency: HKD (港幣), USD (美元), CNY (人民幣) — keep user's choice;
  default to HKD when target is HK and user does not specify.
- Date: 香港常用 DD/MM/YYYY (e.g. 22/09/2026) for local; YYYY-MM-DD
  (ISO) acceptable in technical documents.
- Time: 24-hour (e.g. 14:30) common; 12-hour (e.g. 2:30pm) in casual.
- Numbers: comma thousand separator (1,000); no space (English uses
  space).

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| WhatsApp / Signal / Telegram | `yue-hk-chat-casual` | 短訊，Cantonese 口語可，emoji 適度 |
| Facebook comment | `yue-hk-facebook-casual` | 短回覆，Cantonese + 英文混合 |
| Facebook post (long) | `yue-hk-facebook-friendly` | 150-300 字，友善，Cantonese 輕量 |
| Instagram caption | `yue-hk-instagram-casual` | 短 + emoji + hashtags |
| LIHKG forum | `yue-hk-lihkg-style` | 論壇文化，強烈個人聲音，Cantonese + slang |
| LinkedIn (HK style) | `yue-hk-linkedin-professional` | 英文夾雜，較正式 |
| 商業 email | `yue-hk-email-professional` | 正式，可中英夾雜 |
| 商業提案 / 報告 | `yue-hk-business-consulting` | 正式書面，避免 Cantonese |
| 法律 / 合規文件 | `yue-hk-legal-formal` | 嚴謹，避免任何口語 |
| 客服回覆 | `yue-hk-customer-support` | 共情，具體動作 |
| 長文 / 文章 | `yue-hk-long-form-article` | 正式書面 |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for the full schema and
exemplars.

## G. AI-pattern reduction

Same rules as `zh-TW` and `zh-CN`:

- 三段式排比 (avoid three consecutive similar structures).
- 空泛總結 (避免「總而言之」「值得注意的是」).
- 過度客套 (避免「希望對您有所幫助」).
- 過度連接詞 (避免「首先 / 其次 / 再次 / 最後」連用).
- 萬能動詞 (避免「進行」「展開」「推動」泛用).

## H. Editing intensity rules

Same as `zh-TW` and `zh-CN`:

- `none` — protect everything (code, IDs, URLs, brand names).
- `light` — minimal cleanup of obvious typos.
- `standard` — apply glossary substitutions + AI-pattern reduction.
- `strict_precision` — high precision, label uncertainty, no rhetorical
  softening. Mandatory for legal / medical / financial / security /
  compliance / regulated disclosures.

The router auto-escalates to `strict_precision` for regulated content.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: facebook-casual

**Before:** 多謝你嘅支持, 我哋會繼續努力。

**After:** 多謝你嘅支持 💛 我哋會繼續努力，下個月仲有新嘢推出，敬請期待！

(注：保留 Cantonese「我哋」「嘅」；加 emoji + 期待語氣。)

### I.2 Intensity: standard, channel: linkedin-professional

**Before:** 我哋公司做軟件好叻。

**After:** 我哋公司專注於企業軟件開發，過去三年服務超過 200 家中港客戶。如有合作機會，歡迎 DM 詳談。

(注：LinkedIn 接受中英夾雜；保留 Cantonese「我哋」但避免太口語。)

### I.3 Intensity: light, channel: translation (HK English → TC)

**Before (English):** "Thanks for your support, we'll keep improving."

**After:** 多謝支持，我哋會繼續努力。

(注：保留「我哋」(HK)，不強行改成「我們」。)

### I.4 Intensity: strict_precision, channel: legal-formal

**Before:** 我哋公司通常會 comply 啲 regulations。

**After:** 本公司根據香港法例第 [X] 章 [法規名稱] 的規定處理客戶資料。如需查閱完整合規說明，請聯絡 compliance@company.com。

(注：strict_precision 完全禁止 Cantonese 口語；改為正式書面 + 引法例章節。)

### I.5 Intensity: standard, channel: email-professional

**Before:** 你好, 我係 Mary, 想約時間傾下個 project。

**After:**
```text
王先生：

您好。

我是 Mary [職銜]，[公司名稱]。關於 [項目] 的下一步安排，建議本週三（10 月 7 日）
下午 3 點在 [地點 / Zoom] 開會討論。如時間合適，請回覆確認。

順祝商祺。

Mary
[公司名稱]
[聯絡電話]
```

(注：HK 商業 email 接受 Cantonese「係」，但正式開頭用「您好」而非粵語「你好嗎」。)

## K. Safety boundaries

Same as `zh-TW` and `zh-CN`:

- 不宣稱能繞過 AI 檢測、刪除浮水印、或證明人類撰寫。
- 不在使用者未要求時主動把數字、單位、貨幣轉換。
- 不取代 `zh-TW`；香港讀者用 `yue-Hant-HK`，但若用戶寫的是繁體中文且目標市場不明，預設 `zh-TW`。
- 政治、監管、合規話題使用中性、實質性表述。

## L. Reference files

- [TERM_GLOSSARY.md](TERM_GLOSSARY.md) — HK / 台灣 / 大陸 術語對照 + Cantonese 口語詞。
- [STYLE_PROFILES.md](STYLE_PROFILES.md) — Style profiles for HK channels。
- [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) — 雙層品質檢查。
- [`../zh-TW/README.md`](../zh-TW/README.md) — `zh-TW` reference implementation。
- [`../zh-CN/README.md`](../zh-CN/README.md) — `zh-CN` 平行版本。
- [`../FUTURE_LOCALE_EXPANSION_PLAN.md`](../FUTURE_LOCALE_EXPANSION_PLAN.md) section 2 — 原始計劃。

## M. Citations

Editorial principles borrowed from:

- `zh-TW` reference implementation (shared/locales/zh-TW/).
- `zh-CN` reference implementation (shared/locales/zh-CN/).
- HK-specific linguistic research from public-domain Cantonese grammar
  references. Specific citations TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal capability.