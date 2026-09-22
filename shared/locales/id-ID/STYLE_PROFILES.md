# Style Profiles — `id-ID` (Indonesian — Indonesia)

> Source-of-truth file for the `id-ID` style profiles. Lives under
> `shared/locales/id-ID/` per the architecture in
> [`../README.md`](../README.md).

10 style profiles cover the canonical channels for Indonesian. Each
profile uses the shared schema in
[`../SHARED_STYLE_PROFILE_SCHEMA.md`](../SHARED_STYLE_PROFILE_SCHEMA.md).

## Schema

Each profile uses:

- **Code**: identifier.
- **Channel**: where this profile applies.
- **`second_person`**: how to address the reader.
- **`formality`**: high / medium / low.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: punctuation conventions.
- **`common_pitfalls`**: patterns the layer avoids.
- **`exemplar`**: a sentence in this profile's voice.

---

## 1. `id-id-friendly-professional`

- **Channel**: general business / professional writing fallback.
- **`second_person`**: Anda.
- **`formality`**: medium.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: full-width `,` `.`; no space between
  Indonesian words and punctuation; space between Indonesian and
  English.
- **`common_pitfalls`**:
  - 「dengan ini kami memberitahukan」 excessive formality.
  - 「sangat」「amat」「sekali」 excessive intensifiers.
  - Using `kamu` (informal) in business context.
- **`exemplar`**: Kami mengembangkan perangkat lunak untuk industri
  [industry]. Pelanggan kami biasanya melihat [outcome] dalam
  [timeframe].

## 2. `id-id-email-formal`

- **Channel**: business email (formal).
- **`second_person`**: Bapak / Ibu [Name] / Yang terhormat.
- **`formality`**: very high.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: full-width punctuation; formal opener;
  signature block.
- **`common_pitfalls`**:
  - Dropping to informal mid-email.
  - 「demikianlah」 / 「akhir kata」 letter closing clichés.
  - Missing specific action.
- **`exemplar**:
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

## 3. `id-id-email-casual`

- **Channel**: casual / internal email.
- **`second_person`**: Anda / Halo [Name].
- **`formality`**: medium.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: full-width punctuation; no formal opener;
  polite but not ceremonial.
- **`common_pitfalls`**:
  - Over-formality in internal communication.
  - Casual particles (sih / dong / deh) leaking in.
- **`exemplar`**: Halo [Name], mohon konfirmasi untuk [topik]. Terima
  kasih sebelumnya. Jika ada pertanyaan, jangan ragu menghubungi.

## 4. `id-id-twitter-casual`

- **Channel**: Twitter / X.
- **`second_person`**: kamu / kalian / Anda.
- **`formality`**: low.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: short sentences; emoji OK; particles OK.
- **`common_pitfalls`**:
  - Excessive formality kills engagement.
  - Excessive hashtags.
- **`exemplar`**: Udah 6 bulan nungguin tool ini keluarin fitur
  baru. Akhirnya bikin sendiri dalam 2 minggu. DIY terbaik. ✨

## 5. `id-id-instagram-casual`

- **Channel**: Instagram captions.
- **`second_person`**: kamu / kalian.
- **`formality`**: low.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: short + emoji + hashtags.
- **`common_pitfalls`**:
  - Excessive hashtags (>5).
  - No emoji (loses IG voice).
- **`exemplar`**: ☕️ Tempat ngopi baru di [lokasi]! Latte art-nya
  keren banget 📸 Wajib mampir kalau lagi di area sini. #kopi
  #caféhits

## 6. `id-id-whatsapp-casual`

- **Channel**: WhatsApp messages (dominant in Indonesia).
- **`second_person`**: kamu / [name].
- **`formality`**: low.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: short messages; emoji OK; casual particles.
- **`common_pitfalls`**:
  - Over-formality in chat.
  - Long paragraphs.
- **`exemplar`**: Sip! Besok jam 14 ya 👍 Jangan telat!

## 7. `id-id-linkedin-professional`

- **Channel**: LinkedIn posts / comments.
- **`second_person`**: Anda.
- **`formality`**: medium-high.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: em-dash for asides; line breaks between
  paragraphs.
- **`common_pitfalls`**:
  - "Thrilled to announce" English cliché.
  - Excessive hashtags.
  - Casual particles leaking in.
- **`exemplar`**: Senang sekali membagikan bahwa saya telah bergabung
  dengan XYZ sebagai Head of Marketing. Saya berharap dapat
  membangun sesuatu yang luar biasa bersama tim ini.

## 8. `id-id-business-document`

- **Channel**: formal business documents (proposals, contracts).
- **`second_person`**: Bapak / Ibu / Saudara.
- **`formality`**: very high.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: full-width; structured headings; data
  tables.
- **`common_pitfalls`**:
  - Missing required disclosures.
  - Numbers without units.
- **`exemplar`**: Proposal ini merekomendasikan pengenalan [product]
  sebagai solusi untuk [problem]. Implementasi diharapkan memberikan
  [outcome], dengan periode pengembalian investasi selama [period].

## 9. `id-id-customer-support`

- **Channel**: customer support replies.
- **`second_person`**: Bapak / Ibu / Saudara.
- **`formality`**: high.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: empathy first, action second; specific
  timeline.
- **`common_pitfalls`**:
  - 「Mohon maaf atas ketidaknyamanan yang terjadi」 cliché without
    specifics.
  - Defensive tone.
  - No specific next step.
- **`exemplar**:
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

## 10. `id-id-landing-page-clear`

- **Channel**: sales / landing pages.
- **`second_person`**: Anda.
- **`formality`**: medium.
- **`locale`**: Indonesia.
- **`punctuation_notes`**: headline-driven; short paragraphs; CTA
  button text action + outcome.
- **`common_pitfalls`**:
  - 「Revolusioner」 / 「mengubah permainan」 exaggeration.
  - Multiple CTAs.
  - Missing social proof.
- **`exemplar`**: **Headline:** [Outcome] untuk [audience] dalam
  [timeframe]. **Subhead:** [One-line how]. **CTA:** Mulai
  gratis →

---

## How to choose a profile

Decision table:

| Workflow category | Channel hint | Default profile |
| --- | --- | --- |
| content | general | `id-id-friendly-professional` |
| content | Twitter / X | `id-id-twitter-casual` |
| content | Instagram | `id-id-instagram-casual` |
| content | WhatsApp | `id-id-whatsapp-casual` |
| content | long-form | `id-id-friendly-professional` |
| business | email (formal) | `id-id-email-formal` |
| business | email (casual) | `id-id-email-casual` |
| business | LinkedIn | `id-id-linkedin-professional` |
| business | proposal / contract | `id-id-business-document` |
| business | sales / landing | `id-id-landing-page-clear` |
| any | customer support | `id-id-customer-support` |

User's explicit channel hint overrides the default. Workflows may
also declare `localization.default_style_profile` in frontmatter.