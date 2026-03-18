---
name: unit-builder-protocol
description: Step-by-step protocol for building complete 6-day IR units with quality standards and troubleshooting. Use when building full units or ensuring deliverable quality.
---

# Unit Builder Protocol

## When User Says "Build the Unit"

Generate all core deliverables plug-and-play (minimal revision needed):

**REQUIRED (Must be synchronized):**
1. **Teacher Lesson Plan (.md)** - 6-day detailed plans with bellringer answer keys
2. **Student Packet (.md)** - Day-by-day format with bellringers, Teacher-Led, Independent sections
3. **Slide Deck (.pptx)** - Visual support for instruction including bellringer slides

**ADDITIONAL:**
4. **Answer Key & Exemplars (.md)** - Complete responses with text evidence
5. **Feedback Forms (.md)** - IR-Feedback-Form for practice→feedback→revise workflow
6. **Exit Tickets (.md)** - Optional daily formative assessments
7. **Cover Pages (.md)** - Optional unit overview

**CRITICAL:** Files 1-3 must be synchronized (same vocabulary, same examples, same day structure)

## Context Management Protocol

<HARD-GATE>
Before starting any phase, verify that `_unit-spec.md` exists in the unit folder.
If it does not exist, STOP and invoke `menu-mode-planner` first. Never build from
conversational memory alone.
</HARD-GATE>

### Context Refresh Rule
At the start of EVERY phase, re-read `_unit-spec.md` from the unit folder. This is
non-negotiable. The spec file is the source of truth — not your memory of what
the user said 30 messages ago.

### Build State Tracking
After completing each phase, update `_build-state.json` in the unit folder with:
- Phase name and completion status
- Files created (paths)
- Key decisions made (e.g., vocabulary words selected, organizer type chosen)
- Any deviations from the spec (with rationale)

Format:
```json
{
  "unit": "Theme_TheNecklace",
  "spec_file": "_unit-spec.md",
  "phases": {
    "phase_1_gather": {
      "status": "complete",
      "files": [],
      "decisions": ["18 vocabulary words selected", "text chunked into 4 sections"],
      "completed_at": "2025-01-04T10:30:00"
    },
    "phase_2_plan": { "status": "pending" }
  }
}
```

### Curated Agent Briefings
When launching a sub-agent (student-packet-builder, assessment-builder, answer-key-builder, etc.),
construct a briefing from files — NOT from conversational context. The briefing must include:

1. The relevant sections of `_unit-spec.md` (not all of it — only what the agent needs)
2. The build state showing what previous phases produced
3. The specific skill content the agent needs (e.g., benchmark details, brand identity tokens)

**Anti-pattern:** "Build the student packet based on what we discussed."
**Correct pattern:** "Build the student packet. Here is the unit spec [paste relevant sections]. Here are the vocabulary words [from _unit-spec.md]. Here is the organizer structure [from Phase 2 output]. Follow student-packet-design-guide and brand-identity."

This ensures each agent starts with complete, accurate context regardless of how much
conversational context has decayed.

## Build Sequence

### Phase 1: Gather & Analyze
0. **Read the unit spec:**
   - Read `_unit-spec.md` from the unit folder
   - Verify benchmark, text source, and class context match expectations
   - If spec is missing, STOP and run menu-mode-planner

1. **Get materials from user:**
   - Target benchmark (e.g., ELA.10.R.1.2 - Theme)
   - Unit text (title, file, or upload)
   - Any district materials

2. **Read district files if provided:**
   - Use `district-files-reader` skill
   - Extract full text passage
   - Identify margin questions (PRESERVE EXACT WORDING)
   - Note vocabulary words
   - Review any district organizers

3. **Analyze benchmark requirements:**
   - Use `benchmarks` skill (see reference-guide.md)
   - Check Planning Cards for question stems
   - Review 9-10 Guide for achievement level descriptors
   - Identify assessment limits

### Phase 2: Plan Structure
0. **Context refresh:**
   - Re-read `_unit-spec.md` (refresh context)
   - Read `_build-state.json` for Phase 1 outputs

1. **Select vocabulary for bellringers:**
   - Choose 30 words total from unit text (5 per day × 6 days)
   - Must be Tier 2 academic or domain-specific words
   - Must appear in sentences with strong context clues
   - Distribute across Days 1-6

2. **Design 6-day outline:**
   - EVERY DAY: Bellringer (5-10 min) + 3 rotations (20 min each)
   - Days 1-2: Vocab/concepts + first read activities
   - Days 3-4: Organizer structure + guided practice activities
   - Days 5-6: Assessment format + STOP/CER activities

3. **Select ESOL strategies:**
   - Minimum 2 different strategies per day
   - Rotate strategies across the week (don't repeat same ones)
   - Match strategy to task complexity

4. **Identify modifications needed:**
   - Reduced items for assessments
   - Sentence frames for writing tasks
   - Word banks for vocabulary
   - Oral administration options

### Phase 3: Build Lesson Plan (.md format)
0. **Context refresh:**
   - Re-read `_unit-spec.md` (refresh context)
   - Read `_build-state.json` for Phase 1-2 outputs
   - Construct agent briefing if using lesson-plan-coordinator agent

1. **Create bellringer answer keys (each day):**
   - Word, definition, context clues, acceptable variations
   - How to review with students
   - Tier 2/3 support notes

2. **Create daily lesson plans:**
   - Use `ir-framework` skill for structure
   - Include bellringer section FIRST (5-10 min)
   - Include exact benchmark number + clarification
   - Write specific, measurable objectives
   - Time each activity (must total 20 minutes per rotation)
   - Embed ESOL strategies with labels
   - Include CFU methods

3. **Design benchmark organizer:**
   - Use `organizer-design` skill
   - Map to benchmark card steps
   - Create 4 rows: I Do, We Do, You Do w/ Partner, You Do

4. **Write teacher scripts:**
   - I Do: Full think-aloud script
   - We Do: Guiding questions for collaboration
   - You Do w/ Partner: Directions and sentence frames
   - You Do: Monitoring checklist

5. **Output format:**
   - Generate as .md file (Markdown format)
   - Use Markdown heading and table structures

### Phase 4: Build Student Packet (.md format)

**CRITICAL: Student packet MUST be organized DAY-BY-DAY, not activity-by-activity**

0. **Context refresh:**
   - Re-read `_unit-spec.md` (refresh context)
   - Read `_build-state.json` for Phase 1-3 outputs
   - Construct agent briefing: spec sections + vocabulary + organizer + brand identity

1. **For each day, create in this order:**
   - **Context Clues Bellringer** (5-10 min) - 5 vocabulary words from unit text
   - **Teacher-Led Activities** (20 min) - Organizers, guided practice, notes
   - **Independent Activities** (20 min) - Self-running tasks, comprehension questions

2. **Bellringer creation for each day:**
   - Select 5 Tier 2/domain-specific words from unit text
   - Pull exact sentence from text with target word
   - Include paragraph number reference
   - Format: "Word: _______ My definition: _______"

3. **Convert margin questions to MC (for Independent sections):**
   - Use exact wording from source text
   - Create 4 choices using STOP protocol (Silly, Tricky, Opposite, Proven)
   - Add paragraph number references

4. **Add student-friendly elements:**
   - Clear day headers: "DAY [#]: [Title/Focus]"
   - Section headers with icons (📚 Bellringer, 👨‍🏫 Teacher-Led, 📝 Independent)
   - Numbered directions (bold key action words)
   - "Need Help?" troubleshooting section
   - Plenty of white space

5. **Embed feedback checkpoints from benchmark skill:**
   - Read the benchmark skill being used for this unit
   - Locate the "## Feedback Checkpoints" section in that skill
   - Extract Day 4 and Day 6 checkpoint content

   **Day 4 placement:** After organizer activity in Independent Center section
   - Insert heading: `===================================`
   - Insert heading: `📋 ORGANIZER CHECKPOINT`
   - Insert heading: `===================================`
   - Insert Day 4 checkpoint content from benchmark skill

   **Day 6 placement:** After RACE response in Independent Center section
   - Insert heading: `===================================`
   - Insert heading: `📋 RACE RESPONSE CHECKPOINT`
   - Insert heading: `===================================`
   - Insert Day 6 checkpoint content from benchmark skill

   **Example:** For Theme unit (ELA.10.R.1.2), read feedback checkpoints from `benchmarks` skill (see standards/theme.md) and embed in student packet.

6. **Output format:**
   - Generate as Markdown (.md)
   - NOT activity-by-activity structure
   - Each day = one section with all 3 components

### Phase 5: Create Answer Key (.md format)
0. **Context refresh:**
   - Re-read `_unit-spec.md` (refresh context)
   - Read `_build-state.json` for Phase 1-4 outputs
   - Construct agent briefing: spec + lesson plan + student packet content

1. **Provide complete answers:**
   - Bellringer answer keys (word, definition, context clues, acceptable variations)
   - All MC questions with correct answer + STOP justifications
   - Completed organizer with exemplar responses (what proficient looks like)
   - Vocabulary answers with explanations
   - Assessment answers with full RACE/CER responses

2. **Include text evidence:**
   - Cite paragraph numbers for every answer
   - Use quotations where appropriate
   - Show reasoning for why other choices are incorrect

3. **Output format:**
   - Generate as Markdown (.md)
   - Organize by day for easy reference

### Phase 6: Design Support Materials
1. **Slide deck (.pptx format):**
   - Organize slides by day (Day 1 slides, Day 2 slides, etc.)
   - **Each day includes:**
     - Bellringer slide (for projection during warm-up)
     - Benchmark/vocabulary introduction slides
     - I Do examples (modeled with think-aloud)
     - We Do practice prompts
     - You Do preview
   - Use python-pptx to generate
   - Must align with lesson plan and student packet content

2. **Feedback forms (.md format):**
   - Use `feedback-system` skill for structure
   - IR-Feedback-Form.md (print-ready)
   - Includes Days 1-2, 3-4, 5-6 checklists
   - Verbal feedback sections (students transcribe)
   - Student Action Plan section
   - Note in student packet: "This is PRACTICE. You will receive feedback and revise before submitting online."

3. **Exit tickets (.md format):**
   - 1-2 questions per day aligned to daily objective
   - Quick formative checks (2-3 minutes max)

4. **Cover pages (.md format):**
   - List of embedded routines
   - Benchmark numbers + clarifications
   - Materials overview
   - Unit timeline

5. **Synchronization check:**
   - Verify vocabulary matches across all 3 files (lesson plan, student packet, slides)
   - Verify organizers match across all 3 files
   - Verify examples match across all 3 files
   - Verify day structure aligns

## Critical Quality Standards

### Every Deliverable Must Have:
- **Professional tone** (teacher-facing: lesson plans, answer keys)
- **Friendly tone** (student-facing: packets, directions)
- **20-minute pacing** for each rotation task
- **Exact benchmark language** from BEST Standards
- **Text evidence** with paragraph citations for all answers
- **"Pulled from:" citations** to source files

### Lesson Plan Must Include:
- Benchmark number + exact clarification text
- Daily measurable objectives
- Materials list
- Procedures with timing
- 2+ ESOL strategies (labeled)
- Engagement strategies (TWPS, Cold-Call, etc.)
- CFU methods
- Exemplar model rows for organizers
- Teacher script for gradual release
- Differentiation summary
- **Feedback timing notes:** When to give feedback (see `feedback-system` skill)
  - Days 1-2: "Spot-check 5-8 students during IND rotation"
  - Days 3-4: "Collect organizers end of Day 4, return with feedback Day 5"
  - Days 5-6: "Return assessments with feedback, students complete Action Plan"

### Student Packet Must Include:
- Cover page (unit name, benchmark, Days 1-6)
- **Day-by-day structure** (NOT activity-by-activity)
- **Each day section with:**
  - 📚 Context Clues Bellringer (5 vocabulary words from unit text)
  - 👨‍🏫 Teacher-Led activities
  - 📝 Independent activities
- Student-friendly numbered directions
- Self-running tasks
- Sentence frames for ESOL support
- Word banks where appropriate
- "Need Help?" section
- White space and readability (12pt+ font)
- **Format: .md (Markdown)** (use python-docx)

### Organizer Must Include:
- Alignment to benchmark card steps
- I Do row: Complete with citations
- We Do row: Partially complete
- You Do w/ Partner row: Sentence starters
- You Do row: Blank or minimal scaffolds
- Space for paragraph number citations

## Scaffold Removal System

**CRITICAL: Systematically remove scaffolds by Day 5** per benchmark Achievement Level Descriptors

- **Day 1-2**: Maximum support
  - Sentence frames for all writing
  - Word banks provided
  - Exemplars shown
  - Partner work encouraged

- **Day 3-4**: Moderate support
  - Some sentence starters (not full frames)
  - Partial word banks (not complete lists)
  - Reference to previous examples
  - Mix of partner and independent work

- **Day 5-6**: Minimal support (assessment conditions)
  - No sentence frames (students write independently)
  - No word banks (students recall vocabulary)
  - Assessment format
  - Intervention available but not proactive

## Troubleshooting: If Missing Materials

### If missing unit text:
- **Prompt user:** "Please provide the text title or upload the passage"
- **Offer:** "I can work with a text title and research it, or wait for you to upload"
- **Don't:** Proceed without knowing the text

### If missing organizer template:
- **Create one:** Use benchmark card to build structure from scratch
- **Use:** `organizer-design` skill
- **Verify:** Show user the structure before building full unit

### If only benchmark (no text):
- **Request:** "Which text will you use for this benchmark?"
- **Offer options:** "I can suggest grade-appropriate texts for [benchmark], or you can provide one"

## Formatting Standards

### File Naming:
- Format: `[UnitName]_[Days]_[Type]_YYYYMMDD`
- Examples:
  - `Theme_D1-6_TeacherPlan_20250104.md`
  - `Theme_D1-6_StudentPacket_20250104.md`

### Document Format:
- Editable: DOCX or PPTX (not PDF)
- Font: Arial or Calibri, 12pt minimum for students
- Margins: 1 inch all sides
- Page numbers on all pages
- Headers: Unit name, day number

## Version Control Protocol

### When Building New Unit:
1. Create with today's date: `UnitName_D1-6_Type_20250104.md`
2. Save all 6 deliverables in unit folder
3. Create change log: `_ChangeLog.txt`

### When Updating Existing Unit:
1. Create new version with new date: `UnitName_D1-6_Type_20250110.md`
2. Move old version to `_archive/` subfolder
3. Update change log with what changed
4. Use `sync-coordinator` to check alignment across deliverables

### Change Log Format:
```
2025-01-10: Updated student packet - added 5th organizer row
  → Updated: lesson plan (Day 4 procedure), answer key (exemplar row 5)
  → No change needed: assessment, slides
2025-01-04: Initial unit creation
```

## Pre-Delivery Checklist

Before reporting "unit complete," verify:
- [ ] All deliverables created (6 core + feedback form)
- [ ] Files named with today's date and proper extensions (.md, .pptx)
- [ ] **Student packet organized day-by-day** (NOT activity-by-activity)
- [ ] **Each day includes bellringer** (5 vocabulary words from unit text)
- [ ] **Three files synchronized:** lesson plan (.md), student packet (.md), slides (.pptx)
- [ ] Vocabulary matches across all 3 files
- [ ] Organizer content matches across all 3 files
- [ ] Examples match across all 3 files
- [ ] Benchmark number cited in every deliverable
- [ ] Margin questions preserved word-for-word
- [ ] Organizer aligned to benchmark card
- [ ] Gradual release explicitly shown (I Do → We Do → You Do)
- [ ] 2+ ESOL strategies per day
- [ ] All answers have text evidence with paragraph numbers
- [ ] 20-minute pacing for each rotation
- [ ] Student tasks are self-running
- [ ] "Pulled from:" sources cited in lesson plan
- [ ] Bellringer answer keys in lesson plan
- [ ] **Feedback form generated** (IR-Feedback-Form.md)
- [ ] **Student packet includes practice note:** "This is PRACTICE work - you will receive feedback and revise before submitting online"
- [ ] **Lesson plan includes feedback timing** for Days 1-2, 3-4, 5-6
- [ ] **Feedback checkpoints embedded** from appropriate benchmark skill
- [ ] **Day 4 checkpoint** appears after organizer in Independent section
- [ ] **Day 6 checkpoint** appears after RACE response in Independent section
- [ ] Checkpoint criteria match the benchmark being taught

## Coordination with Other Agents

**Relationship to teaching agents:**

| Agent | Role | When This Skill Uses It |
|-------|------|------------------------|
| **unit-planner** | General unit design (any subject, UbD framework) | Use for initial pedagogical planning before IR build |
| **lesson-plan-coordinator** | Single-lesson planning | Use for ad-hoc lesson revisions outside the 6-day cycle |
| **student-packet-builder** | Student-facing materials | Phase 4 of this protocol covers IR packets; use agent for non-IR or standalone materials |

**This skill is the IR-specific orchestrator.** It coordinates the full 6-day build sequence and generates all deliverables. The agents above handle broader or more targeted requests outside the IR context.

After completing unit build:
- Report to user: "Unit complete. All 6 deliverables ready."
- List what was created with file names
- Offer: "Would you like me to use `sync-coordinator` to verify alignment?"
