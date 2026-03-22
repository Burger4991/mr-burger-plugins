# mr-burger-plugins — Project State
*Last updated: 2026-03-22*

## Phase
complete — repo cleaned up; all audit work pushed; stale plans deleted

## Implementation
- **Active:** None
- **Done:**
  - Plugin system audit — full 5-phase audit + eval complete
  - Removed: `benchmark-guides` skill (lower-quality duplicate of `benchmarks`)
  - Cleaned: `settings.local.json` (160 → 78 allow entries)
  - Updated: memory skill counts (91 skills, 16 agents)
  - Moved: `pixel-agents/` to `~/Documents/Tech/third-party/`
  - Fixed: `setup.sh` warns on silent skill/agent/command skips
  - Documented: skill-loading architecture in `CLAUDE.md`
  - Deleted: `gemini/` agents directory (8 files)
  - Removed: Gemini symlink block from `setup.sh` + deleted dangling `~/.gemini/extensions` symlink
  - Deleted: 10 completed plan/spec files (all work was done and marked in TASKS.md)
  - Added: `.playwright-mcp/` to `.gitignore`
  - All commits pushed to origin
- **Blocked:** None

## Parked
- **band-materials eval:** `docs/plans/2026-03-21-band-materials-eval-plan.md` + `docs/specs/2026-03-21-band-materials-eval-design.md` — Someday in TASKS.md; no active work
- **score-transformer build-out:** `docs/superpowers/plans/2026-03-21-mr-burger-music-score-transformer.md` — branch merged but full suite (guide tones, enclosures, 12-key generator) status unclear; needs review before starting
- **GWS plugin:** 92 Google Workspace skills orphaned at `~/.agents/skills/` — not loaded by Claude Code; decision deferred (integrate or leave)

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
- 2026-03-21 21:30: Plugin system audit approach decided — Option A (audit first); scope = full ~/.claude/ + mr-burger-plugins
- 2026-03-21: Audit executed and complete — 0 collisions, 1 redundancy removed, settings cleaned, architecture documented
- 2026-03-21: gemini/ directory deleted — Gemini agent files no longer maintained here
- 2026-03-21: pixel-agents moved to third-party/ — was stray embedded repo
- 2026-03-22: Gemini symlink block removed from setup.sh — gemini/ is gone, no plans to restore
- 2026-03-22: 10 stale plan/spec files deleted — all were completed work never cleaned up
- 2026-03-22: .playwright-mcp/ added to .gitignore — Playwright MCP screenshots not repo content
