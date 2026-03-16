---
name: intervention-planner
description: >
  Use when creating flexible instructional groups based on overall performance levels and intervention
  tiers. Use after assessment periods, starting new IR units, identifying Tier 1/2/3 interventions, or
  developing small-group instruction schedules. Creates High/Middle/Low performance groups and Tier
  1/2/3 intervention designations.

  Note: For groups focused on specific benchmark weaknesses (e.g., all students struggling with Theme),
  use benchmark-mastery-analyzer. For category-specific group analysis, use reporting-category-tracker.
version: 0.1.0
---
# Intervention Planner & Grouping Skill

## Purpose
Create flexible instructional groups based on NWEA reporting category scores and FAST benchmark performance. Group students by specific needs, track intervention effectiveness, and provide data-driven recommendations for differentiated instruction. Generate grouping rosters that consider both overall performance and specific skill gaps.

## When to Use
- After each assessment period (AP1, AP2, AP3 or FAST PM1, PM2, PM3)
- When planning flexible grouping rotations
- Before starting new IR units
- To identify students needing Tier 2 or Tier 3 interventions
- When creating small-group instruction schedules

## Grouping Philosophy

### Multi-Tiered Intervention (RTI) Classification

**Tier 1: On Track (No Intervention Needed)**
- NWEA score: At or above grade-level benchmark
- FAST benchmark proficiency: 75% or higher
- Growth: Meeting or exceeding expected growth trajectory
- Classroom performance: Demonstrating mastery and readiness for grade-level content
- Instructional approach: Whole-class core instruction with extension activities

**Tier 2: At Risk (Targeted Small-Group Intervention)**
- NWEA score: 10-20 points below grade-level benchmark
- FAST benchmark proficiency: 50-74%
- Growth: Below expected trajectory, declining, or stagnant
- Classroom performance: Approaching proficiency but needs strategic support
- Instructional approach: Small-group targeted instruction (3-4x per week, 15-20 minutes)
- Frequency: Monitor progress every 2 weeks, re-assess FAST/NWEA monthly

**Tier 3: High Risk (Intensive 1:1 or Very Small Group Intervention)**
- NWEA score: 20+ points below grade-level benchmark
- FAST benchmark proficiency: Below 50%
- Growth: Significant decline OR no growth despite previous interventions
- Classroom performance: Significantly below grade level, struggling with foundational skills
- Instructional approach: Daily intensive small-group (1:1 or 2-3 students) with explicit strategy instruction
- Frequency: Daily 15-20 minute sessions, progress monitoring 1-2x per week, frequent reassessment

### Dual-Data Integration
- **NWEA Scores**: Overall category performance and growth trends
- **FAST Benchmarks**: Specific skill mastery within categories
- **Combined**: Most accurate picture of student needs

## Key Functions

### 1. Generate Reporting Category Groups (By Class)
**Input**: Class period, reporting category, assessment period
**Output**:
- Three groups: High, Middle, Low performers in that category
- Consider both NWEA scores and aligned FAST benchmarks
- Include student demographics (ELL, ESE, 504)
- Suggest differentiated instruction for each group

**Example Output**:
```
Period 01 - Reading Informational Text Groups (AP2 + FAST PM1)

════════════════════════════════════════════════════════════════

GROUP 1: MASTERY (High Performers)
NWEA Threshold: ≥225 | FAST Benchmarks: ≥75% proficiency

Students (3):
1. LAFOND, Kehana (241) - FAST: R.2.1 (100%), R.2.2 (100%), R.2.3 (75%), R.2.4 (100%)
2. JEAN-CLAUDE, Werleigh (248) - FAST: R.2.1 (75%), R.2.2 (100%), R.2.3 (100%), R.2.4 (75%)
3. CHARLES, Devani (232) - FAST: R.2.1 (75%), R.2.2 (75%), R.2.3 (100%), R.2.4 (75%)

Instructional Focus:
✓ Advanced argument analysis (logical fallacies, bias detection)
✓ Complex informational texts (college-level articles, primary sources)
✓ Independent research and synthesis projects
✓ Rhetorical analysis of speeches and essays
✓ Peer teaching and leadership roles

Recommended Texts:
- Advanced argumentative articles from The Atlantic, NYT Opinion
- Historical documents and speeches
- Scientific journals adapted for high school

════════════════════════════════════════════════════════════════

GROUP 2: APPROACHING MASTERY (Middle Performers)
NWEA Threshold: 210-224 | FAST Benchmarks: 50-74% proficiency

Students (7):
1. FERNANDEZ, Mathias (217) - FAST: R.2.1 (50%), R.2.2 (67%), R.2.3 (50%), R.2.4 (67%)
   [ELL]
2. GONZALEZRODRIG, Genesis (235) - FAST: R.2.1 (50%), R.2.2 (75%), R.2.3 (50%), R.2.4 (50%)
3. JEAN, Judith (226) - FAST: R.2.1 (67%), R.2.2 (50%), R.2.3 (67%), R.2.4 (50%)
4. PIERRE, Kervin (200) - FAST: R.2.1 (50%), R.2.2 (100%), R.2.3 (75%), R.2.4 (0%)
   [ESE: Specific Learning Disability]
5. ROGERS, Ailin (227) - FAST: R.2.1 (33%), R.2.2 (67%), R.2.3 (33%), R.2.4 (missing)
6. LAWRENCE, Raheem (201) - FAST: R.2.1 (50%), R.2.2 (50%), R.2.3 (50%), R.2.4 (50%)
7. BOURGUILLON, Feneisha (206) - FAST: R.2.1 (50%), R.2.2 (67%), R.2.3 (75%), R.2.4 (50%)

Instructional Focus:
→ Guided practice with text structure graphic organizers
→ Scaffold central idea identification (main idea vs. details)
→ Teach claim-evidence-reasoning framework for arguments
→ Author's purpose mini-lessons with think-alouds
→ Collaborative annotation and discussion protocols

Recommended Texts:
- Grade-level informational articles (Newsela, CommonLit at 10th grade)
- Argumentative op-eds with clear structure
- Texts with visible text features (headings, graphics)

Scaffolds for ELL (Fernandez):
- Pre-teach academic vocabulary
- Provide sentence frames for discussion
- Visual supports for text structure

Accommodations for ESE (Pierre):
- Chunked reading assignments
- Extended time for annotation
- Argument graphic organizer with explicit steps

════════════════════════════════════════════════════════════════

GROUP 3: DEVELOPING (Low Performers - Tier 2/3 Intervention)
NWEA Threshold: <210 | FAST Benchmarks: <50% proficiency

Students (4):
1. MITCHELL, Kamaiyah (191) - FAST: R.2.1 (33%), R.2.2 (33%), R.2.3 (33%), R.2.4 (0%)
   ⚠️ TIER 3 INTENSIVE
2. HERNANDEZ, Adelanic (203) - FAST: R.2.1 (0%), R.2.2 (67%), R.2.3 (0%), R.2.4 (0%)
   ⚠️ TIER 3 INTENSIVE
3. IDRIS, Sirag (204) - FAST: R.2.1 (33%), R.2.2 (50%), R.2.3 (33%), R.2.4 (33%)
   → TIER 2 targeted
4. LAROCHE, Fabrice (202) - FAST: R.2.1 (50%), R.2.2 (100%), R.2.3 (0%), R.2.4 (67%)
   → TIER 2 targeted [ESE: Other Health Impaired]

Instructional Focus:
⚠️ Explicit, systematic instruction in foundational skills
⚠️ High-frequency small-group sessions (daily 15-20 min)
⚠️ Simplified texts with high-interest, low-complexity
⚠️ Step-by-step strategy instruction with modeling
⚠️ Frequent comprehension checks and immediate feedback

Recommended Texts:
- Lexile 600-800 informational texts
- Newsela articles at 7th-8th grade level
- High-interest topics (sports, music, gaming, social issues)
- Texts with strong visual support

Intervention Strategies:
- Central Idea: Main Idea Wheel graphic organizer, highlighting topic sentences
- Text Structure: Color-coding organizational patterns, structure signal words
- Argument: Simple CER (Claim-Evidence-Reasoning) templates
- Author's Purpose: PIE (Persuade, Inform, Entertain) sorting activities

Accommodations for ESE (Laroche):
- Read-aloud or audio texts
- Highlight key information
- Reduce text length, increase scaffolding

════════════════════════════════════════════════════════════════

GROUPING SUMMARY:
- Group 1 (High): 3 students (21%) - Extension activities
- Group 2 (Middle): 7 students (50%) - Guided practice
- Group 3 (Low): 4 students (29%) - Intensive intervention

SCHEDULING RECOMMENDATION:
Day 1-2: Whole-class introduction
Day 3-4: Small-group differentiated instruction (3 rotations)
Day 5: Independent practice with tiered assignments
Day 6: Formative assessment and progress monitoring

PROGRESS MONITORING:
- Weekly exit tickets on text structure and central idea
- Bi-weekly informal assessments on argument analysis
- Track benchmark growth on next FAST PM
```

### 2. Cross-Category Flexible Grouping
**Input**: Multiple reporting categories, class period
**Output**:
- Identify students' strongest and weakest categories
- Create groups that rotate focus based on category needs
- Build a flexible grouping rotation schedule

**Example Output**:
```
Period 01 - Multi-Category Flexible Grouping (Weeks 1-6)

Student Category Profiles:

LAFOND, Kehana:
  Strengths: All categories (High across the board)
  Focus: Extension and leadership

CHARLES, Devani:
  Strengths: Reading Informational Text (232), Prose & Poetry (232)
  Weakness: Vocabulary (219)
  Focus: Vocabulary building

MITCHELL, Kamaiyah:
  Strengths: None (Low across all categories)
  Weakness: Reading Across Genres (171 - CRITICAL), Reading Info Text (191)
  Focus: Foundational skills, intensive intervention

════════════════════════════════════════════════════════════════

ROTATION SCHEDULE:

WEEK 1-2 Focus: Reading Informational Text
- Group A (Mastery): LAFOND, JEAN-CLAUDE, CHARLES (3 students)
- Group B (Approaching): FERNANDEZ, GONZALEZRODRIG, JEAN, PIERRE, ROGERS, LAWRENCE, BOURGUILLON (7 students)
- Group C (Intensive): MITCHELL, HERNANDEZ, IDRIS, LAROCHE (4 students)

WEEK 3-4 Focus: Prose and Poetry
- Group A (Mastery): LAFOND, JEAN-CLAUDE, FERNANDEZ (3 students)
  [Note: Fernandez moved up for this category - strength area]
- Group B (Approaching): CHARLES, GONZALEZRODRIG, JEAN, ROGERS, PIERRE (5 students)
- Group C (Intensive): MITCHELL, HERNANDEZ, IDRIS, LAROCHE, LAWRENCE, BOURGUILLON (6 students)
  [Note: LAWRENCE, BOURGUILLON moved down - weakness area]

WEEK 5-6 Focus: Vocabulary
- Group A (Mastery): LAFOND, JEAN-CLAUDE, PIERRE (3 students)
  [Note: PIERRE moved up - vocabulary strength despite overall low scores]
- Group B (Approaching): CHARLES, FERNANDEZ, GONZALEZRODRIG, JEAN, ROGERS, LAWRENCE (6 students)
- Group C (Intensive): MITCHELL, HERNANDEZ, IDRIS, LAROCHE, BOURGUILLON (5 students)

KEY INSIGHT: Students move between groups based on category-specific needs.
PIERRE shows vocabulary strength despite overall struggles - use as confidence builder!
```

### 3. Whole-Cohort Intervention Groups (Across Classes)
**Input**: All classes, specific benchmark or category, proficiency threshold
**Output**:
- Identify all students across all classes needing intervention
- Group for pull-out or push-in support
- Create intervention schedules that don't conflict with core instruction

**Example Output**:
```
School-Wide Tier 3 Intervention Groups - Reading Informational Text

Students Scoring <200 NWEA AND <40% FAST Benchmarks (19 students total)

════════════════════════════════════════════════════════════════

INTERVENTION GROUP 1 (Periods 1, 2, 3)
Schedule: Monday/Wednesday 2:00-2:30 PM
Students (7):
- Period 01: MITCHELL (191), HERNANDEZ (203), IDRIS (204), LAROCHE (202)
- Period 02: SMITH (198), JONES (196)
- Period 03: BROWN (195)

Focus: Central idea and text structure (R.2.1, R.2.2)

════════════════════════════════════════════════════════════════

INTERVENTION GROUP 2 (Periods 4, 7, 8)
Schedule: Tuesday/Thursday 2:00-2:30 PM
Students (6):
- Period 04: WILLIAMS (197), DAVIS (199)
- Period 07: GARCIA (193), MARTINEZ (198)
- Period 08: ANDERSON (194), THOMAS (196)

Focus: Argument analysis (R.2.4)

════════════════════════════════════════════════════════════════

INTERVENTION GROUP 3 (DLA classes)
Schedule: Friday 1:30-2:00 PM
Students (6):
- DLA-01: JOHNSON (189), WILSON (191)
- DLA-02: MOORE (188), TAYLOR (190), WHITE (187), HARRIS (185)

Focus: Foundational informational text comprehension

════════════════════════════════════════════════════════════════

INTERVENTION STRUCTURE (30 minutes):
- 5 min: Review previous session, activate prior knowledge
- 15 min: Explicit instruction with modeling
- 5 min: Guided practice with immediate feedback
- 5 min: Independent application with scaffolds

PROGRESS MONITORING:
- Weekly comprehension checks (informational text passages)
- Track NWEA growth at AP3
- Re-assess FAST benchmarks at PM2

GOAL:
- Increase NWEA scores to ≥205 by AP3
- Increase FAST benchmark proficiency to ≥50% by PM2
```

### 4. Partner/Peer Teaching Groups
**Input**: Class period, identify complementary strengths
**Output**:
- Pair students with opposite strengths to teach each other
- Create structured peer teaching protocols

**Example Output**:
```
Period 01 - Peer Teaching Pairs (Cross-Category Strength Pairing)

PAIR 1: CHARLES (Strong Info Text) ↔ JEAN-CLAUDE (Strong Prose & Poetry)
- Charles teaches: Central idea strategies from informational texts
- Jean-Claude teaches: Theme development strategies from literature
- Shared Activity: Compare/contrast theme vs. central idea with paired texts

PAIR 2: LAFOND (Strong Vocabulary) ↔ FERNANDEZ (Needs Vocabulary Support)
- Lafond teaches: Morphology strategies (prefixes/suffixes)
- Fernandez shares: ELL perspective on context clues
- Shared Activity: Vocabulary practice with academic words

PAIR 3: ROGERS (Strong Reading Across Genres) ↔ PIERRE (Needs Cross-Genre Practice)
- Rogers teaches: Identifying figurative language across genres
- Pierre shares: Close reading strategies that work for him
- Shared Activity: Analyze poetry and informational text for tone

Peer Teaching Protocol:
1. Each student teaches their strength for 10 minutes (explicit instruction)
2. Partner practices with guided support (10 minutes)
3. Both complete independent task and discuss (10 minutes)
4. Reflection: What did you learn? What will you practice? (5 minutes)
```

### 5. Dynamic Regrouping Based on Progress
**Input**: Updated assessment data (e.g., after AP2 or PM2)
**Output**:
- Compare current groups with new data
- Identify students who should move up or down
- Celebrate students showing growth
- Flag students needing increased support

**Example Output**:
```
Period 01 - Regrouping Recommendations (AP1 → AP2)

STUDENTS MOVING UP (Showing Growth):
✓ CHARLES, Devani: 207 → 232 (+25) - Move from Group 3 (Low) → Group 1 (High) in Reading Info Text
✓ PIERRE, Kervin: 217 → 227 (+10) - Move from Group 3 (Low) → Group 2 (Middle) in Prose & Poetry
✓ LAWRENCE, Raheem: 208 → 219 (+11) - Move from Group 3 (Low) → Group 2 (Middle) in Vocabulary

Action: Celebrate growth! Recognize effort and improvement publicly.

════════════════════════════════════════════════════════════════

STUDENTS MOVING DOWN (Showing Decline):
⚠️ HERNANDEZ, Adelanic: 207 → 203 (-4) - Remains in Group 3 (Low), but declining - PRIORITY
⚠️ MITCHELL, Kamaiyah: 183 → 191 (+8 growth but still critically low) - Remains in Group 3, needs Tier 3

Action: Schedule intervention meetings. Investigate causes (attendance, behavior, home issues?).

════════════════════════════════════════════════════════════════

STUDENTS MAINTAINING GROUP:
→ LAFOND, Kehana: 242 → 243 (+1) - Remains Group 1 (High) - Maintain extension activities
→ IDRIS, Sirag: 206 → 204 (-2) - Remains Group 3 (Low) - Stable but not growing, try new strategies

════════════════════════════════════════════════════════════════

UPDATED GROUPS FOR NEXT 6 WEEKS:

Reading Informational Text:
- Group 1: LAFOND, JEAN-CLAUDE, CHARLES (added) - 3 students
- Group 2: FERNANDEZ, GONZALEZRODRIG, JEAN, ROGERS, PIERRE (added), LAWRENCE (added) - 6 students
- Group 3: MITCHELL, HERNANDEZ, IDRIS, LAROCHE, BOURGUILLON - 5 students

Regrouping Date: Week of [Date]
Next Assessment: AP3 (Spring) - Reassess groupings
```

### 6. Subgroup-Specific Grouping (ELL, ESE, 504)
**Input**: Subgroup designation (ELL, ESE, 504)
**Output**:
- Identify all students in subgroup and their performance
- Provide subgroup-specific scaffolds and accommodations
- Track subgroup growth and equity gaps

**Example Output**:
```
ELL Students - Cross-Class Performance & Grouping (AP2)

Total ELL Students: 42 across 8 classes

════════════════════════════════════════════════════════════════

ELL Performance by Category:

Reading Informational Text:
- Avg NWEA: 213.2 (vs. 218.5 school avg) - 5.3 point gap
- % High Performers: 19% (vs. 33% school-wide)
- % Low Performers: 48% (vs. 29% school-wide)

Prose and Poetry:
- Avg NWEA: 211.8 (vs. 219.8 school avg) - 8.0 point gap ⚠️ LARGEST GAP
- % High Performers: 14% (vs. 35% school-wide)
- % Low Performers: 52% (vs. 28% school-wide)

Vocabulary:
- Avg NWEA: 209.5 (vs. 220.0 school avg) - 10.5 point gap ⚠️ CRITICAL GAP
- % High Performers: 10% (vs. 38% school-wide)
- % Low Performers: 57% (vs. 25% school-wide)

════════════════════════════════════════════════════════════════

ELL INTERVENTION GROUPS:

GROUP 1: ELL Students with Moderate English Proficiency (Level 3-4)
Students (24):
Focus: Academic vocabulary, complex syntax, figurative language
Scaffolds:
- Pre-teach vocabulary with visual supports
- Sentence frames for discussion and writing
- Bilingual glossaries
- Extended time for reading

GROUP 2: ELL Students with Beginning English Proficiency (Level 1-2)
Students (18):
Focus: Foundational comprehension, basic vocabulary, grammar
Scaffolds:
- Simplified texts (same content, lower Lexile)
- Audio support for all readings
- Translation tools (Google Translate, bilingual dictionaries)
- Heavy visual supports (graphic organizers, images)
- Small-group reading with ESOL strategies

════════════════════════════════════════════════════════════════

ESOL STRATEGY INTEGRATION:

Reading Informational Text (for ELL):
✓ Use `esol-core` skill for vocabulary pre-teaching
✓ Provide text structure visuals with labeled parts
✓ Teach cognates (English-Spanish academic vocabulary)
✓ Use realia and visuals to build background knowledge

Vocabulary (for ELL):
✓ Morphology focus: Latin/Greek roots (many Spanish cognates)
✓ Context clues with sentence frames
✓ Word walls with images
✓ Interactive word study activities
```

### 7. Generate Grouping Rosters with Student Info
**Input**: Grouping type, class period
**Output**:
- Printable rosters for each group with key student information
- Include scores, demographics, accommodations needed
- Ready for teacher planning and record-keeping

**Example Output**:
```
GROUPING ROSTER - Period 01, Reading Informational Text
Assessment Period: AP2 (Winter 2025-2026)
Generated: [Date]

════════════════════════════════════════════════════════════════

GROUP 1: MASTERY (High Performers)

Student Name          ID        NWEA  Lexile    ELL  ESE  504  Notes
LAFOND, Kehana       0594572    241   1400-1550  N    N    N   Top performer, peer tutor
JEAN-CLAUDE, Werleigh 0648634   248   1150-1300  N    N    N   Strong argument analysis
CHARLES, Devani      0557620    232   1110-1260  N    N    N   Rapid growth (+25 pts)

Instructional Plan: Advanced texts, independent projects, peer teaching

════════════════════════════════════════════════════════════════

GROUP 2: APPROACHING MASTERY (Middle Performers)

Student Name             ID        NWEA  Lexile     ELL  ESE  504  Notes
FERNANDEZ, Mathias      0605819    217   1090-1240  Y    N    N   ELL Level 3, needs vocab pre-teach
GONZALEZRODRIG, Genesis 0783187    235   995-1145   N    N    N   Strong text structure
JEAN, Judith            0587030    226   900-1050   N    N    N   Good growth, needs central idea work
PIERRE, Kervin          0562931    200   915-1065   N    Y    N   SLD, strong text structure, weak argument
ROGERS, Ailin           0649964    227   1015-1165  N    N    N   Central idea weakness (FAST 33%)
LAWRENCE, Raheem        1198364    201   745-895    N    N    N   Moved up from Group 3, monitor closely
BOURGUILLON, Feneisha   0869647    206   765-915    N    N    N   Needs author's purpose support

Instructional Plan: Guided practice, scaffolded texts, graphic organizers
Accommodations: FERNANDEZ (ELL scaffolds), PIERRE (extended time, chunked reading)

════════════════════════════════════════════════════════════════

GROUP 3: DEVELOPING (Low Performers - Tier 2/3)

Student Name          ID        NWEA  Lexile   ELL  ESE  504  Notes
MITCHELL, Kamaiyah   0588989    191   260-410  N    N    N   ⚠️ TIER 3 - Critically low, all categories weak
HERNANDEZ, Adelanic  0603274    203   725-875  N    N    N   ⚠️ TIER 3 - Declining (-4 from AP1)
IDRIS, Sirag         0581731    204   705-855  N    N    N   TIER 2 - Stable, not growing
LAROCHE, Fabrice     0886977    202   630-780  N    Y    N   TIER 2 - OHI, needs read-aloud support

Instructional Plan: Intensive small-group daily, simplified texts, explicit strategy instruction
Accommodations: LAROCHE (read-aloud, extended time, highlighted texts)
Intervention: Daily 15-20 min small-group + weekly 1-on-1 check-ins

════════════════════════════════════════════════════════════════

ROSTER SUMMARY:
Total Students: 14
- Group 1 (High): 3 students (21%)
- Group 2 (Middle): 7 students (50%)
- Group 3 (Low): 4 students (29%)

ELL Students: 1 (FERNANDEZ in Group 2)
ESE Students: 2 (PIERRE in Group 2, LAROCHE in Group 3)
Tier 3 Intervention: 2 students (MITCHELL, HERNANDEZ)
```

## Edge Cases & Data Quality Issues

### Handling Improvement Despite Below Grade Level Performance

**Scenario**: A student shows strong growth (e.g., +15 NWEA points) but still remains significantly below grade-level benchmark.

**Decision Framework**:
- **Progress**: Celebrate and acknowledge growth with the student (this matters for motivation)
- **Placement**: Keep in current intervention tier; don't move up until reaching threshold
- **Instructional adjustment**: If growth is happening, intervention is working; continue current strategies while monitoring
- **Timeline**: Set realistic expectations (might take 2-3 assessment periods to reach benchmark)
- **Family communication**: Share growth data with families, not just the gap

**Example**:
Student was at RIT 191 (AP1), improved to 201 (AP2) - that's +10 growth, which is exceptional! But still below the 210 threshold for Tier 2. Keep in Tier 3 but celebrate the progress and maintain successful intervention strategies.

### Handling Inconsistent Scores Across Periods

**Scenario**: Student scores fluctuate significantly (e.g., AP1: 215, AP2: 203, AP3: 220) making tier assignment unclear.

**Decision Framework**:
- **Look at trend, not snapshot**: Average the three periods, don't just use most recent
- **Investigation first**: Ask why scores are inconsistent. Common causes:
  - Attendance issues on assessment day
  - Testing anxiety or disengagement
  - Medication changes or behavioral shifts
  - Temporary stress (family situation, conflicts with peers)
  - Actual skill variability (strong in some areas, weak in others)
- **Placement**: Use average score for tier assignment
- **Monitoring**: Increase progress monitoring frequency to catch patterns early
- **Check subtest performance**: Does inconsistency appear across categories or just one category?

**Example**:
Student scores: AP1 (215), AP2 (203), AP3 (220). Average = 212.7 (Tier 2). But variability suggests something is affecting performance. Use Tier 2 placement while investigating what caused the AP2 dip.

### Students Not Responding to Intervention

**Scenario**: Student has been in Tier 3 intervention for 6-8 weeks but showing no growth (flat or declining NWEA scores).

**Red Flags**:
- No change after 6+ weeks in same intervention
- Declining scores despite continued intervention
- Large gaps between NWEA and FAST data (not aligned)

**Action Steps**:
1. **Re-assess the intervention match**: Is it aligned to student's actual area of weakness (which category)?
2. **Check attendance**: Are intervention sessions happening consistently?
3. **Assess student effort/engagement**: Is student participating meaningfully or going through motions?
4. **Review accommodations**: Are ESE/504 accommodations being implemented correctly?
5. **Collect diagnostic data**: Informal assessments to pinpoint specific skill gaps
6. **Consider referral**: May need Special Education evaluation or counseling referral if not already involved

**Next Steps**:
- Schedule intervention meeting with reading specialist/ESE specialist
- Consider changing intervention strategy rather than just increasing frequency
- Document what has been tried and results
- Prepare for possible referral for comprehensive evaluation

### Scoring Discrepancies Between Assessments

**Scenario**: NWEA and FAST benchmark data don't align (e.g., RIT 220 but FAST benchmarks only 50% proficient).

**Possible Explanations**:
- NWEA and FAST measure slightly different constructs
- Time gap between assessments (NWEA AP2 vs. FAST PM3, for example)
- Different text types (NWEA doesn't always use literary texts, FAST benchmarks often literature-based)
- Student guessing on NWEA multiple choice vs. constructed response on FAST

**How to Handle**:
- Use BOTH data sources; don't ignore one
- If discrepancy is large (>15 points), investigate which is more reliable
- Consider informal assessments (running records, reading samples) to triangulate
- Make conservative decision (when in doubt, place student in higher support tier)
- Use as opportunity to learn student's strengths (where do they perform better?)

**Example**:
Student has RIT 222 but only 40% FAST mastery on reading informational. This suggests: student can decode/comprehend basic texts (NWEA) but struggles with the specific benchmark (deeper comprehension, analysis). Place in Tier 2, with focus on the specific benchmark skill not yet mastered.

## Grouping Best Practices

### Flexible Grouping Principles
1. **Data-Driven**: Use both NWEA and FAST data to inform grouping
2. **Fluid**: Regroup every 4-6 weeks based on progress
3. **Category-Specific**: Groups change based on which category is being targeted
4. **Transparent**: Students know their groups and goals
5. **Growth-Focused**: Celebrate movement between groups

### Avoiding Tracking Pitfalls
- Rotate students between groups based on category focus
- Ensure all students access to grade-level content
- Provide extension in areas of strength while supporting weaknesses
- Use heterogeneous grouping for collaborative tasks

## Integration with IR Framework

### 6-Day Cycle with Flexible Grouping
- **Day 1**: Whole-class instruction (all students together)
- **Day 2**: Whole-class guided practice
- **Day 3-4**: Small-group differentiated instruction (3 groups rotating)
- **Day 5**: Independent practice (tiered by group)
- **Day 6**: Assessment and regrouping

### Rotation Stations by Group Level
- **Station A**: Teacher-led (Group 3 - intensive)
- **Station B**: Collaborative (Group 2 - guided practice)
- **Station C**: Independent/Extension (Group 1 - mastery)

## File Paths Reference

**Input**:
- NWEA Master Tracker: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/NWEA_Master_Tracker_2025-2026.xlsx`
- FAST PM Data: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/AP1 PM1 scores 2025.xlsx`
- Student Data Table: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Student Data Table ELA-2.xlsx`

**Output**:
- Grouping rosters: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Grouping/`
- Intervention plans: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Intervention/`

## Dependencies

**Works with**:
- `student-data-processor`: Requires clean, merged data
- `reporting-category-tracker`: Uses category-level analysis
- `benchmark-mastery-analyzer`: Uses FAST benchmark data
- `esol-core`: Provides ELL-specific scaffolds
- `ir-framework`: Aligns grouping to 6-day cycle
