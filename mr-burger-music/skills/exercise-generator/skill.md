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
