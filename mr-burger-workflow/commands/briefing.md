---
description: Daily what's-on-deck — priorities and reminders
allowed-tools: Read, Grep, Glob
---

# /briefing Command

Get a quick daily snapshot of your priorities, open items, and reminders. This is a 30-second read to keep you on track.

## How to Use

Simply invoke `/briefing` at the start of your day (or anytime you need a status check).

## What You Get

Claude will read your Second Brain files and deliver a scannable brief with:

1. **Today's Focus** — Active tasks marked urgent or tagged for today, organized by area
2. **Open Items** — Non-urgent active tasks in progress, grouped by area (Teaching, Career, Music, Dog Training, Personal, Tech)
3. **Don't Forget** — Items in your waiting list that might matter today
4. **Inbox Check** — If there are unsorted items in INBOX.md, a flag to process them during next `/plan` session
5. **Week Progress** — Quick visual: how many tasks completed this week vs. how many active

## Output Format

Clean, scannable, no fluff:

```
═════════════════════════════════════════
    Today's Briefing — Monday, Feb 24
═════════════════════════════════════════

📍 TODAY'S FOCUS
  ★ [Teaching] Grade PM2 data (due today)
  ★ [Career] Follow up on application from Friday

📋 OPEN ITEMS
  Teaching: 3 active
    → Unit lesson planning for Week 5
    → ESOL adaptation for benchmark assignment
  Career: 2 active
    → Update portfolio with recent projects
  Music: 1 active
    → Practice Adam routine (30 min)

⏳ WAITING
  [Dog Training] Awaiting feedback on Recallers course

⚠️  INBOX
  3 unsorted items — process during this week's plan session

✓ WEEK PROGRESS
  Completed: 2 tasks | Active: 8 tasks | On track
═════════════════════════════════════════
```

## When to Use

- **Daily**: Start your day with `/briefing` (2 minutes)
- **Check-in**: Feeling lost midday? Run it again
- **Context Switching**: Between areas? Get a quick reset
- **Weekly Prep**: Before your `/plan` session, see what's stacking up

## File Locations Read

- `~/Desktop/SecondBrain/TASKS.md` — Active, waiting, urgent items
- `~/Desktop/SecondBrain/GOALS.md` — This week's focus
- `~/Desktop/SecondBrain/INBOX.md` — Unsorted items (flagged if present)

---

**Tip**: Keep `/briefing` lightweight and fast. If you need deep planning or reflection, that's `/plan` and `/review` territory. This is just: "What matters today?"
