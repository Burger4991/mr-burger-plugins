---
description: Capture a brainstorm session — options explored, decision made, things rejected and why. Saves to docs/brainstorm/ and feeds into writing-plans.
allowed-tools: Read, Write, Bash, Glob
---

# /brainstorm-capture

Lock in the thinking from a brainstorm session before it disappears at `/clear`.
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
- writing-plans checks `docs/brainstorm/` automatically — no extra steps needed
- If called after `/wrap` already ran: still save, just note the timing
- Keep it factual — capture what was said, not new analysis
