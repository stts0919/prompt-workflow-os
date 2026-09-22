# Fact, Inference, and Recommendation Rules

This repository distinguishes five kinds of statements. Mixing them up is the most common quality failure.

| Kind                | Definition                                                                      | Trust basis                                              |
| ------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Verified fact       | Confirmed by a cited, dated, and reachable source                               | Authoritative external source                            |
| User-provided fact  | Stated by the user in this conversation                                         | The user                                                 |
| Assumption          | A judgment the AI makes because something is missing                            | Explicitly labeled; reversible when the user supplies data |
| Inference           | A conclusion derived from verified or user-provided facts                       | Logical chain shown                                       |
| Recommendation      | A course of action, with reasoning and trade-offs                                | Inference or assumption + stated criteria                 |

## Required labeling in outputs

When an output mixes these kinds, mark each section explicitly. Suggested headers:

```
Verified facts
- ...
User-provided facts
- ...
Assumptions
- ...
Inferences
- ...
Recommendations
- ...
```

For short outputs, place labels inline:

- `[fact]` verified or user-provided
- `[assumption]` flagged for replacement
- `[inference]` derived from the above
- `[recommendation]` action with trade-offs

## Guardrails

- Never label a fabricated claim as `[fact]`. Use `[assumption]` or explicitly say "this is unverified".
- Never upgrade an assumption to fact without new evidence.
- When recommending, list at least one alternative with its trade-offs.
- When inferring, show the chain — at least briefly — so the user can challenge it.
- If the user supplies a fact with a request to question it, label it `[user-provided fact — contested in this turn]`.
