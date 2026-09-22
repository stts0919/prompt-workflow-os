#!/usr/bin/env python3
"""Generate the six index files in indexes/.

Run from the repository root.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = ROOT / "workflows"
INDEXES_DIR = ROOT / "indexes"

CATEGORY_DIR = {
    "content": "01-content",
    "business": "02-business",
    "research": "03-research",
    "workflow": "04-workflow",
    "technical": "05-technical",
}

CATEGORY_LABEL = {
    "content": "Content Creation & Communication",
    "business": "Business, Marketing & Customer Growth",
    "research": "Research, Analysis & Decision Making",
    "workflow": "Planning, Operations & Self-Management",
    "technical": "AI, Code & Data",
}

CATEGORY_ORDER = ["content", "business", "research", "workflow", "technical"]


def load_workflows():
    out = []
    for cat in CATEGORY_ORDER:
        d = WORKFLOWS_DIR / CATEGORY_DIR[cat]
        for p in sorted(d.iterdir()):
            m = re.match(r"(\d{3})-([\w-]+)\.md", p.name)
            if not m:
                continue
            wid, slug = m.group(1), m.group(2)
            text = p.read_text()
            title_m = re.search(r"^title:\s*\"(.+)\"", text, flags=re.MULTILINE)
            purp_m = re.search(r'^purpose:\s*"([^"]+)"', text, flags=re.MULTILINE)
            title = title_m.group(1) if title_m else slug
            purpose = purp_m.group(1) if purp_m else ""
            out.append({
                "id": wid,
                "slug": slug,
                "category": cat,
                "title": title,
                "purpose": purpose,
                "path": f"workflows/{CATEGORY_DIR[cat]}/{p.name}",
            })
    return out


def by_category(workflows):
    out = {c: [] for c in CATEGORY_ORDER}
    for w in workflows:
        out[w["category"]].append(w)
    return out


def render_05_all(workflows):
    lines = ["# All 100 Prompt Workflows", ""]
    lines.append("> One entry per workflow. Cross-link any workflow's `Related workflows` section to navigate laterally.")
    lines.append("")
    for cat in CATEGORY_ORDER:
        lines.append(f"## 0{CATEGORY_ORDER.index(cat)+1} — {CATEGORY_LABEL[cat]}")
        lines.append("")
        for w in by_category(workflows)[cat]:
            lines.append(f"- **{w['id']} — [{w['title']}](../{w['path']})** — {w['purpose']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def render_01_by_goal(workflows):
    lines = ["# Browse by Goal", "",
             "What outcome are you trying to produce? Pick the category that matches the goal, then the workflow inside it.",
             ""]
    sections = [
        ("Create and communicate",
         "content",
         "articles, posts, videos, newsletters, stories, presentations, rewriting, localization, quality review"),
        ("Grow a product or business",
         "business",
         "customers, competitors, positioning, validation, pricing, campaigns, sales, retention, strategic choices"),
        ("Learn, verify, and decide",
         "research",
         "source evaluation, summaries, fact checks, evidence, scenarios, decisions"),
        ("Plan and execute work",
         "workflow",
         "tasks, projects, meetings, SOPs, documentation, automation, learning, self-review"),
        ("Build with AI, code, and data",
         "technical",
         "prompts, agents, code, debugging, data, APIs, schemas, system design"),
    ]
    for header, cat, desc in sections:
        lines.append(f"## {header}")
        lines.append("")
        lines.append(f"Use the **{cat}** category for {desc}.")
        lines.append("")
        lines.append("| # | Workflow | Purpose |")
        lines.append("|---|----------|---------|")
        for w in by_category(workflows)[cat]:
            lines.append(f"| {w['id']} | [{w['title']}](../{w['path']}) | {w['purpose']} |")
        lines.append("")
    lines.append("For the complete list, see [All 100 workflows](05-all-100-workflows.md).")
    lines.append("")
    return "\n".join(lines)


def render_02_by_problem(workflows):
    problems = [
        ("I do not know what to write about.", "001 — content-idea-generation"),
        ("My draft feels weak or unclear.", "009 — content-editing"),
        ("My content needs a quality review before I publish.", "029 — content-quality-review"),
        ("I need to translate or adapt content for another market.", "027 — translation-localization"),
        ("I do not know who my customer is.", "031 — customer-persona"),
        ("I do not know if my idea will sell.", "038 — product-idea-validation"),
        ("I cannot tell how I compare to competitors.", "034 — competitor-analysis"),
        ("I have too much information to read.", "058 — document-summary"),
        ("I do not know whether a claim is true.", "064 — fact-check"),
        ("I need a decision memo I can defend.", "069 — decision-memo"),
        ("I am overwhelmed by a project.", "076 — project-plan"),
        ("I need a repeatable process so others can run it.", "080 — sop-builder"),
        ("My code is not working.", "094 — debugging"),
        ("I keep getting generic answers from the AI.", "090 — prompt-improvement"),
        ("I need to give an AI agent a precise brief.", "091 — agent-task-spec"),
        ("I want to design a system from scratch.", "100 — system-design"),
        ("I have raw feedback I want to learn from.", "033 — customer-feedback-analysis"),
        ("I want to challenge my own reasoning.", "067 — counterargument"),
    ]
    lines = ["# Browse by Problem", "",
             "Map common user pain to the workflow that usually starts the work. "
             "The router will confirm context before executing.",
             "",
             "| If you are saying... | Try this workflow |",
             "|---|--------------------|"]
    slug_to_path = {w["slug"]: w["path"] for w in workflows}
    for problem, label in problems:
        wid, name = label.split(" — ", 1)
        slug = name
        path = slug_to_path.get(slug, "")
        if path:
            link = f"[{label}](../{path})"
        else:
            link = label
        lines.append(f"| \"{problem}\" | {link} |")
    lines.append("")
    return "\n".join(lines)


def render_03_by_input(workflows):
    table = [
        ("A rough topic or idea",
         "001 content-idea-generation", "038 product-idea-validation"),
        ("A draft",
         "009 content-editing", "008 article-rewrite", "029 content-quality-review"),
        ("A long document or report",
         "058 document-summary", "060 data-extraction", "064 fact-check", "069 decision-memo"),
        ("A meeting transcript or rough notes",
         "059 meeting-summary", "079 meeting-notes"),
        ("Customer feedback (reviews, tickets, interviews)",
         "033 customer-feedback-analysis", "051 retention-plan"),
        ("A dataset",
         "096 data-exploration", "097 data-analysis"),
        ("Code and an error message",
         "094 debugging", "092 code-explanation"),
        ("A product or service description",
         "034 competitor-analysis", "036 value-proposition", "041 pricing-strategy", "043 sales-page"),
        ("A vague goal (\"I want to launch\")",
         "075 goal-setting", "072 task-breakdown", "076 project-plan"),
        ("A play to defend or a counter-argument",
         "066 reasoning-audit", "067 counterargument"),
    ]
    lines = ["# Browse by What You Already Have", "",
             "Pick the row that matches your input. The router will ask what you want to produce before it picks a workflow.",
             "",
             "| You have... | Workflows to start with |",
             "|-------------|--------------------------|"]
    slug_to_path = {w["slug"]: w["path"] for w in workflows}
    for row in table:
        have = row[0]
        starts = []
        for entry in row[1:]:
            wid, slug = entry.split(" ", 1)
            path = slug_to_path.get(slug, "")
            if path:
                starts.append(f"[{wid} {slug}](../{path})")
            else:
                starts.append(f"{wid} {slug}")
        lines.append(f"| {have} | {', '.join(starts)} |")
    lines.append("")
    return "\n".join(lines)


def render_04_by_output(workflows):
    rows = [
        ("Publishable article or long post",
         "007 article-draft", "009 content-editing"),
        ("Social post", "012 social-post"),
        ("Thread or series", "013 thread-series"),
        ("Carousel or slides", "014 carousel"),
        ("Short-form video", "015 short-video-script"),
        ("Newsletter issue", "011 newsletter"),
        ("Presentation", "019 presentation-story"),
        ("Sales page or landing page", "043 sales-page"),
        ("Email sequence", "046 email-sequence"),
        ("Weekly plan", "074 weekly-plan"),
        ("Project plan", "076 project-plan"),
        ("SOP", "080 sop-builder"),
        ("Decision memo", "069 decision-memo"),
        ("Executive brief", "070 executive-brief"),
        ("Schema", "098 schema-design"),
        ("System design", "100 system-design"),
        ("AI agent task spec", "091 agent-task-spec"),
    ]
    lines = ["# Browse by Desired Output", "",
             "Pick the row that matches the artifact you want to ship at the end.",
             "",
             "| Output | Workflow |",
             "|--------|----------|"]
    slug_to_path = {w["slug"]: w["path"] for w in workflows}
    for desc, *entries in rows:
        links = []
        for e in entries:
            wid, slug = e.split(" ", 1)
            path = slug_to_path.get(slug, "")
            if path:
                links.append(f"[{wid} {slug}](../{path})")
            else:
                links.append(f"{wid} {slug}")
        lines.append(f"| {desc} | {', '.join(links)} |")
    lines.append("")
    return "\n".join(lines)


def render_00_start_here():
    return (
        "# Start Here\n"
        "\n"
        "> If this is your first time using the repository, read this page before anything else.\n"
        "\n"
        "## What this repository is\n"
        "\n"
        "A Markdown-first library of 100 prompt workflows plus a router, playbooks, "
        "shared rules, templates, and evaluation cases. The user never has to memorize "
        "a workflow name. The router infers intent and selects the smallest sufficient workflow chain.\n"
        "\n"
        "## 60-second onboarding\n"
        "\n"
        "1. Share the repository with an AI that can read files.\n"
        "2. Tell it to read [../START.md](../START.md).\n"
        "3. Describe what you want in natural language.\n"
        "4. Answer 1–2 questions, then receive the result.\n"
        "\n"
        "For verbose guidance see [../START.md](../START.md) and [../README.md](../README.md).\n"
        "\n"
        "## Browse paths\n"
        "\n"
        "- [By goal](01-by-goal.md) — when you know the outcome you want.\n"
        "- [By problem](02-by-problem.md) — when you have a known pain.\n"
        "- [By input](03-by-input.md) — when you already have material.\n"
        "- [By output](04-by-output.md) — when you know the artifact you need.\n"
        "- [All 100](05-all-100-workflows.md) — the complete list.\n"
        "\n"
        "## Three modes\n"
        "\n"
        "- **Guide me** — step-by-step discovery, confirm before each major move.\n"
        "- **Quick mode** — execute with labeled assumptions when risk is low.\n"
        "- **Recommend** — propose a workflow chain before starting.\n"
        "\n"
        "## What to read next\n"
        "\n"
        "- New to the repo: [../README.md](../README.md) then [../AGENTS.md](../AGENTS.md).\n"
        "- Building or extending: [../templates/WORKFLOW_TEMPLATE.md](../templates/WORKFLOW_TEMPLATE.md).\n"
        "- Curious about quality: [../shared/QUALITY_CHECKLISTS.md](../shared/QUALITY_CHECKLISTS.md) and [../VALIDATION_REPORT.md](../VALIDATION_REPORT.md).\n"
    )


def main():
    INDEXES_DIR.mkdir(parents=True, exist_ok=True)
    workflows = load_workflows()
    assert len(workflows) == 100, f"expected 100 workflows, got {len(workflows)}"

    (INDEXES_DIR / "00-start-here.md").write_text(render_00_start_here())
    (INDEXES_DIR / "01-by-goal.md").write_text(render_01_by_goal(workflows))
    (INDEXES_DIR / "02-by-problem.md").write_text(render_02_by_problem(workflows))
    (INDEXES_DIR / "03-by-input.md").write_text(render_03_by_input(workflows))
    (INDEXES_DIR / "04-by-output.md").write_text(render_04_by_output(workflows))
    (INDEXES_DIR / "05-all-100-workflows.md").write_text(render_05_all(workflows))
    print("Wrote 6 index files.")


if __name__ == "__main__":
    main()
