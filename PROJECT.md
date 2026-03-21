# mr-burger-plugins — Project State
*Last updated: 2026-03-21 20:00*

## Phase
complete — workflow system shipped, eval + audit done, all pushed and clean

## Plan
- **File:** `docs/plans/2026-03-21-knowledge-workflow-system.md`
- **Current step:** complete
- **Decided:** session-state-reader shared by all commands; two-agent eval pattern (audit + behavioral) for QA; plugin hygiene audit checklist added to knowledge; "done includes docs" as completion criteria

## Implementation
- **Active:** None
- **Done:**
  - Workflow system: session-state-reader, 11 commands, workflow-agent — all shipped
  - Eval session: 5 pass / 6 minor issues / 0 needs work → all 8 fixes applied and pushed
  - Audit: 3 broken symlinks removed, stale benchmark-mastery-analyzer deleted, Cowork daily name collision resolved
  - Cheat sheets: all 5 files updated (new commands + workflow-agent)
  - IR platform: 1 pending commit pushed
  - /reflect: tech-systems.md + workflows.md updated
- **Blocked:** None

## Parked
- **band-materials eval:** `docs/plans/2026-03-21-band-materials-eval-plan.md` — 8 files in `mr-burger-music/eval/`; branch `feat/score-transformer-suite` merged

## Decisions Log
- 2026-03-21 09:38: PROJECT.md layer added to persistence system
- 2026-03-21 09:38: /dump chosen as universal router above /capture
- 2026-03-21 09:38: Brainstorm docs in `docs/brainstorm/` per project
- 2026-03-21 09:38: Hook narrates git ops to build habits, not replace them
- 2026-03-21 17:15: /plan invokes brainstorming first; describe vs invoke antipattern named
- 2026-03-21 17:16: workflow-agent shipped (open/close modes)
- 2026-03-21 20:00: Two-agent eval pattern established (audit agent + behavioral eval agent in parallel)
- 2026-03-21 20:00: "Done includes docs" — cheat sheets are part of completion, not afterthought
- 2026-03-21 20:00: ir-data-pipeline/benchmark-mastery-analyzer removed — ir-teaching version is canonical
