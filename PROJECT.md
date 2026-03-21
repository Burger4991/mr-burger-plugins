# mr-burger-plugins — Project State
*Last updated: 2026-03-21 09:38*

## Phase
implementing — band-materials eval framework (8 tasks, none started)

## Plan
- **File:** `docs/plans/2026-03-21-band-materials-eval-plan.md`
- **Current step:** Task 1 of 8 — not started
- **Decided:** Eval approach = Test Case Library + Rubric (not golden examples or self-critique); subagent reads skill.md and executes directly (no tool calls to the skill); human reviews all passing items, subagent triages failures only; results format = Summary + Top issues sections
- **Open:** Nothing — plan is approved and ready to execute

## Implementation
- **Active:** band-materials eval framework — 8 files to create in `mr-burger-music/eval/`, none exist yet
- **Done:** mr-burger-music plugin Phase 1 + 2 complete (14 knowledge files, 5 skills, 2 agents, merged to main); spec and plan for eval framework written and committed
- **Blocked:** None — working branch is `feat/score-transformer-suite`

## Decisions Log
- 2026-03-21: mr-burger-music plugin formalized — merged Phase 1 + 2 to main
- 2026-03-21: Eval approach chosen: Test Case Library + Rubric over golden examples or self-critique
- 2026-03-21: Subagent executes band-materials skill directly from skill.md — no tool call indirection
- 2026-03-21: Results format: Summary + Top issues sections (spec updated to match plan)
- 2026-03-21: Band-materials skill expansion deferred until eval is built — eval first for a baseline

## Open Questions
- After eval is built: what expansions does band-materials need?
- Other skills that need eval frameworks?

## Watch Out For
- Working branch: `feat/score-transformer-suite` — not main
- Branch has other unrelated work (score-transformer, mscz_utils, band-rehearsal skill) — don't merge everything at once
- Skill stub .md files can appear in `~/.claude/commands/` after package operations — run `ls ~/.claude/commands/` periodically and delete orphans
