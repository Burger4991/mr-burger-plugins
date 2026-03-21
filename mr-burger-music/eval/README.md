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
