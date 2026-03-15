---
description: Weekly planning session — set priorities and focus
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /plan Command

Run your weekly planning session to set priorities, organize your week, and align your tasks with your goals.

## How to Use

Simply invoke `/plan` and Claude will guide you through a structured planning session.

## What Happens

Claude will:

1. **Read Your Current State**
   - Load `TASKS.md` to see what's active, waiting, and someday items
   - Load `GOALS.md` to see your current focus and area-specific goals
   - Load `INBOX.md` to review any unsorted items

2. **Present Your Status**
   - Show: active tasks by area, waiting items, inbox items awaiting routing
   - Surface: tasks that have been active too long, blocked items, completed tasks to move

3. **Ask You to Set Priorities**
   - "What are your 3-5 priorities for this week?"
   - Help narrow down from many active items to clear weekly focus
   - Consider: teaching deadlines, job applications, personal goals

4. **Update Your Planning Files**
   - Update `GOALS.md` "Current Focus" section with this week's priorities (organized by area)
   - Move completed tasks to the "Done" section (dated)
   - Process unsorted inbox items — route them to the right location or delete
   - Tag urgent or time-sensitive items as needed

5. **Sync to Notion** (if available)
   - Push priority updates and completed tasks to your Notion task database
   - Ensure bidirectional sync so Notion reflects your Second Brain

6. **Generate Summary**
   - Create a brief weekly planning summary showing your commitments

## Planning Best Practices

- **Focus**: Aim for 3-5 true priorities (not 20 "priorities")
- **Realistic**: Include existing commitments (teaching load, job search)
- **Flexible**: Leave room for unexpected items and daily adjustments
- **Review**: Check in daily with `/briefing` to stay aligned

## File Locations Touched

- `~/Desktop/SecondBrain/TASKS.md` — Updated with weekly priorities
- `~/Desktop/SecondBrain/GOALS.md` — Current Focus section updated
- `~/Desktop/SecondBrain/INBOX.md` — Unsorted items routed or cleared
- `~/Desktop/SecondBrain/plans/` — Optional: detailed project planning documents

---

**Tip**: Run `/plan` on Sunday evening or Monday morning to start your week with clarity. Pair with `/review` at week's end to close the loop.
