---
name: reporting-category-tracker
description: >
  Use when tracking student performance across the 4 NWEA reporting categories (Reading Across Genres,
  Reading Informational Text, Prose & Poetry, Vocabulary). Use when identifying intervention needs,
  conducting progress monitoring, creating intervention groups, before instructional planning meetings,
  or analyzing performance trends.

  IMPORTANT: This analyzes NWEA REPORTING CATEGORIES, not individual FAST benchmarks. For analysis of
  specific FAST benchmarks, use benchmark-mastery-analyzer instead.
version: 0.1.0
---
# Reporting Category Tracker Skill

## Purpose
Track and analyze student performance across the 4 NWEA reporting categories (Reading Across Genres, Reading Informational Text, Prose & Poetry, Vocabulary) over multiple assessment periods. Identify trends, flag students needing intervention, and provide actionable insights to drive instruction.

## When to Use
- Weekly progress monitoring and student check-ins
- Before instructional planning meetings
- After importing new assessment data
- When creating intervention groups
- Before meetings with reading coach or principal

## The 4 Reporting Categories

### 1. Reading Across Genres (InstructionalArea1)
**NWEA Skills**: Cross-genre analysis, identifying patterns across text types
**FAST Benchmarks**:
- ELA.10.R.3.1: Figurative language & meaning
- ELA.10.R.3.3: Intertextual connections
- ELA.10.R.3.4: Word choice, tone, mood

**Instructional Focus**: Teaching students to recognize literary devices, themes, and techniques across multiple genres (fiction, nonfiction, poetry, drama)

### 2. Reading Informational Text (InstructionalArea2)
**NWEA Skills**: Analyzing nonfiction, understanding text features, evaluating arguments
**FAST Benchmarks**:
- ELA.10.R.2.1: Central idea & objective summary
- ELA.10.R.2.2: Text structure & text features
- ELA.10.R.2.3: Author's purpose & rhetorical appeals
- ELA.10.R.2.4: Argument—claims, evidence, reasoning

**Instructional Focus**: Close reading of informational texts, analyzing arguments, understanding organizational patterns

### 3. Prose and Poetry (InstructionalArea3)
**NWEA Skills**: Literary analysis, understanding narrative elements, interpreting poetry
**FAST Benchmarks**:
- ELA.10.R.1.1: Plot, setting, conflict development
- ELA.10.R.1.2: Theme development & objective summary
- ELA.10.R.1.3: Character development & interactions
- ELA.10.R.1.4: Figurative language & tone

**Instructional Focus**: Literary elements, theme analysis, character development, poetic devices

### 4. Vocabulary (InstructionalArea4)
**NWEA Skills**: Word meaning, context clues, word relationships
**FAST Benchmarks**:
- ELA.10.V.1.2: Morphology (prefixes/suffixes)
- ELA.10.V.1.3: Context clues

**Instructional Focus**: Vocabulary acquisition strategies, morphology, academic language

## Key Functions

### 1. Track Student Progress by Category
**Input**: Student name or ID
**Output**:
- Student's scores in all 4 categories across AP1, AP2, AP3
- Delta scores showing growth/decline in each category
- Visual indicator: ↗ (growth), → (stable), ↘ (decline)
- Category ranking: Best to weakest area
- Suggested focus area for intervention

**Example Output**:
```
Student: LAFOND, KEHANA (0594572)
Period: 01

Category Progress (AP1 → AP2 → AP3):
1. Reading Across Genres:      236 → 241 (+5) → 244 (+3)  ↗ STRONG GROWTH
2. Reading Informational Text: 241 → 239 (-2) → 242 (+3)  → STABLE
3. Prose and Poetry:            247 → 245 (-2) → 250 (+5)  ↗ GROWTH
4. Vocabulary:                  243 → 246 (+3) → 248 (+2)  ↗ GROWTH

Overall RIT: 242 → 243 (+1) → 246 (+3)

Strengths: Prose & Poetry (247), Vocabulary (243)
Weaknesses: Reading Across Genres (236)

Recommendation: Focus intervention on Reading Across Genres. Use cross-genre comparison strategies and intertextual connections.
```

### 2. Identify Category-Specific Struggling Students
**Input**: Reporting category name, performance threshold (e.g., "Below 210")
**Output**:
- List of students below threshold in that category
- Current performance level (High/Middle/Low)
- Growth trend since AP1
- Suggested instructional groupings

**Example Output**:
```
Students Struggling in Reading Informational Text (Below 210):

Period 01:
- HERNANDEZ, ADELANIC (203) - Declining (-5 from AP1) - PRIORITY
- IDRIS, SIRAG (204) - Stable (+1 from AP1)
- MITCHELL, KAMAIYAH (191) - Growing (+8 from AP1)

Period 02:
- SMITH, JOHN (206) - Declining (-3 from AP1) - PRIORITY
...

Total: 15 students across 8 classes
Suggested Group Focus: Text structure, central idea, argument analysis
```

### 3. Compare Category Performance Across Classes
**Input**: Reporting category name
**Output**:
- Class averages in that category
- Rank classes by performance
- Identify highest/lowest performing classes
- Growth rates by class

**Example Output**:
```
Reading Informational Text - Class Comparison (AP2):

Class Rankings:
1. Period 06: Avg 228.5 (+6.2 growth from AP1) ⭐ TOP PERFORMER
2. Period 02: Avg 223.1 (+4.8 growth from AP1)
3. Period 07: Avg 220.3 (+3.1 growth from AP1)
4. Period 01: Avg 218.6 (+2.5 growth from AP1)
5. Period 03: Avg 215.9 (+1.8 growth from AP1)
6. Period 04: Avg 214.2 (+0.9 growth from AP1)
7. Period 08: Avg 212.7 (-0.5 growth from AP1) ⚠️ NEEDS ATTENTION
8. Period DLA-02: Avg 205.3 (+1.2 growth from AP1)

Insight: Period 08 showing regression. Recommend reviewing text structure instruction and increasing informational text exposure.
```

### 4. Generate Category Strength/Weakness Profile
**Input**: Class period OR whole cohort
**Output**:
- Identify strongest and weakest categories
- Percentage of students in High/Middle/Low for each category
- Suggested instructional priorities

**Example Output**:
```
Period 01 - Category Profile (AP2):

Strongest Category: Vocabulary (Avg 221, 65% High)
Weakest Category: Reading Informational Text (Avg 213, 45% Low)

Category Breakdown:
                              Avg Score  High%  Mid%  Low%  Priority
Reading Across Genres           218      40%    35%   25%    Medium
Reading Informational Text      213      25%    30%   45%    HIGH ⚠️
Prose and Poetry                219      45%    35%   20%    Low
Vocabulary                      221      65%    25%   10%    Maintain

Instructional Recommendations:
1. HIGH PRIORITY: Reading Informational Text
   - Focus on text structure recognition
   - Increase exposure to argumentative texts
   - Teach central idea extraction strategies

2. MEDIUM PRIORITY: Reading Across Genres
   - Practice cross-genre comparisons
   - Develop intertextual connection skills

3. MAINTAIN: Prose & Poetry, Vocabulary
   - Continue current strategies
   - Use as bridge to weaker areas
```

### 5. Flag Students with Inconsistent Category Performance
**Input**: Threshold for category variance (default: ±15 points)
**Output**:
- Students with large gaps between highest and lowest categories
- Specific category discrepancies
- Diagnostic recommendations

**Example Output**:
```
Students with High Category Variance (Gap ≥15 points):

JEAN, JUDITH (Period 01):
  Highest: Vocabulary (226)
  Lowest: Prose and Poetry (195)
  Gap: 31 points
  Issue: Strong vocabulary knowledge not transferring to literary analysis
  Recommendation: Explicit instruction on applying vocabulary to literary interpretation

MITCHELL, KAMAIYAH (Period 01):
  Highest: Reading Informational Text (191)
  Lowest: Reading Across Genres (171)
  Gap: 20 points
  Issue: Struggles with cross-genre analysis and figurative language
  Recommendation: Focus on figurative language and genre comparison strategies
```

### 6. Track Category Growth Trajectories
**Input**: Student or class
**Output**:
- Category-by-category growth over time
- Identify accelerating or declining areas
- Predict AP3 performance based on trends

**Example Output**:
```
Period 01 - Growth Trajectories by Category:

Reading Across Genres:
  AP1: 215 → AP2: 218 (+3) → Projected AP3: 221
  Trend: Steady growth ↗

Reading Informational Text:
  AP1: 217 → AP2: 213 (-4) → Projected AP3: 209
  Trend: Declining ↘ ⚠️ INTERVENTION NEEDED

Prose and Poetry:
  AP1: 216 → AP2: 219 (+3) → Projected AP3: 222
  Trend: Steady growth ↗

Vocabulary:
  AP1: 218 → AP2: 221 (+3) → Projected AP3: 224
  Trend: Steady growth ↗

Alert: Reading Informational Text showing decline. Prioritize informational text instruction immediately.
```

### 7. Map FAST Benchmarks to NWEA Categories
**Input**: FAST PM data with benchmark percentages
**Output**:
- Show which specific benchmarks contribute to each NWEA category
- Identify benchmark weaknesses within categories
- Connect FAST weaknesses to NWEA category performance

**Example Output**:
```
ROGERS, AILIN (Period 01) - Category Benchmark Breakdown:

Reading Informational Text (NWEA: 227):
  ✓ ELA.10.R.2.1 (Central idea): 33% - WEAK
  ✓ ELA.10.R.2.2 (Text structure): 67% - MODERATE
  ✓ ELA.10.R.2.3 (Author's purpose): 33% - WEAK
  ✗ ELA.10.R.2.4 (Argument): Data not available

Insight: Strong NWEA score (227) but FAST shows specific weaknesses in central idea and author's purpose. These may be limiting further growth.

Recommendation: Target central idea and author's purpose in next unit to strengthen this already-strong category.
```

## Data-Driven Instructional Strategies

### Strategy 1: Differentiated Category Focus
Based on category analysis, create **3 instructional groups**:

**Group 1: Reading Informational Text Focus**
- Students weak in InstructionalArea2
- Daily informational text close reading
- Text structure graphic organizers
- Argument analysis practice

**Group 2: Prose & Poetry Focus**
- Students weak in InstructionalArea3
- Literary element analysis
- Theme development activities
- Character motivation discussions

**Group 3: Cross-Genre Analysis Focus**
- Students weak in InstructionalArea1
- Comparative reading across genres
- Figurative language in multiple contexts
- Synthesis across text types

### Strategy 2: Leverage Strengths to Build Weaknesses
- Identify students with strong Vocabulary but weak Reading Informational Text
- Use vocabulary strength as entry point to informational text analysis
- Bridge stronger categories to weaker ones

### Strategy 3: Category-Specific Exit Tickets
- Track daily progress in targeted categories
- Use benchmark-aligned questions for each category
- Monitor if instruction is moving the needle

### Strategy 4: Flexible Grouping Based on Category Needs
- Regroup students every 2 weeks based on latest category data
- Target 1-2 categories intensively per cycle
- Rotate focus to address all categories throughout year

## Integration with IR Framework

### 6-Day IR Cycle - Category Integration
- **Day 1-2**: Focus on 1 weak category (e.g., Reading Informational Text)
- **Day 3-4**: Focus on 2nd weak category (e.g., Reading Across Genres)
- **Day 5**: Vocabulary reinforcement (InstructionalArea4)
- **Day 6**: Assessment/application across categories

### Rotation Stations by Category
- **Station A**: Reading Informational Text practice
- **Station B**: Prose & Poetry analysis
- **Station C**: Vocabulary building
- **Station D**: Reading Across Genres synthesis

## Reporting Templates

### Weekly Progress Report (for teacher records)
- Top 5 improving students by category
- Top 5 declining students by category
- Class averages by category
- Focus areas for upcoming week

### Admin Report (for reading coach/principal)
- School-wide category performance
- Classes needing support by category
- Growth trends across cohort
- Intervention recommendations

## Output Specification

The reporting category tracker produces structured analytical output in the following formats:

### Student Progress Reports
- **Format**: Formatted text with visual indicators (↗, →, ↘)
- **Columns**: Student name, student ID, Period, AP1/AP2/AP3 scores per category, delta scores, overall RIT
- **Output type**: Console-ready text report or can be converted to CSV/Excel

### Category Comparison Analysis
- **Format**: Ranked class/cohort comparisons with averages and growth rates
- **Columns**: Class period, average score, growth since AP1, performance level (High/Middle/Low)
- **Output type**: Sortable table with trend indicators

### Category Strength/Weakness Profiles
- **Format**: Summary statistics with percentage breakdowns
- **Columns**: Category name, average score, % High / % Middle / % Low, priority flag, instructional recommendations
- **Output type**: Dashboard-style summary table

### Variance/Gap Analysis
- **Format**: Students with category discrepancies highlighted
- **Columns**: Student name, highest category (score), lowest category (score), gap (points), diagnostic recommendation
- **Output type**: Exception report

### Growth Trajectory Projections
- **Format**: Time-series analysis with trend lines and predictions
- **Columns**: Category, AP1 score, AP2 score, AP3 score (actual or projected), trend direction, alert status
- **Output type**: Forecast table with visual trends

### Benchmark Mapping Cross-Reference
- **Format**: Category scores linked to FAST benchmark performance
- **Columns**: Category name, category score, associated benchmarks, benchmark % performance, alignment notes
- **Output type**: Cross-reference analysis

All outputs include:
- **Data completeness notes** (flagging any missing data)
- **Recommendation section** (actionable instructional priorities)
- **Legend** (explaining visual indicators and performance levels)

## Error Handling

**Missing Category Data**:
- If student missing scores in a category, flag as "Incomplete Data"
- Note in report: "Unable to calculate growth for [Category]"

**Outlier Detection**:
- Flag category scores >30 points different from overall RIT
- May indicate testing irregularity or unique strength/weakness

## Dependencies

**Required files**:
- NWEA Master Tracker (with all category scores)
- Student Data Table (class assignments)
- FAST PM data (for benchmark mapping)

**Works with**:
- `student-data-processor`: Requires clean, processed data
- `intervention-planner`: Provides category-specific groupings
- `benchmark-mastery-analyzer`: Links FAST benchmarks to NWEA categories

## File Paths Reference

**Input**:
- NWEA Master Tracker: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/NWEA_Master_Tracker_2025-2026.xlsx`

**Output**:
- Category analysis reports: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Category_Analysis/`
