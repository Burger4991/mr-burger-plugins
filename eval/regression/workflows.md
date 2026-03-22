# Regression Workflow Definitions

10 canonical multi-skill workflows for pre/post-change regression testing.

Each workflow defines the trigger, the skill/agent chain, handoff points,
and expected behavior at each stage. The eval subagent runs each workflow
end-to-end and verifies that every handoff produces the expected input for
the next stage.

---

## Workflow 1: IR Unit Build

**Trigger:** "Plan and build a 6-day unit on [text] for [benchmark]"

**Chain:** `unit-planner` agent → `unit-builder-protocol` skill → `quality-reviewer` agent

**Handoff points:**
1. unit-planner outputs a unit plan (big idea, essential questions, 6-day outline, standards alignment)
2. unit-builder-protocol receives the plan and builds deliverables (student packet, lesson plans, assessments, answer keys)
3. quality-reviewer receives all deliverables and runs Pass 1 (spec) + Pass 2 (quality)

**Expected behavior:**
- unit-planner references Florida BEST ELA standards, not generic ELA
- unit-builder-protocol produces files in the correct output location
- quality-reviewer catches any spec violations and returns specific fix instructions
- Final output: a complete, reviewed unit ready for classroom use

---

## Workflow 2: Student Data Pipeline

**Trigger:** "I just got PM3 data. Analyze it."

**Chain:** `student-data-processor` → `data-quality-checker` → `growth-analyzer` → `report-builder`

**Handoff points:**
1. student-data-processor ingests raw data (CSV/table) and structures it
2. data-quality-checker validates the structured data and flags issues
3. growth-analyzer calculates growth metrics on validated data
4. report-builder generates the final report/workbook

**Expected behavior:**
- Pipeline pauses at data-quality-checker if critical issues found (doesn't silently proceed)
- growth-analyzer uses the correct thresholds from its configuration
- report-builder produces the 16-sheet Excel format or equivalent structured output
- Each skill receives the output of the prior skill — no data loss between stages

---

## Workflow 3: Bellringer Generation

**Trigger:** "Create a bellringer for this week's vocabulary: [words]"

**Chain:** `bellringer-builder` → `vocabulary-instruction` (context) → `mc-question-generation` (if needed)

**Handoff points:**
1. bellringer-builder selects mode (Context Clue, Word Parts, Benchmark Vocab) based on input
2. Optionally references vocabulary-instruction for word selection criteria and scaffolding
3. Optionally uses mc-question-generation patterns for distractor design

**Expected behavior:**
- Mode selection matches the input (vocabulary words → Context Clue or Word Parts mode)
- STOP distractor pattern applied to all MC questions
- Output includes answer key with explanations
- ESOL modifications present

---

## Workflow 4: Observation Prep

**Trigger:** "I have an observation on [date] for [period/lesson]"

**Chain:** `observation-prep` → `ir-framework` (context) → `esol-core` (if ESOL students present)

**Handoff points:**
1. observation-prep generates the one-page reference sheet
2. References ir-framework for rotation model and lesson structure context
3. References esol-core for ESOL-specific differentiation strategies

**Expected behavior:**
- Output is one page / scannable — not a multi-page essay
- IR rotation model correctly described (3 stations)
- ESOL differentiation is level-specific (Entering vs. Developing vs. Bridging), not generic
- Danielson/Marzano alignment present and appropriate for the lesson described

---

## Workflow 5: Sub Plan

**Trigger:** "I need a sub plan for [date]"

**Chain:** `sub-folder-builder` (reference) → `sub-plan-generator` agent

**Handoff points:**
1. sub-folder-builder provides the standing reference folder (procedures, contacts, rosters)
2. sub-plan-generator creates the day-specific plan using the folder as context + the specific unit/day info

**Expected behavior:**
- sub-plan-generator produces a linear plan (no rotations for subs)
- All instructions are scripted with exact words, no jargon
- Backup activities included (3 alternatives)
- Answer keys provided for all student work
- Plan references the sub folder for standing info (doesn't duplicate it)

---

## Workflow 6: Data Analysis (Agent Orchestration)

**Trigger:** "Analyze my class data" (to data-analyst agent)

**Chain:** `data-analyst` agent orchestrates: `student-data-processor` → `data-quality-checker` → `growth-analyzer` → `class-comparison-generator` → `reporting-category-tracker` → `intervention-planner` → `report-builder` → `data-visualization-builder`

**Handoff points:**
1. data-analyst decides which skills to invoke based on the data provided
2. Each skill receives structured input from the prior skill's output
3. Agent pauses for user decisions at quality-check and grouping stages

**Expected behavior:**
- Agent follows the 6-phase sequence (Ingest → Validate → Analyze → Group → Report → Recommend)
- Doesn't skip validation even if data looks clean
- Pauses conversationally at decision points (doesn't assume thresholds)
- Final report is comprehensive, not just one metric

---

## Workflow 7: Music Practice

**Trigger:** "Let's do a practice session" (to music-coach agent)

**Chain:** `music-coach` agent → `practice-planner` skill → `session-logger` skill

**Handoff points:**
1. music-coach reads practice history and gathers session info
2. practice-planner structures the session with LHS blocks
3. After session, session-logger records what happened

**Expected behavior:**
- music-coach references the player status (trumpet comeback C4–C5, guitar beginner)
- Practice plan uses LHS block structure (fundamentals, outlines, embellish, application)
- Session is time-boxed based on user's available time
- Logger captures blocks used, what worked, what's hard, tomorrow's focus

---

## Workflow 8: Session Lifecycle

**Trigger:** `workflow-agent OPEN` → [work session] → `/wrap` → `workflow-agent CLOSE`

**Chain:** `workflow-agent` (open mode) → [user works] → `/wrap` command → `workflow-agent` (close mode)

**Handoff points:**
1. workflow-agent OPEN reads HANDOFF.md, PROJECT.md, TASKS.md → produces orientation
2. /wrap updates PROJECT.md, writes HANDOFF.md, updates TASKS.md
3. workflow-agent CLOSE verifies all state files are updated

**Expected behavior:**
- Open orientation includes: last session summary, active tasks, recommended start, watch-outs
- /wrap produces lean HANDOFF.md (not a full project dump)
- PROJECT.md updated with current phase, decisions, open questions
- TASKS.md has completed items marked with date, new items added
- Close mode doesn't duplicate /wrap work

---

## Workflow 9: Capture Flow

**Trigger:** `/capture` with mixed items

**Chain:** `/capture` command → `work-logger` skill → TASKS.md + area notes

**Handoff points:**
1. /capture parses and classifies items (task, teaching idea, career note, etc.)
2. Presents routing for approval before filing
3. work-logger handles the TASKS.md entries
4. Area-specific files get their respective items

**Expected behavior:**
- Items are pre-classified before asking for approval (not "where should this go?")
- Routing presented all-at-once, not one-by-one
- Each item goes to the correct destination file
- Time-sensitive items flagged for Reminders
- No items silently dropped

---

## Workflow 10: Score Transformation

**Trigger:** "Transform this score with [transformation type]"

**Chain:** `score-transformer` skill → `tools/` Python scripts → `score-writer` agent (if new score needed)

**Handoff points:**
1. score-transformer reads the .mscz file and identifies the transformation
2. Python scripts in tools/ perform the XML manipulation
3. If a net-new score is needed instead, routes to score-writer agent

**Expected behavior:**
- Correct .mscz file path used (not hallucinated)
- TPC convention applied correctly (tpc2 = tpc + 2 for Bb trumpet)
- Transformation logic matches the type requested (chromatic enclosure, diatonic enclosure, guide tones, 12-key transposer)
- PDF export step included
- 4-measure phrase structure preserved (ii-V-I-rest)
