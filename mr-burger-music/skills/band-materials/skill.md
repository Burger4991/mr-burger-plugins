---
name: band-materials
description: >
  Generates text-based beginning band exercises, rhythm worksheets, chorales,
  jazz leadsheets, and theory worksheets.
  Use when creating materials for beginning or developing trumpet students in band,
  not for personal practice.
version: 2.0.0
---

# Band Materials

Generate beginning band instructional materials in text format.

## Audience

Beginning band and developing trumpet students — first and second year players.

## Inputs

- **Type**: exercise / rhythm worksheet / chorale / warm-up / jazz leadsheet / theory worksheet
- **Skill level**: early beginner / beginner / developing
- **Concept focus** (varies by type — see below)

---

## Exercises, Chorales, Warm-ups

**Concept focus:** tone production / fingerings / rhythms / scales / articulation / ensemble playing

**Output:** title, concept, note names + fingerings, tempo suggestion, teaching tips.

### Range Constraints — Written pitch for Bb trumpet

| Level | Range | Rhythm |
|-------|-------|--------|
| Early beginner | C4–G4 | Whole, half notes only |
| Beginner | C4–C5 | Add quarter notes |
| Developing | C4–F5 | Add eighth notes |

### Handoff Format for score-writer

```
Title: [title]
Instrument: beginning band trumpet
Time signature: [e.g., 4/4]
Key signature: [e.g., concert Bb / written C]
Tempo: [BPM]
Notes: [C4 quarter, D4 quarter, E4 half, C4 whole, ...]
```

---

## Rhythm Worksheets

**Output:** rhythmic patterns in plain language (e.g., "quarter, quarter, half" per measure), counting syllables, teacher note.

No pitch content — rhythm only.

---

## Jazz Leadsheets

Simple jazz tunes for trumpet students. Written pitch (Bb instrument).

### Beginner leadsheet
- Form: 12-bar blues only
- Chords: dominant 7ths only (e.g., Bb7, Eb7, F7)
- Melody: stepwise motion, limited leaps, range C4–C5
- Rhythm: quarter and half notes; occasional dotted quarter + eighth
- Feel: slow swing or medium blues

### Advanced leadsheet
- Form: 12-bar blues or 16-bar AABA
- Chords: maj7, min7, dom7, occasional ii-V-I progressions
- Melody: leaps up to a 5th, some syncopation, range C4–F5
- Rhythm: quarter, eighth, dotted rhythms, ties across barlines
- Feel: medium swing or bossa

### Leadsheet Output Format

```
Title: [title]
Style: [slow swing / medium swing / blues / bossa]
Form: [12-bar blues / AABA / etc.]
Key: [concert key] / Written key for Bb trumpet: [written key]
Tempo: [BPM or descriptor]

Chord symbols (concert): [bar-by-bar, e.g., "1-4: Bb7 | 5-6: Eb7 | 7-8: Bb7 | 9: F7 | 10: Eb7 | 11-12: Bb7"]
Melody (written pitch): [note names + durations, bar by bar]
Teaching notes: [style pointers, articulation, where to breathe]
```

For score-writer handoff, use the same Notes format as exercises:
```
Notes: [Bb4 quarter, C5 quarter, D5 half, ...]
```

---

## Theory Worksheets

Self-contained text worksheets — no notation required. Print-ready format.

### Concept focus options
- **Intervals** — identify and construct intervals above/below a given note
- **Chord spelling** — build major, minor, dominant 7th chords from a root
- **Key signatures** — identify keys, list sharps/flats, name relative major/minor
- **Ear training** — call-and-response descriptions, listening prompts, solfege

### Output Format

```
Title: [concept] Worksheet — [level]
Objective: [one sentence]
Instructions: [student-facing directions]

Section 1: [label]
[numbered exercise items with blanks]

Section 2 (if applicable): [label]
[numbered exercise items with blanks]

Answer Key:
[numbered answers matching above]

Teacher Notes: [common errors, how to use in class]
```

Keep worksheets to one page (10–15 items max). Use plain language — no assumed music theory vocabulary unless it's the concept being taught.

---

## Knowledge File

`knowledge/band/beginning-band-essentials.md`

If stub: notify user, proceed using general beginning band knowledge.
