<a id="pmskills"></a>
# Product Manager Skills (Automattic)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](https://github.com/p3ob7o/Product-Manager-Skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/p3ob7o/Product-Manager-Skills/blob/main/CONTRIBUTING.md)
![Skills](https://img.shields.io/badge/skills-46-informational?style=flat-square)
![Commands](https://img.shields.io/badge/commands-6-informational?style=flat-square)

> **Fork notice:** This is a fork of [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills) by [Dean Peters](https://linkedin.com/in/deanpeters). The original project provides 46 battle-tested PM skills for AI agents. All credit for the foundational work belongs to Dean and the upstream contributors. This fork is licensed under the same [CC BY-NC-SA 4.0](LICENSE) terms as the original.

## Automattic Adaptation

This fork is being **progressively adapted** to align with Automattic's product management practices and frameworks. The upstream skills provide an excellent foundation; the goal here is to tailor them for the specific ways Automattic teams work and for internal tooling conventions.

Changes in this fork may include:
- Adjusting frameworks and examples to reflect Automattic's product culture
- Adding skills specific to the WordPress and WooCommerce ecosystem
- Modifying interactive advisors to account for Automattic's distributed team dynamics
- Updating references and terminology to match internal conventions
- Updating and introducing templates aligned with our Product Practice

Upstream changes will be pulled in periodically. Contributions that are generally useful will be proposed back to the original repo.

---

**Help product managers become more awesome at their craft — and help them send the ladder down to others.**

Battle-tested PM frameworks that teach both you and your AI agents how to do product management work at a professional level. You learn the *why*. Your agents execute the *how*. Everyone gets better.

Frame problems, hunt opportunities, scaffold validation experiments, and kill bad bets fast. With frameworks from Teresa Torres, Geoffrey Moore, Amazon, MITRE, and much more from product management's greatest hits.

---

## 🎯 What This Is

**46 ready-to-use PM skills + reusable command workflows** that teach both you and your AI agents how to do product management work at a professional level — so the PM understands the *why* and the agent can execute the *how*.

Instead of saying *"Write a PRD"* and hoping for the best, you and your agent both know:
- ✅ How to structure a PRD and why each section earns its place
- ✅ What questions to ask stakeholders and what you're listening for
- ✅ Which prioritization framework to use (and when each one breaks down)
- ✅ How to run customer discovery interviews and what signals matter
- ✅ How to break down epics using proven patterns — and the tradeoffs of each

**Result:** You work faster, with better consistency, at a higher strategic level — and you can explain why.

**Works with:** Claude Code, Cowork, OpenAI Codex, ChatGPT, Gemini, and any AI agent that can read structured knowledge.

---

## 🎓 Design Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. They equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework — so they can explain it, adapt it, and pass it on.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started.

This means:
- Skills explain reasoning, not just steps
- Examples show the thinking, not just the output
- Anti-patterns name the failure mode so you recognize it in the wild
- Interactive skills coach through discovery — they don't just collect answers

**An edit that strips learning scaffolding to tighten copy is a defect, not an improvement.**

---

## ⚡ Start in 60 Seconds

New here? Start with [`START_HERE.md`](START_HERE.md).

```bash
# Run a skill (artifact/analysis)
./scripts/run-pm.sh skill prioritization-advisor "We have 12 requests and one sprint"

# Run a command (multi-skill workflow)
./scripts/run-pm.sh command discover "Reduce onboarding drop-off for self-serve users"
```

Need discovery first?

```bash
./scripts/find-a-skill.sh --keyword onboarding
./scripts/find-a-command.sh --keyword roadmap
```

---

## Why The Command Layer Helps

Commands make using skills easier without replacing skills.

- Skills stay deep and pedagogic: they are the source of truth for frameworks, reasoning, and quality — for humans and agents alike.
- Commands remove stitching work: one command chains the right skills in the right order.
- You start faster: less "which skill should I run first?" and fewer manual handoffs.
- Outputs are more consistent: commands enforce checkpoints, then defer to skill-level rigor.
- Teams onboard quicker: new users can run `/discover` or `/write-prd` and learn the skill system while shipping.

In short: **skills provide expertise; commands provide momentum.**

---

## 🧪 Streamlit (beta)

Want a quick local test-drive before using skills in your agent workflow?

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

What you can do in v0.7:
- `Learn` setup and integration paths without leaving the app
- `Find My Skill` by describing your situation in plain English
- `Run Skills` with your own scenario once you know what you want

This beta interface is a feature in flight. Feedback is welcome via [GitHub Issues](https://github.com/p3ob7o/Product-Manager-Skills/issues).

---

## ✅ Safety and Evaluation

Before using any skill:
- Review the skill file and any linked resources. If it includes `scripts/`, read them before running.
- Prefer least privilege. Skills should not require secrets or network access unless explicitly documented.
- Do a quick dry run with a realistic prompt, then refine `name` and `description` for better discoverability.
- Run `python3 scripts/check-skill-triggers.py --show-cases` before packaging if you want a quick trigger-readiness pass.

---

## 🧰 Optional Scripts (Deterministic Helpers)

Some skills include a `scripts/` folder with deterministic helpers for calculations or formatting. These are optional, should be audited before running, and should avoid network calls or external dependencies.

**Examples:**
- `skills/tam-sam-som-calculator/scripts/market-sizing.py`
- `skills/user-story/scripts/user-story-template.py`

---

## 🤖 Skill Creation Utility

**Want to create your own skills?** Choose one of these utilities:

- `scripts/add-a-skill.sh` - Content-first, AI-assisted generation from notes/frameworks.
- `scripts/build-a-skill.sh` - Guided "build-a-bear" wizard that prompts section-by-section.
- `scripts/find-a-skill.sh` - Search skills by name/type/keyword with ranked results.
- `scripts/find-a-command.sh` - Search commands by name/keyword/used skills.
- `scripts/run-pm.sh` - Fast runner for either a skill or a command.
- `scripts/test-a-skill.sh` - Run strict conformance checks and optional smoke checks.
- `scripts/check-skill-triggers.py` - Audit frontmatter descriptions and scenario prompts for Claude-style triggering.
- `scripts/test-library.sh` - Validate skills, commands, and regenerate catalogs.
- `scripts/zip-a-skill.sh` - Build upload-ready `.zip` files by skill, type, or all skills.
- `scripts/generate-catalog.py` - Regenerate skill/command navigation indexes.

**New to terminals?** See [`scripts/README.md`](scripts/README.md) for a plain-language walkthrough.
**Power users:** These scripts are designed to chain together into fast end-to-end workflows (idea -> prompt -> validation -> packaging).

**What it does:**
1. Analyzes your content and suggests skill types
2. Generates complete skill files with examples
3. Validates metadata for marketplace compliance
4. Updates documentation automatically

**Usage:**
```bash
# From a file
./scripts/add-a-skill.sh research/your-framework.md

# Guided wizard
./scripts/build-a-skill.sh

# Find a skill
./scripts/find-a-skill.sh --keyword pricing --type interactive

# Find a command
./scripts/find-a-command.sh --keyword roadmap

# Run a command workflow
./scripts/run-pm.sh command write-prd "Mobile onboarding redesign"

# Test one skill
./scripts/test-a-skill.sh --skill finance-based-pricing-advisor --smoke

# Test full library surface
./scripts/test-library.sh

# Build Claude upload zip for one skill
./scripts/zip-a-skill.sh --skill finance-based-pricing-advisor

# Build Claude upload zips for all skills
./scripts/zip-a-skill.sh --all --output dist/skill-zips

# Build Claude upload zips for one category (component|interactive|workflow)
./scripts/zip-a-skill.sh --type component --output dist/skill-zips

# Build curated starter pack
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips

# Show available curated presets
./scripts/zip-a-skill.sh --list-presets

# From clipboard
pbpaste | ./scripts/add-a-skill.sh

# Check available adapters
./scripts/add-a-skill.sh --list-agents
```

**Agent support:** Claude Code, Manual mode (works with any CLI), and custom adapters via `scripts/adapters/ADAPTER_TEMPLATE.sh`

**Learn more:** See [`docs/Add-a-Skill Utility Guide.md`](docs/Add-a-Skill%20Utility%20Guide.md) for complete guide.
**Cloning locally?** Start with [`docs/Building PM Skills.md#local-clone-quickstart`](docs/Building%20PM%20Skills.md#local-clone-quickstart).

---

## ✅ Claude Web Upload Checklist

- Keep frontmatter `name` <= 64 chars and `description` <= 200 chars.
- Use `intent` for the richer repo-facing explanation of the skill, while keeping `description` short and trigger-oriented.
- Ensure the skill folder name matches the `name` value.
- Use `scripts/zip-a-skill.sh --skill <skill-name>` (or `--type component`, `--preset core-pm`) to generate upload-ready ZIPs.
- (Advanced) Use `scripts/package-claude-skills.sh` if you need unpacked upload-ready folders.
- Validate metadata with `scripts/check-skill-metadata.py`.
- For GitHub ZIP upload flow, see [`docs/Using PM Skills with Claude.md`](docs/Using%20PM%20Skills%20with%20Claude.md#github-zip-install).

---

## 🏗️ Three-Tier Architecture (How Skills Work Together)

These 46 skills are organized into **three types** that build on each other:

```text
┌───────────────────────────────────────────────────────────┐
│  WORKFLOW SKILLS (6)                                      │
│  Complete end-to-end PM processes                         │
│  Example: "Run a product strategy session"                │
│  Timeline: 2-4 weeks                                      │
└───────────────────────────────────────────────────────────┘
                         ↓ orchestrates
┌───────────────────────────────────────────────────────────┐
│  INTERACTIVE SKILLS (20)                                  │
│  Guided discovery with adaptive questions                 │
│  Example: "Which prioritization framework should I use?"  │
│  Timeline: 30-90 minutes                                  │
└───────────────────────────────────────────────────────────┘
                         ↓ uses
┌───────────────────────────────────────────────────────────┐
│  COMPONENT SKILLS (20)                                    │
│  Templates for specific PM deliverables                   │
│  Example: "Write a user story"                            │
│  Timeline: 10-30 minutes                                  │
└───────────────────────────────────────────────────────────┘
```

### Component Skills (20) — Templates & Artifacts
**What:** Reusable templates for creating specific PM deliverables (user stories, positioning statements, epics, personas, PRDs, etc.)

**When to use:** You need a standard template or format for a specific deliverable.

**Example:** "Write a user story with acceptance criteria" → Use [`user-story.md`](skills/user-story/SKILL.md)

---

### Interactive Skills (20) — Guided Discovery
**What:** Multi-turn conversational flows where AI asks you 3-5 adaptive questions, then offers smart recommendations based on your context.

**When to use:** You need help deciding which approach to take or gathering context before executing.

**Example:** "Which prioritization framework should I use?" → Run [`prioritization-advisor.md`](skills/prioritization-advisor/SKILL.md), which asks about your product stage, team size, data availability, then recommends RICE, ICE, Kano, or other frameworks.

**How they work:**
1. AI asks 3-5 questions about your context
2. You answer (or pick from numbered options)
3. AI offers 3-5 tailored recommendations
4. You choose one (or combine approaches)
5. AI executes using the right component skills

---

### Workflow Skills (6) — End-to-End Processes
**What:** Complete PM processes that orchestrate multiple component and interactive skills over days/weeks.

**When to use:** You need to run a full PM workflow from start to finish (strategy session, discovery cycle, roadmap planning, PRD creation).

**Example:** "Align stakeholders on product strategy" → Run [`product-strategy-session.md`](skills/product-strategy-session/SKILL.md), which guides you through positioning → problem framing → solution exploration → roadmap planning over 2-4 weeks.

---

## 📦 All 46 Skills (Clickable)

Now that you understand the three types, here's the complete catalog:

### 🧱 Component Skills (20)

| Skill | Use When You Need To... |
|-------|-------------------------|
| **[altitude-horizon-framework](skills/altitude-horizon-framework/SKILL.md)** | Understand the PM→Director mindset shift: altitude (scope), horizon (time), four transition zones, failure modes, and the Cascading Context Map. Based on [The Product Porch E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1) |
| **[company-research](skills/company-research/SKILL.md)** | Deep-dive competitor or company analysis |
| **[customer-journey-map](skills/customer-journey-map/SKILL.md)** | Map customer experience across all touchpoints (NNGroup framework) |
| **[eol-message](skills/eol-message/SKILL.md)** | Communicate product/feature deprecation gracefully |
| **[epic-hypothesis](skills/epic-hypothesis/SKILL.md)** | Turn vague initiatives into testable hypotheses with success metrics |
| **[finance-metrics-quickref](skills/finance-metrics-quickref/SKILL.md)** | Fast lookup table for 32+ SaaS finance metrics with formulas, benchmarks, and when to use each |
| **[jobs-to-be-done](skills/jobs-to-be-done/SKILL.md)** | Understand what customers are trying to accomplish (JTBD framework) |
| **[pestel-analysis](skills/pestel-analysis/SKILL.md)** | Analyze external factors (Political, Economic, Social, Tech, Environmental, Legal) |
| **[pol-probe](skills/pol-probe/SKILL.md)** | Define lightweight, disposable validation experiments to test hypotheses before building (Dean Peters PoL framework) |
| **[positioning-statement](skills/positioning-statement/SKILL.md)** | Define who you serve, what problem you solve, and how you're different (Geoffrey Moore framework) |
| **[press-release](skills/press-release/SKILL.md)** | Write a future press release to clarify product vision (Amazon Working Backwards) |
| **[problem-statement](skills/problem-statement/SKILL.md)** | Frame a customer problem with evidence before jumping to solutions |
| **[proto-persona](skills/proto-persona/SKILL.md)** | Create hypothesis-driven personas before doing full research |
| **[recommendation-canvas](skills/recommendation-canvas/SKILL.md)** | Document AI-powered product recommendations |
| **[saas-economics-efficiency-metrics](skills/saas-economics-efficiency-metrics/SKILL.md)** | Evaluate unit economics and capital efficiency (CAC, LTV, payback, margins, burn rate, Rule of 40, magic number) |
| **[saas-revenue-growth-metrics](skills/saas-revenue-growth-metrics/SKILL.md)** | Calculate and interpret revenue, retention, and growth metrics (revenue, ARPU, MRR/ARR, churn, NRR, expansion) |
| **[storyboard](skills/storyboard/SKILL.md)** | Visualize user journeys with 6-frame narrative storyboards |
| **[user-story](skills/user-story/SKILL.md)** | Write user stories with proper acceptance criteria (Mike Cohn + Gherkin) |
| **[user-story-mapping](skills/user-story-mapping/SKILL.md)** | Organize stories by user workflow (Jeff Patton framework) |
| **[user-story-splitting](skills/user-story-splitting/SKILL.md)** | Break down large stories using 8 proven patterns |

---

### 🔄 Interactive Skills (20)

| Skill | What It Does |
|-------|--------------|
| **[acquisition-channel-advisor](skills/acquisition-channel-advisor/SKILL.md)** | Evaluate acquisition channels using unit economics, customer quality, and scalability. Recommends scale/test/kill decisions |
| **[ai-shaped-readiness-advisor](skills/ai-shaped-readiness-advisor/SKILL.md)** | Assess if you're "AI-first" (automating tasks) or "AI-shaped" (redesigning how you work). Evaluates 5 competencies and recommends which to build first |
| **[business-health-diagnostic](skills/business-health-diagnostic/SKILL.md)** | Diagnose SaaS business health using key metrics, identify red flags, and prioritize actions. Analyzes growth, retention, efficiency, and capital health |
| **[context-engineering-advisor](skills/context-engineering-advisor/SKILL.md)** | Diagnose context stuffing (volume without intent) vs. context engineering (structure for attention). Guides memory architecture, retrieval strategies, and Research→Plan→Reset→Implement cycle |
| **[customer-journey-mapping-workshop](skills/customer-journey-mapping-workshop/SKILL.md)** | Guides journey mapping with pain point identification |
| **[director-readiness-advisor](skills/director-readiness-advisor/SKILL.md)** | Coaches PMs and new Directors through the transition across four situations: preparing, interviewing, newly landed, recalibrating. Based on [The Product Porch E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1) |
| **[discovery-interview-prep](skills/discovery-interview-prep/SKILL.md)** | Plans customer interviews (Mom Test style) based on your research goals |
| **[epic-breakdown-advisor](skills/epic-breakdown-advisor/SKILL.md)** | Splits epics into user stories using Richard Lawrence's 9 patterns |
| **[feature-investment-advisor](skills/feature-investment-advisor/SKILL.md)** | Evaluate feature investments using revenue impact, cost structure, ROI, and strategic value. Delivers build/don't build recommendations |
| **[finance-based-pricing-advisor](skills/finance-based-pricing-advisor/SKILL.md)** | Evaluate pricing changes using financial impact analysis (ARPU/ARPA, conversion, churn risk, NRR, payback) |
| **[lean-ux-canvas](skills/lean-ux-canvas/SKILL.md)** | Sets up hypothesis-driven planning (Jeff Gothelf Lean UX Canvas v2) |
| **[opportunity-solution-tree](skills/opportunity-solution-tree/SKILL.md)** | Generates opportunities and solutions, recommends best proof-of-concept to test |
| **[pol-probe-advisor](skills/pol-probe-advisor/SKILL.md)** | Recommends which of 5 prototype types to use based on your hypothesis and risk (Feasibility, Task-Focused, Narrative, Synthetic Data, Vibe-Coded) |
| **[positioning-workshop](skills/positioning-workshop/SKILL.md)** | Guides you through defining your positioning with adaptive questions |
| **[prioritization-advisor](skills/prioritization-advisor/SKILL.md)** | Recommends the right prioritization framework (RICE, ICE, Kano, etc.) for your situation |
| **[problem-framing-canvas](skills/problem-framing-canvas/SKILL.md)** | Leads you through MITRE Problem Framing (Look Inward/Outward/Reframe) |
| **[tam-sam-som-calculator](skills/tam-sam-som-calculator/SKILL.md)** | Projects market size (TAM/SAM/SOM) with real-world data and citations |
| **[user-story-mapping-workshop](skills/user-story-mapping-workshop/SKILL.md)** | Walks you through creating story maps with backbone and release slices |
| **[vp-cpo-readiness-advisor](skills/vp-cpo-readiness-advisor/SKILL.md)** | Coaches Directors and executives through the VP/CPO transition — includes CEO interview framework for evaluating roles before accepting. Based on [The Product Porch E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2) |
| **[workshop-facilitation](skills/workshop-facilitation/SKILL.md)** | Adds one-step-at-a-time facilitation with numbered recommendations for workshop skills |

---

### 🎭 Workflow Skills (6)

| Skill | What It Does | Timeline |
|-------|--------------|----------|
| **[discovery-process](skills/discovery-process/SKILL.md)** | Complete discovery cycle: frame problem → research → synthesize → validate solutions | 3-4 weeks |
| **[executive-onboarding-playbook](skills/executive-onboarding-playbook/SKILL.md)** | 30-60-90 day diagnostic playbook for VP/CPO transitions: diagnose before acting, surface unwritten strategy, assess people, act with evidence. Based on [The Product Porch E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2) | 90 days |
| **[prd-development](skills/prd-development/SKILL.md)** | Structured PRD: problem statement → personas → solution → metrics → user stories | 2-4 days |
| **[product-strategy-session](skills/product-strategy-session/SKILL.md)** | Full strategy: positioning → problem framing → solution exploration → roadmap | 2-4 weeks |
| **[roadmap-planning](skills/roadmap-planning/SKILL.md)** | Strategic roadmap: gather inputs → define epics → prioritize → sequence → communicate | 1-2 weeks |
| **[skill-authoring-workflow](skills/skill-authoring-workflow/SKILL.md)** | Meta workflow: choose add/build path → validate conformance → update docs → package/publish | 30-90 minutes |

<a id="future-skills"></a>
### 🔮 Agent Skills of the Future

**_Possible skills in development:_**

- **Dangerous Animals of Product Management** - Feature hostage negotiations and stakeholder shuttle diplomacy for when you're facing HiPPOs, RHiNOs, and WoLFs (_oh my!_).
- **Pricing for Product Managers** - Value-based pricing, packaging strategy, price increases, and grandfather clause negotiations without the panic spiral and flop sweat.
- **Classic Business Strategy Frameworks** - Ansoff, BCG, Porter's 5 Forces, Blue Ocean, and SWOT in agent-ready format that helps you decide, not decorate slides.
- **Storytelling for Product Managers** - Narrative arc, demo choreography, and pitch structure built on pro-opera lessons and Hakawati orations for commanding the room.
- **Prompt Building for Product Managers** - Industrial-strength prompt engineering: team session starters, multi-turn workflow wizards, and reverse engineering templates for artifacts like PRDs.
- **Nightmares of Product Management** - Telemetry, triage, and tactics for when things don't go as planned: adoption theater, feature graveyards, metric manipulation, launch amnesia, technical debt wildfires. Plus prevention strategies.

Detailed concept notes live in [`PLANS.md`](PLANS.md#future-skill-candidates).

---

## 🚀 How to Use

**Confused by setup options?** Start here: [PM Skills Rule-of-Thumb Guide](docs/PM%20Skills%20Rule-of-Thumb%20Guide.md).

### Fastest Path (Local Repo)

```bash
# Skill mode
./scripts/run-pm.sh skill user-story "Checkout improvements for returning customers"

# Command mode
./scripts/run-pm.sh command plan-roadmap "Q3-Q4 roadmap for enterprise reporting"
```

Command definitions live in [`commands/`](commands/README.md), and generated browse indexes live in [`catalog/`](catalog/README.md).

### With Claude Desktop or Claude.ai

1. Open a conversation with Claude
2. Share the skill file: "Read user-story.md"
3. Ask Claude to apply it: "Using the User Story skill, write stories for our checkout flow"

### With Claude Code (CLI)

```bash
# Install a single skill from the plugin marketplace
/plugin marketplace add p3ob7o/Product-Manager-Skills
/plugin install prd-development@pm-skills

# Or use the cloned repo directly
cd product-manager-skills
claude "Using the PRD Development workflow, create a PRD for our mobile feature"
```

You can discover via `npx skills find <query>` and `npx skills add p3ob7o/Product-Manager-Skills --list`, then install for Claude Code. See [Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md).

### With OpenAI Codex

Use local workspace paths, GitHub-connected Codex on ChatGPT, or discover/install directly with `npx skills`. See [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md).

### With ChatGPT

Use GitHub app connections (formerly connectors), Custom GPT Knowledge uploads, or Project files. See [Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md).

### With Cowork or Other Agents

**Cowork:** Import skills as knowledge modules, invoke via natural language.
**Other agents:** Follow your agent's docs for loading custom knowledge.

---

## 📄 Docs

- **[Using PM Skills 101](docs/Using%20PM%20Skills%20101.md)** — Beginner-friendly orientation for PMs who want clear setup without technical overload.
- **[Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md)** — Claude Code usage plus GitHub ZIP upload steps for Claude Desktop/Web.
- **[Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)** — Local workspace usage plus GitHub-connected Codex on ChatGPT.
- **[Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md)** — GitHub app connection, Custom GPT Knowledge setup, and Project-based usage.
- **[Platform Guides for PMs](docs/Platform%20Guides%20for%20PMs.md)** — Tool-by-tool setup chooser for Claude Code, Codex, OpenClaw, Cowork, Claude Desktop, ChatGPT Desktop, n8n, LangFlow, and Python agents.
- **[Using PM Skills with Claude Code](docs/Using%20PM%20Skills%20with%20Claude%20Code.md)** — PM-focused quickstart for Claude Code users.
- **[Using PM Skills with Slash Commands 101](docs/Using%20PM%20Skills%20with%20Slash%20Commands%20101.md)** — Turn PM skills into reusable Claude slash commands like `/pm-story` and `/pm-prd`.
- **[Using PM Skills with Claude Desktop](docs/Using%20PM%20Skills%20with%20Claude%20Desktop.md)** — Skill upload workflow for non-technical desktop users.
- **[Using PM Skills with ChatGPT Desktop](docs/Using%20PM%20Skills%20with%20ChatGPT%20Desktop.md)** — Project-first setup for desktop-based PM work.
- **[Using PM Skills with n8n](docs/Using%20PM%20Skills%20with%20n8n.md)** — Practical automation patterns for repeatable PM workflows.
- **[Using PM Skills with LangFlow](docs/Using%20PM%20Skills%20with%20LangFlow.md)** — Visual workflow setup using skill-guided prompt templates.
- **Additional harness guides:** [Cursor](docs/Using%20PM%20Skills%20with%20Cursor.md), [Windsurf](docs/Using%20PM%20Skills%20with%20Windsurf.md), [Bolt](docs/Using%20PM%20Skills%20with%20Bolt.md), [Replit Agent](docs/Using%20PM%20Skills%20with%20Replit%20Agent.md), [Make.com](docs/Using%20PM%20Skills%20with%20Make.com.md), [Devin](docs/Using%20PM%20Skills%20with%20Devin.md), [CrewAI](docs/Using%20PM%20Skills%20with%20CrewAI.md), [Gemini](docs/Using%20PM%20Skills%20with%20Gemini.md)
- **[Start Here](START_HERE.md)** — One-page "do this now" onboarding for skills and commands.
- **[Commands](commands/README.md)** — Command format, command list, validation, and discovery.
- **[Catalog Artifacts](catalog/README.md)** — Generated skill/command indexes for fast navigation.
- **[PM Skills Rule-of-Thumb Guide](docs/PM%20Skills%20Rule-of-Thumb%20Guide.md)** — Non-technical setup choices (local repo vs ZIP vs app connections) in plain English.
- **[Marketplace Strategy](MARKETPLACE_STRATEGY.md)** — PM-friendly strategy for distributing skills in marketplaces.
- **[Marketplace Submission Runbook](docs/Marketplace%20Submission%20Runbook.md)** — Step-by-step submission workflow for non-technical teams.
- **[Marketplace Issue Templates](docs/Marketplace%20Issue%20Templates.md)** — Reusable issue templates for marketplace execution and tracking.
- **[PM Tooling Operations Charter](docs/PM%20Tooling%20Operations%20Charter.md)** — Pedagogic operating stack across M365 Copilot, Codex, ChatGPT, VS Code/Copilot, Cursor, n8n, and Lovable.
- **[Add-a-Skill Utility Guide](docs/Add-a-Skill%20Utility%20Guide.md)** — End-to-end automation guide for generating and validating new skills.
- **[Building PM Skills](docs/Building%20PM%20Skills.md)** — How we distill sources into agent-ready PM skills.

---

## 💼 Real-World Use Cases

### "I need to align stakeholders on product strategy"
→ **Workflow:** [`product-strategy-session`](skills/product-strategy-session/SKILL.md) (2-4 weeks, orchestrates positioning → roadmap)

### "I need to validate a customer problem before building"
→ **Workflow:** [`discovery-process`](skills/discovery-process/SKILL.md) (3-4 weeks, interviews → synthesis → validation)

### "I need to test a hypothesis quickly before investing in development"
→ **Interactive:** [`pol-probe-advisor`](skills/pol-probe-advisor/SKILL.md) (recommends which prototype type: Feasibility, Task-Focused, Narrative, Synthetic Data, or Vibe-Coded)
→ **Component:** [`pol-probe`](skills/pol-probe/SKILL.md) (template for documenting validation experiments)

### "I want to know if I'm using AI strategically or just for efficiency"
→ **Interactive:** [`ai-shaped-readiness-advisor`](skills/ai-shaped-readiness-advisor/SKILL.md) (assesses 5 competencies: Context Design, Agent Orchestration, Outcome Acceleration, Team-AI Facilitation, Strategic Differentiation)

### "I'm pasting entire docs into AI and getting vague responses"
→ **Interactive:** [`context-engineering-advisor`](skills/context-engineering-advisor/SKILL.md) (diagnose context stuffing vs. engineering, define boundaries, implement Research→Plan→Reset→Implement cycle)

### "I need to write a PRD for a new feature"
→ **Workflow:** [`prd-development`](skills/prd-development/SKILL.md) (2-4 days, problem → solution → stories)

### "I need to create a Q2 roadmap"
→ **Workflow:** [`roadmap-planning`](skills/roadmap-planning/SKILL.md) (1-2 weeks, epics → prioritization → sequencing)

### "I need to choose a prioritization framework"
→ **Interactive:** [`prioritization-advisor`](skills/prioritization-advisor/SKILL.md) (asks questions, recommends RICE/ICE/Kano)

### "I need to split a large epic"
→ **Interactive:** [`epic-breakdown-advisor`](skills/epic-breakdown-advisor/SKILL.md) (Richard Lawrence's 9 patterns)

### "I need to write a user story"
→ **Component:** [`user-story`](skills/user-story/SKILL.md) (template + examples)

---

## 💡 Why Skills Beat Prompts

| Prompts | Skills |
|---------|--------|
| One-time instructions per task | Reusable frameworks learned once |
| "Write a PRD for X" | Agent knows PRD structure, asks smart questions, handles edge cases |
| You repeat yourself constantly | Agent remembers best practices |
| Inconsistent outputs | Consistent, professional results |

**Skills = Less explaining, more strategic work.**

---

## 🌟 What Makes These Skills Different

### ✅ Battle-Tested Frameworks
Built on proven methods from Geoffrey Moore, Jeff Patton, Teresa Torres, Amazon, Richard Lawrence, MITRE, and more.

### ✅ Real Client Work
Based on decades of PM consulting across healthcare, finance, manufacturing, and tech.

### ✅ Agent-Ready Format
Optimized for AI comprehension—not blog posts, not books, not courses. **Executable frameworks.**

### ✅ Zero Fluff
Every word earns its keep. No filler, no buzzwords, no generic advice.

### ✅ Example-Rich
Shows both "good" and "bad" examples so you know what works and what to avoid.

---

## 📚 Skill Structure (What's Inside Each File)

Every skill follows the same format:

```
## Purpose
What this skill does and when to use it.

## Key Concepts
Core frameworks, definitions, anti-patterns.

## Application
Step-by-step instructions (with examples).

## Examples
Real-world cases (good and bad).

## Common Pitfalls
What to avoid and why.

## References
Related skills and external frameworks.
```

**Clean. Practical. Zero fluff.**

---

## 🤝 Contributing

Found a gap? Have a PM framework you'd like to see included?

**Ways to contribute:**
- Open an issue with your suggestion
- Submit a pull request (we'll help you format it)
- Share feedback on what's working or missing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🎓 Philosophy

**Principles:**
- **Outcome-driven** over output-driven (solve problems, don't just ship features)
- **Evidence over vibes** (validate with data, not opinions)
- **Clarity beats completeness** (simple and usable beats comprehensive and confusing)
- **Examples beat explanations** (show, don't just tell)

**No hype. No buzzwords. Just frameworks that work.**

---

## 📖 Related Resources

- **[Original Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)** — The upstream repo this fork is based on
- **[Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)** — Task-specific prompts for ChatGPT, Claude, Gemini (by Dean Peters)
- **[Productside](https://productside.com)** — AI-powered product management training and consulting

---

## 📜 License

CC BY-NC-SA 4.0 — non-commercial use with share-alike.

See [LICENSE](LICENSE) for full details.

---

## 📞 Questions?

- **Fork issues:** [Report bugs or suggest features for this fork](https://github.com/p3ob7o/Product-Manager-Skills/issues)
- **Upstream project:** [Original Product Manager Skills by Dean Peters](https://github.com/deanpeters/Product-Manager-Skills)

---

Originally built by [Dean Peters](https://linkedin.com/in/deanpeters) (Principal Consultant and Trainer at [Productside](https://productside.com)) with Anthropic Claude and OpenAI Codex. This fork is maintained for Automattic's internal product management use.

*Helping product managers work smarter with AI.*
