# Locale Style Profile Schema

Every locale pack must define its style profiles using this canonical schema. The schema is intentionally minimal so any locale can express its profile.

## Schema

```yaml
id:
locale:
best_for:
tone:
formality:
directness:
sentence_rhythm:
first_person_policy:
second_person_policy:
rhetorical_question_policy:
evidence_standard:
punctuation_notes:
avoid:
preferred_patterns:
ending_style:
```

## Field definitions

| Field                       | Type                          | Description |
| --------------------------- | ----------------------------- | ----------- |
| `id`                        | string (kebab-case)            | Stable identifier. Convention: `{locale}-{channel-or-role}`. Example: `zh-tw-threads-insightful`, `en-us-formal-email`, `ja-jp-business-consulting`. |
| `locale`                    | BCP-47 locale code            | e.g., `zh-TW`, `en-US`, `ja-JP`. |
| `best_for`                  | string                        | Short human description. |
| `tone`                      | string                        | Emotional register in the locale's words. |
| `formality`                 | enum: low / medium / high      | Bookish vs casual. |
| `directness`                | enum: low / medium / high / very-high | How terse and action-oriented. |
| `sentence_rhythm`           | string                        | Variation in length and structure. |
| `first_person_policy`       | string                        | When to use 我 / 我方 / 我們 / 不使用 / etc. |
| `second_person_policy`      | string                        | When to use 你 / 您 / 閣下 / 読者の皆さま / etc. |
| `rhetorical_question_policy`| string                        | When rhetorical questions are appropriate. |
| `evidence_standard`         | enum: light / medium / high / strict | What support claims need. |
| `punctuation_notes`         | list of strings               | Quotation marks, list punctuation, full-width vs half-width, etc. |
| `avoid`                     | list of strings               | Phrases and patterns to remove. |
| `preferred_patterns`        | list of strings               | Patterns that fit naturally in this locale. |
| `ending_style`              | string                        | How the piece typically closes. |

## Sample paragraph

Every profile must include one short sample paragraph in the locale's natural writing. The sample should:

- Use only protected content from real workflows.
- Demonstrate the rhythm, tone, formality, and ending style.
- Avoid AI tells (era framing, slogan-like endings, forced three-item lists).

## Minimum profile set per locale

A locale pack should at minimum cover these channel-or-role profiles. New channels add new profiles; the router chooses.

1. Conversational default.
2. Friendly professional.
3. Business consulting.
4. Threads / X-style social (optional if locale rarely writes there).
5. Instagram-style social (optional if locale rarely writes there).
6. LinkedIn-style social.
7. Email.
8. Sales copy.
9. Landing page.
10. Long-form article.
11. Research / report.
12. Technical doc.
13. SOP / runbook.
14. Agent / API specification.
15. Customer support.

Locales with regional usage patterns may add more (for example, `ja-jp-keigo-formal`, `de-de-formal-letter`). Each addition must satisfy the schema.

## Validation

The structural validator (`scripts/validate.py`) checks:

- Each profile has all 15 schema fields.
- Each profile has at least one sample paragraph.
- `locale` is a valid BCP-47 tag.

Functional validation runs against real models using the cases in `tests/workflow-cases/`.
