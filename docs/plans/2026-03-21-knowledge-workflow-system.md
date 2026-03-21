# Knowledge & Workflow System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a cohesive session infrastructure — auto-loading context hierarchy, shared session state, enhanced commands, brainstorm capture, universal brain dump routing, and git habit integration.

**Architecture:** A shared `session-state-reader` skill provides structured project state to all commands. A SessionStart hook injects compact context automatically. Commands (/resume, /capture, /wrap) are enhanced to call the reader first. Two new commands (/brainstorm-capture, /dump) are added. All git operations are narrated for habit-building.

**Spec:** `docs/specs/2026-03-21-knowledge-workflow-system-design.md`

**Tech Stack:** Markdown skill files, Node.js (existing SessionStart hook pattern), bash.

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `~/.claude/hooks/teaching-session-init.js` | Add PROJECT.md + TASKS.md context injection |
| Create | `mr-burger-workflow/skills/session-state-reader/skill.md` | Shared state reader all commands call first |
| Modify | `mr-burger-workflow/commands/resume.md` | Full hierarchy orientation |
| Modify | `mr-burger-workflow/commands/capture.md` | Context-first routing + brainstorm detection |
| Modify | `mr-burger-workflow/commands/wrap.md` | Validate state + brainstorm flag |
| Create | `mr-burger-workflow/commands/brainstorm-capture.md` | Explicit brainstorm session capture |
| Create | `mr-burger-workflow/commands/dump.md` | Universal brain dump router |
| Create | `~/Desktop/github-cheat-sheet.md` | Git/GitHub quick reference |
| Create | `~/Desktop/project-workflow-cheat-sheet.md` | Full habit loop cheat sheet |

---

## Task 1: session-state-reader skill

**Files:**
- Create: `mr-burger-workflow/skills/session-state-reader/skill.md`

- [ ] **Step 1: Create the skill file**

```markdown
---
description: Read current project state hierarchy — PROJECT.md, TASKS.md, HANDOFF.md, plan files. Called by all workflow commands before acting.
---

# Session State Reader

A shared skill — not user-facing. Called internally by /resume, /capture, /wrap, and /dump before they do anything else.

## What to do

Read the following in order. Return a structured state block.

### 1. Find PROJECT.md
- Check current working directory for `PROJECT.md`
- If not found, walk up directories to `~/`
- If found, extract: project name, phase, resume_at point

### 2. Find TASKS.md
- Always at `~/Documents/TASKS.md`
- Extract active items only (lines under `## Active` that are unchecked `- [ ]`)
- Filter to current project if PROJECT.md found (match `[ProjectName]` tag)

### 3. Find HANDOFF.md
- Check current working directory only
- Note if it exists — don't read it (that's /resume's job)

### 4. Find plan file
- If PROJECT.md references a plan file path, note it
- Don't read it yet — just note the path

### 5. Find brainstorm doc
- Check `docs/brainstorm/` in current directory
- Note most recent file if present

## Output

Return this structured block (fill in what's found, use "none" for missing):

---
SESSION STATE
Project: [name] | none
Phase: [phase] | none
Resume at: [exact next step] | none
Active tasks: [comma-separated list filtered to project] | none
Handoff: exists | not found
Plan file: [path] | none
Brainstorm doc: [path] | none
---

## Notes
- If no PROJECT.md found anywhere: return all fields as "none"
- Never read HANDOFF.md — that's /resume's responsibility
- Never read the plan file — just surface the path
- This skill is fast — it reads metadata, not full file contents
```

- [ ] **Step 2: Verify skill file exists and is readable**

```bash
cat mr-burger-workflow/skills/session-state-reader/skill.md
```

- [ ] **Step 3: Run setup.sh to symlink**

```bash
cd ~/Documents/Tech/mr-burger-plugins && ./scripts/setup.sh
```

Expected: session-state-reader appears in `~/.claude/skills/`

- [ ] **Step 4: Commit**

```bash
git add mr-burger-workflow/skills/session-state-reader/skill.md
git commit -m "feat(workflow): add session-state-reader shared skill

Shared state layer called by all workflow commands before acting.
Reads PROJECT.md → TASKS.md → HANDOFF.md hierarchy and returns
structured state so commands don't each re-read the file system.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 2: Enhance SessionStart hook

**Files:**
- Modify: `~/.claude/hooks/teaching-session-init.js`

The existing hook injects teaching skill awareness. Extend it to also read PROJECT.md + TASKS.md and inject compact project context.

- [ ] **Step 1: Read current hook**

```bash
cat ~/.claude/hooks/teaching-session-init.js
```

- [ ] **Step 2: Add project context injection after teaching block**

Add this logic after the existing teaching message is built:

```javascript
// Project context injection
const projectContext = [];
let dir = process.cwd();
const home = os.homedir();
let projectMd = null;

// Walk up from cwd to home looking for PROJECT.md
while (dir !== path.dirname(home)) {
  const candidate = path.join(dir, 'PROJECT.md');
  if (fs.existsSync(candidate)) {
    projectMd = candidate;
    break;
  }
  if (dir === home) break;
  dir = path.dirname(dir);
}

if (projectMd) {
  const content = fs.readFileSync(projectMd, 'utf8');
  const phaseMatch = content.match(/^## Phase\n(.+)/m);
  const resumeMatch = content.match(/\*\*Current step:\*\* (.+)/m);
  const phase = phaseMatch ? phaseMatch[1].trim() : 'unknown';
  const resume = resumeMatch ? resumeMatch[1].trim() : 'see PROJECT.md';

  // Read active tasks filtered to project
  const tasksPath = path.join(home, 'Documents', 'TASKS.md');
  let tasks = [];
  if (fs.existsSync(tasksPath)) {
    const tasksContent = fs.readFileSync(tasksPath, 'utf8');
    const activeSection = tasksContent.match(/## Active([\s\S]*?)##/);
    if (activeSection) {
      tasks = activeSection[1]
        .split('\n')
        .filter(l => l.startsWith('- [ ]'))
        .slice(0, 3);
    }
  }

  const handoffExists = fs.existsSync(path.join(process.cwd(), 'HANDOFF.md'));

  projectContext.push('');
  projectContext.push('--- Session Context ---');
  projectContext.push(`Project: ${path.basename(path.dirname(projectMd))} | Phase: ${phase}`);
  projectContext.push(`Resume at: ${resume}`);
  if (tasks.length) projectContext.push(`Active tasks: ${tasks.map(t => t.replace('- [ ] ','').substring(0,60)).join(' | ')}`);
  if (handoffExists) projectContext.push('Handoff found — run /resume for full context');
  projectContext.push('---');
}

const fullMessage = message + projectContext.join('\n');
process.stdout.write(fullMessage);
```

- [ ] **Step 3: Test by opening a new Claude session in ir-platform directory**

```bash
cd ~/Desktop/ir-platform && claude
```

Expected: Session context block appears below teaching init block.

- [ ] **Step 4: Test in home directory (no PROJECT.md)**

```bash
cd ~ && claude
```

Expected: No project context block — just teaching init as before.

- [ ] **Step 5: Commit hook change**

```bash
# Hook lives outside the plugin repo — commit note only
# The hook file at ~/.claude/hooks/teaching-session-init.js is not git-tracked
# Document the change in mr-burger-plugins instead:
git add -A
git commit -m "docs: note SessionStart hook updated with project context injection

Hook at ~/.claude/hooks/teaching-session-init.js now reads PROJECT.md
and TASKS.md at session start and injects compact context block.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 3: Enhance /resume

**Files:**
- Modify: `mr-burger-workflow/commands/resume.md`

- [ ] **Step 1: Read current resume.md**

```bash
cat mr-burger-workflow/commands/resume.md
```

- [ ] **Step 2: Rewrite to call session-state-reader first, then layer HANDOFF + plan**

Replace content with:

```markdown
---
description: Resume a previous session — reads full context hierarchy (PROJECT.md → HANDOFF.md → plan file) and delivers a synthesized orientation
allowed-tools: Read, Glob, Bash
---

# /resume

Pick up where you left off. Reads the full context hierarchy and orients you for the session ahead.

## What to do

1. **Call session-state-reader** — get structured project state before reading anything else

2. **Read HANDOFF.md** (if it exists in current dir):
```bash
cat ./HANDOFF.md 2>/dev/null
```

3. **Read plan file** (if session state has a plan_file path):
   - Read it, find the current step (first unchecked `- [ ]`)

4. **Check active tasks**:
```bash
awk '/^## Active/{found=1; next} /^## /{found=0} found && /^\- \[ \]/{print}' ~/Documents/TASKS.md 2>/dev/null | head -5
```

5. **Synthesize orientation** — combine all sources into a brief summary:
   - Current phase + where in it (from PROJECT.md — authoritative)
   - What happened last session (from HANDOFF.md)
   - Exact next action (from plan file current step, or PROJECT.md resume_at)
   - Relevant active tasks only (filtered to current project)
   - Open questions or watch-outs

   **Conflict rule:** PROJECT.md beats HANDOFF.md when they conflict.

   Keep it short. End with: "Ready to continue. What would you like to start with?"

6. **If no PROJECT.md and no HANDOFF.md** — say so and show active tasks.

## Notes
- Don't recite files verbatim — synthesize and orient
- If files are stale (old date), flag it
- If a brainstorm doc exists for the active topic, mention it
```

- [ ] **Step 3: Verify file written correctly**

```bash
head -20 mr-burger-workflow/commands/resume.md
```

- [ ] **Step 4: Commit**

```bash
git add mr-burger-workflow/commands/resume.md
git commit -m "feat(resume): enhance with full context hierarchy orientation

Now calls session-state-reader first, reads HANDOFF + plan file,
synthesizes orientation from all sources. PROJECT.md takes precedence
over HANDOFF.md when they conflict.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 4: Enhance /capture

**Files:**
- Modify: `mr-burger-workflow/commands/capture.md`

- [ ] **Step 1: Read current capture.md**

```bash
cat mr-burger-workflow/commands/capture.md
```

- [ ] **Step 2: Add session-state-reader call + context-first routing + brainstorm detection**

Key additions to existing capture logic:

```markdown
### Step 0: Call session-state-reader
Get current project state. Use it to pre-classify items — life area and project context are already known.

### Step 1: Parse + pre-classify (context-first)
Use session state + conversation context to infer routing for every item.
Confidence: high = file it; low = flag for confirm.

Brainstorm detection — classify as brainstorm if:
- Multiple options being compared
- Exploratory language ("should we / what if / I'm thinking about")
- No clear action item — it's directional, not actionable
Route brainstorm items to `docs/brainstorm/YYYY-MM-DD-topic.md`

### Step 2: One confirm message for ALL items
Present routing for everything at once:
"I'll route these:
→ TASKS.md: [item]
→ Teaching/ideas.md: [item]
→ docs/brainstorm/[topic].md: [item]
Anything to change?"

File everything on approval. No item-by-item back-and-forth.
```

- [ ] **Step 3: Commit**

```bash
git add mr-burger-workflow/commands/capture.md
git commit -m "feat(capture): add context-first routing and brainstorm detection

Now calls session-state-reader to pre-classify all items before
presenting. One confirm round-trip instead of item-by-item questions.
Brainstorm content auto-detected and routed to docs/brainstorm/.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 5: Enhance /wrap

**Files:**
- Modify: `mr-burger-workflow/commands/wrap.md`

- [ ] **Step 1: Add Step 0 (session-state-reader call) to existing wrap**

Add before current Step 1:

```markdown
### Step 0: Call session-state-reader
Get current project state. Use it to:
- Validate what you write to PROJECT.md (does it match actual current state?)
- Detect if brainstorm-style discussion happened this session
```

- [ ] **Step 2: Add brainstorm detection flag before confirm step**

Add before the final confirm:

```markdown
### Brainstorm check
If session contained exploratory discussion (options compared, directions weighed)
and no /brainstorm-capture was run, flag it:
"Looks like this session had brainstorm-style discussion about [topic].
Run /brainstorm-capture before /clear to preserve that thinking?"
This is a flag, not a blocker — user can skip it.
```

- [ ] **Step 3: Commit**

```bash
git add mr-burger-workflow/commands/wrap.md
git commit -m "feat(wrap): add session-state-reader validation and brainstorm flag

Now validates PROJECT.md/HANDOFF.md writes against actual session state.
Flags brainstorm-style discussions before /clear so thinking isn't lost.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 6: Create /brainstorm-capture

**Files:**
- Create: `mr-burger-workflow/commands/brainstorm-capture.md`

- [ ] **Step 1: Create the command**

```markdown
---
description: Capture a brainstorm session — options explored, decision made, things rejected and why. Saves to docs/brainstorm/ and feeds into writing-plans.
allowed-tools: Read, Write, Bash, Glob
---

# /brainstorm-capture

Lock in the thinking from a brainstorm session before it disappears at /clear.
Run this at the end of any brainstorm — formal (superpowers) or informal (conversation).

## What to do

1. **Call session-state-reader** — get project name and active topic

2. **Scan conversation** — extract:
   - The question being explored
   - Options that were presented and their trade-offs
   - What was decided and why
   - What was rejected and why
   - Open questions going into the spec/plan

3. **Determine save location**
   - If in a project directory with `docs/brainstorm/` → save there
   - If no project / user-scope work → save to `~/Documents/Knowledge/brainstorm/`
   - Create the directory if it doesn't exist

4. **Write the capture file** as `YYYY-MM-DD-[topic].md`:

```markdown
# [Topic] — Brainstorm Capture
*Date: YYYY-MM-DD HH:MM*

## What we were figuring out
[1-3 sentences]

## Options considered
- **Option A** — [description + trade-offs]
- **Option B** — [description + trade-offs]

## Decision
[What was chosen and why]

## Rejected (and why)
- [Option]: [reason]

## Open questions going into the spec
- [question]
```

5. **Confirm** — tell user where it was saved and that it will be picked up by writing-plans.

## Notes
- writing-plans checks docs/brainstorm/ automatically — no extra steps needed
- If called after /wrap already ran: still save, just note the timing
- Keep it factual — capture what was said, not new analysis
```

- [ ] **Step 2: Commit**

```bash
git add mr-burger-workflow/commands/brainstorm-capture.md
git commit -m "feat(workflow): add /brainstorm-capture command

New command that locks in pre-spec thinking — options explored,
decision made, things rejected. Saves to docs/brainstorm/ and feeds
automatically into writing-plans.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 7: Create /dump (universal brain dump router)

**Files:**
- Create: `mr-burger-workflow/commands/dump.md`

- [ ] **Step 1: Create the command**

```markdown
---
description: Universal brain dump — accepts anything, decides what to do with it. Routes to /capture, /brainstorm-capture, a skill, or multiple at once.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /dump

The smart brain dump. Throw anything at it — tasks, ideas, brainstorms, skill friction, half-formed thoughts. It reads the context, classifies everything, and routes to the right place or skill.

## What to do

1. **Call session-state-reader** — know what project/phase we're in

2. **Classify every item** in the dump:

| Classification | Triggers | Routes to |
|---------------|----------|-----------|
| Task/reminder | Action verb, deadline, "I need to" | TASKS.md via /capture |
| Teaching idea | Unit, lesson, student, benchmark | Teaching/ideas.md via /capture |
| Career note | Job, edtech, application, networking | Career/notes.md via /capture |
| Brainstorm | Options being weighed, "should we", exploratory | /brainstorm-capture |
| Skill friction | "The skill didn't", "that didn't work" | /skill-update flag |
| Memory-worthy | Durable preference or lesson | Memory (ask first) |
| Needs a skill | Benchmark code, data keyword, unit topic | Route to relevant skill |
| Mixed | Multiple types | Split and route each part |

3. **For items that need a skill** — identify which skill applies and invoke it:
   - Benchmark codes → benchmark skill
   - Data keywords (PM, FAST, NWEA) → data pipeline skills
   - Unit topics → ir-teaching skills
   - Plugin friction → skill-update

4. **Present routing for all items in one message** — same confirm pattern as /capture

5. **Execute on approval**

## Examples

```
/dump LAFS.8.RI.1.2 — students are struggling with central idea. Also I need
to grade PM data this week. Been thinking about whether to add a new skill
for vocabulary — not sure if esol-core covers it or we need something new.
```

Routes:
→ benchmark skill: LAFS.8.RI.1.2 (central idea instruction)
→ TASKS.md: grade PM data this week
→ /brainstorm-capture: vocabulary skill gap question

## Notes
- /dump is the entry point; /capture and /brainstorm-capture are its execution layer
- If everything in the dump is clearly one type, just do it — don't over-route
- For skill invocations: surface what the skill would do, get approval before running
```

- [ ] **Step 2: Commit**

```bash
git add mr-burger-workflow/commands/dump.md
git commit -m "feat(workflow): add /dump universal brain dump router

New command that accepts any brain dump and routes intelligently —
to /capture, /brainstorm-capture, relevant skills, or multiple at once.
The smart entry point above /capture.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Task 8: Run setup.sh and verify all commands symlinked

- [ ] **Step 1: Run setup**

```bash
cd ~/Documents/Tech/mr-burger-plugins && ./scripts/setup.sh
```

- [ ] **Step 2: Verify new commands appear**

```bash
ls ~/.claude/skills/ | grep session-state
ls ~/.claude/commands/ | grep -E "brainstorm|dump"
```

Expected: `session-state-reader`, `brainstorm-capture`, `dump` all present.

---

## Task 9: Create cheat sheets

**Files:**
- Create: `~/Desktop/github-cheat-sheet.md`
- Create: `~/Desktop/project-workflow-cheat-sheet.md`

- [ ] **Step 1: Create github-cheat-sheet.md**

Write a scannable reference covering:
- Branch creation + naming conventions
- Commit message format (subject + body)
- PR steps (create, review diff, merge)
- Issue linking (`Closes #N`)
- Tags + releases
- Common commands quick-ref

- [ ] **Step 2: Create project-workflow-cheat-sheet.md**

Write the full habit loop mapped to the existing system:
- How git events map to PROJECT.md / HANDOFF.md / TASKS.md updates
- Branch → commit body → PR → merge → tag sequence
- When to update PROJECT.md vs HANDOFF.md vs TASKS.md
- Narration rule reminder

- [ ] **Step 3: Commit cheat sheets to mr-burger-plugins docs**

```bash
cp ~/Desktop/github-cheat-sheet.md docs/
cp ~/Desktop/project-workflow-cheat-sheet.md docs/
git add docs/github-cheat-sheet.md docs/project-workflow-cheat-sheet.md
git commit -m "docs: add GitHub and project workflow cheat sheets

Reference cards for git habit loop — branch, commit body, PR, merge,
release — mapped to the PROJECT.md/HANDOFF.md/TASKS.md system.

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

## Execution Order

Tasks must run in this order — each builds on the previous:

1. Task 1: session-state-reader (dependency for all commands)
2. Task 2: SessionStart hook (standalone, no dependencies)
3. Task 3: /resume (uses session-state-reader)
4. Task 4: /capture (uses session-state-reader)
5. Task 5: /wrap (uses session-state-reader)
6. Task 6: /brainstorm-capture (standalone new command)
7. Task 7: /dump (depends on /capture and /brainstorm-capture existing)
8. Task 8: setup.sh + verify
9. Task 9: cheat sheets (standalone)
