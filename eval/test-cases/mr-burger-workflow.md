# mr-burger-workflow Smoke Test Cases

## Test Case 9: work-logger

**Skill:** `mr-burger-workflow/skills/work-logger/skill.md`

**Prompt:** I just finished building a Unit 7 student packet for my IR class. It's a
poetry unit covering ELA.10.R.1.4 (figurative language) and ELA.10.R.3.2 (poetry analysis).
The packet has 18 pages with 4 poems, annotation guides, and a CER assessment. Log this work.

**Expected concept:** A properly formatted TASKS.md entry and/or area note for a teaching
deliverable (unit/packet type). Should use the correct logging format with date, tags,
and relevant details.

**Key checks:**
- Uses the teaching/unit logging format (not data analysis or career)
- Includes today's date in YYYY-MM-DD format
- Tags reference the benchmarks (R.1.4, R.3.2)
- Notes are selective — captures key details (18 pages, 4 poems, CER assessment) without over-documenting
- Identifies correct primary log (TASKS.md) and secondary log if applicable
- Does NOT log trivial metadata

---

## Test Case 10: plugin-registry

**Skill:** `mr-burger-workflow/skills/plugin-registry/skill.md`

**Prompt:** I just ran a student data analysis for PM3 and it generated a growth report.
Which plugins were involved and where should the outputs live?

**Expected concept:** Identification of the cross-plugin data flow from ir-data-pipeline
(analysis) to mr-burger-workflow (task logging), with correct file locations.

**Key checks:**
- Identifies ir-data-pipeline as the source plugin for data analysis
- Identifies mr-burger-workflow as the destination for task logging
- References correct file paths for data outputs and TASKS.md
- Shows the cross-plugin data flow (analysis → tasks)
- Mentions relevant skills by name (student-data-processor, growth-analyzer, report-builder, work-logger)
- Does NOT confuse plugins or misroute outputs
