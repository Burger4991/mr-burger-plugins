# mr-burger-music Plugin — Phase 2: Plugin Build
**Date:** 2026-03-21
**Status:** Approved
**Spec:** `~/Documents/Tech/mr-burger-plugins/docs/specs/2026-03-21-music-plugin-phase2-design.md`
**Implementation plan:** `~/Documents/Tech/mr-burger-plugins/docs/plans/2026-03-21-music-plugin-phase2-plan.md`
**Depends on:** Phase 1 (knowledge base extraction) — v1 uses LHS markdown as initial knowledge base; Phase 1 output drops into the same structure when complete.

---

## Overview

A new Claude Code plugin (`mr-burger-music`) in the `mr-burger-plugins` monorepo. Serves two audiences: Mr. Burger as a personal musician (trumpet/guitar, Linear Harmony System) and Mr. Burger as a beginning band director. Provides three core functions: practice planning, music material generation, and session logging/reflection.

---

## Plugin Location

`~/Documents/Tech/mr-burger-plugins/mr-burger-music/`

Follows the same structure as `ir-teaching`, `ir-data-pipeline`, and `mr-burger-workflow`.

---

## `plugin.json`

Follows the schema used by other plugins in the monorepo. Key fields:

```json
{
  "name": "mr-burger-music",
  "plugin_id": "mr-burger-music",
  "version": "1.0.0",
  "skills": ["practice-planner", "session-logger", "exercise-generator", "band-materials"],
  "agents": ["music-coach", "score-writer"]
}
```

---

## Plugin Structure

```
mr-burger-music/
├── plugin.json
├── skills/
│   ├── practice-planner/skill.md
│   ├── session-logger/skill.md
│   ├── exercise-generator/skill.md
│   └── band-materials/skill.md
├── agents/
│   ├── music-coach.md
│   └── score-writer.md
└── knowledge/
    ├── linear-harmony-system/     ← symlink to ~/Documents/Music/Practice/Linear Harmony System/
    ├── trumpet/
    │   ├── william-adam.md        ← placeholder (Phase 1 fills this)
    │   ├── klobnak-trumpet.md     ← placeholder (Phase 1 fills this)
    │   └── clarke-essentials.md  ← placeholder (Phase 1 fills this)
    ├── guitar/
    │   ├── shell-voicings.md      ← placeholder (Phase 1 fills this)
    │   ├── fretboard.md           ← placeholder (Phase 1 fills this)
    │   └── jazz-guitar-foundations.md ← placeholder (Phase 1 fills this)
    ├── jazz/
    │   ├── ligon-linear-harmony.md     ← placeholder (Phase 1 fills this)
    │   ├── windau-outlines.md          ← placeholder (Phase 1 fills this)
    │   ├── aebersold-handbook.md       ← placeholder (Phase 1 fills this)
    │   ├── bebop-language.md           ← placeholder (Phase 1 fills this)
    │   ├── ii-v-i-vocabulary.md        ← placeholder (Phase 1 fills this)
    │   ├── jazz-standards-playbook.md  ← placeholder (Phase 1 fills this)
    │   └── klobnak-jazz.md             ← placeholder (Phase 1 fills this)
    ├── band/
    │   └── beginning-band-essentials.md ← placeholder (Phase 1 fills this)
    └── musescore-cli.md                 ← real content (researched and written in Phase 2)
```

---

## Skills

### `practice-planner`

**Purpose:** Generate a practice session plan based on available time and current focus.

**Input:** Available time (10/20/30/60 min), instrument focus (trumpet/guitar/both), optional current priority.

**Output:** A structured session plan using LHS block names (e.g., T-Fundamentals-S, G-Chords-Shells), with brief instructions for each block. References knowledge base for block content.

**Context it knows:**
- All LHS blocks and their durations (from `linear-harmony-system/`)
- Current player status: trumpet comeback player, embouchure rebuilding, range limited to C in staff; guitar beginner, basic open chords, fretboard geography in progress
- Practice philosophy: tempo of success, sing before play, modular blocks

---

### `session-logger`

**Purpose:** Capture a practice session brain dump and append it to the Practice Log.

**Input:** Freeform brain dump — what was practiced, what worked, what was hard, what to focus on next.

**Output:** Formats the entry using the Practice Log template and appends to `~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md`.

**File-not-found behavior:** If `Practice-Log.md` does not exist, create it using the full journal template (header + weekly structure) before appending the entry.

**Template fields:**
- Date / Time Practiced
- Blocks Used
- What Worked
- What's Still Hard
- Tomorrow's Focus

---

### `exercise-generator`

**Purpose:** Generate a text-based drill or exercise for personal practice.

**Input:** Instrument (trumpet/guitar), LHS component (outline number 1–3, key, technique), skill level (beginner/intermediate, or LHS stage: Part 1/2/3/4).

**Output:** A complete exercise description — notes, fingerings if helpful, tempo, number of repetitions, tips. Text format. Not a score file.

**References:** `linear-harmony-system/`, trumpet or guitar knowledge files as appropriate.

---

### `band-materials`

**Purpose:** Generate beginning band exercises, rhythm worksheets, or chorale descriptions in text.

**Input:** Type (exercise/worksheet/chorale), skill level, concept focus (scales, rhythms, articulation, etc.).

**Output:** Text-based material ready to be used as-is or passed to `score-writer`. When passing to `score-writer`, the handoff format is structured plain text including: title, instrument, time signature, key signature, tempo (BPM), and note sequence (using letter names, octave numbers, and durations — e.g., "D4 quarter, F4 quarter, A4 half").

**References:** `knowledge/band/beginning-band-essentials.md`

---

## Agents

### `music-coach`

**Purpose:** Full-session assistant. Reads practice history, plans a session, optionally logs after.

**Flow:**
1. Read `Practice-Log.md` to surface recent patterns (what's been hard, what's improving, what's been skipped)
2. Ask about available time and instrument focus
3. Generate session plan (agent contains its own planning logic — does not call `practice-planner` as a subagent)
4. After session: capture and format log entry, append to `Practice-Log.md` (agent contains its own logging logic — does not call `session-logger` as a subagent)

**What it knows:** Full LHS system, player status, practice philosophy. Treats the log as the source of truth for where the player currently is.

**Stub fallback:** If any knowledge file is a stub, the agent notifies the user ("Note: [filename] has not yet been populated from source PDFs — using LHS system content only") and proceeds.

---

### `score-writer`

**Purpose:** Generate a printable/playable score from any exercise description. Exports PDF and/or MP3 via MuseScore.

**Flow:**
1. Receive exercise description (from user, `exercise-generator`, or `band-materials` handoff format)
2. Validate instrument — v1 supports trumpet and simple single-line band exercises only. If guitar or unsupported instrument is requested, respond: "score-writer v1 supports trumpet and beginning band exercises only. Use exercise-generator for a text-based guitar exercise instead." Do not proceed.
3. Generate standard MusicXML 3.1 (`partwise` root element, standard note/pitch/duration encoding)
4. Write `.musicxml` file to a temp path
5. Call MuseScore CLI to export to target format
6. Create output directory if it does not exist
7. Return file path(s) to user

**CLI syntax:**
```bash
# PDF export
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.pdf input.musicxml

# MP3 export
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.mp3 input.musicxml
```
Error detection: exit code 0 = success; non-zero exit code or stderr output = failure. On failure, report the stderr message to the user and retain the `.musicxml` source file for debugging.

**MusicXML format:**
- Version: 3.1 (`partwise`)
- Pitch encoding: standard (`<step>`, `<octave>`, `<alter>`)
- Duration: divisions-based (set `<divisions>` to 4; quarter = 4, half = 8, whole = 16, eighth = 2)

**Output locations:**
- Personal drills → `~/Documents/Music/Practice/Generated/`
- Band materials → `~/Documents/Music/Beginning-Band/Generated/`
- Both directories created by the agent if they do not exist.

**Trumpet constraints (personal exercises):**
- Range limited to C4–C5 (middle C to C in staff — embouchure rebuilding)
- Tempos slow: ♩=40–80 depending on exercise type

**Input handoff format (from `band-materials` or `exercise-generator`):**
Structured plain text including: title, instrument, time signature, key signature, tempo (BPM), note sequence using letter names + octave numbers + durations (e.g., "D4 quarter, F4 quarter, A4 half").

**v1 scope limits:** Single-instrument parts only. No multi-part scores, no backing tracks, no complex arrangements, no guitar scores.

---

## Knowledge Base (v1 State)

Skills and agents read from `knowledge/` at runtime.

**Ready at launch (Phase 2):**
- `linear-harmony-system/` — symlinked to existing LHS docs. Full design document, trumpet track, guitar track, practice system, all reference files, journal.

**Placeholders (filled by Phase 1):**
- All other knowledge files contain a stub noting the source PDFs they will be distilled from.
- Stub fallback behavior: skills and agents notify the user when a stub is encountered ("Note: [filename] has not yet been populated — using LHS system content only") and proceed using LHS markdown and general jazz/music knowledge. They do not fail silently or refuse the request.

---

## Output Locations

| Type | Location |
|------|----------|
| Practice Log | `~/Documents/Music/Practice/Linear Harmony System/Journal/Practice-Log.md` |
| Generated personal scores | `~/Documents/Music/Practice/Generated/` |
| Generated band materials (scores) | `~/Documents/Music/Beginning-Band/Generated/` |

---

## Setup Integration

Plugin registered in `mr-burger-plugins/` monorepo. Symlinks created via `setup.sh` to:
- `~/.claude/skills/` (4 skills)
- `~/.claude/agents/` (2 agents)

---

## What's Out of Scope (v1)

- Multi-instrument scores or full arrangements
- Play-along backing tracks
- Audio analysis or transcription tools
- Guitar-specific score generation (trumpet only for v1 score-writer)
- Integration with external music apps beyond MuseScore
