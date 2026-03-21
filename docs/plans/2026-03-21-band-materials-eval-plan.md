# band-materials Eval Framework — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable eval framework for the `band-materials` skill — test case library, 4-dimension rubric, and a reviewer subagent that scores outputs and produces a two-section report (flagged + passing).

**Architecture:** All files live in `mr-burger-music/eval/`. The framework is pure markdown — no code. A subagent prompt (`band-materials-eval.md`) reads the rubric and test cases, generates outputs by executing the band-materials skill instructions directly, scores each output 1–3 on four dimensions, and writes a dated results file. Human reviews passing items; flagged items include the reason.

**Tech Stack:** Markdown files only. No code, no dependencies. Git for version control.

**Spec:** `docs/specs/2026-03-21-band-materials-eval-design.md`

---

## File Map

### New files to create

```
mr-burger-music/eval/
├── README.md                           ← Task 1
├── rubric.md                           ← Task 2
├── test-cases/
│   ├── exercises.md                    ← Task 3
│   ├── rhythm-worksheets.md            ← Task 4
│   ├── chorales.md                     ← Task 5
│   └── warm-ups.md                     ← Task 6
├── results/
│   └── .gitkeep                        ← Task 1
└── band-materials-eval.md              ← Task 7
```

### No existing files modified.

---

## Task 1: Scaffold the eval directory + README

**Files:**
- Create: `mr-burger-music/eval/README.md`
- Create: `mr-burger-music/eval/results/.gitkeep`

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p mr-burger-music/eval/test-cases
mkdir -p mr-burger-music/eval/results
touch mr-burger-music/eval/results/.gitkeep
```

- [ ] **Step 2: Write `mr-burger-music/eval/README.md`**

```markdown
# band-materials Eval Framework

A reusable eval framework for the `band-materials` skill.

## What this is

Test case library + 4-dimension rubric + reviewer subagent. Catches bad outputs
(wrong range, too generic, pedagogically unsound, wrong level) and surfaces skill
gaps for the human to review and fix.

## How to run

Dispatch the `band-materials-eval` agent:

> "Run the band-materials eval and write results to eval/results/"

The agent will:
1. Read `eval/rubric.md` and all four test-case files (12 test cases total)
2. Execute each test case using the band-materials skill instructions
3. Score each output on 4 dimensions (1–3)
4. Write a dated results file to `eval/results/YYYY-MM-DD-run.md`
5. Report a summary: X flagged, X passing, top issues found

## After the run

- **Flagged items** — subagent identified a failure. Review and file a skill fix.
- **Passing items** — passed automated checks. Review these yourself for subtle issues.

## Re-running after fixes

Re-run the eval after any change to `band-materials/skill.md` or its knowledge files.
The 12 original test cases act as a regression suite.

## Adding new test cases

When `band-materials` is expanded (jazz leadsheets, theory worksheets, etc.):
1. Add a new test-case file to `eval/test-cases/`
2. Update the subagent prompt in `band-materials-eval.md` to include the new file
3. Optionally add new rubric dimensions if the new output type needs different scoring

## File structure

| File | Purpose |
|------|---------|
| `rubric.md` | Scoring criteria for all 4 dimensions |
| `test-cases/exercises.md` | 3 exercise test prompts |
| `test-cases/rhythm-worksheets.md` | 3 rhythm worksheet test prompts |
| `test-cases/chorales.md` | 3 chorale test prompts |
| `test-cases/warm-ups.md` | 3 warm-up test prompts |
| `results/` | Dated eval run reports |
| `band-materials-eval.md` | Reviewer subagent prompt |
```

- [ ] **Step 3: Verify**

Both files exist:
```bash
ls mr-burger-music/eval/
ls mr-burger-music/eval/results/
```

- [ ] **Step 4: Commit**

```bash
git add mr-burger-music/eval/README.md mr-burger-music/eval/results/.gitkeep
git commit -m "feat(eval): scaffold band-materials eval directory"
```

---

## Task 2: Write the rubric

**Files:**
- Create: `mr-burger-music/eval/rubric.md`

- [ ] **Step 1: Write `mr-burger-music/eval/rubric.md`**

```markdown
# band-materials Eval Rubric

Each output is scored on four dimensions. Scores are 1–3.

| Score | Meaning |
|-------|---------|
| 1 | Fail — clear problem, needs fix |
| 2 | Acceptable — works but could be better |
| 3 | Strong — correct, specific, usable as-is |

---

## Dimension 1: Range/Notes Accuracy

Does every note in the output fall within the correct written range for the stated level?

Score this only on range correctness — not on pedagogical sequence or difficulty calibration.

- **3:** All notes within range; no errors
- **2:** Minor range issue (one note slightly outside, easily corrected)
- **1:** Notes clearly outside range; output is not usable for the stated level

**Reference ranges (written pitch for Bb trumpet):**

| Level | Range |
|-------|-------|
| Early beginner | C4–G4 |
| Beginner | C4–C5 |
| Developing | C4–F5 |

---

## Dimension 2: Specificity

Is the output tailored to the context (beginning band trumpet, stated level, concept focus),
or is it generic enough to come from any source?

Score this only on whether the output uses skill/instrument/concept context — not on
difficulty calibration (that is Dimension 4).

- **3:** Output references the specific concept, level, and instrument with concrete detail
- **2:** Mostly specific; one or two generic filler elements
- **1:** Generic — could have been produced without any skill context at all

---

## Dimension 3: Pedagogical Soundness

Does the output follow correct teaching sequence? Does it build on prior skills correctly?
Are instructions clear and logically ordered?

- **3:** Correct progression, no skipped prerequisites, clear step-by-step structure
- **2:** Mostly sound; minor sequencing issue or unclear step
- **1:** Skips prerequisites, teaches concepts in wrong order, or instructions are confusing

---

## Dimension 4: Level Appropriateness

Is the difficulty of the output a match for the stated student level?

Score this only on difficulty calibration — not on whether the output names the level or
instrument (that is Dimension 2).

- **3:** Difficulty is well-calibrated — not too easy, not too hard
- **2:** Slightly off (a bit too easy or a bit too hard) but usable
- **1:** Clearly wrong level — would frustrate or bore students at the stated level

---

## Flag Threshold

An output is **flagged** if:
- Any single dimension scores **1**, OR
- The exact average score across all four dimensions is **below 2.0**

The threshold is applied to the exact average before rounding for display.

Outputs that pass the threshold appear in the **Passing** section for human review.
```

- [ ] **Step 2: Verify** — confirm rubric has all 4 dimensions, flag threshold, and reference ranges

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/rubric.md
git commit -m "feat(eval): add band-materials eval rubric"
```

---

## Task 3: Write exercise test cases

**Files:**
- Create: `mr-burger-music/eval/test-cases/exercises.md`

> **Domain note:** Exercises teach a specific physical or technical skill (fingerings, articulation, tone production). Range is the most important rubric dimension here — beginners will fail if notes exceed their physical capability.

- [ ] **Step 1: Write `mr-burger-music/eval/test-cases/exercises.md`**

```markdown
# Exercise Test Cases

## Early Beginner

**Prompt:** Generate a whole note and half note exercise introducing C4, D4, and E4
for beginning trumpet players in their first 3 weeks.

**Expected concept:** Stepwise exercise on C4–E4 using whole and half notes only.
Written instructions for fingerings (C=open, D=1+3, E=1+2). Metronome at 60.

**Key checks:** All notes must be C4, D4, or E4 only — no F4 or above.
Rhythm must use only whole notes or half notes — no quarter notes yet.

---

## Beginner

**Prompt:** Generate an articulation exercise using quarter notes on the Bb major scale
(C4–C5) for beginning trumpet players who have been playing 8–10 weeks.

**Expected concept:** Ascending and descending Bb major scale (written: C D E F G A B C)
with quarter notes. Single tongue articulation ("tu"). Metronome at 60–72.

**Key checks:** All 8 scale tones present (C D E F G A B C, written pitch).
Quarter notes throughout — no eighth notes yet. "Tu" syllable instruction included.

---

## Developing

**Prompt:** Generate an eighth note scale exercise in Bb major for developing trumpet
players who have mastered quarter note articulation and are ready for faster note values.

**Expected concept:** Ascending/descending Bb scale in eighth notes. Alternating slur
and tongue patterns. Metronome at 60–80. Stays within C4–C5 (beginner range) or
extends slightly to F5 at most.

**Key checks:** Exercise must actually use eighth notes — not just mention them.
No notes above F5. Articulation pattern should be specified (slur/tongue groupings).
```

- [ ] **Step 2: Verify** — 3 test cases present, each with Prompt, Expected concept, Key checks

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/test-cases/exercises.md
git commit -m "feat(eval): add exercise test cases"
```

---

## Task 4: Write rhythm worksheet test cases

**Files:**
- Create: `mr-burger-music/eval/test-cases/rhythm-worksheets.md`

> **Domain note:** Rhythm worksheets are pitch-independent — they test reading and counting, not note range. Pedagogical soundness and level appropriateness are the most important dimensions. Check that rhythm complexity matches the stated stage.

- [ ] **Step 1: Write `mr-burger-music/eval/test-cases/rhythm-worksheets.md`**

```markdown
# Rhythm Worksheet Test Cases

## Early Beginner

**Prompt:** Generate a rhythm worksheet using only quarter notes and half notes in 4/4
time for early beginner band students who are just learning to count.

**Expected concept:** 4–6 lines of rhythmic patterns using only quarter notes (1 beat)
and half notes (2 beats) in 4/4. Counting syllables written below each note.
Instructions to tap and count aloud. No eighth notes.

**Key checks:** No eighth notes or whole notes beyond 4-beat holds.
Counting syllables (1, 2, 3, 4) must be shown. Worksheet must have multiple lines
of patterns, not just one example.

---

## Beginner

**Prompt:** Generate a rhythm worksheet introducing eighth note pairs mixed with quarter
notes in 4/4 for beginner band students who are solid on whole, half, and quarter notes.

**Expected concept:** Patterns combining quarter notes and eighth note pairs (ti-ti or
1-and). Counting syllables shown. Instructions to write counts first, then tap, then
play. Progresses from simple (all quarters + one eighth pair) to more mixed.

**Key checks:** Eighth notes must appear as PAIRS only — no isolated eighth notes.
Counting syllable "1-and" or "ti-ti" must be shown for eighth pairs.
Worksheet must show progression from simple to more complex within the sheet.

---

## Developing

**Prompt:** Generate a rhythm worksheet with freely mixed eighth notes, quarter notes,
half notes, and dotted half notes in 4/4 for developing band students.

**Expected concept:** 6–8 lines of increasingly complex patterns mixing all note values
including dotted half notes. Counting shown. At least one line with continuous eighth
note runs.

**Key checks:** Dotted half notes (3 beats) must appear with correct counting shown
(1-2-3). At least one line should have 4+ consecutive eighth notes.
No dotted quarter notes or syncopation yet — those come later.
```

- [ ] **Step 2: Verify** — 3 test cases present, each with Prompt, Expected concept, Key checks

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/test-cases/rhythm-worksheets.md
git commit -m "feat(eval): add rhythm worksheet test cases"
```

---

## Task 5: Write chorale test cases

**Files:**
- Create: `mr-burger-music/eval/test-cases/chorales.md`

> **Domain note:** Chorales develop ensemble listening and blend — they're harmonically simple but require sustained tone and breath support. Range accuracy is critical; early chorales must stay within C4–G4. Specificity check: a chorale must be written for Bb trumpet, not concert pitch.

- [ ] **Step 1: Write `mr-burger-music/eval/test-cases/chorales.md`**

```markdown
# Chorale Test Cases

## Early Beginner

**Prompt:** Generate a simple 4-bar I-IV-V-I chorale in Bb major using whole notes
for early beginner trumpet players in their first month.

**Expected concept:** 4 bars, one chord per bar (I-IV-V-I in Bb: tonic-subdominant-
dominant-tonic). Whole notes only. Soprano melody line for Bb trumpet stays C4–G4.
Teaching note: listen across the section, sustain fully.

**Key checks:** Trumpet notes (written pitch) must stay within C4–G4.
Chord progression must be clearly I-IV-V-I with Roman numerals labeled.
Whole notes only — no other rhythms.

---

## Beginner

**Prompt:** Generate a 4-bar chorale in Bb major using half notes and whole notes
for beginner trumpet players who know the full Bb major scale (C4–C5).

**Expected concept:** 4-bar soprano melody in Bb major using half and whole notes.
Range up to C5. Simple harmonic motion (stepwise or small leaps). Director cues
(rests for instruction) noted. Teaching focus: matching tone across the section.

**Key checks:** Notes must stay within C4–C5 (written pitch).
Must use both half notes and whole notes — not just one value.
Must include at least one teaching note or director instruction.

---

## Developing

**Prompt:** Generate an 8-bar chorale in Bb major with quarter, half, and whole note
rhythms for developing trumpet players, suitable for a section warm-up.

**Expected concept:** 8-bar soprano melody with rhythmic variety. Written range
C4–F5 (developing range). Clear phrase structure with breathing points. Teaching
focus: blend and intonation.

**Key checks:** Notes must stay within C4–F5 (written pitch).
Must have rhythmic variety — at least 3 different note values used.
Must have at least one clearly marked breathing point or rest.
```

- [ ] **Step 2: Verify** — 3 test cases present, each with Prompt, Expected concept, Key checks

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/test-cases/chorales.md
git commit -m "feat(eval): add chorale test cases"
```

---

## Task 6: Write warm-up test cases

**Files:**
- Create: `mr-burger-music/eval/test-cases/warm-ups.md`

> **Domain note:** Warm-ups are sequenced — the order matters (long tones → flexibility → scales → chorale). Pedagogical soundness is the most important dimension here. Check that the sequence follows correct warm-up order and doesn't skip steps.

- [ ] **Step 1: Write `mr-burger-music/eval/test-cases/warm-ups.md`**

```markdown
# Warm-Up Test Cases

## Early Beginner

**Prompt:** Generate a 5-minute warm-up for early beginner trumpet players focused
on open tones G4 and C4 only.

**Expected concept:** Long tones on G4 and C4 (both open, no valves). Whole notes
at metronome 60. "Tu" syllable. Instruction to play softly. Rest between notes.
Total time ~5 minutes.

**Key checks:** Only G4 and C4 should appear — no fingered notes.
Must include explicit rest instructions between tones.
Must specify playing softly (forte playing damages early embouchure).

---

## Beginner

**Prompt:** Generate a 10-minute warm-up sequence combining long tones and a simple
Bb scale exercise for beginner trumpet players (8–12 weeks in).

**Expected concept:** Sequenced warm-up: (1) long tones on C4 and G4 with rests,
(2) Bb major scale ascending and descending in half notes. Total time ~10 minutes.
Range C4–C5.

**Key checks:** Must have two distinct sections in the correct order (long tones
BEFORE scale work — never reversed). Notes within C4–C5 only. Scale must be
labeled as Bb major (written C major for trumpet).

---

## Developing

**Prompt:** Generate a full 15-minute warm-up sequence for developing trumpet players
covering long tones, flexibility, scale, and a short chorale.

**Expected concept:** Four-section warm-up in order: (1) long tones 3 min,
(2) flexibility/lip slurs 3 min, (3) Bb scale with eighth notes 5 min,
(4) simple chorale 4 min. Each section labeled with duration.

**Key checks:** All four sections must be present AND in this order:
long tones → flexibility → scale → chorale. Never scale before long tones.
Durations must add up to approximately 15 minutes.
Flexibility/lip slur section must be present — this is the most commonly missing
element in generated warm-ups.
```

- [ ] **Step 2: Verify** — 3 test cases present, each with Prompt, Expected concept, Key checks

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/test-cases/warm-ups.md
git commit -m "feat(eval): add warm-up test cases"
```

---

## Task 7: Write the eval subagent prompt

**Files:**
- Create: `mr-burger-music/eval/band-materials-eval.md`

> **Note:** This is an agent definition file, not a Claude Code skill/agent registered in plugin.json. It is dispatched manually with the Agent tool. It lives in `eval/` as a dev tool, not in `agents/`.

- [ ] **Step 1: Write `mr-burger-music/eval/band-materials-eval.md`**

```markdown
---
name: band-materials-eval
description: >
  Eval agent for the band-materials skill. Runs 12 test cases, scores each output
  on 4 dimensions using the rubric, and writes a dated results report.
  Dispatch manually: "Run the band-materials eval and write results to eval/results/"
---

You are the band-materials eval agent. Your job is to run all 12 test cases, score each
output against the rubric, and write a results report.

## Setup

Before running any test cases:

1. Read `mr-burger-music/eval/rubric.md` — this is your scoring guide
2. Read `mr-burger-music/skills/band-materials/skill.md` — this is the skill you are evaluating
3. Read all four test-case files:
   - `mr-burger-music/eval/test-cases/exercises.md`
   - `mr-burger-music/eval/test-cases/rhythm-worksheets.md`
   - `mr-burger-music/eval/test-cases/chorales.md`
   - `mr-burger-music/eval/test-cases/warm-ups.md`

## For each test case (12 total)

1. **Generate the output:** Read `band-materials/skill.md` and execute its instructions
   directly using the test case's Prompt as your input. Generate the output as if you
   ARE the band-materials skill responding to that prompt.

2. **Score the output** on all four rubric dimensions (1–3 each), using the test case's
   **Key checks** field to guide your scoring focus for that specific case.

3. **Calculate the exact average** (sum of 4 scores ÷ 4).

4. **Determine flag status:**
   - FLAGGED if any dimension = 1
   - FLAGGED if exact average < 2.0
   - PASSING otherwise

## Results file

Write the complete results to `mr-burger-music/eval/results/YYYY-MM-DD-run.md`
(use today's date).

Use this format exactly:

```markdown
# band-materials Eval — YYYY-MM-DD

**Summary:** X flagged, X passing of 12 total

**Top issues:** [1-3 bullet points on most common failure patterns, or "None — all passing"]

---

## Flagged (X of 12)

### [Output type] — [Level]
**Prompt:** [exact prompt used]
**Scores:** Range: X | Specificity: X | Pedagogy: X | Level: X | Avg: X.XX
**Flag reason:** [which dimension failed and why — be specific]
**Output:**
[the full output you generated]

---

## Passing (X of 12)

### [Output type] — [Level]
**Prompt:** [exact prompt used]
**Scores:** Range: X | Specificity: X | Pedagogy: X | Level: X | Avg: X.XX
**Output:**
[the full output you generated]

---
```

## After writing the results file

Report back:
- Path to results file
- X flagged, X passing
- Top 1-2 issues found (or "all passing")
- Any knowledge gaps you noticed (e.g., "band-materials did not reference the knowledge
  file for beginning band essentials — the output was generic")
```

- [ ] **Step 2: Verify** — agent file has Setup, For each test case, Results file format, and After writing sections

- [ ] **Step 3: Commit**

```bash
git add mr-burger-music/eval/band-materials-eval.md
git commit -m "feat(eval): add band-materials eval subagent prompt"
```

---

## Task 8: Final verification + push

- [ ] **Step 1: Verify complete file structure**

```bash
find mr-burger-music/eval -type f | sort
```

Expected output:
```
mr-burger-music/eval/README.md
mr-burger-music/eval/band-materials-eval.md
mr-burger-music/eval/results/.gitkeep
mr-burger-music/eval/rubric.md
mr-burger-music/eval/test-cases/chorales.md
mr-burger-music/eval/test-cases/exercises.md
mr-burger-music/eval/test-cases/rhythm-worksheets.md
mr-burger-music/eval/test-cases/warm-ups.md
```

- [ ] **Step 2: Check git log** — verify all 6 commits are present

```bash
git log --oneline | head -10
```

- [ ] **Step 3: Push branch**

```bash
git push origin music-score-transformer
```

- [ ] **Step 4: Do a smoke test** — dispatch the eval agent manually

> "Run the band-materials eval using the files in mr-burger-music/eval/ and write results to mr-burger-music/eval/results/"

Verify the results file passes all of the following before calling this done:
- [ ] Results file exists at `eval/results/YYYY-MM-DD-run.md`
- [ ] File contains exactly 12 entries (Flagged + Passing sections combined)
- [ ] Both `## Flagged` and `## Passing` sections are present
- [ ] Every entry has all four score dimensions (Range, Specificity, Pedagogy, Level)
- [ ] All scores are integers 1, 2, or 3 — no other values
- [ ] Summary line shows correct totals (flagged + passing = 12)
