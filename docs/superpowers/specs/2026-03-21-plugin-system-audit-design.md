# Plugin System Audit — Design Spec
*Date: 2026-03-21*
*Status: Approved*

## Overview

A full audit of the Claude Code plugin system at user scope (`~/.claude/`) and the `mr-burger-plugins` source repo. Goal: establish ground truth on what is loaded, from where, and what conflicts exist — then clean up based on findings. No speculative changes.

## Goals

- Every active skill, agent, command, and hook has a known, verified source
- No ambiguous name collisions where Claude might invoke the wrong thing
- A clean inventory doc to reference going forward
- Community plugins clearly identified and documented; boundary with custom plugins recorded in CLAUDE.md

## Out of Scope

- Redesigning the loading/symlink mechanism (unless audit reveals it's fundamentally broken)
- Adding or expanding skills
- Cowork packaging changes

## Success Criteria

- Full inventory of all items in `~/.claude/` with source and status verified
- Name collision report produced (custom vs community, skills + agents)
- Within-plugin overlap candidates identified
- Broken symlinks fixed
- `~/.claude/CLAUDE.md` updated with documented community/custom plugin boundary
- Audit doc committed to repo

---

## Phase 1: Full `~/.claude/` Inventory

Audit every location at user scope:

| Location | What to Check |
|---|---|
| `~/.claude/skills/` | All entries — valid symlink, broken symlink, or regular file; target path |
| `~/.claude/agents/` | All entries — valid symlink, broken symlink, or regular file; target path |
| `~/.claude/commands/` | All files — symlinked or local; target path |
| `~/.claude/hooks/` | All hook scripts — which event, what it runs, where it points |
| `~/.claude/plugins/` | Plugin registrations + full cache inventory (what community plugins are loaded, what skills/agents they expose) |
| `~/.claude/settings.json` | Hooks, permissions, env vars — anything pointing to a path that no longer exists |
| `~/.claude/settings.local.json` | Same — local overrides |
| `~/.claude/CLAUDE.md` | Global instructions — stale content, dead paths, conflicting rules |
| `~/.claude/memory/` | Memory files — references to dead paths or outdated system state |
| `~/.claude/keybindings.json` | Bindings pointing to removed or renamed commands |
| `~/.claude/projects/` | Project-level `.claude/` configs that shadow or conflict with user-level |

---

## Phase 2: Collision Detection

### Custom vs Community
- Extract all skill/agent names from `~/.claude/plugins/cache/` (community plugins, especially superpowers)
- Cross-reference against every skill and agent name in `mr-burger-plugins`
- Flag exact name matches — these are ambiguous; Claude may invoke the wrong one

### Within-Plugin Overlaps
- Flag skills in the same plugin with overlapping names or suspected redundant purpose
- **Consolidation rule:** Consolidate if (a) both skills share more than half their behavioral instructions verbatim or near-verbatim, or (b) one skill's description is a strict subset of the other's and would produce functionally identical output for the same input. Otherwise, document as distinct and note the difference.
- Known candidates to investigate:
  - `benchmarks` + `benchmark-guides` + 11 individual `benchmark-[topic]` skills (ir-teaching)
  - `feedback-system` + `feedback-checkpoint-builder` (ir-teaching)
  - `unit-quality-gate` + `skill-quality-gate` (ir-teaching)
  - `unit-recovery` + `unit-troubleshooter` (ir-teaching)
  - `esol-core` + `esol-strategies` (ir-teaching)
  - `interactive-lesson-builder` exists as both a skill and an agent (ir-teaching)
  - `session-logger` (mr-burger-music) vs session-related skills in mr-burger-workflow

### Commands / Hooks / Agents
- Check mr-burger-workflow commands against any community plugin commands with the same trigger
- Check hooks — are any events handled by both a custom hook and a community plugin hook?

---

## Phase 3: Findings Report

Produce a structured markdown report at `docs/audits/2026-03-21-plugin-system-audit.md` with:

```
## Summary
- Total skills (custom): N
- Total agents (custom): N
- Broken symlinks: N
- Name collisions — skills + agents (custom vs community): N
- Within-plugin overlap candidates: N

## Broken Symlinks
[list with path and what it was pointing to]

## Name Collisions — Custom vs Community
[list: skill name | custom source | community source]

## Within-Plugin Overlap Candidates
[list: skill A | skill B | suspected overlap | recommendation]

## Settings Issues
[anything in settings.json/local pointing to dead paths; include keybindings.json issues here]

## Project-Level Conflicts
[any ~/.claude/projects/ configs that shadow or conflict with user-level settings]

## Memory / CLAUDE.md Issues
[stale references found]

## Decisions Made
[what was fixed and why]
```

---

## Phase 4: Cleanup

Based on findings only — no speculative changes.

**Actions (in order):**
1. Fix broken symlinks (or remove orphans)
2. Resolve name collisions — tiebreaker rule: prefer namespace prefix if the skill is actively used and customized (e.g., rename `interactive-lesson-builder` → `ir-interactive-lesson-builder` so it won't clash with any community skill of the same name); prefer removal only if the skill is a straight duplicate of community functionality with no customization; rename only if the community skill name is clearly canonical and yours is the divergent one. "Actively used" means the skill is referenced in CLAUDE.md, a hook, a command, or a cheat sheet.
3. Consolidate within-plugin overlaps where clearly redundant (read both skill files, decide)
4. Remove stale entries from settings.json/settings.local.json
5. Update CLAUDE.md and memory files if dead paths found
6. Re-run `./scripts/setup.sh` to verify clean state
7. Final verification pass — re-inventory `~/.claude/`, confirm zero broken symlinks, confirm no remaining name collisions, and verify all settings.json paths resolve correctly

---

## Deliverable

- `docs/audits/2026-03-21-plugin-system-audit.md` — living audit doc (inventory + findings + decisions)
- Review checkpoint before committing — after Phase 4 Steps 1–5, pause and present the planned destructive changes list (removals, renames) to the user. Wait for explicit approval before committing. Record sign-off in the audit doc under "Decisions Made."
- All fixes committed to main
- `PROJECT.md` updated to reflect audit complete
