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
4. Read `knowledge/linear-harmony-system/Journal/Current-Stage.md` (if missing, default to Part 1 for all instruments) and limit block selection to the current LHS Part for each instrument.
5. If practice history is available (from Practice-Log.md), factor in what's been hard or skipped.
6. Present the session as a numbered sequence with a one-line note per block.

## Knowledge Files

- `knowledge/linear-harmony-system/03-Practice-System.md` — full block details
- `knowledge/linear-harmony-system/01-Trumpet-Track.md` — trumpet track context
- `knowledge/linear-harmony-system/02-Guitar-Track.md` — guitar track context

If any knowledge file is a stub, notify the user and proceed using the block reference above.
