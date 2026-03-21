# band-materials Eval Framework — Design Spec

**Date:** 2026-03-21
**Plugin:** mr-burger-music
**Scope:** band-materials skill (current output types: exercises, rhythm worksheets, chorales, warm-ups)
**Goal:** A reusable eval framework that catches bad outputs and surfaces gaps in the skill's knowledge and prompts.

---

## Problem

The `band-materials` skill can produce outputs that fail in four ways:
1. **Wrong range/notes** — notes outside correct range for the stated student level
2. **Too generic** — output has no context-specificity; could come from any source
3. **Pedagogically unsound** — wrong teaching sequence, skipped steps, incorrect progression
4. **Wrong level** — difficulty doesn't match the stated student level

No current mechanism exists to catch these failures systematically or track improvement over time.

---

## Solution

A test case library + rubric eval framework stored in `mr-burger-music/eval/`. A subagent runs test prompts against the skill, scores outputs on four dimensions, and produces a two-section report: flagged items (automatic failures) and passing items for human review.

---

## File Structure

```
mr-burger-music/eval/
├── README.md                         — how to run the eval
├── rubric.md                         — scoring criteria for all 4 dimensions
├── test-cases/
│   ├── exercises.md                  — 3 test prompts (early beginner / beginner / developing)
│   ├── rhythm-worksheets.md          — 3 test prompts
│   ├── chorales.md                   — 3 test prompts
│   └── warm-ups.md                   — 3 test prompts
├── results/
│   └── YYYY-MM-DD-run.md             — one report per eval run (gitignored or committed)
└── band-materials-eval.md            — subagent prompt
```

Total: 12 test cases across 4 output types × 3 difficulty levels.

---

## Rubric

Each output is scored on four dimensions. Scores are 1–3.

| Score | Meaning |
|-------|---------|
| 1 | Fail — clear problem, needs fix |
| 2 | Acceptable — works but could be better |
| 3 | Strong — correct, specific, usable as-is |

### Dimension 1: Range/Notes Accuracy
Does every note in the output fall within the correct written range for the stated level?

- **3:** All notes within range; no errors
- **2:** Minor range issue (one note slightly outside, easily corrected)
- **1:** Notes clearly outside range; output is not usable for the stated level

**Reference ranges (written pitch for Bb trumpet):**
- Early beginner: C4–G4
- Beginner: C4–C5
- Developing: C4–F5

### Dimension 2: Specificity
Is the output tailored to the context (beginning band trumpet, stated level, concept focus), or is it generic enough to come from any source? Score this only on whether the output uses skill/instrument/concept context — not on difficulty calibration (that is Dimension 4).

- **3:** Output references the specific concept, level, and instrument with concrete detail
- **2:** Mostly specific; one or two generic filler elements
- **1:** Generic — could have been produced without any skill context at all

### Dimension 3: Pedagogical Soundness
Does the output follow correct teaching sequence? Does it build on prior skills correctly? Are instructions clear and logically ordered?

- **3:** Correct progression, no skipped prerequisites, clear step-by-step structure
- **2:** Mostly sound; minor sequencing issue or unclear step
- **1:** Skips prerequisites, teaches concepts in wrong order, or instructions are confusing

### Dimension 4: Level Appropriateness
Is the difficulty of the output a match for the stated student level? Score this only on difficulty calibration — not on whether the output names the level or instrument (that is Dimension 2).

- **3:** Difficulty is well-calibrated — not too easy, not too hard
- **2:** Slightly off (a bit too easy or a bit too hard) but usable
- **1:** Clearly wrong level — would frustrate or bore students at the stated level

---

## Flag Threshold

An output is **flagged** (subagent calls it out explicitly) if:
- Any single dimension scores **1**, OR
- The average score across all four dimensions is **below 2.0**

The threshold is applied to the exact average before rounding for display.

Outputs that pass the threshold appear in the **Passing** section of the report for human review.

---

## Eval Report Format

```markdown
# band-materials Eval — YYYY-MM-DD

**Summary:** X flagged, X passing of 12 total

**Top issues:** [1-3 bullet points on most common failure patterns, or "None — all passing"]

---

## Flagged (X of 12)

### [Output type] — [Level]
**Prompt:** [test prompt used]
**Scores:** Range: X | Specificity: X | Pedagogy: X | Level: X | Avg: X.X
**Flag reason:** [which dimension failed and why]
**Output:**
[full output from band-materials]

---

## Passing (X of 12)

### [Output type] — [Level]
**Prompt:** [test prompt used]
**Scores:** Range: X | Specificity: X | Pedagogy: X | Level: X | Avg: X.X
**Output:**
[full output from band-materials]

---
```

---

## Subagent Behavior (`band-materials-eval.md`)

The eval subagent:

1. Reads `eval/rubric.md` and all four test-case files
2. For each of the 12 test cases:
   a. Reads `mr-burger-music/skills/band-materials/skill.md` and executes its instructions directly to generate the output for the test prompt
   b. Scores the output on all four dimensions, using the test case's **Key checks** field to guide scoring focus for that specific case
   c. Determines pass/flag status
3. Writes a results file to `eval/results/YYYY-MM-DD-run.md`
4. Reports a summary: X flagged, X passing, top issues found

**The subagent does not fix issues** — it reports them. Fix decisions are made by the human after reviewing the report.

---

## Test Case Format (per file)

```markdown
# [Output Type] Test Cases

## Early Beginner
**Prompt:** [exact prompt to send to band-materials]
**Expected concept:** [what this should produce]
**Key checks:** [1-2 things the subagent should pay special attention to when scoring this case — used to guide rubric focus, not replace it]

## Beginner
...

## Developing
...
```

---

## Workflow

```
Run band-materials-eval agent
        ↓
Subagent generates + scores all 12 outputs
        ↓
Results file written to eval/results/
        ↓
Flagged section → subagent identifies failures + reasons
Passing section → human reviews for subtle issues
        ↓
Issues documented → skill fixes or knowledge gaps filed
        ↓
Re-run eval after fixes to verify improvement
```

---

## Future Expansion

When `band-materials` is expanded (jazz leadsheets, theory worksheets, text+notation guides, practice opportunities), new test-case files are added to `eval/test-cases/` and the rubric may gain additional dimensions. The subagent prompt is updated to include the new types. The existing 12 test cases remain as a regression suite.

---

## Out of Scope

- Scoring personal practice skill outputs (practice-planner, exercise-generator, music-coach) — separate eval if needed
- Automated fix generation — eval identifies problems, human decides fixes
- Score-writer eval — separate concern (output is a file, not text)
