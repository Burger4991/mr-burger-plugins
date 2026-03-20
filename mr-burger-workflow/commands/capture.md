---
description: Brain dump anything — Claude routes it to the right place
allowed-tools: Read, Write, Edit, Bash, Glob
---

# /capture

Brain dump anything. Claude parses it, files what it can, and surfaces what needs your action.

## How to Use

Invoke `/capture` followed by your brain dump (or just run it and talk):

- `/capture I need to grade PM2 data before Friday and look into that Amplify job posting. Also been thinking about jazz vocabulary.`
- `/capture remind me to check Olive's sit-stay progress. Also the benchmark-rhetoric skill needs updating based on today's session.`
- `/capture ideas for the next unit — something with informational texts and a current events angle`

## What to Do

### Step 1: Parse the dump

Identify each item and classify it:

| Type | Description | Example |
|------|-------------|---------|
| **Task/reminder** | Something to do — has an action | "Grade PM2 data before Friday" |
| **Teaching idea** | Content, unit, or instructional idea | "Unit with current events angle" |
| **Career note** | Job search, networking, edtech | "Look into Amplify posting" |
| **Skill/agent fix** | Something to improve in the plugin system | "benchmark-rhetoric skill needs updating" |
| **Memory-worthy** | A preference, lesson, or fact Claude should retain | "User prefers X approach" |
| **Music/Dog/Personal** | Life area note | "Jazz vocabulary practice" |
| **Unclear** | Can't route confidently | Ask one targeted question |

### Step 2: Surface existing notes first

Before filing anything, check what's already been captured in the relevant areas:

```bash
cat ~/Documents/Teaching/Resources/ideas.md 2>/dev/null | tail -10
cat ~/Documents/Career/notes.md 2>/dev/null | tail -10
# etc. for any area touched by this dump
```

Show the last 5-10 entries for each relevant area under a heading like:
```
📋 Already in Teaching Ideas:
- 2026-03-15 Unit with current events angle
- 2026-03-10 Short story sequence with ESOL scaffold
```

This lets you spot duplicates or related items before adding.

### Step 3: File what you can

**Teaching ideas** → Append to `~/Documents/Teaching/Resources/ideas.md`
- Create the file if it doesn't exist with a `# Teaching Ideas` header
- Add as `- [date] [idea]`

**Career notes** → Append to `~/Documents/Career/notes.md`
- Create if needed with `# Career Notes` header
- Add as `- [date] [note]`

**Music notes** → Append to `~/Documents/Music/notes.md`

**Dog training notes** → Append to `~/Documents/Dog-Training/notes.md`

**Personal notes** → Append to `~/Documents/Personal/notes.md`

**Skill/agent fixes** → Note these for `/skill-update` — don't edit skill files here, just surface them clearly

**Memory-worthy** → Write to the appropriate memory file at `~/.claude/projects/-Users-alexanderburger/memory/` following the memory format (user/feedback/project/reference). Ask before saving.

### Step 4: Handle tasks

Write tasks and action items to `~/Documents/TASKS.md` under `## Active`:
```
- [ ] Grade PM2 data (by Friday)
- [ ] Look into Amplify job posting
```

For time-sensitive tasks, also output a copy-paste list for iPhone Reminders:
```
📱 Also add to iPhone Reminders (time-sensitive):
- Grade PM2 data — by Friday
```

Only suggest iPhone Reminders for things with deadlines or that need a push notification. Everything else just goes in TASKS.md.

### Step 5: Confirm

Output a brief summary:
```
Captured [N] items:
✓ Filed: [what went where]
✓ Skill fix noted: [which skill, what issue]
📱 Reminders to add: [count] (listed above)
```

## Notes

- Don't create new files in places that don't exist yet — check with `ls` first, create only notes files
- If the dump is ambiguous about life area, ask once rather than guess
- Don't route to memory without asking — memory is for durable lessons, not task notes
- Keep filed notes minimal — one line per idea, dated
