---
name: benchmark-mastery-analyzer
description: >
  Analyze student performance at the individual Florida BEST benchmark level using FAST PM data.
  Use when analyzing FAST PM results (PM1, PM2, PM3), identifying benchmark mastery gaps,
  mapping ELA.10.R benchmarks to NWEA reporting categories, creating flexible student groups
  based on benchmark proficiency, tracking benchmark progress across assessment periods,
  or planning differentiated instruction based on benchmark data. Bridges ir-teaching
  benchmarks with ir-data-pipeline student data analysis.
---

# Benchmark Mastery Analyzer Skill

## Purpose
Analyze student performance at the individual Florida BEST benchmark level using FAST PM data. Map specific ELA.10.R.x.x benchmarks to NWEA reporting categories, identify benchmark clusters for flexible grouping, and provide targeted instructional recommendations aligned to the IR framework.

## When to Use
- After receiving FAST PM results (PM1, PM2, PM3)
- When planning instructional units and selecting focus benchmarks
- Creating flexible groups based on benchmark needs
- Correlating FAST benchmark performance with NWEA category scores
- Planning differentiated instruction

## Florida BEST Benchmarks (Grade 10 ELA)

### Literature Benchmarks (ELA.10.R.1.x) → Prose and Poetry
- **R.1.1**: Analyze how plot, setting & conflict develop
- **R.1.2**: Theme development & objective summary
- **R.1.3**: Coming of Age & Conflicting Perspectives (perspective transformation, author's craft)
- **R.1.4**: Layers of Meaning & Ambiguity in Poetry (multiple meanings, unresolved ideas)

### Informational Text Benchmarks (ELA.10.R.2.x) → Reading Informational Text
- **R.2.1**: Text structure & text features
- **R.2.2**: Central idea & objective summary
- **R.2.3**: Author's purpose & rhetorical appeals
- **R.2.4**: Argument—claims, evidence, reasoning

### Across Genres Benchmarks (ELA.10.R.3.x) → Reading Across Genres
- **R.3.1**: Figurative language & meaning
- **R.3.3**: Intertextual connections
- **R.3.4**: Understanding Rhetoric (ethos, pathos, logos, rhetorical devices)

### Vocabulary Benchmarks (ELA.10.V.1.x) → Vocabulary
- **V.1.2**: Morphology (prefixes/suffixes)
- **V.1.3**: Context clues

## Key Functions

### 1. Student Benchmark Profile
**Input**: Student name or ID
**Output**:
- List all benchmarks with performance percentages
- Identify top 3 strengths and top 3 weaknesses
- Map benchmarks to NWEA reporting categories
- Compare FAST benchmark performance to NWEA category scores

**Example Output**:
```
Student: ROGERS, AILIN (Period 01)

Benchmark Performance (FAST PM1):

STRENGTHS (Top 3):
1. ELA.10.R.1.1 (Plot, setting, conflict): 100% ✓ MASTERED
   → Prose and Poetry category
2. ELA.10.R.1.2 (Theme development): 100% ✓ MASTERED
   → Prose and Poetry category
3. ELA.10.R.3.3 (Intertextual connections): 100% ✓ MASTERED
   → Reading Across Genres category

WEAKNESSES (Top 3):
1. ELA.10.R.2.2 (Central idea): 33% ⚠️ DEVELOPING
   → Reading Informational Text category
2. ELA.10.R.2.3 (Author's purpose): 33% ⚠️ DEVELOPING
   → Reading Informational Text category
3. ELA.10.V.1.3 (Context clues): 33% ⚠️ DEVELOPING
   → Vocabulary category

NWEA-FAST Correlation:
- Prose and Poetry (NWEA: 218) ↔ Literature benchmarks (FAST: 100%) ✓ ALIGNED
- Reading Informational Text (NWEA: 227) ↔ Informational benchmarks (FAST: 33%) ⚠️ MISALIGNED

Insight: High NWEA score in Reading Informational Text (227) does NOT match low FAST benchmark performance (33%). This suggests:
- Student may have gaps in specific skills despite overall category strength
- Target R.2.2 (central idea) and R.2.3 (author's purpose) to strengthen foundation

Instructional Recommendations:
1. Focus on central idea extraction strategies (main idea vs. supporting details)
2. Teach author's purpose and rhetorical appeals analysis
3. Provide context clues vocabulary practice
```

### 2. Class Benchmark Mastery Report
**Input**: Class period
**Output**:
- Percentage of class mastering each benchmark
- Rank benchmarks from strongest to weakest
- Identify class-wide instructional priorities

**Example Output**:
```
Period 01 - Benchmark Mastery Report (FAST PM1)

Benchmark Proficiency (% of students ≥67%):

STRONG BENCHMARKS (≥70% of class proficient):
1. ELA.10.R.1.4 (Poetry): 86% proficient (12/14 students)
2. ELA.10.R.3.4 (Rhetoric): 79% proficient (11/14 students)
3. ELA.10.V.1.3 (Context clues): 71% proficient (10/14 students)

DEVELOPING BENCHMARKS (40-69% of class proficient):
4. ELA.10.R.1.3 (Coming of Age): 64% proficient (9/14 students)
5. ELA.10.R.2.1 (Text structure): 57% proficient (8/14 students)
6. ELA.10.V.1.2 (Morphology): 57% proficient (8/14 students)

WEAK BENCHMARKS (<40% of class proficient):
7. ELA.10.R.2.2 (Central idea): 36% proficient (5/14 students) ⚠️ PRIORITY
8. ELA.10.R.2.4 (Argument analysis): 29% proficient (4/14 students) ⚠️ PRIORITY
9. ELA.10.R.1.2 (Theme development): 21% proficient (3/14 students) ⚠️ PRIORITY

Instructional Priorities (Next 4-6 weeks):
1. HIGH PRIORITY: ELA.10.R.1.2 (Theme) - 79% need intervention
2. HIGH PRIORITY: ELA.10.R.2.4 (Argument) - 71% need intervention
3. MEDIUM PRIORITY: ELA.10.R.2.2 (Central idea) - 64% need intervention

Suggested Unit Focus:
- Unit on theme development (literary texts)
- Unit on argument analysis (informational texts)
- Daily central idea practice with nonfiction articles
```

### 3. Benchmark-Based Flexible Grouping
**Input**: Class period, target benchmarks
**Output**:
- Group students by benchmark needs
- Create 3-4 flexible groups for differentiated instruction

**Example Output**:
```
Period 01 - Flexible Groups for Theme & Argument Instruction

GROUP 1: Mastery (Ready for Extension)
Students: LAFOND, CHARLES, ELVIR (3 students)
Benchmark Status:
- ELA.10.R.1.2 (Theme): 100%
- ELA.10.R.2.4 (Argument): 100%

Instruction:
- Complex multi-theme texts
- Advanced argumentative analysis (logical fallacies, bias)
- Independent reading with theme synthesis projects

GROUP 2: Approaching Mastery (Guided Practice)
Students: BONNET, SIKORSKI, BIEN-AIME, JOHNSON, DORILAS (5 students)
Benchmark Status:
- ELA.10.R.1.2 (Theme): 67-75%
- ELA.10.R.2.4 (Argument): 50-75%

Instruction:
- Theme identification with graphic organizers
- Argument analysis with teacher modeling
- Collaborative theme discussions
- Claim-evidence-reasoning practice

GROUP 3: Developing (Direct Instruction)
Students: DORMEUSJR, JONES, MAXIMILLIEN, HAMILTON, GUERRIER, GUIRAND (6 students)
Benchmark Status:
- ELA.10.R.1.2 (Theme): 0-50%
- ELA.10.R.2.4 (Argument): 0-50%

Instruction:
- Explicit theme instruction (theme vs. topic)
- Scaffold argument structure (claim → evidence → reasoning)
- Simple texts with clear themes
- Annotated argument exemplars with think-alouds

Rotation Schedule (6-Day IR Cycle):
- Day 1-2: Direct instruction on theme (all groups differentiated)
- Day 3-4: Direct instruction on argument (all groups differentiated)
- Day 5: Practice and application
- Day 6: Formative assessment and regrouping
```

### 4. Cross-Benchmark Analysis
**Input**: Two or more related benchmarks
**Output**:
- Identify students strong in one but weak in another
- Reveal skill transfer gaps
- Suggest bridging strategies

**Example Output**:
```
Cross-Benchmark Analysis: Theme vs. Central Idea

Students Strong in Theme (R.1.2) but Weak in Central Idea (R.2.2):

CHARLES, HUDSON:
- Theme (R.1.2): 100%
- Central Idea (R.2.2): 0%
Gap: Can identify themes in literature but struggles with main ideas in informational text

ELVIR, WALTER:
- Theme (R.1.2): 67%
- Central Idea (R.2.2): 0%
Gap: Moderate theme skills not transferring to nonfiction

Insight: These students have developed literary analysis skills but need explicit instruction on transferring theme-finding strategies to informational texts.

Bridging Strategy:
1. Teach comparison: "Theme in literature = Central idea in informational text"
2. Use parallel texts (fiction story + nonfiction article on same topic)
3. Practice identifying "what the author wants you to understand" in both genres
4. Apply same annotation strategies across genres

---

Students Strong in Central Idea (R.2.2) but Weak in Theme (R.1.2):

BONNET, CHRISTY:
- Central Idea (R.2.2): 75%
- Theme (R.1.2): 0%
Gap: Strong nonfiction comprehension but struggles with abstract literary themes

Bridging Strategy:
1. Start with themes explicitly stated in text
2. Use informational text strategies to analyze literature (main idea → theme)
3. Gradual release to implicit, complex themes
```

### 5. NWEA-FAST Correlation Analysis
**Input**: Student or class data with both NWEA and FAST scores
**Output**:
- Identify alignment and misalignment between NWEA categories and FAST benchmarks
- Explain discrepancies
- Provide diagnostic insights

**Example Output**:
```
NWEA-FAST Correlation Analysis: Period 01

ALIGNED Performance (NWEA and FAST both strong or both weak):

Reading Across Genres Category:
- NWEA Avg: 218.3
- FAST Benchmarks (R.3.1, R.3.3, R.3.4): 69% avg proficiency
→ ✓ ALIGNED (both moderate performance)

Vocabulary Category:
- NWEA Avg: 219.2
- FAST Benchmarks (V.1.2, V.1.3): 64% avg proficiency
→ ✓ ALIGNED (both moderate performance)

---

MISALIGNED Performance (NWEA and FAST divergent):

Reading Informational Text Category:
- NWEA Avg: 215.4 (WEAK)
- FAST Benchmarks (R.2.1, R.2.2, R.2.3, R.2.4): 36% avg proficiency (VERY WEAK)
→ ⚠️ NWEA UNDERESTIMATES struggle - FAST reveals critical gaps

Prose and Poetry Category:
- NWEA Avg: 221.7 (STRONG)
- FAST Benchmarks (R.1.1, R.1.2, R.1.3, R.1.4): 53% avg proficiency (MODERATE)
→ ⚠️ NWEA OVERESTIMATES mastery - FAST reveals skill gaps despite high NWEA scores

Diagnostic Insights:
1. Students performing better on NWEA's multiple-choice format than FAST's complex tasks
2. FAST reveals specific benchmark weaknesses hidden by overall NWEA category scores
3. Theme (R.1.2) and Argument (R.2.4) critically weak despite decent NWEA scores

Action Steps:
- Use FAST benchmark data for instructional planning (more specific)
- Monitor students with high NWEA but low FAST (may have test-taking skills but content gaps)
- Target specific benchmarks rather than broad categories
```

### 6. Benchmark Progress Tracking (PM1→PM2→PM3)
**Input**: Student or class, multiple FAST PM periods
**Output**:
- Track benchmark mastery over time
- Identify benchmarks showing growth or decline
- Evaluate instructional effectiveness

**Example Output**:
```
Period 01 - Benchmark Progress (PM1 → PM2 → PM3)

Benchmarks Showing GROWTH:

ELA.10.R.2.1 (Text structure):
  PM1: 57% proficient → PM2: 71% proficient → PM3: 86% proficient
  Growth: +29 percentage points (4 more students proficient)
  ✓ INSTRUCTION EFFECTIVE - continue text structure focus

ELA.10.R.1.3 (Coming of Age):
  PM1: 64% proficient → PM2: 71% proficient → PM3: 79% proficient
  Growth: +15 percentage points (2 more students proficient)
  ✓ STEADY IMPROVEMENT

---

Benchmarks Showing DECLINE:

ELA.10.R.1.4 (Poetry):
  PM1: 86% proficient → PM2: 79% proficient → PM3: 71% proficient
  Decline: -15 percentage points (2 fewer students proficient)
  ⚠️ SKILL ATTRITION - needs re-teaching/spiraling

---

Benchmarks Showing STAGNATION:

ELA.10.R.2.4 (Argument):
  PM1: 29% proficient → PM2: 29% proficient → PM3: 36% proficient
  Growth: +7 percentage points (minimal)
  ⚠️ INSTRUCTION NOT EFFECTIVE - change approach

Recommendations:
1. Celebrate growth in text structure instruction
2. Re-spiral figurative language throughout units (prevent attrition)
3. Re-teach argument analysis with new strategies (current approach ineffective)
```

### 7. IR Unit Alignment with Benchmark Needs
**Input**: Benchmark priority list, IR unit library
**Output**:
- Match IR units to class benchmark needs
- Suggest unit sequence for maximum impact
- Integrate benchmark focus into 6-day cycle

**Example Output**:
```
Period 01 - Unit Recommendations Based on Benchmark Needs

PRIORITY BENCHMARKS:
1. ELA.10.R.1.2 (Theme): 21% proficient
2. ELA.10.R.2.4 (Argument): 29% proficient
3. ELA.10.R.2.2 (Central idea): 36% proficient

RECOMMENDED UNIT SEQUENCE (Next 12 weeks):

Weeks 1-2: Theme in Short Stories (addresses R.1.2)
- Focus Benchmark: ELA.10.R.1.2
- Texts: Grade 10 short stories with clear themes
- Strategy: Theme vs. Topic, theme development across plot
- Integration: Use `benchmarks` skill (see standards/theme.md) for organizer design

Weeks 3-4: Analyzing Arguments in Informational Texts (addresses R.2.4)
- Focus Benchmark: ELA.10.R.2.4
- Texts: Op-eds, speeches, argumentative articles
- Strategy: Claims, evidence, reasoning; logical fallacies
- Integration: Use `benchmarks` skill (see standards/argument.md) for organizer design

Weeks 5-6: Central Idea in Nonfiction (addresses R.2.2)
- Focus Benchmark: ELA.10.R.2.2
- Texts: Nonfiction articles, essays
- Strategy: Main idea vs. supporting details, objective summary
- Integration: Use `benchmarks` skill (see standards/central-idea.md)

Weeks 7-8: Comparative Theme Analysis (spirals R.1.2, addresses R.3.3)
- Focus Benchmarks: ELA.10.R.1.2, ELA.10.R.3.3
- Texts: Paired texts (fiction + poetry OR fiction + nonfiction)
- Strategy: Intertextual connections, comparative theme analysis

Week 9: Formative Assessment & Regrouping
- Re-assess benchmarks with FAST-style tasks
- Regroup students based on new data

Weeks 10-12: Intensive Intervention for Non-Mastery Students
- Small-group focus on R.1.2, R.2.4, R.2.2
- Extension activities for mastery students
```

## Benchmark Grouping Strategies

### Strategy 1: Homogeneous Benchmark Groups
Group students by similar benchmark needs for targeted instruction.

**Example**: All students weak in R.2.4 (Argument) in one group for intensive argument instruction.

### Strategy 2: Heterogeneous Benchmark Groups
Mix students with varied benchmark strengths for peer teaching.

**Example**: Pair student strong in R.1.2 (Theme) with student strong in R.2.2 (Central idea) to teach each other.

### Strategy 3: Spiral Grouping
Rotate focus benchmarks every 2 weeks while spiraling previously taught benchmarks.

**Week 1-2**: Focus on R.2.4 (Argument)
**Week 3-4**: Focus on R.1.2 (Theme), spiral argument practice
**Week 5-6**: Focus on R.2.2 (Central idea), spiral theme and argument

## Integration with IR Framework

### 6-Day IR Cycle - Benchmark Integration
- **Day 1**: Introduce target benchmark with explicit instruction
- **Day 2**: Guided practice with benchmark-aligned texts
- **Day 3**: Small-group differentiation by benchmark proficiency level
- **Day 4**: Independent practice and application
- **Day 5**: Spiral previous benchmarks with new texts
- **Day 6**: Formative assessment of target benchmark

## File Paths

File paths are dynamic and should be determined at runtime based on the user's current working directory. Look for:

**Input**:
- FAST PM data: Look for files matching `*PM*scores*.xlsx` or `*FAST*.xlsx` in the user's data folder
- NWEA Master Tracker: Look for files matching `*NWEA*Tracker*.xlsx` in the user's data folder

**Output**:
- Benchmark reports: Save to a `Reports/Benchmark_Analysis/` subfolder within the user's data directory

## Dependencies

**Works with**:
- `student-data-processor`: Requires FAST data import and benchmark mapping
- `reporting-category-tracker`: Links benchmarks to NWEA categories
- `benchmarks` skill: IR framework benchmark standards (see standards/ directory)
