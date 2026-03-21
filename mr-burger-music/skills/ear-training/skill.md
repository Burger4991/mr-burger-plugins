---
name: ear-training
description: >
  Guides a sing-before-play ear training exercise using the LHS Ear Training Protocol.
  Use when asked to "work on ear training", "practice singing outlines", "do ear training",
  or when the user wants to strengthen the connection between ear and instrument.
version: 1.0.0
---

# Ear Training

Guide an ear training exercise using the LHS Ear Training Protocol.

## Core Rule

**If you can't sing it, you can't play it with intention.** Always open with this.

## Knowledge File

Read `knowledge/linear-harmony-system/04-Reference/Ear-Training-Protocol.md` for the full protocol before generating any exercise.

If the file is missing: proceed using the core rule and the protocol structure below.

## Player Status

- **Trumpet**: Comeback player, range C4–C5, embouchure rebuilding
- **Guitar**: Beginner, shell voicings in progress

## Inputs

- **Instrument**: trumpet, guitar, or voice-only
- **Outline/focus**: which outline or interval to work on (default: Outline 1)
- **Level**: Level 1 (basic sing-then-play) / Level 2 (sing with chord) / Level 3 (full audiation)

## Output Format

1. **Exercise title** — specific and brief (e.g., "Outline 1 in C — Level 1 Sing-Then-Play")
2. **Core rule reminder** — one line
3. **Protocol level** — which level this targets and why
4. **Setup** — metronome BPM, which outline/key, what to have ready
5. **Steps** — numbered, plain language, following the protocol from the knowledge file
6. **Success criterion** — one clear signal that it's working (e.g., "You played the note you intended before your fingers moved")

## Notes

- Default to Level 1 unless the user specifies otherwise or history shows Level 1 is solid
- Voice-only exercises (no instrument) are valid and useful for beginners
- If the user says "just sing it" — that IS the exercise, not a warm-up
