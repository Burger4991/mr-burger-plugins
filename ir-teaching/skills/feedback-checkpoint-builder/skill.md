---
name: feedback-checkpoint-builder
description: Generate benchmark-specific feedback checklists for Day 4 organizers and Day 6 RACE responses. Use when building units to embed feedback checkpoints.
---

# Feedback Checkpoint Builder

## Purpose
Generate two types of feedback checklists for IR units:
1. **Day 4 Organizer Checkpoint** - Holistic review before RACE writing
2. **Day 6 RACE Response Checkpoint** - Diagnostic quality review

Each checkpoint is benchmark-specific with criteria aligned to Planning Cards and organizer structure.

## When to Use
- Called automatically by `unit-builder-protocol` during Phase 4 (Student Packet creation)
- Can be invoked manually when retrofitting existing units with checkpoints
- Use when creating custom units that need feedback integration

## How It Works

### Input Required
1. **Benchmark code** (e.g., ELA.10.R.1.2)
2. **Organizer structure** (column headers or row structure)
3. **Unit context** (optional: text title, theme focus)

### Output Generated
1. Day 4 Organizer Checkpoint (formatted for student packet embedding)
2. Day 6 RACE Response Checkpoint (formatted for student packet embedding)

Both outputs include:
- Student self-check section
- Teacher review criteria
- Quality decision checkboxes
- Comment space (1-2 targeted improvements)
- Student action plan section

## Checkpoint Template Structure

### Day 4: Organizer Checkpoint (Holistic Review)

```
DAY 4 CHECKPOINT: [Benchmark Name] Organizer

STUDENT SELF-CHECK:
Before you write your RACE response, review your organizer:
□ I found strong evidence from the text for each section
□ My evidence connects to the question/prompt
□ I included [specific organizer requirement, e.g., "page numbers for each quote"]
□ My organizer is complete (no blank sections)

TEACHER REVIEW:
Evidence Quality:
□ READY - All evidence is text-based and relevant
□ NEEDS REVISION - Missing evidence or off-topic selections

[Benchmark-Specific Criterion]:
□ READY - [e.g., "Clear cause-effect relationships identified"]
□ NEEDS REVISION - [e.g., "Confuses correlation with causation"]

Completion:
□ READY - Organizer fully completed and legible
□ NEEDS REVISION - Missing sections or unclear responses

FEEDBACK (1-2 specific improvements):
[blank space for teacher comments]

STUDENT ACTION PLAN:
Based on feedback, I will:
1. _________________________________
2. _________________________________
```

**Components:**
1. **Student Self-Check** - 4 criteria focusing on evidence quality and completion
2. **Teacher Review** - 3 dimensions (Evidence Quality, Benchmark-Specific Criterion, Completion)
3. **Ready/Needs Revision** - Binary decision for each dimension
4. **Feedback Space** - 1-2 targeted improvements (not comprehensive critique)
5. **Student Action Plan** - Two concrete next steps based on feedback

### Day 6: RACE Response Checkpoint (Diagnostic Review)

```
DAY 6 CHECKPOINT: [Benchmark Name] RACE Response

STUDENT SELF-CHECK:
Before submitting, check your RACE response:
□ R - I restated the question in my answer
□ A - I answered the question directly
□ C - I cited specific evidence from the text
□ E - I explained how my evidence supports my answer

TEACHER REVIEW:
RACE Structure:
□ READY - All RACE components present and identifiable
□ NEEDS REVISION - Missing or unclear components

[Benchmark-Specific Criterion]:
□ READY - [e.g., "Accurately identifies and explains theme"]
□ NEEDS REVISION - [e.g., "Confuses theme with topic or plot summary"]

Evidence Use:
□ READY - Evidence is relevant and properly explained
□ NEEDS REVISION - Evidence missing, irrelevant, or unexplained

FEEDBACK (1-2 specific improvements):
[blank space for teacher comments]

STUDENT ACTION PLAN:
Based on feedback, I will:
1. _________________________________
2. _________________________________
```

**Components:**
1. **Student Self-Check** - Standard RACE criteria (4 components)
2. **Teacher Review** - 3 dimensions (RACE Structure, Benchmark-Specific Criterion, Evidence Use)
3. **Ready/Needs Revision** - Binary decision for each dimension
4. **Feedback Space** - 1-2 targeted improvements (diagnostic, not evaluative)
5. **Student Action Plan** - Two concrete next steps for revision

## Complete Example: Day 4 Theme Checkpoint (Filled In)

This example shows what a completed Day 4 checkpoint looks like when embedded in a student packet's Independent section after the organizer activity:

```
---

INDEPENDENT PRACTICE: Theme Organizer Review & Checkpoint

Name: _________________________________     Date: ____________     Period: _____

[Students complete the Theme Organizer in the preceding section]

---

DAY 4 CHECKPOINT: Theme Organizer
Student Self-Assessment & Teacher Review

**STUDENT SELF-CHECK:**
Before you write your RACE response, review your organizer:

[✓] I identified at least 3 universal themes (not topics or plot summaries)
[✓] I found evidence from the beginning, middle, and end of the text
[ ] I included paragraph numbers for all evidence
[✓] My organizer shows how themes are introduced and developed
[✓] I completed the theme comparison section
[✓] My organizer is complete (no blank sections)

---

**TEACHER REVIEW:**

**Evidence Quality:**
[✓] READY - All evidence is text-based with paragraph numbers
[ ] NEEDS REVISION - Missing evidence or missing paragraph numbers

**Theme Identification (Benchmark-Specific):**
[✓] READY - All themes are UNIVERSAL (apply to anyone, anywhere, anytime)
[ ] NEEDS REVISION - Contains topics or plot summaries instead of universal themes

**Theme Development:**
[✓] READY - Shows evidence from beginning, middle, and end
[✓] READY - "Where/How Introduced" column completed for each theme
[ ] NEEDS REVISION - Missing evidence from key sections of text
[ ] NEEDS REVISION - Does not show HOW themes are introduced/developed

**Theme Analysis:**
[ ] READY - Theme comparison row shows relationships between themes
[✓] NEEDS REVISION - Missing theme comparison or unclear relationships
   _Quality issue:_ Theme comparison row incomplete - shows individual themes but doesn't explain how they connect

**Completion:**
[✓] READY - Organizer fully completed and legible
[ ] NEEDS REVISION - Missing sections or unclear responses

---

**TEACHER FEEDBACK (1-2 specific improvements):**

Your evidence is excellent and well-sourced! You've done a strong job finding where each theme first appears.

Next step: In your "Theme Comparison" row, explain how the themes of family loyalty and individual dreams connect or conflict in the story. How do they work together?

---

**STUDENT ACTION PLAN:**
Based on feedback, I will revise my organizer by:

1. Add how "family loyalty" and "individual dreams" relate in the comparison row
2. Include a sentence explaining whether these themes support or contradict each other

**Revision Status:**
[ ] Revised and ready for Day 6 RACE writing
[✓] Still needs work before Day 6

Teacher Signature: JC Garcia          Date: 2/19/2026
```
