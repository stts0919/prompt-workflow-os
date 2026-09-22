# Output Formats

How the AI delivers results from workflow execution.

## 1. Universal header

Every deliverable opens with a short header so the user can scan the answer.

```
Goal: <one-line goal>
Mode: <guide | quick | recommend>
Workflow: <slug>
Assumptions: <count> labeled — listed in the Assumptions section
Verification: <none | soft | strict> — see Verification section
Next step: <suggested workflow slug or "none">
```

## 2. Common output skeletons

| Output kind        | Skeleton                                                                                  |
| ------------------ | ----------------------------------------------------------------------------------------- |
| Article draft      | title → lede → subheadings → body → call to action → sources                              |
| Decision memo      | decision → criteria → options considered → chosen option → trade-offs → next steps       |
| Executive brief    | bottom line → why now → key facts → risks → recommended actions                           |
| Sales page         | headline → sub-headline → problem → promise → proof → offer → guarantee → call to action  |
| Email sequence     | per email: subject → preview → body → call to action → plain-text fallback                |
| SOP                | purpose → scope → prerequisites → numbered steps → exceptions → quality check             |
| Project plan       | objective → milestones → tasks per milestone → owners → risks → dependencies              |
| Code task spec     | objective → inputs → outputs → acceptance criteria → non-goals → constraints             |
| System design      | context → requirements → architecture → components → data flow → trade-offs → open Qs    |
| Schema             | entity → fields → relationships → indexes → sample queries → migrations                   |
| Review             | verdict → strengths → issues (severity-tagged) → recommendations                          |
| Comparison table   | rows = options; columns = criteria the user cares about                                   |

## 3. Format selection rules

- Match the channel. Article → markdown headings. Email → plain text fallback. Carousel → slide-by-slide JSON or outline.
- Prefer tables when the user is comparing 3+ options.
- Prefer numbered lists when order matters.
- Prefer bullets when only enumeration matters.
- Use code blocks for code, JSON, and shell commands.
- Use blockquotes for direct quotes from sources.

## 4. Length discipline

- Default to short. If the user did not specify length, aim for "minimum useful".
- Articles: ask for target length, otherwise assume 800–1,500 words.
- Emails: 120–250 words for transactional, 400–700 words for educational.
- Briefs: 1 page or less.
- Plans: 1–2 pages; expand only when the user requests detail.
- Code: shortest correct snippet that satisfies the contract.

## 5. Final review checklist

Before delivering, run the [QUALITY_CHECKLISTS.md](QUALITY_CHECKLISTS.md) checks. Only deliver when they pass.
