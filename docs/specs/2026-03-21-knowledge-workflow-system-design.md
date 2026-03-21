# Knowledge & Workflow System — Design Spec
*Created: 2026-03-21*

> Redesign the session infrastructure so context loading, knowledge persistence, git habits, and brainstorm capture work as a cohesive system. Goal: Mr. Burger internalizes these as real skills, not just automation.

---

## Section 1: Overall Architecture

Four layers that build on each other:

```
Layer 1 — SessionStart Hook (always-on, silent)
  Reads: current dir PROJECT.md → parent PROJECT.md → TASKS.md (active only)
  Injects: compact structured block into every session automatically
  Output: current phase, active project, top tasks — not full file dumps

Layer 2 — Session State Reader (shared skill)
  A reusable skill all commands call before doing anything
  Knows how to read the full hierarchy and return structured state
  Makes commands aware of each other — they all read the same source

Layer 3 — Enhanced Commands (all call Layer 2 first)
  /resume              → full orientation (hierarchy + HANDOFF + plan files synthesized)
  /capture             → context-first routing (pre-classifies using session state)
  /wrap                → validates PROJECT.md + HANDOFF against current session state
  /brainstorm-capture  → new command (see Layer 4)

Layer 4 — /brainstorm-capture (new command)
  Captures brainstorm session content in structured format
  Saves to docs/brainstorm/YYYY-MM-DD-topic.md
  Output feeds directly into writing-plans
```

**Status: Approved**

---

## Section 2: Layer 1 — SessionStart Hook

Fires at every session start. Fast and compact — injects only what's needed, not full file dumps.

**Behavior:**
1. Detect current working directory
2. Search for `PROJECT.md` in current dir, then walk up to `~/`
3. Read `PROJECT.md` — phase + resume point only
4. Read `TASKS.md` — active items only, filtered to current project if PROJECT.md found
5. Check for `HANDOFF.md` — if found, flag it but don't read it (that's /resume's job)
6. Inject compact structured block:

```
--- Session Context ---
Project: [name] | Phase: [phase]
Resume at: [exact next step]
Active tasks: [2-3 relevant items]
Handoff found — run /resume for full context
---
```

If no `PROJECT.md` found anywhere: inject nothing, stay silent.
If no `HANDOFF.md`: omit that line.

**What it does NOT do:** Read HANDOFF.md, read plan files, synthesize orientation — that's /resume's responsibility.

**Status: Approved**

---

## Section 3: Brainstorm Capture

**File location:** `docs/brainstorm/YYYY-MM-DD-topic.md` per project repo.
User-scope brainstorms (not tied to a project): `~/Documents/Knowledge/brainstorm/`

**Document structure:**
```markdown
# [Topic] — Brainstorm Capture
*Date: YYYY-MM-DD HH:MM*

## What we were figuring out
[1-3 sentences on the question being explored]

## Options considered
- **Option A** — [description + trade-offs]
- **Option B** — [description + trade-offs]
- **Option C** — [description + trade-offs]

## Decision
[What was chosen and why]

## Rejected (and why)
- [Option X]: [reason it was ruled out]

## Open questions going into the spec
- [question]
```

**`/brainstorm-capture` command:**
- Run at end of any brainstorm session (formal or informal)
- Reads conversation, extracts structure above, saves to `docs/brainstorm/`
- Can also run standalone — captures pre-spec thinking before a plan exists

**`writing-plans` integration:**
When writing-plans runs, it checks for a matching brainstorm doc in `docs/brainstorm/` and uses it as context — plan inherits the reasoning, not just the outcome.

**Status: Approved**

---

## Section 4a: Enhanced /resume

**Steps:**
1. Call Session State Reader — get current hierarchy state
2. Read `HANDOFF.md` — session bridge
3. If plan file referenced in `PROJECT.md` → read it, surface current step
4. If brainstorm doc exists for active topic → note it
5. Synthesize orientation:
   - Current phase + where in it (from PROJECT.md)
   - What happened last session (from HANDOFF.md)
   - Exact next action (from plan file or PROJECT.md resume point)
   - Relevant active tasks only (filtered to current project)
   - Open questions or watch-outs

**Conflict resolution:** PROJECT.md beats HANDOFF.md — it's the persistent record.

**Status: Approved**

---

## Section 4b: Enhanced /capture

**Steps:**
1. Call Session State Reader — know what project/phase we're in
2. Scan last exchanges of conversation for context signals
3. Pre-classify every item in the dump:
   - Life area inferred from session context + keywords
   - Confidence: high (file it) | low (flag for confirm)
4. Present one confirm message for ALL items:
   ```
   I'll route these:
   → TASKS.md: [item]
   → Teaching/ideas.md: [item]
   → docs/brainstorm/: [item]
   Anything to change?
   ```
5. File everything on approval — no item-by-item back-and-forth

**Brainstorm auto-detection:**
If the dump contains exploratory thinking — options being weighed, directions being compared, pre-plan reasoning — classify as brainstorm and route to `docs/brainstorm/` with the Section 3 structure.

Triggers: multiple options being compared, "should we / what if / I'm thinking about...", no clear action item.

**Brainstorm capture is also its own explicit command** (`/brainstorm-capture`) for when you want to deliberately lock in session thinking. Auto-detection in `/capture` handles the opportunistic case; the explicit command handles the intentional case.

**Status: Approved**

---

## Section 4c: Enhanced /wrap

Existing steps unchanged. One addition at the top and one new behavior at the end.

**Addition — Step 0 (before anything else):**
Call Session State Reader — use it to validate what gets written to PROJECT.md and HANDOFF.md against the actual current state. Catches drift between session activity and project record.

**New behavior — brainstorm detection:**
If the session contained exploratory brainstorm-style discussion and no `/brainstorm-capture` was run, flag it before confirming:
```
Looks like this session had brainstorm-style discussion about [topic].
Run /brainstorm-capture before /clear to preserve that thinking?
```
User can skip it — it's a flag, not a blocker.

**Status: Approved**

---

## Section 5: Layer 2 — Session State Reader

A shared skill (`session-state-reader`) in `mr-burger-workflow/skills/`. Not a command — users never call it directly. All enhanced commands invoke it first.

**Input:** current working directory

**Steps:**
1. Find `PROJECT.md` — current dir, walk up to `~/`
2. Find `TASKS.md` — always at `~/Documents/TASKS.md`
3. Find `HANDOFF.md` — current dir only
4. Find plan file — path from `PROJECT.md` if referenced
5. Find brainstorm doc — `docs/brainstorm/` matching active topic

**Returns structured state:**
```
project:        [name] | "none"
phase:          [current phase] | "none"
resume_at:      [exact next step] | null
active_tasks:   [filtered to current project]
handoff_exists: true | false
plan_file:      [path] | null
brainstorm_doc: [path] | null
```

Commands use this state to make decisions — they don't each re-read the file system independently. If `project: "none"`, commands fall back to generic behavior.

**Status: Approved**

---

## Section 6: Git Workflow Integration

Goal: habits that feel natural, not automation that replaces thinking. Claude narrates every git operation — shows the manual steps alongside doing them.

**The habit loop:**
```
Start feature  → create branch (feat/what-youre-doing)
Work + commit  → commits have a body (why, not just what)
Done           → open PR with description tied to plan step
Review diff    → use GitHub's diff view before merging (even solo)
Merge          → PROJECT.md updated, task marked done
Tag/release    → for mr-burger-plugins milestones (v1.x.x)
```

**How it maps to the existing system:**

| Git event | System update |
|-----------|--------------|
| Branch created | PROJECT.md notes active branch |
| Commit | Body explains why — references plan step if applicable |
| PR opened | HANDOFF.md notes PR number + branch |
| PR merged | PROJECT.md phase/step updated, task marked done in TASKS.md |
| Release tagged | PROJECT.md decisions log entry |

**Cheat sheets (Desktop):**
- `github-cheat-sheet.md` — git commands, branch rules, PR steps, issue linking
- `project-workflow-cheat-sheet.md` — full habit loop with PROJECT.md/HANDOFF.md system mapped in

**Narration rule:** When Claude runs a git operation, it shows the command and explains what it does and why — so the pattern becomes familiar, not invisible.

**Status: Approved**

---

## Summary

**What this system builds:**

| Component | What it is | Where it lives |
|-----------|-----------|----------------|
| SessionStart hook (enhanced) | Auto-injects project context every session | `~/.claude/hooks/` |
| `session-state-reader` skill | Shared state layer all commands call first | `mr-burger-workflow/skills/` |
| Enhanced `/resume` | Full orientation using hierarchy | `mr-burger-workflow/commands/` |
| Enhanced `/capture` | Context-first routing + brainstorm detection | `mr-burger-workflow/commands/` |
| Enhanced `/wrap` | Validates state + brainstorm flag | `mr-burger-workflow/commands/` |
| `/brainstorm-capture` command | Locks in pre-spec thinking | `mr-burger-workflow/commands/` |
| `docs/brainstorm/` | Brainstorm capture docs per project | Each project repo |
| Git habit loop | Branch → commit body → PR → merge → tag | All repos |
| Two cheat sheets | GitHub quick-ref + project workflow | `~/Desktop/` |
