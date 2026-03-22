# Plugin System Audit — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a verified inventory of everything loaded in `~/.claude/`, identify all name collisions and within-plugin overlaps, and clean up based only on what the audit finds.

**Architecture:** 5 sequential phases — inventory → collision detection → findings report → cleanup → evaluation. No changes made until Phase 3 findings are reviewed and approved. The audit doc (`docs/audits/2026-03-21-plugin-system-audit.md`) is built incrementally throughout and committed at phase boundaries.

**Tech Stack:** Bash (`find`, `ls -la`, `readlink`, `file`), manual skill file inspection, `./scripts/setup.sh` for final verification.

---

## Files

| Action | Path | Purpose |
|--------|------|---------|
| Create | `docs/audits/2026-03-21-plugin-system-audit.md` | Living audit doc — built up across all phases |
| Modify | `~/.claude/CLAUDE.md` | Update if stale paths or conflicting rules found |
| Modify | `~/.claude/settings.json` | Remove dead paths if found |
| Modify | `~/.claude/settings.local.json` | Remove dead paths if found |
| Modify | Skill files in `mr-burger-plugins/` | Renames or removals from collision resolution |
| Modify | `PROJECT.md` | Mark audit complete |
| Modify | `HANDOFF.md` | Update at phase boundaries |

---

## Task 1: Commit the Spec

**Files:**
- Already exists: `docs/superpowers/specs/2026-03-21-plugin-system-audit-design.md`

- [ ] **Step 1: Stage and commit the spec**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/superpowers/specs/2026-03-21-plugin-system-audit-design.md
git status
```

Expected: spec file staged, nothing else unintentionally staged.

- [ ] **Step 2: Commit**

```bash
git commit -m "docs: add plugin system audit design spec"
```

Expected: commit succeeds on `main`.

---

## Task 2: Create Audit Doc Scaffold

**Files:**
- Create: `docs/audits/2026-03-21-plugin-system-audit.md`

- [ ] **Step 1: Create the scaffold**

Create `docs/audits/2026-03-21-plugin-system-audit.md` with this content:

```markdown
# Plugin System Audit
*Date: 2026-03-21 | Status: In Progress*

## Summary
- Total skills (custom): TBD
- Total agents (custom): TBD
- Broken symlinks: TBD
- Name collisions — skills + agents (custom vs community): TBD
- Within-plugin overlap candidates: TBD

## Phase 1: Inventory

### Skills (`~/.claude/skills/`)
<!-- populated in Task 3 -->

### Agents (`~/.claude/agents/`)
<!-- populated in Task 4 -->

### Commands (`~/.claude/commands/`)
<!-- populated in Task 5 -->

### Hooks (`~/.claude/hooks/`)
<!-- populated in Task 6 -->

### Plugins Cache (`~/.claude/plugins/`)
<!-- populated in Task 7 -->

### Settings + Keybindings + CLAUDE.md + Memory
<!-- populated in Task 8 -->

### Project-Level Configs (`~/.claude/projects/`)
<!-- populated in Task 9 -->

## Phase 2: Collision Detection

### Custom vs Community Name Collisions
<!-- populated in Task 11 -->

### Within-Plugin Overlap Candidates
<!-- populated in Task 12 -->

### Commands / Hooks / Agents Collisions
<!-- populated in Task 13 -->

## Phase 3: Findings Report

### Broken Symlinks
<!-- populated in Task 15 -->

### Name Collisions — Custom vs Community
<!-- populated in Task 15 -->

### Within-Plugin Overlap Candidates
<!-- populated in Task 15 -->

### Settings Issues
<!-- populated in Task 15 -->

### Project-Level Conflicts
<!-- populated in Task 15 -->

### Memory / CLAUDE.md Issues
<!-- populated in Task 15 -->

## Phase 4: Cleanup

### Decisions Made
<!-- populated in Task 17+ -->
```

- [ ] **Step 2: Commit scaffold**

```bash
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: add plugin system audit doc scaffold"
```

---

## Task 3: Phase 1 — Inventory `~/.claude/skills/`

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (skills section)

1353 entries in `~/.claude/skills/` — the majority are symlinks managed by `setup.sh`. Goal: confirm all are valid symlinks with correct targets, find any broken ones, and spot any unexpected regular files (which would mean something was manually placed there).

- [ ] **Step 1: Count entry types**

```bash
total=$(ls ~/.claude/skills/ | wc -l)
valid_symlinks=$(find ~/.claude/skills/ -maxdepth 1 -type l | wc -l)
broken_symlinks=$(find ~/.claude/skills/ -maxdepth 1 -xtype l | wc -l)
regular_files=$(find ~/.claude/skills/ -maxdepth 1 -type f | wc -l)
dirs=$(find ~/.claude/skills/ -maxdepth 1 -type d | wc -l)
echo "Total: $total | Valid symlinks: $valid_symlinks | Broken: $broken_symlinks | Regular files: $regular_files | Dirs: $dirs"
```

Expected: total ≈ 1353, nearly all valid symlinks, broken = 0 ideally.

- [ ] **Step 2: List any broken symlinks**

```bash
find ~/.claude/skills/ -maxdepth 1 -xtype l -print
```

Expected: empty output if setup.sh is clean. If any appear, record them — target no longer exists.

- [ ] **Step 3: List any unexpected regular files**

```bash
find ~/.claude/skills/ -maxdepth 1 -type f -print
```

Expected: empty — all entries should be symlinks, not plain files.

- [ ] **Step 4: Sample-verify symlink targets**

Spot-check that custom skill symlinks point into `mr-burger-plugins/`:

```bash
# Check a few known custom skills
readlink ~/.claude/skills/unit-builder-protocol 2>/dev/null
readlink ~/.claude/skills/menu-mode-planner 2>/dev/null
readlink ~/.claude/skills/benchmark-theme 2>/dev/null
```

Expected: paths resolve to `~/Documents/Tech/mr-burger-plugins/[plugin]/skills/[name]/skill.md` (or similar).

- [ ] **Step 5: Identify which skills are community vs custom**

```bash
# Community skills symlink into plugins/cache; custom skills symlink into mr-burger-plugins
community=$(find ~/.claude/skills/ -maxdepth 1 -type l | xargs -I {} readlink {} | grep "plugins/cache" | wc -l)
custom=$(find ~/.claude/skills/ -maxdepth 1 -type l | xargs -I {} readlink {} | grep "mr-burger-plugins" | wc -l)
other=$(find ~/.claude/skills/ -maxdepth 1 -type l | xargs -I {} readlink {} | grep -v "plugins/cache" | grep -v "mr-burger-plugins" | wc -l)
echo "Community: $community | Custom: $custom | Other: $other"
```

- [ ] **Step 6: Record findings in audit doc**

Update the `### Skills` section with actual counts, any broken symlinks found, and the community/custom breakdown.

---

## Task 4: Phase 1 — Inventory `~/.claude/agents/`

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (agents section)

16 entries total.

- [ ] **Step 1: List all agents with their targets**

```bash
find ~/.claude/agents/ -maxdepth 1 \( -type l -o -type f \) | sort | while read entry; do
  if [ -L "$entry" ]; then
    target=$(readlink "$entry")
    if [ -e "$entry" ]; then
      echo "OK   $(basename $entry) -> $target"
    else
      echo "BROKEN $(basename $entry) -> $target"
    fi
  else
    echo "FILE $(basename $entry)"
  fi
done
```

Expected: 16 entries, all valid symlinks, all pointing into `mr-burger-plugins/`.

- [ ] **Step 2: Record findings in audit doc**

Update `### Agents` section with the full list.

---

## Task 5: Phase 1 — Inventory `~/.claude/commands/`

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (commands section)

11 entries. Commands are `.md` files that act as slash command triggers.

- [ ] **Step 1: List all commands with targets**

```bash
find ~/.claude/commands/ -maxdepth 1 \( -type l -o -type f \) | sort | while read entry; do
  if [ -L "$entry" ]; then
    target=$(readlink "$entry")
    if [ -e "$entry" ]; then
      echo "OK   $(basename $entry) -> $target"
    else
      echo "BROKEN $(basename $entry) -> $target"
    fi
  else
    echo "FILE $(basename $entry)"
  fi
done
```

- [ ] **Step 2: Check for name conflicts between commands**

List command names (without `.md`) and check for duplicates:

```bash
find ~/.claude/commands/ -maxdepth 1 -name "*.md" | sed 's|.*/||' | sed 's|\.md||' | sort | uniq -d
```

Expected: empty (no duplicates).

- [ ] **Step 3: Record findings in audit doc**

---

## Task 6: Phase 1 — Inventory `~/.claude/hooks/`

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (hooks section)

4 files found: `teaching-session-init.js`, `teaching-session-init.js.md`, `teaching-skill-router.js`, `teaching-skill-router.js.md`. The `.md` files are descriptions; the `.js` files are the actual hook scripts.

- [ ] **Step 1: Identify hook events from settings.json**

```bash
cat ~/.claude/settings.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d.get('hooks', {}), indent=2))"
```

This shows which events trigger which scripts.

- [ ] **Step 2: Verify hook scripts are valid (not broken paths)**

```bash
# Check the hooks referenced in settings.json actually exist
# Replace paths below with actual hook paths found in step 1
ls -la ~/.claude/hooks/teaching-session-init.js
ls -la ~/.claude/hooks/teaching-skill-router.js
```

- [ ] **Step 3: Check if any community plugin also registers hooks for the same events**

```bash
# Look for hooks config in community plugin manifests
find ~/.claude/plugins/cache/ -name "settings.json" -o -name "plugin.json" 2>/dev/null | xargs grep -l "hooks" 2>/dev/null
```

- [ ] **Step 4: Record findings in audit doc**

Document: hook name, event, script path, status (valid/broken), and any event conflicts with community plugins.

---

## Task 7: Phase 1 — Inventory `~/.claude/plugins/`

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (plugins section)

3 plugin sources found in cache: `claude-hud`, `claude-plugins-official`, `mr-burger-plugins`.

- [ ] **Step 1: List all registered plugins**

```bash
cat ~/.claude/settings.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d.get('plugins', []), indent=2))"
```

Shows which plugins are officially registered (vs just present in cache).

- [ ] **Step 2: Inventory claude-plugins-official**

```bash
ls ~/.claude/plugins/cache/claude-plugins-official/
```

For each plugin in that directory:

```bash
find ~/.claude/plugins/cache/claude-plugins-official/ -mindepth 1 -maxdepth 1 -type d | while read plugin; do
  name=$(basename $plugin)
  version=$(ls $plugin/ | head -1)
  skill_count=$(find $plugin/$version/skills/ -type d -mindepth 1 -maxdepth 1 2>/dev/null | wc -l)
  agent_count=$(find $plugin/$version/agents/ -name "*.md" 2>/dev/null | wc -l)
  echo "$name ($version): $skill_count skills, $agent_count agents"
done
```

- [ ] **Step 3: Inventory claude-hud**

```bash
ls ~/.claude/plugins/cache/claude-hud/
find ~/.claude/plugins/cache/claude-hud/ -name "*.md" | head -20
```

- [ ] **Step 4: Inventory mr-burger-plugins cache entry**

```bash
ls ~/.claude/plugins/cache/mr-burger-plugins/ 2>/dev/null
```

Note: custom plugins loaded via symlinks should not have a cache entry — if they do, investigate whether it's redundant.

- [ ] **Step 5: Record findings in audit doc**

Document: each plugin source, version, skill count, agent count, and whether it's registered vs orphaned in cache.

---

## Task 8: Phase 1 — Inventory Settings, Keybindings, CLAUDE.md, Memory

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (settings section)

- [ ] **Step 1: Check settings.json for dead paths**

```bash
cat ~/.claude/settings.json
```

For any file path values found (hooks, includes, etc.), verify each path exists:

```bash
# Example — replace with actual paths found
ls -la <path-from-settings>
```

- [ ] **Step 2: Check settings.local.json**

```bash
cat ~/.claude/settings.local.json 2>/dev/null || echo "not found"
```

Same path verification.

- [ ] **Step 3: Check keybindings.json**

```bash
cat ~/.claude/keybindings.json 2>/dev/null || echo "not found"
```

Look for bindings that reference commands no longer present in `~/.claude/commands/`.

- [ ] **Step 4: Check ~/.claude/CLAUDE.md**

```bash
cat ~/.claude/CLAUDE.md
```

Look for: file paths that no longer exist, plugin references that are outdated, instructions that conflict with `~/CLAUDE.md`.

- [ ] **Step 5: Spot-check memory files**

```bash
ls ~/.claude/memory/ 2>/dev/null | head -20
# Check project-specific memory if it exists for mr-burger-plugins
ls /Users/alexanderburger/.claude/projects/-Users-alexanderburger-Documents-Tech-mr-burger-plugins/memory/ 2>/dev/null
```

Read the MEMORY.md index and flag any memory files that reference paths or system state that has changed:

```bash
cat /Users/alexanderburger/.claude/projects/-Users-alexanderburger-Documents-Tech-mr-burger-plugins/memory/MEMORY.md 2>/dev/null
```

- [ ] **Step 6: Record findings in audit doc**

---

## Task 9: Phase 1 — Inventory Project-Level Configs

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (project-level section)

- [ ] **Step 1: List project-level claude configs**

```bash
ls ~/.claude/projects/ 2>/dev/null
```

- [ ] **Step 2: Check for project-level settings that shadow user-level**

For each project folder:

```bash
find ~/.claude/projects/ -name "settings.json" -o -name "settings.local.json" 2>/dev/null
```

Read any found and note if they override hooks, permissions, or other user-level settings in a way that could cause unexpected behavior.

- [ ] **Step 3: Record findings in audit doc**

---

## Task 10: Commit Phase 1 Inventory

- [ ] **Step 1: Update Summary section of audit doc**

Fill in the actual counts at the top of the audit doc:
- Total skills (custom): [from Task 3]
- Total agents (custom): [from Task 4]
- Broken symlinks: [from Tasks 3–5]

- [ ] **Step 2: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: add Phase 1 inventory to plugin system audit"
```

---

## Task 11: Phase 2 — Custom vs Community Name Collision Detection

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (collision section)

- [ ] **Step 1: Extract all community skill names**

```bash
find ~/.claude/plugins/cache/claude-plugins-official/ -path "*/skills/*/skill.md" -type f \
  | sed 's|.*/skills/||' | sed 's|/skill.md||' | sort > /tmp/community-skills.txt
wc -l /tmp/community-skills.txt
```

- [ ] **Step 2: Extract all community agent names**

```bash
find ~/.claude/plugins/cache/claude-plugins-official/ -path "*/agents/*.md" -type f \
  | sed 's|.*/agents/||' | sed 's|\.md||' | sort > /tmp/community-agents.txt
wc -l /tmp/community-agents.txt
```

- [ ] **Step 3: Extract all custom skill names from mr-burger-plugins**

```bash
find ~/Documents/Tech/mr-burger-plugins/ -path "*/skills/*/skill.md" -type f \
  | sed 's|.*/skills/||' | sed 's|/skill.md||' | sort > /tmp/custom-skills.txt
wc -l /tmp/custom-skills.txt
```

- [ ] **Step 4: Extract all custom agent names**

```bash
find ~/Documents/Tech/mr-burger-plugins/ -path "*/agents/*.md" -type f \
  | sed 's|.*/agents/||' | sed 's|\.md||' | sort > /tmp/custom-agents.txt
wc -l /tmp/custom-agents.txt
```

- [ ] **Step 5: Find skill name collisions**

```bash
comm -12 /tmp/community-skills.txt /tmp/custom-skills.txt
```

Expected: lists exact name matches. For each collision, note the custom plugin source and the community plugin source.

- [ ] **Step 6: Find agent name collisions**

```bash
comm -12 /tmp/community-agents.txt /tmp/custom-agents.txt
```

- [ ] **Step 7: For each collision, classify using the tiebreaker rule**

For each colliding name, determine:
- Is the custom skill "actively used"? (check: referenced in `~/CLAUDE.md`, a hook, a command, a cheat sheet, or `PROJECT.md`)
- Is it purely duplicating community functionality, or customized?

Apply tiebreaker:
- Actively used + customized → **namespace prefix** (e.g., `ir-interactive-lesson-builder`)
- Pure duplicate of community → **remove custom**
- Community name is clearly canonical, custom is the divergent one → **rename**

Record decision for each collision.

- [ ] **Step 8: Record all collisions and decisions in audit doc**

---

## Task 12: Phase 2 — Within-Plugin Overlap Analysis

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (overlap section)

These are the known candidates from the spec. For each pair:
1. Read both skill files
2. Apply consolidation rule: consolidate if >50% behavioral instructions overlap verbatim, or one is a strict subset of the other for the same input
3. Record recommendation

- [ ] **Step 1: `benchmarks` + `benchmark-guides` + individual `benchmark-[topic]` skills**

```bash
# Read the parent skills
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/benchmarks/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/benchmark-guides/skill.md
# Spot-check one specific benchmark skill
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/benchmark-theme/skill.md
```

Determine: do `benchmarks` and `benchmark-guides` overlap? Do individual `benchmark-[topic]` skills duplicate content from `benchmarks` or `benchmark-guides`?

- [ ] **Step 2: `feedback-system` + `feedback-checkpoint-builder`**

```bash
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/feedback-system/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/feedback-checkpoint-builder/skill.md
```

- [ ] **Step 3: `unit-quality-gate` + `skill-quality-gate`**

```bash
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/unit-quality-gate/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/skill-quality-gate/skill.md
```

- [ ] **Step 4: `unit-recovery` + `unit-troubleshooter`**

```bash
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/unit-recovery/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/unit-troubleshooter/skill.md
```

- [ ] **Step 5: `esol-core` + `esol-strategies`**

```bash
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/esol-core/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/esol-strategies/skill.md
```

- [ ] **Step 6: `interactive-lesson-builder` — skill vs agent**

```bash
# Does a skill AND an agent exist with this name?
ls ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/interactive-lesson-builder/
ls ~/Documents/Tech/mr-burger-plugins/ir-teaching/agents/interactive-lesson-builder.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/interactive-lesson-builder/skill.md
cat ~/Documents/Tech/mr-burger-plugins/ir-teaching/agents/interactive-lesson-builder.md
```

Determine if the skill and agent serve different purposes or if the skill is stale.

- [ ] **Step 7: `session-logger` (mr-burger-music) vs session skills in mr-burger-workflow**

```bash
cat ~/Documents/Tech/mr-burger-plugins/mr-burger-music/skills/session-logger/skill.md 2>/dev/null
# Find session-related skills in mr-burger-workflow
find ~/Documents/Tech/mr-burger-plugins/mr-burger-workflow/ -name "*.md" | xargs grep -l "session" 2>/dev/null
```

- [ ] **Step 8: Record all overlap findings and recommendations in audit doc**

---

## Task 13: Phase 2 — Commands and Hooks Collision Check

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (commands/hooks collision section)

- [ ] **Step 1: List all mr-burger-workflow command triggers**

```bash
find ~/Documents/Tech/mr-burger-plugins/mr-burger-workflow/commands/ -name "*.md" 2>/dev/null | sed 's|.*/||' | sed 's|\.md||'
ls ~/.claude/commands/ | sed 's|\.md||'
```

- [ ] **Step 2: Check for same-name commands from community plugins**

```bash
find ~/.claude/plugins/cache/claude-plugins-official/ -path "*/commands/*.md" 2>/dev/null | sed 's|.*/||' | sed 's|\.md||' | sort
```

Cross-reference against custom command names.

- [ ] **Step 3: Check hook event conflicts (community vs custom)**

From Task 6 Step 3 results — are any hook events (SessionStart, UserPromptSubmit) registered by both a custom hook AND a community plugin? If so, both fire, which may cause unexpected behavior.

- [ ] **Step 4: Record findings**

---

## Task 14: Commit Phase 2 Findings

- [ ] **Step 1: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: add Phase 2 collision detection findings to audit"
```

---

## Task 15: Phase 3 — Finalize Findings Report + Human Review Gate

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (Phase 3 section)

- [ ] **Step 1: Consolidate all findings into the Phase 3 report sections**

Transfer and organize findings from Phase 1 and 2 into the structured report format:
- Broken Symlinks (with path and dead target)
- Name Collisions — Custom vs Community (skill name | custom source | community source | decision)
- Within-Plugin Overlap Candidates (skill A | skill B | overlap assessment | recommendation)
- Settings Issues (dead paths in settings.json/keybindings.json)
- Project-Level Conflicts (any shadowing found)
- Memory / CLAUDE.md Issues (stale references)

- [ ] **Step 2: Update the Summary section counts**

Fill in final numbers at the top of the audit doc.

- [ ] **Step 3: Commit the findings report**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: add Phase 3 findings report to plugin system audit"
```

- [ ] **Step 4: HUMAN REVIEW GATE — present destructive changes for approval**

Present to the user:
- All planned removals (which skills/agents will be deleted)
- All planned renames (old name → new name)
- All planned consolidations (which skill absorbs which)

**Do not proceed to Phase 4 until the user explicitly approves.**

Record their approval in the audit doc under `## Phase 4: Cleanup > ### Decisions Made`.

---

## Task 16: Phase 4 — Fix Broken Symlinks

*(Only proceed after human approval from Task 15 Step 4)*

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (decisions made)

- [ ] **Step 1: Remove or re-point each broken symlink**

For each broken symlink found in Phase 1:
```bash
# If the target no longer exists and skill is defunct:
rm ~/.claude/skills/<broken-skill-name>
# If the target moved, re-run setup.sh (see Task 20)
```

- [ ] **Step 2: Record each action in audit doc under "Decisions Made"**

- [ ] **Step 3: Commit**

```bash
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "fix: remove broken symlinks from plugin system cleanup"
```

---

## Task 17: Phase 4 — Resolve Name Collisions

**Files:**
- Modify: skill files and directories in `mr-burger-plugins/` as needed

- [ ] **Step 1: Execute each collision decision from Task 11 Step 7**

For namespace prefix (rename):
```bash
# Example: rename skill directory in source
mv ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/interactive-lesson-builder \
   ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/ir-interactive-lesson-builder
# Update any references in CLAUDE.md, hooks, cheat sheets
```

For removal (pure duplicate):
```bash
rm -rf ~/Documents/Tech/mr-burger-plugins/[plugin]/skills/[skill-name]
```

- [ ] **Step 2: Re-run setup.sh to update symlinks**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

- [ ] **Step 3: Verify renamed/removed skills no longer appear with old names**

```bash
ls ~/.claude/skills/ | grep "interactive-lesson-builder"  # should show new name only
```

- [ ] **Step 4: Record each action in audit doc**

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "fix: resolve plugin name collisions — renames and removals"
```

---

## Task 18: Phase 4 — Consolidate Within-Plugin Overlaps

**Files:**
- Modify: skill files in `mr-burger-plugins/` as needed

For each overlap pair where consolidation was recommended in Task 12:

- [ ] **Step 1: Execute consolidation**

Typically: keep the more comprehensive skill, delete the redundant one, update any references.

- [ ] **Step 2: Re-run setup.sh**

```bash
./scripts/setup.sh
```

- [ ] **Step 3: Verify in Claude Code that the kept skill loads correctly**

Check that the remaining skill's description is accurate for the merged scope.

- [ ] **Step 4: Record in audit doc**

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "fix: consolidate within-plugin skill overlaps"
```

---

## Task 19: Phase 4 — Clean Settings, CLAUDE.md, Memory

**Files:**
- Modify: `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, memory files as needed

- [ ] **Step 1: Remove dead paths from settings.json and settings.local.json**

Edit the files directly, removing any hook paths or include paths that no longer resolve.

- [ ] **Step 2: Update `~/.claude/CLAUDE.md`**

Remove stale content, dead paths, or instructions that conflict with current `~/CLAUDE.md`.

- [ ] **Step 3: Update or remove stale memory files**

For each memory file flagged in Task 8 Step 5, either update the content or delete the file and remove the pointer from MEMORY.md.

- [ ] **Step 4: Record actions in audit doc**

- [ ] **Step 5: Commit audit doc changes**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "fix: clean stale settings and memory references"
```

---

## Task 20: Phase 4 — Final Verification Pass

**Files:**
- No new changes — verification only

- [ ] **Step 1: Re-run setup.sh for clean state**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

Expected: no errors, no orphaned symlinks reported.

- [ ] **Step 2: Re-inventory for zero broken symlinks**

```bash
find ~/.claude/skills/ -maxdepth 1 -xtype l -print
find ~/.claude/agents/ -maxdepth 1 -xtype l -print
find ~/.claude/commands/ -maxdepth 1 -xtype l -print
```

Expected: empty output across all three.

- [ ] **Step 3: Verify no remaining name collisions**

```bash
find ~/.claude/plugins/cache/claude-plugins-official/ -path "*/skills/*/skill.md" -type f \
  | sed 's|.*/skills/||' | sed 's|/skill.md||' | sort > /tmp/community-skills-final.txt
find ~/Documents/Tech/mr-burger-plugins/ -path "*/skills/*/skill.md" -type f \
  | sed 's|.*/skills/||' | sed 's|/skill.md||' | sort > /tmp/custom-skills-final.txt
comm -12 /tmp/community-skills-final.txt /tmp/custom-skills-final.txt
```

Expected: empty (all collisions resolved).

- [ ] **Step 4: Verify settings paths resolve**

Re-read settings.json and confirm every path referenced exists.

- [ ] **Step 5: Record verification results in audit doc — mark Status: Complete**

---

## Task 21: Final Commit + Update PROJECT.md

- [ ] **Step 1: Final commit of audit doc**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: mark plugin system audit complete"
```

- [ ] **Step 2: Update PROJECT.md**

Change phase to `complete — plugin system audit done` and update the Implementation section accordingly.

- [ ] **Step 3: Commit PROJECT.md**

```bash
git add PROJECT.md
git commit -m "docs: update PROJECT.md — plugin system audit complete"
```

---

---

## Task 22: Phase 5 — Behavioral Eval (Renamed + Consolidated Skills)

**Goal:** Confirm that every skill renamed or consolidated in Phase 4 still triggers correctly and produces expected output.

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (eval results section)

This task is only meaningful if Phase 4 produced renames or consolidations. If Phase 4 made no changes, skip to Task 23.

- [ ] **Step 1: Build the eval list**

From the audit doc's "Decisions Made" section, extract every skill that was:
- Renamed (old name → new name)
- Consolidated (skill A absorbed into skill B)

Create a table:

| Skill | Change | Trigger to test | Expected behavior |
|-------|--------|-----------------|-------------------|
| `interactive-lesson-builder` | renamed to `ir-interactive-lesson-builder` | invoke by new name | loads skill, produces HTML lesson output |
| ... | ... | ... | ... |

- [ ] **Step 2: Test each renamed skill — trigger check**

For each renamed skill, verify the new name resolves in `~/.claude/skills/`:

```bash
ls -la ~/.claude/skills/<new-name>
readlink ~/.claude/skills/<new-name>
```

Expected: symlink exists and points to the correct source file in `mr-burger-plugins/`.

- [ ] **Step 3: Test each renamed skill — behavioral check**

For each renamed skill, invoke it with a minimal representative prompt and verify:
- The skill loads (no "skill not found" error)
- The output matches the skill's documented purpose (spot-check, not full eval)

Document: skill name | prompt used | output summary | pass/fail

- [ ] **Step 4: Test each consolidated skill — coverage check**

For each consolidation (skill A absorbed into B), verify that skill B's content covers both original use cases:

Read the kept skill file and confirm:
- The trigger descriptions cover both former skills' use cases
- No behavioral instructions were dropped that were unique to the removed skill

```bash
cat ~/Documents/Tech/mr-burger-plugins/<plugin>/skills/<kept-skill>/skill.md
```

- [ ] **Step 5: Record eval results in audit doc**

Add a `## Phase 5: Evaluation` section to the audit doc with:
- Eval table (from Step 1)
- Pass/fail per skill
- Any issues found

- [ ] **Step 6: Fix any failures before proceeding**

If a renamed or consolidated skill fails behavioral check:
- Diagnose: is the symlink wrong, is the skill file missing content, or is the trigger not matching?
- Fix the root cause (re-run `setup.sh`, update skill content, etc.)
- Re-test until passing

---

## Task 23: Phase 5 — Regression Check (Known-Good Workflows)

**Goal:** Verify that the 3 most critical end-to-end workflows still work correctly after all Phase 4 changes.

**Files:**
- Modify: `docs/audits/2026-03-21-plugin-system-audit.md` (regression results section)

**Workflows to test:**

| Workflow | Entry point | What "working" looks like |
|----------|-------------|---------------------------|
| IR unit build | `menu-mode-planner` → `unit-builder-protocol` | menu-mode-planner loads and presents the planner menu; unit-builder-protocol triggers on demand |
| Student data pipeline | `student-data-processor` → `data-quality-checker` → `growth-analyzer` | each skill loads; skill descriptions are accurate and non-overlapping |
| IR teaching core | `benchmark-theme`, `unit-builder-protocol`, `stop-strategy`, `race-strategy` | all load by name; no name collision with community skills |

- [ ] **Step 1: Verify entry-point skills exist and resolve**

```bash
for skill in menu-mode-planner unit-builder-protocol student-data-processor data-quality-checker growth-analyzer benchmark-theme stop-strategy race-strategy; do
  target=$(readlink ~/.claude/skills/$skill 2>/dev/null)
  if [ -n "$target" ] && [ -e "$target" ]; then
    echo "OK   $skill -> $target"
  elif [ -d ~/.claude/skills/$skill ]; then
    echo "DIR  $skill (community install)"
  else
    echo "MISSING $skill"
  fi
done
```

Expected: all 8 show `OK` or `DIR` — none show `MISSING`.

- [ ] **Step 2: Spot-invoke each workflow entry point**

For each entry-point skill, invoke it with a minimal prompt in a fresh Claude Code session and confirm:
- Skill loads without error
- Output is coherent and matches the skill's purpose
- No unintended community skill of the same name fires instead

Document: skill | invoked | response coherent | correct skill fired (custom vs community) | pass/fail

- [ ] **Step 3: Cross-check the IR unit build chain**

Specifically confirm that `menu-mode-planner` and `unit-builder-protocol` chain correctly — `menu-mode-planner` should refer the user to `unit-builder-protocol` as part of its flow.

```bash
grep -i "unit-builder-protocol" ~/Documents/Tech/mr-burger-plugins/ir-teaching/skills/menu-mode-planner/skill.md
```

Expected: reference exists confirming the chain is intact.

- [ ] **Step 4: Record regression results in audit doc**

Add to the `## Phase 5: Evaluation` section:
- Regression table with pass/fail per workflow
- Any issues found and resolved

- [ ] **Step 5: Fix any regressions before marking audit complete**

If a workflow is broken:
- Check if a Phase 4 rename or removal is the cause
- Re-run `setup.sh` if symlinks are stale
- Fix the root cause — do not mark the audit complete until all 3 workflows pass

---

## Task 24: Final Commit + Mark Audit Complete

- [ ] **Step 1: Commit eval results to audit doc**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add docs/audits/2026-03-21-plugin-system-audit.md
git commit -m "docs: add Phase 5 eval and regression results — audit complete"
```

- [ ] **Step 2: Update audit doc Status to Complete**

Change the header line from `Status: In Progress` to `Status: Complete`.

- [ ] **Step 3: Update PROJECT.md**

Change phase to `complete — plugin system audit + eval done`.

- [ ] **Step 4: Final commit**

```bash
git add docs/audits/2026-03-21-plugin-system-audit.md PROJECT.md
git commit -m "docs: mark plugin system audit complete"
```

---

*Plan written: 2026-03-21 | Spec: `docs/superpowers/specs/2026-03-21-plugin-system-audit-design.md`*
