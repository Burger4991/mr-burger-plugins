# mr-burger-plugins — Project State
*Last updated: 2026-03-21 09:38*

## Phase
implementing — knowledge & workflow system (9 tasks, none started)

## Plan
- **File:** `docs/plans/2026-03-21-knowledge-workflow-system.md`
- **Current step:** Task 1 — create `session-state-reader` skill (dependency for all other tasks)
- **Spec:** `docs/specs/2026-03-21-knowledge-workflow-system-design.md`
- **Decided:** session-state-reader first; hook second; commands in order; /dump is new universal router above /capture; brainstorm docs in `docs/brainstorm/` per project
- **Open:** Nothing — ready to execute Task 1

## Implementation
- **Active:** Task 1 — session-state-reader skill
- **Done:** Spec written + approved (6 sections); plan written (9 tasks); PROJECT.md system deployed to all repos; wrap/resume/capture commands previously updated (will be superseded by this plan)
- **Blocked:** None

## Parked
- **band-materials eval:** `docs/plans/2026-03-21-band-materials-eval-plan.md` — 8 files in `mr-burger-music/eval/`, branch `feat/score-transformer-suite`
- **git-workflow-system plan:** superseded by knowledge-workflow-system plan (broader scope)

## Decisions Log
- 2026-03-21 09:38: PROJECT.md layer added to persistence system
- 2026-03-21 09:38: Git workflow system expanded to full knowledge & workflow system (added brainstorm capture, /dump command, session-state-reader shared skill)
- 2026-03-21 09:38: /dump chosen as universal router above /capture — /capture remains the filing layer
- 2026-03-21 09:38: Brainstorm docs in `docs/brainstorm/` per project; user-scope in `~/Documents/Knowledge/brainstorm/`
- 2026-03-21 09:38: Hook narrates git ops to build habits, not replace them

## Open Questions
- After this system: resume band-materials eval, or use PR workflow as practice on README updates first?
