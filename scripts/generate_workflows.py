#!/usr/bin/env python3
"""Generate the 100 workflow files from a curated content map.

Run from the repository root.
"""

import os
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = ROOT / "workflows"

CATEGORY_DIR = {
    "content": "01-content",
    "business": "02-business",
    "research": "03-research",
    "workflow": "04-workflow",
    "technical": "05-technical",
}


# --- Taiwan Traditional Chinese localization overrides -----------------------
# Workflows that are high-traffic in Taiwan get an explicit `localization:` block
# in their frontmatter. Other workflows fall back to the category default the
# router infers from `templates/WORKFLOW_TEMPLATE.md`.
#
# Schema per id:
#   default_style_profile: zh-TW profile name (see ../shared/locales/zh-TW/STYLE_PROFILES.md)
#   locale_override:       None to use default, or a profile name to override
#                          when the deliverable's target market is Taiwan
#   editing_intensity:     one of none / light / standard / strict_precision
LOCALIZATION_OVERRIDES: dict[str, dict] = {
    # ---- content (11) — local social / content creation ----
    "012": {"default_style_profile": "zh-tw-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "013": {"default_style_profile": "zh-tw-threads-insightful",    "locale_override": None, "editing_intensity": "standard"},
    "014": {"default_style_profile": "zh-tw-instagram-casual",       "locale_override": None, "editing_intensity": "standard"},
    "015": {"default_style_profile": "zh-tw-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "018": {"default_style_profile": "zh-tw-conversational-help",    "locale_override": None, "editing_intensity": "standard"},
    "022": {"default_style_profile": "zh-tw-customer-support",       "locale_override": None, "editing_intensity": "standard"},
    "023": {"default_style_profile": "zh-tw-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "025": {"default_style_profile": "zh-tw-long-form-article",      "locale_override": None, "editing_intensity": "standard"},
    "026": {"default_style_profile": "zh-tw-conversational-help",    "locale_override": None, "editing_intensity": "standard"},
    "027": {"default_style_profile": "zh-tw-friendly-professional", "locale_override": None, "editing_intensity": "light"},
    "028": {"default_style_profile": "zh-tw-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    # ---- business (12) — local business / marketing / sales ----
    "031": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "standard"},
    "032": {"default_style_profile": "zh-tw-conversational-help",    "locale_override": None, "editing_intensity": "standard"},
    "035": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "standard"},
    "036": {"default_style_profile": "zh-tw-landing-page-clear",     "locale_override": None, "editing_intensity": "standard"},
    "037": {"default_style_profile": "zh-tw-sales-clear",            "locale_override": None, "editing_intensity": "standard"},
    "042": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "standard"},
    "043": {"default_style_profile": "zh-tw-landing-page-clear",     "locale_override": "zh-tw-sales-clear", "editing_intensity": "standard"},
    "045": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "standard"},
    "046": {"default_style_profile": "zh-tw-email-professional",     "locale_override": None, "editing_intensity": "standard"},
    "047": {"default_style_profile": "zh-tw-email-professional",     "locale_override": "zh-tw-sales-clear", "editing_intensity": "standard"},
    "048": {"default_style_profile": "zh-tw-sales-clear",            "locale_override": None, "editing_intensity": "standard"},
    "052": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "strict_precision"},
    # ---- research (6) — local research / reporting / decision ----
    "055": {"default_style_profile": "zh-tw-research-precise",       "locale_override": None, "editing_intensity": "standard"},
    "057": {"default_style_profile": "zh-tw-research-precise",       "locale_override": None, "editing_intensity": "standard"},
    "064": {"default_style_profile": "zh-tw-research-precise",       "locale_override": None, "editing_intensity": "strict_precision"},
    "065": {"default_style_profile": "zh-tw-research-precise",       "locale_override": None, "editing_intensity": "strict_precision"},
    "069": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "strict_precision"},
    "070": {"default_style_profile": "zh-tw-business-consulting",    "locale_override": None, "editing_intensity": "strict_precision"},
    # ---- workflow (7) — process / SOP / planning ----
    # These workflows ship BOTH the Taiwan zh-TW reference and a zh-CN Mainland
    # profile, since both audiences use the same operational categories
    # (SOPs, plans, handoffs). default_style_profile points at the zh-TW
    # canonical; locale_style_profile_overrides.zh-TW is null (use category
    # default) and zh-CN override points at zh-cn-friendly-professional.
    "072": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "074": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "076": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "080": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "081": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "086": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    "088": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "standard"},
    # ---- technical (5) — code / data / agent spec ----
    "089": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "light"},
    "091": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "strict_precision"},
    "092": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "light"},
    "095": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "light"},
    "098": {"default_style_profile": "zh-cn-friendly-professional", "locale_override": None, "editing_intensity": "light"},
}

# --- Curated content for all 100 workflows ----------------------------------
# Each entry: (slug, title, category, aliases, triggers, input_types, output_types,
#              requires, produces, related, playbooks, mode_support, purpose,
#              what, why, when_use, when_not_use, prepare, how_ai_helps,
#              what_you_get, next_steps, handoff_text)

WORKFLOWS = {
    # ---------------------------------------------------------------- 01-content 001-029
    "001": {
        "slug": "content-idea-generation",
        "title": "Generate Content Ideas",
        "category": "content",
        "aliases": ["blog ideas", "content ideas", "video ideas", "post ideas", "topic ideas"],
        "triggers": ["need topics", "ran out of ideas", "what should I post", "give me ideas", "brainstorm content"],
        "input_types": ["topic or domain", "audience description", "business goal"],
        "output_types": ["idea list", "angles", "hooks"],
        "requires": ["topic or domain", "target audience", "high-level goal (educate, sell, build authority)"],
        "produces": ["prioritized idea list", "angles per idea", "opening hooks for top ideas"],
        "related": ["content-pillar-design", "topic-prioritization", "audience-message-map"],
        "playbooks": ["create-high-quality-content"],
        "purpose": "Turn a vague topic into a prioritized backlog of distinct content ideas.",
        "what": (
            "Produce a structured set of content ideas for a topic, audience, and goal. "
            "Each idea is paired with an angle, an opening hook, and a fitness note so you can pick what to publish next."
        ),
        "why": (
            "Most content stalls because the backlog is shallow or repetitive. "
            "A short, ranked backlog with explicit angles prevents rehashed posts and keeps the editorial calendar full."
        ),
        "when_use": [
            "You're staring at a blank content calendar.",
            "Your niche feels saturated and you want fresh angles.",
            "You have a topic but no idea which slice of the audience to address first.",
        ],
        "when_not_use": [
            "You already have a backlog that needs filtering — use topic-prioritization (005) instead.",
            "You're producing one specific artifact — go straight to article-outline (006), social-post (012), or short-video-script (015).",
            "You want strategic guidance on what to be about — use content-pillar-design (002).",
        ],
        "prepare": [
            "Topic or domain — be specific (\"B2B SaaS pricing\"), not vague (\"marketing\").",
            "Target audience — jobs-to-be-done or one-line persona.",
            "Goal — educate, drive sign-ups, build authority, nurture, sell.",
        ],
        "how_ai": [
            "1. Restate the goal in one sentence and confirm the audience and channel.",
            "2. Generate 15–25 distinct ideas across angles (contrarian, beginner, advanced, story, data, comparison).",
            "3. Score each idea on audience fit, novelty, and production cost.",
            "4. Provide an opening hook for the top 5 ideas.",
            "5. Suggest the next workflow: article-outline (006) for the chosen idea.",
        ],
        "what_get": [
            "A prioritized idea table with score and angle.",
            "A short hook for each of the top 5 ideas.",
            "Assumptions about audience and goal.",
            "One next-workflow suggestion.",
        ],
        "next_steps": ["article-outline (006)", "topic-prioritization (005)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: selected_idea\n"
            "    description: the idea chosen by the user for further development\n"
            "  - key: audience\n"
            "    description: confirmed audience description\n"
            "  - key: goal\n"
            "    description: confirmed content goal"
        ),
    },
    "002": {
        "slug": "content-pillar-design",
        "title": "Design Content Pillars",
        "category": "content",
        "aliases": ["content pillars", "niche pillars", "editorial pillars", "topic clusters"],
        "triggers": ["what should I be about", "build my brand pillars", "editorial pillars", "topic clusters"],
        "input_types": ["brand or expert description", "audience", "competitors or references"],
        "output_types": ["pillar list", "pillar rationale", "pillar boundaries"],
        "requires": ["brand or expert positioning", "target audience", "optional reference creators or competitors"],
        "produces": ["pillar list (3–6)", "pillar rationale", "pillar boundaries (what each pillar covers and excludes)"],
        "related": ["content-idea-generation", "positioning", "audience-message-map"],
        "playbooks": [],
        "purpose": "Define durable content pillars that anchor an editorial calendar and brand identity.",
        "what": (
            "Pick 3–6 content pillars that justify every post you publish. "
            "Each pillar gets a clear scope (what it covers), a boundary (what it doesn't), and a differentiator (why you own it)."
        ),
        "why": (
            "Without pillars, content drifts across topics, confuses the audience, and never compounds. "
            "Pillars let ideas, repurposing, and SEO reinforce each other."
        ),
        "when_use": [
            "You're starting a blog, channel, or newsletter.",
            "Your content feels scattered; readers can't summarize what you're about.",
            "You want to align your team or contractors around the same themes.",
        ],
        "when_not_use": [
            "You already have working pillars and need ideas — use content-idea-generation (001).",
            "You need a one-time article — skip the pillar work.",
        ],
        "prepare": [
            "Brand summary or expert bio.",
            "Target audience description.",
            "Optional: 3 creators or publications you admire, with reasons.",
        ],
        "how_ai": [
            "1. Restate the brand and audience in one sentence.",
            "2. Propose 4–6 candidate pillars with one-line rationale each.",
            "3. Note boundaries and overlap risks between pillars.",
            "4. Recommend the strongest 3–5 pillars with confidence rationale.",
            "5. Suggest how to test the pillars with content-idea-generation (001).",
        ],
        "what_get": [
            "A pillar table (pillar → scope → boundary → differentiator).",
            "A 2-paragraph rationale for the chosen set.",
            "One next-workflow suggestion: content-idea-generation (001).",
        ],
        "next_steps": ["content-idea-generation (001)", "audience-message-map (003)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: pillars\n"
            "    description: list of pillars with one-line definitions\n"
            "  - key: boundaries\n"
            "    description: notes on what each pillar excludes"
        ),
    },
    "003": {
        "slug": "audience-message-map",
        "title": "Map Audience Messages",
        "category": "content",
        "aliases": ["audience map", "message map", "awareness levels", "message matrix"],
        "triggers": ["map my audience", "write for different awareness levels", "message by segment", "what to say to whom"],
        "input_types": ["audience segments", "product or topic", "awareness levels"],
        "output_types": ["message map", "segment matrix", "call to action matrix"],
        "requires": ["audience segments", "product, service or topic", "awareness stages (problem-aware, solution-aware, etc.)"],
        "produces": ["message map", "segment × stage matrix", "tailored CTAs per cell"],
        "related": ["customer-persona", "content-pillar-design", "marketing-funnel"],
        "playbooks": [],
        "purpose": "Match each audience segment to the right message and call to action across awareness levels.",
        "what": (
            "Build a 2-axis map: audience segment on one axis, awareness level on the other. "
            "For each cell, write the headline message, the supporting proof, and the call to action."
        ),
        "why": (
            "A single message for everyone ignores where the reader is in their journey. "
            "Mapping segments to stages prevents both over-selling to novices and under-selling to ready buyers."
        ),
        "when_use": [
            "Conversion is uneven — some segments engage, others bounce.",
            "You're scaling content and need predictable message patterns.",
            "Sales calls keep repeating \"we didn't realize this was for us\".",
        ],
        "when_not_use": [
            "You don't yet know who the audience is — start with customer-persona (031).",
            "You only need one piece of content — skip the map and write directly.",
        ],
        "prepare": [
            "Audience segments (2–5).",
            "Awareness levels you care about.",
            "Product or topic summary.",
        ],
        "how_ai": [
            "1. Confirm segments and stages.",
            "2. Define the message per cell (headline, proof, CTA).",
            "3. Highlight cells where the message is risky or unsupported.",
            "4. Suggest a follow-up playbook to test one segment first.",
        ],
        "what_get": [
            "A segment × stage message matrix.",
            "CTA per cell.",
            "Risk flags for unsupported cells.",
            "Next-workflow suggestion: marketing-funnel (044).",
        ],
        "next_steps": ["marketing-funnel (044)", "campaign-plan (045)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: message_matrix\n"
            "    description: segment × stage map with headlines and CTAs"
        ),
    },
    "004": {
        "slug": "content-calendar",
        "title": "Plan a Content Calendar",
        "category": "content",
        "aliases": ["editorial calendar", "publishing calendar", "schedule posts"],
        "triggers": ["plan a calendar", "editorial calendar", "when to publish", "publishing schedule"],
        "input_types": ["channels", "posting frequency", "backlog or theme"],
        "output_types": ["calendar table", "themes per week", "production milestones"],
        "requires": ["channels (blog, LinkedIn, X, newsletter, etc.)", "cadence", "content backlog or pillars"],
        "produces": ["rolling N-week calendar", "theme-per-week summary", "production milestones"],
        "related": ["topic-prioritization", "content-pillar-design", "content-repurposing"],
        "playbooks": [],
        "purpose": "Build a rolling content calendar with concrete dates, channels, and themes.",
        "what": (
            "Lay out a calendar (typically 4–8 weeks) with date, channel, format, theme, owner, and status. "
            "It mixes pillar content, repurposed posts, and reactive opportunities."
        ),
        "why": (
            "A calendar turns a backlog into shipping velocity. Without dates, nothing gets published consistently."
        ),
        "when_use": [
            "You have ideas but no shipping rhythm.",
            "Your publishing output dropped off.",
            "You're coordinating multiple channels or contributors.",
        ],
        "when_not_use": [
            "You have no backlog yet — start with content-idea-generation (001) or topic-prioritization (005).",
            "You need a launch plan, not a steady calendar — use campaign-plan (045).",
        ],
        "prepare": [
            "Channels to publish on.",
            "Cadence (e.g., 3 posts a week).",
            "Backlog or pillars.",
        ],
        "how_ai": [
            "1. Confirm channels, cadence, and timeframe.",
            "2. Distribute backlog across dates and channels.",
            "3. Reserve 20% of slots for reactive or trending topics.",
            "4. Output a calendar table with owners and themes.",
        ],
        "what_get": [
            "Calendar table.",
            "Themes per week.",
            "Production milestones (draft dates, review dates).",
            "Suggested next workflow: content-quality-review (029).",
        ],
        "next_steps": ["topic-prioritization (005)", "content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: calendar\n"
            "    description: dated calendar slots per channel\n"
            "  - key: themes\n"
            "    description: theme summary per week"
        ),
    },
    "005": {
        "slug": "topic-prioritization",
        "title": "Prioritize Content Topics",
        "category": "content",
        "aliases": ["rank topics", "topic scoring", "decide what to write"],
        "triggers": ["which topic first", "rank my ideas", "score my backlog", "what to write next"],
        "input_types": ["topic list", "scoring criteria"],
        "output_types": ["ranked list", "scoring table", "recommended top 3"],
        "requires": ["list of topics or ideas", "scoring criteria (audience fit, novelty, effort, business value)"],
        "produces": ["ranked list", "scoring breakdown", "top-3 recommendation with rationale"],
        "related": ["content-idea-generation", "content-calendar"],
        "playbooks": [],
        "purpose": "Score and rank a backlog of topics so the next piece is the highest-leverage one.",
        "what": (
            "Apply a transparent scoring rubric to every topic. "
            "Surface the top 3 with rationale, and call out the bottom of the list so it can be cut."
        ),
        "why": (
            "Backlogs grow faster than publishing capacity. Without explicit scoring, pet topics win and high-leverage ones starve."
        ),
        "when_use": [
            "You have a backlog but no shipping decision.",
            "Your team disagrees on priority.",
            "You want to defend cuts in a backlog.",
        ],
        "when_not_use": [
            "You don't have a backlog — start with content-idea-generation (001).",
            "You need to ship a single urgent thing — skip prioritization.",
        ],
        "prepare": [
            "Topic list (5–30 items).",
            "Scoring criteria (e.g., audience fit, novelty, ease, business value).",
            "Optional weighting for each criterion.",
        ],
        "how_ai": [
            "1. Confirm scoring criteria and weights.",
            "2. Score each topic transparently.",
            "3. Output the ranked list with rationale per topic.",
            "4. Recommend top 3 to feed into article-outline (006).",
        ],
        "what_get": [
            "Ranked list.",
            "Scoring table.",
            "Top-3 recommendation.",
            "Suggested next workflow: article-outline (006).",
        ],
        "next_steps": ["article-outline (006)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: ranked_topics\n"
            "    description: ranked list with scores\n"
            "  - key: scoring_rubric\n"
            "    description: criteria and weights"
        ),
    },
    "006": {
        "slug": "article-outline",
        "title": "Create an Article Outline",
        "category": "content",
        "aliases": ["outline", "post outline", "article structure"],
        "triggers": ["outline an article", "structure a post", "help me organize", "skeleton of article"],
        "input_types": ["topic", "reader", "key points or sources"],
        "output_types": ["outline", "section beats", "opening hook draft"],
        "requires": ["topic and angle", "target reader", "key points or sources"],
        "produces": ["structured outline", "section beats", "draft opening hook"],
        "related": ["article-draft", "article-rewrite", "storytelling"],
        "playbooks": ["create-high-quality-content"],
        "purpose": "Produce a tight, ready-to-write outline for an article or long-form post.",
        "what": (
            "Create a hierarchical outline (H2/H3) with one or two lines per section and a stated job for each section. "
            "Optionally draft the opening hook."
        ),
        "why": (
            "Drafting without an outline produces bloated, meandering posts. A tight outline keeps every section earning its place."
        ),
        "when_use": [
            "You're starting a long article (800+ words).",
            "You have sources or notes and need a skeleton.",
            "You want to check structure before committing to a draft.",
        ],
        "when_not_use": [
            "You're writing a short post — go straight to social-post (012).",
            "You already have a draft and want refinement — use content-editing (009).",
        ],
        "prepare": [
            "Topic and angle.",
            "Target reader.",
            "Key points, quotes, or sources to include.",
        ],
        "how_ai": [
            "1. Lock the reader and the angle.",
            "2. Build the H2/H3 outline with one-line jobs per section.",
            "3. Insert evidence placeholders where claims will need sources.",
            "4. Draft the opening hook.",
            "5. Suggest the next workflow: article-draft (007).",
        ],
        "what_get": [
            "Hierarchical outline.",
            "One-line job per section.",
            "Draft opening hook.",
            "Source placeholders where needed.",
        ],
        "next_steps": ["article-draft (007)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: outline\n"
            "    description: section-by-section outline\n"
            "  - key: hook\n"
            "    description: opening hook draft\n"
            "  - key: source_placeholders\n"
            "    description: list of places where sources are needed"
        ),
    },
    "007": {
        "slug": "article-draft",
        "title": "Draft an Article",
        "category": "content",
        "aliases": ["write an article", "draft post", "long-form draft"],
        "triggers": ["write the article", "draft the post", "give me a draft", "compose the article"],
        "input_types": ["outline or brief", "voice guide", "word count target"],
        "output_types": ["first draft"],
        "requires": ["outline or brief", "target length", "voice guide or sample"],
        "produces": ["complete first draft", "open assumptions", "fact flags"],
        "related": ["article-outline", "article-rewrite", "content-editing", "content-quality-review"],
        "playbooks": ["create-high-quality-content"],
        "purpose": "Produce a complete first draft from a confirmed outline or brief.",
        "what": (
            "Convert an outline into a full draft that hits the target length and voice. "
            "Flag every place where a fact needs verification."
        ),
        "why": (
            "Outlines without drafts don't ship. The AI handles the mechanical writing so the user spends energy editing, not typing."
        ),
        "when_use": [
            "You have an outline and want to draft.",
            "You have a brief with audience and angle and want a fast draft.",
        ],
        "when_not_use": [
            "You don't have an outline — start with article-outline (006).",
            "You're revising an existing draft — use article-rewrite (008).",
        ],
        "prepare": [
            "Outline or brief.",
            "Target word count.",
            "Voice guide or sample paragraphs.",
        ],
        "how_ai": [
            "1. Confirm the voice and length.",
            "2. Draft section by section.",
            "3. Insert `[fact-check]` flags where claims need verification.",
            "4. End with a short Assumptions section.",
        ],
        "what_get": [
            "Complete first draft.",
            "Inline fact-check flags.",
            "Assumptions section.",
            "Suggested next workflow: content-editing (009).",
        ],
        "next_steps": ["content-editing (009)", "content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: draft\n"
            "    description: complete draft text\n"
            "  - key: fact_check_flags\n"
            "    description: inline markers where verification is required"
        ),
    },
    "008": {
        "slug": "article-rewrite",
        "title": "Rewrite an Existing Article",
        "category": "content",
        "aliases": ["rewrite", "rework draft", "improve post", "tighten article"],
        "triggers": ["rewrite this", "improve my draft", "tighten this post", "make this sharper"],
        "input_types": ["existing draft", "rewrite goal"],
        "output_types": ["rewritten draft", "change summary"],
        "requires": ["existing draft or text", "rewrite goal (shorter, sharper, different audience, new angle)"],
        "produces": ["rewritten draft", "summary of changes"],
        "related": ["article-draft", "content-editing"],
        "playbooks": [],
        "purpose": "Rewrite an existing article to meet a stated goal while preserving intent and facts.",
        "what": (
            "Take an existing draft and produce a rewritten version that meets a specific goal "
            "(shorter, sharper, different angle, different audience, new voice). "
            "Return both a change summary and the rewritten text."
        ),
        "why": (
            "Rewriting from scratch wastes work. A targeted rewrite preserves the proven core while fixing the specific weakness."
        ),
        "when_use": [
            "An old post underperforms and needs a refresh.",
            "A draft hits the wrong tone.",
            "You need the same content for a different audience.",
        ],
        "when_not_use": [
            "The draft is in good shape and only needs light editing — use content-editing (009).",
            "You're starting fresh — use article-draft (007).",
        ],
        "prepare": [
            "Existing draft.",
            "Clear rewrite goal.",
            "Voice and audience constraints.",
        ],
        "how_ai": [
            "1. Diagnose what's not working in the draft (audience, structure, voice).",
            "2. Define the rewrite target (length, angle, audience).",
            "3. Rewrite section by section, preserving factual claims.",
            "4. Add a 5-bullet change summary at the top.",
        ],
        "what_get": [
            "Rewritten draft.",
            "5-bullet change summary.",
            "Assumption and verification notes.",
        ],
        "next_steps": ["content-editing (009)", "content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: rewritten_draft\n"
            "    description: the rewritten article text\n"
            "  - key: change_summary\n"
            "    description: list of material changes"
        ),
    },
    "009": {
        "slug": "content-editing",
        "title": "Edit for Clarity",
        "category": "content",
        "aliases": ["copy edit", "editorial pass", "clarity edit", "proofread"],
        "triggers": ["edit this", "clean up", "proofread", "tighten prose", "clarity pass"],
        "input_types": ["draft", "editing goal"],
        "output_types": ["edited draft", "edit notes"],
        "requires": ["draft", "editing goal (clarity, brevity, voice, accuracy)"],
        "produces": ["edited draft", "inline edit notes", "open questions"],
        "related": ["article-draft", "article-rewrite", "content-quality-review"],
        "playbooks": [],
        "purpose": "Run a focused editorial pass that improves clarity, structure, concision, and accuracy.",
        "what": (
            "Apply a multi-pass edit: structure, sentence-level clarity, concision, voice, and accuracy. "
            "Return an edited draft with inline edit notes and a short list of open questions for the author."
        ),
        "why": (
            "First drafts are usually bloated, redundant, or meandering. A focused editorial pass turns a draft into publishable prose."
        ),
        "when_use": [
            "A draft is in good shape but reads rough.",
            "You want an outside perspective without a full rewrite.",
        ],
        "when_not_use": [
            "The structure is broken — start with article-outline (006).",
            "You need to change angle or audience — use article-rewrite (008).",
        ],
        "prepare": [
            "Draft.",
            "Editing goal.",
            "Voice reference (optional).",
        ],
        "how_ai": [
            "1. Diagnose structural issues first.",
            "2. Edit sentence by sentence for clarity and concision.",
            "3. Flag factual claims requiring verification.",
            "4. Output the edited draft plus a short edit-notes block.",
        ],
        "what_get": [
            "Edited draft.",
            "Edit notes block (issues caught + how they were fixed).",
            "Open questions for the author.",
        ],
        "next_steps": ["content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: edited_draft\n"
            "    description: draft after editing\n"
            "  - key: edit_notes\n"
            "    description: list of edits made and open questions"
        ),
    },
    "010": {
        "slug": "content-summary",
        "title": "Summarize Content",
        "category": "content",
        "aliases": ["summarize", "summary", "tldr", "shorten"],
        "triggers": ["summarize this", "give me a summary", "shorten this", "tldr"],
        "input_types": ["content (article, video transcript, document)"],
        "output_types": ["summary", "key takeaways"],
        "requires": ["content to summarize", "reader and use case"],
        "produces": ["summary tailored to reader", "5 key takeaways", "one-paragraph synopsis"],
        "related": ["document-summary", "article-draft", "content-repurposing"],
        "playbooks": [],
        "purpose": "Summarize content for a specific reader and use case.",
        "what": (
            "Read the supplied content and produce a summary sized to a specific reader and use case. "
            "Default to a one-paragraph synopsis plus 5 takeaways. Adjust when the user specifies."
        ),
        "why": (
            "Reading time is expensive. Summaries let the user decide quickly whether to dive deeper, and they feed into other workflows."
        ),
        "when_use": [
            "You're deciding whether to read an article or watch a video.",
            "You need a brief for a meeting.",
            "You want to repurpose the core of someone else's piece.",
        ],
        "when_not_use": [
            "You're summarizing a long internal document — use document-summary (058) for richer structure.",
            "You're rebuilding the article — use article-rewrite (008).",
        ],
        "prepare": [
            "Content to summarize.",
            "Reader (you, your team, executives, etc.).",
            "Use case (decision prep, briefing, newsletter).",
        ],
        "how_ai": [
            "1. Read the content.",
            "2. Identify the central claim and supporting points.",
            "3. Write a synopsis, then 5 takeaways, then a \"why this matters\" line.",
            "4. Flag any factual claim that needs verification.",
        ],
        "what_get": [
            "One-paragraph synopsis.",
            "5 key takeaways.",
            "Why-it-matters line.",
            "Suggested next workflow based on use case.",
        ],
        "next_steps": ["article-rewrite (008)", "content-repurposing (028)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: summary\n"
            "    description: tailored summary text\n"
            "  - key: takeaways\n"
            "    description: bullet takeaways"
        ),
    },
    "011": {
        "slug": "newsletter",
        "title": "Write a Newsletter",
        "category": "content",
        "aliases": ["newsletter issue", "email newsletter", "mailing"],
        "triggers": ["newsletter", "send an email update", "weekly newsletter"],
        "input_types": ["theme or topic", "audience", "previous issues"],
        "output_types": ["newsletter issue", "subject lines", "preview text"],
        "requires": ["theme or topic", "audience profile", "voice reference"],
        "produces": ["newsletter copy", "subject line variants", "preview text variants"],
        "related": ["email-sequence", "article-draft", "content-calendar"],
        "playbooks": [],
        "purpose": "Produce a single newsletter issue with subject-line variants and preview text.",
        "what": (
            "Write a complete newsletter issue (lede, body, sections, footer) for a known audience. "
            "Provide three subject line variants and three preview text variants."
        ),
        "why": (
            "Newsletters are the highest-trust one-to-many channel for many creators. "
            "A consistent format and a tight subject line set compound open rates over time."
        ),
        "when_use": [
            "You're publishing a regular newsletter.",
            "You have an underused email list.",
        ],
        "when_not_use": [
            "You're building a multi-step automated sequence — use email-sequence (046).",
            "You want a one-time announcement — consider campaign-plan (045) instead.",
        ],
        "prepare": [
            "Theme or topic.",
            "Audience profile.",
            "Voice reference or previous issues.",
        ],
        "how_ai": [
            "1. Confirm theme and audience.",
            "2. Draft the issue with sections and a clear lede.",
            "3. Generate subject-line and preview-text variants.",
            "4. Add plain-text fallback for email clients that strip CSS.",
        ],
        "what_get": [
            "Newsletter copy.",
            "3 subject line variants.",
            "3 preview text variants.",
            "Plain-text fallback.",
        ],
        "next_steps": ["email-sequence (046)", "content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: issue_copy\n"
            "    description: full newsletter text\n"
            "  - key: subject_variants\n"
            "    description: subject line options"
        ),
    },
    "012": {
        "slug": "social-post",
        "title": "Create a Social Post",
        "category": "content",
        "aliases": ["social media post", "linkedin post", "twitter post", "x post", "instagram caption"],
        "triggers": ["write a post", "linkedin post", "tweet", "instagram caption", "social post"],
        "input_types": ["topic", "platform", "voice"],
        "output_types": ["post copy", "hashtag suggestions"],
        "requires": ["topic or hook", "platform (X, LinkedIn, Instagram, etc.)", "voice guide"],
        "produces": ["platform-aware post", "alternative versions", "hashtag suggestions"],
        "related": ["thread-series", "video-hook", "content-repurposing"],
        "playbooks": [],
        "purpose": "Create a single social post adapted to platform, audience, and voice.",
        "what": (
            "Write a platform-aware social post with a strong hook, clear structure, and a soft call to action. "
            "Adapt length and tone to the platform's norms."
        ),
        "why": (
            "Posts that ignore platform norms underperform. The same message must be reframed for X, LinkedIn, Instagram, etc."
        ),
        "when_use": [
            "You're publishing one post.",
            "You're testing an angle quickly.",
        ],
        "when_not_use": [
            "You want a multi-post narrative — use thread-series (013).",
            "You want a carousel — use carousel (014).",
        ],
        "prepare": [
            "Topic or hook.",
            "Platform.",
            "Voice reference.",
        ],
        "how_ai": [
            "1. Confirm platform and audience.",
            "2. Generate a hook (first line / first 7 words).",
            "3. Write the post adapting length and structure.",
            "4. Suggest hashtag or mention conventions.",
            "5. Provide 1–2 alternate versions.",
        ],
        "what_get": [
            "Platform-aware post.",
            "1–2 alternate versions.",
            "Hashtag / mention suggestions.",
        ],
        "next_steps": ["thread-series (013)", "content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: post_copy\n"
            "    description: the social post text\n"
            "  - key: platform\n"
            "    description: target platform"
        ),
    },
    "013": {
        "slug": "thread-series",
        "title": "Create a Thread or Series",
        "category": "content",
        "aliases": ["twitter thread", "x thread", "linkedin carousel as text", "post series", "narrative series"],
        "triggers": ["thread", "x thread", "post series", "carousel as text"],
        "input_types": ["core idea", "platform", "number of posts"],
        "output_types": ["post-by-post outline", "first post variants"],
        "requires": ["core idea", "platform and conventions", "target post count"],
        "produces": ["post-by-post outline", "post 1 hooks", "call-to-action in final post"],
        "related": ["social-post", "carousel", "article-outline"],
        "playbooks": [],
        "purpose": "Turn a single idea into a multi-post thread or series tuned to platform conventions.",
        "what": (
            "Lay out an ordered series of posts that reads as one narrative. "
            "Each post stands alone but the sequence compounds. "
            "First and last posts are emphasized because they drive reach and conversion."
        ),
        "why": (
            "A single post rarely has space to teach or persuade. A series lets a creator deliver value, build trust, and prompt action."
        ),
        "when_use": [
            "You want to teach a short course on a platform.",
            "You have a complex story to tell in segments.",
        ],
        "when_not_use": [
            "You only need one post — use social-post (012).",
            "Your content is slide-driven — use carousel (014).",
        ],
        "prepare": [
            "Core idea.",
            "Target platform.",
            "Number of posts.",
        ],
        "how_ai": [
            "1. Plan the arc (setup → development → payoff).",
            "2. Write a one-line beat per post.",
            "3. Draft post 1 with hook variants.",
            "4. Draft the closing post with CTA.",
            "5. Hand off post bodies for the user to expand.",
        ],
        "what_get": [
            "Post-by-post outline.",
            "Post 1 hook variants.",
            "Closing post with CTA.",
        ],
        "next_steps": ["social-post (012)", "content-repurposing (028)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: series_outline\n"
            "    description: ordered beats per post\n"
            "  - key: post_1_hooks\n"
            "    description: alternative openers"
        ),
    },
    "014": {
        "slug": "carousel",
        "title": "Create a Carousel",
        "category": "content",
        "aliases": ["carousel post", "instagram carousel", "linkedin carousel", "slide post"],
        "triggers": ["carousel", "instagram carousel", "linkedin carousel", "slide post"],
        "input_types": ["core message", "slide count target", "audience"],
        "output_types": ["slide-by-slide outline", "slide copy", "CTA slide"],
        "requires": ["core message", "target slide count", "audience"],
        "produces": ["slide-by-slide outline", "slide text", "CTA slide"],
        "related": ["thread-series", "social-post", "presentation-story"],
        "playbooks": [],
        "purpose": "Plan a slide-by-slide carousel that teaches one idea clearly.",
        "what": (
            "Design a carousel with a hook slide, a teaching arc, and a CTA slide. "
            "Each slide has one idea and one visual cue."
        ),
        "why": (
            "Carousels reward clarity. One idea per slide beats dense text — the format itself teaches users how to read it."
        ),
        "when_use": [
            "You're publishing a teaching post on Instagram or LinkedIn.",
            "You want a downloadable reference asset.",
        ],
        "when_not_use": [
            "You need a multi-post text series — use thread-series (013).",
            "You're presenting live — use presentation-story (019).",
        ],
        "prepare": [
            "Core message.",
            "Target slide count (typically 5–12).",
            "Audience and voice.",
        ],
        "how_ai": [
            "1. Design the arc (hook → problem → insight → steps → CTA).",
            "2. Write one idea per slide.",
            "3. Add visual suggestions per slide (chart, diagram, photo).",
            "4. End with a CTA slide.",
        ],
        "what_get": [
            "Slide-by-slide outline.",
            "Slide copy.",
            "Visual suggestions.",
            "CTA slide.",
        ],
        "next_steps": ["content-quality-review (029)", "content-repurposing (028)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: slides\n"
            "    description: list of slides with text and visual cues"
        ),
    },
    "015": {
        "slug": "short-video-script",
        "title": "Write a Short-Form Video Script",
        "category": "content",
        "aliases": ["reels script", "tiktok script", "shorts script", "short video script"],
        "triggers": ["reels script", "tiktok script", "shorts script", "short video", "vertical video script"],
        "input_types": ["topic", "hook", "platform", "target length"],
        "output_types": ["video script", "shot list", "caption draft"],
        "requires": ["topic", "hook idea", "platform and length (15s/30s/60s/90s)"],
        "produces": ["video script", "shot list", "caption draft", "CTA draft"],
        "related": ["video-hook", "video-storyboard", "social-post"],
        "playbooks": [],
        "purpose": "Write a short-form video script tuned to platform, length, and audience.",
        "what": (
            "Write a video script with the opening hook, the body beats, and the closing CTA. "
            "Include on-screen text, voice-over, and shot direction."
        ),
        "why": (
            "Short video rewards tight structure. A scripted arc beats improvised rambling every time."
        ),
        "when_use": [
            "You're scripting a Reel, TikTok, or Short.",
            "You have a hook idea but not the body.",
        ],
        "when_not_use": [
            "You only need hooks — use video-hook (016).",
            "You're producing a long video — use video-storyboard (017).",
        ],
        "prepare": [
            "Topic and angle.",
            "Target length.",
            "Platform conventions.",
        ],
        "how_ai": [
            "1. Confirm hook, length, platform.",
            "2. Write the arc beats.",
            "3. Add on-screen text, voice-over, and shot notes.",
            "4. Draft the caption.",
        ],
        "what_get": [
            "Video script.",
            "Shot list.",
            "Caption draft.",
            "Suggested next workflow: video-storyboard (017).",
        ],
        "next_steps": ["video-storyboard (017)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: script\n"
            "    description: the video script\n"
            "  - key: shots\n"
            "    description: ordered shot notes"
        ),
    },
    "016": {
        "slug": "video-hook",
        "title": "Generate Video Hooks",
        "category": "content",
        "aliases": ["video hooks", "tiktok hooks", "opening lines for video"],
        "triggers": ["video hook", "opening line", "scroll-stopper", "first 3 seconds"],
        "input_types": ["video topic", "platform", "tone"],
        "output_types": ["hook variants", "rationale per hook"],
        "requires": ["video topic", "platform", "tone"],
        "produces": ["ranked hook variants", "rationale per hook"],
        "related": ["short-video-script", "headline-generation"],
        "playbooks": [],
        "purpose": "Generate and rank opening hooks for short-form video.",
        "what": (
            "Produce multiple opening hooks tailored to platform norms, ranked by likely scroll-stopping power and fit with the topic."
        ),
        "why": (
            "Short video lives or dies in the first 2 seconds. A bank of tested hooks is the single highest-leverage asset a video creator has."
        ),
        "when_use": [
            "You're scripting a Reel / TikTok / Short and want a hook.",
            "Your hooks feel tired.",
        ],
        "when_not_use": [
            "You already have a script — skip this and write the body.",
            "You want a full script — use short-video-script (015).",
        ],
        "prepare": [
            "Video topic.",
            "Platform.",
            "Tone (educational, contrarian, funny, etc.).",
        ],
        "how_ai": [
            "1. Confirm topic and platform.",
            "2. Generate 10–20 hooks across formats (question, stat, story, contrarian).",
            "3. Score each for fit and scroll-stopping.",
            "4. Recommend the top 5 with rationale.",
        ],
        "what_get": [
            "10–20 hook variants.",
            "Top-5 recommendation.",
            "Suggested next workflow: short-video-script (015).",
        ],
        "next_steps": ["short-video-script (015)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: hooks\n"
            "    description: ranked list of hook variants"
        ),
    },
    "017": {
        "slug": "video-storyboard",
        "title": "Create a Video Storyboard",
        "category": "content",
        "aliases": ["storyboard", "shot list", "scene plan"],
        "triggers": ["storyboard", "shot list", "scene plan", "visual plan for video"],
        "input_types": ["script or outline", "platform"],
        "output_types": ["scene-by-scene storyboard", "shot notes"],
        "requires": ["video script or outline", "platform and length"],
        "produces": ["scene-by-scene storyboard", "shot notes", "transition notes"],
        "related": ["short-video-script", "presentation-story"],
        "playbooks": [],
        "purpose": "Translate a video script into scenes, shots, text overlays, and transitions.",
        "what": (
            "Build a storyboard that maps each scene to a shot, an on-screen text overlay, a voice-over line, and a transition."
        ),
        "why": (
            "A storyboard reveals pacing problems before you film. It also makes editing predictable."
        ),
        "when_use": [
            "You have a script and want to film efficiently.",
            "You want to brief an editor.",
        ],
        "when_not_use": [
            "You're scripting for the first time — start with short-video-script (015).",
            "You're producing audio-only — use podcast-interview (018).",
        ],
        "prepare": [
            "Video script or outline.",
            "Platform and length.",
            "Visual style or brand references.",
        ],
        "how_ai": [
            "1. Read the script and identify scenes.",
            "2. Map each scene to a shot, on-screen text, and transition.",
            "3. Flag pacing risks (too slow / too fast).",
            "4. Suggest locations, props, or B-roll.",
        ],
        "what_get": [
            "Scene-by-scene storyboard.",
            "Shot, text, transition notes per scene.",
            "Pacing flags.",
        ],
        "next_steps": ["content-quality-review (029)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: storyboard\n"
            "    description: ordered scenes with shots and transitions"
        ),
    },
    "018": {
        "slug": "podcast-interview",
        "title": "Plan a Podcast Interview",
        "category": "content",
        "aliases": ["podcast prep", "interview questions", "guest interview prep"],
        "triggers": ["podcast prep", "interview questions", "guest interview", "talk show prep"],
        "input_types": ["guest", "topic", "show tone"],
        "output_types": ["interview brief", "questions", "follow-ups"],
        "requires": ["guest profile", "topic", "show tone and audience"],
        "produces": ["interview brief", "questions sequenced by arc", "follow-ups", "call-to-action"],
        "related": ["presentation-story", "short-video-script", "audience-message-map"],
        "playbooks": [],
        "purpose": "Prepare a podcast interview: brief, sequenced questions, follow-ups, and CTA.",
        "what": (
            "Build a one-page brief, an arc of 8–14 questions, follow-ups, and a closing CTA — all in service of an engaging interview that serves the listener."
        ),
        "why": (
            "Most podcast interviews meander. A pre-built arc and follow-ups keep the conversation on track without feeling scripted."
        ),
        "when_use": [
            "You're hosting a guest.",
            "You're preparing to be interviewed.",
        ],
        "when_not_use": [
            "You're running an internal team meeting — use meeting-agenda (078).",
            "You're speaking without an audience Q&A — use presentation-story (019).",
        ],
        "prepare": [
            "Guest profile and bio.",
            "Topic and key angles.",
            "Show tone.",
        ],
        "how_ai": [
            "1. Confirm tone and audience.",
            "2. Draft an interview brief (5 bullets).",
            "3. Sequence 8–14 questions by arc.",
            "4. Add follow-ups and a closing CTA.",
        ],
        "what_get": [
            "Interview brief.",
            "Sequenced questions.",
            "Follow-ups.",
            "Closing CTA.",
        ],
        "next_steps": ["meeting-notes (079)", "content-repurposing (028)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: interview_brief\n"
            "    description: the brief and question arc\n"
            "  - key: follow_ups\n"
            "    description: list of follow-up questions"
        ),
    },
    "019": {
        "slug": "presentation-story",
        "title": "Build a Presentation Narrative",
        "category": "content",
        "aliases": ["keynote structure", "talk narrative", "pitch deck story"],
        "triggers": ["presentation", "keynote", "talk structure", "pitch deck story"],
        "input_types": ["topic", "audience", "length"],
        "output_types": ["narrative arc", "section beats", "opening and closing"],
        "requires": ["topic", "audience profile", "talk length"],
        "produces": ["narrative arc", "section beats", "opening and closing"],
        "related": ["presentation-story", "storytelling", "video-storyboard"],
        "playbooks": [],
        "purpose": "Build the narrative structure for a presentation or talk.",
        "what": (
            "Design the narrative arc: opening hook, tension, payoff, call to action. "
            "Lay out section-by-section beats the speaker can deliver."
        ),
        "why": (
            "Presentations fail when they recite information instead of telling a story. A clear arc gives the speaker something to land."
        ),
        "when_use": [
            "You're preparing a talk or pitch.",
            "Your deck reads like a report and you need a story.",
        ],
        "when_not_use": [
            "You only need the visual side — use video-storyboard (017).",
            "You're leading a meeting, not a presentation — use meeting-agenda (078).",
        ],
        "prepare": [
            "Topic and audience.",
            "Length.",
            "One-line core message.",
        ],
        "how_ai": [
            "1. Confirm audience and length.",
            "2. Draft the narrative arc.",
            "3. Lay out section beats.",
            "4. Write the opening hook and the closing call to action.",
        ],
        "what_get": [
            "Narrative arc.",
            "Section beats.",
            "Opening and closing copy.",
        ],
        "next_steps": ["video-storyboard (017)", "presentation-story → storytelling (024)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: arc\n"
            "    description: narrative arc summary\n"
            "  - key: section_beats\n"
            "    description: ordered beats per section"
        ),
    },
    "020": {
        "slug": "headline-generation",
        "title": "Generate Headlines",
        "category": "content",
        "aliases": ["headlines", "titles", "subject lines", "headline ideas"],
        "triggers": ["headline", "title ideas", "subject line", "click-worthy title"],
        "input_types": ["content summary", "audience", "channel"],
        "output_types": ["headline variants", "rationale"],
        "requires": ["content summary or angle", "audience", "channel"],
        "produces": ["ranked headline variants", "rationale per headline"],
        "related": ["video-hook", "social-post", "article-outline"],
        "playbooks": [],
        "purpose": "Generate and rank headlines for articles, posts, and subject lines.",
        "what": (
            "Produce multiple headline variants across styles (curiosity, benefit, contrarian, how-to, numeric). "
            "Rank them and explain why each should or shouldn't be picked."
        ),
        "why": (
            "The headline is the most leveraged sentence in any piece. Even a great article can be flattened by a weak title."
        ),
        "when_use": [
            "You're publishing an article, post, or email and need a title.",
            "You want to A/B test multiple options.",
        ],
        "when_not_use": [
            "You're writing a full article — start with article-outline (006).",
        ],
        "prepare": [
            "Content summary.",
            "Audience.",
            "Channel (search, social, email).",
        ],
        "how_ai": [
            "1. Confirm summary, audience, and channel.",
            "2. Generate 15+ variants across styles.",
            "3. Rank the top 5 with rationale.",
            "4. Note channels where each variant fits best.",
        ],
        "what_get": [
            "15+ headline variants.",
            "Top-5 recommendation with rationale.",
            "Channel notes per headline.",
        ],
        "next_steps": ["article-outline (006)", "social-post (012)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: headlines\n"
            "    description: ranked headline variants\n"
            "  - key: chosen_headline\n"
            "    description: user-selected headline"
        ),
    },
    "021": {
        "slug": "cta-design",
        "title": "Design Calls to Action",
        "category": "content",
        "aliases": ["call to action", "cta copy", "cta design", "next action prompt"],
        "triggers": ["call to action", "what should they do next", "cta", "next button"],
        "input_types": ["context (article, email, post)", "intended action", "audience"],
        "output_types": ["CTA variants", "rationale"],
        "requires": ["context", "intended action", "audience"],
        "produces": ["CTA variants tuned to context", "rationale", "placement suggestions"],
        "related": ["social-post", "newsletter", "email-sequence"],
        "playbooks": [],
        "purpose": "Design context-appropriate calls to action that move readers to the next step.",
        "what": (
            "Generate CTA variants tuned to context (article, email, post, landing page). "
            "Include button text, micro-copy, and placement suggestions."
        ),
        "why": (
            "Even engaged readers stall without a clear next step. A weak CTA is the most common reason content under-converts."
        ),
        "when_use": [
            "You're publishing any content that needs the reader to act.",
            "Your current CTAs are bland or generic.",
        ],
        "when_not_use": [
            "You're building a full landing page — use sales-page (043).",
            "You're building an automated sequence — use email-sequence (046).",
        ],
        "prepare": [
            "Context (where the CTA lives).",
            "Intended action.",
            "Audience.",
        ],
        "how_ai": [
            "1. Confirm context and intended action.",
            "2. Generate CTA variants across tones.",
            "3. Recommend placement and micro-copy.",
            "4. Suggest a test plan (A/B variant ideas).",
        ],
        "what_get": [
            "CTA variants.",
            "Placement suggestions.",
            "Test plan.",
        ],
        "next_steps": ["content-quality-review (029)", "email-sequence (046)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: cta_variants\n"
            "    description: CTA options\n"
            "  - key: placement\n"
            "    description: placement suggestions"
        ),
    },
    "022": {
        "slug": "faq-creation",
        "title": "Create FAQs",
        "category": "content",
        "aliases": ["faq", "frequently asked questions", "qa page", "questions and answers"],
        "triggers": ["faq", "questions and answers", "make a faq", "common questions"],
        "input_types": ["product or service", "audience", "existing questions"],
        "output_types": ["FAQ list", "categorized questions"],
        "requires": ["product or service description", "audience", "any existing customer questions"],
        "produces": ["categorized FAQ", "short-form answers", "suggested long-form articles"],
        "related": ["customer-feedback-analysis", "content-repurposing"],
        "playbooks": [],
        "purpose": "Convert product, service, or policy information into an FAQ for a chosen audience.",
        "what": (
            "Draft an FAQ grouped by category, with concise answers and pointers to long-form articles where useful."
        ),
        "why": (
            "An FAQ catches the most common support questions, removes friction before conversion, and improves SEO on long-tail queries."
        ),
        "when_use": [
            "You're launching a product or service.",
            "Your support team keeps answering the same questions.",
            "You want a public \"common questions\" page.",
        ],
        "when_not_use": [
            "You're responding to specific public comments — use comment-response (026).",
            "You're capturing real customer questions before launching — start with customer-interview (032).",
        ],
        "prepare": [
            "Product or service summary.",
            "Existing questions or support tickets.",
            "Audience.",
        ],
        "how_ai": [
            "1. Read product summary and any supplied questions.",
            "2. Group by category.",
            "3. Write concise answers and link to long-form where useful.",
            "4. Flag questions that need a domain expert.",
        ],
        "what_get": [
            "Categorized FAQ.",
            "Short-form answers.",
            "Suggestions for follow-up articles.",
        ],
        "next_steps": ["article-outline (006)", "sales-page (043)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: faq\n"
            "    description: categorized question list with answers"
        ),
    },
    "023": {
        "slug": "brand-voice-guide",
        "title": "Create a Brand Voice Guide",
        "category": "content",
        "aliases": ["voice guide", "tone of voice", "writing style", "brand voice"],
        "triggers": ["voice guide", "tone of voice", "writing style", "brand voice"],
        "input_types": ["brand description", "audience", "samples"],
        "output_types": ["voice guide", "do/don't list", "examples"],
        "requires": ["brand summary", "audience", "any existing sample text"],
        "produces": ["voice guide", "do and don't list", "sample paragraphs"],
        "related": ["content-pillar-design", "content-quality-review"],
        "playbooks": [],
        "purpose": "Document a repeatable writing voice others can follow.",
        "what": (
            "Define voice attributes (3–5), a do-and-don't list, and sample paragraphs that show the voice in action."
        ),
        "why": (
            "Without a documented voice, every contributor reinvents the brand and content drifts. A voice guide eliminates arguments about tone."
        ),
        "when_use": [
            "You're scaling content production across people or tools.",
            "Your content sounds inconsistent.",
        ],
        "when_not_use": [
            "You're writing one piece — use content-editing (009) directly.",
        ],
        "prepare": [
            "Brand summary or positioning.",
            "Audience.",
            "Optional: existing sample text that you like.",
        ],
        "how_ai": [
            "1. Read the brand summary and samples.",
            "2. Name 3–5 voice attributes with one-line definitions.",
            "3. Write do-and-don't examples per attribute.",
            "4. Produce two sample paragraphs in the voice.",
        ],
        "what_get": [
            "Voice attributes.",
            "Do-and-don't list.",
            "Sample paragraphs.",
        ],
        "next_steps": ["content-quality-review (029)", "content-pillar-design (002)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: voice_attributes\n"
            "    description: 3–5 attributes with definitions\n"
            "  - key: examples\n"
            "    description: do/don't examples and sample paragraphs"
        ),
    },
    "024": {
        "slug": "storytelling",
        "title": "Develop a Story",
        "category": "content",
        "aliases": ["story arc", "narrative", "story structure"],
        "triggers": ["story arc", "narrative", "tell a story", "story structure"],
        "input_types": ["raw events or facts", "audience", "story goal"],
        "output_types": ["story outline", "drafted story"],
        "requires": ["raw events or facts", "audience", "story goal (inspire, teach, persuade, explain)"],
        "produces": ["structured story", "drafted story", "moral or takeaway"],
        "related": ["case-study", "presentation-story", "storytelling"],
        "playbooks": [],
        "purpose": "Shape facts or experience into a coherent story with an arc and takeaway.",
        "what": (
            "Convert raw events or facts into a structured story with a clear setup, conflict, resolution, and takeaway. "
            "Return both an outline and a draft."
        ),
        "why": (
            "Facts alone don't stick. A story makes the meaning memorable and the audience more likely to act on it."
        ),
        "when_use": [
            "You want to land a key idea in a presentation or article.",
            "You're turning an experience into content.",
        ],
        "when_not_use": [
            "You're documenting a customer outcome — use case-study (025).",
            "You're scripting a talk — use presentation-story (019).",
        ],
        "prepare": [
            "Raw events or facts.",
            "Audience.",
            "Story goal.",
        ],
        "how_ai": [
            "1. Identify the protagonist, conflict, and turning point.",
            "2. Build a 3-act arc.",
            "3. Draft the story in the chosen voice.",
            "4. State the takeaway plainly.",
        ],
        "what_get": [
            "Story outline.",
            "Drafted story.",
            "One-line takeaway.",
        ],
        "next_steps": ["article-draft (007)", "case-study (025)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: story_outline\n"
            "    description: arc summary\n"
            "  - key: story_draft\n"
            "    description: drafted story text"
        ),
    },
    "025": {
        "slug": "case-study",
        "title": "Write a Case Study",
        "category": "content",
        "aliases": ["customer story", "success story", "case write-up"],
        "triggers": ["case study", "customer story", "success story", "write up a project"],
        "input_types": ["project or customer outcome", "metrics", "testimonial"],
        "output_types": ["case study"],
        "requires": ["project description", "outcome metrics", "optional customer testimonial"],
        "produces": ["structured case study (challenge, approach, result, takeaways)"],
        "related": ["storytelling", "marketing-funnel", "sales-page"],
        "playbooks": [],
        "purpose": "Turn a project or customer outcome into a credible case study.",
        "what": (
            "Convert a project description into a structured case study that includes the customer's challenge, the approach, the result (with metrics), and the takeaways. "
            "Quote the customer where appropriate."
        ),
        "why": (
            "B2B buyers trust peer outcomes more than vendor claims. A clear case study is one of the highest-ROI sales assets you can produce."
        ),
        "when_use": [
            "You finished a successful project with measurable outcomes.",
            "Your sales team needs an asset for late-stage prospects.",
        ],
        "when_not_use": [
            "You're documenting your own learning — use self-review (088).",
            "You're capturing results from a customer interview — use customer-interview (032).",
        ],
        "prepare": [
            "Project description.",
            "Outcome metrics or changes.",
            "Optional: customer testimonial.",
        ],
        "how_ai": [
            "1. Identify the customer's challenge in one sentence.",
            "2. Describe the approach in concrete steps.",
            "3. Show results with before/after metrics.",
            "4. Add customer quote and a takeaways section.",
        ],
        "what_get": [
            "Case study (challenge → approach → result → takeaways).",
            "Pull-quote highlights.",
            "Suggested next workflow: sales-page (043).",
        ],
        "next_steps": ["sales-page (043)", "marketing-funnel (044)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: case_study\n"
            "    description: structured case study text\n"
            "  - key: metrics\n"
            "    description: before/after metrics"
        ),
    },
    "026": {
        "slug": "comment-response",
        "title": "Draft Comment Responses",
        "category": "content",
        "aliases": ["reply", "comment reply", "public response"],
        "triggers": ["reply to comment", "respond publicly", "draft a reply", "comment response"],
        "input_types": ["comment text", "tone", "context"],
        "output_types": ["response variant(s)"],
        "requires": ["comment or question", "tone (warm, neutral, firm)", "context (post, video, etc.)"],
        "produces": ["response variants", "rationale per variant"],
        "related": ["faq-creation", "social-post", "brand-voice-guide"],
        "playbooks": [],
        "purpose": "Draft useful replies to public comments or questions.",
        "what": (
            "Draft one to three response variants calibrated to tone and context. "
            "Flag comments that should escalate or be ignored."
        ),
        "why": (
            "Public replies shape how others see your brand. A polite, useful reply builds trust; a defensive one erodes it."
        ),
        "when_use": [
            "You're responding to comments on posts or videos.",
            "You're facing a sensitive public question.",
        ],
        "when_not_use": [
            "You're writing a private email — use newsletter (011) or email-sequence (046).",
            "The question needs legal or compliance review — escalate.",
        ],
        "prepare": [
            "Comment text.",
            "Tone.",
            "Context (post, article, etc.).",
        ],
        "how_ai": [
            "1. Classify the comment (question, complaint, agreement, troll).",
            "2. Recommend a response strategy.",
            "3. Draft 1–3 variants.",
            "4. Flag comments that should be escalated.",
        ],
        "what_get": [
            "Response variants.",
            "Strategy per variant.",
            "Escalation flag if relevant.",
        ],
        "next_steps": ["faq-creation (022)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: responses\n"
            "    description: response variants"
        ),
    },
    "027": {
        "slug": "translation-localization",
        "title": "Translate and Localize",
        "category": "content",
        "aliases": ["translate", "localization", "localize", "i18n"],
        "triggers": ["translate", "localize", "i18n", "convert to spanish", "french version"],
        "input_types": ["source content", "target language", "audience"],
        "output_types": ["translated content", "localization notes"],
        "requires": ["source content", "target language", "audience context"],
        "produces": ["localized translation", "cultural adaptation notes"],
        "related": ["article-rewrite", "content-editing", "brand-voice-guide"],
        "playbooks": [],
        "purpose": "Translate content while adapting tone, context, and terminology.",
        "what": (
            "Produce a localized version of the content for the target language and audience, with notes on cultural adaptation choices."
        ),
        "why": (
            "Direct translation loses nuance. Localization preserves meaning and adapts idioms, examples, and references."
        ),
        "when_use": [
            "You're publishing content in a new market.",
            "You're adapting a campaign for a regional audience.",
        ],
        "when_not_use": [
            "You're adapting for a different channel — use content-repurposing (028).",
            "You're rewriting in the same language — use article-rewrite (008).",
        ],
        "prepare": [
            "Source content.",
            "Target language(s).",
            "Audience context (region, age, expertise).",
        ],
        "how_ai": [
            "1. Translate.",
            "2. Adapt idioms and cultural references.",
            "3. Preserve technical terms and brand names.",
            "4. Add adaptation notes.",
        ],
        "what_get": [
            "Localized version.",
            "Adaptation notes.",
            "Glossary of preserved terms.",
        ],
        "next_steps": ["content-quality-review (029)", "content-repurposing (028)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: localized_text\n"
            "    description: translated and adapted text\n"
            "  - key: adaptation_notes\n"
            "    description: list of notable choices"
        ),
    },
    "028": {
        "slug": "content-repurposing",
        "title": "Repurpose Content",
        "category": "content",
        "aliases": ["repurpose", "repurpose content", "adapt for another channel", "cross-post"],
        "triggers": ["repurpose", "adapt for twitter", "convert to carousel", "republish as newsletter"],
        "input_types": ["source content", "target channels"],
        "output_types": ["channel-specific adaptations"],
        "requires": ["source content", "target channels", "voice guide"],
        "produces": ["one adaptation per target channel", "publishing order recommendation"],
        "related": ["social-post", "thread-series", "short-video-script", "newsletter"],
        "playbooks": ["create-high-quality-content"],
        "purpose": "Convert a source asset into multiple channel-specific formats.",
        "what": (
            "Take the source asset and produce channel-specific adaptations that respect platform norms, "
            "returning one artifact per target channel plus a publishing order recommendation."
        ),
        "why": (
            "Most content under-leverages its source asset. Repurposing lets a single research effort drive weeks of distribution."
        ),
        "when_use": [
            "You finished a long article or talk and want more reach.",
            "You publish on multiple channels but produce only one source format.",
        ],
        "when_not_use": [
            "You're translating — use translation-localization (027).",
            "You're splitting a single idea into a series — use thread-series (013).",
        ],
        "prepare": [
            "Source content.",
            "Target channels.",
            "Voice guide.",
        ],
        "how_ai": [
            "1. Read the source.",
            "2. For each channel, design the adaptation respecting norms.",
            "3. Output each adaptation as a standalone artifact.",
            "4. Recommend publishing order.",
        ],
        "what_get": [
            "Per-channel adaptations.",
            "Publishing order recommendation.",
            "Channel-specific hashtags / mentions.",
        ],
        "next_steps": ["content-quality-review (029)", "content-calendar (004)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: adaptations\n"
            "    description: list of channel-specific adaptations\n"
            "  - key: publish_order\n"
            "    description: recommended publish order"
        ),
    },
    "029": {
        "slug": "content-quality-review",
        "title": "Review Content Quality",
        "category": "content",
        "aliases": ["content review", "qa", "quality check", "editorial review"],
        "triggers": ["review this content", "is this good", "qa the draft", "quality check"],
        "input_types": ["content", "criteria"],
        "output_types": ["review report", "improvement suggestions"],
        "requires": ["content", "review criteria (clarity, accuracy, voice, accessibility)"],
        "produces": ["review report", "severity-tagged issues", "improvement suggestions"],
        "related": ["content-editing", "article-rewrite", "fact-check"],
        "playbooks": [],
        "purpose": "Audit content against a defined quality rubric.",
        "what": (
            "Run a multi-axis review (clarity, structure, voice, accuracy, accessibility). "
            "Return a structured report with severity tags and concrete improvement suggestions."
        ),
        "why": (
            "Most publishing regret comes from skipping review. A repeatable rubric catches the issues the author is blind to."
        ),
        "when_use": [
            "You're publishing an important piece.",
            "You're onboarding a new editor.",
        ],
        "when_not_use": [
            "You're polishing prose — use content-editing (009).",
            "You want to change direction — use article-rewrite (008).",
        ],
        "prepare": [
            "Content.",
            "Review criteria.",
            "Target audience.",
        ],
        "how_ai": [
            "1. Confirm criteria.",
            "2. Run each axis.",
            "3. Tag issues by severity (blocker, should-fix, nice-to-have).",
            "4. Recommend concrete edits.",
        ],
        "what_get": [
            "Review report.",
            "Severity-tagged issues.",
            "Concrete improvement suggestions.",
        ],
        "next_steps": ["content-editing (009)", "article-rewrite (008)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: review_report\n"
            "    description: structured review with severity tags\n"
            "  - key: suggestions\n"
            "    description: list of concrete edits"
        ),
    },
    # ---------------------------------------------------------------- 02-business 030-053
    "030": {
        "slug": "market-research",
        "title": "Plan Market Research",
        "category": "business",
        "aliases": ["market research", "research plan", "market intel"],
        "triggers": ["research the market", "market research plan", "industry overview", "size the market"],
        "input_types": ["market", "research goal", "existing knowledge"],
        "output_types": ["research plan", "key questions", "source list"],
        "requires": ["market or industry", "research goal", "existing knowledge gaps"],
        "optional_inputs": ["timeline", "budget", "audience for the research output"],
        "produces": ["research plan", "key questions", "suggested sources"],
        "related": ["research-plan", "competitor-analysis", "customer-interview"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Design a focused market-research approach.",
        "what": (
            "Build a research plan that names the questions, the methods, the sources, and the timeline. "
            "It clarifies what is in scope and what to skip."
        ),
        "why": (
            "Most market research drowns the reader in facts and skips the questions. A plan makes the research answer real decisions."
        ),
        "when_use": [
            "You're entering a new market or category.",
            "A leadership question needs evidence-based support.",
            "A consultant or agency needs a clear brief.",
        ],
        "when_not_use": [
            "You need quick competitive intel — use competitor-analysis (034).",
            "You need to talk to customers — use customer-interview (032).",
        ],
        "prepare": [
            "Market or industry.",
            "Decision the research must support.",
            "Existing knowledge and known gaps.",
        ],
        "how_ai": [
            "1. Confirm decision and audience.",
            "2. List 5–9 research questions ranked by impact.",
            "3. Pick methods (web research, interviews, surveys, datasets).",
            "4. Suggest primary sources.",
            "5. Output a one-page research plan.",
        ],
        "what_get": [
            "One-page research plan.",
            "Ranked research questions.",
            "Suggested sources.",
            "Next-workflow suggestion: web-research-synthesis (057).",
        ],
        "next_steps": ["web-research-synthesis (057)", "customer-interview (032)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: research_plan\n"
            "    description: ranked questions, methods, sources\n"
            "  - key: decision_context\n"
            "    description: the decision the research must inform"
        ),
    },
    "031": {
        "slug": "customer-persona",
        "title": "Define Target Customer",
        "category": "business",
        "aliases": ["persona", "icp", "ideal customer profile", "buyer persona"],
        "triggers": ["who is my customer", "icp", "target persona", "buyer persona"],
        "input_types": ["product or service", "existing customer signals", "market"],
        "output_types": ["persona card", "jobs-to-be-done"],
        "requires": ["product or service summary", "any existing customer signals", "target market"],
        "optional_inputs": ["competitors", "pricing", "sales notes"],
        "produces": ["persona card", "jobs-to-be-done", "anti-persona"],
        "related": ["customer-interview", "value-proposition", "competitor-analysis"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Define a target customer based on jobs, context, pains, and desired outcomes.",
        "what": (
            "Produce a persona card with jobs-to-be-done, context, pains, gains, and an anti-persona. "
            "The card is concrete enough to brief a copywriter or sales team."
        ),
        "why": (
            "Marketing fails when it targets \"everyone\". A persona makes it possible to choose channels, messages, and trade-offs."
        ),
        "when_use": [
            "You're targeting a new segment.",
            "Your messaging gets no traction.",
        ],
        "when_not_use": [
            "You have rich qualitative interviews — synthesize them first with customer-feedback-analysis (033).",
        ],
        "prepare": [
            "Product or service summary.",
            "Existing customer signals (sales notes, support tickets, reviews).",
            "Market scope.",
        ],
        "how_ai": [
            "1. Confirm product and market.",
            "2. Build a persona card (demographics, jobs, pains, gains).",
            "3. Add an anti-persona.",
            "4. Verify against existing signals.",
        ],
        "what_get": [
            "Persona card.",
            "Jobs-to-be-done list.",
            "Anti-persona.",
            "Next-workflow suggestion: customer-interview (032).",
        ],
        "next_steps": ["customer-interview (032)", "value-proposition (036)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: persona\n"
            "    description: persona card with jobs, pains, gains\n"
            "  - key: anti_persona\n"
            "    description: who is not the target"
        ),
    },
    "032": {
        "slug": "customer-interview",
        "title": "Design Customer Interviews",
        "category": "business",
        "aliases": ["interview script", "user interview", "discovery call", "interview questions"],
        "triggers": ["interview questions", "user research script", "discovery interview", "research interview"],
        "input_types": ["research goal", "persona", "topic"],
        "output_types": ["interview script", "consent note"],
        "requires": ["research goal", "persona or segment", "topic boundaries"],
        "optional_inputs": ["incentive", "interview duration"],
        "produces": ["interview script (8–12 questions)", "consent note", "follow-up plan"],
        "related": ["customer-persona", "customer-feedback-analysis", "research-plan"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Create non-leading customer interview questions.",
        "what": (
            "Produce an interview script with an opener, behavior-anchored questions, follow-ups, "
            "and a closing note. Include the consent line and a recap plan."
        ),
        "why": (
            "Leading questions confirm what you already believe. Behavior-anchored questions reveal what people actually do."
        ),
        "when_use": [
            "You're validating a problem or solution.",
            "You're trying to understand how customers decide.",
        ],
        "when_not_use": [
            "You have lots of interview transcripts and need synthesis — use customer-feedback-analysis (033).",
        ],
        "prepare": [
            "Research goal.",
            "Persona or segment.",
            "Topic boundaries.",
        ],
        "how_ai": [
            "1. Confirm goal and persona.",
            "2. Draft an opener that does not lead.",
            "3. Build 8–12 behavior-anchored questions.",
            "4. Add follow-ups and a wrap-up.",
            "5. Include consent note.",
        ],
        "what_get": [
            "Interview script.",
            "Consent line.",
            "Wrap-up plan.",
        ],
        "next_steps": ["customer-feedback-analysis (033)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: interview_script\n"
            "    description: ordered interview questions\n"
            "  - key: consent_note\n"
            "    description: consent statement"
        ),
    },
    "033": {
        "slug": "customer-feedback-analysis",
        "title": "Analyze Customer Feedback",
        "category": "business",
        "aliases": ["feedback analysis", "thematic analysis", "review analysis"],
        "triggers": ["analyze feedback", "thematic analysis", "review themes", "feedback summary"],
        "input_types": ["feedback transcripts or texts"],
        "output_types": ["thematic report", "quotes per theme"],
        "requires": ["feedback corpus (transcripts, reviews, tickets)"],
        "optional_inputs": ["research goal", "segments"],
        "produces": ["thematic report", "quotes per theme", "recommendations"],
        "related": ["customer-interview", "customer-persona"],
        "playbooks": [],
        "purpose": "Classify feedback and identify recurring patterns.",
        "what": (
            "Group feedback into themes, count frequency, surface representative quotes, "
            "and propose 2–3 actions."
        ),
        "why": (
            "Without structure, customer feedback is just complaining. With themes and counts, it becomes a roadmap input."
        ),
        "when_use": [
            "You have 5+ interviews or 50+ tickets.",
            "You need to brief product or marketing on what customers say.",
        ],
        "when_not_use": [
            "You have only one interview — read it directly with customer-interview (032).",
        ],
        "prepare": [
            "Feedback corpus.",
            "Optional: research goal or segmentation.",
        ],
        "how_ai": [
            "1. Read the corpus.",
            "2. Code themes.",
            "3. Count frequency and surface quotes.",
            "4. Recommend 2–3 actions.",
        ],
        "what_get": [
            "Thematic report.",
            "Quotes per theme.",
            "Action recommendations.",
        ],
        "next_steps": ["customer-persona (031)", "positioning (035)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: themes\n"
            "    description: themes with counts and quotes\n"
            "  - key: recommendations\n"
            "    description: 2–3 prioritized actions"
        ),
    },
    "034": {
        "slug": "competitor-analysis",
        "title": "Analyze Competitors",
        "category": "business",
        "aliases": ["competitive analysis", "competition", "competitors"],
        "triggers": ["competitors", "competitive landscape", "who competes with me", "competitor analysis"],
        "input_types": ["offer", "customer", "competitor list"],
        "output_types": ["landscape map", "comparison table", "gaps"],
        "requires": ["offer", "customer", "market", "known competitors"],
        "optional_inputs": ["competitor URLs", "positioning notes"],
        "produces": ["landscape map", "comparison table", "gap analysis"],
        "related": ["positioning", "customer-persona", "value-proposition"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Compare direct, indirect, and substitute competitors.",
        "what": (
            "Build a competitor landscape using a comparison table (audience, features, pricing, messaging) "
            "and a gaps section that highlights whitespace."
        ),
        "why": (
            "Defensibility is built on contrast. A clear comparison surfaces differentiation that an internal team takes for granted."
        ),
        "when_use": [
            "You're entering a new market.",
            "Your messaging feels undifferentiated.",
        ],
        "when_not_use": [
            "You need continuous tracking — set up a recurring process with marketing-funnel (044).",
        ],
        "prepare": [
            "Offer summary.",
            "Customer profile.",
            "Known competitor list or URLs.",
        ],
        "how_ai": [
            "1. Confirm offer and customer.",
            "2. Build a comparison table.",
            "3. Map positioning quadrants.",
            "4. Identify gaps and whitespace.",
        ],
        "what_get": [
            "Comparison table.",
            "Positioning quadrants.",
            "Whitespace and gap notes.",
        ],
        "next_steps": ["positioning (035)", "value-proposition (036)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: comparison_table\n"
            "    description: competitor matrix\n"
            "  - key: whitespace\n"
            "    description: gaps and white-space opportunities"
        ),
    },
    "035": {
        "slug": "positioning",
        "title": "Create Positioning",
        "category": "business",
        "aliases": ["positioning statement", "market position", "positioning canvas"],
        "triggers": ["positioning", "where do we sit", "market position"],
        "input_types": ["customer", "competitors", "offer"],
        "output_types": ["positioning statement", "positioning canvas"],
        "requires": ["customer", "competitor landscape", "offer"],
        "optional_inputs": ["current positioning"],
        "produces": ["positioning statement", "positioning canvas", "alternative positions"],
        "related": ["value-proposition", "competitor-analysis", "brand-voice-guide"],
        "playbooks": [],
        "purpose": "Write a focused positioning statement.",
        "what": (
            "Produce a positioning statement that names the target customer, the alternative, "
            "the value, and the reason to believe. Provide one alternative position."
        ),
        "why": (
            "Positioning determines every downstream choice — pricing, channels, messages. Vague positioning leaks revenue."
        ),
        "when_use": [
            "You're launching a new product or refreshing an old one.",
            "Your team disagrees on who you are for.",
        ],
        "when_not_use": [
            "You only need a tag-line — use headline-generation (020).",
            "You're writing a sales page — use sales-page (043).",
        ],
        "prepare": [
            "Customer profile.",
            "Competitor landscape.",
            "Offer summary.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Draft a positioning statement.",
            "3. Generate one alternative position.",
            "4. Test against competitor language.",
        ],
        "what_get": [
            "Positioning statement.",
            "Alternative position.",
            "Sanity check against competitors.",
        ],
        "next_steps": ["value-proposition (036)", "sales-page (043)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: positioning_statement\n"
            "    description: the chosen position\n"
            "  - key: alternative_position\n"
            "    description: backup position"
        ),
    },
    "036": {
        "slug": "value-proposition",
        "title": "Create a Value Proposition",
        "category": "business",
        "aliases": ["value prop", "vp", "value proposition canvas"],
        "triggers": ["value proposition", "value prop", "why us", "benefits"],
        "input_types": ["offer", "customer", "pains and gains"],
        "output_types": ["value proposition canvas", "headline value prop"],
        "requires": ["offer", "customer profile", "pains and gains"],
        "optional_inputs": ["existing value prop"],
        "produces": ["value proposition canvas", "headline value prop", "supporting statements"],
        "related": ["positioning", "sales-page", "customer-persona"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Map customer jobs, pains, gains, and offer value.",
        "what": (
            "Produce a value proposition canvas (jobs, pains, gains; products, pain relievers, gain creators) "
            "and a single headline that combines customer, value, and differentiator."
        ),
        "why": (
            "A value prop is more than a tagline — it is a structured promise that matches what the customer wants."
        ),
        "when_use": [
            "You're launching a new product.",
            "Your landing pages under-convert.",
        ],
        "when_not_use": [
            "You only need a tagline — use headline-generation (020).",
        ],
        "prepare": [
            "Offer summary.",
            "Customer pains and gains.",
        ],
        "how_ai": [
            "1. Build the canvas.",
            "2. Draft a headline value prop.",
            "3. Add supporting statements.",
            "4. Sanity-check against the persona.",
        ],
        "what_get": [
            "Value proposition canvas.",
            "Headline value prop.",
            "Supporting statements.",
        ],
        "next_steps": ["sales-page (043)", "mvp-scope (039)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: value_prop_canvas\n"
            "    description: jobs/pains/gains map\n"
            "  - key: headline_value_prop\n"
            "    description: headline statement"
        ),
    },
    "037": {
        "slug": "offer-design",
        "title": "Design an Offer",
        "category": "business",
        "aliases": ["offer", "product offer", "service offer", "package"],
        "triggers": ["design an offer", "package", "what to sell", "bundling"],
        "input_types": ["offer", "audience", "pricing constraints"],
        "output_types": ["offer card", "pricing tiers"],
        "requires": ["underlying product or service", "audience", "pricing constraints"],
        "optional_inputs": ["competitor pricing"],
        "produces": ["offer card", "pricing tiers", "guarantee or risk-reversal"],
        "related": ["pricing-strategy", "value-proposition", "sales-page"],
        "playbooks": [],
        "purpose": "Package a service or product into a clear offer.",
        "what": (
            "Combine features, deliverables, pricing tiers, bonuses, and a guarantee into a single offer card. "
            "The card should be readable in 60 seconds."
        ),
        "why": (
            "Most offers underperform because they bury the outcome. A well-designed offer aligns price, value, and risk reversal."
        ),
        "when_use": [
            "You're launching a paid product or service.",
            "Your conversion is low even though traffic is good.",
        ],
        "when_not_use": [
            "You only need pricing logic — use pricing-strategy (041).",
        ],
        "prepare": [
            "Product or service.",
            "Audience.",
            "Pricing constraints.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build a tiered offer card.",
            "3. Add bonuses and guarantee.",
            "4. Suggest price-test variations.",
        ],
        "what_get": [
            "Tiered offer card.",
            "Bonuses and guarantee.",
            "Price-test variations.",
        ],
        "next_steps": ["pricing-strategy (041)", "sales-page (043)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: offer_card\n"
            "    description: tiered offer summary\n"
            "  - key: guarantee\n"
            "    description: risk-reversal options"
        ),
    },
    "038": {
        "slug": "product-idea-validation",
        "title": "Validate a Product Idea",
        "category": "business",
        "aliases": ["idea validation", "validate idea", "test demand"],
        "triggers": ["validate my idea", "test demand", "is this idea worth it", "validate a product"],
        "input_types": ["idea", "customer", "market"],
        "output_types": ["validation plan", "experiments"],
        "requires": ["idea summary", "customer profile", "market context"],
        "optional_inputs": ["budget", "timeline"],
        "produces": ["validation plan", "experiment designs", "success criteria"],
        "related": ["customer-interview", "pricing-strategy", "mvp-scope"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Design experiments to test demand and desirability.",
        "what": (
            "Plan 2–4 low-cost experiments (interviews, smoke-tests, prototypes, landing pages) "
            "with explicit success criteria and decision rules."
        ),
        "why": (
            "Most products fail from not from engineering but from lack of demand. Cheap experiments reduce risk before heavy investment."
        ),
        "when_use": [
            "You have a new product or feature concept.",
            "You're deciding between two directions.",
        ],
        "when_not_use": [
            "You're scoping the build — use mvp-scope (039) after validation.",
        ],
        "prepare": [
            "Idea summary.",
            "Customer profile.",
            "Market context.",
        ],
        "how_ai": [
            "1. Confirm idea and riskiest assumption.",
            "2. Design 2–4 experiments with success criteria.",
            "3. Sequence cheap before expensive.",
            "4. Define go / no-go rules.",
        ],
        "what_get": [
            "Validation plan.",
            "Experiments.",
            "Go / no-go rules.",
        ],
        "next_steps": ["mvp-scope (039)", "pricing-strategy (041)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: validation_plan\n"
            "    description: ordered experiments\n"
            "  - key: go_no_go_rules\n"
            "    description: decision thresholds"
        ),
    },
    "039": {
        "slug": "mvp-scope",
        "title": "Define MVP Scope",
        "category": "business",
        "aliases": ["mvp", "minimum viable product", "scope cut", "v1 scope"],
        "triggers": ["mvp", "minimum viable", "cut scope", "v1 scope"],
        "input_types": ["product idea", "validation results", "constraints"],
        "output_types": ["MVP scope card", "non-goals"],
        "requires": ["product idea", "validation results", "constraints (time, team, money)"],
        "optional_inputs": ["tech stack"],
        "produces": ["MVP scope card", "non-goals list", "success criteria"],
        "related": ["product-idea-validation", "product-roadmap", "agent-task-spec"],
        "playbooks": [],
        "purpose": "Define the smallest viable scope for an experiment or product.",
        "what": (
            "Cut a long wish list into the smallest scope that could still produce learning or value. "
            "Explicitly list what is not in scope."
        ),
        "why": (
            "MVPs that try to be MRPs (minimally respectable products) rarely ship. A ruthless scope accelerates learning."
        ),
        "when_use": [
            "You finished idea validation.",
            "Your team keeps adding features.",
        ],
        "when_not_use": [
            "You don't have validation yet — use product-idea-validation (038) first.",
        ],
        "prepare": [
            "Product idea and validation results.",
            "Constraints.",
        ],
        "how_ai": [
            "1. List candidate features.",
            "2. Rank by learning value per cost.",
            "3. Cut to MVP scope.",
            "4. Enumerate non-goals.",
        ],
        "what_get": [
            "MVP scope card.",
            "Non-goals list.",
            "Success criteria.",
        ],
        "next_steps": ["product-roadmap (040)", "agent-task-spec (091)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: mvp_scope\n"
            "    description: in-scope features\n"
            "  - key: non_goals\n"
            "    description: explicit out-of-scope list"
        ),
    },
    "040": {
        "slug": "product-roadmap",
        "title": "Create a Product Roadmap",
        "category": "business",
        "aliases": ["roadmap", "product plan", "release plan"],
        "triggers": ["product roadmap", "release plan", "what to build when"],
        "input_types": ["product", "strategy", "constraints"],
        "output_types": ["time-phased roadmap"],
        "requires": ["product", "strategy", "team capacity"],
        "optional_inputs": ["priorities", "dependencies"],
        "produces": ["time-phased roadmap", "themes per horizon", "trade-off notes"],
        "related": ["mvp-scope", "goal-setting", "task-breakdown"],
        "playbooks": [],
        "purpose": "Prioritize product work across time horizons.",
        "what": (
            "Group initiatives into horizons (now / next / later) and call out the trade-offs. "
            "Each horizon has a theme and 2–4 initiatives."
        ),
        "why": (
            "Roadmaps without trade-offs are wish lists. Naming what you won't do is what makes a roadmap executable."
        ),
        "when_use": [
            "You finished MVP scope and need to plan the next 6–12 months.",
            "Stakeholders want a single page showing what's coming.",
        ],
        "when_not_use": [
            "You only need a sprint plan — use task-breakdown (072) or project-plan (076).",
        ],
        "prepare": [
            "Product state.",
            "Strategy.",
            "Team capacity.",
        ],
        "how_ai": [
            "1. Confirm horizons (now / next / later).",
            "2. Group themes per horizon.",
            "3. List 2–4 initiatives each.",
            "4. Add trade-off notes.",
        ],
        "what_get": [
            "Time-phased roadmap.",
            "Trade-off notes.",
            "Next-workflow suggestion: project-plan (076).",
        ],
        "next_steps": ["project-plan (076)", "task-breakdown (072)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: roadmap\n"
            "    description: horizon-grouped initiatives\n"
            "  - key: trade_offs\n"
            "    description: notes on what was deferred"
        ),
    },
    "041": {
        "slug": "pricing-strategy",
        "title": "Design Pricing Strategy",
        "category": "business",
        "aliases": ["pricing", "price", "monetization pricing"],
        "triggers": ["pricing", "how to price", "pricing tiers", "monetization"],
        "input_types": ["offer", "market", "constraints"],
        "output_types": ["pricing strategy", "tier logic"],
        "requires": ["offer", "market willingness to pay", "business model constraints"],
        "optional_inputs": ["competitor pricing"],
        "produces": ["pricing strategy", "tier table", "test plan"],
        "related": ["offer-design", "value-proposition", "business-model"],
        "playbooks": ["validate-a-business-idea"],
        "purpose": "Develop pricing options and validation steps.",
        "what": (
            "Propose 2–3 pricing models (good-better-best, usage, tiered) with rationale, "
            "a tier table, and a price-test plan."
        ),
        "why": (
            "Pricing changes margin more than any other lever. A pricing strategy defends the choice and the trade-offs."
        ),
        "when_use": [
            "You're launching a paid offer.",
            "Your pricing feels arbitrary.",
        ],
        "when_not_use": [
            "You only need a headline price — use offer-design (037).",
        ],
        "prepare": [
            "Offer summary.",
            "Market willingness to pay signals.",
            "Business model constraints.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Generate 2–3 pricing models.",
            "3. Build a tier table.",
            "4. Define a price-test plan.",
        ],
        "what_get": [
            "Pricing models.",
            "Tier table.",
            "Price-test plan.",
        ],
        "next_steps": ["sales-page (043)", "marketing-funnel (044)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: pricing_models\n"
            "    description: candidate pricing strategies\n"
            "  - key: tier_table\n"
            "    description: tiers with rationale"
        ),
    },
    "042": {
        "slug": "business-model",
        "title": "Design a Business Model",
        "category": "business",
        "aliases": ["business model canvas", "bmc", "revenue model"],
        "triggers": ["business model", "how do we make money", "revenue model", "business model canvas"],
        "input_types": ["offer", "customer", "channels"],
        "output_types": ["business model canvas"],
        "requires": ["offer", "customer", "channels", "cost structure hints"],
        "optional_inputs": ["competitor models", "regulation"],
        "produces": ["business model canvas", "alternate models"],
        "related": ["pricing-strategy", "value-proposition", "offer-design"],
        "playbooks": [],
        "purpose": "Map value creation, delivery, and revenue logic.",
        "what": (
            "Produce a business model canvas (segments, value props, channels, relationships, revenue, costs, etc.) "
            "plus one alternate model."
        ),
        "why": (
            "Most pitch decks describe what the product does, not how it makes money. A business model makes the economics visible."
        ),
        "when_use": [
            "You're starting or pivoting a business.",
            "Investors or partners ask how money flows.",
        ],
        "when_not_use": [
            "You only need pricing — use pricing-strategy (041).",
        ],
        "prepare": [
            "Offer.",
            "Customer segments.",
            "Channels.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build a canvas.",
            "3. Add an alternate model.",
            "4. Highlight weakest assumptions.",
        ],
        "what_get": [
            "Business model canvas.",
            "Alternate model.",
            "Weakest-assumption list.",
        ],
        "next_steps": ["pricing-strategy (041)", "offer-design (037)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: business_model_canvas\n"
            "    description: 9-block canvas\n"
            "  - key: alternate_model\n"
            "    description: backup model"
        ),
    },
    "043": {
        "slug": "sales-page",
        "title": "Create a Sales Page",
        "category": "business",
        "aliases": ["landing page", "sales letter", "product page copy"],
        "triggers": ["sales page", "landing page", "product page", "long-form sales letter"],
        "input_types": ["offer", "audience", "tone"],
        "output_types": ["sales page"],
        "requires": ["offer card", "audience", "tone reference"],
        "optional_inputs": ["testimonials"],
        "produces": ["sales page copy", "section-by-section outline"],
        "related": ["offer-design", "value-proposition", "case-study"],
        "playbooks": [],
        "purpose": "Create a structured sales page from an offer brief.",
        "what": (
            "Produce a long-form sales page: headline, sub-headline, problem, promise, proof, offer, "
            "guarantee, call to action, FAQ."
        ),
        "why": (
            "A sales page without structure scatters attention. The classic sections carry the reader from skepticism to action."
        ),
        "when_use": [
            "You're launching a paid offer.",
            "Your landing page is under-converting.",
        ],
        "when_not_use": [
            "You want a quick landing page — use a simpler structure with cta-design (021).",
        ],
        "prepare": [
            "Offer card.",
            "Audience.",
            "Tone and proof.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Write each section.",
            "3. Insert proof and FAQs.",
            "4. Close with a strong CTA.",
        ],
        "what_get": [
            "Section-by-section outline.",
            "Sales page copy.",
            "Sample CTA.",
        ],
        "next_steps": ["content-quality-review (029)", "email-sequence (046)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: sales_page\n"
            "    description: sectioned page copy\n"
            "  - key: cta\n"
            "    description: closing call to action"
        ),
    },
    "044": {
        "slug": "marketing-funnel",
        "title": "Design a Marketing Funnel",
        "category": "business",
        "aliases": ["funnel", "marketing funnel", "tofu mofu bofu", "customer journey funnel"],
        "triggers": ["marketing funnel", "funnel design", "tofu mofu bofu", "customer journey funnel"],
        "input_types": ["offer", "audience", "channels"],
        "output_types": ["funnel map", "stage definitions"],
        "requires": ["offer", "audience", "channels"],
        "optional_inputs": ["awareness stage"],
        "produces": ["funnel map", "stage definitions", "content per stage"],
        "related": ["audience-message-map", "campaign-plan", "email-sequence"],
        "playbooks": [],
        "purpose": "Map the funnel from first contact to customer.",
        "what": (
            "Lay out a funnel (awareness, consideration, decision, retention) with stage definitions, "
            "content ideas per stage, and key metrics."
        ),
        "why": (
            "Funnels clarify who sees what content at what moment. They make conversion problems attributable to a stage."
        ),
        "when_use": [
            "You're building a campaign from scratch.",
            "Conversion is uneven and you don't know why.",
        ],
        "when_not_use": [
            "You want a one-time launch — use campaign-plan (045).",
        ],
        "prepare": [
            "Offer.",
            "Audience segments.",
            "Channels.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Lay out stages.",
            "3. Add content per stage.",
            "4. Add metrics per stage.",
        ],
        "what_get": [
            "Funnel map.",
            "Stage definitions.",
            "Content ideas per stage.",
            "Metrics per stage.",
        ],
        "next_steps": ["campaign-plan (045)", "email-sequence (046)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: funnel_map\n"
            "    description: stage definitions and metrics\n"
            "  - key: stage_content\n"
            "    description: content ideas per stage"
        ),
    },
    "045": {
        "slug": "campaign-plan",
        "title": "Plan a Campaign",
        "category": "business",
        "aliases": ["campaign", "launch plan", "marketing campaign"],
        "triggers": ["campaign plan", "launch plan", "marketing campaign"],
        "input_types": ["goal", "audience", "channels"],
        "output_types": ["campaign plan", "timeline", "assets list"],
        "requires": ["campaign goal", "audience", "channels", "timeline"],
        "optional_inputs": ["budget", "assets"],
        "produces": ["campaign plan", "channel mix", "asset list", "timeline"],
        "related": ["marketing-funnel", "email-sequence", "content-calendar"],
        "playbooks": [],
        "purpose": "Plan a multi-channel campaign for a defined period.",
        "what": (
            "Build a campaign plan with objectives, audience, channel mix, asset list, timeline, "
            "and measurement plan."
        ),
        "why": (
            "Campaigns without a plan collapse into ad-hoc execution. A simple plan makes the team aligned and accountable."
        ),
        "when_use": [
            "You're launching a product or feature.",
            "You want a one-time push for a promotion.",
        ],
        "when_not_use": [
            "You need a steady-state calendar — use content-calendar (004).",
        ],
        "prepare": [
            "Campaign goal.",
            "Audience.",
            "Channels and timeline.",
        ],
        "how_ai": [
            "1. Confirm goal, audience, channels.",
            "2. Pick the channel mix.",
            "3. List assets per channel.",
            "4. Timeline with milestones.",
            "5. Measurement plan.",
        ],
        "what_get": [
            "Campaign plan.",
            "Asset list.",
            "Timeline.",
            "Measurement plan.",
        ],
        "next_steps": ["email-sequence (046)", "content-calendar (004)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: campaign_plan\n"
            "    description: asset list and timeline\n"
            "  - key: measurement_plan\n"
            "    description: KPIs and tracking"
        ),
    },
    "046": {
        "slug": "email-sequence",
        "title": "Build an Email Sequence",
        "category": "business",
        "aliases": ["drip campaign", "email automation", "sequence"],
        "triggers": ["email sequence", "drip campaign", "nurture sequence", "automated emails"],
        "input_types": ["goal", "audience", "trigger"],
        "output_types": ["email sequence", "subject lines"],
        "requires": ["sequence goal", "audience", "entry trigger"],
        "optional_inputs": ["tone guide", "deliverability constraints"],
        "produces": ["per-email copy", "subject lines", "preview text", "send timing"],
        "related": ["newsletter", "marketing-funnel", "sales-page"],
        "playbooks": [],
        "purpose": "Design a triggered email sequence with the right cadence and goal.",
        "what": (
            "Design a multi-email sequence (typically 3–7 emails) with subject lines, body copy, "
            "preview text, send timing, and exit conditions."
        ),
        "why": (
            "One-off emails convert only at the moment of intent. A timed sequence nudges people back into a decision."
        ),
        "when_use": [
            "You're onboarding new users.",
            "You're launching a campaign that needs follow-up.",
        ],
        "when_not_use": [
            "You only need a single newsletter issue — use newsletter (011).",
        ],
        "prepare": [
            "Sequence goal.",
            "Audience and trigger.",
            "Tone.",
        ],
        "how_ai": [
            "1. Confirm goal, audience, trigger.",
            "2. Sequence the emails (3–7).",
            "3. Write subject lines and body.",
            "4. Add timing and exit conditions.",
        ],
        "what_get": [
            "Per-email copy.",
            "Subject lines and preview text.",
            "Timing and exit conditions.",
        ],
        "next_steps": ["content-quality-review (029)", "marketing-funnel (044)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: email_sequence\n"
            "    description: ordered emails with timing\n"
            "  - key: exit_conditions\n"
            "    description: rules to remove from sequence"
        ),
    },
    "047": {
        "slug": "cold-outreach",
        "title": "Draft Cold Outreach",
        "category": "business",
        "aliases": ["cold email", "cold pitch", "outreach"],
        "triggers": ["cold email", "cold outreach", "intro email", "first contact"],
        "input_types": ["recipient", "context", "ask"],
        "output_types": ["outreach variants"],
        "requires": ["recipient context", "the ask", "your credibility"],
        "optional_inputs": ["tone", "channels (email vs DM)"],
        "produces": ["outreach variants", "subject lines", "follow-up variants"],
        "related": ["email-sequence", "partnership-pitch", "sales-objection-handling"],
        "playbooks": [],
        "purpose": "Draft cold outreach that earns a reply.",
        "what": (
            "Write a short, specific outreach email or message. Provide subject lines and a follow-up."
        ),
        "why": (
            "Cold outreach fails when it talks about the sender. The recipient should see relevance in the first sentence."
        ),
        "when_use": [
            "You're reaching out to a prospect, partner, or press contact.",
            "Your open rates are low on cold emails.",
        ],
        "when_not_use": [
            "You're replying to a known prospect — use sales-objection-handling (048).",
        ],
        "prepare": [
            "Recipient context.",
            "The ask.",
            "Your credibility line.",
        ],
        "how_ai": [
            "1. Confirm recipient and ask.",
            "2. Write a 4–7 sentence email.",
            "3. Provide a subject line and follow-up variant.",
            "4. Sanity-check for warmth vs creepiness.",
        ],
        "what_get": [
            "Outreach copy.",
            "Subject line variants.",
            "Follow-up variant.",
        ],
        "next_steps": ["sales-objection-handling (048)", "email-sequence (046)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: outreach_copy\n"
            "    description: short cold email/message\n"
            "  - key: follow_up\n"
            "    description: follow-up variant"
        ),
    },
    "048": {
        "slug": "sales-objection-handling",
        "title": "Handle Sales Objections",
        "category": "business",
        "aliases": ["objections", "objection handling", "sales rebuttal"],
        "triggers": ["objection", "sales objection", "they said no", "rebuttal"],
        "input_types": ["objection", "context"],
        "output_types": ["response variants", "redirect to next step"],
        "requires": ["objection text", "context (offer, stage, customer)"],
        "optional_inputs": ["history of the conversation"],
        "produces": ["response variants", "disqualification note", "next-step suggestion"],
        "related": ["cold-outreach", "sales-page", "retention-plan"],
        "playbooks": [],
        "purpose": "Draft responses to common sales objections without arguing.",
        "what": (
            "For each objection, produce a short response that acknowledges, reframes, and offers a "
            "concrete next step. Add a disqualification note when the objection signals a bad fit."
        ),
        "why": (
            "Arguing with objections triggers more resistance. Acknowledging and reframing keeps the conversation alive."
        ),
        "when_use": [
            "You're preparing for sales calls.",
            "A prospect raised an objection in writing.",
        ],
        "when_not_use": [
            "You're losing customers after purchase — use retention-plan (051).",
        ],
        "prepare": [
            "Objection text.",
            "Context of the deal.",
        ],
        "how_ai": [
            "1. Confirm objection and context.",
            "2. Classify (price, trust, fit, timing).",
            "3. Produce 2 response variants.",
            "4. Suggest a next step.",
        ],
        "what_get": [
            "Objection classification.",
            "2 response variants.",
            "Next-step suggestion.",
        ],
        "next_steps": ["retention-plan (051)", "cold-outreach (047)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: classification\n"
            "    description: objection category\n"
            "  - key: response_variants\n"
            "    description: response options"
        ),
    },
    "049": {
        "slug": "partnership-pitch",
        "title": "Pitch a Partnership",
        "category": "business",
        "aliases": ["partner pitch", "partnership", "joint venture"],
        "triggers": ["partner pitch", "partnership", "joint venture", "co-marketing"],
        "input_types": ["partner", "goal", "offer"],
        "output_types": ["partnership pitch deck or memo"],
        "requires": ["partner profile", "goal", "your offer"],
        "optional_inputs": ["case study", "audience overlap"],
        "produces": ["partnership pitch memo", "joint value story", "next steps"],
        "related": ["cold-outreach", "value-proposition", "case-study"],
        "playbooks": [],
        "purpose": "Build a partnership pitch that earns a meeting.",
        "what": (
            "Write a partnership pitch: who you are, who they are, the joint opportunity, the structure, the ask. "
            "Keep it to one page."
        ),
        "why": (
            "Most partnership pitches focus on one side. Framing joint value earns attention faster than pitching alone."
        ),
        "when_use": [
            "You're approaching a potential partner.",
            "A partner approached you and you need a structured response.",
        ],
        "when_not_use": [
            "You're selling to a customer — use cold-outreach (047) or sales-page (043).",
        ],
        "prepare": [
            "Partner profile.",
            "Goal.",
            "Your offer.",
        ],
        "how_ai": [
            "1. Confirm partner and goal.",
            "2. Frame the joint value.",
            "3. Propose structures (co-marketing, bundling, distribution).",
            "4. State the next step clearly.",
        ],
        "what_get": [
            "Partnership pitch memo.",
            "Joint value story.",
            "Next step.",
        ],
        "next_steps": ["email-sequence (046)", "case-study (025)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: pitch_memo\n"
            "    description: one-page pitch\n"
            "  - key: joint_value\n"
            "    description: explanation of mutual benefit"
        ),
    },
    "050": {
        "slug": "customer-journey",
        "title": "Map the Customer Journey",
        "category": "business",
        "aliases": ["journey map", "customer journey", "touchpoints"],
        "triggers": ["customer journey", "touchpoints", "journey map", "user journey"],
        "input_types": ["customer", "stages", "channels"],
        "output_types": ["journey map"],
        "requires": ["customer profile", "stages", "channels"],
        "optional_inputs": ["existing journey map"],
        "produces": ["journey map (stages × touchpoints)", "pain points", "moments of truth"],
        "related": ["marketing-funnel", "retention-plan", "audience-message-map"],
        "playbooks": [],
        "purpose": "Map the customer journey across stages and touchpoints.",
        "what": (
            "Produce a journey map: stages × touchpoints, with emotions, pain points, and moments of truth. "
            "Identify quick wins and structural fixes."
        ),
        "why": (
            "A journey map makes moments of truth obvious. It also removes finger-pointing between teams because the journey is shared."
        ),
        "when_use": [
            "You want to improve onboarding, conversion, or retention.",
            "Different teams disagree on where problems happen.",
        ],
        "when_not_use": [
            "You only need a funnel for conversion — use marketing-funnel (044).",
        ],
        "prepare": [
            "Customer profile.",
            "Stages (awareness, consideration, etc.).",
            "Channels.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build the map.",
            "3. Identify pain points and moments of truth.",
            "4. Recommend quick wins.",
        ],
        "what_get": [
            "Journey map.",
            "Pain points.",
            "Moments of truth.",
            "Quick wins.",
        ],
        "next_steps": ["retention-plan (051)", "marketing-funnel (044)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: journey_map\n"
            "    description: stages and touchpoints\n"
            "  - key: moments_of_truth\n"
            "    description: critical interactions"
        ),
    },
    "051": {
        "slug": "retention-plan",
        "title": "Design a Retention Plan",
        "category": "business",
        "aliases": ["retention", "churn", "customer retention"],
        "triggers": ["retention", "churn plan", "reduce churn", "keep customers"],
        "input_types": ["product", "current churn signals", "customer segments"],
        "output_types": ["retention plan", "trigger matrix"],
        "requires": ["product", "current churn signals", "segments"],
        "optional_inputs": ["interview notes"],
        "produces": ["retention plan", "trigger-based actions", "measurement plan"],
        "related": ["customer-journey", "customer-feedback-analysis", "email-sequence"],
        "playbooks": [],
        "purpose": "Reduce churn with a trigger-based retention plan.",
        "what": (
            "Build a retention plan with key churn signals, trigger-based actions, "
            "and a measurement approach (e.g., cohort retention curves)."
        ),
        "why": (
            "Retention compounds. A small improvement in churn is worth more than aggressive acquisition."
        ),
        "when_use": [
            "You're noticing churn or downgrade signals.",
            "You want to launch a habit / loyalty feature.",
        ],
        "when_not_use": [
            "You're optimizing acquisition only — use marketing-funnel (044).",
        ],
        "prepare": [
            "Product context.",
            "Current churn or downgrade signals.",
            "Segments.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Map churn triggers.",
            "3. Design trigger-based actions.",
            "4. Define measurement.",
        ],
        "what_get": [
            "Trigger matrix.",
            "Action playbook.",
            "Measurement plan.",
        ],
        "next_steps": ["customer-feedback-analysis (033)", "email-sequence (046)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: trigger_matrix\n"
            "    description: triggers and matching actions\n"
            "  - key: measurement_plan\n"
            "    description: cohort or NPS tracking"
        ),
    },
    "052": {
        "slug": "business-decision",
        "title": "Make a Business Decision",
        "category": "business",
        "aliases": ["business decision", "strategic decision", "go or no-go"],
        "triggers": ["should we", "go or no-go", "business decision", "make a call"],
        "input_types": ["decision", "options", "criteria"],
        "output_types": ["decision memo"],
        "requires": ["decision statement", "options considered", "decision criteria"],
        "optional_inputs": ["research sources"],
        "produces": ["decision memo", "trade-off table", "next steps"],
        "related": ["decision-memo", "risk-stress-test", "scenario-planning"],
        "playbooks": [],
        "purpose": "Structure a strategic business decision before committing.",
        "what": (
            "Produce a decision memo with the decision statement, criteria, options, "
            "trade-offs, recommendation, and next steps."
        ),
        "why": (
            "Most bad strategic decisions were never written down. A memo forces clarity and survives group-think."
        ),
        "when_use": [
            "A major decision sits with leadership.",
            "You want to defend the call later.",
        ],
        "when_not_use": [
            "The decision needs research first — use research-before-a-decision playbook.",
        ],
        "prepare": [
            "Decision statement.",
            "Options considered.",
            "Decision criteria.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Frame the decision.",
            "3. Compare options against criteria.",
            "4. Recommend with conditions.",
        ],
        "what_get": [
            "Decision memo.",
            "Trade-off table.",
            "Recommendation.",
        ],
        "next_steps": ["risk-stress-test (053)", "decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: decision_memo\n"
            "    description: structured decision\n"
            "  - key: trade_offs\n"
            "    description: trade-off table"
        ),
    },
    "053": {
        "slug": "risk-stress-test",
        "title": "Stress-Test a Plan Against Risks",
        "category": "business",
        "aliases": ["risk test", "pre-mortem", "stress test a plan"],
        "triggers": ["risk check", "pre-mortem", "stress test this plan", "what could go wrong"],
        "input_types": ["plan", "risks"],
        "output_types": ["risk register", "mitigations"],
        "requires": ["plan summary", "known risks"],
        "optional_inputs": ["stakeholders"],
        "produces": ["risk register", "mitigations", "owner suggestions"],
        "related": ["business-decision", "project-risk", "scenario-planning"],
        "playbooks": [],
        "purpose": "Identify, score, and mitigate risks in a plan.",
        "what": (
            "Generate a risk register with risk statements, likelihood, impact, score, "
            "mitigations, and owners. Include at least one pre-mortem scenario."
        ),
        "why": (
            "Plans fail in ways you didn't prepare for. Stress-testing converts vague worry into mitigable risks."
        ),
        "when_use": [
            "Before committing to a major plan.",
            "When a stakeholder asks \"what could go wrong?\"",
        ],
        "when_not_use": [
            "You're planning long-range scenarios — use scenario-planning (068).",
        ],
        "prepare": [
            "Plan summary.",
            "Known risks.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Generate a risk register.",
            "3. Run a pre-mortem.",
            "4. Recommend mitigations.",
        ],
        "what_get": [
            "Risk register.",
            "Pre-mortem notes.",
            "Mitigations.",
        ],
        "next_steps": ["business-decision (052)", "project-risk (077)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: risk_register\n"
            "    description: ranked risks with mitigations\n"
            "  - key: pre_mortem\n"
            "    description: pre-mortem narrative"
        ),
    },
    # ---------------------------------------------------------------- 03-research 054-071
    "054": {
        "slug": "research-question",
        "title": "Define Research Questions",
        "category": "research",
        "aliases": ["research questions", "questions to research"],
        "triggers": ["research question", "what should we ask", "what do we need to know"],
        "input_types": ["topic", "goal"],
        "output_types": ["question list", "decision relevance"],
        "requires": ["topic", "research goal"],
        "optional_inputs": ["audience", "timeline"],
        "produces": ["ranked question list", "decision relevance per question"],
        "related": ["research-plan", "web-research-synthesis"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Frame the questions a piece of research must answer.",
        "what": (
            "Produce a ranked list of research questions, each annotated with why the answer matters for the decision."
        ),
        "why": (
            "Most research is unfocused because the questions were never written down. Defining questions first turns research from a chore into an answer-finding mission."
        ),
        "when_use": [
            "You're commissioning research.",
            "You're starting an investigation and need focus.",
        ],
        "when_not_use": [
            "You're planning the research method itself — use research-plan (055).",
        ],
        "prepare": [
            "Topic.",
            "Research goal.",
        ],
        "how_ai": [
            "1. Confirm the decision context.",
            "2. Brainstorm candidate questions.",
            "3. Rank by decision relevance.",
            "4. Drop low-value questions.",
        ],
        "what_get": [
            "Ranked research question list.",
            "Decision relevance per question.",
        ],
        "next_steps": ["research-plan (055)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: research_questions\n"
            "    description: ranked list with rationale"
        ),
    },
    "055": {
        "slug": "research-plan",
        "title": "Plan a Research Project",
        "category": "research",
        "aliases": ["research plan", "study plan", "investigation plan"],
        "triggers": ["research plan", "study plan", "how to research this"],
        "input_types": ["research questions", "constraints"],
        "output_types": ["research plan"],
        "requires": ["research questions", "constraints (time, budget, tools)"],
        "optional_inputs": ["primary sources", "audience for the output"],
        "produces": ["research plan", "method selection", "timeline"],
        "related": ["research-question", "web-research-synthesis", "evidence-matrix"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Plan a research project: methods, sources, timeline, deliverables.",
        "what": (
            "Build a research plan with methods, source list, timeline, and decision-ready output format."
        ),
        "why": (
            "Without a plan, research meanders and over-runs. A plan commits to methods and a deadline."
        ),
        "when_use": [
            "You're starting a multi-day research project.",
            "You're scoping research for a client or stakeholder.",
        ],
        "when_not_use": [
            "You only need a quick study — use web-research-synthesis (057).",
        ],
        "prepare": [
            "Research questions.",
            "Constraints.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Pick methods per question.",
            "3. List primary sources.",
            "4. Build a timeline.",
            "5. Specify the output.",
        ],
        "what_get": [
            "Research plan.",
            "Method selection.",
            "Timeline.",
            "Output spec.",
        ],
        "next_steps": ["web-research-synthesis (057)", "evidence-matrix (065)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: research_plan\n"
            "    description: methods, sources, timeline\n"
            "  - key: output_spec\n"
            "    description: what the research will produce"
        ),
    },
    "056": {
        "slug": "source-evaluation",
        "title": "Evaluate a Source",
        "category": "research",
        "aliases": ["source check", "credibility", "rate the source"],
        "triggers": ["is this reliable", "check this source", "evaluate this article"],
        "input_types": ["source link or text"],
        "output_types": ["credibility assessment"],
        "requires": ["source link or text", "decision context"],
        "optional_inputs": ["author", "publication"],
        "produces": ["credibility assessment", "bias flags"],
        "related": ["fact-check", "web-research-synthesis", "research-question"],
        "playbooks": [],
        "purpose": "Evaluate the credibility and relevance of a source.",
        "what": (
            "Score the source on credibility (authorship, evidence, incentives) "
            "and relevance (recency, fit to the question). Flag known biases."
        ),
        "why": (
            "Basing decisions on weak sources produces weak decisions. A structured evaluation surfaces issues you would otherwise skim past."
        ),
        "when_use": [
            "You're about to cite a source in a decision document.",
            "You suspect a source is biased.",
        ],
        "when_not_use": [
            "You're fact-checking specific claims — use fact-check (064).",
        ],
        "prepare": [
            "Source link or text.",
            "Decision context.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Score credibility.",
            "3. Score relevance.",
            "4. Flag bias risks.",
            "5. Recommend how to use the source.",
        ],
        "what_get": [
            "Credibility assessment.",
            "Relevance assessment.",
            "Bias flags.",
            "Usage recommendation.",
        ],
        "next_steps": ["fact-check (064)", "evidence-matrix (065)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: credibility_score\n"
            "    description: numeric credibility score with rationale\n"
            "  - key: bias_flags\n"
            "    description: list of detected biases"
        ),
    },
    "057": {
        "slug": "web-research-synthesis",
        "title": "Synthesize Web Research",
        "category": "research",
        "aliases": ["research summary", "synthesize", "research synthesis"],
        "triggers": ["research this online", "what does the web say", "synthesize findings"],
        "input_types": ["topic", "questions"],
        "output_types": ["synthesis", "source list"],
        "requires": ["topic or question", "recency sensitivity"],
        "optional_inputs": ["authoritative sources preferred", "regions"],
        "produces": ["synthesis", "source list", "verification log"],
        "related": ["research-question", "source-evaluation", "fact-check"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Synthesize current public information on a topic.",
        "what": (
            "Read public sources, summarize findings by sub-question, "
            "and produce a synthesis with a source list and a verification log."
        ),
        "why": (
            "Today's web is flooded with content. A synthesis separates signal from noise and tells the user what is solid and what is contested."
        ),
        "when_use": [
            "You need current information on a topic.",
            "You're preparing for a decision and want to scan the landscape.",
        ],
        "when_not_use": [
            "You have one document — use document-summary (058).",
            "You need to defend a specific claim — use fact-check (064).",
        ],
        "prepare": [
            "Topic or question.",
            "Recency sensitivity.",
            "Output length.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Pull current sources.",
            "3. Group by sub-question.",
            "4. Note disagreements and gaps.",
            "5. Output the synthesis with sources.",
        ],
        "what_get": [
            "Synthesis.",
            "Source list.",
            "Verification log.",
            "Next-workflow suggestion: fact-check (064) or evidence-matrix (065).",
        ],
        "next_steps": ["fact-check (064)", "evidence-matrix (065)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: synthesis\n"
            "    description: topic synthesis\n"
            "  - key: source_list\n"
            "    description: cited sources with URL and date"
        ),
    },
    "058": {
        "slug": "document-summary",
        "title": "Summarize a Long Document",
        "category": "research",
        "aliases": ["document summary", "long doc summary", "summarize paper"],
        "triggers": ["summarize this document", "long doc summary", "summarize this paper"],
        "input_types": ["document"],
        "output_types": ["structured summary"],
        "requires": ["document (text or URL)", "reader and use case"],
        "optional_inputs": ["question to answer"],
        "produces": ["structured summary", "key facts", "open questions"],
        "related": ["content-summary", "fact-check", "evidence-matrix"],
        "playbooks": [],
        "purpose": "Summarize a long document into a structured, decision-ready briefing.",
        "what": (
            "Produce a structured summary (purpose, key claims, evidence, conclusions, open questions) "
            "tuned to a chosen reader and use case."
        ),
        "why": (
            "Long documents often bury the punchline. A structured summary surfaces what matters for the reader."
        ),
        "when_use": [
            "You're reviewing a 20+ page report or paper.",
            "You're preparing for a decision meeting.",
        ],
        "when_not_use": [
            "You're summarizing short content — use content-summary (010).",
        ],
        "prepare": [
            "Document.",
            "Reader and use case.",
        ],
        "how_ai": [
            "1. Read the document.",
            "2. Identify purpose, key claims, evidence, conclusions.",
            "3. Summarize per section.",
            "4. Flag open questions and verification needs.",
        ],
        "what_get": [
            "Structured summary.",
            "Key facts list.",
            "Open questions list.",
            "Suggested next workflow: evidence-matrix (065).",
        ],
        "next_steps": ["evidence-matrix (065)", "decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: structured_summary\n"
            "    description: summary by section\n"
            "  - key: open_questions\n"
            "    description: verification needs"
        ),
    },
    "059": {
        "slug": "meeting-summary",
        "title": "Summarize a Meeting Transcript",
        "category": "research",
        "aliases": ["meeting notes", "transcript summary", "meeting recap"],
        "triggers": ["summarize this meeting", "meeting transcript", "what was decided"],
        "input_types": ["transcript or notes"],
        "output_types": ["meeting summary", "action items"],
        "requires": ["transcript or notes", "audience for the summary"],
        "optional_inputs": ["agenda"],
        "produces": ["meeting summary", "decisions", "action items", "open questions"],
        "related": ["meeting-notes", "decision-memo", "task-breakdown"],
        "playbooks": [],
        "purpose": "Turn a meeting transcript into a usable summary.",
        "what": (
            "Read the transcript and produce a structured summary: decisions, action items, "
            "open questions, and brief context for absent teammates."
        ),
        "why": (
            "Without a structured summary, meetings forget themselves. Action items lose owners and deadlines drift."
        ),
        "when_use": [
            "You have a meeting transcript or detailed notes.",
            "You missed a meeting and need a recap.",
        ],
        "when_not_use": [
            "You're turning notes into an internal memo — use meeting-notes (079).",
        ],
        "prepare": [
            "Transcript or notes.",
            "Audience (full team, execs).",
        ],
        "how_ai": [
            "1. Read the transcript.",
            "2. Extract decisions, actions, open questions.",
            "3. Surface disagreements.",
            "4. Write a short context recap.",
        ],
        "what_get": [
            "Decisions list.",
            "Action items (who/what/when).",
            "Open questions.",
            "Context recap.",
        ],
        "next_steps": ["task-breakdown (072)", "decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: decisions\n"
            "    description: decision list\n"
            "  - key: action_items\n"
            "    description: who / what / when"
        ),
    },
    "060": {
        "slug": "data-extraction",
        "title": "Extract Structured Data",
        "category": "research",
        "aliases": ["extract data", "pull out facts", "structured extraction"],
        "triggers": ["extract data", "pull out the data", "structure these facts"],
        "input_types": ["unstructured text"],
        "output_types": ["structured table or JSON"],
        "requires": ["source text", "schema or field list"],
        "optional_inputs": ["output format"],
        "produces": ["extracted records", "missing-field flags"],
        "related": ["classification", "document-summary", "data-analysis"],
        "playbooks": [],
        "purpose": "Convert unstructured text into structured data.",
        "what": (
            "Define the schema, then extract records from the text. Flag fields you cannot fill."
        ),
        "why": (
            "Locked-in text is hard to query, audit, or feed into other tools. Structured extraction unlocks the data."
        ),
        "when_use": [
            "You have invoices, contracts, or product pages to inventory.",
            "You want to feed downstream analytics with text.",
        ],
        "when_not_use": [
            "You want a free-form summary — use document-summary (058).",
        ],
        "prepare": [
            "Source text.",
            "Schema or field list.",
        ],
        "how_ai": [
            "1. Confirm the schema.",
            "2. Extract records row by row.",
            "3. Flag missing or unparsed fields.",
            "4. Return as table or JSON.",
        ],
        "what_get": [
            "Extracted records.",
            "Missing-field flags.",
            "Suggested schema refinements.",
        ],
        "next_steps": ["classification (061)", "data-analysis (097)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: extracted_records\n"
            "    description: structured output\n"
            "  - key: missing_fields\n"
            "    description: list of fields that could not be filled"
        ),
    },
    "061": {
        "slug": "classification",
        "title": "Classify Items into Buckets",
        "category": "research",
        "aliases": ["classify", "categorize", "tagging"],
        "triggers": ["classify", "categorize", "sort into buckets", "tag these"],
        "input_types": ["items", "categories"],
        "output_types": ["classification result"],
        "requires": ["items list", "taxonomy or categories", "rules"],
        "optional_inputs": ["examples"],
        "produces": ["classification per item", "ambiguous flags"],
        "related": ["data-extraction", "knowledge-organization"],
        "playbooks": [],
        "purpose": "Classify a set of items into a defined taxonomy.",
        "what": (
            "Apply the taxonomy to each item and produce a classification. "
            "Flag items that don't fit cleanly."
        ),
        "why": (
            "Manual classification is slow and inconsistent. A consistent rubric surfaces edge cases and patterns."
        ),
        "when_use": [
            "You have customer feedback to triage.",
            "You want to bucket transactions or inventory.",
        ],
        "when_not_use": [
            "You want a free-form summary — use document-summary (058).",
        ],
        "prepare": [
            "Items list.",
            "Taxonomy.",
            "Optional examples.",
        ],
        "how_ai": [
            "1. Confirm taxonomy.",
            "2. Classify each item.",
            "3. Flag ambiguous items.",
            "4. Suggest taxonomy refinements.",
        ],
        "what_get": [
            "Classification per item.",
            "Ambiguous flags.",
            "Taxonomy refinement notes.",
        ],
        "next_steps": ["data-analysis (097)", "knowledge-organization (083)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: classifications\n"
            "    description: per-item categories\n"
            "  - key: ambiguous_flags\n"
            "    description: items needing review"
        ),
    },
    "062": {
        "slug": "knowledge-map",
        "title": "Build a Knowledge Map",
        "category": "research",
        "aliases": ["knowledge graph", "concept map", "taxonomy map"],
        "triggers": ["knowledge map", "map concepts", "concept map", "taxonomy"],
        "input_types": ["domain", "sources"],
        "output_types": ["knowledge map"],
        "requires": ["domain", "source list or materials"],
        "optional_inputs": ["target audience"],
        "produces": ["concept map", "definitions", "relationships"],
        "related": ["knowledge-organization", "research-plan", "concept-explanation"],
        "playbooks": [],
        "purpose": "Map the core concepts and relationships in a domain.",
        "what": (
            "Build a concept map (entities, definitions, relationships) for a chosen domain."
        ),
        "why": (
            "A concept map is faster to learn from than a long document. It also surfaces gaps in shared understanding."
        ),
        "when_use": [
            "You're onboarding into a new domain.",
            "You're building a course or wiki.",
        ],
        "when_not_use": [
            "You only need definitions — use concept-explanation (086).",
        ],
        "prepare": [
            "Domain.",
            "Sources.",
        ],
        "how_ai": [
            "1. Confirm domain.",
            "2. List core concepts.",
            "3. Define each.",
            "4. Identify relationships.",
            "5. Render as a map.",
        ],
        "what_get": [
            "Concept map.",
            "Definitions.",
            "Relationships.",
        ],
        "next_steps": ["concept-explanation (086)", "knowledge-organization (083)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: concept_map\n"
            "    description: entities and relationships\n"
            "  - key: definitions\n"
            "    description: short definitions per concept"
        ),
    },
    "063": {
        "slug": "timeline",
        "title": "Build a Timeline",
        "category": "research",
        "aliases": ["timeline", "chronology", "history"],
        "triggers": ["timeline", "chronology", "history of", "build a timeline"],
        "input_types": ["events or sources"],
        "output_types": ["timeline"],
        "requires": ["events list or sources", "time range"],
        "optional_inputs": ["significance"],
        "produces": ["timeline", "key inflection points"],
        "related": ["document-summary", "knowledge-map"],
        "playbooks": [],
        "purpose": "Order events into a clear timeline with inflection points.",
        "what": (
            "Read the sources and produce a timeline of events, each with date, summary, and source. "
            "Highlight inflection points."
        ),
        "why": (
            "Timelines turn dense history into a story. They also expose patterns that are invisible in prose."
        ),
        "when_use": [
            "You're preparing a history section.",
            "You're analyzing how a field evolved.",
        ],
        "when_not_use": [
            "You need scenario planning — use scenario-planning (068).",
        ],
        "prepare": [
            "Events or sources.",
            "Time range.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Read sources.",
            "3. Order events.",
            "4. Highlight inflection points.",
        ],
        "what_get": [
            "Timeline.",
            "Inflection points.",
        ],
        "next_steps": ["document-summary (058)", "knowledge-map (062)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: timeline\n"
            "    description: ordered events\n"
            "  - key: inflection_points\n"
            "    description: notable turning points"
        ),
    },
    "064": {
        "slug": "fact-check",
        "title": "Fact-Check Claims",
        "category": "research",
        "aliases": ["fact check", "verify claims", "check facts"],
        "triggers": ["fact check", "verify this", "is this true"],
        "input_types": ["claims"],
        "output_types": ["verification report"],
        "requires": ["claims to check", "sources available"],
        "optional_inputs": ["verification standard (strict / soft)"],
        "produces": ["per-claim verdict", "source references", "open issues"],
        "related": ["source-evaluation", "evidence-matrix", "web-research-synthesis"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Check specific claims against sources and label their status.",
        "what": (
            "Examine each claim against available sources. Label it verified, partially verified, "
            "contradicted, or unverified."
        ),
        "why": (
            "Decisions break on unverified claims. A structured fact-check turns a doc into one a decision-maker can rely on."
        ),
        "when_use": [
            "You're about to publish or present claims.",
            "A decision rests on a contested number.",
        ],
        "when_not_use": [
            "You want general source quality — use source-evaluation (056).",
        ],
        "prepare": [
            "Claims.",
            "Sources.",
        ],
        "how_ai": [
            "1. List claims.",
            "2. For each, retrieve source evidence.",
            "3. Label the claim.",
            "4. Note remaining uncertainty.",
        ],
        "what_get": [
            "Per-claim verdict.",
            "Source references.",
            "Uncertainty log.",
        ],
        "next_steps": ["evidence-matrix (065)", "decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: verdicts\n"
            "    description: per-claim label\n"
            "  - key: uncertainty_log\n"
            "    description: remaining doubts"
        ),
    },
    "065": {
        "slug": "evidence-matrix",
        "title": "Build an Evidence Matrix",
        "category": "research",
        "aliases": ["evidence matrix", "weight evidence", "claim evidence table"],
        "triggers": ["evidence matrix", "compare evidence", "weight the evidence"],
        "input_types": ["claims and evidence"],
        "output_types": ["evidence matrix"],
        "requires": ["claims", "evidence items", "criteria"],
        "optional_inputs": ["weighting"],
        "produces": ["claim × evidence matrix", "weighted score per claim"],
        "related": ["fact-check", "decision-memo", "reasoning-audit"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Map claims to evidence and weight them.",
        "what": (
            "Build a matrix of claims × evidence pieces. Weight the evidence and "
            "score each claim. Identify the most and least supported claims."
        ),
        "why": (
            "Decisions become defensible when the evidence behind them is visible. A matrix makes that visible."
        ),
        "when_use": [
            "You're supporting or rejecting a strategic hypothesis.",
            "You're comparing two courses of action.",
        ],
        "when_not_use": [
            "You want to verify one claim — use fact-check (064).",
        ],
        "prepare": [
            "Claims.",
            "Evidence items.",
            "Criteria.",
        ],
        "how_ai": [
            "1. Build the matrix.",
            "2. Apply weights.",
            "3. Score claims.",
            "4. Highlight outliers.",
        ],
        "what_get": [
            "Evidence matrix.",
            "Weighted scores.",
            "Outlier claims.",
        ],
        "next_steps": ["decision-memo (069)", "reasoning-audit (066)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: matrix\n"
            "    description: claim × evidence grid\n"
            "  - key: scores\n"
            "    description: weighted scores per claim"
        ),
    },
    "066": {
        "slug": "reasoning-audit",
        "title": "Audit Your Reasoning",
        "category": "research",
        "aliases": ["reasoning audit", "logic check", "check my reasoning"],
        "triggers": ["check my reasoning", "audit my logic", "is this argument sound"],
        "input_types": ["argument"],
        "output_types": ["reasoning audit"],
        "requires": ["argument text", "audience"],
        "optional_inputs": ["target conclusion"],
        "produces": ["logical gaps", "fallacy checks", "suggested fixes"],
        "related": ["counterargument", "evidence-matrix", "decision-memo"],
        "playbooks": [],
        "purpose": "Audit the reasoning behind an argument.",
        "what": (
            "Walk through the argument step by step. Identify logical gaps, "
            "unstated assumptions, and known fallacies. Recommend fixes."
        ),
        "why": (
            "Most reasoning errors hide in unstated assumptions. An audit surfaces them before they become decisions."
        ),
        "when_use": [
            "You're preparing a memo or strategy document.",
            "You want to challenge your own argument.",
        ],
        "when_not_use": [
            "You want counter-evidence — use counterargument (067).",
        ],
        "prepare": [
            "Argument text.",
            "Audience.",
        ],
        "how_ai": [
            "1. Identify the conclusion.",
            "2. Walk through the steps.",
            "3. Flag gaps and assumptions.",
            "4. Recommend fixes.",
        ],
        "what_get": [
            "Step-by-step trace.",
            "Logical gaps.",
            "Suggested fixes.",
        ],
        "next_steps": ["counterargument (067)", "decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: gaps\n"
            "    description: list of logical gaps\n"
            "  - key: fixes\n"
            "    description: recommended corrections"
        ),
    },
    "067": {
        "slug": "counterargument",
        "title": "Build the Counter-Argument",
        "category": "research",
        "aliases": ["counterargument", "steelman the other side", "devil's advocate"],
        "triggers": ["counterargument", "steelman", "devils advocate", "what's the other side"],
        "input_types": ["argument"],
        "output_types": ["counter-argument"],
        "requires": ["argument or position", "context"],
        "optional_inputs": ["target audience"],
        "produces": ["counter-argument", "strongest counter-points", "how to address them"],
        "related": ["reasoning-audit", "decision-memo", "scenario-planning"],
        "playbooks": [],
        "purpose": "Build the strongest counter-argument to a position.",
        "what": (
            "Restate the position, then build the strongest counter-case using available evidence. "
            "Suggest how the original position can be reinforced."
        ),
        "why": (
            "Stronger arguments survive contact with strong counter-arguments. Building them in advance is a sign of rigor."
        ),
        "when_use": [
            "You're defending a position in writing.",
            "You want to stress-test a decision.",
        ],
        "when_not_use": [
            "You want a logical audit — use reasoning-audit (066).",
        ],
        "prepare": [
            "Position.",
            "Context.",
        ],
        "how_ai": [
            "1. Restate the position.",
            "2. Build the strongest counter-case.",
            "3. Identify the strongest counter-points.",
            "4. Recommend responses.",
        ],
        "what_get": [
            "Counter-argument.",
            "Strongest counter-points.",
            "Recommended responses.",
        ],
        "next_steps": ["decision-memo (069)", "reasoning-audit (066)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: counter_argument\n"
            "    description: strongest counter-argument\n"
            "  - key: responses\n"
            "    description: how to address them"
        ),
    },
    "068": {
        "slug": "scenario-planning",
        "title": "Plan Across Scenarios",
        "category": "research",
        "aliases": ["scenarios", "scenario planning", "what if"],
        "triggers": ["scenarios", "what if", "scenario planning", "futures"],
        "input_types": ["decision context", "drivers"],
        "output_types": ["scenario set"],
        "requires": ["decision context", "key drivers (2–3)", "time horizon"],
        "optional_inputs": ["internal constraints"],
        "produces": ["3–4 scenarios", "trigger indicators", "implications"],
        "related": ["risk-stress-test", "decision-memo", "business-decision"],
        "playbooks": [],
        "purpose": "Plan across 3–4 plausible futures.",
        "what": (
            "Build 3–4 distinct scenarios from the chosen drivers. For each, "
            "describe the situation, the trigger indicators, and the implications for the decision."
        ),
        "why": (
            "Single-point forecasts fail when conditions change. Scenario planning builds robustness under uncertainty."
        ),
        "when_use": [
            "You're making a long-horizon decision.",
            "A board wants to stress-test strategy.",
        ],
        "when_not_use": [
            "You're consolidating existing evidence — use evidence-matrix (065).",
        ],
        "prepare": [
            "Decision context.",
            "Key drivers.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build 3–4 scenarios.",
            "3. Define trigger indicators.",
            "4. List implications.",
        ],
        "what_get": [
            "Scenario set.",
            "Trigger indicators.",
            "Implications per scenario.",
        ],
        "next_steps": ["business-decision (052)", "risk-stress-test (053)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: scenarios\n"
            "    description: distinct futures\n"
            "  - key: trigger_indicators\n"
            "    description: signals to watch"
        ),
    },
    "069": {
        "slug": "decision-memo",
        "title": "Write a Decision Memo",
        "category": "research",
        "aliases": ["decision memo", "decision document", "recommendation memo"],
        "triggers": ["decision memo", "recommendation", "decide this"],
        "input_types": ["decision", "options", "evidence"],
        "output_types": ["decision memo"],
        "requires": ["decision statement", "options", "evidence or criteria"],
        "optional_inputs": ["stakeholders", "risks"],
        "produces": ["decision memo", "options table", "next steps"],
        "related": ["executive-brief", "evidence-matrix", "business-decision"],
        "playbooks": ["research-before-a-decision"],
        "purpose": "Produce a decision-ready memo with options, criteria, and recommendation.",
        "what": (
            "Write a 1–2 page memo: decision, criteria, options, recommendation, trade-offs, "
            "next steps, and open questions."
        ),
        "why": (
            "Most decisions are made on the back of imprecise arguments. A memo forces clarity, criteria, and trade-offs."
        ),
        "when_use": [
            "A strategic decision needs written support.",
            "You want to brief executives.",
        ],
        "when_not_use": [
            "You only need a one-page summary — use executive-brief (070).",
        ],
        "prepare": [
            "Decision statement.",
            "Options.",
            "Evidence.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Frame decision.",
            "3. Compare options.",
            "4. Recommend with conditions.",
            "5. List next steps and risks.",
        ],
        "what_get": [
            "Decision memo.",
            "Options table.",
            "Recommendation.",
            "Next steps and risks.",
        ],
        "next_steps": ["executive-brief (070)", "scenario-planning (068)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: decision_memo\n"
            "    description: 1–2 page memo\n"
            "  - key: recommendation\n"
            "    description: chosen option"
        ),
    },
    "070": {
        "slug": "executive-brief",
        "title": "Write an Executive Brief",
        "category": "research",
        "aliases": ["exec brief", "brief", "leadership brief"],
        "triggers": ["exec brief", "executive brief", "leadership update"],
        "input_types": ["topic", "audience"],
        "output_types": ["1-page executive brief"],
        "requires": ["topic or decision", "executive audience", "key facts"],
        "optional_inputs": ["constraints"],
        "produces": ["1-page brief", "recommendation", "ask"],
        "related": ["decision-memo", "report-review"],
        "playbooks": [],
        "purpose": "Compress a topic or decision into a one-page brief for executives.",
        "what": (
            "Produce a one-page brief: bottom line, why now, key facts, risks, recommended actions, and the ask."
        ),
        "why": (
            "Executives want the bottom line first. A short brief saves time and earns the next meeting."
        ),
        "when_use": [
            "You're briefing executives.",
            "You're preparing for a board update.",
        ],
        "when_not_use": [
            "The decision needs full criteria — use decision-memo (069).",
        ],
        "prepare": [
            "Topic or decision.",
            "Key facts.",
            "Audience.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Write bottom line.",
            "3. Add why now, key facts, risks, actions, ask.",
            "4. Trim to one page.",
        ],
        "what_get": [
            "One-page brief.",
            "Bottom line.",
            "Ask.",
        ],
        "next_steps": ["decision-memo (069)", "report-review (071)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: brief\n"
            "    description: one-page brief\n"
            "  - key: ask\n"
            "    description: explicit decision requested"
        ),
    },
    "071": {
        "slug": "report-review",
        "title": "Review a Report",
        "category": "research",
        "aliases": ["review report", "report audit", "manuscript review"],
        "triggers": ["review this report", "audit this report", "report feedback"],
        "input_types": ["report"],
        "output_types": ["review report"],
        "requires": ["report text", "criteria"],
        "optional_inputs": ["intended audience"],
        "produces": ["review report", "improvement suggestions"],
        "related": ["executive-brief", "reasoning-audit", "content-quality-review"],
        "playbooks": [],
        "purpose": "Review a report against clarity, evidence, and structure.",
        "what": (
            "Audit the report's clarity, evidence, structure, and conclusions. "
            "Return severity-tagged issues and improvement suggestions."
        ),
        "why": (
            "Reports often skip what an audience needs. A structured review turns rough drafts into publishable work."
        ),
        "when_use": [
            "You finished a report and want a second pass.",
            "You're reviewing someone else's report.",
        ],
        "when_not_use": [
            "You're reviewing prose — use content-quality-review (029).",
        ],
        "prepare": [
            "Report text.",
            "Review criteria.",
        ],
        "how_ai": [
            "1. Confirm criteria.",
            "2. Run each axis.",
            "3. Tag issues by severity.",
            "4. Recommend edits.",
        ],
        "what_get": [
            "Review report.",
            "Severity-tagged issues.",
            "Improvement suggestions.",
        ],
        "next_steps": ["content-quality-review (029)", "executive-brief (070)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: review\n"
            "    description: structured review\n"
            "  - key: severity_tags\n"
            "    description: per-issue severity"
        ),
    },
    # ---------------------------------------------------------------- 04-workflow 072-088
    "072": {
        "slug": "task-breakdown",
        "title": "Break a Task Down",
        "category": "workflow",
        "aliases": ["task breakdown", "subtasks", "decompose task"],
        "triggers": ["break this down", "decompose this task", "what are the steps"],
        "input_types": ["task", "context"],
        "output_types": ["task tree"],
        "requires": ["task description", "definition of done"],
        "optional_inputs": ["skills needed", "dependencies"],
        "produces": ["task tree", "time estimates", "dependencies"],
        "related": ["priority-planning", "weekly-plan", "project-plan"],
        "playbooks": ["plan-and-execute-a-project"],
        "purpose": "Break a task into actionable subtasks with clear definitions of done.",
        "what": (
            "Produce a task tree with 3–7 levels of depth, time estimates, dependencies, "
            "and acceptance criteria per leaf."
        ),
        "why": (
            "Unbroken tasks are skipped. Tasks with explicit subtasks and clear \"done\" conditions ship more reliably."
        ),
        "when_use": [
            "You're staring at a fuzzy task.",
            "You're estimating effort and need structure.",
        ],
        "when_not_use": [
            "You already have a project plan — use task-breakdown as the leaf step there.",
        ],
        "prepare": [
            "Task description.",
            "Definition of done.",
        ],
        "how_ai": [
            "1. Confirm task and definition of done.",
            "2. Break into subtasks.",
            "3. Time each.",
            "4. Mark dependencies.",
            "5. Add acceptance criteria.",
        ],
        "what_get": [
            "Task tree.",
            "Estimates.",
            "Dependencies.",
            "Acceptance criteria.",
        ],
        "next_steps": ["priority-planning (073)", "weekly-plan (074)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: task_tree\n"
            "    description: subtasks with estimates\n"
            "  - key: acceptance_criteria\n"
            "    description: done conditions"
        ),
    },
    "073": {
        "slug": "priority-planning",
        "title": "Plan Priorities",
        "category": "workflow",
        "aliases": ["priorities", "what to do first", "ranking"],
        "triggers": ["what to prioritize", "rank these", "priority order"],
        "input_types": ["list", "criteria"],
        "output_types": ["ranked list"],
        "requires": ["list of items", "criteria"],
        "optional_inputs": ["constraints"],
        "produces": ["ranked list", "rationale per item"],
        "related": ["task-breakdown", "goal-setting", "weekly-plan"],
        "playbooks": ["plan-and-execute-a-project"],
        "purpose": "Rank a list of items by explicit criteria.",
        "what": (
            "Apply a scoring rubric to rank items. Show the reasoning and any ties."
        ),
        "why": (
            "Unspoken priority means re-litigating every meeting. A transparent ranking ends the debate."
        ),
        "when_use": [
            "You have a backlog of competing items.",
            "Your team needs a defensible priority order.",
        ],
        "when_not_use": [
            "You only have a small todo list — use weekly-plan (074).",
        ],
        "prepare": [
            "List of items.",
            "Criteria and weights.",
        ],
        "how_ai": [
            "1. Confirm criteria.",
            "2. Score each item.",
            "3. Apply weights.",
            "4. Output the ranked list.",
        ],
        "what_get": [
            "Ranked list.",
            "Score table.",
            "Tie-breaker notes.",
        ],
        "next_steps": ["weekly-plan (074)", "task-breakdown (072)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: ranked_list\n"
            "    description: items in priority order\n"
            "  - key: rationale\n"
            "    description: rationale per item"
        ),
    },
    "074": {
        "slug": "weekly-plan",
        "title": "Plan the Week",
        "category": "workflow",
        "aliases": ["weekly planning", "this week", "week plan"],
        "triggers": ["plan my week", "this week", "weekly plan"],
        "input_types": ["tasks", "goals"],
        "output_types": ["weekly plan"],
        "requires": ["task list", "weekly goals", "constraints"],
        "optional_inputs": ["calendar"],
        "produces": ["day-by-day plan", "focus blocks", "weekly review checklist"],
        "related": ["task-breakdown", "priority-planning", "weekly-plan"],
        "playbooks": [],
        "purpose": "Plan a realistic week with focus blocks and a weekly review ritual.",
        "what": (
            "Build a day-by-day plan with focus blocks, meetings protected, "
            "and a Friday weekly-review ritual."
        ),
        "why": (
            "Weeks drift into meetings without explicit plans. A weekly plan protects focus time and builds review habits."
        ),
        "when_use": [
            "Sunday / Monday planning.",
            "A week got away from you and you want to reset.",
        ],
        "when_not_use": [
            "You only have one task — use task-breakdown (072).",
            "You're planning a long project — use project-plan (076).",
        ],
        "prepare": [
            "Task list.",
            "Weekly goals.",
            "Known meetings.",
        ],
        "how_ai": [
            "1. Confirm tasks and goals.",
            "2. Group by day and energy level.",
            "3. Block focus time.",
            "4. Add a Friday review.",
        ],
        "what_get": [
            "Day-by-day plan.",
            "Focus blocks.",
            "Friday review template.",
        ],
        "next_steps": ["self-review (088)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: weekly_plan\n"
            "    description: day-by-day plan\n"
            "  - key: review_template\n"
            "    description: Friday review checklist"
        ),
    },
    "075": {
        "slug": "goal-setting",
        "title": "Set Goals",
        "category": "workflow",
        "aliases": ["goals", "okrs", "set objectives"],
        "triggers": ["set goals", "okrs", "what should we aim for"],
        "input_types": ["context", "horizon"],
        "output_types": ["goals with criteria"],
        "requires": ["context or domain", "horizon (quarter, year)", "definition of success"],
        "optional_inputs": ["team or individual"],
        "produces": ["goal statement", "key results or success metrics"],
        "related": ["task-breakdown", "project-plan", "priority-planning"],
        "playbooks": ["plan-and-execute-a-project"],
        "purpose": "Set clear goals with measurable success criteria.",
        "what": (
            "Write a goal statement with 3–5 measurable key results. "
            "Distinguish outcomes from outputs and surface risks to each goal."
        ),
        "why": (
            "Goals without metrics are wishes. Goals with metrics force trade-offs and accountability."
        ),
        "when_use": [
            "You're starting a quarter or year.",
            "Your team lacks a shared definition of success.",
        ],
        "when_not_use": [
            "You want a single metric — use metric definition outside this workflow.",
        ],
        "prepare": [
            "Context or domain.",
            "Horizon.",
            "Definition of success.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Draft a goal statement.",
            "3. Add 3–5 key results.",
            "4. Identify risks.",
        ],
        "what_get": [
            "Goal statement.",
            "Key results with metrics.",
            "Risk list.",
        ],
        "next_steps": ["project-plan (076)", "task-breakdown (072)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: goals\n"
            "    description: goal + key results\n"
            "  - key: risks\n"
            "    description: risks to each goal"
        ),
    },
    "076": {
        "slug": "project-plan",
        "title": "Plan a Project",
        "category": "workflow",
        "aliases": ["project plan", "project management", "Gantt-style plan"],
        "triggers": ["project plan", "plan a project", "project management"],
        "input_types": ["project", "constraints"],
        "output_types": ["project plan"],
        "requires": ["objective", "milestones", "team or owner", "timeline"],
        "optional_inputs": ["dependencies", "risks"],
        "produces": ["milestones", "tasks per milestone", "owners", "risks"],
        "related": ["task-breakdown", "project-risk", "weekly-plan"],
        "playbooks": ["plan-and-execute-a-project"],
        "purpose": "Build a complete project plan with milestones, tasks, and risks.",
        "what": (
            "Produce a project plan: objective, milestones, tasks per milestone, "
            "owners, dependencies, risks, and a communication cadence."
        ),
        "why": (
            "Most projects fail from coordination, not from design. A plan makes coordination explicit."
        ),
        "when_use": [
            "You're starting a multi-week project.",
            "You need alignment across stakeholders.",
        ],
        "when_not_use": [
            "You only need a weekly cadence — use weekly-plan (074).",
        ],
        "prepare": [
            "Objective.",
            "Milestones.",
            "Team and timeline.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build milestones.",
            "3. Tasks per milestone.",
            "4. Owners and dependencies.",
            "5. Risks and communication cadence.",
        ],
        "what_get": [
            "Milestones.",
            "Tasks per milestone.",
            "Owners and dependencies.",
            "Risk register.",
        ],
        "next_steps": ["project-risk (077)", "weekly-plan (074)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: project_plan\n"
            "    description: full plan\n"
            "  - key: risk_register\n"
            "    description: risk list"
        ),
    },
    "077": {
        "slug": "project-risk",
        "title": "Manage Project Risks",
        "category": "workflow",
        "aliases": ["risk management", "project risks", "risk register"],
        "triggers": ["risk register", "project risks", "what could go wrong"],
        "input_types": ["project", "risks"],
        "output_types": ["risk register"],
        "requires": ["project or plan", "known risks"],
        "optional_inputs": ["stakeholders"],
        "produces": ["risk register", "mitigations", "owners"],
        "related": ["project-plan", "risk-stress-test"],
        "playbooks": ["plan-and-execute-a-project"],
        "purpose": "Identify, score, and mitigate project-level risks.",
        "what": (
            "Build a risk register: risk statement, likelihood, impact, score, mitigation, owner."
        ),
        "why": (
            "Risks that aren't tracked become incidents. A risk register makes risk visible and assignable."
        ),
        "when_use": [
            "You start any non-trivial project.",
            "A project slips and you want to reset.",
        ],
        "when_not_use": [
            "You want scenario planning for the future — use scenario-planning (068).",
        ],
        "prepare": [
            "Project summary.",
            "Known risks.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. List risks.",
            "3. Score likelihood and impact.",
            "4. Assign mitigations and owners.",
        ],
        "what_get": [
            "Risk register.",
            "Mitigations.",
            "Owners.",
        ],
        "next_steps": ["project-plan (076)", "weekly-plan (074)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: risk_register\n"
            "    description: scored risks\n"
            "  - key: mitigations\n"
            "    description: actions to reduce risk"
        ),
    },
    "078": {
        "slug": "meeting-agenda",
        "title": "Build a Meeting Agenda",
        "category": "workflow",
        "aliases": ["agenda", "meeting agenda", "meeting prep"],
        "triggers": ["meeting agenda", "agenda", "meeting prep"],
        "input_types": ["meeting goal", "attendees"],
        "output_types": ["meeting agenda"],
        "requires": ["meeting goal", "attendees or roles", "time budget"],
        "optional_inputs": ["pre-read"],
        "produces": ["agenda", "pre-read list", "decision points"],
        "related": ["meeting-notes", "podcast-interview"],
        "playbooks": [],
        "purpose": "Build a tight meeting agenda that ends on time with clear decisions.",
        "what": (
            "Produce an agenda with time boxes per item, decision points, "
            "who is responsible for each, and a pre-read list."
        ),
        "why": (
            "Meetings without agendas turn into status reports. Tight agendas force decisions and respect time."
        ),
        "when_use": [
            "You're scheduling a meeting.",
            "Past meetings have run over or ended without decisions.",
        ],
        "when_not_use": [
            "You're hosting a podcast — use podcast-interview (018).",
        ],
        "prepare": [
            "Meeting goal.",
            "Attendees.",
            "Time budget.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build agenda.",
            "3. Add time boxes.",
            "4. Mark decisions.",
            "5. Add pre-read list.",
        ],
        "what_get": [
            "Agenda.",
            "Pre-read list.",
            "Decisions list.",
        ],
        "next_steps": ["meeting-notes (079)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: agenda\n"
            "    description: agenda with time boxes\n"
            "  - key: pre_read\n"
            "    description: required pre-reading"
        ),
    },
    "079": {
        "slug": "meeting-notes",
        "title": "Take Meeting Notes",
        "category": "workflow",
        "aliases": ["meeting notes", "note-taking", "minutes"],
        "triggers": ["take notes", "meeting minutes", "capture this meeting"],
        "input_types": ["meeting context", "agenda"],
        "output_types": ["meeting notes"],
        "requires": ["agenda or goal", "transcript or rough notes"],
        "optional_inputs": ["attendees"],
        "produces": ["meeting notes", "decisions", "action items"],
        "related": ["meeting-agenda", "meeting-summary", "task-breakdown"],
        "playbooks": [],
        "purpose": "Turn a meeting into actionable notes with decisions and owners.",
        "what": (
            "Produce notes: agenda items, decisions, action items (who/what/when), and open questions."
        ),
        "why": (
            "Most meeting notes are unusable later. Structured notes give the absent a place to start and the present a record."
        ),
        "when_use": [
            "You're taking notes live.",
            "You want to summarize notes after a meeting.",
        ],
        "when_not_use": [
            "You only have a transcript — use meeting-summary (059).",
        ],
        "prepare": [
            "Agenda.",
            "Live or rough notes.",
        ],
        "how_ai": [
            "1. Confirm agenda.",
            "2. Capture per-item summary.",
            "3. Pull out decisions and action items.",
            "4. Note open questions.",
        ],
        "what_get": [
            "Meeting notes.",
            "Decisions.",
            "Action items.",
        ],
        "next_steps": ["task-breakdown (072)", "project-plan (076)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: notes\n"
            "    description: meeting notes\n"
            "  - key: action_items\n"
            "    description: who / what / when"
        ),
    },
    "080": {
        "slug": "sop-builder",
        "title": "Build a Standard Operating Procedure",
        "category": "workflow",
        "aliases": ["sop", "standard operating procedure", "playbook"],
        "triggers": ["sop", "standard operating procedure", "build a playbook"],
        "input_types": ["process", "audience"],
        "output_types": ["SOP"],
        "requires": ["process to document", "operator profile", "exceptions"],
        "optional_inputs": ["tools", "compliance"],
        "produces": ["SOP", "exceptions section", "quality check"],
        "related": ["checklist-builder", "documentation-template"],
        "playbooks": [],
        "purpose": "Document a repeatable process so others can execute it consistently.",
        "what": (
            "Produce a SOP with purpose, scope, prerequisites, numbered steps, "
            "an exceptions section, and a quality check."
        ),
        "why": (
            "Processes that live in one person's head create bus-factor risk. SOPs scale without sacrificing quality."
        ),
        "when_use": [
            "You're scaling a process across people or teams.",
            "Your team keeps making the same mistakes.",
        ],
        "when_not_use": [
            "You're building a quick checklist — use checklist-builder (081).",
        ],
        "prepare": [
            "Process description.",
            "Operator profile.",
            "Known exceptions.",
        ],
        "how_ai": [
            "1. Confirm process.",
            "2. List prerequisites.",
            "3. Number the steps.",
            "4. Add exceptions and quality check.",
        ],
        "what_get": [
            "SOP.",
            "Exceptions list.",
            "Quality check.",
        ],
        "next_steps": ["checklist-builder (081)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: sop\n"
            "    description: structured SOP\n"
            "  - key: exceptions\n"
            "    description: known exceptions"
        ),
    },
    "081": {
        "slug": "checklist-builder",
        "title": "Build a Checklist",
        "category": "workflow",
        "aliases": ["checklist", "todo list", "preflight"],
        "triggers": ["checklist", "preflight", "verification list"],
        "input_types": ["process"],
        "output_types": ["checklist"],
        "requires": ["process or context", "verification criteria"],
        "optional_inputs": ["roles", "frequencies"],
        "produces": ["checklist", "grouping by phase", "verification rules"],
        "related": ["sop-builder", "documentation-template"],
        "playbooks": [],
        "purpose": "Build a checklist that catches the most common omissions.",
        "what": (
            "Produce a checklist grouped by phase or role, with verification rules where useful."
        ),
        "why": (
            "Checklists beat memory. Even experts miss steps under pressure; checklists catch them cheaply."
        ),
        "when_use": [
            "You're running a recurring process.",
            "You want a pre-flight check before shipping.",
        ],
        "when_not_use": [
            "The process is poorly defined — use sop-builder (080) first.",
        ],
        "prepare": [
            "Process context.",
            "Common omissions or past mistakes.",
        ],
        "how_ai": [
            "1. Confirm context.",
            "2. List the steps.",
            "3. Group by phase.",
            "4. Add verification rules where helpful.",
        ],
        "what_get": [
            "Grouped checklist.",
            "Verification rules.",
        ],
        "next_steps": ["sop-builder (080)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: checklist\n"
            "    description: grouped checklist\n"
            "  - key: verification_rules\n"
            "    description: rules per item"
        ),
    },
    "082": {
        "slug": "documentation-template",
        "title": "Create a Documentation Template",
        "category": "workflow",
        "aliases": ["doc template", "documentation template", "doc scaffold"],
        "triggers": ["doc template", "documentation template", "create a doc scaffold"],
        "input_types": ["doc purpose"],
        "output_types": ["doc template"],
        "requires": ["documentation purpose", "audience"],
        "optional_inputs": ["style guide"],
        "produces": ["template skeleton", "section guidance"],
        "related": ["sop-builder", "checklist-builder", "knowledge-organization"],
        "playbooks": [],
        "purpose": "Build a documentation template that fits a recurring need.",
        "what": (
            "Produce a doc template with section structure, section guidance, and example snippets."
        ),
        "why": (
            "Ad-hoc docs drift in style and depth. Templates keep documentation consistent and reviewable."
        ),
        "when_use": [
            "You're scaling documentation across a team.",
            "Your existing docs are inconsistent.",
        ],
        "when_not_use": [
            "You're documenting one process — use sop-builder (080).",
        ],
        "prepare": [
            "Doc purpose.",
            "Audience.",
            "Style guide (optional).",
        ],
        "how_ai": [
            "1. Confirm purpose.",
            "2. List sections.",
            "3. Add guidance per section.",
            "4. Provide example snippets.",
        ],
        "what_get": [
            "Template skeleton.",
            "Section guidance.",
            "Example snippets.",
        ],
        "next_steps": ["sop-builder (080)", "knowledge-organization (083)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: template\n"
            "    description: doc skeleton\n"
            "  - key: guidance\n"
            "    description: per-section guidance"
        ),
    },
    "083": {
        "slug": "knowledge-organization",
        "title": "Organize a Knowledge Base",
        "category": "workflow",
        "aliases": ["organize notes", "knowledge organization", "taxonomy", "wiki"],
        "triggers": ["organize notes", "knowledge base", "set up a wiki"],
        "input_types": ["content corpus"],
        "output_types": ["information architecture"],
        "requires": ["content corpus or domain", "users"],
        "optional_inputs": ["existing taxonomy"],
        "produces": ["information architecture", "taxonomy", "naming rules"],
        "related": ["documentation-template", "knowledge-map", "classification"],
        "playbooks": [],
        "purpose": "Design an information architecture for a knowledge base.",
        "what": (
            "Produce an information architecture: top-level categories, subcategories, naming rules, and tagging conventions."
        ),
        "why": (
            "A messy knowledge base wastes more time than it saves. A clean architecture turns notes into leverage."
        ),
        "when_use": [
            "Your team notes are scattered.",
            "You're setting up a wiki or Notion space.",
        ],
        "when_not_use": [
            "You're writing one document — use documentation-template (082).",
        ],
        "prepare": [
            "Content or domain summary.",
            "User roles.",
            "Existing taxonomy (optional).",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Propose categories.",
            "3. Set naming rules.",
            "4. Define tagging conventions.",
        ],
        "what_get": [
            "Information architecture.",
            "Naming rules.",
            "Tagging conventions.",
        ],
        "next_steps": ["documentation-template (082)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: architecture\n"
            "    description: categories and subcategories\n"
            "  - key: naming_rules\n"
            "    description: naming conventions"
        ),
    },
    "084": {
        "slug": "automation-opportunity",
        "title": "Find Automation Opportunities",
        "category": "workflow",
        "aliases": ["automation", "what to automate", "automate this"],
        "triggers": ["automate this", "what should i automate", "find automation"],
        "input_types": ["processes", "tools"],
        "output_types": ["automation candidates"],
        "requires": ["process list", "current tools"],
        "optional_inputs": ["effort estimates", "stakeholders"],
        "produces": ["automation candidates", "ROI notes", "risk notes"],
        "related": ["sop-builder", "task-breakdown"],
        "playbooks": [],
        "purpose": "Identify and prioritize automation opportunities.",
        "what": (
            "Score processes on volume, error cost, and automation cost. "
            "Recommend the top 3 with ROI notes and risk notes."
        ),
        "why": (
            "Most teams automate the wrong things first. A scoring rubric reveals which automation actually pays back."
        ),
        "when_use": [
            "You're feeling manual work piling up.",
            "You want to pitch automation to leadership.",
        ],
        "when_not_use": [
            "You're documenting one process — use sop-builder (080).",
        ],
        "prepare": [
            "Process list.",
            "Current tools.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Score each process.",
            "3. Recommend the top 3.",
            "4. Add risk and ROI notes.",
        ],
        "what_get": [
            "Top 3 candidates.",
            "Scoring rationale.",
            "Risk and ROI notes.",
        ],
        "next_steps": ["sop-builder (080)", "task-breakdown (072)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: candidates\n"
            "    description: top automation candidates\n"
            "  - key: roi_notes\n"
            "    description: ROI rationale"
        ),
    },
    "085": {
        "slug": "learning-path",
        "title": "Design a Learning Path",
        "category": "workflow",
        "aliases": ["learning plan", "study plan", "course plan"],
        "triggers": ["learning path", "how to learn", "study plan"],
        "input_types": ["topic", "level"],
        "output_types": ["learning path"],
        "requires": ["topic", "current level", "goal level", "time budget"],
        "optional_inputs": ["preferred format", "tools"],
        "produces": ["learning path", "milestones", "resources"],
        "related": ["concept-explanation", "practice-design"],
        "playbooks": [],
        "purpose": "Build a learning path that takes you from current to goal level.",
        "what": (
            "Produce a learning path with phases, milestones, recommended resources, and verification exercises."
        ),
        "why": (
            "Self-learning fails when it lacks structure. A path turns \"learn X\" into \"do A, then B, then C\"."
        ),
        "when_use": [
            "You're learning a new skill.",
            "You're onboarding someone to a topic.",
        ],
        "when_not_use": [
            "You just need a single concept explained — use concept-explanation (086).",
        ],
        "prepare": [
            "Topic.",
            "Current and goal level.",
            "Time budget.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Build phases.",
            "3. Pick resources.",
            "4. Add verification per phase.",
        ],
        "what_get": [
            "Learning path.",
            "Milestones.",
            "Resources and verification per phase.",
        ],
        "next_steps": ["concept-explanation (086)", "practice-design (087)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: path\n"
            "    description: phased learning plan\n"
            "  - key: resources\n"
            "    description: resource list"
        ),
    },
    "086": {
        "slug": "concept-explanation",
        "title": "Explain a Concept",
        "category": "workflow",
        "aliases": ["explain", "what is x", "concept explanation"],
        "triggers": ["explain", "what is", "how does x work"],
        "input_types": ["concept", "audience level"],
        "output_types": ["explanation"],
        "requires": ["concept", "audience level"],
        "optional_inputs": ["background", "desired depth"],
        "produces": ["explanation with examples", "analogy", "common pitfalls"],
        "related": ["learning-path", "practice-design", "knowledge-map"],
        "playbooks": [],
        "purpose": "Explain a concept in plain language with examples.",
        "what": (
            "Produce a multi-layer explanation: one-sentence summary, intuition, "
            "worked example, common pitfalls, and a deeper dive."
        ),
        "why": (
            "Most \"explanations\" are still jargon. Plain-language explanations with examples make concepts stick."
        ),
        "when_use": [
            "You're learning a new topic.",
            "You're teaching a concept to someone else.",
        ],
        "when_not_use": [
            "You want a full curriculum — use learning-path (085).",
        ],
        "prepare": [
            "Concept.",
            "Audience level.",
        ],
        "how_ai": [
            "1. Confirm concept and audience.",
            "2. Write a one-sentence summary.",
            "3. Add intuition and example.",
            "4. Note pitfalls.",
            "5. Offer a deeper dive.",
        ],
        "what_get": [
            "One-sentence summary.",
            "Intuition.",
            "Worked example.",
            "Common pitfalls.",
            "Deeper dive pointer.",
        ],
        "next_steps": ["learning-path (085)", "practice-design (087)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: explanation\n"
            "    description: multi-layer explanation\n"
            "  - key: analogy\n"
            "    description: analogy used"
        ),
    },
    "087": {
        "slug": "practice-design",
        "title": "Design a Practice Exercise",
        "category": "workflow",
        "aliases": ["practice exercise", "drill", "exercise design"],
        "triggers": ["design a drill", "practice exercise", "deliberate practice"],
        "input_types": ["skill", "current level"],
        "output_types": ["practice exercise"],
        "requires": ["skill", "current level", "available time"],
        "optional_inputs": ["tools", "feedback source"],
        "produces": ["exercise", "feedback criteria", "success threshold"],
        "related": ["learning-path", "concept-explanation"],
        "playbooks": [],
        "purpose": "Design a focused practice exercise for a chosen skill.",
        "what": (
            "Produce an exercise: setup, instructions, feedback criteria, "
            "and what success looks like."
        ),
        "why": (
            "Practice without feedback builds habits, not skill. Deliberate practice is specific, measurable, and revisitable."
        ),
        "when_use": [
            "You're learning a skill and need structured drills.",
            "You're designing a course or workshop.",
        ],
        "when_not_use": [
            "You want general encouragement — use learning-path (085) instead.",
        ],
        "prepare": [
            "Skill.",
            "Current level.",
            "Time available.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Write the exercise.",
            "3. Define feedback.",
            "4. Define success.",
        ],
        "what_get": [
            "Exercise.",
            "Feedback criteria.",
            "Success threshold.",
        ],
        "next_steps": ["self-review (088)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: exercise\n"
            "    description: exercise instructions\n"
            "  - key: feedback\n"
            "    description: feedback criteria"
        ),
    },
    "088": {
        "slug": "self-review",
        "title": "Run a Personal Review",
        "category": "workflow",
        "aliases": ["self review", "weekly review", "retrospective"],
        "triggers": ["weekly review", "self review", "retrospective"],
        "input_types": ["period", "data"],
        "output_types": ["self-review"],
        "requires": ["period (week, month, quarter)", "highlights and lowlights"],
        "optional_inputs": ["goals"],
        "produces": ["self-review", "lessons learned", "next-period commitments"],
        "related": ["weekly-plan", "goal-setting"],
        "playbooks": [],
        "purpose": "Run a structured personal review for a chosen period.",
        "what": (
            "Build a review: highlights, lowlights, lessons, and next-period commitments. "
            "Connect lessons to specific actions."
        ),
        "why": (
            "Reflection is only useful when it changes behavior. A review converts experience into the next plan."
        ),
        "when_use": [
            "End of week / month / quarter.",
            "You're stuck and want to reset.",
        ],
        "when_not_use": [
            "You're auditing a project's outcomes — use project-risk (077).",
        ],
        "prepare": [
            "Period.",
            "Highlights and lowlights.",
            "Goals (optional).",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Structure highlights/lowlights.",
            "3. Draw lessons.",
            "4. Propose next-period commitments.",
        ],
        "what_get": [
            "Self-review.",
            "Lessons.",
            "Next-period commitments.",
        ],
        "next_steps": ["goal-setting (075)", "weekly-plan (074)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: review\n"
            "    description: structured review\n"
            "  - key: next_commitments\n"
            "    description: next-period commitments"
        ),
    },
    # ---------------------------------------------------------------- 05-technical 089-100
    "089": {
        "slug": "prompt-designer",
        "title": "Design a Prompt from Scratch",
        "category": "technical",
        "aliases": ["prompt design", "design a prompt", "system prompt"],
        "triggers": ["design a prompt", "system prompt", "write a prompt for", "new prompt"],
        "input_types": ["task", "model constraints"],
        "output_types": ["prompt"],
        "requires": ["task description", "model or system constraints", "examples"],
        "optional_inputs": ["evaluation criteria", "tone"],
        "produces": ["prompt", "rationale", "test cases"],
        "related": ["prompt-improvement", "agent-task-spec", "debugging"],
        "playbooks": [],
        "purpose": "Design a prompt from scratch with explicit structure and rationale.",
        "what": (
            "Build a prompt with role, inputs, instructions, output format, "
            "constraints, and 3 example test cases."
        ),
        "why": (
            "First-draft prompts are vague and brittle. Structured prompts document the intent and stay portable."
        ),
        "when_use": [
            "You're building a prompt for a new workflow.",
            "You're handing a prompt to teammates or contractors.",
        ],
        "when_not_use": [
            "You already have a prompt and want to improve it — use prompt-improvement (090).",
        ],
        "prepare": [
            "Task description.",
            "Model or system constraints.",
            "Examples.",
        ],
        "how_ai": [
            "1. Confirm task and constraints.",
            "2. Draft a structured prompt.",
            "3. Add 3 test cases.",
            "4. Document rationale.",
        ],
        "what_get": [
            "Prompt.",
            "Rationale.",
            "3 test cases.",
        ],
        "next_steps": ["prompt-improvement (090)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: prompt\n"
            "    description: structured prompt\n"
            "  - key: test_cases\n"
            "    description: example inputs and expected outputs"
        ),
    },
    "090": {
        "slug": "prompt-improvement",
        "title": "Improve an Existing Prompt",
        "category": "technical",
        "aliases": ["improve prompt", "tune prompt", "prompt audit"],
        "triggers": ["improve my prompt", "tune this prompt", "audit this prompt"],
        "input_types": ["prompt", "issues"],
        "output_types": ["improved prompt", "change summary"],
        "requires": ["prompt text", "failing or weak examples"],
        "optional_inputs": ["evaluation criteria", "constraints"],
        "produces": ["improved prompt", "rationale", "test cases"],
        "related": ["prompt-designer", "code-review", "debugging"],
        "playbooks": [],
        "purpose": "Diagnose and improve an existing prompt.",
        "what": (
            "Identify failure modes, propose a rewrite, and explain each change. "
            "Provide new test cases targeting the failures."
        ),
        "why": (
            "Most prompt regressions come from unclear instructions or missing constraints. A targeted rewrite fixes them."
        ),
        "when_use": [
            "A prompt works but feels inconsistent.",
            "The model often misses a constraint.",
        ],
        "when_not_use": [
            "You're starting a new prompt — use prompt-designer (089).",
        ],
        "prepare": [
            "Prompt text.",
            "Failing examples.",
        ],
        "how_ai": [
            "1. Diagnose failure modes.",
            "2. Propose rewrite.",
            "3. Explain changes.",
            "4. Add test cases.",
        ],
        "what_get": [
            "Improved prompt.",
            "Change rationale.",
            "New test cases.",
        ],
        "next_steps": ["prompt-designer (089)", "code-review (095)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: improved_prompt\n"
            "    description: new prompt text\n"
            "  - key: change_log\n"
            "    description: rationale per change"
        ),
    },
    "091": {
        "slug": "agent-task-spec",
        "title": "Spec an AI Agent Task",
        "category": "technical",
        "aliases": ["agent spec", "task spec", "agent task"],
        "triggers": ["agent task", "spec an agent", "ai agent brief"],
        "input_types": ["task", "agent capabilities"],
        "output_types": ["agent task spec"],
        "requires": ["task", "agent capabilities", "acceptance criteria"],
        "optional_inputs": ["tools", "budget"],
        "produces": ["agent task spec", "non-goals", "evaluation plan"],
        "related": ["prompt-designer", "code-generation", "system-design"],
        "playbooks": ["build-an-ai-agent-task"],
        "purpose": "Produce a precise AI agent task specification.",
        "what": (
            "Write an agent task spec: objective, inputs, outputs, acceptance criteria, "
            "non-goals, tool access, and an evaluation plan."
        ),
        "why": (
            "Vague agent briefs produce inconsistent behavior. A precise spec is the difference between useful automation and a demo."
        ),
        "when_use": [
            "You're setting up an agent task.",
            "You're briefing a build for an agent.",
        ],
        "when_not_use": [
            "You're generating code — use code-generation (093) or system-design (100).",
        ],
        "prepare": [
            "Task description.",
            "Agent capabilities.",
            "Acceptance criteria.",
        ],
        "how_ai": [
            "1. Confirm inputs.",
            "2. Define objective and inputs.",
            "3. Specify outputs and acceptance criteria.",
            "4. State non-goals.",
            "5. Define tool access and evaluation plan.",
        ],
        "what_get": [
            "Agent task spec.",
            "Non-goals.",
            "Evaluation plan.",
        ],
        "next_steps": ["code-generation (093)", "system-design (100)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: agent_spec\n"
            "    description: structured agent brief\n"
            "  - key: acceptance_criteria\n"
            "    description: success criteria"
        ),
    },
    "092": {
        "slug": "code-explanation",
        "title": "Explain Code",
        "category": "technical",
        "aliases": ["explain code", "what does this code do", "code walkthrough"],
        "triggers": ["explain this code", "what does this code do", "walk me through this"],
        "input_types": ["code"],
        "output_types": ["code explanation"],
        "requires": ["code snippet or repo pointer", "audience level"],
        "optional_inputs": ["focus areas", "background"],
        "produces": ["layered explanation", "diagram suggestion", "open questions"],
        "related": ["code-review", "code-generation", "system-design"],
        "playbooks": [],
        "purpose": "Explain code in a layered way for the chosen audience.",
        "what": (
            "Produce a layered explanation: one-sentence summary, "
            "control flow, data flow, edge cases, and a deeper dive for the curious."
        ),
        "why": (
            "Most code explanations are too dense for newcomers and too shallow for experienced engineers. "
            "Layered explanations serve both."
        ),
        "when_use": [
            "You're learning a new codebase.",
            "You're documenting legacy code.",
        ],
        "when_not_use": [
            "You want bugs caught — use code-review (095) or debugging (094).",
        ],
        "prepare": [
            "Code.",
            "Audience level.",
        ],
        "how_ai": [
            "1. Confirm code and audience.",
            "2. One-sentence summary.",
            "3. Control flow and data flow.",
            "4. Edge cases.",
            "5. Deeper dive pointer.",
        ],
        "what_get": [
            "Layered explanation.",
            "Diagram suggestion.",
            "Open questions.",
        ],
        "next_steps": ["code-review (095)", "system-design (100)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: explanation\n"
            "    description: layered walkthrough\n"
            "  - key: diagram\n"
            "    description: visual aid suggestion"
        ),
    },
    "093": {
        "slug": "code-generation",
        "title": "Generate Code",
        "category": "technical",
        "aliases": ["write code", "implement", "code generation"],
        "triggers": ["write this code", "implement this", "generate code"],
        "input_types": ["task spec"],
        "output_types": ["code"],
        "requires": ["task spec (objective, inputs, outputs)", "language and constraints", "acceptance criteria"],
        "optional_inputs": ["style guide", "test framework"],
        "produces": ["code", "tests", "usage notes"],
        "related": ["code-review", "debugging", "system-design"],
        "playbooks": ["build-an-ai-agent-task"],
        "purpose": "Generate code that satisfies a task spec.",
        "what": (
            "Read the spec and produce code with tests, "
            "edge-case handling, and usage notes."
        ),
        "why": (
            "Generated code without a spec is brittle. A spec makes the generation testable and the code auditable."
        ),
        "when_use": [
            "You have a small task spec and want code.",
            "You're scripting a one-off.",
        ],
        "when_not_use": [
            "You're designing architecture — use system-design (100).",
            "You don't yet have a spec — use agent-task-spec (091) first.",
        ],
        "prepare": [
            "Task spec.",
            "Language and constraints.",
            "Acceptance criteria.",
        ],
        "how_ai": [
            "1. Confirm spec.",
            "2. Generate code.",
            "3. Add tests.",
            "4. Note edge cases.",
            "5. Provide usage notes.",
        ],
        "what_get": [
            "Code.",
            "Tests.",
            "Usage notes.",
            "Edge cases.",
        ],
        "next_steps": ["code-review (095)", "debugging (094)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: code\n"
            "    description: generated code\n"
            "  - key: tests\n"
            "    description: test coverage"
        ),
    },
    "094": {
        "slug": "debugging",
        "title": "Debug Failing Code",
        "category": "technical",
        "aliases": ["debug", "fix bug", "failing code"],
        "triggers": ["this is broken", "debug this", "find the bug"],
        "input_types": ["failing code", "error"],
        "output_types": ["debug plan", "fix"],
        "requires": ["failing code or error message", "reproduction steps"],
        "optional_inputs": ["logs", "expected vs actual"],
        "produces": ["root-cause candidates", "fix proposal", "verification plan"],
        "related": ["code-review", "code-explanation"],
        "playbooks": [],
        "purpose": "Diagnose and propose a fix for failing code.",
        "what": (
            "Reproduce mentally, list root-cause candidates ranked by likelihood, "
            "propose a fix, and define how to verify the fix."
        ),
        "why": (
            "Most debugging time is spent on the wrong hypothesis. Structured root-cause ranking shortens the loop."
        ),
        "when_use": [
            "Your code fails or returns wrong output.",
            "You have an error message and don't know where to start.",
        ],
        "when_not_use": [
            "You're auditing code quality — use code-review (095).",
        ],
        "prepare": [
            "Code.",
            "Error or reproduction steps.",
        ],
        "how_ai": [
            "1. Confirm code and error.",
            "2. List root-cause candidates ranked by likelihood.",
            "3. Propose a fix.",
            "4. Define verification.",
        ],
        "what_get": [
            "Root-cause candidates.",
            "Fix proposal.",
            "Verification plan.",
        ],
        "next_steps": ["code-review (095)", "code-generation (093)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: root_cause\n"
            "    description: top candidate cause\n"
            "  - key: fix\n"
            "    description: proposed fix"
        ),
    },
    "095": {
        "slug": "code-review",
        "title": "Review Code",
        "category": "technical",
        "aliases": ["review code", "PR review", "code audit"],
        "triggers": ["review my code", "PR review", "audit this code"],
        "input_types": ["code"],
        "output_types": ["review"],
        "requires": ["code diff or file", "review criteria (correctness, security, style)"],
        "optional_inputs": ["context", "tests"],
        "produces": ["review report", "severity-tagged issues", "improvement suggestions"],
        "related": ["code-explanation", "debugging", "prompt-improvement"],
        "playbooks": [],
        "purpose": "Review code against correctness, security, and style criteria.",
        "what": (
            "Audit code on correctness, security, performance, readability, and tests. "
            "Return severity-tagged issues and concrete suggestions."
        ),
        "why": (
            "Most bugs hide in the corners of code that's \"working\". A structured review catches them before they ship."
        ),
        "when_use": [
            "You're submitting a PR.",
            "You're inheriting new code.",
        ],
        "when_not_use": [
            "The code is failing — use debugging (094) first.",
        ],
        "prepare": [
            "Code.",
            "Review criteria.",
            "Context.",
        ],
        "how_ai": [
            "1. Confirm criteria.",
            "2. Run each axis.",
            "3. Tag issues by severity.",
            "4. Recommend fixes.",
        ],
        "what_get": [
            "Review report.",
            "Severity-tagged issues.",
            "Improvement suggestions.",
        ],
        "next_steps": ["debugging (094)", "code-generation (093)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: review\n"
            "    description: structured review\n"
            "  - key: severity_tags\n"
            "    description: per-issue severity"
        ),
    },
    "096": {
        "slug": "data-exploration",
        "title": "Explore a Dataset",
        "category": "technical",
        "aliases": ["explore data", "data exploration", "EDA"],
        "triggers": ["explore this data", "eda", "what's in this dataset"],
        "input_types": ["dataset"],
        "output_types": ["exploration report"],
        "requires": ["dataset (path or sample)", "exploration goal"],
        "optional_inputs": ["columns of interest"],
        "produces": ["summary stats", "distributions", "anomalies", "questions"],
        "related": ["data-analysis", "data-extraction"],
        "playbooks": [],
        "purpose": "Run structured EDA on a dataset.",
        "what": (
            "Run structured EDA: shape, types, missing values, distributions, "
            "correlations, anomalies, and 5 questions worth answering next."
        ),
        "why": (
            "Most analyses skip exploration and produce fragile findings. EDA grounds the rest of the analysis."
        ),
        "when_use": [
            "You just received a dataset.",
            "You want to know what's in it before modeling.",
        ],
        "when_not_use": [
            "You're answering a specific question — use data-analysis (097).",
        ],
        "prepare": [
            "Dataset.",
            "Exploration goal.",
        ],
        "how_ai": [
            "1. Confirm dataset and goal.",
            "2. Run EDA.",
            "3. Surface anomalies.",
            "4. List next questions.",
        ],
        "what_get": [
            "Summary stats.",
            "Distributions.",
            "Anomalies.",
            "5 next questions.",
        ],
        "next_steps": ["data-analysis (097)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: eda_report\n"
            "    description: exploration findings\n"
            "  - key: anomalies\n"
            "    description: anomalies and warnings"
        ),
    },
    "097": {
        "slug": "data-analysis",
        "title": "Answer a Question with Data",
        "category": "technical",
        "aliases": ["analyze data", "answer with data", "data analysis"],
        "triggers": ["answer with data", "analyze the data", "what does the data show"],
        "input_types": ["dataset", "question"],
        "output_types": ["analysis"],
        "requires": ["dataset", "question", "audience"],
        "optional_inputs": ["hypothesis", "control variables"],
        "produces": ["answer with evidence", "caveats", "next questions"],
        "related": ["data-exploration", "data-extraction", "decision-memo"],
        "playbooks": [],
        "purpose": "Answer a specific question with data.",
        "what": (
            "Plan the analysis, run it, and report the answer with caveats. "
            "Surface what's not in the data."
        ),
        "why": (
            "Most \"data answers\" are guesses. A planned analysis that says what it can and can't conclude earns trust."
        ),
        "when_use": [
            "You have a specific business question and clean data.",
            "You're preparing a chart or table for a decision.",
        ],
        "when_not_use": [
            "You don't yet know the dataset — use data-exploration (096) first.",
        ],
        "prepare": [
            "Dataset.",
            "Question.",
            "Audience.",
        ],
        "how_ai": [
            "1. Confirm question.",
            "2. Plan analysis.",
            "3. Run it.",
            "4. Report answer + caveats.",
            "5. Suggest next questions.",
        ],
        "what_get": [
            "Answer with evidence.",
            "Caveats.",
            "Next questions.",
        ],
        "next_steps": ["decision-memo (069)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: answer\n"
            "    description: structured answer\n"
            "  - key: caveats\n"
            "    description: known limitations"
        ),
    },
    "098": {
        "slug": "schema-design",
        "title": "Design a Schema",
        "category": "technical",
        "aliases": ["schema", "database schema", "data model"],
        "triggers": ["design a schema", "database design", "data model"],
        "input_types": ["data requirements"],
        "output_types": ["schema"],
        "requires": ["data requirements", "query patterns"],
        "optional_inputs": ["scale", "constraints"],
        "produces": ["entity model", "field definitions", "index strategy", "sample queries"],
        "related": ["system-design", "api-integration", "data-analysis"],
        "playbooks": [],
        "purpose": "Design a data schema for the requirements and query patterns.",
        "what": (
            "Build a schema: entities, fields, types, relationships, indexes, and 3 sample queries."
        ),
        "why": (
            "Most schema regret comes from mismatched query patterns. Designing around the real queries avoids rewrites."
        ),
        "when_use": [
            "You're starting a new app or feature.",
            "You're restructuring an existing schema.",
        ],
        "when_not_use": [
            "You're designing whole-system architecture — use system-design (100).",
        ],
        "prepare": [
            "Data requirements.",
            "Query patterns.",
        ],
        "how_ai": [
            "1. Confirm requirements and queries.",
            "2. Identify entities.",
            "3. Define fields and types.",
            "4. Mark indexes.",
            "5. Write sample queries.",
        ],
        "what_get": [
            "Entity model.",
            "Field definitions.",
            "Index strategy.",
            "Sample queries.",
        ],
        "next_steps": ["api-integration (099)", "system-design (100)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: schema\n"
            "    description: entity and field definitions\n"
            "  - key: indexes\n"
            "    description: index strategy"
        ),
    },
    "099": {
        "slug": "api-integration",
        "title": "Design an API Integration",
        "category": "technical",
        "aliases": ["api integration", "integrate with api", "third-party api"],
        "triggers": ["integrate an api", "third-party api", "build an integration"],
        "input_types": ["provider", "use case"],
        "output_types": ["integration plan"],
        "requires": ["provider and use case", "constraints (auth, rate limits, latency)"],
        "optional_inputs": ["data shape", "environments"],
        "produces": ["integration plan", "auth and rate-limit handling", "error handling", "tests"],
        "related": ["system-design", "schema-design", "code-review"],
        "playbooks": [],
        "purpose": "Plan an API integration with predictable error handling.",
        "what": (
            "Produce an integration plan: auth, rate-limit handling, retries, idempotency, "
            "error handling, logging, tests, and observability."
        ),
        "why": (
            "Most integrations break at the corners: rate limits, retries, partial failures. A plan closes the corners early."
        ),
        "when_use": [
            "You're integrating with a third-party API.",
            "You're rebuilding an existing integration that's flaky.",
        ],
        "when_not_use": [
            "You're designing whole-system architecture — use system-design (100).",
        ],
        "prepare": [
            "Provider.",
            "Use case.",
            "Constraints.",
        ],
        "how_ai": [
            "1. Confirm use case.",
            "2. Map provider endpoints.",
            "3. Define auth and rate-limit handling.",
            "4. Define retries, idempotency, error handling.",
            "5. Specify tests and observability.",
        ],
        "what_get": [
            "Integration plan.",
            "Auth and rate-limit handling.",
            "Error handling.",
            "Tests.",
        ],
        "next_steps": ["code-generation (093)", "code-review (095)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: integration_plan\n"
            "    description: structured plan\n"
            "  - key: error_strategy\n"
            "    description: retries and idempotency"
        ),
    },
    "100": {
        "slug": "system-design",
        "title": "Design a System",
        "category": "technical",
        "aliases": ["system design", "architecture", "tech design"],
        "triggers": ["system design", "architecture", "design this system"],
        "input_types": ["requirements"],
        "output_types": ["system design"],
        "requires": ["requirements (functional + non-functional)", "constraints (scale, budget, team)"],
        "optional_inputs": ["existing system context"],
        "produces": ["architecture", "components", "data flow", "trade-offs", "open questions"],
        "related": ["schema-design", "api-integration", "agent-task-spec"],
        "playbooks": ["build-an-ai-agent-task"],
        "purpose": "Design the architecture for a system that meets stated requirements.",
        "what": (
            "Produce a system design: requirements, architecture, components, "
            "data flow, trade-offs, decisions, and open questions."
        ),
        "why": (
            "Most systems accrue complexity without explicit design. A written design is the contract the team builds against."
        ),
        "when_use": [
            "You're building a non-trivial system.",
            "A stakeholder asks how the system works.",
        ],
        "when_not_use": [
            "You only need a database schema — use schema-design (098).",
            "You only need an API integration — use api-integration (099).",
        ],
        "prepare": [
            "Requirements.",
            "Constraints.",
        ],
        "how_ai": [
            "1. Confirm requirements and constraints.",
            "2. List components.",
            "3. Map data flow.",
            "4. State trade-offs.",
            "5. List open questions.",
        ],
        "what_get": [
            "Architecture.",
            "Components.",
            "Data flow.",
            "Trade-offs.",
            "Open questions.",
        ],
        "next_steps": ["schema-design (098)", "api-integration (099)", "code-generation (093)"],
        "handoff_text": (
            "handoff:\n"
            "  - key: architecture\n"
            "    description: components and data flow\n"
            "  - key: trade_offs\n"
            "    description: explicit trade-offs"
        ),
    },
}


def render_frontmatter(entry):
    """Render the YAML frontmatter block for a workflow entry."""
    def fmt_list(key):
        items = entry.get(key, [])
        if not items:
            return f"{key}: []\n"
        return f"{key}:\n" + "\n".join(f"  - {item}" for item in items) + "\n"

    def fmt_handoff():
        items = entry.get("handoff_keys", [])
        if not items:
            return "handoff: []\n"
        lines = ["handoff:"]
        for item in items:
            lines.append(f"  - key: {item['key']}")
            lines.append(f"    description: \"{item['description']}\"")
        return "\n".join(lines) + "\n"

    return (
        "---\n"
        f"id: \"{entry['id']}\"\n"
        f"slug: \"{entry['slug']}\"\n"
        f"title: \"{entry['title']}\"\n"
        f"category: \"{entry['category']}\"\n"
        + fmt_list("aliases")
        + fmt_list("triggers")
        + fmt_list("input_types")
        + fmt_list("output_types")
        + fmt_list("requires")
        + fmt_list("produces")
        + fmt_list("related")
        + fmt_list("playbooks")
        + fmt_list("mode_support")
        + "language_support:\n  input: auto-detect\n  output: mirror-user-language\n"
        + fmt_localization(entry["id"])
        + fmt_handoff()
        + "---\n"
    )


def fmt_localization(idn: str) -> str:
    """Render the `localization:` block from LOCALIZATION_OVERRIDES.

    Workflows not in the override map produce an empty string — the router
    falls back to the category default documented in
    `templates/WORKFLOW_TEMPLATE.md`.
    """
    spec = LOCALIZATION_OVERRIDES.get(idn)
    if not spec:
        return ""

    override = spec.get("locale_override")
    if override:
        overrides_block = (
            "  locale_style_profile_overrides:\n"
            f"    zh-TW: {override}\n"
        )
    else:
        # Empty value — router falls back to category default.
        overrides_block = (
            "  locale_style_profile_overrides:\n"
            "    zh-TW:\n"
        )

    return (
        "localization:\n"
        "  supported_locales:\n"
        "    - en\n"
        "    - zh-TW\n"
        f"  default_style_profile: {spec['default_style_profile']}\n"
        f"{overrides_block}"
        f"  editing_intensity: {spec['editing_intensity']}\n"
    )


def render_body(entry):
    """Render the markdown body for a workflow entry."""
    cat = entry["category"]
    cat_dir = CATEGORY_DIR[cat]
    idn = entry["id"]
    related_links = "\n".join(
        f"- [{r}](../{guess_dir_for_slug(r, cat)}/{guess_id_for_slug(r)}-{r}.md)"
        for r in entry["related"]
    )
    next_links = "\n".join(f"- {n}" for n in entry["next_steps"])

    parts = []
    parts.append(f"# {idn} — {entry['title']}\n")
    parts.append("## What is this?\n")
    parts.append(entry["what"].strip() + "\n")
    parts.append("## Why use it?\n")
    parts.append(entry["why"].strip() + "\n")
    parts.append("## When should I use it?\n")
    for b in entry["when_use"]:
        parts.append(f"- {b}")
    parts.append("")
    parts.append("## When should I not use it?\n")
    for b in entry["when_not_use"]:
        parts.append(f"- {b}")
    parts.append("")
    parts.append("## What should I prepare?\n")
    for b in entry["prepare"]:
        parts.append(f"- {b}")
    parts.append("")
    parts.append("## How does the AI help me?\n")
    for b in entry["how_ai"]:
        parts.append(b)
    parts.append("")
    parts.append("## What will I get?\n")
    for b in entry["what_get"]:
        parts.append(f"- {b}")
    parts.append("")
    parts.append("## How to start\n")
    parts.append("Open a conversation with any AI that can read this repository and say:\n")
    parts.append("```\nRead this repository's START.md and help me with this:\n")
    parts.append("[describe what you want — your goal, topic, audience, and any constraints]\n```\n")
    parts.append("")
    parts.append("## Related workflows\n")
    parts.append(related_links)
    parts.append("")
    parts.append("## Recommended next steps\n")
    parts.append(next_links)
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## AI specification")
    parts.append("")
    parts.append("```text")
    parts.append(f"purpose: \"{entry['purpose']}\"")
    parts.append("required_inputs:")
    for r in entry["requires"]:
        parts.append(f"  - {r}")
    parts.append("optional_inputs:")
    for i in entry.get("optional_inputs", []):
        parts.append(f"  - {i}")
    parts.append("ask_if_missing:")
    parts.append("  - \"What is the desired outcome and who is it for?\"")
    parts.append("  - \"Any constraints on tone, length, or required terminology?\"")
    parts.append("do_not_use_when:")
    for b in entry["when_not_use"]:
        parts.append(f"  - \"{b}\"")
    parts.append("workflow:")
    for b in entry["how_ai"]:
        parts.append(f"  - \"{b}\"")
    parts.append("output_contract:")
    for o in entry["produces"]:
        parts.append(f"  - \"{o}\"")
    parts.append("quality_rules:")
    parts.append("  - \"Mirror the user's language unless another output language is requested.\"")
    parts.append("  - \"Do not invent facts, sources, numbers, or user context.\"")
    parts.append("  - \"Use current-source verification only when recency is material.\"")
    parts.append("  - \"Label assumptions and verification gaps explicitly.\"")
    parts.append("handoff:")
    parts.append(entry["handoff_text"])
    parts.append("```")
    return "\n".join(parts)


# Helpers to reconstruct directory & ID from a workflow slug.
# We rely on a category lookup table; the slug may not include the directory.

SLUG_INDEX = {}  # slug -> (category, id)


def build_index():
    for wid, e in WORKFLOWS.items():
        SLUG_INDEX[e["slug"]] = (e["category"], e["id"])


def guess_dir_for_slug(slug, default_category):
    build_index()
    if slug in SLUG_INDEX:
        return CATEGORY_DIR[SLUG_INDEX[slug][0]]
    return CATEGORY_DIR[default_category]


def guess_id_for_slug(slug):
    build_index()
    entry = SLUG_INDEX.get(slug)
    if entry is None:
        return "000"
    return entry[1]


def render_file(entry):
    parts = []
    parts.append(render_frontmatter(entry))
    parts.append("\n")
    parts.append(render_body(entry))
    return "\n".join(parts)


def main():
    # Pre-seed ids and the slug index once.
    for wid in sorted(WORKFLOWS.keys()):
        WORKFLOWS[wid]["id"] = wid
    build_index()
    for wid in sorted(WORKFLOWS.keys()):
        entry = WORKFLOWS[wid]
        # Defaults for any missing optional fields.
        entry.setdefault("mode_support", ["guide", "quick", "recommend"])
        entry.setdefault("optional_inputs", ["example or sample", "tone guide", "verification needs"])
        entry.setdefault("handoff_keys", [{"key": "context", "description": "summary of upstream context"}])
        cat = entry["category"]
        sub = WORKFLOWS_DIR / CATEGORY_DIR[cat]
        sub.mkdir(parents=True, exist_ok=True)
        path = sub / f"{wid}-{entry['slug']}.md"
        path.write_text(render_file(entry))
    print("Wrote", len(WORKFLOWS), "workflow files.")


if __name__ == "__main__":
    main()
