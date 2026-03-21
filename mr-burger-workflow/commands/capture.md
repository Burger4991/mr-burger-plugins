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

### Step 0: Call session-state-reader

Get current project state. Use it to pre-classify items — life area and project context are already known.

### Step 1: Parse + pre-classify (context-first)

Use session state + conversation context to infer routing for every item before asking anything.
Confidence: high = file it; low = flag for confirm.

| Type | Description | Example |
|------|-------------|---------|
| **Task/reminder** | Something to do — has an action | "Grade PM2 data before Friday" |
| **Teaching idea** | Content, unit, or instructional idea | "Unit with current events angle" |
| **Career note** | Job search, networking, edtech | "Look into Amplify posting" |
| **Skill/agent fix** | Something to improve in the plugin system | "benchmark-rhetoric skill needs updating" |
| **Memory-worthy** | A preference, lesson, or fact Claude should retain | "User prefers X approach" |
| **Music/Dog/Personal** | Life area note | "Jazz vocabulary practice" |
| **Brainstorm** | Multiple options compared, exploratory, directional not actionable | "Should we add a new skill or extend esol-core?" |
| **Unclear** | Can't route confidently | Flag for confirm |

**Brainstorm detection** — classify as brainstorm if:
- Multiple options being compared
- Exploratory language ("should we / what if / I'm thinking about")
- No clear action item — it's directional, not actionable

Route brainstorm items to `docs/brainstorm/YYYY-MM-DD-topic.md` (or `~/Documents/Knowledge/brainstorm/` if no project context).

### Step 2: One confirm message for ALL items

Present routing for everything at once before filing anything:

```
I'll route these:
→ TASKS.md: [item]
→ Teaching/ideas.md: [item]
→ docs/brainstorm/[topic].md: [item]
→ Career/notes.md: [item]
Anything to change?
```

File everything on approval. No item-by-item back-and-forth.

For time-sensitive tasks, note them for iPhone Reminders:
```
📱 Also add to iPhone Reminders (time-sensitive):
- Grade PM2 data — by Friday
```

### Step 3: File on approval

**Teaching ideas** → Append to `~/Documents/Teaching/Resources/ideas.md`
- Create if needed with `# Teaching Ideas` header
- Add as `- [date] [idea]`

**Career notes** → Append to `~/Documents/Career/notes.md`
- Create if needed with `# Career Notes` header

**Music notes** → Append to `~/Documents/Music/notes.md`

**Dog training notes** → Append to `~/Documents/Dog-Training/notes.md`

**Personal notes** → Append to `~/Documents/Personal/notes.md`

**Tasks** → Write to `~/Documents/TASKS.md` under `## Active`

**Brainstorm** → Use session state to determine the absolute path:
- If in a project (PROJECT.md found): `[project-dir]/docs/brainstorm/YYYY-MM-DD-[topic].md`
- If no project context: `~/Documents/Knowledge/brainstorm/YYYY-MM-DD-[topic].md`
- Create the directory if it doesn't exist

**Skill/agent fixes** → Note for `/skill-update` — surface the exact file path:
`~/Documents/Tech/mr-burger-plugins/[plugin]/skills/[skill-name]/skill.md`
Don't edit skill files here, just identify clearly what needs to change and where

**Memory-worthy** → Write to `~/.claude/projects/-Users-alexanderburger/memory/` — always ask before saving

### Step 4: Confirm

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
