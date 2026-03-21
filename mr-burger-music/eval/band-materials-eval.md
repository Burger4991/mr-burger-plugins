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
