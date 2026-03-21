# Workflow Upgrades Implementation Plan
*Created: 2026-03-21*

**Goal:** Resolve gaps identified in the mr-burger-workflow review — orphaned files, command overlap, missing commands, broken invocation paths, dormant skills.

**Spec:** See TASKS.md [Workflow] items for full list.

---

## Execution Order

Tasks are ordered by impact + dependency. Do quick wins first.

---

## Task 1: Delete capture 2.md

**Files:**
- Delete: `mr-burger-workflow/commands/capture 2.md`
- Delete: `~/.claude/commands/capture 2.md` (symlink)

- [ ] **Step 1: Remove the file**
```bash
rm "mr-burger-workflow/commands/capture 2.md"
rm ~/.claude/commands/"capture 2.md" 2>/dev/null
```

- [ ] **Step 2: Verify gone**
```bash
ls ~/.claude/commands/ | grep capture
```
Expected: only `capture.md`

- [ ] **Step 3: Commit**
```bash
git add -A
git commit -m "chore(workflow): remove orphaned capture 2.md command"
git push
```

---

## Task 2: Clarify /wrap vs /checkpoint

**Problem:** Both commands do HANDOFF + TASKS + memory. Unclear when to use which.

**Decision to make before writing:**
- Option A: Merge — `/wrap` absorbs `/checkpoint`, delete `/checkpoint`
- Option B: Differentiate clearly — `/wrap` = lean session end (HANDOFF + TASKS); `/checkpoint` = deep save (adds CLAUDE.md + skills + knowledge + memory)
- Recommendation: **Option B** — they serve different moments. `/wrap` is fast and frequent; `/checkpoint` is thorough and less frequent.

- [ ] **Step 1: Update /wrap description** — add "for quick session end; use /checkpoint for full deep save"
- [ ] **Step 2: Update /checkpoint description** — add "for end of significant work blocks; includes CLAUDE.md + skill + knowledge review"
- [ ] **Step 3: Add guidance to cheat sheet** — when to use each
- [ ] **Step 4: Commit**

---

## Task 3: Fix /resume — auto-find plan step

**Files:**
- Modify: `mr-burger-workflow/commands/resume.md`

**Change:** In step 3 (Read plan file), add explicit instruction to find the first unchecked `- [ ]` line and surface it as the exact next action.

- [ ] **Step 1: Edit resume.md**

Replace current step 3:
```markdown
3. **Read plan file** (if session state has a plan_file path):
   - Read it, find the current step (first unchecked `- [ ]`)
```

With:
```markdown
3. **Read plan file** (if session state has a plan_file path):
   - Read it
   - Find the first unchecked `- [ ]` line — that is the exact next action
   - If all checked: note "plan complete" and surface next project from PROJECT.md
```

- [ ] **Step 2: Commit**

---

## Task 4: Add /reflect + /skill-update prompts to /wrap

**Files:**
- Modify: `mr-burger-workflow/commands/wrap.md`

**Change:** After the brainstorm check (step 5), add prompts for /reflect and /skill-update before the confirm step.

- [ ] **Step 1: Add to wrap.md after brainstorm check**

```markdown
6. **Knowledge check** — did anything shift about *how you approach* something this session?
   If yes: "Run /reflect before /clear to update your knowledge files?"
   Flag only — don't auto-run.

7. **Skill friction check** — did any skill have gaps or cause repeated corrections?
   If yes: "Run /skill-update [skill-name] before /clear?"
   Flag only — don't auto-run.
```

- [ ] **Step 2: Renumber confirm step to 8**
- [ ] **Step 3: Commit**

---

## Task 5: Create /plan command

**Files:**
- Create: `mr-burger-workflow/commands/plan.md`

**What it does:** Scaffolds a new PLAN.md (or dated plan file) for the active project. Reads PROJECT.md to know the project name and docs/plans/ path. Uses the standard plan format.

- [ ] **Step 1: Create plan.md**

```markdown
---
description: Scaffold a new plan file for the active project — creates docs/plans/YYYY-MM-DD-[topic].md with standard structure
allowed-tools: Read, Write, Bash, Glob
---

# /plan

Create a new implementation plan for the current project. Call this before starting a new phase of work.

## What to do

1. **Call session-state-reader** — get project name and current phase

2. **Ask if not provided:** "What are we planning?" (topic/feature name)

3. **Check for existing plan**
```bash
ls docs/plans/ 2>/dev/null | tail -5
```
If a recent plan exists for the same topic, ask if continuing or creating new.

4. **Scaffold the plan file** at `docs/plans/YYYY-MM-DD-[topic].md`:

Use this structure:
- Goal (1-2 sentences)
- File Map (what files are created/modified)
- Tasks (numbered, each with Steps as - [ ] checkboxes)
- Execution Order

5. **Update PROJECT.md** — set Plan.File to the new path, set Plan.Current step to Task 1.

6. **Confirm** — tell user the file path and that they can now use /resume to orient to it.

## Notes
- Plan files go in `docs/plans/` relative to the project root
- If no docs/plans/ directory exists, create it
- Filename: YYYY-MM-DD-[short-topic-slug].md
- Always include an Execution Order section — tasks have dependencies
```

- [ ] **Step 2: Run setup.sh to symlink**
- [ ] **Step 3: Commit**

---

## Task 6: Fix /brain-dump skill invocation

**Files:**
- Modify: `mr-burger-workflow/commands/brain-dump.md`

**Problem:** The routing table says "route to benchmark skill" but there's no actual invocation mechanism. Claude reads it and then... describes what it would do.

**Fix:** Replace the routing table's "Routes to" column entries with explicit invocation instructions for skills.

- [ ] **Step 1: Update routing section in brain-dump.md**

Add after the routing table:
```markdown
### For items that need a skill — invoke it

When an item routes to a skill:
1. Say: "Routing [item] to [skill] — here's what it will do: [1-sentence preview]"
2. Get confirmation
3. Use the Skill tool to invoke: `skill: "[skill-name]"`

Do not just describe the routing — actually invoke the skill on confirmation.
```

- [ ] **Step 2: Commit**

---

## Task 7: Add /daily command

**Files:**
- Create: `mr-burger-workflow/commands/daily.md`

**What it does:** Lightweight daily planning view — surfaces top tasks across all projects, flags urgent items, suggests focus for today.

- [ ] **Step 1: Create daily.md**
- [ ] **Step 2: Run setup.sh**
- [ ] **Step 3: Commit**

---

## Task 8: Activate dormant skills

**Skills:** `plugin-registry`, `work-logger`, `notion-sync`

**Problem:** These skills exist but no command calls them and there's no documented trigger.

- [ ] **Step 1: Read each skill to understand what it does**
- [ ] **Step 2: Add trigger guidance to each skill's description**
- [ ] **Step 3: Add to claude-code-cheat-sheet.md** — when to invoke each
- [ ] **Step 4: Commit**

---

## Execution Order

1. Task 1 — delete orphan (5 min, no decisions)
2. Task 3 — fix /resume plan step (5 min, no decisions)
3. Task 4 — add prompts to /wrap (10 min)
4. Task 2 — clarify /wrap vs /checkpoint (15 min, one decision)
5. Task 5 — create /plan command (20 min)
6. Task 6 — fix /brain-dump invocation (15 min)
7. Task 7 — create /daily (20 min)
8. Task 8 — activate dormant skills (30 min)
