---
description: Review session and propose CLAUDE.md updates for the current project
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /revise

Review this session for anything worth adding to the current project's CLAUDE.md. Only propose additions that would genuinely help future sessions — skip anything already documented, obvious from the code, or too ephemeral to matter.

## Step 1: Find CLAUDE.md files

Run:
```bash
find . -name "CLAUDE.md" -maxdepth 3 2>/dev/null
```

If none found in the current directory tree, check the parent:
```bash
find .. -name "CLAUDE.md" -maxdepth 2 2>/dev/null
```

Read the relevant CLAUDE.md file(s) before proposing anything — don't suggest what's already there.

## Step 2: Review the session

Look for things that came up in this conversation that aren't documented:

- Gotchas or constraints that tripped us up
- Conventions or patterns we followed that aren't obvious from the code
- Commands or workflows that were useful
- Decisions made with a "why" that won't be obvious later
- Structural facts about the project (file locations, naming conventions, etc.)

**Skip:**
- One-off fixes unlikely to recur
- Things already in CLAUDE.md
- Things obvious from reading the code or files
- Ephemeral session details (what we talked about, current task state — that's HANDOFF.md territory)

## Step 3: Propose changes

For each proposed addition, show:

```
### Proposed addition to [file path]

**Why:** [one sentence — what problem this solves for future sessions]

> [the addition — keep it to 1-3 lines max]
```

If nothing worth adding was found, say so explicitly: "Nothing from this session warrants a CLAUDE.md update."

## Step 4: Apply with approval

Ask: "Apply any of these?" List them numbered. Apply only the ones approved.

Keep additions concise — CLAUDE.md is loaded into every session prompt, so brevity matters.
