# mr-burger-music Plugin — Phase 1: Knowledge Base Extraction
**Date:** 2026-03-21
**Status:** Approved
**Spec:** `~/Documents/Tech/mr-burger-plugins/docs/specs/2026-03-21-music-plugin-phase1-design.md`
**Implementation plan:** `~/Documents/Tech/mr-burger-plugins/docs/plans/2026-03-21-music-plugin-phase1-plan.md`
**Output feeds:** Phase 2 plugin (`mr-burger-music/knowledge/`)

---

## Overview

Extract and distill key content from Mr. Burger's music PDF and document library into structured markdown reference files. These files become the knowledge base for the `mr-burger-music` plugin's skills and agents. Full source PDFs remain at their original locations for deep lookup.

---

## Source Library Locations

| Area | Path |
|------|------|
| Trumpet | `~/Documents/Music/Trumpet/` |
| Trumpet routines | `~/Documents/Music/Trumpet/Routines/` |
| Guitar | `~/Documents/Music/Guitar/` |
| Jazz books | `~/Documents/Music/Jazz/Jazz books/` |
| Jazz theory | `~/Documents/Music/Jazz/ Theory/` |
| Jazz vocabulary | `~/Documents/Music/Jazz/Vocabulary/` |
| Jazz practice | `~/Documents/Music/Jazz/Practice/` |
| Beginning band | `~/Documents/Music/Beginning-Band/` |

---

## Output Location

All knowledge files go to:
`~/Documents/Tech/mr-burger-plugins/mr-burger-music/knowledge/`

**Note on `linear-harmony-system/`:** This directory is a symlink to `~/Documents/Music/Practice/Linear Harmony System/` — it is pre-existing and out of scope for Phase 1 extraction. The LHS docs are already structured markdown and require no processing.

**Note on `Music/Practice/` directory:** `~/Documents/Music/Practice/` contains the Linear Harmony System (handled via symlink above) plus Adam and Klobnak PDFs that are already covered under the Trumpet section. No additional extraction needed from this directory.

**Path note — `Jazz/ Theory/`:** This directory name contains a leading space (`Jazz/ Theory/`, not `Jazz/Theory/`). This is the real filesystem path. Any script or automation must quote this path carefully to avoid failures.

---

## Extraction Plan

### Priority Order

Process in this order — highest value for LHS system first.

---

### 1. `jazz/ligon-linear-harmony.md`

**Sources:**
- `Jazz books/connecting-chords-with-linear-harmony-bert-ligon.pdf` ← PRIMARY
- `Jazz books/bert-ligon-comprehensive-technique-for-jazz-musicians-pdf-free.pdf`

**Extract:**
- The three outlines (Dm7 → G7 → Cmaj7 in C, all characters)
- 7→3 resolution principle with examples
- Embellishment techniques: chromatic approaches, enclosures, neighbor tones, rhythm variations
- How to practice outlines (Ligon's method)
- Key concepts from Comprehensive Technique relevant to LHS

---

### 2. `jazz/windau-outlines.md`

**Source:**
- `~/Documents/Music/Jazz/Practice/outlines-for-jazz-improvisation-in-all-keys.pdf`

**Note:** `Jazz/Practice/` contains a mix of jazz and trumpet files (Adam PDFs, Klobnak). The Windau outlines file is confirmed present there alongside misfiled trumpet materials — use the full path above.

**Extract:**
- All three outlines in all 12 keys (Windau's version)
- Formatted as quick-reference tables matching LHS Design Document style
- Note: Windau's outlines may include passing tones — flag where they differ from bare Ligon outlines

**Also check:**
- `Jazz/ Theory/The following outlines all include passing tones...pdf` — may be directly related

---

### 3. `trumpet/william-adam.md`

**Sources (in priority order):**
- `Trumpet/A Tribute to William Adam - Compiled & Edited by Charles Davis.pdf` ← most comprehensive
- `Trumpet/Routines/ITG 2024 William Adam.pdf`
- `Trumpet/Routines/BILL-ADAM-ROUTINE-Trumpet-Magazine.pdf`
- `Trumpet/Routines/pdfcoffee.com-the-bill-adam-daily-routine.pdf`
- `Trumpet/Routines/pdfcoffee.com-jerry-hey-amp-larry-hall-extended-adam-routine-for-trumpet.pdf`
- `Trumpet/Routines/Routine-explanation-update-4121BobSlack.pdf`
- `Trumpet/Adam1.pdf`, `Adam2.pdf`, `Adam3.pdf`

**Extract:**
- Core philosophy (sound concept, embouchure approach)
- Daily routine structure: long tones, lip slurs, flexibility exercises, range building
- Sequence and pacing for comeback players / embouchure rebuilding
- Key exercises with notes/fingerings where possible
- Extended routine variations (Jerry Hey/Larry Hall)
- Bob Slack's explanation of the routine philosophy

---

### 4. `trumpet/klobnak-trumpet.md`

**Sources:**
- `Trumpet/Jason Klobnak trumpet routine.pdf`
- `Trumpet/Jason Klobnak's Jazz Trumpet Routine Major Day.pdf`
- `Trumpet/Routines/The-Jazz-Warm-Up-2.pdf`

**Extract:**
- Daily routine structure (warm-up → technique → jazz vocabulary)
- Major Day vs. other day structure
- How Klobnak's routine integrates with jazz practice (outlines, vocabulary)
- Key exercises and their purpose

---

### 5. `guitar/shell-voicings.md`

**Sources:**
- `Guitar/Shell-voicings.pdf` ← PRIMARY
- `Guitar/Jazz-Chord-Survival-Kit1.pdf`

**Extract:**
- Shell voicing shapes for ii-V-I (Dm7, G7, Cmaj7) in multiple keys
- Fingering diagrams described in text (string, fret, finger)
- Voice leading between chords
- Common keys for LHS practice

---

### 6. `guitar/fretboard.md`

**Sources:**
- `Guitar/Fingerboard Workbook.pdf`
- `Guitar/Fretboard+Mastery+eBook.pdf`

**Extract:**
- Natural note locations on each string
- Five position system (CAGED or equivalent)
- How to map LHS outlines onto fretboard positions
- Progressive exercises for fretboard geography

---

### 7. `guitar/jazz-guitar-foundations.md`

**Sources:**
- `Guitar/Beginner's Guide to Jazz Guitar.pdf`
- `Guitar/Jazz Guitar Aebersold.pdf`
- `Guitar/The Complete Jazz Guitar Method by Jody Fisher/Vol.1 - Beginning Jazz Guitar.pdf`
- `Guitar/The Complete Jazz Guitar Method by Jody Fisher/Basic chords by Jody Fisher.pdf`

**Extract:**
- Core concepts for jazz guitar beginners
- First chord shapes (open and moveable)
- Rhythm guitar basics
- How jazz guitar fits into ensemble context

---

### 8. `jazz/aebersold-handbook.md`

**Source:**
- `Jazz/ Theory/Aebersold Handbook.pdf`

**Extract:**
- Foundational jazz theory concepts (scales, modes, chord-scale relationships)
- How to practice with play-alongs
- ii-V-I progressions explained
- Key vocabulary and concepts referenced throughout Mr. Burger's library

---

### 9. `jazz/bebop-language.md`

**Sources:**
- `Jazz/ Theory/A Comprehensive Curriculum for Jazz Improvisation and the Bebop Language.docx`
- `Jazz/ Theory/A Beginner's Guide to Jazz Improvisation_ Your First Steps to Finding Your Voice-2.docx`

**Extract:**
- Bebop vocabulary: chromatic approaches, enclosures, bebop scale
- Curriculum sequence for learning bebop language
- Connection to LHS outlines (how bebop embellishments extend the outlines)

---

### 10. `jazz/ii-v-i-vocabulary.md`

**Sources:**
- `Jazz/Vocabulary/Building-Bebop-Vocabulary.pdf`
- `Jazz/Vocabulary/How Do I Play Long 2-5-1 2.pdf`
- `Jazz/Vocabulary/pdfcoffee.com-bb-20-approach-note-etudes-chad-lb.pdf`
- `Jazz/Vocabulary/Digital Patterns.pdf`
- `Jazz/Vocabulary/Jazz Exercises 2021.pdf`

**Extract:**
- ii-V-I vocabulary patterns (licks, approaches, resolutions)
- Approach note techniques
- Digital patterns (1-2-3-5 type patterns over chords)
- How vocabulary connects to LHS outlines and embellishments

---

### 11. `jazz/jazz-standards-playbook.md`

**Source:**
- `Jazz/pdfcoffee.com-the-jazz-standards-playbook-c-instruments.pdf`

**Extract:**
- Most common standards and their ii-V-I progressions
- Key center map for standards (where outlines apply)
- Standards relevant to beginner/intermediate level (not too complex)
- Standards with simple enough changes to apply LHS outlines

---

### 12. `jazz/klobnak-jazz.md`

**Sources:**
- `~/Documents/Music/Jazz/Jazz books/Targeting-by-Jason-Klobnak.pdf`
- `~/Documents/Music/Jazz/Transcriptions/` — index of available transcriptions (not distilled, just catalogued)

**Extract:**
- Targeting concept (hitting chord tones at key moments)
- How targeting integrates with LHS outlines
- Reference index of available transcriptions for study

---

### 13. `trumpet/clarke-essentials.md`

**Source:**
- `Trumpet/pdfcoffee.com-clarke-studies-parte-1.pdf`
- `Trumpet/pdfcoffee.com-clarke-studies-parte-4.pdf`
- `Trumpet/pdfcoffee.com_clarke-characteristic-studies-pdf-free.pdf`

**Extract:**
- Core Clarke exercises (Technical Studies)
- How they integrate with Adam routine (warmup → Clarke → jazz)
- Key studies for embouchure development and flexibility

---

### 14. `band/beginning-band-essentials.md`

**Sources (text/PDF only — skip image files):**
- `~/Documents/Music/Beginning-Band/band_basics_in_bb (dragged).pdf`
- `~/Documents/Music/Beginning-Band/Chorale_08_Trumpet_v1.0.pdf`
- `~/Documents/Music/Beginning-Band/StructureOfTheMajorScaleTable-1.pdf`
- `~/Documents/Music/Beginning-Band/young_ensemble_warm-ups.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/eighth-notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-notes-2.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Food+Rhythms,+eighth+and+quarter+notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-Notes-Alternating-Hands-1.pdf`

**Skip:** `.png` image files, `PromoBandOrchestraEejazzsampler.pdf` (promo material, not instructional)

**Extract:**
- Fundamental exercises for beginning trumpet players (fingerings, tone production)
- Chorale structures and warm-up sequences
- Major scale structure table
- Rhythm worksheet content: quarter notes, eighth notes, alternating patterns
- Progression sequence for beginning band curriculum

---

## Knowledge File Format

Each knowledge file follows this structure:

```markdown
# [Title]

**Source(s):** [List of PDFs this was distilled from]
**Last updated:** [Date]
**Relevance to LHS:** [How this connects to the Linear Harmony System]

---

## Key Concepts

[Distilled core ideas — 200-400 words max]

## Exercises / Reference

[Specific exercises, patterns, or reference material — structured for quick lookup]

## Connection to LHS

[Explicit callouts for how this content supports the practice system]

## Full Source

[File path(s) to original PDF(s) for deep lookup]
```

---

## Placeholder Stubs

Before Phase 1 is complete, each knowledge file (except `linear-harmony-system/`) contains a stub:

```markdown
# [Title] — STUB

**Source(s):** [PDF paths]
**Status:** Pending Phase 1 extraction

Skills and agents using this file will fall back to LHS markdown and general knowledge
until this file is populated.
```

---

## What's Out of Scope (Phase 1)

- **Advanced guitar content** — Mick Goodrick (*The Advancing Guitarist*, *Almanac of Guitar Voice Leading*), Jody Fisher Vol.2–4, Drop 2 voicings (`Jazz-Chord-Essentials-Drop-2-voicings-part-1.pdf`) — deferred until guitar track progresses. These files live in `~/Documents/Music/Guitar/` and `~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/`.
- **Full transcription analysis** — `Jazz/Transcriptions/` is indexed only (filenames catalogued in `klobnak-jazz.md`), not distilled
- **Real Books** — `~/Documents/Music/Jazz/Jazz books/Real Books/` — reference only, no extraction
- **Holiday/seasonal materials** — `Guitar/Holiday-Jazz-Guitar-Chord-Melodies.pdf`, `Trumpet/silent-night-trumpet.pdf`
- **Image files** — `.png` files in Beginning-Band and elsewhere are not text sources
