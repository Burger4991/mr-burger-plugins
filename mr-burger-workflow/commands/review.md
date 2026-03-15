---
description: End-of-week review — what got done, what's next
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /review Command

Run your end-of-week review to reflect on what got done, identify blockers, and prepare for the next week.

## How to Use

Simply invoke `/review` and Claude will guide you through a structured reflection session.

## What Happens

Claude will:

1. **Read Your Week**
   - Load `TASKS.md` to see what moved (completed, still active, newly added)
   - Load `GOALS.md` to review this week's focus items
   - Load `journal/` recent entries for context on your week

2. **Present Your Results**
   - Show: what tasks moved to Done (celebrate wins!)
   - Show: what items are still active or stuck
   - Surface: any tasks active for more than 2-3 weeks (needs attention or reprioritization)
   - Highlight: any items that didn't get touched (maybe remove or reschedule)

3. **Ask Reflection Questions**
   - "What went well this week?"
   - "What got in the way?"
   - "What should we carry forward to next week?"
   - "What should we let go of?"

4. **Update Your Second Brain**
   - Archive completed tasks: move to "Done" section with completion date `(completed YYYY-MM-DD)`
   - Mark stuck items: consider moving to "Waiting" or "Someday" or breaking them down
   - Update `GOALS.md` with progress notes and reflections
   - Create a journal entry at `~/Desktop/SecondBrain/journal/YYYY-MM-DD-weekly-review.md` with:
     - What got done (wins)
     - What didn't move (blockers or deprioritizations)
     - Learnings or observations
     - Focus for next week

5. **Sync to Notion** (if available)
   - Push all task status updates to Notion
   - Ensure journal entry links to Notion for traceability

6. **Generate Next Week Prompt**
   - Suggest what to focus on next week based on what's waiting and upcoming deadlines

## Review Best Practices

- **Honest**: Note what didn't happen and why (no judgment)
- **Specific**: Capture real blockers so you can address them
- **Grateful**: Acknowledge what you *did* accomplish
- **Adaptive**: Use blockers and learnings to adjust next week's plan
- **Time-Bound**: Spend 20-30 minutes on your review

## File Locations Touched

- `~/Desktop/SecondBrain/TASKS.md` — Archive completed items, surface blockers
- `~/Desktop/SecondBrain/GOALS.md` — Add progress notes and reflections
- `~/Desktop/SecondBrain/journal/YYYY-MM-DD-weekly-review.md` — New review entry created

---

**Tip**: Run `/review` on Friday afternoon or Saturday morning to close out the week. Pair with `/plan` to start fresh for the upcoming week. Together they form a weekly rhythm: Plan → Execute → Review → Repeat.
