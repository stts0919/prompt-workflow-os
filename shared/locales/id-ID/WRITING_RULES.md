# Writing Rules — `id-ID` (Indonesian — Indonesia)

> Source-of-truth file for the `id-ID` writing rules. Lives under
> `shared/locales/id-ID/` per the architecture in
> [`../README.md`](../README.md).

## A. Purpose and scope

Defines how `prompt-workflow-os` produces user-facing content in
Indonesian for Indonesia readers. Covers PUEBI spelling, formal /
informal register, loanword handling, and channel-specific tone.

Does not cover:

- Malay (Bahasa Melayu) / Malaysian Indonesian variants.
- Bypassing AI detection or removing watermarks (see section K).

## B. Automatic activation rules

The router activates the `id-ID` layer when **all** hold:

1. User requested output in Indonesian, **or** explicitly named
   Indonesia as target market, **or** the input contains Indonesian
   text.
2. Selected workflow's `localization.supported_locales` includes
   `id-ID`, or category default applies.

When the user explicitly says "bahasa formal" (formal) or "bahasa
santai" (casual), respect the explicit register.

## C. Input vs output vs target market

| Input | Output | Target | Action |
| --- | --- | --- | --- |
| Indonesian | Indonesian | Indonesia | Load `id-ID`. |
| English | Indonesian | Indonesia | Load `id-ID`. |
| Indonesian | English | any | Skip id-ID; use en-US / en-GB. |

## D. Protected content

Same as other locale layers.

## E. Indonesian language guidance

### E.1 PUEBI spelling

PUEBI (Pedoman Umum Ejaan Bahasa Indonesia) was published by the
Indonesian Ministry of Education in 2015 and is the current official
spelling standard. Key points:

- Use `bahasa` (not `bahasa` only — it's one word).
- "Indonesia" (not "Nusantara" in formal contexts).
- Loanwords: use established loanword forms when available; preserve
  English for brand names.
- Affixes: `me-`, `ber-`, `pe-`, `per-`, `ke-`, `se-` — written as part
  of the word (no hyphen in PUEBI; pre-2015 EYD used hyphens).
- Plural: Indonesian has no grammatical plural; context determines
  plurality. Avoid English-style -s suffix unless quoting.
- Possessive: use `nya` suffix (no apostrophe).

### E.2 Register

- **Formal**: `Anda` (you), `kami` (we, exclusive), `mereka` (they),
  `saudara` (brother / sister / Mr / Mrs — polite), `Bapak / Ibu`
  (Mr / Mrs).
- **Informal**: `kamu` (you), `kita` (we, inclusive), `mereka` (they),
  friend / family names.
- Default to formal in business / official / first-contact contexts.
- Use informal only in explicitly casual contexts (chat, friends,
  social media).

### E.3 Punctuation

- Full-width punctuation for narrative: `,` `.` `?` `!` `;` (rare).
- Quotes: `" "` for direct speech; `"` for inline emphasis.
- Sentence-ending period mandatory.
- No space between Indonesian words and punctuation (e.g. 「Halo.」
  not 「Halo .」).
- Space between Indonesian and English (e.g. 「GitHub repositori」).

### E.4 Numbers, dates, currency

- Currency: `Rp` before number with space (e.g. `Rp 100.000`). Use
  `IDR` in international contexts.
- Date: `22 September 2026` (long form, common); `22/09/2026`
  (numeric); `2026-09-22` (ISO, technical).
- Time: `14.30` (24-hour, technical); `2:30 sore` (12-hour + siang /
  sore / malam, casual).
- Numbers: `.` thousand separator (Indonesian uses period, not
  comma); `,` decimal separator. Example: `Rp 1.000.000,50`.
- Phone: `+62 21 1234 5678` (international); `0812-3456-7890` (mobile).

### E.5 Loanwords

Common English tech terms in Indonesian:

- software (English preserved)
- hardware (English preserved)
- komputer (computer)
- internet (English preserved)
- surel / email (both used; "surel" is the official loanword; "email"
  more common in practice)
- aplikasi / app (application; both used)
- unduh / download (both used; "unduh" is official, "download" common)
- unggah / upload (similar)
- berkas / file (both used; "berkas" official)
- data (English preserved)
- server (English preserved)
- klien / client (both used)
- AI (English preserved)
- rapat / meeting (both used)
- alur kerja / workflow (both used)

Default to English term when both are acceptable; switch to the
Indonesian loanword when the audience clearly prefers it (formal
documents often use the Indonesian loanword).

### E.6 Honorifics

- Bapak (Mr) / Ibu (Mrs) + name: most polite.
- Saudara (Sdr.) + name: polite, gender-neutral.
- Formal greeting: "Bapak / Ibu [Name]" or "Yang terhormat Bapak /
  Ibu [Name]".
- Job titles: Direktur (Director), Manajer (Manager), etc.

### E.7 Casual register

Common particles:

- "sih": emphasis / mild frustration. 「Apa sih?」
- "deh": soft assertion. 「Ya udah deh.」
- "kok": surprise / questioning. 「Kok bisa?」
- "dong": request / suggestion. 「Masuk dong.」
- "lho": surprise / "wait, what?". 「Lho, bener?」

Avoid these in business / formal writing.

## F. Channel-specific tone

| Channel | Profile | Notes |
| --- | --- | --- |
| Email (business) | `id-id-email-formal` | Formal, Bapak / Ibu |
| Email (casual) | `id-id-email-casual` | Friendly, less formal |
| Twitter / X | `id-id-twitter-casual` | Short, particles OK |
| Instagram | `id-id-instagram-casual` | Caption + hashtags |
| LinkedIn (ID) | `id-id-linkedin-professional` | Achievement, formal |
| WhatsApp | `id-id-whatsapp-casual` | Short, friendly |
| Business document | `id-id-business-document` | Very formal |
| Customer support | `id-id-customer-support` | Empathetic, specific action |
| Sales / landing | `id-id-landing-page-clear` | Headline, CTA |
| General professional | `id-id-friendly-professional` | Polite default fallback |

See [STYLE_PROFILES.md](STYLE_PROFILES.md) for full schema and
exemplars.

## G. AI-pattern reduction

Same rules as other locales, plus:

- Avoid 「dengan ini kami memberitahukan」 / 「berhubung dengan」
  excessive formality.
- 「sangat」「amat」「sekali」 excessive intensifiers.
- 「demikianlah」 / 「akhir kata」 letter closing clichés.
- 「sebagaimana mestinya」 vague formality.

## H. Editing intensity rules

Same as other locales.

## I. Before-and-after examples

### I.1 Intensity: standard, channel: friendly-professional

**Before:** Perusahaan kami membuat software.

**After:** Kami mengembangkan perangkat lunak untuk industri [industry].

(Note: Perusahaan → Kami (formal but direct); software → perangkat
lunak when Indonesian loanword preferred in formal context.)

### I.2 Intensity: standard, channel: email-formal

**Before:** Tolong gunakan produk kami.

**After:**
```text
Yang terhormat Bapak / Ibu [Name],

Perkenalkan, saya [Nama] dari [Perusahaan]. Kami bergerak di
bidang [industri] dan telah melayani lebih dari [jumlah] klien di
seluruh Indonesia.

Apakah Bapak / Ibu berkenan untuk meluangkan waktu 15 menit dalam
beberapa minggu ke depan agar kami dapat berdiskusi?

Terima kasih atas perhatian Bapak / Ibu.

Hormat kami,

[Nama]
[Jabatan]
[Perusahaan]
[Kontak]
```

### I.3 Intensity: light, channel: translation

**Before (English):** "Welcome to our service. Please feel free to
contact us if you have any questions."

**After:** Selamat datang di layanan kami. Jangan ragu untuk
menghubungi kami jika ada pertanyaan.

### I.4 Intensity: strict_precision, channel: research-precise

**Before:** Sebagian besar pengguna menyukai produk ini.

**After:** Berdasarkan survei pengguna 2025 (n=1.247, tingkat
kepercayaan 95%), 78% responden menyatakan preferensi untuk [produk]
dibandingkan [produk pesaing]. Hasil ini berlaku untuk sub-sampel
[demografi].

### I.5 Intensity: standard, channel: customer-support

**Before:** Maaf atas ketidaknyamanannya. Akan kami proses segera.

**After:**
```text
Halo [Nama],

Mohon maaf atas ketidaknyamanan yang terjadi.
Kami telah menerima keluhan Anda tentang [masalah].

[Tindakan spesifik yang diambil]

[Tindakan tersebut] akan selesai dalam [waktu spesifik] hari kerja.

Jangan ragu untuk menghubungi kami jika ada hal lain yang bisa kami
bantu.

Salam,
[Nama agen]
[Perusahaan]
[Kontak]
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

Editorial principles borrowed from PUEBI (Pedoman Umum Ejaan Bahasa
Indonesia, 2015), KBBI (Kamus Besar Bahasa Indonesia). Specific
citations TBD as the pack matures.

The pack does not claim any anti-detection or watermark-removal
capability.