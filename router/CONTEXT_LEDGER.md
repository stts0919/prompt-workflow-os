# Context Ledger

The AI maintains this internally. Show it to the user only when useful or requested.

## Schema

```yaml
goal: null                       # one-sentence restatement of what the user wants
mode: guide                      # guide | quick | recommend
language: auto                   # detected user language; deliverable_language holds the requested output language
deliverable_language: null       # explicit output language if different from language
current_stage: null              # blank | exploratory | material-in-hand | drafting | refining | publishing
primary_goal: null               # create | understand | decide | organize | analyze | build | fix
complexity: low                  # low | medium | high
urgency: low                     # low | medium | high
verification_need: none          # none | soft | strict
current_information_need: none   # none | soft | strict
experience_level: null           # novice | intermediate | expert
confirmed_context: []            # list of strings: facts the user provided
constraints: []                  # tone, length, deadline, must-include/must-avoid
available_inputs: []             # list of provided artefacts (with short labels)
unknowns: []                     # missing items, ranked by impact on output
selected_workflow: null          # single workflow slug
workflow_chain: []               # ordered slugs if multi-step
playbook: null                   # playbook slug if a playbook is in play
need_current_information: false  # true if decision needs fresh data
need_verification: false         # true if factual claims must be checked
open_assumptions: []             # assumptions the AI made, labeled with why
```

## Update discipline

- Update on every state transition (DISCOVER → CLARIFY → SELECT → …).
- Drop entries that no longer apply.
- Never let `open_assumptions` exceed five without warning the user.
- Persist the ledger across turns; do not ask the user to repeat themselves.

## When to show the ledger

- User asks "what do you know so far?"
- Switching from quick → guide mid-conversation.
- Before recommending a workflow chain in `recommend` mode.
- When the AI is about to make a non-trivial assumption.
