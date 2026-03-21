---
description: Brain dump anything — Claude routes it to the right place
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /capture Command

Use this command to brain dump anything into your Second Brain system. Whether it's loose rambling, structured items, or "remind me to..." style messages, Claude will parse and route everything to the correct location.

## How to Use

Simply invoke `/capture` followed by your brain dump. Examples:

- "I need to grade PM2 data and update my resume before Friday. Also been thinking about learning more jazz vocabulary."
- "remind me to check on Olive's training progress with the Recallers course"
- "Teaching unit on short stories, ESOL adaptations needed, personal finance review, new keyboard layout to explore"

## What Happens

Claude will:

1. **Parse** your input to identify: tasks, ideas, notes, reminders, and calendar items
2. **Route** each item to the correct Second Brain location:
   - **Tasks** → append to `~/Desktop/SecondBrain/TASKS.md` under the "Active" section with appropriate area tags
   - **Ideas & Notes** → create or append to the appropriate `notes/` subfolder (teaching, career, music, dog-training, personal, tech)
   - **Quick Thoughts** → append to `~/Desktop/SecondBrain/INBOX.md` under "Unsorted" for later processing
   - **Calendar Items** → note for you to add manually or suggest timing
3. **Sync to Notion** (if available) — push new tasks to your Notion task database with appropriate properties (Area, Status)
4. **Confirm** what was captured and where it went
5. **Ask Follow-up Questions** if clarification is needed to route items correctly

## Second Brain File Locations

- **TASKS.md**: Master task list with sections: Active, Waiting, Someday, Done
- **INBOX.md**: Unsorted capture inbox
- **GOALS.md**: Current focus and area-specific goals
- **notes/**: Teaching, Career, Music, Dog Training, Personal, Tech subfolders
- **journal/**: Date-stamped reflection entries
- **knowledge/**: Reference material
- **memory/**: Context, preferences, glossary, project notes

## Integration

This command uses the `second-brain-ops` skill to handle routing and file management, and `area-context` to determine which life area each item belongs to. If Notion is connected, it also uses `notion-sync` to keep your Notion database in sync.

---

**Tip**: Use this whenever you need to dump something from your head without worrying about where it goes. Capture first, organize during your weekly `/plan` session.
