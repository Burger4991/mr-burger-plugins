# mr-burger-plugins — Project State
*Last updated: 2026-03-21*

## Phase
complete — plugin system audit done; no active implementation

## Plan
- **File:** `docs/superpowers/plans/2026-03-21-plugin-system-audit.md`
- **Status:** All 24 tasks complete
- **Audit doc:** `docs/audits/2026-03-21-plugin-system-audit.md`

## Implementation
- **Active:** None
- **Done:**
  - Plugin system audit — full 5-phase audit + eval complete
  - Removed: `benchmark-guides` skill (lower-quality duplicate of `benchmarks`)
  - Cleaned: `settings.local.json` (160 → 78 allow entries; removed GSD, Obsidian, stale superpowers 5.0.2 refs)
  - Updated: memory skill counts (91 skills, 16 agents)
  - Moved: `pixel-agents/` to `~/Documents/Tech/third-party/` (was stray embedded repo)
  - Fixed: `setup.sh` now warns on silent skill/agent/command skips instead of silently dropping
  - Documented: skill-loading architecture in `CLAUDE.md` (3-mechanism system, shadowing risk, superpowers dual-presence)
  - Deleted: `gemini/` agents directory (8 files, no longer needed)
  - All eval and regression checks PASS
- **Blocked:** None

## Parked
- **band-materials eval:** `docs/plans/2026-03-21-band-materials-eval-plan.md` — 8 files in `mr-burger-music/eval/`; branch `feat/score-transformer-suite` merged
- **GWS plugin:** 92 Google Workspace skills orphaned at `~/.agents/skills/` — not loaded by Claude Code; decision deferred (integrate or leave)
- **Untracked plan:** `docs/superpowers/plans/2026-03-21-fill-course-gaps.md` — needs review

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
- 2026-03-21: Audit executed and complete — 0 collisions, 1 redundancy removed, settings cleaned, architecture documented
- 2026-03-21: gemini/ directory deleted — Gemini agent files no longer maintained here
- 2026-03-21: pixel-agents moved to third-party/ — was stray embedded repo (pablodelucca/pixel-agents)
