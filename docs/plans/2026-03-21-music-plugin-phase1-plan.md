# mr-burger-music Plugin — Phase 1: Knowledge Base Extraction — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Read and distill 14 source PDFs/documents from Mr. Burger's music library into structured markdown knowledge files that power the `mr-burger-music` plugin's skills and agents.

**Architecture:** Each task reads source file(s), extracts key content per the spec's extraction targets, and writes a markdown file following the standard knowledge file format. Tasks are independent and can be done in any order, but priority order is recommended (highest LHS value first). Full source PDFs remain at their original locations — knowledge files are distilled summaries, not replacements.

**Tech Stack:** Read tool (PDFs), Write tool (markdown output). No code. Each task is read → extract → write → verify → commit.

**Spec:** `~/Documents/Tech/mr-burger-plugins/docs/specs/2026-03-21-music-plugin-phase1-design.md`

**Path note:** `Jazz/ Theory/` directory has a real leading space in its name — always quote this path in commands.

---

## Knowledge File Format

Every file follows this structure:

```markdown
# [Title]

**Source(s):** [list of PDFs]
**Last updated:** [date]
**Relevance to LHS:** [one sentence connecting this to the Linear Harmony System]

---

## Key Concepts

[Distilled core ideas — 200–400 words max]

## Exercises / Reference

[Specific exercises, patterns, or reference material — structured for quick lookup]

## Connection to LHS

[Explicit callouts for how this content supports the practice system]

## Full Source

[File path(s) to original PDF(s)]
```

---

## Output Directory

`~/Documents/Tech/mr-burger-plugins/mr-burger-music/knowledge/`

All stub files from Phase 2 Task 2 are already in place. Phase 1 replaces each stub with real content.

---

## Task 1: `jazz/ligon-linear-harmony.md` ← Priority 1

**Sources:**
- `~/Documents/Music/Jazz/Jazz books/connecting-chords-with-linear-harmony-bert-ligon.pdf` ← PRIMARY
- `~/Documents/Music/Jazz/Jazz books/bert-ligon-comprehensive-technique-for-jazz-musicians-pdf-free.pdf`

**Extract:**
- The three outlines over ii-V-I in C (Dm7 → G7 → Cmaj7) — exact note sequences
- 7→3 resolution principle with examples
- Embellishment techniques: chromatic approaches, enclosures, neighbor tones, rhythm variations
- Ligon's method for practicing outlines (singing first, slow tempos, etc.)
- Key concepts from Comprehensive Technique relevant to LHS (chord-tone targeting, guide tones)

- [ ] **Step 1: Read primary source**

```
Read: ~/Documents/Music/Jazz/Jazz books/connecting-chords-with-linear-harmony-bert-ligon.pdf
```

Focus on: outline definitions, 7→3 explanation, embellishment chapter, practice methodology.

- [ ] **Step 2: Read secondary source**

```
Read: ~/Documents/Music/Jazz/Jazz books/bert-ligon-comprehensive-technique-for-jazz-musicians-pdf-free.pdf
```

Focus on: sections that relate to chord-tone targeting and guide tones. Skip unrelated chapters.

- [ ] **Step 3: Write the knowledge file**

Replace the stub at `knowledge/jazz/ligon-linear-harmony.md` with full content. Follow the standard format. The Exercises / Reference section should include:
- A table of all three outlines in C with note sequences and character descriptions
- The 7→3 resolution shown with notation (text-based, e.g., C → B, F → E)
- A list of embellishment techniques with one-line descriptions each
- A short practice sequence (how Ligon recommends building from outline to improvisation)

- [ ] **Step 4: Verify**

Read the completed file and confirm:
- All three outlines are present with correct notes
- 7→3 resolution is explained clearly
- At least 3 embellishment techniques are documented
- Connection to LHS section is specific (not generic)

- [ ] **Step 5: Commit**

```bash
cd ~/Documents/Tech/mr-burger-plugins
git add mr-burger-music/knowledge/jazz/ligon-linear-harmony.md
git commit -m "feat(knowledge): extract Ligon linear harmony content"
```

---

## Task 2: `jazz/windau-outlines.md` ← Priority 2

**Sources:**
- `~/Documents/Music/Jazz/Practice/outlines-for-jazz-improvisation-in-all-keys.pdf`
- `~/Documents/Music/Jazz/ Theory/The following outlines all include passing tones and all begin with added pick up notes. They range from.pdf` (check if related)

**Note:** `Jazz/Practice/` contains a mix of jazz and trumpet files — the Windau PDF is confirmed present alongside misfiled trumpet materials. Use the full path above.

**Extract:**
- All three outlines in all 12 keys — formatted as quick-reference tables
- Note where Windau's version includes passing tones that differ from bare Ligon outlines — flag these clearly
- Any practice instructions included in the source

- [ ] **Step 1: Read Windau source**

```
Read: ~/Documents/Music/Jazz/Practice/outlines-for-jazz-improvisation-in-all-keys.pdf
```

- [ ] **Step 2: Check passing-tones document**

```
Read: ~/Documents/Music/Jazz/ Theory/The following outlines all include passing tones and all begin with added pick up notes. They range from.pdf
```

Determine if this is a Windau supplement or a separate source. Note any differences from the bare outlines.

- [ ] **Step 3: Write the knowledge file**

Replace stub at `knowledge/jazz/windau-outlines.md`. The Exercises / Reference section should be a clean reference table — one table per outline (1, 2, 3), columns for each of the 12 keys. Use letter names only (no solfege). Flag passing-tone variations clearly with a note.

Format example:
```
## Outline 2 — All Keys (Windau)

| Key | Dm7 equivalent | G7 equivalent | Cmaj7 equivalent |
|-----|---------------|--------------|-----------------|
| C   | D F A C       | B A G F      | E               |
| F   | G Bb D F      | E D C Bb     | A               |
...
```

- [ ] **Step 4: Verify**

Confirm all 12 keys are present for all 3 outlines. Spot-check 2-3 keys against the source for accuracy.

- [ ] **Step 5: Commit**

```bash
git add mr-burger-music/knowledge/jazz/windau-outlines.md
git commit -m "feat(knowledge): extract Windau all-keys outlines reference"
```

---

## Task 3: `trumpet/william-adam.md` ← Priority 3

**Sources (read in this order):**
1. `~/Documents/Music/Trumpet/A Tribute to William Adam - Compiled & Edited by Charles Davis.pdf` ← most comprehensive
2. `~/Documents/Music/Trumpet/Routines/ITG 2024 William Adam.pdf`
3. `~/Documents/Music/Trumpet/Routines/BILL-ADAM-ROUTINE-Trumpet-Magazine.pdf`
4. `~/Documents/Music/Trumpet/Routines/pdfcoffee.com-the-bill-adam-daily-routine.pdf`
5. `~/Documents/Music/Trumpet/Routines/pdfcoffee.com-jerry-hey-amp-larry-hall-extended-adam-routine-for-trumpet.pdf`
6. `~/Documents/Music/Trumpet/Routines/Routine-explanation-update-4121BobSlack.pdf`
7. `~/Documents/Music/Trumpet/Adam1.pdf`, `Adam2.pdf`, `Adam3.pdf`

**Extract:**
- Core philosophy: sound concept, embouchure approach, Adam's teaching principles
- Daily routine structure: long tones, lip slurs, flexibility exercises, range building — sequence and timing
- Specific exercises with notes/fingerings where possible (text-based description)
- Guidance for comeback players and embouchure rebuilding
- Extended routine variations (Jerry Hey/Larry Hall)
- Bob Slack's explanation of the routine philosophy

- [ ] **Step 1: Read primary source (Charles Davis tribute)**

```
Read: ~/Documents/Music/Trumpet/A Tribute to William Adam - Compiled & Edited by Charles Davis.pdf
```

This is the most comprehensive — take detailed notes on routine structure, philosophy, and specific exercises.

- [ ] **Step 2: Read supporting sources**

Read each remaining source, adding any unique content not covered in the Davis tribute:

```
Read: ~/Documents/Music/Trumpet/Routines/ITG 2024 William Adam.pdf
Read: ~/Documents/Music/Trumpet/Routines/BILL-ADAM-ROUTINE-Trumpet-Magazine.pdf
Read: ~/Documents/Music/Trumpet/Routines/pdfcoffee.com-the-bill-adam-daily-routine.pdf
Read: ~/Documents/Music/Trumpet/Routines/pdfcoffee.com-jerry-hey-amp-larry-hall-extended-adam-routine-for-trumpet.pdf
Read: ~/Documents/Music/Trumpet/Routines/Routine-explanation-update-4121BobSlack.pdf
Read: ~/Documents/Music/Trumpet/Adam1.pdf
Read: ~/Documents/Music/Trumpet/Adam2.pdf
Read: ~/Documents/Music/Trumpet/Adam3.pdf
```

- [ ] **Step 3: Write the knowledge file**

Replace stub at `knowledge/trumpet/william-adam.md`. Structure the Exercises / Reference section as:

1. **Daily Routine Sequence** — ordered list of components with duration estimates
2. **Long Tones** — description, starting pitch, duration per note, what to listen for
3. **Lip Slurs** — description, which partials, what to feel
4. **Flexibility Exercises** — key exercises from Adam1/2/3
5. **Extended Routine** (Jerry Hey/Larry Hall) — what it adds and when to use it
6. **Comeback Player Notes** — Adam's specific guidance for rebuilding embouchure

- [ ] **Step 4: Verify**

Confirm the routine sequence is complete and ordered. Verify comeback player guidance is present and specific (not generic advice).

- [ ] **Step 5: Commit**

```bash
git add mr-burger-music/knowledge/trumpet/william-adam.md
git commit -m "feat(knowledge): extract William Adam routine and philosophy"
```

---

## Task 4: `trumpet/klobnak-trumpet.md` ← Priority 4

**Sources:**
- `~/Documents/Music/Trumpet/Jason Klobnak trumpet routine.pdf`
- `~/Documents/Music/Trumpet/Jason Klobnak's Jazz Trumpet Routine Major Day.pdf`
- `~/Documents/Music/Trumpet/Routines/The-Jazz-Warm-Up-2.pdf`

**Extract:**
- Daily routine structure (warm-up → technique → jazz vocabulary)
- Major Day vs. other day structure — what changes
- How Klobnak integrates jazz vocabulary into the routine
- Key exercises and their purpose
- Connection points to LHS (outlines, ii-V-I vocabulary)

- [ ] **Step 1: Read all three sources**

```
Read: ~/Documents/Music/Trumpet/Jason Klobnak trumpet routine.pdf
Read: ~/Documents/Music/Trumpet/Jason Klobnak's Jazz Trumpet Routine Major Day.pdf
Read: ~/Documents/Music/Trumpet/Routines/The-Jazz-Warm-Up-2.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/trumpet/klobnak-trumpet.md`. Structure:
1. **Routine Overview** — how Klobnak's routine fits alongside Adam
2. **Major Day Structure** — ordered component list
3. **Jazz Warm-Up** — key exercises from The-Jazz-Warm-Up-2
4. **Connection to LHS** — where Klobnak vocabulary overlaps with outlines/ii-V-I

- [ ] **Step 3: Verify**

Read the completed file and confirm:
- Routine overview covers both the standard routine and Major Day variant
- Jazz Warm-Up exercises are documented with specific content
- Connection to LHS section identifies at least one overlap with LHS outlines or ii-V-I work

- [ ] **Step 4: Commit**

```bash
git add mr-burger-music/knowledge/trumpet/klobnak-trumpet.md
git commit -m "feat(knowledge): extract Klobnak trumpet routine"
```

---

## Task 5: `guitar/shell-voicings.md` ← Priority 5

**Sources:**
- `~/Documents/Music/Guitar/Shell-voicings.pdf` ← PRIMARY
- `~/Documents/Music/Guitar/Jazz-Chord-Survival-Kit1.pdf`

**Extract:**
- Shell voicing shapes for ii-V-I (Dm7, G7, Cmaj7 and equivalents) in multiple keys
- Fingering descriptions (string, fret, finger — text-based since no diagrams)
- Voice leading between shells (how to move from chord to chord)
- Common keys for LHS practice (C, F, Bb, Eb, G)

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Guitar/Shell-voicings.pdf
Read: ~/Documents/Music/Guitar/Jazz-Chord-Survival-Kit1.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/guitar/shell-voicings.md`. Exercises / Reference section:
1. **Shell Voicing Concept** — what shells are, why they work for LHS
2. **ii-V-I Shell Shapes in C** — Dm7, G7, Cmaj7 with string/fret/finger descriptions
3. **Moving Through Keys** — shell shapes transposed to F, Bb, Eb, G
4. **Voice Leading Notes** — which fingers stay, which move between chords

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/guitar/shell-voicings.md
git commit -m "feat(knowledge): extract shell voicings reference"
```

---

## Task 6: `guitar/fretboard.md` ← Priority 6

**Sources:**
- `~/Documents/Music/Guitar/Fingerboard Workbook.pdf`
- `~/Documents/Music/Guitar/Fretboard+Mastery+eBook.pdf`

**Extract:**
- Natural note locations on each string (E A D G B e)
- Five position system overview
- How to map LHS outlines onto fretboard positions
- Progressive exercises for learning fretboard geography (beginner-appropriate)

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Guitar/Fingerboard Workbook.pdf
Read: ~/Documents/Music/Guitar/Fretboard+Mastery+eBook.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/guitar/fretboard.md`. Structure:
1. **Natural Notes by String** — reference table (string name → notes at frets 0–12)
2. **Five Position Overview** — position names/anchors, which frets they cover
3. **LHS Outlines on the Fretboard** — where Outline 2 in C sits in Position II
4. **Learning Sequence** — recommended order for fretboard geography study

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/guitar/fretboard.md
git commit -m "feat(knowledge): extract fretboard geography reference"
```

---

## Task 7: `guitar/jazz-guitar-foundations.md` ← Priority 7

**Sources:**
- `~/Documents/Music/Guitar/Beginner's Guide to Jazz Guitar.pdf`
- `~/Documents/Music/Guitar/Jazz Guitar Aebersold.pdf`
- `~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Vol.1 - Beginning Jazz Guitar.pdf`
- `~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Basic chords by Jody Fisher.pdf`

**Extract:**
- Core concepts for jazz guitar beginners
- First chord shapes (open and moveable forms)
- Rhythm guitar basics (comping patterns, time feel)
- How jazz guitar fits into ensemble context
- Beginner-appropriate progression sequence

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Guitar/Beginner's Guide to Jazz Guitar.pdf
Read: ~/Documents/Music/Guitar/Jazz Guitar Aebersold.pdf
Read: ~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Vol.1 - Beginning Jazz Guitar.pdf
Read: ~/Documents/Music/Guitar/The Complete Jazz Guitar Method by Jody Fisher/Basic chords by Jody Fisher.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/guitar/jazz-guitar-foundations.md`. Structure:
1. **Starting Point** — where a beginner with open chords begins in jazz guitar
2. **First Jazz Chord Shapes** — most important moveable forms (7th chords)
3. **Rhythm Guitar Basics** — comping approach, where to place the beat
4. **Beginner Sequence** — recommended learning order from these sources
5. **Connection to LHS** — how foundations support the guitar track (Part 1A/1B)

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/guitar/jazz-guitar-foundations.md
git commit -m "feat(knowledge): extract jazz guitar foundations"
```

---

## Task 8: `jazz/aebersold-handbook.md` ← Priority 8

**Source:**
- `~/Documents/Music/Jazz/ Theory/Aebersold Handbook.pdf`

**Path note:** Directory name has a leading space — use: `~/Documents/Music/Jazz/\ Theory/Aebersold\ Handbook.pdf` in any shell command, or the full quoted path.

**Extract:**
- Foundational jazz theory (scales, modes, chord-scale relationships)
- How to practice with play-along tracks
- ii-V-I progressions explained (Aebersold's framework)
- Key vocabulary and concepts referenced throughout the library

- [ ] **Step 1: Read source**

```
Read: ~/Documents/Music/Jazz/ Theory/Aebersold Handbook.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/jazz/aebersold-handbook.md`. Structure:
1. **Core Theory Concepts** — chord-scale relationships, modes in context
2. **ii-V-I Framework** — Aebersold's explanation and practice approach
3. **Play-Along Practice** — how to use Aebersold volumes effectively
4. **Key Vocabulary** — terms used across the jazz library (changes, guide tones, etc.)
5. **Connection to LHS** — where Aebersold's framework supports outline practice

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/jazz/aebersold-handbook.md
git commit -m "feat(knowledge): extract Aebersold handbook"
```

---

## Task 9: `jazz/bebop-language.md` ← Priority 9

**Sources:**
- `~/Documents/Music/Jazz/ Theory/A Comprehensive Curriculum for Jazz Improvisation and the Bebop Language.docx`
- `~/Documents/Music/Jazz/ Theory/A Beginner's Guide to Jazz Improvisation_ Your First Steps to Finding Your Voice-2.docx`

**Extract:**
- Bebop vocabulary: chromatic approaches, enclosures, bebop scale
- Curriculum sequence for learning bebop language (what order to learn things)
- Connection to LHS outlines (how bebop embellishments extend the outlines)
- Beginner entry points (what to learn first)

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Jazz/ Theory/A Comprehensive Curriculum for Jazz Improvisation and the Bebop Language.docx
Read: ~/Documents/Music/Jazz/ Theory/A Beginner's Guide to Jazz Improvisation_ Your First Steps to Finding Your Voice-2.docx
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/jazz/bebop-language.md`. Structure:
1. **Bebop Vocabulary** — chromatic approaches (below, above, double), enclosures, bebop scale
2. **Learning Sequence** — curriculum order from beginner to developing
3. **Applying to Outlines** — how each embellishment type modifies LHS Outlines 1/2/3
4. **First Steps** — what a beginner should learn before tackling full bebop language

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/jazz/bebop-language.md
git commit -m "feat(knowledge): extract bebop language curriculum"
```

---

## Task 10: `jazz/ii-v-i-vocabulary.md` ← Priority 10

**Sources:**
- `~/Documents/Music/Jazz/Vocabulary/Building-Bebop-Vocabulary.pdf`
- `~/Documents/Music/Jazz/Vocabulary/How Do I Play Long 2-5-1 2.pdf`
- `~/Documents/Music/Jazz/Vocabulary/pdfcoffee.com-bb-20-approach-note-etudes-chad-lb.pdf`
- `~/Documents/Music/Jazz/Vocabulary/Digital Patterns.pdf`
- `~/Documents/Music/Jazz/Vocabulary/Jazz Exercises 2021.pdf`

**Extract:**
- ii-V-I vocabulary patterns (licks, approaches, resolutions)
- Approach note techniques (single, double, chromatic)
- Digital patterns (1-2-3-5 type patterns over chords)
- How vocabulary connects to LHS outlines and embellishments

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Jazz/Vocabulary/Building-Bebop-Vocabulary.pdf
Read: ~/Documents/Music/Jazz/Vocabulary/How Do I Play Long 2-5-1 2.pdf
Read: ~/Documents/Music/Jazz/Vocabulary/pdfcoffee.com-bb-20-approach-note-etudes-chad-lb.pdf
Read: ~/Documents/Music/Jazz/Vocabulary/Digital Patterns.pdf
Read: ~/Documents/Music/Jazz/Vocabulary/Jazz Exercises 2021.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/jazz/ii-v-i-vocabulary.md`. Structure:
1. **Approach Note Types** — below, above, double (with examples in C)
2. **Digital Patterns** — most useful patterns over ii-V-I, written in C
3. **ii-V-I Licks** — 3-5 beginner-appropriate licks in C that extend LHS outlines
4. **Long ii-V-I Lines** — how to construct longer lines from the vocabulary
5. **Connection to LHS** — which vocabulary items apply at LHS Part 3 (Embellishment)

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/jazz/ii-v-i-vocabulary.md
git commit -m "feat(knowledge): extract ii-V-I vocabulary reference"
```

---

## Task 11: `jazz/jazz-standards-playbook.md` ← Priority 11

**Source:**
- `~/Documents/Music/Jazz/pdfcoffee.com-the-jazz-standards-playbook-c-instruments.pdf`

**Extract:**
- Most common standards and their ii-V-I progressions (key center map)
- Standards appropriate for beginner/intermediate level
- Standards with simple enough changes to apply LHS outlines directly
- Progression patterns that repeat across standards (reusable ii-V-I spots)

- [ ] **Step 1: Read source**

```
Read: ~/Documents/Music/Jazz/pdfcoffee.com-the-jazz-standards-playbook-c-instruments.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/jazz/jazz-standards-playbook.md`. Structure:
1. **Beginner-Friendly Standards** — list of 8-10 standards with simple changes, key center, and LHS applicability rating
2. **ii-V-I Spots by Standard** — for each standard, which bars are ii-V-I and in which key
3. **Most Common Keys** — which keys appear most often across standards (prioritize for outline practice)
4. **Practice Entry Point** — recommended first standard to apply LHS outlines

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/jazz/jazz-standards-playbook.md
git commit -m "feat(knowledge): extract jazz standards playbook reference"
```

---

## Task 12: `jazz/klobnak-jazz.md` ← Priority 12

**Sources:**
- `~/Documents/Music/Jazz/Jazz books/Targeting-by-Jason-Klobnak.pdf` ← PRIMARY
- `~/Documents/Music/Jazz/Transcriptions/` ← index only (list filenames, do not distill)

**Extract:**
- Targeting concept — hitting chord tones at key rhythmic moments
- How targeting integrates with LHS outlines (target the 7→3 resolution points)
- Practice method for developing targeting
- Index of available transcriptions (filenames only — not analysed)

- [ ] **Step 1: Read Targeting**

```
Read: ~/Documents/Music/Jazz/Jazz books/Targeting-by-Jason-Klobnak.pdf
```

- [ ] **Step 2: List transcription filenames**

```bash
ls ~/Documents/Music/Jazz/Transcriptions/
```

Copy the filenames into the knowledge file as an index (not content).

- [ ] **Step 3: Write the knowledge file**

Replace stub at `knowledge/jazz/klobnak-jazz.md`. Structure:
1. **Targeting Concept** — what it is, why it works harmonically
2. **Targeting + LHS Outlines** — which outline notes are the strongest targets (7th and 3rd)
3. **Practice Method** — how to develop targeting awareness
4. **Transcription Index** — list of available transcriptions at `~/Documents/Music/Jazz/Transcriptions/`

- [ ] **Step 4: Verify and commit**

```bash
git add mr-burger-music/knowledge/jazz/klobnak-jazz.md
git commit -m "feat(knowledge): extract Klobnak targeting and transcription index"
```

---

## Task 13: `trumpet/clarke-essentials.md` ← Priority 13

**Sources:**
- `~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-1.pdf`
- `~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-4.pdf`
- `~/Documents/Music/Trumpet/pdfcoffee.com_clarke-characteristic-studies-pdf-free.pdf`

**Extract:**
- Core Clarke Technical Studies (which ones, what they develop)
- How Clarke integrates with Adam routine (warm-up → Clarke → jazz)
- Key studies for embouchure development and flexibility
- Appropriate studies for comeback/embouchure rebuilding stage

- [ ] **Step 1: Read sources**

```
Read: ~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-1.pdf
Read: ~/Documents/Music/Trumpet/pdfcoffee.com-clarke-studies-parte-4.pdf
Read: ~/Documents/Music/Trumpet/pdfcoffee.com_clarke-characteristic-studies-pdf-free.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/trumpet/clarke-essentials.md`. Structure:
1. **Clarke Overview** — what the studies develop, how they're organized
2. **Essential Studies** — the 4-6 most important studies for trumpet fundamentals, with brief description of each
3. **Comeback Player Selection** — which studies to prioritize when rebuilding embouchure
4. **Integration with Adam** — where Clarke fits in the daily routine sequence

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/trumpet/clarke-essentials.md
git commit -m "feat(knowledge): extract Clarke technical studies essentials"
```

---

## Task 14: `band/beginning-band-essentials.md` ← Priority 14

**Sources (text/PDF only — skip image files):**
- `~/Documents/Music/Beginning-Band/band_basics_in_bb (dragged).pdf`
- `~/Documents/Music/Beginning-Band/Chorale_08_Trumpet_v1.0.pdf`
- `~/Documents/Music/Beginning-Band/StructureOfTheMajorScaleTable-1.pdf`
- `~/Documents/Music/Beginning-Band/young_ensemble_warm-ups.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/eighth-notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-notes-2.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Food+Rhythms,+eighth+and+quarter+notes.pdf`
- `~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-Notes-Alternating-Hands-1.pdf`

**Skip:** `.png` image files, `PromoBandOrchestraEejazzsampler.pdf`

**Extract:**
- Fundamental exercises for beginning trumpet (fingerings, tone production, range)
- Chorale structure and how to use it in band warm-up
- Major scale structure table
- Rhythm content: quarter notes, half notes, whole notes, eighth notes, alternating patterns
- Progression sequence for beginning band curriculum

- [ ] **Step 1: Read all text sources**

```
Read: ~/Documents/Music/Beginning-Band/band_basics_in_bb (dragged).pdf
Read: ~/Documents/Music/Beginning-Band/Chorale_08_Trumpet_v1.0.pdf
Read: ~/Documents/Music/Beginning-Band/StructureOfTheMajorScaleTable-1.pdf
Read: ~/Documents/Music/Beginning-Band/young_ensemble_warm-ups.pdf
Read: ~/Documents/Music/Beginning-Band/Rhythm Worksheets/eighth-notes.pdf
Read: ~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-notes-2.pdf
Read: ~/Documents/Music/Beginning-Band/Rhythm Worksheets/Food+Rhythms,+eighth+and+quarter+notes.pdf
Read: ~/Documents/Music/Beginning-Band/Rhythm Worksheets/Eighth-Notes-Alternating-Hands-1.pdf
```

- [ ] **Step 2: Write the knowledge file**

Replace stub at `knowledge/band/beginning-band-essentials.md`. Structure:
1. **Beginning Trumpet Fundamentals** — posture, embouchure, first notes (C4–G4 range), fingering chart summary
2. **Warm-Up Sequence** — recommended order for band warm-up (long tones → chorales → scales → exercises)
3. **Chorale Content** — what Chorale 08 contains, how to use it
4. **Scale Structure** — major scale pattern (W-W-H-W-W-W-H) with Bb major as first key
5. **Rhythm Curriculum** — sequence: quarter/half/whole → eighth notes → alternating patterns; counting syllables for each
6. **Beginner Lesson Sequence** — suggested week-by-week progression for first-year players

- [ ] **Step 3: Verify and commit**

```bash
git add mr-burger-music/knowledge/band/beginning-band-essentials.md
git commit -m "feat(knowledge): extract beginning band essentials"
```

---

## Done

All 14 knowledge files are populated. Stubs are replaced with real distilled content. The `mr-burger-music` plugin is now fully knowledge-complete.

**Verify all files are populated (no stubs remaining):**

```bash
# Check for stub status line
grep -rl "Pending Phase 1 extraction" ~/Documents/Tech/mr-burger-plugins/mr-burger-music/knowledge/

# Check for stub title marker
grep -rl "-- STUB" ~/Documents/Tech/mr-burger-plugins/mr-burger-music/knowledge/
```

Expected: no output from either command (all stubs replaced with real content).
