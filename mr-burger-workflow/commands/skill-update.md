---
description: Review session and propose improvements to skill or agent files based on how they performed
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /skill-update

Review this session for anything that would improve a skill or agent file. Only propose changes based on real experience from this conversation — how the skill actually performed, what was missing, what caused friction.

## Step 1: Identify skills and agents used

Look at this session and identify which skills and agents were invoked. If the user passed an argument (e.g., `/skill-update bellringer-builder`), focus on that one.

Find the source file — always edit source, never symlinks:
```bash
find ~/Documents/Tech/mr-burger-plugins -name "skill.md" -path "*[skill-name]*" 2>/dev/null
find ~/Documents/Tech/mr-burger-plugins -name "[agent-name].md" -path "*/agents/*" 2>/dev/null
```

Read the current file before proposing anything.

## Step 2: Review session performance

Look for evidence of:
- **Gaps** — the skill didn't cover something it should have, requiring manual correction
- **Wrong assumptions** — the skill assumed something about context that wasn't true
- **Missing steps** — something had to be added mid-task that should be built in
- **Friction** — output needed repeated correction in a predictable way
- **Outdated content** — skill referenced files, paths, or structures that have since changed
- **What worked well** — confirm patterns worth keeping explicitly, especially if non-obvious

**Skip:**
- One-off issues specific to this task
- Style preferences
- Things already in the skill
- Theoretical improvements not grounded in this session

## Step 3: Propose changes

For each proposed change, show:

```
### Proposed edit to [file path]

**What happened:** [1 sentence — what friction or gap occurred]
**Fix:** [what to add, change, or remove]

[diff-style or inline — show exactly what changes]
```

If no changes are warranted: "The skill(s) used this session performed as expected — no updates needed."

## Step 4: Apply with approval

List proposed changes numbered. Apply only approved ones.

After applying: remind the user to run `cd ~/Documents/Tech/mr-burger-plugins && git add -p && git commit` to save the changes to version control. Changes are live immediately via symlinks without any rebuild needed.

## Notes

- Source files live in `~/Documents/Tech/mr-burger-plugins/[plugin]/skills/[name]/skill.md`
- Agent files: `~/Documents/Tech/mr-burger-plugins/[plugin]/agents/[name].md`
- Never edit `~/.claude/skills/` or `~/.claude/agents/` — those are symlinks
- For Cowork users: after editing, run `./scripts/package.sh` to rebuild `.plugin` packages
