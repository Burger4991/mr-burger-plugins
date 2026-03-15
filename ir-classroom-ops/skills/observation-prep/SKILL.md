---
name: observation-prep
description: >
  This skill should be used when "preparing for an observation", "admin walkthrough",
  "being observed", or generating lesson documentation for evaluators.
  Use when the /obs-prep command is invoked.
version: 1.0.0
---

# observation-prep Skill

## Purpose

Generate a one-page, scannable reference sheet for administrator observations (formal evaluations, walkthroughs, informal observations). The sheet is designed to be visible or accessible during the observation so you can glance at it for talking points and context.

## Output Location

`~/Documents/Teaching/observation-prep/YYYY-MM-DD-obs-prep.md`

Format: `YYYY-MM-DD` is the observation date

## Template Structure

### Header Section

```markdown
# Observation Prep: [Unit Name]
**Date**: MM/DD/YYYY | **Period**: [#] | **Day**: [X of Y] | **BEST Code**: [FL.BEST.X.X.X]
```

- **Date**: Date of the observation
- **Period**: Class period
- **Day**: Day X of Y (for multi-day units)
- **BEST Code**: Florida BEST ELA standard code (e.g., FL.BEST.ELA.10.R.1.1)

### Objective Section

```markdown
## Objective
[Student-facing objective — what students will be able to do]

Example: "Students will analyze character motivation using textual evidence and the RACE framework."
```

- Write in student-friendly language
- Should be visible/stated in the classroom
- Connects to the BEST benchmark

### Teacher Actions & Student Actions

```markdown
## What the Observer Will See

### Teacher Actions
- [Action 1]: [Detail]
- [Action 2]: [Detail]
- [Action 3]: [Detail]

Example:
- **Mini-lesson**: Modeling annotation strategy for 5-7 minutes
- **Conferencing**: Checking in with students at independent station, asking guiding questions
- **Facilitation**: Rotating between stations, giving feedback, prompting deeper thinking
```

```markdown
### Student Actions
- [Action 1]: [Detail]
- [Action 2]: [Detail]
- [Action 3]: [Detail]

Example:
- **Reading**: Independently reading assigned text, annotating for character motivation
- **Discussing**: Sharing predictions with partner, using sentence starters
- **Completing task**: Recording evidence in RACE graphic organizer
```

### Transitions

```markdown
### Transitions
[Describe how you move between activities or stations]

Example: "At [time], I'll signal for students to wrap up and rotate to next station. [Student leader] will explain the next activity while I reset materials. Rotation takes ~2 minutes."
```

### IR Rotation Model (IR-Specific)

For Intensive Reading classes, include:

```markdown
## IR Rotation Model (3-Station Rotation)

**Current Rotation Day**: [Day X of rotation cycle]
**Gradual Release Stage**: [I Do / We Do / You Do]

### Station 1: Teacher-Led (15-20 min)
[Activity: What you're teaching/assessing with this group]

### Station 2: Independent (15-20 min)
[Activity: What students do alone — reading, annotating, completing organizer, etc.]

### Station 3: Collaborative (15-20 min)
[Activity: Peer or small group work — literature circle, partner discussion, peer review, etc.]

**Note**: Stations rotate tomorrow; today's Station 1 group will do Station 2 next rotation.
```

### Differentiation Section

```markdown
## Differentiation

### ESOL Support (Levels Represented: 1-2, 3-4, 5)
| ESOL Level | Scaffold | Accommodation |
|-----------|----------|---------------|
| 1-2 | [simplified sentence structure, vocabulary support] | [word bank, visual aids, bilingual resources] |
| 3-4 | [sentence starters, graphic organizer] | [extended time, modified text] |
| 5 | [guiding questions, higher-level tasks] | [challenge text, leadership role] |

### Other Accommodations
- [Student name/concern]: [Accommodation/strategy]
- [Student name/concern]: [Accommodation/strategy]
```

### Assessment Section

```markdown
## Assessment: How I'll Know Students Learned
- **Observation**: [What you'll listen/watch for]
- **Product**: [What students produce — exit ticket, organizer, annotation, etc.]
- **Conferencing**: [Specific questions you'll ask]

Example:
- **Observation**: Students using RACE framework language; accurate textual references
- **Product**: Completed RACE graphic organizer with evidence and explanation
- **Conferencing**: "What evidence shows this character motivation? How do you know?"
```

### Classroom Layout

```markdown
## Classroom Layout

```
       Door
        |
    [Shelf]

  [Table 1] [Table 2]
  (Station 1) (Station 2)

      [Table 3]
      (Station 3)

   [Student Desk] [Teacher Desk]
```

- **Station 1 (Teacher-Led)**: [Location + grouping]
- **Station 2 (Independent)**: [Location + description]
- **Station 3 (Collaborative)**: [Location + grouping]

Optional: Include description instead of ASCII if layout is complex.
```

### Key Vocabulary

```markdown
## Key Vocabulary Students Should Be Using
- **[Term]**: [Definition/context] — e.g., used in RACE: "Restate the question before answering"
- **[Term]**: [Definition/context]
- **[Term]**: [Definition/context]

Example:
- **Character motivation**: Why a character acts a certain way; revealed through actions, dialogue, thoughts
- **Text evidence**: Specific words, sentences, or scenes from the text that support an idea
- **Annotation**: Making notes directly on the text to mark important ideas
```

### Materials Needed

```markdown
## Materials Needed
- [Material 1]: [Where, quantity]
- [Material 2]: [Where, quantity]

Example:
- Text (copies for all 3 groups, color-coded by station)
- RACE graphic organizers (completed example displayed)
- Highlighters & pens (in caddy on each table)
- Word bank poster (visible to all, especially for ESOL support)
```

### Danielson Framework Alignment

```markdown
## Danielson Framework Alignment

- **Domain 1: Planning & Preparation**
  - [Your lesson shows: clear objectives, evidence of content knowledge, appropriate materials, differentiation plan]

- **Domain 2: Classroom Environment**
  - [Your classroom shows: respectful interactions, clear routines/procedures for rotations, student engagement, efficient transitions]

- **Domain 3: Instruction**
  - [Your instruction shows: clear explanations, student engagement, questioning/discussion, use of formative assessment, differentiation in action]

- **Domain 4: Professional Responsibilities**
  - [You demonstrate: use of student data (FAST/NWEA scores drive grouping), communication with families, reflection/improvement, professionalism]

Example:
- **Domain 1**: Objective aligned to FL.BEST standard; differentiation plan visible in station assignments
- **Domain 2**: Clear station rotation procedure; students move independently; teacher-led table has 1:1 attention
- **Domain 3**: Mini-lesson models annotation; students annotate independently; teacher conferences for formative assessment
- **Domain 4**: Groups formed by FAST data; all materials inclusive of ESOL supports; observation data informs next lesson
```

### Marzano Alignment (Optional)

If your school uses Marzano scales, include:

```markdown
## Marzano Alignment (Implementation Guide)

- **Instructional Strategies**:
  - [Specific strategy used + evidence from lesson] (e.g., "Nonlinguistic representations: students use graphic organizer")

- **Engagement**:
  - [How students are cognitively engaged] (e.g., "High-level tasks requiring synthesis and inference")

- **Formative Assessment**:
  - [How you're gathering evidence of learning] (e.g., "Teacher conferencing, observation notes, exit ticket")
```

### Observer Talking Points

```markdown
## Observer Talking Points

**If the admin asks: "What am I seeing right now?"**

> "Right now I have three stations running. Station 1 [description of what you're doing]. Station 2 [what students are doing]. Station 3 [collaborative activity]. This design lets me deliver small-group instruction while all students engage with rigorous, scaffolded tasks. In 15 minutes, groups will rotate."

**Key points to mention if asked:**
1. [How this lesson connects to the standard/objective]
2. [Why this rotation/activity choice supports learning]
3. [How differentiation is happening (ESOL, accommodations, grouping)]
4. [What evidence you'll have that students learned]
5. [How today's observation fits into the larger unit/trajectory]

**If asked about [student concern/challenge]:**
> "[Student name] is [current status]. I've been [intervention strategy]. We'll monitor progress through [assessment method]."
```

## Best Practices for This Skill

1. **Keep it scannable**:
   - Use headers, bullet points, tables
   - Avoid long paragraphs
   - One page maximum (or two pages if necessary, but one is better)

2. **Be specific**:
   - ✓ "Students will annotate for character motivation using a 3-color highlighter system"
   - ✗ "Students will read and think about the text"

3. **Show, don't tell**:
   - Display the objective in the classroom
   - Have materials visible and organized
   - Show that you know your students (specific ESOL levels, specific students with accommodations)

4. **Connect to frameworks**:
   - Danielson/Marzano mapping shows you understand evaluation criteria
   - Administrators see intentionality

5. **Be honest about what's happening**:
   - If Station 1 is teacher-led with struggling readers, say that
   - If a student has an accommodation, note it (don't hide it)
   - Evaluators respect transparency

6. **Have talking points ready**:
   - Don't wait to be asked — rehearse how you'd explain your choices
   - Know your data (FAST scores, reading levels, accommodation reasons)
   - Have a quick answer for "Why this lesson, why today?"

## Integration with Other Commands/Skills

- **Pulls context from**: Recent lesson files, unit materials in `~/Documents/Teaching/`
- **Uses data from**: FAST results, NWEA scores, student rosters (inform grouping and differentiation sections)
- **Complements**: `/log` command (can reference recent behavior observations in "Student Actions")
- **Feeds into**: Post-observation reflection (save to Second Brain for later review)

## File Naming & Storage

**Location**: `~/Documents/Teaching/observation-prep/YYYY-MM-DD-obs-prep.md`

**Examples**:
- `2026-02-24-obs-prep.md` (today's date, observation today)
- `2026-02-27-obs-prep.md` (Friday observation)

Keep all observation preps in this folder for:
- Quick reference before obs
- Archive for evaluation cycle
- Reflection after formal observations
- Evidence of preparation if evaluator asks
