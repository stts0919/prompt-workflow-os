# Router Case — Multi-Workflow Mapping

## Setup

- Mode: `guide`.
- Language: English.

## Input

> We're launching a course next quarter. I need the offer, the funnel, the landing page, and three emails.

## Expected routing

Multiple workflows fit. Use the `validate-a-business-idea` playbook style sequence, but for an existing offer. Run:

1. `offer-design` (037) — refine the offer.
2. `marketing-funnel` (044) — map the funnel.
3. `sales-page` (043) — landing copy.
4. `email-sequence` (046) — three-email launch.

Skip steps whose input the user already supplied.

## Expected questions

1. "What's the offer summary, audience, and price?"
2. "Which channel does the funnel start from (cold list, social, paid)?"

## Failure conditions

- Picking just one workflow and ignoring the others.
- Running all five without asking for the offer summary.
- Asking for the same context the user already supplied.
