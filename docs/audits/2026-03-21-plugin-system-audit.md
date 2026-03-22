# Plugin System Audit
*Date: 2026-03-21 | Status: In Progress*

## Summary
- Total custom skills: 91 (via symlinks → mr-burger-plugins)
- Total community skill dirs (Cowork): 1259
- Total agents (custom): 16
- Broken symlinks: 0
- Name collisions — custom vs community: **0**
- Within-plugin overlap candidates: **1** (`benchmark-guides` → remove)
- `.fuse_hidden` artifacts: 10 (skills), 183 (commands), 0 (agents)
- Stale items flagged: GWS plugin (orphaned at ~/.agents/skills/), GSD plugin (dead references in settings.local.json), stale memory counts

## Phase 1: Inventory

### Skills (`~/.claude/skills/`)

**Counts:**
| Type | Count |
|------|-------|
| Total entries | 1353 |
| Custom symlinks (→ mr-burger-plugins) | 91 |
| Community skill dirs (installed by Cowork/plugin system) | 1259 |
| Regular files (non-hidden) | 3 |
| Hidden files (.fuse_hidden*, .gitignore) | 11 |
| **Broken symlinks** | **0** |

**Custom skills by plugin (91 total):**
| Plugin | Skills |
|--------|--------|
| ir-teaching | assessment-design, assessment-rubrics, attack-the-passage, bellringer-builder, benchmark-argument, benchmark-central-idea, benchmark-figurative-language, benchmark-guides, benchmark-literary-elements, benchmark-mastery-analyzer, benchmark-poetry, benchmark-point-of-view, benchmark-purpose-perspective, benchmark-rhetoric, benchmark-text-structure, benchmark-theme, benchmarks, brand-identity, cer-writing-guide, collaborative-protocols, cubes-annotation, diagnostic-teacher-scripts, district-files-reader, engagement-protocols, error-analysis-tracker, esol-core, esol-strategies, feedback-checkpoint-builder, feedback-system, file-management, gradual-release-scripts, interactive-lesson-builder, ir-framework, literacy-benchmark-connections, literacy-skills-framework, mc-question-generation, menu-mode-planner, metacognitive-tools, organizer-design, prep-incentive-system, question-stem-analysis, race-strategy, reading-strategies, review-games, self-assessment-tools, session-continuity, skill-index, skill-quality-gate, slide-deck-generation, station-activities, stop-strategy, student-packet-design-guide, teaching-templates, test-prep-unit, test-taking-strategies, unit-builder-protocol, unit-discovery, unit-feedback-protocol, unit-quality-gate, unit-recovery, unit-troubleshooter, vocabulary-instruction *(63)* |
| ir-data-pipeline | class-comparison-generator, data-quality-checker, data-visualization-builder, growth-analyzer, intervention-planner, report-builder, reporting-category-tracker, student-data-processor, student-data-workflow *(9)* |
| ir-classroom-ops | behavior-tracker, observation-prep, parent-contact-log, pd-tracker, sub-folder-builder, unit-distribution *(6)* |
| mr-burger-music | band-materials, band-rehearsal, ear-training, exercise-generator, practice-planner, score-transformer, session-logger *(7)* |
| mr-burger-workflow | area-context, notion-sync, plugin-registry, prompt-scaffold, second-brain-ops, session-state-reader, work-logger *(7)* |

**Unexpected regular files (not symlinks):**
- `README.md` — Cowork/plugin system README, benign
- `workflow_bundles_readme.md` — Cowork artifact, benign
- `workflow- bundlesREADME.md` — Cowork artifact with space in name, benign

**Hidden artifacts:**
- 10x `.fuse_hidden*` files — FUSE filesystem leftovers from a previously mounted Cowork volume. Harmless but messy. Flag for cleanup if desired.
- `.gitignore` — present in `~/.claude/skills/`, indicates this directory may be managed as a git repo by the plugin system.

### Agents (`~/.claude/agents/`)

**Counts:** 16 total | 16 valid symlinks | 0 broken | 0 regular files

| Agent | Plugin | Status |
|-------|--------|--------|
| answer-key-builder | ir-teaching | OK |
| assessment-builder | ir-teaching | OK |
| data-analyst | ir-data-pipeline | OK |
| esol-adapter | ir-teaching | OK |
| interactive-lesson-builder | ir-teaching | OK |
| lesson-plan-coordinator | ir-teaching | OK |
| music-coach | mr-burger-music | OK |
| parent-reporter | ir-data-pipeline | OK |
| quality-reviewer | ir-teaching | OK |
| score-writer | mr-burger-music | OK |
| student-packet-builder | ir-teaching | OK |
| sub-plan-generator | ir-teaching | OK |
| unit-planner | ir-teaching | OK |
| unit-reviewer | ir-teaching | OK |
| unit-reviser | ir-teaching | OK |
| workflow-agent | mr-burger-workflow | OK |

**Note:** `interactive-lesson-builder` exists as both an agent (here) and a skill — flagged for Phase 2 overlap analysis.

### Commands (`~/.claude/commands/`)

**Counts:** 11 active commands (symlinks) | 0 broken | 183 `.fuse_hidden` artifacts | 1 `.DS_Store`

**Active commands — all valid symlinks → mr-burger-workflow:**
| Command | Trigger | Status |
|---------|---------|--------|
| brain-dump.md | `/brain-dump` | OK |
| brainstorm-capture.md | `/brainstorm-capture` | OK |
| capture.md | `/capture` | OK |
| checkpoint.md | `/checkpoint` | OK |
| daily.md | `/daily` | OK |
| plan.md | `/plan` | OK |
| reflect.md | `/reflect` | OK |
| resume.md | `/resume` | OK |
| revise.md | `/revise` | OK |
| skill-update.md | `/skill-update` | OK |
| wrap.md | `/wrap` | OK |

**No duplicate command names found.**

**⚠️ FUSE artifact issue:** 183 `.fuse_hidden*` files present in `~/.claude/commands/`. These are leftovers from a previously mounted FUSE filesystem (Cowork). They do not affect Claude Code behavior but are significant clutter. Flagged for Phase 4 cleanup consideration.

### Hooks (`~/.claude/hooks/`)

**Files:** 4 total (2 `.js` scripts + 2 `.md` description files)

| Hook script | Event | Command | Status |
|-------------|-------|---------|--------|
| `teaching-session-init.js` | SessionStart | `node "$HOME/.claude/hooks/teaching-session-init.js"` | OK — file exists |
| `teaching-skill-router.js` | UserPromptSubmit | `node "$HOME/.claude/hooks/teaching-skill-router.js"` | OK — file exists |

**Additional hooks (inline bash in settings.json — no script file):**
| Event | Purpose | Status |
|-------|---------|--------|
| Stop | Reminds to `/wrap` if HANDOFF.md is stale (>30 min) or missing | OK |
| PreCompact (matcher: auto) | Stamps HANDOFF.md with auto-compact timestamp | OK |

**Community plugin hook conflicts:** None. Checked all `plugin.json` files in `~/.claude/plugins/cache/` — no community plugin registers hooks for SessionStart, UserPromptSubmit, Stop, or PreCompact.

### Plugins Cache (`~/.claude/plugins/`)

**`plugins` setting in settings.json:** `[]` (empty — no plugins formally registered via settings)

**Three skill-loading mechanisms are active simultaneously:**

| Mechanism | Source | Count | How loaded |
|-----------|--------|-------|------------|
| Custom symlinks | `mr-burger-plugins/` via `setup.sh` | 91 skills, 16 agents | `ln -s` into `~/.claude/skills/` and `~/.claude/agents/` |
| Cowork community dirs | Installed by Cowork desktop app | 1259 skill dirs | Actual directories in `~/.claude/skills/` with `SKILL.md` files |
| Plugin cache | `~/.claude/plugins/cache/claude-plugins-official/` | superpowers + others | Accessed directly by Claude Code plugin system |

**Plugin cache inventory:**

| Plugin | Version | Skills | Agents | Commands | Notes |
|--------|---------|--------|--------|----------|-------|
| Notion | 0.1.0 | 0 | 0 | 6 | |
| claude-code-setup | 1.0.0 | 0 | 0 | 0 | |
| claude-md-management | 1.0.0 | 0 | 0 | 1 | |
| commit-commands | 158ef95c | 0 | 0 | 3 | |
| feature-dev | 158ef95c | 0 | 3 | 1 | |
| github | 158ef95c | 0 | 0 | 0 | |
| gitlab | 158ef95c | 0 | 0 | 0 | |
| playwright | 158ef95c | 0 | 0 | 0 | |
| plugin-dev | 158ef95c | 0 | 3 | 1 | |
| skill-creator | 158ef95c | 0 | 3 | 0 | |
| superpowers | 5.0.5 | 14 | — | — | Skills in cache AND as Cowork dirs |
| mr-burger-plugins | 1.0.0 / 3.0.0 | — | — | — | Packaged versions; NOT loaded (plugins: []) |
| claude-hud | — | — | — | — | |

**⚠️ Key architectural finding:** `setup.sh` silently skips creating a custom symlink if a Cowork community directory with the same name already exists (`SKIP [name] — already exists (not a symlink)`). If Cowork installs a community skill with the same name as a custom skill, the custom skill is silently shadowed with no warning.

**⚠️ Superpowers dual-presence:** All 14 superpowers skills exist as both Cowork-installed directories in `~/.claude/skills/` AND in the plugin cache at `~/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.5/skills/`. These are two separate copies — potential version drift if either updates independently.

**`mr-burger-plugins` cache entry:** Versions 1.0.0 and 3.0.0 exist in cache but are NOT loaded (plugins: []). Custom skills load exclusively via symlinks. The packaged versions may be stale relative to current source.

### Settings + Keybindings + CLAUDE.md + Memory

**`~/.claude/settings.json` — paths verified:**
- `statusLine` command: references `claude-hud` plugin path via glob — valid as long as claude-hud cache exists ✓
- `mcpServers.filesystem` paths: `/Users/alexanderburger/Documents`, `/Users/alexanderburger/Desktop`, Google Drive — all expected to exist ✓
- `extraKnownMarketplaces.mr-burger-plugins.path`: `/Users/alexanderburger/Documents/Tech/mr-burger-plugins` — valid ✓
- `enabledPlugins`: 15 plugins enabled — matches what's in cache ✓
- No dead paths found in settings.json

**`~/.claude/settings.local.json` — ⚠️ significant issues:**
- **Massive size** — hundreds of accumulated session-specific permissions, many highly specific bash commands that are one-time actions from past sessions
- **Stale GSD skill permissions:** `Skill(gsd:map-codebase)`, `Skill(gsd:add-phase)`, `Skill(gsd:new-project)` — GSD plugin (`~/.claude/commands/gsd/`) does not exist; these permissions are dead
- **Stale superpowers version reference:** permissions reference superpowers `5.0.2` path (now `5.0.5`)
- **Obsidian vault paths**: multiple `Read` permissions for `iCloud~md~obsidian/Documents/Teaching/Teaching/` paths — vault status unclear (migration in progress per CLAUDE.md)
- **Recommendation:** settings.local.json should be reviewed and stripped of one-time session permissions

**`~/.claude/keybindings.json`:** Not found — not in use.

**`~/.claude/CLAUDE.md`:** Not found — no global instructions file at user level.

**Memory:**
| Location | Files | Notes |
|----------|-------|-------|
| `~/.claude/projects/-Users-alexanderburger/memory/` | 9 files | User-level memory |
| `~/.claude/projects/-Users-alexanderburger-Documents-Tech-mr-burger-plugins/memory/` | 0 files | Project memory empty |
| `~/.claude/projects/-Users-alexanderburger-Desktop-gaby-portfolio/memory/` | 2 files | Gaby portfolio |
| `~/.claude/projects/-Users-alexanderburger-Desktop-ir-platform/memory/` | 0 files | Empty |
| `~/.claude/projects/-Users-alexanderburger-Desktop/memory/` | 0 files | Empty |

**⚠️ Stale memory — `project_mr_burger_plugins.md`:** Lists "69 skills, 14 agents" but current count is 91 skills, 16 agents. Needs update.

**⚠️ Unknown location — GWS plugin:** `~/.agents/skills/` contains 92 Google Workspace skills (gws-admin-reports, gws-calendar, gws-docs, etc.). This path is NOT monitored by Claude Code — these skills are not loaded. Memory notes this as "unwrapped." Status: orphaned at non-standard path.

**⚠️ GSD plugin:** `~/.claude/commands/gsd/` does not exist. `Skill(gsd:*)` permissions in settings.local.json are dead references. The GSD plugin is not installed.

### Project-Level Configs (`~/.claude/projects/`)

5 project directories found. None have a `settings.json` — no project-level settings are overriding user-level config.

| Project dir | Memory files | settings.json | Notes |
|-------------|-------------|--------------|-------|
| `-Users-alexanderburger` | 9 | No | User-scope memory (home dir) |
| `-Users-alexanderburger-Desktop` | 0 | No | Empty |
| `-Users-alexanderburger-Desktop-gaby-portfolio` | 2 | No | Gaby portfolio project |
| `-Users-alexanderburger-Desktop-ir-platform` | 0 | No | IR platform project, no memory |
| `-Users-alexanderburger-Documents-Tech-mr-burger-plugins` | 0 | No | This repo — project memory empty |

**No project-level conflicts found.** No settings.json at any project level — all settings flow from user-level `~/.claude/settings.json` and `settings.local.json` only.

**Note:** `mr-burger-plugins` project has zero memory files — the project memory system uses this repo's own `memory/` directory instead (managed by auto-memory instructions).

## Phase 2: Collision Detection

### Custom vs Community Name Collisions

**Result: ZERO collisions.**

Checked custom skill names (91) against:
- 1259 Cowork community directories in `~/.claude/skills/` — no matches
- 14 superpowers skills in plugin cache — no matches
- All other official plugin skills (plugin-dev, skill-creator, Notion, claude-code-setup, etc.) — no matches

Checked custom agent names (16) against:
- 6 community agents (agent-creator, code-architect, code-explorer, code-reviewer, plugin-validator, skill-reviewer) — no matches

**No Phase 4 collision resolution needed.**

**Note:** 14 superpowers skills appear as both Cowork dirs AND plugin cache entries — community-vs-community duplication, not a custom/community collision. Not actionable for cleanup.

### Within-Plugin Overlap Candidates

| Pair | Overlap? | Recommendation |
|------|----------|----------------|
| `benchmarks` + `benchmark-guides` | Yes — same purpose, `benchmark-guides` is a lower-quality subset | **Remove `benchmark-guides`** |
| `benchmarks` + 11 `benchmark-[topic]` skills | No — complementary routing hub vs. deep-dive content | Keep both |
| `feedback-system` + `feedback-checkpoint-builder` | No — pedagogical framework vs. generator tool | Keep both |
| `unit-quality-gate` + `skill-quality-gate` | No — checks units vs. checks skill files (different domains) | Keep both |
| `unit-recovery` + `unit-troubleshooter` | No — restore from archive vs. diagnose underperformance | Keep both |
| `esol-core` + `esol-strategies` | Partial — daily requirements in both, but intentional primary/supplementary design | Keep both |
| `interactive-lesson-builder` skill + agent | No — skill is implementation, agent is routing wrapper | Keep both |
| `session-logger` (music) + `session-state-reader` (workflow) | No — music logging vs. project state reading | Keep both |

**Details:**

**`benchmark-guides` → REMOVE**
- Same purpose as `benchmarks` (benchmark reference/navigation) but strictly worse
- Contains factual errors: R.1.2 labeled as "Point of View" (it's Theme); R.1.3 description is duplicated
- References dead file paths: `/Users/alexanderburger/Documents/Teaching/Resources/BenchmarkCards/`
- `benchmarks` already covers all routing and quick-reference needs, and links to the correct `standards/` content
- Passes consolidation rule: `benchmark-guides` is a strict subset of `benchmarks` for the same input

**All other pairs: keep as distinct.** None meet the consolidation threshold — either serve different domains, serve different roles in the same workflow, or are intentionally layered (esol-core/esol-strategies).

### Commands / Hooks / Agents Collisions

**Commands:** No active collisions.
- 11 custom commands loaded in `~/.claude/commands/` (all custom symlinks)
- Community plugin commands (from enabled plugins) are loaded separately through the plugin system — not written to `~/.claude/commands/`. They surface as `pluginname:commandname` and do not conflict with unnamespaced custom commands.
- The Notion plugin has a `commands/tasks/plan.md` (subcommand path, not `/plan`) — not a collision with custom `/plan`.

**Hooks:** No conflicts.
- 2 custom hook scripts (SessionStart, UserPromptSubmit) + 2 inline bash hooks (Stop, PreCompact)
- No community plugin registers hooks for any of the same events (verified in Task 6)

**Agents:** No collisions.
- 16 custom agents, 6 community agents — zero name overlap (verified in Task 11)

## Phase 3: Findings Report

### Broken Symlinks

**None.** All 91 custom skill symlinks and 16 agent symlinks are valid. No Phase 4 action needed for symlinks.

### Name Collisions — Custom vs Community

**None.** Zero name conflicts between custom skills/agents and any community plugin skills/agents (Cowork dirs, superpowers cache, or other enabled plugins).

### Within-Plugin Overlap Candidates

| Skill | Plugin | Action | Reason |
|-------|--------|--------|--------|
| `benchmark-guides` | ir-teaching | **Remove** | Lower-quality subset of `benchmarks`; contains factual errors; references dead file paths |

### Settings Issues

| Location | Issue | Action |
|----------|-------|--------|
| `settings.local.json` | 3 dead `Skill(gsd:*)` permissions — GSD plugin not installed | Remove |
| `settings.local.json` | Stale superpowers `5.0.2` path in permissions (now `5.0.5`) | Remove |
| `settings.local.json` | Hundreds of one-time session permissions accumulated over time | Review + prune |
| `settings.local.json` | Obsidian vault `Read` permissions — vault migration status unclear | Leave (low risk) |

### Project-Level Conflicts

**None.** No project-level `settings.json` files found — no shadowing or override conflicts.

### Memory / CLAUDE.md Issues

| Item | Issue | Action |
|------|-------|--------|
| `project_mr_burger_plugins.md` (user memory) | Skill count stale: "69 skills, 14 agents" → actual: 91 skills, 16 agents | Update |
| `~/.claude/CLAUDE.md` | Does not exist | No action needed |
| GWS plugin (`~/.agents/skills/`) | 92 skills at non-standard path, not loaded by Claude Code | Decide: integrate or leave |
| GSD plugin | Dead `Skill(gsd:*)` in settings.local.json, plugin not installed | Remove permissions |

## Phase 4: Cleanup

### Decisions Made

**Approved by user: 2026-03-21**

| Action | What | Result |
|--------|------|--------|
| Remove skill | `ir-teaching/skills/benchmark-guides/` + symlink | Done — lower-quality duplicate of `benchmarks` |
| Clean settings | `settings.local.json` — removed GSD permissions, Obsidian permissions, stale superpowers 5.0.2 refs, one-time session permissions | Done — 160 → 78 allow entries |
| Update memory | `project_mr_burger_plugins.md` — skill counts updated to 91 skills, 16 agents | Done |
| Re-run setup.sh | Verified clean state post-removal | Done — no errors, no skips |

## Phase 5: Evaluation

### Behavioral Eval — Renamed + Consolidated Skills
<!-- populated in Task 22 -->

### Regression Check — Known-Good Workflows
<!-- populated in Task 23 -->
