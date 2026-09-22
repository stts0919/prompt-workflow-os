# Playbooks

A playbook is a connected sequence of workflows that delivers a multi-step outcome.

Use a playbook when the user wants the whole journey, not a single step. The router should still prefer the smallest sufficient workflow chain when only one step is needed.

## Available playbooks

- [validate-a-business-idea](validate-a-business-idea.md) — from customer definition to pricing.
- [create-high-quality-content](create-high-quality-content.md) — from topic to publish-ready article.
- [research-before-a-decision](research-before-a-decision.md) — research → memo pipeline.
- [plan-and-execute-a-project](plan-and-execute-a-project.md) — goals → task plan → review.
- [build-an-ai-agent-task](build-an-ai-agent-task.md) — spec → build → review.

## How playbooks interact with the router

- The router detects signals that point to a playbook (e.g., "validate my idea", "publish a piece", "research before I decide").
- The router then runs the playbook, skipping steps whose output already exists.
- Each playbook includes routing conditions and skip conditions — apply them.
- The playbook's final quality check runs before sign-off.

## Adding a new playbook

Follow [templates/PLAYBOOK_TEMPLATE.md](../templates/PLAYBOOK_TEMPLATE.md). Add the playbook slug to the frontmatter `playbooks:` list of each workflow that participates.
