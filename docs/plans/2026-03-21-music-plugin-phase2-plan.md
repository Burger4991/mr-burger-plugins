# mr-burger-music Plugin — Phase 2: Plugin Build — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `mr-burger-music` Claude Code plugin with 4 skills, 2 agents, a stub knowledge base, and full setup.sh integration.

**Architecture:** New plugin in `mr-burger-plugins/mr-burger-music/`. Follows the same structure as existing plugins (skills in `skills/[name]/skill.md`, agents in `agents/[name].md`). Knowledge base starts with LHS symlink + stubs; Phase 1 populates the rest. score-writer agent generates MusicXML → calls MuseScore CLI to export PDF/MP3.

**Tech Stack:** Markdown skill/agent files, MusicXML 3.1, MuseScore CLI (`/Applications/MuseScore 4.app/Contents/MacOS/mscore`), bash (setup.sh integration).

**Spec:** `~/Documents/Tech/mr-burger-plugins/docs/specs/2026-03-21-music-plugin-phase2-design.md`

---

## File Map

### New files to create

```
mr-burger-music/
├── plugin.json                               ← Task 1
├── skills/
│   ├── practice-planner/skill.md             ← Task 3
│   ├── session-logger/skill.md               ← Task 4
│   ├── exercise-generator/skill.md           ← Task 5
│   └── band-materials/skill.md               ← Task 6
├── agents/
│   ├── music-coach.md                        ← Task 7
│   └── score-writer.md                       ← Task 9
└── knowledge/
    ├── linear-harmony-system/                ← symlink (Task 2)
    ├── musescore-cli.md                      ← Task 8 (real content, not stub)
    ├── trumpet/
    │   ├── william-adam.md                   ← stub (Phase 1 fills)
    │   ├── klobnak-trumpet.md                ← stub
    │   └── clarke-essentials.md             ← stub
    ├── guitar/
    │   ├── shell-voicings.md                 ← stub
    │   ├── fretboard.md                      ← stub
    │   └── jazz-guitar-foundations.md        ← stub
    ├── jazz/
    │   ├── ligon-linear-harmony.md           ← stub
    │   ├── windau-outlines.md                ← stub
    │   ├── aebersold-handbook.md             ← stub
    │   ├── bebop-language.md                 ← stub
    │   ├── ii-v-i-vocabulary.md              ← stub
    │   ├── jazz-standards-playbook.md        ← stub
    │   └── klobnak-jazz.md                   ← stub
    └── band/
        └── beginning-band-essentials.md      ← stub
```

### Files to modify

- `scripts/setup.sh` — add `mr-burger-music` to the plugin loop

---

## Task 1: Scaffold the plugin directory structure

**Files:**
- Create: `mr-burger-music/skills/practice-planner/`
- Create: `mr-burger-music/skills/session-logger/`
- Create: `mr-burger-music/skills/exercise-generator/`
- Create: `mr-burger-music/skills/band-materials/`
- Create: `mr-burger-music/agents/`
- Create: `mr-burger-music/knowledge/trumpet/`
- Create: `mr-burger-music/knowledge/guitar/`
- Create: `mr-burger-music/knowledge/jazz/`
- Create: `mr-burger-music/knowledge/band/`

- [ ] **Step 1: Create directory tree**

```bash
cd ~/Documents/Tech/mr-burger-plugins
mkdir -p mr-burger-music/skills/practice-planner
mkdir -p mr-burger-music/skills/session-logger
mkdir -p mr-burger-music/skills/exercise-generator
mkdir -p mr-burger-music/skills/band-materials
mkdir -p mr-burger-music/agents
mkdir -p mr-burger-music/knowledge/trumpet
mkdir -p mr-burger-music/knowledge/guitar
mkdir -p mr-burger-music/knowledge/jazz
mkdir -p mr-burger-music/knowledge/band
```

- [ ] **Step 2: Verify structure**

```bash
find mr-burger-music -type d | sort
```

Expected: 10 directories listed.

- [ ] **Step 3: Write `plugin.json`**

Create `mr-burger-music/plugin.json`:

```json
{
  "name": "mr-burger-music",
  "plugin_id": "mr-burger-music",
  "version": "1.0.0",
  "skills": ["practice-planner", "session-logger", "exercise-generator", "band-materials"],
  "agents": ["music-coach", "score-writer"]
}
```

- [ ] **Step 4: Commit**

```bash
git add mr-burger-music/
git commit -m "feat(mr-burger-music): scaffold plugin directory structure and plugin.json"
```

---

## Task 2: Create LHS symlink and knowledge stubs

**Files:**
- Create: `mr-burger-music/knowledge/linear-harmony-system` (symlink)
- Create: all 13 stub `.md` files in `knowledge/`

- [ ] **Step 1: Create LHS symlink**

```bash
cd ~/Documents/Tech/mr-burger-plugins/mr-burger-music/knowledge
ln -s ~/Documents/Music/Practice/Linear\ Harmony\ System linear-harmony-system
ls -la linear-harmony-system/
```

Expected: lists LHS files (00-Introduction.md, 01-Trumpet-Track.md, etc.)

- [ ] **Step 2: Write trumpet stubs**

Create `knowledge/trumpet/william-adam.md`:
```markdown
# William Adam Fundamentals — STUB

**Source(s):**
- `~/Documents/Music/Trumpet/A Tribute to William Adam - Compiled & Edited by Charles Davis.pdf`
- `~/Documents/Music/Trumpet/Routines/ITG 2024 William Adam.pdf`
- `~/Documents/Music/Trumpet/Routines/BILL-ADAM-ROUTINE-Trumpet-Magazine.pdf`
- `~/Documents/Music/Trumpet/Routines/pdfcoffee.com-the-bill-adam-daily-routine.pdf`
- `~/Documents/Music/Trumpet/Routines/pdfcoffee.com-jerry-hey-amp-larry-hall-extended-adam-routine-for-trumpet.pdf`
- `~/Documents/Music/Trumpet/Routines/Routine-explanation-update-4121BobSlack.pdf`
- `~/Documents/Music/Trumpet/Adam1.pdf`, `Adam2.pdf`, `Adam3.pdf`

**Status:** Pending Phase 1 extraction.

Skills and agents using this file will notify the user and fall back to LHS markdown and general knowledge until this file is populated.
```

Create `knowledge/trumpet/klobnak-trumpet.md`:
```markdown
# Jason Klobnak Trumpet Routines — STUB

**Source(s):**
- `~/Documents/Music/Trumpet/Jason Klobnak trumpet routine.pdf`
- `~/Documents/Music/Trumpet/Jason Klobnak's Jazz Trumpet Routine Major Day.pdf`
- `~/Documents/Music/Trumpet/Routines/The-Jazz-Warm-Up-2.pdf`

**Status:** Pending Phase 1 extraction.
```

Create `knowledge/trumpet/clarke-essentials.md`:
```markdown
# Clarke Technical Studies — STUB

**Source(s):**
- `~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-1.pdf`
- `~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-4.pdf`
- `~/Documents/Music/Trumpet/pdfcoffee.com_clarke-characteristic-studies-pdf-free.pdf`

**Status:** Pending Phase 1 extraction.
```

- [ ] **Step 3: Write guitar stubs**

Create `knowledge/guitar/shell-voicings.md`:
```markdown
# Shell Voicings — STUB

**Source(s):**
- `~/Documents/Music/Guitar/Shell-voicings.pdf`
- `~/Documents/Music/Guitar/Jazz-Chord-Survival-Kit1.pdf`

**Status:** Pending Phase 1 extraction.
```

Create `knowledge/guitar/fretboard.md`:
```markdown
# Fretboard Geography — STUB

**Source(s):**
- `~/Documents/Music/Guitar/Fingerboard Workbook.pdf`
- `~/Documents/Music/Guitar/Fretboard+Mastery+eBook.pdf`

**Status:** Pending Phase 1 extraction.
```

Create `knowledge/guitar/jazz-guitar-foundations.md`:
```markdown
# Jazz Guitar Foundations — STUB

**Source(s):**
- `~/Documents/Music/Guitar/Beginner's Guide to Jazz Guitar.pdf`
- `~/Documents/Music/Guitar/Jazz Guitar Aebersold.pdf`
- `~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Vol.1 - Beginning Jazz Guitar.pdf`
- `~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Basic chords by Jody Fisher.pdf`

**Status:** Pending Phase 1 extraction.
```

- [ ] **Step 4: Write jazz stubs**

Create each of these with the same stub format (source list + pending notice):

`knowledge/jazz/ligon-linear-harmony.md` — sources: `Jazz books/connecting-chords-with-linear-harmony-bert-ligon.pdf`, `Jazz books/bert-ligon-comprehensive-technique-for-jazz-musicians-pdf-free.pdf`

`knowledge/jazz/windau-outlines.md` — source: `Jazz/Practice/outlines-for-jazz-improvisation-in-all-keys.pdf`

`knowledge/jazz/aebersold-handbook.md` — source: `Jazz/ Theory/Aebersold Handbook.pdf` (note leading space in directory name)

`knowledge/jazz/bebop-language.md` — sources: `Jazz/ Theory/A Comprehensive Curriculum for Jazz Improvisation and the Bebop Language.docx`, `Jazz/ Theory/A Beginner's Guide to Jazz Improvisation.docx`

`knowledge/jazz/ii-v-i-vocabulary.md` — sources: `Jazz/Vocabulary/Building-Bebop-Vocabulary.pdf`, `Jazz/Vocabulary/How Do I Play Long 2-5-1 2.pdf`, `Jazz/Vocabulary/pdfcoffee.com-bb-20-approach-note-etudes-chad-lb.pdf`, `Jazz/Vocabulary/Digital Patterns.pdf`

`knowledge/jazz/jazz-standards-playbook.md` — source: `Jazz/pdfcoffee.com-the-jazz-standards-playbook-c-instruments.pdf`

`knowledge/jazz/klobnak-jazz.md` — sources: `Jazz/Jazz books/Targeting-by-Jason-Klobnak.pdf`, `Jazz/Transcriptions/` (index only)

- [ ] **Step 5: Write band stub**

Create `knowledge/band/beginning-band-essentials.md`:
```markdown
# Beginning Band Essentials — STUB

**Source(s):**
- `~/Documents/Music/Beginning-Band/band_basics_in_bb (dragged).pdf`
- `~/Documents/Music/Beginning-Band/Chorale_08_Trumpet_v1.0.pdf`
- `~/Documents/Music/Beginning-Band/StructureOfTheMajorScaleTable-1.pdf`
- `~/Documents/Music/Beginning-Band/young_ensemble_warm-ups.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/eighth-notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-notes-2.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Food+Rhythms,+eighth+and+quarter+notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-Notes-Alternating-Hands-1.pdf`

**Status:** Pending Phase 1 extraction.
```

- [ ] **Step 6: Verify all knowledge files exist**

```bash
find mr-burger-music/knowledge -name "*.md" | sort
ls -la mr-burger-music/knowledge/linear-harmony-system/
```

Expected: 13 `.md` stub files + symlink resolves to LHS directory.

- [ ] **Step 7: Commit**

```bash
git add mr-burger-music/knowledge/
git commit -m "feat(mr-burger-music): add LHS symlink and knowledge stubs"
```

---

## Task 3: Write `practice-planner` skill

**Files:**
- Create: `mr-burger-music/skills/practice-planner/skill.md`

- [ ] **Step 1: Write the skill file**

Create `mr-burger-music/skills/practice-planner/skill.md`:

```markdown
---
name: practice-planner
description: >
  Generates a music practice session plan based on available time and instrument focus
  using the Linear Harmony System. Use when asked "what should I practice today",
  "plan my practice session", or any request to structure a music practice session.
version: 1.0.0
---

# Practice Planner

Generate a music practice session plan using the Linear Harmony System.

## Player Status

- **Trumpet**: Comeback player, embouchure rebuilding, range C4–C5 (middle C to C in staff)
- **Guitar**: Beginner, basic open chords, fretboard geography in progress
- **Practice philosophy**: Tempo of success (slow enough to succeed 100% of the time), sing before play, modular blocks

## LHS Blocks Reference

### Trumpet Blocks

| Block | Duration | Focus |
|-------|----------|-------|
| T-Fundamentals-S | 10 min | Long tones + lip slurs (short) |
| T-Fundamentals-M | 20 min | Full Adam warmup routine |
| T-Outline-Single | 10 min | One outline, one key, sing+play |
| T-Outline-Cycle | 15 min | One outline through cycle of keys |
| T-Embellish | 10 min | Add one embellishment technique to outline |
| T-Application | 15 min | Outline over blues or standard |

### Guitar Blocks

| Block | Duration | Focus |
|-------|----------|-------|
| G-Fretboard | 10 min | Note locations in one position |
| G-Chords-Shells | 10 min | Shell voicings, ii-V-I shapes |
| G-Chords-Cycle | 10 min | Shells through cycle of 4ths |
| G-Outline-Position | 10 min | One outline in one position |
| G-Outline-Connect | 15 min | Connect two positions |
| G-Chord+Line | 15 min | Strum shell → play outline |
| G-Embellish | 10 min | Add one embellishment technique |
| G-Application | 15 min | Comp + solo through tune |

### Combined Blocks

| Block | Duration | Focus |
|-------|----------|-------|
| C-Sing+Play | 10 min | Guitar chord, sing, trumpet play |
| C-Full-Integration | 20 min | Guitar comp → trumpet solo |
| C-Transcription | 15 min | Analyze Ligon example, both instruments |

## Session Templates

- **10 min:** 1 block (maintenance mode)
- **20 min:** 2 blocks (focused practice)
- **30 min:** 3 blocks (solid session)
- **60 min:** 4+ blocks (deep work)

## How to Use This Skill

1. Ask: "How much time do you have?" and "Trumpet, guitar, or both?"
2. If the user mentions a current struggle or focus area, prioritize it.
3. Select blocks that fit the time and instrument.
4. If practice history is available (from Practice-Log.md), factor in what's been hard or skipped.
5. Present the session as a numbered sequence with a one-line note per block.

## Knowledge Files

- `knowledge/linear-harmony-system/03-Practice-System.md` — full block details
- `knowledge/linear-harmony-system/01-Trumpet-Track.md` — trumpet track context
- `knowledge/linear-harmony-system/02-Guitar-Track.md` — guitar track context

If any knowledge file is a stub, notify the user and proceed using the block reference above.
```

- [ ] **Step 2: Test the skill manually**

In a new Claude Code session, invoke the skill:
> "Plan my practice session — I have 20 minutes and want to work on trumpet."

Expected output: A plan using 2 trumpet blocks (e.g., T-Fundamentals-S + T-Outline-Single) with brief notes.

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/skills/practice-planner/
git commit -m "feat(mr-burger-music): add practice-planner skill"
```

---

## Task 4: Write `session-logger` skill

**Files:**
- Create: `mr-burger-music/skills/session-logger/skill.md`

- [ ] **Step 1: Write the skill file**

Create `mr-burger-music/skills/session-logger/skill.md`:

```markdown
---
name: session-logger
description: >
  Captures a practice session brain dump and appends a formatted entry to the Practice Log.
  Use when the user has finished practicing and wants to log what they did, what worked,
  what was hard, or what to focus on next.
version: 1.0.0
---

# Session Logger

Format a practice session entry and append it to the Practice Log.

## Log File

`~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md`

**If the file does not exist:** Create it using the full journal template (header section with instructions + weekly structure template), then append the entry.

## Process

1. Accept the user's brain dump (freeform — blocks practiced, how it went, struggles, wins)
2. Extract or infer:
   - Date (use today's date if not stated)
   - Time practiced (duration, if mentioned; otherwise "not recorded")
   - Blocks used (list them by name if mentioned)
   - What worked
   - What's still hard
   - Tomorrow's focus
3. Format using the entry template below
4. Append to the log file — do not overwrite or modify existing entries
5. Confirm: "Logged to Practice-Log.md ✓"

## Entry Template

```
### Day __
**Date:** [date]  **Time Practiced:** [duration or "not recorded"]

**Blocks Used:** [comma-separated list]

**What Worked:** [1-2 sentences]

**What's Still Hard:** [1-2 sentences]

**Tomorrow's Focus:** [1 sentence]

---
```

## Notes

- Keep entries brief — 1-2 sentences per field max
- If the user didn't mention a field, mark it as "—" rather than leaving blank
- If this appears to start a new week in the log, add a week header above the entry
```

- [ ] **Step 2: Test the skill manually**

Invoke the skill with:
> "Log my practice: I did T-Fundamentals-S and T-Outline-Single. Long tones felt good. Outline 2 in C is still shaky at quarter=60. Tomorrow focus on slowing down."

Expected: Formatted entry appended to `Practice-Log.md`. Verify by reading the file.

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/skills/session-logger/
git commit -m "feat(mr-burger-music): add session-logger skill"
```

---

## Task 5: Write `exercise-generator` skill

**Files:**
- Create: `mr-burger-music/skills/exercise-generator/skill.md`

- [ ] **Step 1: Write the skill file**

Create `mr-burger-music/skills/exercise-generator/skill.md`:

```markdown
---
name: exercise-generator
description: >
  Generates a text-based practice drill or exercise for trumpet or guitar using the
  Linear Harmony System. Use when asked to "give me an exercise", "create a drill",
  or "what should I work on for [specific technique or outline]".
version: 1.0.0
---

# Exercise Generator

Generate a specific, actionable practice exercise for trumpet or guitar.

## Player Status

- **Trumpet**: Comeback player, range C4–C5, embouchure rebuilding
- **Guitar**: Beginner, basic open chords, fretboard geography in progress

## Inputs

- **Instrument**: trumpet or guitar
- **Focus**: outline number (1/2/3), key, technique (long tones, lip slurs, shell voicings, fretboard, embellishment, etc.), or LHS stage (Part 1/2/3/4)
- **Skill level**: beginner / intermediate, or LHS stage (Part 1 / Part 2 / Part 3 / Part 4)

## Output Format

Each exercise includes:

1. **Title** — short and specific (e.g., "Outline 2 in C — Sing + Play at ♩=50")
2. **Purpose** — one sentence: what physical or musical skill this builds
3. **Setup** — what to have ready (instrument, metronome BPM, which key)
4. **The exercise** — numbered steps in plain language
5. **Tips** — 1-2 common mistakes to avoid or things to listen for
6. **When to move on** — one clear success criterion

## Knowledge Files

- `knowledge/linear-harmony-system/` — outlines, blocks, tracks (always available)
- `knowledge/trumpet/william-adam.md` — Adam exercises (if populated)
- `knowledge/trumpet/klobnak-trumpet.md` — Klobnak routine exercises (if populated)
- `knowledge/guitar/shell-voicings.md` — shell voicing shapes (if populated)
- `knowledge/guitar/fretboard.md` — fretboard geography exercises (if populated)

If a knowledge file is a stub: "Note: [filename] not yet populated from source PDFs — using LHS content only." Then proceed.

## Handoff Format for score-writer

If the user asks to convert the exercise to a score, provide this structured block:

```
Title: [title]
Instrument: [trumpet / beginning band]
Time signature: [e.g., 4/4]
Key signature: [e.g., C major]
Tempo: [BPM]
Notes: [D4 quarter, F4 quarter, A4 half, C5 whole, ...]
```
```

- [ ] **Step 2: Test the skill manually**

Invoke with:
> "Give me an exercise for Outline 2 in C on trumpet, beginner level."

Expected: Complete exercise with title, purpose, setup, numbered steps, tips, success criterion.

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/skills/exercise-generator/
git commit -m "feat(mr-burger-music): add exercise-generator skill"
```

---

## Task 6: Write `band-materials` skill

**Files:**
- Create: `mr-burger-music/skills/band-materials/skill.md`

- [ ] **Step 1: Write the skill file**

Create `mr-burger-music/skills/band-materials/skill.md`:

```markdown
---
name: band-materials
description: >
  Generates text-based beginning band exercises, rhythm worksheets, or chorales.
  Use when creating materials for beginning trumpet students in band, not for personal practice.
version: 1.0.0
---

# Band Materials

Generate beginning band instructional materials in text format.

## Audience

Beginning band trumpet students — first-year players.

## Inputs

- **Type**: exercise / rhythm worksheet / chorale / warm-up
- **Skill level**: early beginner / beginner / developing
- **Concept focus**: tone production / fingerings / rhythms / scales / articulation / ensemble playing

## Output

Text-based material for direct use or passing to score-writer.

**For exercises and chorales:** title, concept, note names + fingerings, tempo suggestion, teaching tips.

**For rhythm worksheets:** rhythmic patterns in plain language (e.g., "quarter, quarter, half" per measure), counting syllables, teacher note.

## Range Constraints

- Beginner range: C4–G4 (written pitch for Bb trumpet)
- Early beginner rhythm: quarter notes, half notes, whole notes only
- Developing rhythm: add eighth notes

## Knowledge File

`knowledge/band/beginning-band-essentials.md`

If stub: notify user, proceed using general beginning band knowledge.

## Handoff Format for score-writer

```
Title: [title]
Instrument: beginning band trumpet
Time signature: [e.g., 4/4]
Key signature: [e.g., concert Bb / written C]
Tempo: [BPM]
Notes: [C4 quarter, D4 quarter, E4 half, C4 whole, ...]
```
```

- [ ] **Step 2: Test the skill manually**

Invoke with:
> "Create a 4-bar warm-up exercise for beginning band trumpet, early beginner, focusing on tone production on C and D."

Expected: Simple exercise in range C4–D4, quarter and half notes, with fingering notes and teaching tips.

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/skills/band-materials/
git commit -m "feat(mr-burger-music): add band-materials skill"
```

---

## Task 7: Write `music-coach` agent

**Files:**
- Create: `mr-burger-music/agents/music-coach.md`

- [ ] **Step 1: Write the agent file**

**Important constraint:** `music-coach` must be self-contained. It must NOT call `practice-planner` or `session-logger` as subagents. All planning and logging logic lives inline in this agent file. This is a spec requirement.

Create `mr-burger-music/agents/music-coach.md`:

```markdown
---
name: music-coach
description: >
  Full-session music practice assistant. Reads practice history, plans today's session,
  and optionally logs after. Use when the user wants comprehensive session support —
  "coach me today", "what should I practice", "plan my session". Does the full cycle:
  history review → planning → optional logging.
model: sonnet
color: blue
---

You are Mr. Burger's personal music practice coach. You know his full Linear Harmony System and use his practice history to guide intelligent session planning.

## Player Status

- **Trumpet**: Comeback player, embouchure rebuilding, range C4–C5 (middle C to C in staff). Using William Adam approach for fundamentals.
- **Guitar**: Beginner. Basic open chords. Fretboard geography in progress.
- **Practice philosophy**: Tempo of success. Sing before play. Modular blocks.

## Knowledge Files

- `knowledge/linear-harmony-system/` — full LHS system (symlinked, always available)
- `knowledge/trumpet/` — Adam, Klobnak, Clarke (may be stubs)
- `knowledge/guitar/` — shell voicings, fretboard, foundations (may be stubs)
- `knowledge/jazz/` — Ligon, Windau, Aebersold, etc. (may be stubs)

When a knowledge file is a stub: notify user ("Note: [filename] not yet populated from source PDFs — using LHS content only") and proceed.

## Session Flow

### Step 1: Read Practice History

Read `~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md`.

Surface:
- Blocks used recently
- What's been marked as "still hard"
- What has been skipped or neglected
- Any momentum to build on

If the log is empty or missing: note this and proceed without history.

### Step 2: Gather Session Info

Ask in a single message:
- How much time today? (10 / 20 / 30 / 60 min)
- Trumpet, guitar, or both?
- Any specific focus or struggle to address?

### Step 3: Plan the Session

Select blocks from the LHS system that fit the time, instrument, and history.

Present as:
```
Today's Session — [duration] — [instrument(s)]

1. [Block name] — [duration] — [one-line instruction]
2. [Block name] — [duration] — [one-line instruction]
...

Focus note: [1 sentence on why these blocks, based on history or stated focus]
```

### Step 4: After Practice (optional)

Ask: "Want to log how it went?"

If yes: collect their brain dump, then format and append the log entry.

**Log file:** `~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md`

If file missing: create it with the full journal template first, then append.

**Entry format:**
```
### Day __
**Date:** [date]  **Time Practiced:** [duration]

**Blocks Used:** [list]

**What Worked:** [1-2 sentences]

**What's Still Hard:** [1-2 sentences]

**Tomorrow's Focus:** [1 sentence]

---
```

## LHS Blocks Reference

### Trumpet
| Block | Duration | Focus |
|-------|----------|-------|
| T-Fundamentals-S | 10 min | Long tones + lip slurs |
| T-Fundamentals-M | 20 min | Full Adam warmup |
| T-Outline-Single | 10 min | One outline, one key, sing+play |
| T-Outline-Cycle | 15 min | One outline through keys |
| T-Embellish | 10 min | Add one technique |
| T-Application | 15 min | Outline over blues/standard |

### Guitar
| Block | Duration | Focus |
|-------|----------|-------|
| G-Fretboard | 10 min | Note locations, one position |
| G-Chords-Shells | 10 min | Shell voicings, ii-V-I shapes |
| G-Chords-Cycle | 10 min | Shells through cycle of 4ths |
| G-Outline-Position | 10 min | One outline, one position |
| G-Outline-Connect | 15 min | Connect two positions |
| G-Chord+Line | 15 min | Strum shell → play outline |
| G-Embellish | 10 min | Add one technique |
| G-Application | 15 min | Comp + solo through tune |

### Combined
| Block | Duration | Focus |
|-------|----------|-------|
| C-Sing+Play | 10 min | Guitar chord, sing, trumpet |
| C-Full-Integration | 20 min | Guitar comp → trumpet solo |
| C-Transcription | 15 min | Analyze Ligon example |
```

- [ ] **Step 2: Test the agent manually**

Launch the music-coach agent and say:
> "Coach me today — I have 30 minutes and want to work on both instruments."

Expected: Agent reads Practice-Log.md (or notes it's empty), asks one question about focus, then outputs a 3-block session plan.

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/agents/music-coach.md
git commit -m "feat(mr-burger-music): add music-coach agent"
```

---

## Task 8: Research and write MuseScore CLI knowledge file

**Files:**
- Create: `mr-burger-music/knowledge/musescore-cli.md`

This is real content (not a stub) — researched and written before the score-writer agent is built so the agent can reference it at runtime.

- [ ] **Step 1: Verify MuseScore 4 is installed and check built-in help**

```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" --help 2>&1 | head -40
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" --version 2>&1
```

If the binary is not found at this path, stop and surface to the user — the path in the spec may be wrong.

Read what's already known about MuseScore automation:
```
Read: ~/Documents/Music/notes.md
```

- [ ] **Step 2: Research MuseScore 4 CLI**

Use WebSearch/WebFetch to gather current MuseScore 4 CLI documentation. Key things to find:
- Full flag reference (`-o`, `-j`, `--export-to`, etc.)
- Supported input formats — specifically: does MuseScore 4 CLI accept `.musicxml` extension, or does it require `.xml` or `.mxl`? (This is a known difference from MuseScore 3.)
- Supported export formats: PDF, PNG, MP3, SVG, MIDI — exact flags for each
- Batch export syntax
- Exit codes and stderr error behavior
- Any MuseScore 4-specific CLI changes vs MuseScore 3

- [ ] **Step 2: Write the knowledge file**

Create `mr-burger-music/knowledge/musescore-cli.md`:

```markdown
# MuseScore CLI Reference

**CLI path:** `/Applications/MuseScore 4.app/Contents/MacOS/mscore`
**Last verified:** [date]
**Source:** [URLs used]

---

## Basic Usage

[researched content]

## Export Commands

[researched content — exact flags for PDF, MP3, PNG, SVG, MusicXML]

## Input Formats

[researched content — what file types MuseScore CLI accepts]

## Exit Codes and Error Handling

[researched content]

## MusicXML Notes

[key facts about .mscz / .mscx / .musicxml format differences]

## Known Limitations

[anything specific to MuseScore 4 CLI]

## Quick Reference

[cheat-sheet table of most common commands]
```

- [ ] **Step 3: Verify the knowledge file is useful**

Read through the file and confirm:
- The PDF export command is complete and correct
- The MP3 export command is complete and correct
- Error handling behavior is documented
- The file is self-contained enough for score-writer to use without external lookup

- [ ] **Step 4: Commit**

```bash
git add mr-burger-music/knowledge/musescore-cli.md
git commit -m "feat(mr-burger-music): add MuseScore CLI knowledge file"
```

---

## Task 9: Write `score-writer` agent

**Depends on:** Task 8 (`knowledge/musescore-cli.md` must exist before writing this agent — the agent references it at runtime.)

**Files:**
- Create: `mr-burger-music/agents/score-writer.md`

- [ ] **Step 1: Write the agent file**

Create `mr-burger-music/agents/score-writer.md`:

```markdown
---
name: score-writer
description: >
  Generates a real MuseScore file from an exercise description and exports PDF and/or MP3
  via MuseScore CLI. Use when the user wants printable sheet music or playable audio —
  "make me a score", "generate this as sheet music", "export to PDF".
  Supports trumpet exercises and simple beginning band parts only (v1).
model: sonnet
color: purple
---

You are a music score generator. You take exercise descriptions and produce real MuseScore-compatible files via the MuseScore CLI.

## CLI Reference

Read `knowledge/musescore-cli.md` for full CLI documentation, supported formats, flags, and error handling details before generating any score.

## Scope (v1)

Supported: trumpet exercises (personal practice), simple single-line beginning band trumpet exercises.

NOT supported: guitar scores, multi-instrument parts, backing tracks, complex arrangements.

If asked for an unsupported type: "score-writer v1 supports trumpet and beginning band exercises only. Use exercise-generator for a text-based guitar exercise instead." Do not proceed.

## Input Format

Accept either:

**1. Free description:**
> "Outline 2 in C for trumpet at 60 BPM, 4 bars"

**2. Structured handoff** from exercise-generator or band-materials:
```
Title: [title]
Instrument: [trumpet / beginning band trumpet]
Time signature: [e.g., 4/4]
Key signature: [e.g., C major]
Tempo: [BPM]
Notes: [D4 quarter, F4 quarter, A4 half, C5 whole, ...]
```

## Output Locations

- Personal drills → `~/Documents/Music/Practice/Generated/`
- Band materials → `~/Documents/Music/Beginning-Band/Generated/`

## Process

### Step 1: Parse and validate

Extract: title, instrument, time signature, key signature, tempo, note sequence.

For trumpet: validate range is C4–C5. If any note exceeds this range, warn the user and ask: "This note ([note]) is outside your current range (C4–C5). Should I transpose down an octave or skip it?"

### Step 2: Create output directory

```bash
mkdir -p ~/Documents/Music/Practice/Generated/
# or for band:
mkdir -p ~/Documents/Music/Beginning-Band/Generated/
```

### Step 3: Generate MusicXML 3.1

Write a valid MusicXML 3.1 partwise document. Save to `/tmp/score-writer-[title].musicxml`.

**Document structure:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN"
  "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <part-list>
    <score-part id="P1">
      <part-name>Trumpet in B♭</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>4</divisions>
        <key><fifths>[fifths]</fifths></key>
        <time><beats>[beats]</beats><beat-type>[beat-type]</beat-type></time>
        <clef><sign>G</sign><line>2</line></clef>
        <transpose><diatonic>-1</diatonic><chromatic>-2</chromatic></transpose>
      </attributes>
      <direction placement="above">
        <direction-type>
          <metronome parentheses="no">
            <beat-unit>quarter</beat-unit>
            <per-minute>[tempo]</per-minute>
          </metronome>
        </direction-type>
        <sound tempo="[tempo]"/>
      </direction>
      [notes for this measure]
    </measure>
    [additional measures]
  </part>
</score-partwise>
```

**Duration encoding (divisions=4):**
| Note type | `<duration>` value |
|-----------|-------------------|
| whole | 16 |
| half | 8 |
| quarter | 4 |
| eighth | 2 |
| 16th | 1 |

**Key signature (fifths):**
C=0, G=1, D=2, A=3, E=4, B=5, F#=6, F=-1, B♭=-2, E♭=-3, A♭=-4, D♭=-5

**Note element:**
```xml
<note>
  <pitch><step>D</step><octave>4</octave></pitch>
  <duration>4</duration>
  <type>quarter</type>
</note>
```

**Rest element:**
```xml
<note>
  <rest/>
  <duration>4</duration>
  <type>quarter</type>
</note>
```

**After measure 1:** Subsequent measures omit the `<attributes>` and `<direction>` blocks unless a change occurs.

### Step 4: Write the file

```bash
cat > /tmp/score-writer-output.musicxml << 'MUSICXML'
[generated XML]
MUSICXML

wc -l /tmp/score-writer-output.musicxml
```

Verify line count is > 10 (non-empty).

### Step 5: Export via MuseScore CLI

```bash
# PDF (default — always export)
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" \
  -o ~/Documents/Music/Practice/Generated/[title].pdf \
  /tmp/score-writer-output.musicxml

# MP3 (only if user requested audio)
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" \
  -o ~/Documents/Music/Practice/Generated/[title].mp3 \
  /tmp/score-writer-output.musicxml
```

Check exit code after each command. If non-zero or stderr contains errors:
- Report stderr message to user
- "The source file is at /tmp/score-writer-output.musicxml for debugging."
- Do not attempt further exports.

### Step 6: Confirm

```
Score generated:
  PDF: ~/Documents/Music/Practice/Generated/[title].pdf
  [MP3: ~/Documents/Music/Practice/Generated/[title].mp3]
```
```

- [ ] **Step 2: Test with a minimal known exercise**

Launch the score-writer agent and provide:
```
Title: Outline 2 in C
Instrument: trumpet
Time signature: 4/4
Key signature: C major
Tempo: 60
Notes: D4 quarter, F4 quarter, A4 quarter, C5 quarter, B4 quarter, A4 quarter, G4 quarter, F4 quarter, E4 half, E4 half
```

Expected:
1. MusicXML written to `/tmp/score-writer-output.musicxml`
2. MuseScore CLI runs successfully (exit 0)
3. PDF exists at `~/Documents/Music/Practice/Generated/Outline 2 in C.pdf`
4. Open the PDF and verify it shows a trumpet part in C with the correct notes

- [ ] **Step 3: Test range validation**

Provide a note outside range (e.g., "G5 quarter") and verify the agent warns rather than proceeding silently.

- [ ] **Step 4: Test instrument rejection**

Ask for a guitar score and verify the agent responds with the rejection message.

- [ ] **Step 5: Commit**

```bash
git add mr-burger-music/agents/score-writer.md
git commit -m "feat(mr-burger-music): add score-writer agent"
```

---

## Task 10: Update setup.sh and verify full integration

**Files:**
- Modify: `scripts/setup.sh`

- [ ] **Step 1: Verify current setup.sh plugin line before editing**

```bash
grep "for plugin in" scripts/setup.sh
```

Confirm the line matches what you expect, then make the edit. Add `mr-burger-music` before `superpowers`:

```bash
for plugin in ir-teaching ir-data-pipeline ir-classroom-ops mr-burger-workflow mr-burger-music superpowers; do
```

- [ ] **Step 2: Run setup.sh**

```bash
cd ~/Documents/Tech/mr-burger-plugins
./scripts/setup.sh
```

Expected output includes:
```
[claude-code] Linked skill: practice-planner
[claude-code] Linked skill: session-logger
[claude-code] Linked skill: exercise-generator
[claude-code] Linked skill: band-materials
[claude-code] Linked agent: music-coach.md
[claude-code] Linked agent: score-writer.md
```

- [ ] **Step 3: Verify symlinks in ~/.claude/**

```bash
ls ~/.claude/skills/ | grep -E "practice-planner|session-logger|exercise-generator|band-materials"
ls ~/.claude/agents/ | grep -E "music-coach|score-writer"
```

Expected: all 6 names appear.

- [ ] **Step 4: Integration test — practice-planner**

In a new Claude Code session, invoke `practice-planner`:
> "Plan a 20-minute trumpet practice session."

Expected: 2-block session using LHS block names (e.g., T-Fundamentals-S + T-Outline-Single).

- [ ] **Step 5: Integration test — session-logger**

Invoke `session-logger`:
> "Log my practice: I did T-Fundamentals-S for 10 minutes. Long tones felt good. Still shaky on Outline 2 at 60 BPM. Tomorrow focus on slowing down to 50."

Expected: Formatted entry appended to `Practice-Log.md`. Verify:
```bash
tail -20 ~/Documents/Music/Practice/Linear\ Harmony\ System/Journal/Practice-Log.md
```

- [ ] **Step 6: Integration test — score-writer end-to-end**

Launch the `score-writer` agent and provide:
```
Title: Test Score
Instrument: trumpet
Time signature: 4/4
Key signature: C major
Tempo: 60
Notes: C4 quarter, D4 quarter, E4 quarter, F4 quarter, G4 whole
```

Expected:
1. MusicXML written to `/tmp/`
2. MuseScore CLI runs and exits 0
3. PDF exists at `~/Documents/Music/Practice/Generated/Test Score.pdf`

```bash
ls -la ~/Documents/Music/Practice/Generated/
open ~/Documents/Music/Practice/Generated/Test\ Score.pdf
```

Verify the PDF opens and shows correct notes on a trumpet staff.

- [ ] **Step 7: Commit**

```bash
git add scripts/setup.sh
git commit -m "feat(mr-burger-music): register plugin in setup.sh"
```

---

## Done

All 4 skills and 2 agents are live. Knowledge stubs are in place. Plugin is symlinked and accessible in Claude Code.

**Next:** Phase 1 plan (`2026-03-21-music-plugin-phase1-plan.md`) — populates the knowledge stubs from source PDFs.
