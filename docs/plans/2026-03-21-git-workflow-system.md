# Git Workflow System — Implementation Plan
*Created: 2026-03-21*

> Build git/GitHub habits and tooling into the existing workflow system. Goal: Mr. Burger internalizes these as real skills, not just automation. Narrate, teach, and build habits alongside the tooling.

---

## Order of Execution

### Phase 1 — Foundation (do first, everything else depends on this)

- [ ] **Task 1: Update `/resume`** — surface context hierarchy correctly: PROJECT.md → HANDOFF.md → TASKS.md (project-filtered). Already partially done; tighten the order and make PROJECT.md the clear lead.

- [ ] **Task 2: Update `/capture`** — use current conversation context automatically when routing brain dumps. Claude should infer the life area and file without asking for every item. Ask only when genuinely ambiguous.

### Phase 2 — Commit discipline

- [ ] **Task 3: Update commit skill** — make message body non-optional. Body explains *why*, not what. Add examples relevant to Mr. Burger's actual repos (plugin updates, unit additions, portfolio features).

### Phase 3 — Cheat sheets

- [ ] **Task 4: GitHub quick-reference cheat sheet** — git commands, branch rules, PR steps, issue linking. Practical and scannable. Save to `~/Desktop/github-cheat-sheet.md`.

- [ ] **Task 5: Project workflow cheat sheet** — the full habit loop: branch → work → commit (with body) → PR → merge → tag/release. How git features map to the existing PROJECT.md / HANDOFF.md / TASKS.md system. Save to `~/Desktop/project-workflow-cheat-sheet.md`.

### Phase 4 — Repo hygiene

- [ ] **Task 6: `.gitignore` audit** — check all repos for uncommitted junk (`__pycache__`, `.env`, `node_modules`, `.DS_Store`, `.git 2`, `.git.nosync`). Fix as needed.

- [ ] **Task 7: README audit + updates** — every repo gets a real README: what it is, how to run it, gotchas. Repos: ir-platform, gaby-portfolio, mr-burger-plugins. Use PR workflow to do each one.

### Phase 5 — System feature (bigger, save for last)

- [ ] **Task 8: Context-loading hierarchy** — build a mechanism for Claude to detect and load CLAUDE.md → PROJECT.md → TASKS.md → workflow files top-down at session start. May involve a hook or resume enhancement.

---

## Guiding Principles

- Narrate git operations — show the manual steps alongside automation
- Each README update is a PR, not a direct commit to main — practice the habit
- Commit messages have a body. Always.
- Habits first, automation second

## Repos in Scope

| Repo | Path |
|------|------|
| mr-burger-plugins | `~/Documents/Tech/mr-burger-plugins/` |
| ir-platform | `~/Desktop/ir-platform/` |
| gaby-portfolio | `~/Desktop/gaby-portfolio/` |
