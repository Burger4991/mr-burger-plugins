---
name: skill-index
description: MUST USE this skill whenever the user asks "which skill should I use" or needs to navigate the ir-teaching system. Trigger on: "which skill", "what skills exist", "help me find", "how do I get started", "workflow for building a unit", "I need a skill for..."... Complete navigation guide mapping common teaching tasks to the right skill or agent, with quick lookup table, full skill directory, agent descriptions, and workflow diagrams.
---

# Skill Discovery Index

**For:** 10th Grade Intensive Reading Teacher
**Plugin:** ir-teaching
**Active Skills:** 37
**Active Agents:** 9 (unit-planner, lesson-plan-coordinator, student-packet-builder, unit-reviser, unit-reviewer, sub-plan-generator, esol-adapter, assessment-builder, quality-reviewer)
**Last Updated:** 2026-03-17

---

## Quick Lookup: "I want to..."

| I want to... | Start with | Then use | Requires |
|---|---|---|---|
| Check brand/visual standards for materials | `brand-identity` | (Single source of truth for all design decisions) | — |
| Build a full 6-day IR unit | `menu-mode-planner` | → `unit-builder-protocol` (all deliverables) | Text passage, benchmark selection |
| Plan a single lesson (not IR) | `lesson-plan-coordinator` agent | → `benchmarks` (for standards) | — |
| Create student worksheets/packets (standalone) | `student-packet-builder` agent | → `student-packet-design-guide` + `benchmarks` | — |
| Check student packet formatting standards | `student-packet-design-guide` | (Typography, layout, frame boxes) | — |
| Design a multi-week unit (any subject) | `unit-planner` agent | → `teaching-templates` | — |
| Look up a benchmark standard | `benchmarks` skill | Specify code (e.g., ELA.10.R.1.2) or topic | — |
| Select vocabulary for bellringers | `vocabulary-instruction` | → `bellringer-builder` (create items) | Unit text passage |
| Create a graphic organizer | `organizer-design` | → `benchmarks` (template options) | Benchmark selected |
| Write teacher scripts for gradual release | `gradual-release-scripts` | → `ir-framework` (I Do/We Do structure) | Benchmark + organizer |
| Teach/embed the STOP strategy | `stop-strategy` | → `cubes-annotation` (full workflow) + `assessment-design` (MC items) | — |
| Build a test prep / cold read unit | `test-prep-unit` | → `attack-the-passage` (protocol) + `stop-strategy` + `assessment-design` | 4 texts (2 fiction, 2 nonfiction) |
| Teach Attack the Passage protocol | `attack-the-passage` | → `stop-strategy` (Phase 3) + `cubes-annotation` (Phases 1-2) + `cer-writing-guide` / `race-strategy` (Phase 4) | — |
| Teach/embed the RACE/ACE strategy | `race-strategy` | → `cer-writing-guide` (CER alternative) + `assessment-design` (CR format) | — |
| Build CER/ACE writing scaffolds | `cer-writing-guide` | → `assessment-design` (student format) | — |
| Design an assessment | `assessment-design` | → `assessment-builder` agent (produces .docx files) | Benchmark + text |
| Build assessment .docx files | `assessment-builder` agent | → `assessment-rubrics` (scoring) | Benchmark + text + unit config |
| Review completed deliverables | `quality-reviewer` agent | Two-stage: spec compliance → quality review | Completed deliverable(s) |
| Create bellringers | `bellringer-builder` | → `vocabulary-instruction` (word selection) | 18 vocabulary words |
| Build rubrics | `assessment-rubrics` | → `benchmarks` (achievement levels) | Benchmark selected |
| Update an existing unit | `unit-reviser` agent | Handles text swaps, benchmark changes | Existing unit folder |
| Diagnose why a unit didn't work | `unit-troubleshooter` | → `unit-reviser` (with diagnosis) | Student data or observation |
| Check if a unit is done | `unit-quality-gate` | (Run automatically after unit-builder-protocol) | All 4 deliverables |
| Ship / print / archive a unit | `unit-distribution` | (After quality gate passes) | Quality gate PASS |
| Restore a previous version | `unit-recovery` | (From _archive/ snapshots or git) | _archive/ folder |
| Evaluate feedback before revising | `unit-feedback-protocol` | → `unit-reviser` (accepted items only) | Feedback from source |
| Gather context before planning | `unit-discovery` | → `menu-mode-planner` (pre-loaded context) | — |
| Quality-check a skill before deploy | `skill-quality-gate` | (Before syncing to ~/.claude/) | — |
| Resume an interrupted build | `session-continuity` | → `unit-builder-protocol` (from last batch) | _build-state.json |
| Get a fresh-eyes unit review | `unit-reviewer` agent | Independent cold review of deliverables | Completed unit folder |
| Adapt materials for ESOL | `esol-adapter` agent | Transforms materials for specific proficiency levels | Completed materials |
| Teach question stem analysis / categorization | `question-stem-analysis` | → `attack-the-passage` (Phase 1) + `benchmarks` (stem map) | MC questions from text |
| Track and analyze student error patterns | `error-analysis-tracker` | → `stop-strategy` (S/T/O reteach) + `unit-troubleshooter` (diagnosis) | Scored MC data |
| Teach annotation strategies | `cubes-annotation` | → `stop-strategy` (STOP detail) | — |
| Set up feedback system | `feedback-system` | → `feedback-checkpoint-builder` | — |
| Read district files | `district-files-reader` | → `benchmarks` (for alignment) | District PDF/doc files |
| Manage file versions | `file-management` | (Use with unit-builder-protocol) | — |
| Build an interactive lesson for the board | `interactive-lesson-builder` | → requires `cubes-annotation` + `ir-framework` | Lesson Plan + Answer Key |

---

## All Skills (37)

### Unit Building & Orchestration

- **`menu-mode-planner`** — Entry point for unit planning, collects all preferences upfront
- **`unit-builder-protocol`** — Full 6-day IR unit generation (ORCHESTRATOR). Outputs: Teacher Plan (.docx), Student Packet (.docx), Answer Key (.docx), Feedback Forms (.docx), optional Teacher Slides (.pptx). All files in ONE flat folder per unit.
- **`ir-framework`** — 6-day cycle structure, daily rotations (Bellringer → TL → IND), gradual release
- **`teaching-templates`** — Reusable lesson structures, naming conventions, formats, 8 visual components with design tokens and docx-js implementation code
- **`brand-identity`** — **Single source of truth** for all visual design decisions. Design philosophy ("Structured Clarity"), grayscale color system, 5-level typography scale, spacing system, terminology standards, document header/footer specs, 5-point design self-critique checklist, and implementation notes for docx-js/python-docx. Read before generating ANY deliverable.
- **`unit-discovery`** — Optional pre-planning context gathering (district files, student data, recent units check) before menu-mode-planner
- **`unit-quality-gate`** — Structured quality checklist run after every build (8 checks: deliverables, sync, bellringers, organizer, assessment, feedback, ESOL, brand)
- **`unit-distribution`** — Ship a completed unit: print, upload to OneDrive, archive as template, adapt for ESOL, share with department
- **`unit-troubleshooter`** — Diagnose root causes when a unit doesn't land (before revising). Maps symptoms to fixes.
- **`unit-recovery`** — List and restore previous versions from _archive/ snapshots or git history
- **`unit-feedback-protocol`** — Evaluate feedback from admins/coaches/peers critically before revising (Accept/Modify/Reject/Clarify)
- **`session-continuity`** — Resume an in-progress unit build after session ends (reads _build-state.json)
- **`skill-quality-gate`** — Quality checklist for IR teaching skills before deploying to ~/.claude/
- **`file-management`** — Versioning, organization, file naming standards

### Benchmark & Standards

- **`benchmarks`** — Central repository for all 10 ELA.10.R benchmarks (with `standards/` subdirectory). All rewritten from 10th Grade Planning Guide (pages 17-31).
  - R.1.1 Literary Elements, R.1.2 Theme, R.1.3 Coming of Age & Conflicting Perspectives, R.1.4 Layers of Meaning & Ambiguity in Poetry, R.2.1 Text Structure, R.2.2 Central Idea (Historical American Speeches/Essays), R.2.3 Purpose (Historical American Speeches/Essays), R.2.4 Argument, R.3.1 Figurative Language & Mood, R.3.4 Rhetoric

### Instruction Design

- **`vocabulary-instruction`** — Tier 2/3 word selection, 6-day progression, bellringer vocabulary
- **`bellringer-builder`** — Context clues bellringer creation (18 words per unit: 3/day × 6 days, 2 MC + 1 written)
- **`gradual-release-scripts`** — I Do / We Do / You Do w/ Partner / You Do teacher talk scripts
- **`cer-writing-guide`** — RACE and CER constructed response frameworks (one chosen per unit). Includes systematic scaffolding: Restate practice Days 1-2, Explain scaffolding Days 3-4, full CR Days 5-6.
- **`organizer-design`** — Graphic organizer creation aligned to benchmarks
- **`student-packet-design-guide`** — Typography, layout, sentence frame boxes, organizer formatting, and visual design standards for all student-facing materials. Referenced by student-packet-builder agent.
- **`stop-strategy`** — STOP test-taking strategy (Silly/Tricky/Opposite/Proven). Two modes: Simplified Default (select + justify) and Full STOP (label all four). Teaching sequence, anchor charts, practice templates, ESOL modifications, and agent integration reference.
- **`race-strategy`** — RACE constructed response framework (Restate/Answer/Cite/Explain). Includes ACE shortened form. Three-tier progression (Lite → Standard → Full). Teaching sequence, scoring rubrics, anchor charts, ESOL modifications, and agent integration reference.
- **`assessment-design`** — STOP protocol, RACE/CER constructed response design, assessment item design
- **`assessment-rubrics`** — Rubrics aligned to Florida BEST ELA achievement level descriptors (Levels 2-5)
- **`cubes-annotation`** — CUBES annotation protocol for BOTH text passages AND questions. Passages: 3-step layered approach (close reading → question-driven rereading → synthesis). Questions: 3-step approach (CUBES → find key details → STOP strategy for answer elimination). Adaptable by benchmark focus. Embeddable annotation boxes for student packets.

### Test Prep & Cold Read

- **`attack-the-passage`** — 4-phase test-taking protocol: Phase 1 (Attack the Questions — C-U-B annotation), Phase 2 (Attack the Passage — evidence gathering), Phase 3 (Attack the Answers — STOP elimination), Phase 4 (Attack the Justification — CER/RACE proof). Includes teacher implementation scripts, student quick reference card, error analysis tracker, review games, ticket system, benchmark-specific hunt guides, and ESOL modifications. The PROTOCOL skill.
- **`test-prep-unit`** — 16-day unit framework for Q3-Q4 test prep: 4 texts (2 fiction, 2 nonfiction) × 4 days each. Each 4-day cycle: Day 1 cold read + MC, Day 2 question stem analysis, Day 3 STOP elimination + CER/RACE, Day 4 review game + extended response. Includes ticket system, tracker system, benchmark alignment, calendar templates, materials checklists, differentiation, and ESOL strategies. The UNIT skill.
- **`question-stem-analysis`** — Day 2 instructional skill for teaching students to categorize MC questions by type (Literal/Inference/Analysis/Evaluation) and benchmark, write hunt predictions, and connect C-U-B annotations to evidence strategy. Includes benchmark-to-stem map, teaching sequence (I Do/We Do/You Do), student worksheet template, signal word decoder, common errors, and ESOL modifications.
- **`error-analysis-tracker`** — Complete system for tracking, aggregating, and acting on MC error patterns (S/T/O/MR/R/V/NE codes). Includes per-text student tracker, unit progress tracker, class error audit, per-question breakdown, unit trend analysis, chronic error identification, error-to-reteach map, and small group pull schedule. Connects error data to instructional response.

### Student Support

- **`esol-core`** — Complete ESOL strategy bank: sentence frames, vocabulary scaffolds, modifications, scaffolding progression
- **`feedback-system`** — Formative feedback structure for Days 1-2, 3-4, 5-6
- **`feedback-checkpoint-builder`** — Benchmark-specific feedback checklists (Day 4 organizer, Day 6 CR response)

### Utilities

- **`district-files-reader`** — Extract text, margin questions, vocabulary from district PDFs
- **`benchmark-mastery-analyzer`** — Analyze FAST PM results and identify benchmark mastery gaps (bridges to ir-data-pipeline)

### Interactive Projection

- **`interactive-lesson-builder`** — Generates a single self-contained HTML website per unit for Promethean board projection. Replaces slide deck (Phase 5B) with an interactive tool (Phase 5C). Features: teacher-paced progressive reveal, text annotations with think-aloud popups, bellringer display with configurable timer, organizer display with GR phases, STOP protocol walkthrough, ACE modeling, MC polls, teacher tally counter, light/dark mode toggle. Requires completed Lesson Plan + Answer Key.

---

## Agents (8)

| Agent | Scope | When to Use | Primary Output |
|---|---|---|---|
| **`unit-planner`** | Multi-week unit design (any subject) | General UbD framework planning. IR units → routes to menu-mode-planner (hard gate) | Unit outline, pacing guide |
| **`lesson-plan-coordinator`** | Single lesson planning | One-off lessons not part of IR cycle | Single lesson plan (.docx) |
| **`student-packet-builder`** | Student-facing materials | Standalone worksheets, non-IR packets | Worksheet packet (.docx) |
| **`assessment-builder`** | Assessment .docx files | MC items + CR prompts + answer keys + rubrics. Phase 6 of unit builds. | Assessment (.docx) + Answer Key (.docx) |
| **`quality-reviewer`** | Two-stage deliverable review | Auto-runs after each Phase in unit builds. On-demand for standalone work. | Review report (PASS/FAIL per check) |
| **`unit-reviewer`** | Fresh-eyes independent review | Cold review of completed unit — no build context. Finds sync issues, missing elements, benchmark misalignment. | Structured review report |
| **`unit-reviser`** | Update existing units | Text swaps, benchmark changes, data-driven revisions | Updated deliverables |
| **`sub-plan-generator`** | Substitute teacher plans | When you'll be absent | Simplified sub plan (.docx) |
| **`esol-adapter`** | Material adaptation | Adapt materials for ESOL levels 1-5 | Modified packets with scaffolds |

**v2.0 Upgrade (all agents):** Every agent now has (1) Required Skill Invocations (calls skills via Skill tool, not just "references" them), (2) Verification Gate with Iron Law (must state evidence before claiming done), (3) Brand enforcement for .docx-producing agents.

---

## Workflow: Build a Complete 6-Day IR Unit

```
menu-mode-planner (HARD GATE — all tabs must complete before building)
→ brand-identity (read FIRST — design philosophy, colors, typography, spacing)
→ district-files-reader (if needed)
→ benchmarks (look up standard)
→ ir-framework (understand cycle)
→ vocabulary-instruction (select 18 words)
→ bellringer-builder (create bellringer items)
→ organizer-design (create graphic organizer)
→ cubes-annotation (embed annotation boxes)
→ unit-builder-protocol (ORCHESTRATOR - generates all deliverables)
    ├─ Phase 3: Teacher Lesson Plan (.docx) → quality-reviewer (auto)
    ├─ Phase 4: Student Packet (.docx) → quality-reviewer (auto)
    ├─ Phase 5: Answer Key (.docx) → quality-reviewer (auto + cross-file sync)
    ├─ Phase 6: assessment-builder agent → Assessment (.docx) → quality-reviewer (auto)
    ├─ Feedback Forms (.docx)
    ├─ Teacher Slides (.pptx) — optional
    └─ Interactive Lesson (.html) — optional (replaces slides, Phase 5C)
→ quality-reviewer: Final cross-file sync across ALL deliverables
→ file-management (organize and version)
```

**Output:** All files in ONE flat folder per unit. Core deliverables are .docx; optional teacher slides are .pptx.

## Workflow: Build a Test Prep / Cold Read Unit (Q3-Q4)

```
test-prep-unit (FRAMEWORK — 16 days, 4 texts × 4 days)
→ attack-the-passage (PROTOCOL — 4-phase strategy for each text)
→ brand-identity (read FIRST)
→ benchmarks (select 2-3 benchmarks per text)
→ assessment-design (10 MC per text, 80/20 benchmark/vocab split, S/T/O/P distractor design)
→ stop-strategy (Phase 3 — elimination teaching)
→ cer-writing-guide / race-strategy (Phase 4 — justification framework per genre)
→ question-stem-analysis (Day 2 — stem categorization, benchmark mapping, hunt predictions)
→ error-analysis-tracker (Days 3-4 — error coding, class audit, reteach routing)
→ bellringer-builder (vocabulary bellringers, 3 words/day)
→ esol-core (integrated ESOL strategies)
For each text (4-day cycle):
    ├─ Student Packet: passage + 10 MC + C-U-B boxes + tracker + justification templates
    ├─ Teacher Lesson Plan: 4-day cycle with scripts per phase
    ├─ Answer Key: S/T/O/P labels + CER/RACE exemplars for all MC
    └─ Review game materials (Day 4)
```

**Output:** Per-text packets + unit tracker + reference cards. All .docx files.

**Superpowers Integration (v2.0):** Unit building uses 5 patterns from `superpowers-cowork`: Hard Gate (no building without menu completion), Bite-Sized Tasks (2-5 min per task in TodoWrite), Two-Stage Review (spec compliance then quality via quality-reviewer agent), Verification Iron Law (evidence before "unit complete"), and Parallel Dispatch (independent deliverables build simultaneously).

**Agent Upgrades (v2.0):** All 8 agents now have Required Skill Invocations (must call skills via Skill tool), Verification Gates (must state evidence), and Brand Enforcement (for .docx producers). New agents: assessment-builder (builds MC + CR .docx files) and quality-reviewer (auto-runs after each build Phase).

---

## Cross-Plugin References

This plugin focuses on **instruction design and delivery**. Related plugins handle other domains:

| Need | Plugin | Key Skills |
|---|---|---|
| Student data analysis | **ir-data-pipeline** | student-data-processor, growth-analyzer, report-builder, intervention-planner |
| Classroom logistics | **ir-classroom-ops** | behavior-tracker, observation-prep, parent-contact-log, sub-folder-builder |
| Personal productivity | **mr-burger-workflow** | second-brain-ops, area-context, notion-sync |
| Cross-plugin sync | **cross-plugin-bridge** | plugin-registry, work-logger |
| Workflow discipline | **superpowers-cowork** | brainstorming, verification-before-completion, writing-plans, parallel-execution, quality-driven-creation |

---

## By Benchmark Topic

| Topic | Code | File |
|---|---|---|
| Literary Elements | ELA.10.R.1.1 | `standards/literary-elements.md` |
| Theme | ELA.10.R.1.2 | `standards/theme.md` |
| Coming of Age & Conflicting Perspectives | ELA.10.R.1.3 | `standards/point-of-view.md` |
| Layers of Meaning & Ambiguity in Poetry | ELA.10.R.1.4 | `standards/poetry.md` |
| Text Structure & Features | ELA.10.R.2.1 | `standards/text-structure.md` |
| Central Idea (Historical American Speeches/Essays) | ELA.10.R.2.2 | `standards/central-idea.md` |
| Purpose (Historical American Speeches/Essays) | ELA.10.R.2.3 | `standards/purpose-perspective.md` |
| Argument | ELA.10.R.2.4 | `standards/argument.md` |
| Figurative Language & Mood | ELA.10.R.3.1 | `standards/figurative-language.md` |
| Rhetoric | ELA.10.R.3.4 | `standards/rhetoric.md` |
