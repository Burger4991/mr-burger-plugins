# mr-burger-plugins — Project State
*Last updated: 2026-03-21*

## Phase
complete — plugin system audit done (2026-03-21)

## Plan
- **File:** `docs/superpowers/plans/2026-03-21-plugin-system-audit.md`
- **Status:** All 24 tasks complete

## Implementation
- **Active:** None
- **Done:**
  - Plugin system audit — full 5-phase audit complete
  - Spec: `docs/superpowers/specs/2026-03-21-plugin-system-audit-design.md`
  - Audit doc: `docs/audits/2026-03-21-plugin-system-audit.md`
  - Removed: `benchmark-guides` (lower-quality duplicate)
  - Cleaned: `settings.local.json` (160 → 78 allow entries; removed GSD, Obsidian, stale refs)
  - Updated: memory skill counts (91 skills, 16 agents)
  - Eval: all behavioral + regression checks PASS
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
- 2026-03-21 21:30: Plugin system audit approach decided — Option A (audit first); scope = full ~/.claude/ + mr-burger-plugins; 4-phase spec written and reviewed
