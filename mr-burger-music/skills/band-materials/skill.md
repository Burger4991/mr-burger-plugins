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
