---
name: menu-mode-planner
description: >
  MUST USE this skill whenever the user wants to plan, build, create, design, set up, or start ANY
  new IR unit — regardless of how the request is phrased. Trigger on: "build a unit", "plan a unit",
  "new unit on [benchmark]", "set up a unit", "design a unit", "start a new 6-day cycle", "let's do
  [benchmark] next", "help me put together a unit", "I want to teach [benchmark/topic]", or ANY
  mention of starting fresh unit work for a specific benchmark or text. Also trigger when the user
  names a benchmark (R.1.1, R.1.2, R.1.3, R.1.4, R.2.1-R.2.4, R.3.1, R.3.4) in the context of
  planning instruction. This is the ENTRY POINT — always use this BEFORE unit-builder-protocol.
  Collects all preferences upfront via multi-tab questionnaire: benchmark selection, text passage,
  vocabulary words, CR framework choice (RACE default / CER for argument), daily activity choices,
  ESOL levels, and deliverable options. After collecting preferences, hands off to
  unit-builder-protocol which chains all relevant skills (benchmarks, ir-framework,
  vocabulary-instruction, bellringer-builder, organizer-design, cubes-annotation,
  gradual-release-scripts, assessment-design, assessment-rubrics, cer-writing-guide,
  student-packet-design-guide, esol-core, feedback-system, feedback-checkpoint-builder,
  teaching-templates). Use when starting a new unit, planning a unit, or when the user says
  "build a unit".
---

# Menu Mode Planner - Interactive Unit Setup

## Purpose
Collect ALL planning decisions upfront through a comprehensive multi-tab questionnaire BEFORE building any unit materials. Eliminates mid-build interruptions and ensures complete requirements are gathered.

## When to Use
- User says "plan a new unit" or "build a unit"
- User says "let's plan [benchmark] unit"
- User wants to design a full 6-day cycle
- Starting any new IR unit from scratch

## Optional Pre-Step: Unit Discovery

Before running the planning menu, you can gather context with `unit-discovery` skill:
- If user has district-provided files → invoke `district-files-reader` via `unit-discovery`
- If user has student PM/FAST data to factor in → invoke `unit-discovery` first
- If user is unsure which benchmark to target → invoke `unit-discovery` for data-informed recommendation

**When to offer discovery:**
Ask: "Before we start planning — do you have district files, student data, or any context you want me to factor in first?"
- If yes → invoke `unit-discovery` skill, then return here with pre-loaded context
- If no → proceed directly to Tab 1

**When NOT to offer discovery:**
- User already knows exactly what they want (benchmark, text, preferences clear)
- User explicitly says "just build it" or provides all details upfront

## DO NOT Use When
- User provides complete specifications already
- User is editing/updating existing unit
- User just wants one specific deliverable
- User has already made all decisions

## Hard Gate: Design Before Building

<HARD-GATE>
Do NOT create any deliverable, write any .md file, invoke any builder agent, or start
unit-builder-protocol until the user has completed ALL menu tabs and confirmed the
UNIT_CONFIG summary. This applies regardless of how "simple" the request seems.

Even if the user says "just build it," walk them through the menu. Unexamined assumptions
cause the most rework. The menu takes 2-3 minutes; rebuilding a wrong unit takes 30+.
</HARD-GATE>

**Anti-pattern:** "The user said Theme unit with this text — I know enough to start building."
**Reality:** You don't know CR tier, organizer type, frame density, class composition, difficulty ramp, or assessment structure. Every skipped question is a coin flip on rework.

## Menu Structure

Present questions using AskUserQuestion tool in sequence. Each question = one "tab" of the planning menu.

---

## TAB 1: Unit Basics (header: "Unit Setup")

### Question 1: Which benchmark are you targeting?
**Header:** "Benchmark"
**MultiSelect:** false

**Options:**
- **ELA.10.R.1.1 Literary Elements** - "Analyze character, setting, and plot interaction"
- **ELA.10.R.1.2 Theme** - "Analyze universal themes and development"
- **ELA.10.R.1.3 Coming of Age & Conflicting Perspectives** - "Analyze coming-of-age experiences and how author represents conflicting perspectives"
- **ELA.10.R.1.4 Poetry** - "Analyze layers of meaning and ambiguity in poetry"
- **ELA.10.R.2.1 Text Structure** - "Analyze organizational patterns in informational texts"
- **ELA.10.R.2.2 Central Idea** - "Analyze central ideas and supporting details"
- **ELA.10.R.2.3 Purpose & Perspective** - "Analyze author's purpose and perspective"
- **ELA.10.R.2.4 Argument** - "Evaluate arguments, claims, and evidence"
- **ELA.10.R.3.1 Figurative Language** - "Interpret figurative language and analyze mood"
- **ELA.10.R.3.4 Rhetoric** - "Analyze rhetorical devices and appeals"

### Question 2: What is your unit text source?
**Header:** "Text Source"
**MultiSelect:** false

**Options:**
- **District files uploaded** - "I have district PDF/Word files with text and materials"
- **Text title to research** - "I'll provide a title and you research/find the text"
- **Public domain text** - "Use Project Gutenberg or other public domain source"
- **I'll paste the text** - "I have the text ready to paste directly"

---

## TAB 2: Class Context (header: "Your Class")

### Question 1: What's your class composition?
**Header:** "Class Type"
**MultiSelect:** false

**Options:**
- **High ESOL (50%+ ELLs)** - "Heavy scaffolding, extra visuals, simplified language, sentence frames throughout"
- **Mixed abilities (standard IR)** - "Standard scaffolding with gradual release, 2+ ESOL strategies per day"
- **ESE inclusion** - "Significant modifications, reduced items, oral administration options, extended time"
- **Advanced/honors students** - "Minimal scaffolding, faster pace, extension activities, deeper analysis"

### Question 2: Do you have existing district materials? (multiSelect: true)
**Header:** "Materials"
**MultiSelect:** true

**Options:**
- **District organizer template** - "Template provided by district for this benchmark"
- **Pre-made margin questions** - "Questions already written in district materials"
- **District vocabulary list** - "Specific words district wants taught"
- **Assessment items** - "District-created MC or CR questions"

---

## TAB 3: CR Framework & Assessment (header: "Writing & Assessment")

### Question 1: Which constructed response framework for this unit?
**Header:** "CR Framework"
**MultiSelect:** false

**Options:**
- **RACE (default)** - "Restate-Answer-Cite-Explain — best for most benchmarks. Students struggle with Restate and Explain steps."
- **CER (argument units)** - "Claim-Evidence-Reasoning — use for R.2.4 Argument and R.2.3 Purpose & Perspective. Note: 'claim' is tricky in ELA."

**Note:** One framework per unit, never mixed. See `cer-writing-guide` for full details. Whichever is chosen, the systematic scaffolding stays the same: Days 1-2 Restate/Claim practice → Days 3-4 Explain/Reasoning scaffolding → Days 5-6 full independent CR.

### Question 2: What CR tier are your students at?
**Header:** "CR Tier"
**MultiSelect:** false

**Options:**
- **Lite (Semester 1)** - "R+A only — students practice Restate and Answer (or Claim and Evidence for CER). Simplest form."
- **Standard (Semester 2 start)** - "R+A+C — adds Cite step. Students quote text with paragraph numbers."
- **Full (Semester 2 mid+)** - "R+A+C+E — full framework including Explain. Goal by end of year."

### Question 3: Assessment format confirmation
**Header:** "Assessment"
**MultiSelect:** false

**Options:**
- **Standard (Recommended)** - "Mini-assessment: 6-8 MC (80% benchmark / 20% vocabulary) + 1 CR. Unit assessment: 10-12 MC (80/20) + 1-2 CRs."
- **Lighter** - "Mini-assessment: 4-6 MC + 1 CR. For units with heavy new content or early semester."

---

## TAB 4: Text Chunking & Pacing (header: "Text & Pacing")

### Question 1: How should the text be split across 6 days?
**Header:** "Text Split"
**MultiSelect:** false

**Options:**
- **Even split** - "Divide text roughly equally across Days 1-4 (reading days). Days 5-6 are assessment — students reference full text."
- **Front-loaded** - "Most reading on Days 1-2, Days 3-4 focus on re-reading key passages for analysis. Good for shorter texts."
- **Back-loaded** - "Intro + context Days 1-2, main text Days 3-4. Good for complex texts that need vocabulary/background first."
- **I'll specify** - "I want to tell you exactly which paragraphs/sections go on which day."

**Note:** If the user selects "I'll specify," ask a follow-up for paragraph/section assignments per day.

### Question 2: Which instructional mode per day pair?
**Header:** "Daily Mode"
**MultiSelect:** false

**Options:**
- **Default Rotations all 6 days** - "20 min Teacher-Led → 20 min Independent → 20 min Technology. Standard IR model."
- **Workshop for Days 3-4** - "Rotations Days 1-2 & 5-6, Workshop (mini-lesson → extended work time → share-out) Days 3-4. Good for deep organizer work."
- **Flexible Stations Days 3-4** - "Rotations Days 1-2 & 5-6, Stations (2-4 stations, student choice) Days 3-4. Good for differentiation."
- **I'll specify per day** - "I want to choose the mode for each day individually."

### Question 3: How steep should the difficulty ramp be?
**Header:** "Difficulty"
**MultiSelect:** false

**Options:**
- **Gradual (standard)** - "Days 1-2: DOK 1-2 (recall, identify). Days 3-4: DOK 2-3 (analyze, compare). Days 5-6: DOK 2-3 (apply, evaluate). Steady climb."
- **Steep** - "Days 1-2: DOK 1 only (recall, define). Days 3-4: Jump to DOK 2-3. Days 5-6: DOK 3 (analyze, evaluate). For classes that need more scaffolding early."
- **Flat/even** - "DOK 2 throughout all 6 days. For classes that can handle consistent rigor. Good for advanced or late-semester units."

---

## TAB 5: Deliverables (header: "What to Build")

### Question: Which deliverables do you need? (multiSelect: true)
**Header:** "Deliverables"
**MultiSelect:** true

**Options:**
- **Teacher Lesson Plan (.md)** - "Required: 6-day detailed plans with bellringer keys, scripts, ESOL strategies, feedback timing"
- **Student Packet (.md)** - "Required: Day-by-day format following student-packet-design-guide (Arial, 12pt, sentence frames, organizers)"
- **Answer Key & Exemplars (.md)** - "Complete responses with text evidence, STOP justifications, and CR model response at chosen tier"
- **Feedback Forms (.md)** - "Practice→feedback→revise→submit forms (see feedback-system skill)"
- **Exit Tickets (.md)** - "Daily formative assessments (1-2 questions per day)"
- **Cover Pages (.md)** - "Unit overview with benchmarks, routines, materials list"

**Note:** First 2 are always required (Teacher Lesson Plan, Student Packet). Answer Key is strongly recommended.

---

## TAB 6: Days 1-2 Details (header: "Days 1-2")

### Context for User:
"Days 1-2 build the foundation: vocabulary, first read, comprehension. CR scaffolding embeds Restate practice. Questions stay DOK 1-2."

### Question 1: Teacher-Led focus for Days 1-2? (multiSelect: true)
**Header:** "Teacher-Led"
**MultiSelect:** true

**Options:**
- **Vocabulary instruction** - "Teach 6 Tier 2/3 words (Days 1-2 bellringer words) with visuals, gestures, context sentences"
- **Benchmark introduction + anchor chart** - "Explicitly teach the benchmark concept with anchor chart. Students copy key terms."
- **CUBES annotation modeling** - "Model 3-step layered annotation on first paragraphs of text (see cubes-annotation skill)"
- **Text preview with prediction** - "Activate background knowledge, preview text structure, set purpose for reading"

### Question 2: Independent focus for Days 1-2? (multiSelect: true)
**Header:** "Independent"
**MultiSelect:** true

**Options:**
- **First read + annotation** - "Read assigned section with CUBES annotation (underline key details, circle unknown words, box names/dates)"
- **Comprehension MC with process of elimination** - "4-6 MC questions (DOK 1-2) with explicit 'cross out 2 wrong answers first' instruction"
- **Margin questions as MC** - "Convert district margin questions to MC format (keep exact wording from district files)"
- **Vocabulary context clues practice** - "Match bellringer words to definitions using text context (ties to bellringer skill-building)"

### Question 3: What sentence frames do you want on Days 1-2?
**Header:** "Frames D1-2"
**MultiSelect:** true

**Options:**
- **Discussion frames only** - "'Language to Discuss' boxes: 'I noticed that...', 'This reminds me of...', 'I think the author is saying...'"
- **Restate practice frames** - "CR-step frames for Restate: 'The question is asking about...', 'In this passage, the author explores...'"
- **Both discussion + Restate** - "Include both types (Recommended — matches CR scaffolding progression)"
- **Minimal (advanced classes)** - "One 'Language to Discuss' box only — for classes that don't need heavy framing"

---

## TAB 7: Days 3-4 Details (header: "Days 3-4")

### Context for User:
"Days 3-4 are the analysis core: benchmark organizer with gradual release, text evidence, deeper questions. CR scaffolding embeds Explain practice via the organizer's Analysis column."

### Question 1: Which organizer type for this benchmark?
**Header:** "Organizer"
**MultiSelect:** false

**Options:**
- **2-column Evidence + Analysis** - "Left: text evidence (quote + para #). Right: analysis/explanation. Best for Theme, Central Idea, Purpose."
- **3-column Evidence + Analysis + Connection** - "Adds a 'So What?' or connection column. Best for Perspective, Argument, Rhetoric."
- **Concept map (radial)** - "Central concept with branches. Best for Figurative Language, Literary Elements, Poetry."
- **I'll describe what I want** - "I have a specific organizer layout in mind."

### Question 2: How many organizer rows and what gradual release?
**Header:** "Rows & GR"
**MultiSelect:** false

**Options:**
- **4 rows: I Do (1) → We Do (1) → You Do w/ Partner (1) → You Do (1)** - "Standard progression. I Do row pre-filled with gray background."
- **5 rows: I Do (1) → We Do (2) → You Do w/ Partner (1) → You Do (1)** - "Extra We Do row for classes needing more guided practice."
- **5 rows: I Do (1) → We Do (1) → You Do w/ Partner (1) → You Do (2)** - "Extra independent row for classes ready for more practice."

### Question 3: Teacher-Led focus for Days 3-4? (multiSelect: true)
**Header:** "Teacher-Led"
**MultiSelect:** true

**Options:**
- **Gradual release organizer modeling** - "I Do think-aloud → We Do shared practice → release to partners/independent"
- **Text evidence mini-lesson** - "How to locate, cite (with para #), and explain evidence. 'The author states... This shows...'"
- **Close reading of key passage** - "Reread 1-2 key paragraphs for deeper analysis (word choice, structure, implicit meaning)"
- **Vocabulary in context** - "Revisit bellringer words where they appear in the unit text"

### Question 4: Independent focus for Days 3-4? (multiSelect: true)
**Header:** "Independent"
**MultiSelect:** true

**Options:**
- **Complete organizer You Do rows** - "Finish independent + partner rows of the benchmark organizer"
- **Text-dependent MC questions** - "DOK 2-3 questions using Planning Card stems (analysis level)"
- **Quote analysis activity** - "Select key quotes, explain what they reveal about [benchmark element]"
- **Partner annotation** - "Collaborative CUBES re-annotation focused on benchmark-specific elements"

### Question 5: What sentence frames do you want on Days 3-4?
**Header:** "Frames D3-4"
**MultiSelect:** true

**Options:**
- **Discussion frames** - "'Language to Analyze' boxes: 'The evidence suggests...', 'This connects to [benchmark] because...'"
- **CR-step frames for Explain** - "Scaffolded frames for the Explain step: 'This evidence shows [benchmark element] because...'"
- **Both discussion + Explain** - "Include both types (Recommended — matches CR scaffolding progression)"
- **Minimal (advanced classes)** - "One 'Language to Analyze' box only"

---

## TAB 8: Days 5-6 Details (header: "Days 5-6")

### Context for User:
"Days 5-6 are assessment and application: STOP protocol for MC, full independent CR writing, mini-assessment. CR scaffolding culminates in full independent response at chosen tier."

### Question 1: Teacher-Led focus for Days 5-6? (multiSelect: true)
**Header:** "Teacher-Led"
**MultiSelect:** true

**Options:**
- **STOP protocol modeling (Day 5)** - "Model Silly/Tricky/Opposite/Proven with a sample MC question. Students practice labeling each choice."
- **CR writing instruction (Day 5)** - "Model full RACE or CER response at current tier using a NEW text-dependent prompt (not the assessment prompt)"
- **Small group intervention (Day 6)** - "Pull 4-6 struggling students based on Read 180 data or Day 4 organizer feedback for targeted reteach"
- **Assessment review (Day 6)** - "Quick review of common errors from practice work before students take mini-assessment"

### Question 2: Assessment structure for Days 5-6?
**Header:** "Assessment"
**MultiSelect:** false

**Options:**
- **Practice Day 5 + Assessment Day 6** - "Day 5: STOP practice MC + CR draft with feedback. Day 6: Mini-assessment (graded). Recommended."
- **Assessment split across both days** - "Day 5: MC portion. Day 6: CR portion. For classes that need more time."
- **Both days as practice + take-home assessment** - "Both days are practice with feedback. Assessment is a separate document for a 7th day or in-class submission."

### Question 3: What should the CR prompt assess?
**Header:** "CR Prompt"
**MultiSelect:** false

**Options:**
- **Same text, new prompt** - "Students write about the unit text but with a prompt they haven't seen. Tests transfer of benchmark skill."
- **New short passage** - "Provide a new 1-2 paragraph passage. Students apply benchmark skill to unfamiliar text. Harder but better measure."
- **Choice of prompts** - "Offer 2 prompts (one easier, one harder). Students choose. Good for differentiation."

### Question 4: What sentence frames on Days 5-6?
**Header:** "Frames D5-6"
**MultiSelect:** false

**Options:**
- **Full CR frames (scaffolded)** - "Labeled frames for each RACE/CER step. 'Restate: The question asks about... Answer: In this text...' For Lite/Standard tiers."
- **Starter only** - "Just the opening sentence starter: 'In [text title], the author...' For Full tier or advanced classes."
- **No frames (independent)** - "Students write without frames. Only for Full tier classes with strong writers."
- **Frames on practice, none on assessment** - "Day 5 practice includes frames. Day 6 assessment removes them. Tests independence."

---

## TAB 9: Google Classroom Integration (header: "Google Classroom")

### Question 1: Do you want Google Classroom assignments included?
**Header:** "Google Classroom"
**MultiSelect:** false

**Options:**
- **Yes, create assignment list** - "I'll generate a list of Google Classroom assignments with titles, descriptions, due dates"
- **Yes, with assignment templates** - "I'll create detailed assignment instructions ready to copy-paste into Google Classroom"
- **No, I'll handle Google Classroom myself** - "Skip Google Classroom integration"

### Question 2 (if user selected "Yes"): Which Google Classroom assignment types? (multiSelect: true)
**Header:** "Assignment Types"
**MultiSelect:** true

**Options:**
- **Google Forms (quizzes)** - "Interactive MC and short answer quizzes"
- **Google Docs (uploads)** - "Students submit written responses, organizers, reflections"
- **Discussion posts** - "Prompts for student discussion and feedback"
- **Google Sheets (data collection)** - "Vocabulary tracking, self-assessment, data recording"
- **Reflection journals** - "Daily or end-of-unit reflection prompts"

---

## TAB 10: Special Priorities (header: "Priorities")

### Question: Any special priorities for this unit? (multiSelect: true)
**Header:** "Focus Areas"
**MultiSelect:** true

**Options:**
- **Heavy vocabulary focus** - "Prioritize vocabulary instruction, include extra vocab activities"
- **CR writing emphasis** - "Include additional RACE or CER practice, model responses, extra sentence frames"
- **Visual/graphic organizer heavy** - "More organizers, charts, diagrams for visual learners"
- **Technology integration** - "Incorporate tech tools beyond Read 180 (Padlet, Jamboard, etc.)"
- **Small group differentiation** - "Include leveled activities, tiered tasks, intervention plans"
- **Test prep focus** - "Align closely to FSA/state test format and question stems"

---

## TAB 11: Submit & Confirm (header: "Review")

### Display Summary
Show user a summary of all selections made:

```
UNIT PLAN SUMMARY
=================

UNIT BASICS:
Benchmark: ELA.10.R.1.2 (Theme)
Text Source: District files uploaded
Class Type: High ESOL (50%+ ELLs)

CR FRAMEWORK & ASSESSMENT:
Framework: RACE (default) — Tier: Lite (R+A only)
Assessment: Standard — 6-8 MC (80/20) + 1 CR per mini-assessment

TEXT & PACING:
Text Split: Even split across Days 1-4
Daily Mode: Default Rotations all 6 days
Difficulty Ramp: Gradual (DOK 1-2 → DOK 2-3 → DOK 2-3)

DELIVERABLES:
✓ Teacher Lesson Plan (.md)
✓ Student Packet (.md) — follows student-packet-design-guide
✓ Answer Key & Exemplars (.md)

DAYS 1-2:
Teacher-Led: Vocabulary instruction, Benchmark intro + anchor chart, CUBES annotation modeling
Independent: First read + annotation, Comprehension MC with process of elimination
Frames: Both discussion + Restate practice frames
CR Scaffolding: Restate practice embedded

DAYS 3-4:
Teacher-Led: Gradual release organizer modeling, Text evidence mini-lesson
Independent: Complete organizer You Do rows, Text-dependent MC (DOK 2-3)
Organizer: 2-column Evidence + Analysis, 4 rows (I Do → We Do → YDwP → YD)
Frames: Both discussion + Explain frames
CR Scaffolding: Explain scaffolding via organizer Analysis column

DAYS 5-6:
Teacher-Led: STOP protocol modeling (Day 5), CR writing instruction (Day 5), Small group (Day 6)
Assessment: Practice Day 5 + Assessment Day 6
CR Prompt: Same text, new prompt
Frames: Full CR frames on practice, starter only on assessment
CR Scaffolding: Full independent CR

GOOGLE CLASSROOM:
Assignment templates for Google Forms quizzes, Google Docs uploads

SPECIAL PRIORITIES:
Heavy vocabulary focus, Visual/graphic organizer heavy
```

### Final Confirmation
"Ready to build this unit with these settings? I'll create all selected deliverables with activities aligned to your choices."

**Options:**
- **Yes, start building!** - "Proceed with unit creation"
- **Let me adjust something** - "Go back and modify selections"

---

## After User Confirms

### Write the Unit Spec (MANDATORY — before any building begins)

<HARD-GATE>
Before invoking unit-builder-protocol or ANY builder agent, you MUST write a `_unit-spec.md` file
to the unit folder. This file is the single source of truth for the entire build. Every downstream
skill and agent reads from this file — not from conversational memory.

This is the "pipe" between skills. Without it, context rots across long build chains.
</HARD-GATE>

**Step 1: Create the unit folder** (if it doesn't exist):
```
Units/[BenchmarkTopic]_[TextTitle]/
```

**Step 2: Write `_unit-spec.md`** with ALL confirmed preferences:

```markdown
# Unit Specification

> Auto-generated by menu-mode-planner. Do not edit manually during build.
> This file is the single source of truth for all downstream skills and agents.

## Unit Identity
- **Benchmark:** [code] — [name]
- **Text Title:** [title]
- **Text Source:** [district_files | title_to_research | public_domain | paste]
- **Date Created:** [YYYY-MM-DD]

## Class Context
- **Class Type:** [high_esol | mixed_standard | ese_inclusion | advanced]
- **District Materials:** [list or "none"]

## CR Framework
- **Framework:** [RACE | CER]
- **Tier:** [lite | standard | full]
- **Tier Label:** [e.g., "Lite (R+A)"]

## Assessment
- **Format:** [standard | lighter]
- **MC Count (mini):** [6-8 | 4-6]
- **MC Split:** 80% benchmark / 20% vocabulary
- **CR Count (mini):** 1

## Text & Pacing
- **Text Split:** [even | front_loaded | back_loaded | custom]
- **Custom Split:** [null or day-by-day breakdown]
- **Daily Mode:** [default_rotations | workshop_days_3_4 | stations_days_3_4 | custom]
- **Difficulty Ramp:** [gradual | steep | flat]

## Deliverables
[checklist of selected deliverables]

## Days 1-2
- **Teacher-Led:** [list]
- **Independent:** [list]
- **Sentence Frames:** [type]

## Days 3-4
- **Teacher-Led:** [list]
- **Independent:** [list]
- **Organizer Type:** [type]
- **Organizer Rows:** [count and GR pattern]
- **Sentence Frames:** [type]

## Days 5-6
- **Teacher-Led:** [list]
- **Independent:** [list]
- **Assessment Structure:** [type]
- **CR Prompt Type:** [type]
- **Sentence Frames:** [type]

## Google Classroom
- **Integration:** [yes | no]
- **Types:** [list or "n/a"]

## Special Priorities
[list]

## Vocabulary (18 words)
[populated after Phase 1 — vocabulary-instruction fills this in]

## Auto-Routes Applied
[list any auto-routing decisions made based on selections]
```

**Step 3: Confirm the file was written:**
Report to user: "Unit spec saved to `_unit-spec.md`. This is the build contract — all deliverables will follow these settings."

### Next Steps:
1. **Thank user and confirm plan**: "Got it! Building your [Benchmark] unit with [Text Title]."

2. **Request materials if needed**:
   - If user selected "District files uploaded": "Please upload your district files now."
   - If user selected "Text title to research": "Please provide the text title."
   - If user selected "I'll paste the text": "Please paste the text below."

3. **Invoke appropriate skills**:
   - All skills read from `_unit-spec.md` — do NOT re-derive settings from conversation
   - Use `district-files-reader` if district files provided
   - Use `benchmarks` skill for benchmark-specific guidance
   - Use `unit-builder-protocol` for build sequence
   - Use `organizer-design` for organizer creation
   - Use `student-packet-design-guide` for all student-facing formatting (Arial, 12pt/14pt, sentence frames, organizer rules)
   - Use `cer-writing-guide` for CR framework scaffolding (RACE or CER based on Tab 3 selection)
   - Use `assessment-design` for MC format (80/20 split) and CR prompt alignment
   - Use `teaching-templates` for file naming and packet structure

4. **Build in this order**:
   - Phase 1: Gather & Analyze (read materials, analyze benchmark); Update `_unit-spec.md` vocabulary section after vocabulary selection
   - Phase 2: Plan Structure (18 vocab words, 6-day outline, ESOL strategies, CR framework + tier from Tab 3)
   - Phase 3: Build Lesson Plan (.md) — Include selected activities per day, CR scaffolding progression, feedback timing
   - Phase 4: Build Student Packet (.md) — Day-by-day format following `student-packet-design-guide` specs
   - Phase 5: Build Answer Key (.md) — Complete exemplars including CR model response at chosen tier
   - Phase 6: Build Optional Deliverables (exit tickets, cover pages, feedback forms)
   - Phase 7: Create Google Classroom Assignments (if selected)

5. **Synchronization check**:
   - Verify vocabulary matches across all core files (18 words, 3/day)
   - Verify organizer content matches lesson plan and answer key
   - Verify CR framework and tier are consistent across all deliverables
   - Verify assessment format (80/20 MC split + CR) matches assessment-design specs
   - Verify day structure aligns across lesson plan and student packet

6. **Deliver files**:
   - Generate all files with proper naming: `[PassageTitle]_[Type]_[MM-DD].md`
   - Report completion: "Unit complete! All [#] deliverables ready."
   - List files created with brief description

---

## Activity Integration Guidelines

When building deliverables based on user's activity selections:

### Teacher-Led Center (Lesson Plan)
- **List selected activities** under "Teacher-Led Center (20 min)" for each day
- **Provide detailed procedures** with timing for each selected activity
- **Include teacher scripts** for modeling (especially for gradual release)
- **Embed ESOL strategies** within each activity (labeled, minimum 2 per day)
- **Add CFU methods** specific to each activity

### Independent Center (Student Packet)
- **Include selected activities** under "INDEPENDENT CENTER (20 minutes)" for each day
- **Write student-friendly numbered directions** for each activity (bolded action verbs, 1 step per line)
- **Ensure self-running tasks** (students can complete without teacher)
- **Add sentence frames** based on Tab 6-8 frame selections (discussion frames, CR-step frames, or both)
- **Include "Need Help?" boxes** for ESOL support where applicable
- **Follow student-packet-design-guide** for all formatting (Arial 12pt, organizer structure, frame box styles)

### Organizer Integration (Student Packet)
- **Use organizer type from Tab 7** (2-col, 3-col, concept map, or custom)
- **Set row count from Tab 7** (4 or 5 rows with specified gradual release progression)
- **Pre-fill I Do row** with gray background — content comes from lesson plan modeling
- **Label rows explicitly**: I Do (Teacher Models), We Do (Whole Class), You Do w/ Partner, You Do (Independent)
- **Cap columns at 3 max** per organizer-design rules

### No Homework Policy
- **All work stays in class** — no homework assigned
- **Unfinished work** continues next class period or during Technology center
- **Revision happens in class** during feedback cycle (see feedback-system skill)

### Google Classroom Assignments
When Google Classroom integration is selected, create separate section with assignment templates:

**Format:**
```
GOOGLE CLASSROOM ASSIGNMENT: [Title]
Day: [#]
Type: [Document Upload/Google Form/Discussion/etc.]
Points: [#]
Due Date: [End of Day # or specific date]

DESCRIPTION (copy-paste into Google Classroom):
[Full description with student-friendly instructions]

RUBRIC/CRITERIA:
[Point breakdown or rubric]

TEACHER NOTES:
[Grading guidance, common errors, exemplar responses]
```

---

## Example Usage Flow

**User:** "Let's plan a new unit"

**Assistant:** "I'll walk you through a planning menu to gather all your preferences upfront. This will take about 2-3 minutes, then I'll build everything based on your selections."

[Present Tab 1: Unit Basics — benchmark + text source]
[Present Tab 2: Class Context — composition + existing materials]
[Present Tab 3: CR Framework & Assessment — RACE/CER choice, tier, assessment format]
[Present Tab 4: Text Chunking & Pacing — text split, daily mode, difficulty ramp]
[Present Tab 5: Deliverables — which .md files to build]
[Present Tab 6: Days 1-2 Details — Teacher-Led, Independent, sentence frames]
[Present Tab 7: Days 3-4 Details — organizer type, rows, Teacher-Led, Independent, frames]
[Present Tab 8: Days 5-6 Details — assessment structure, CR prompt, frames]
[Present Tab 9: Google Classroom Integration]
[Present Tab 10: Special Priorities]
[Present Tab 11: Display summary and confirmation]

**User confirms**

**Assistant:** "Perfect! Building your ELA.10.R.1.2 (Theme) unit now with all your selected activities and deliverables (Teacher Lesson Plan, Student Packet, Answer Key, and optional additions)."

[Proceed with unit-builder-protocol using all gathered preferences]

---

## Unit Config Object

After Tab 10 confirmation, generate this structured config that all downstream skills and agents reference. This is the single source of truth for the entire build.

```
UNIT_CONFIG = {
  # Tab 1: Unit Basics
  benchmark: "ELA.10.R.1.2",
  benchmark_name: "Theme",
  text_source: "district_files" | "title_to_research" | "public_domain" | "paste",
  text_title: "[Passage Title]",

  # Tab 2: Class Context
  class_type: "high_esol" | "mixed_standard" | "ese_inclusion" | "advanced",
  district_materials: ["organizer_template", "margin_questions", "vocab_list", "assessment_items"],

  # Tab 3: CR Framework & Assessment
  cr_framework: "RACE" | "CER",
  cr_tier: "lite" | "standard" | "full",
  assessment_format: "standard" | "lighter",
  # Derived values:
  cr_tier_label: "Lite (R+A)" | "Standard (R+A+C)" | "Full (R+A+C+E)",
  mc_count_mini: 6-8,
  mc_split: "80% benchmark / 20% vocabulary",
  cr_count_mini: 1,

  # Tab 4: Text Chunking & Pacing
  text_split: "even" | "front_loaded" | "back_loaded" | "custom",
  text_split_custom: null | { day1: "paras 1-5", day2: "paras 6-12", ... },
  daily_mode: "default_rotations" | "workshop_days_3_4" | "stations_days_3_4" | "custom",
  daily_mode_custom: null | { day1: "rotations", day2: "rotations", day3: "workshop", ... },
  difficulty_ramp: "gradual" | "steep" | "flat",

  # Tab 5: Deliverables
  deliverables: ["lesson_plan", "student_packet", "answer_key", "feedback_forms", "exit_tickets", "cover_pages"],

  # Tab 6: Days 1-2 Details
  days_1_2: {
    teacher_led: [...selected activities...],
    independent: [...selected activities...],
    sentence_frames: "discussion_only" | "restate_only" | "both" | "minimal",
  },

  # Tab 7: Days 3-4 Details
  days_3_4: {
    teacher_led: [...selected activities...],
    independent: [...selected activities...],
    organizer_type: "2_col_evidence_analysis" | "3_col_evidence_analysis_connection" | "concept_map" | "custom",
    organizer_rows: "4_standard" | "5_extra_we_do" | "5_extra_you_do",
    sentence_frames: "discussion_only" | "explain_only" | "both" | "minimal",
  },

  # Tab 8: Days 5-6 Details
  days_5_6: {
    teacher_led: [...selected activities...],
    assessment_structure: "practice_day5_assess_day6" | "split_across_both" | "both_practice_separate_assess",
    cr_prompt_type: "same_text_new_prompt" | "new_passage" | "choice_of_prompts",
    sentence_frames: "full_cr_frames" | "starter_only" | "no_frames" | "frames_practice_none_assess",
  },

  # Tab 9: Google Classroom
  gc_integration: true | false,
  gc_types: ["forms", "docs", "discussion", "sheets", "journals"],

  # Tab 10: Special Priorities
  priorities: [...selected priorities...],

  # Auto-derived (see Auto-Routing Logic below)
  esol_adapter_needed: true | false,
  argument_unit: true | false,
  district_reader_needed: true | false,
}
```

Every downstream skill and agent should read from this config rather than re-asking the user.

---

## Decision Passthrough Map

Each menu tab answer flows to specific skills and agents. Use this map to ensure no decision is lost in the handoff.

| Menu Decision | Consumed By | What It Controls |
|---|---|---|
| **Benchmark** (Tab 1) | `benchmarks`, `organizer-design`, `assessment-design`, `bellringer-builder`, `cubes-annotation` | Organizer type, question stems, annotation focus, achievement level descriptors |
| **Text source** (Tab 1) | `district-files-reader` (if district), `vocabulary-instruction` | Where text comes from, how vocab is extracted |
| **Class type** (Tab 2) | `esol-core`, `esol-adapter` agent, `student-packet-design-guide` | Scaffolding density, ESOL strategy count, font size, white space |
| **District materials** (Tab 2) | `district-files-reader`, `organizer-design` | Whether to use district templates or build from scratch |
| **CR framework** (Tab 3) | `cer-writing-guide`, `student-packet-builder` agent, `lesson-plan-coordinator` agent, `assessment-design` | Frame box type (RACE vs CER), CR prompt wording, model response format |
| **CR tier** (Tab 3) | `cer-writing-guide`, `gradual-release-scripts`, `assessment-rubrics` | How many RACE/CER steps students complete, rubric expectations |
| **Assessment format** (Tab 3) | `assessment-design`, `assessment-rubrics`, `student-packet-design-guide` | MC count, 80/20 split, CR count on mini and unit assessments |
| **Text split** (Tab 4) | `lesson-plan-coordinator` agent, `student-packet-builder` agent | Which text sections appear on which day, reading assignment length |
| **Daily mode** (Tab 4) | `ir-framework`, `lesson-plan-coordinator` agent | Rotations vs Workshop vs Stations per day, center timing |
| **Difficulty ramp** (Tab 4) | `assessment-design`, `gradual-release-scripts`, `organizer-design` | DOK level progression, question complexity per day pair |
| **Deliverables** (Tab 5) | `unit-builder-protocol`, `teaching-templates`, `file-management` | Which .md files to generate, file naming |
| **Daily activities** (Tabs 6-8) | `lesson-plan-coordinator` agent, `student-packet-builder` agent, `gradual-release-scripts` | What goes in each center per day, teacher scripts, student directions |
| **Organizer type & rows** (Tab 7) | `organizer-design`, `student-packet-builder` agent | Column count, row count, gradual release labels, I Do pre-fill content |
| **Sentence frames** (Tabs 6-8) | `student-packet-design-guide`, `student-packet-builder` agent, `cer-writing-guide` | Frame type per day (discussion vs CR-step), density, removal schedule |
| **Assessment structure** (Tab 8) | `assessment-design`, `lesson-plan-coordinator` agent | Practice vs assessment day split, CR prompt type |
| **Google Classroom** (Tab 9) | `lesson-plan-coordinator` agent | Assignment descriptions, due dates, submission types |
| **Special priorities** (Tab 10) | All skills — flags emphasis | e.g., "heavy vocab" → extra bellringer activities; "test prep" → more STOP practice |

---

## Auto-Routing Logic

Based on menu answers, auto-trigger these decisions WITHOUT asking the user again:

### Benchmark-Based Auto-Routes
```
IF benchmark IN [R.2.4, R.2.3]:
  → Auto-suggest CER in Tab 3 (mark as "Recommended" option)
  → Flag: argument_unit = true
  → Load cubes-annotation with claim/evidence focus

IF benchmark IN [R.1.4]:
  → Note: Poetry units may need shorter text passages
  → Adjust organizer-design to figurative language template

IF benchmark IN [R.3.1, R.3.4]:
  → Load cubes-annotation with rhetoric/figurative language focus
```

### Class-Type Auto-Routes
```
IF class_type == "high_esol":
  → esol_adapter_needed = true
  → Auto-add esol-adapter agent to Phase 4 handoff
  → Increase sentence frame density in student-packet-design-guide
  → Set minimum 3 ESOL strategies per day (instead of 2)

IF class_type == "ese_inclusion":
  → Flag: reduced items may be needed for assessments
  → Auto-add extended time notation to assessment headers
```

### Text Source Auto-Routes
```
IF text_source == "district_files":
  → district_reader_needed = true
  → Invoke district-files-reader FIRST in Phase 1
  → Extract vocabulary candidates before bellringer-builder runs

IF text_source == "public_domain":
  → Note: Verify text is appropriate for 10th grade reading level
  → May need to chunk long texts for IR page budget (1 front/back per day)
```

### Priority Auto-Routes
```
IF "test_prep" IN priorities:
  → Increase STOP protocol practice on Days 3-4 (not just Days 5-6)
  → Add process of elimination to ALL MC activities, not just Days 1-2
  → Use FSA-style question stems from Planning Cards

IF "heavy_vocab" IN priorities:
  → Add vocabulary review to Days 3-4 Teacher-Led
  → Include Word Network concept map in student packet
  → Extend bellringer review time from 1 min to 2 min

IF "cr_writing_emphasis" IN priorities:
  → Add extra CR practice on Day 4 (in addition to Days 5-6)
  → Include model response comparison activity
  → Add peer feedback on CR drafts
```

---

## Agent Handoff Protocol

After user confirms in Tab 10, the build follows this agent/skill chain. Each handoff includes what data passes forward.

### Phase 1: Gather & Analyze
```
INVOKE: district-files-reader (if district_reader_needed)
  PASS: uploaded files
  RECEIVE: extracted text, margin questions, vocabulary candidates

INVOKE: benchmarks
  PASS: UNIT_CONFIG.benchmark
  RECEIVE: benchmark description, achievement level descriptors, question stem bank

INVOKE: vocabulary-instruction
  PASS: extracted text (or pasted text), benchmark
  RECEIVE: 18 Tier 2/3 words selected, organized into 3/day × 6 days
```

### Phase 2: Plan Structure
```
INVOKE: ir-framework
  PASS: UNIT_CONFIG (full)
  RECEIVE: 6-day skeleton with daily sequence, mode assignments

INVOKE: organizer-design
  PASS: benchmark, cr_framework, cr_tier
  RECEIVE: organizer template (columns, rows, gradual release labels)

INVOKE: cer-writing-guide
  PASS: cr_framework, cr_tier
  RECEIVE: scaffolding progression (Days 1-2 → 3-4 → 5-6), frame types, model response format

INVOKE: bellringer-builder
  PASS: 18 vocabulary words, text passages
  RECEIVE: 6 days of bellringers (2 MC + 1 written each)
```

### Phase 3: Build Deliverables
```
INVOKE: lesson-plan-coordinator AGENT
  PASS: UNIT_CONFIG, 6-day skeleton, bellringer answer keys, organizer template
  RECEIVE: Teacher Lesson Plan (.md)
  NOTE: Agent references gradual-release-scripts for teacher talk, feedback-system for feedback timing

INVOKE: student-packet-builder AGENT
  PASS: UNIT_CONFIG, daily activities, organizer template, bellringers, sentence frame specs
  RECEIVE: Student Packet (.md)
  NOTE: Agent references student-packet-design-guide for ALL formatting decisions

INVOKE: assessment-design
  PASS: benchmark, cr_framework, cr_tier, assessment_format
  RECEIVE: Mini-assessment items (MC with 80/20 split + CR prompt), answer key entries
```

### Phase 4: ESOL Adaptation (conditional)
```
IF esol_adapter_needed:
  INVOKE: esol-adapter AGENT
    PASS: Student Packet (.md), class_type, ESOL proficiency levels
    RECEIVE: ESOL-adapted Student Packet (.md)
    NOTE: Agent references esol-core for strategy selection, student-packet-design-guide for ESOL formatting specs
```

### Phase 5: Quality & Sync
```
INVOKE: unit-reviser AGENT (sync check mode)
  PASS: All generated .md files
  CHECK:
    - Vocabulary matches across lesson plan, student packet, bellringers, answer key
    - Organizer content matches between lesson plan and student packet
    - CR framework and tier consistent across all files
    - Assessment format (80/20 MC + CR) matches assessment-design specs
    - Day structure aligns across all deliverables
    - File naming follows [PassageTitle]_[Type]_[MM-DD].md
  RECEIVE: Sync report with any mismatches flagged

INVOKE: feedback-checkpoint-builder
  PASS: benchmark, cr_framework, cr_tier
  RECEIVE: Day 4 organizer checkpoint + Day 6 CR checkpoint forms
```

### Phase 6: Deliver
```
OUTPUT: All .md files with proper naming
REPORT: File list with descriptions
OFFER: "Want me to create ESOL adaptations? Google Classroom assignments? Sub plans for any days?"
```

---

## Critical Notes

- **Write `_unit-spec.md` FIRST** — no building without the spec file. This is the anti-context-rot mechanism.
- **ALWAYS use AskUserQuestion tool** for menu presentation (not plain text)
- **Present questions sequentially** (one tab at a time or in groups of 3-4 max per message)
- **Generate the UNIT_CONFIG object** after Tab 10 confirmation — this is the build contract
- **Store user's answers** and reference throughout build process via the config
- **Don't skip tabs** even if you think you know the answer (auto-routing suggests defaults, doesn't skip)
- **Allow users to go back** and modify if needed before final confirmation
- **Follow the Agent Handoff Protocol** — invoke skills/agents in the specified order with specified data
- **Every downstream skill reads from UNIT_CONFIG** — no re-asking the user for decisions already made

---

*Pulled from: IR Framework, Unit Builder Protocol, Teaching Templates, Organizer Design, CER Writing Guide, Student Packet Design Guide, Assessment Design*
*Last Updated: 2026-03-08*
*Version: 3.0 - Added CR framework tab (RACE/CER + tier selection), updated assessment format to 80/20 MC split + CR, unified Days 5-6 options to one-framework model, added student-packet-design-guide and cer-writing-guide references, updated skill references in build sequence*
