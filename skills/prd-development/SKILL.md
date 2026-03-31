---
name: prd-development
description: Build a structured PRD that connects problem, users, solution, and success criteria. Use when turning discovery notes into an engineering-ready document for a major initiative.
intent: >-
  Guide product managers through structured PRD (Product Requirements Document) creation by orchestrating problem framing, user research synthesis, solution definition, and success criteria into a cohesive document. Use this to move from scattered notes and Slack threads to a clear, comprehensive PRD that aligns stakeholders, provides engineering context, and serves as a source of truth—avoiding ambiguity, scope creep, and the "build what's in my head" trap.
type: workflow
theme: pm-artifacts
best_for:
  - "Writing a complete PRD from scratch"
  - "Structuring product requirements for an engineering handoff"
  - "Documenting a major new feature before development begins"
scenarios:
  - "I need a PRD for a new AI-powered recommendation feature in our e-commerce platform"
  - "I've completed a discovery sprint and need to turn the findings into a PRD my engineers can act on"
estimated_time: "60-120 min"
---


## Purpose
Guide product managers through structured PRD (Product Requirements Document) creation by orchestrating problem framing, user research synthesis, solution definition, and success criteria into a cohesive document. Use this to move from scattered notes and Slack threads to a clear, comprehensive PRD that aligns stakeholders, provides engineering context, and serves as a source of truth—avoiding ambiguity, scope creep, and the "build what's in my head" trap.

This is not a waterfall spec—it's a living document that captures strategic context, customer problems, proposed solutions, and success criteria, evolving as you learn through delivery.

## Key Concepts

### What is a PRD?

A PRD (Product Requirements Document) is a structured document that answers:
1. **Why are we doing this?** (Summary)
2. **What problem are we solving, for whom, and why now?** (Problem statement)
3. **Who are we building for — and who are we not?** (Target audience)
4. **What does the user need to accomplish?** (User stories)
5. **What are we building and what's out of scope?** (Feature definition)
6. **How does this compare to the competition?** (Competitive overview)
7. **How will we measure success?** (Success and measurement)
8. **What could go wrong and what don't we know yet?** (Risks and open questions)
9. **How much effort is this?** (Level of effort)
10. **Who is accountable, responsible, consulted, and informed?** (Ownership & stakeholders)

### PRD Structure (Standard Template)

```markdown
# [Feature/Product Name] PRD

**Product DRI:**
**Design DRI:**
**Engineering DRI:**
**Last revised:**

## 1. Summary
- Relevant opening paragraph setting up the "why"

## 2. Problem Statement
- What problem are we solving, for whom, and why does it matter now?
- One to three sentences grounded in evidence

## 3. Target Audience
- **Primary**: Describe the audience specifically. Avoid "users" — name the customer type, role, or use case.
- **Key traits**: Note any relevant behaviours, habits, or expectations that shape how this audience will interact with the feature.
- **Not for this phase**: Be explicit about who this is not for and why. This helps prevent scope creep and keeps the team aligned on who we're solving for.

## 4. User Stories
- Short, simple descriptions of functionality told from the user's perspective, focusing on who, what, and why.

## 5. Feature Definition
- Product / feature explanation in simple, straightforward language. This should inform the broader Design, Engineering, and GTM teams about the specifics of the product.
- Feature 1. ...
- Feature 2. ...
- Feature 3. ...

### Out of Scope
- Features, functionalities, or user scenarios that will not be included in the current release.

## 6. Competitive Overview
| Competitor | Current approach | Gap / opportunity |
| :---- | :---- | :---- |
|  |  |  |

## 7. Success and Measurement
- **Business objective**: Describe the business outcome this advances.
- **Success metrics**: What we intend to measure. Include a baseline where possible.
- **Definition of done**: Agreed criteria the project must meet before it's considered complete and ready for release.

## 8. Risks and Open Questions
- What do you not yet know, and what could go wrong?
- Flag unresolved decisions, unvalidated assumptions, and known risks before projects kick off.
- For each risk, note how you plan to address it.

## 9. Level of Effort
**Size**: [XS / S / M / L / XL]. Plus one or two sentences summarizing the estimated engineering effort. Estimated collaboratively by the Product, Design, and Engineering DRIs.

## 10. Ownership & Stakeholders
| Role        | Name(s) | Notes                                                                  |
| :---------- | :------ | :--------------------------------------------------------------------- |
| Accountable |         | Single owner. Typically the Artistic Director.                         |
| Responsible |         | Typically includes: PM, Eng Lead, and Design Lead.                     |
| Consulted   |         | Those whose input is needed before key decisions are made.             |
| Informed    |         | Those kept up to date on progress but not in the decision-making loop. |
```

### Why This Works
- **Alignment:** Ensures everyone (PM, design, eng, stakeholders) understands the "why"
- **Context preservation:** Captures research and strategic rationale for future reference
- **Decision log:** Documents what's in scope, out of scope, and why
- **Execution clarity:** Provides engineering with user stories and acceptance criteria
- **Accountability:** RACI table makes ownership explicit before work begins

### Anti-Patterns (What This Is NOT)
- **Not a detailed spec:** PRDs frame the problem and solution; they don't specify UI pixel-by-pixel
- **Not waterfall:** PRDs evolve as you learn; they're not frozen contracts
- **Not a substitute for collaboration:** PRDs complement conversation, not replace it

### When to Use This
- Starting a major feature or product initiative
- Aligning cross-functional teams on scope and requirements
- Documenting decisions for future reference
- Onboarding new team members to a project

### When NOT to Use This
- For small bug fixes or trivial features (overkill)
- When problem and solution are already clear and aligned (just write user stories)
- For continuous discovery experiments (use Lean UX Canvas instead)

---

### Facilitation Source of Truth

When running this workflow as a guided conversation, use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the interaction protocol.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the workflow sequence and domain-specific outputs. If there is a conflict, follow this file's workflow logic.

## Application

Use `template.md` for the full fill-in structure.

This workflow orchestrates **10 phases** over **2-4 days**, using multiple component and interactive skills.

---

## Phase 1: Summary (30 minutes)

**Goal:** Write the opening "why" paragraph that sets context for the whole document.

### Activities

**1. Draft Summary**
- **Format:** One paragraph that sets up why this work matters — the context, the opportunity, and the direction.
- **Example:**
  > "Our onboarding drop-off rate has reached 60%, driven by users landing on an empty dashboard with no guidance. This PRD defines a guided onboarding checklist that walks new users through their first three core actions, giving them a clear path to value and reducing early churn."

- **Participants:** PM
- **Duration:** 30 minutes
- **Output:** One-paragraph opening

**Tip:** Write this first to force clarity, but refine it last — after all other sections are complete, the summary almost writes itself.

---

## Phase 2: Problem Statement (60 minutes)

**Goal:** Frame the customer problem with evidence in one to three sentences.

### Activities

**1. Write Problem Statement**
- **Use:** `skills/problem-statement/SKILL.md` (component)
- **Input:** Discovery insights from `skills/discovery-process/SKILL.md` or `skills/problem-framing-canvas/SKILL.md`
- **Participants:** PM
- **Duration:** 30 minutes
- **Output:** Structured problem statement

**Example Problem Statement:**

```markdown
## 2. Problem Statement

60% of new users abandon onboarding within the first 24 hours because they land on an
empty dashboard with no guidance — overwhelming them before they experience any value.
This is the #1 driver of early churn, supported by exit interviews, analytics, and
support ticket volume. Solving it now is critical to hitting our Q1 retention OKR.
```

**2. Add Supporting Context (Optional)**
- **Customer journey map:** If problem spans multiple touchpoints
- **Use:** `skills/customer-journey-mapping-workshop/SKILL.md` output
- **Jobs-to-be-done:** If motivations are key
- **Use:** `skills/jobs-to-be-done/SKILL.md` output

### Outputs from Phase 2

- **Problem statement:** What problem, for whom, why now, grounded in evidence
- **Supporting artifacts:** Journey map, JTBD (if relevant)

---

## Phase 3: Target Audience (30 minutes)

**Goal:** Define who you're building for — and explicitly who you're not.

### Activities

**1. Document Target Audience**
- **Use:** `skills/proto-persona/SKILL.md` (component) output
- **Participants:** PM
- **Duration:** 30 minutes
- **Format:** Primary audience, key traits, explicit exclusions for this phase

**Example:**

```markdown
## 3. Target Audience

- **Primary**: Non-technical solopreneurs signing up for their first SaaS product.
  Not "users" — specifically owner-operators with no IT support, using email and
  spreadsheets as their baseline.
- **Key traits**: Low tolerance for complexity, no time for tutorials, need to see
  value within minutes of signing up. Will abandon rather than ask for help.
- **Not for this phase**: Teams of 5+ employees, technical users, existing customers
  upgrading plans. Serving them well requires different onboarding logic — scope that
  separately.
```

### Outputs from Phase 3

- **Primary audience:** Named specifically, not generically
- **Key traits:** Behaviours and expectations that shape the design
- **Explicit exclusions:** Who this release is not for and why

---

## Phase 4: User Stories (90-120 minutes)

**Goal:** Break the solution into user stories with acceptance criteria, told from the user's perspective.

### Activities

**1. Write Epic Hypothesis**
- **Use:** `skills/epic-hypothesis/SKILL.md` (component)
- **Participants:** PM
- **Duration:** 30 minutes
- **Output:** Epic hypothesis statement

**Example:**
> "We believe that adding a guided onboarding checklist for non-technical users will increase activation rate from 40% to 60% because users currently drop off due to lack of guidance. We'll measure success by activation rate 30 days post-launch."

**2. Break Down Epic into User Stories**
- **Use:** `skills/epic-breakdown-advisor/SKILL.md` (interactive - with Richard Lawrence's 9 patterns)
- **Participants:** PM, design, engineering
- **Duration:** 90 minutes
- **Output:** User stories split by patterns (workflow, CRUD, business rules, etc.)

**3. Write User Stories**
- **Use:** `skills/user-story/SKILL.md` (component)
- **Participants:** PM
- **Duration:** 30 minutes per story
- **Format:** "As a [who], I want [what], so that [why]" + acceptance criteria

**Example User Stories:**

```markdown
## 4. User Stories

**Story 1: Display onboarding checklist on first login**
As a new user, I want to see a guided checklist when I first log in, so I know what to do first.

**Acceptance Criteria:**
- [ ] When user logs in for the first time, modal appears with checklist
- [ ] Checklist shows 3 steps: "Create project," "Invite teammate," "Complete task"
- [ ] Modal is dismissible (close button)
- [ ] If dismissed, checklist doesn't reappear (user preference saved)

**Story 2: Track checklist progress**
As a new user, I want to see my progress as I complete checklist steps, so I feel a sense of accomplishment.

**Acceptance Criteria:**
- [ ] When user completes step 1, checkmark appears next to "Create project"
- [ ] Progress bar updates (1/3 → 2/3 → 3/3)
- [ ] Checklist persists across sessions (if user logs out and back in)
```

**4. Document Edge Cases**
- **Edge cases:** What if user skips a step? What if they complete steps out of order?

### Outputs from Phase 4

- **Epic hypothesis:** Testable statement
- **User stories:** 3-10 stories with acceptance criteria
- **Edge cases:** Scenarios outside the happy path

---

## Phase 5: Feature Definition (60 minutes)

**Goal:** Explain what you're building in plain language — and explicitly what's not included in this release.

### Activities

**1. Write Feature Definition**
- **Format:** Plain-language explanation of the product or feature. Write for a colleague in Design, Engineering, or GTM who needs to understand what this is and how it works — not a spec, but enough to act on.
- **Example:**

```markdown
## 5. Feature Definition

We're building a **guided onboarding checklist** that appears when a user logs in for
the first time. It walks them through three core actions — creating a project, inviting
a teammate, and completing a sample task — with a progress bar and a completion
celebration.

- Feature 1. First-login modal with a 3-step checklist and progress bar.
- Feature 2. Per-step completion tracking that persists across sessions.
- Feature 3. Celebration state on full completion with suggested next actions.

### Out of Scope
- Persona-specific checklist variants (adds complexity — validate the concept first)
- Embedded video tutorials (resource-intensive — iterate if completion rates are high)
- Gamification (badges, points) — nice-to-have for a future phase
```

**2. Add User Flows or Wireframes (Optional)**
- **Use:** Design tools (Figma, Sketch), or hand-drawn sketches
- **When:** For complex features requiring visual explanation
- **Output:** Embedded in PRD or linked

### Outputs from Phase 5

- **Feature description:** Plain-language explanation for cross-functional teams
- **Feature list:** Discrete capabilities included in this release
- **Out of scope:** Explicit exclusions with rationale

---

## Phase 6: Competitive Overview (45 minutes)

**Goal:** Evaluate how key competitors approach this problem and identify the gap or opportunity.

### Activities

**1. Identify Key Competitors**
- **Scope:** Direct competitors addressing the same user problem, not the entire market
- **Sources:** G2/Capterra reviews, direct product trials, exit survey data

**2. Fill the Competitive Overview Table**
- **Format:** For each competitor, document their current approach and the gap or opportunity it reveals for your product.

**Example:**

```markdown
## 6. Competitive Overview

| Competitor  | Current approach                                      | Gap / opportunity                                      |
| :---------- | :---------------------------------------------------- | :----------------------------------------------------- |
| Competitor A | Guided setup wizard (5 steps, mandatory)             | Wizard is blocking — users abandon mid-flow            |
| Competitor B | Video library on first login                         | Passive — users don't engage; no interactive guidance  |
| Competitor C | No onboarding; assumes self-service discovery        | High churn; cited in exit surveys as top complaint     |
```

**3. Identify Your Angle**
- **Question:** What does this competitive landscape tell you about the right approach?
- **Example:** "Mandatory wizards block exploration. Video libraries are passive. The opportunity is lightweight, dismissible, interactive guidance."

### Outputs from Phase 6

- **Competitive table:** Competitor approach + gap for each
- **Strategic angle:** What the landscape tells you about how to differentiate

---

## Phase 7: Success and Measurement (30 minutes)

**Goal:** Define the business objective, what you'll measure, and what "done" looks like.

### Activities

**1. Define Business Objective**
- **Question:** What business outcome does this advance?
- **Example:** "This supports our Q1 OKR: reduce 30-day churn from 15% to 8%."

**2. Define Success Metrics**
- **Question:** What will you measure, and what's the baseline?
- **Examples:**
  - Activation rate: 40% → 60% (measured 30 days post-launch)
  - Time-to-first-action: 3 days → 1 day
  - Support ticket volume: reduce "How do I get started?" tickets by 50%

**3. Define Definition of Done**
- **Question:** What criteria must be met before this is considered complete and ready for release?
- **Example:** "Checklist ships to 100% of new signups, activation rate tracking is instrumented, and no regression in sign-up conversion rate."

**Example:**

```markdown
## 7. Success and Measurement

- **Business objective**: Reduce 30-day churn from 15% to 8% (Q1 retention OKR).
- **Success metrics**: Activation rate (40% → 60%, measured 30 days post-launch);
  time-to-first-action (3 days → 1 day); support tickets for "getting started" (−50%).
- **Definition of done**: Checklist live for 100% of new signups, activation tracking
  instrumented, sign-up conversion rate not regressed.
```

### Outputs from Phase 7

- **Business objective:** The outcome this advances
- **Success metrics:** What to measure, with baselines
- **Definition of done:** Agreed release criteria

---

## Phase 8: Risks and Open Questions (30 minutes)

**Goal:** Surface what you don't know, what could go wrong, and how you'll address it.

### Activities

**1. Identify Risks**
- **Format:** For each risk, name it, note its potential impact, and state your mitigation plan.
- **Example:**

```markdown
## 8. Risks and Open Questions

- **Risk:** Users dismiss the checklist immediately and never re-engage with it.
  - **Mitigation:** Track dismissal rate; if >50%, iterate on timing or copy before scaling.
- **Risk:** Checklist steps don't resonate with all user types.
  - **Mitigation:** Start with primary audience (non-technical solopreneurs); personalize in a follow-on phase.
- **Assumption to validate:** Users who complete the checklist have meaningfully higher
  30-day retention. Will confirm with cohort analysis 30 days post-launch.
- **Open question:** Should we A/B test checklist vs. no checklist, or ship to 100%?
  Decision needed before engineering begins.
```

**2. Flag Unresolved Decisions**
- **What decisions must be made before engineering begins?** Name them explicitly.
- **What assumptions are you making that haven't been validated?** State them so the team can flag disagreement early.

### Outputs from Phase 8

- **Risks:** Named, with impact and mitigation for each
- **Unvalidated assumptions:** Stated explicitly
- **Open questions:** Decisions needed before work starts

---

## Phase 9: Level of Effort (30 minutes)

**Goal:** Estimate the size and engineering effort collaboratively across Product, Design, and Engineering DRIs.

### Activities

**1. Size the Work**
- **Scale:** XS / S / M / L / XL
- **Who:** PM, Design DRI, and Engineering DRI estimate together — not unilaterally by PM
- **Format:** T-shirt size + one or two sentences summarizing what drives the estimate

**Example:**

```markdown
## 9. Level of Effort

**Size**: M. Core checklist logic and session persistence are straightforward using the
existing modals framework. The main complexity is instrumentation — activation tracking
requires a new event pipeline. Design is one sprint; engineering is two.
```

**Tip:** The LOE conversation often surfaces scope assumptions that weren't explicit. If engineering pushes back on size, look first at the Feature Definition and Out of Scope sections — the boundary may need sharpening.

### Outputs from Phase 9

- **T-shirt size:** XS / S / M / L / XL
- **Effort summary:** What drives the estimate

---

## Phase 10: Ownership & Stakeholders (15 minutes)

**Goal:** Make accountability and communication structure explicit before work begins.

### Activities

**1. Fill the RACI Table**
- **Accountable:** Single owner. The person who has final say and answers for outcomes.
- **Responsible:** Those doing the work — typically PM, Eng Lead, and Design Lead.
- **Consulted:** Those whose input is needed before key decisions are made.
- **Informed:** Those kept up to date on progress but not in the decision-making loop.

**Example:**

```markdown
## 10. Ownership & Stakeholders

| Role        | Name(s)              | Notes                                              |
| :---------- | :------------------- | :------------------------------------------------- |
| Accountable | Jordan (PM)          | Final decisions on scope and priorities            |
| Responsible | Jordan, Alex, Sam    | PM, Eng Lead, Design Lead                          |
| Consulted   | Data, Support, GTM   | Input needed on instrumentation and messaging      |
| Informed    | Leadership, Marketing| Status updates at milestones, not in daily loop    |
```

**Tip:** If you have more than one Accountable, you have zero. Resolve before this PRD moves forward.

### Outputs from Phase 10

- **RACI table:** Completed with named individuals

---

## Complete Workflow: End-to-End Summary

```
Day 1:
├─ Phase 1: Summary (30 min)
├─ Phase 2: Problem Statement (60 min)
│  └─ Use: skills/problem-statement/SKILL.md
├─ Phase 3: Target Audience (30 min)
│  └─ Use: skills/proto-persona/SKILL.md
└─ Phase 4: User Stories (90-120 min)
   ├─ Use: skills/epic-hypothesis/SKILL.md
   ├─ Use: skills/epic-breakdown-advisor/SKILL.md
   └─ Use: skills/user-story/SKILL.md

Day 2:
├─ Phase 5: Feature Definition (60 min)
│  └─ Use: skills/user-story-mapping-workshop/SKILL.md (optional)
├─ Phase 6: Competitive Overview (45 min)
└─ Phase 7: Success and Measurement (30 min)

Day 3:
├─ Phase 8: Risks and Open Questions (30 min)
├─ Phase 9: Level of Effort (30 min)
├─ Phase 10: Ownership & Stakeholders (15 min)
└─ Review & Refine (60 min)
   └─ Read full PRD, polish, get feedback

Day 4 (Optional):
└─ Stakeholder Review & Approval
   └─ Present PRD to stakeholders, incorporate feedback
```

**Total Time Investment:**
- **Fast track:** 1.5-2 days (straightforward feature, clear requirements)
- **Typical:** 2-3 days (includes discovery synthesis, stakeholder review)
- **Complex:** 3-4 days (major initiative, multiple personas, extensive user stories)

---

## Examples

See `examples/sample.md` for full PRD examples.

Mini example excerpt:

```markdown
## 2. Problem Statement
- 60% of trial users drop off in first 24 hours, driven by lack of onboarding guidance.
## 7. Success and Measurement
- Business objective: Reduce 30-day churn from 15% to 8%.
- Success metrics: Activation rate 40% → 60%.
```

## Common Pitfalls

### Pitfall 1: PRD Written in Isolation
**Symptom:** PM writes PRD alone, presents finished doc to team

**Consequence:** No buy-in, team doesn't understand rationale

**Fix:** Collaborate on Phase 4 (user stories) with design + eng; review draft PRD before finalizing

---

### Pitfall 2: No Evidence in Problem Statement
**Symptom:** "We believe users have this problem" (no data, no quotes)

**Consequence:** Team questions whether problem is real

**Fix:** Use discovery insights from `skills/discovery-process/SKILL.md`; include customer quotes, analytics, support tickets

---

### Pitfall 3: Feature Definition Too Prescriptive
**Symptom:** PRD specifies exact UI, pixel dimensions, button colors

**Consequence:** Removes design collaboration, becomes waterfall spec

**Fix:** Keep Phase 5 high-level; let design own UI details

---

### Pitfall 4: No Success Metrics
**Symptom:** PRD defines problem + solution but no metrics

**Consequence:** Can't validate if feature succeeded

**Fix:** Always define business objective and success metrics in Phase 7 (what you're optimizing for)

---

### Pitfall 5: Out of Scope Not Documented
**Symptom:** No explicit exclusions in the Feature Definition

**Consequence:** Scope creep, stakeholders expect features not planned

**Fix:** Always fill the Out of Scope subsection in Phase 5, with rationale for each exclusion

---

### Pitfall 6: No Accountable Owner
**Symptom:** RACI table lists two or more people as Accountable

**Consequence:** Decisions stall; no one answers for outcomes

**Fix:** One Accountable, always. Resolve ambiguity before Phase 10 is complete.

---

## References

### Related Skills (Orchestrated by This Workflow)

**Phase 2:**
- `skills/problem-statement/SKILL.md` (component)
- `skills/problem-framing-canvas/SKILL.md` (interactive, for context)
- `skills/customer-journey-mapping-workshop/SKILL.md` (interactive, optional)

**Phase 3:**
- `skills/proto-persona/SKILL.md` (component)
- `skills/jobs-to-be-done/SKILL.md` (component, optional)

**Phase 4:**
- `skills/epic-hypothesis/SKILL.md` (component)
- `skills/epic-breakdown-advisor/SKILL.md` (interactive)
- `skills/user-story/SKILL.md` (component)

**Phase 5:**
- `skills/user-story-mapping-workshop/SKILL.md` (interactive, optional)

### External Frameworks
- Martin Eriksson, "How to Write a Good PRD" (2012) — PRD structure
- Marty Cagan, *Inspired* (2017) — Product spec principles
- Amazon, "Working Backwards" (PR/FAQ format) — Alternative to PRD

### Dean's Work
- [If Dean has PRD templates, link here]

---

**Skill type:** Workflow
**Suggested filename:** `prd-development.md`
**Suggested placement:** `/skills/workflows/`
**Dependencies:** Orchestrates 8+ component and interactive skills across 10 phases
