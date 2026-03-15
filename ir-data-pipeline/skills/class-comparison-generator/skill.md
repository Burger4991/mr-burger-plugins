---
name: class-comparison-generator
description: >
  This skill should be used when "generating class comparison reports" or "analyzing performance across multiple periods" for administrative meetings. Use when "preparing for meetings with reading coach or principal", "reporting end-of-grading-period results", or "identifying classes needing additional support".
version: 0.1.0
---
# Class Comparison Generator Skill

## Purpose
Generate comprehensive comparison reports analyzing performance across all 8 class periods (Intensive Reading and Developmental Language Arts). Identify strengths, weaknesses, growth rates, and instructional needs for each class to inform resource allocation, intervention planning, and administrative reporting.

## When to Use
- Before meetings with reading coach or principal
- After each assessment period (AP1, AP2, AP3)
- When planning professional development or peer observations
- To identify classes needing additional support
- For end-of-grading-period reports

## Class Overview (2025-2026)

### Intensive Reading 2 Classes
- Period 01: ~14 students
- Period 02: ~26 students
- Period 03: ~20 students
- Period 04: ~18 students
- Period 07: ~29 students
- Period 08: ~20 students

### Developmental Language Arts Classes
- Period 01: ~12 students
- Period 02: ~15 students
- Period 03: ~12 students
- Period 07: ~12 students
- Period 08: ~10 students

**Total**: ~8 classes, ~120+ students

## Key Functions

### 1. Overall Class Performance Comparison
**Input**: Assessment period (AP1, AP2, or AP3)
**Output**:
- Rank all classes by average overall RIT score
- Show class size, average score, median score, standard deviation
- Identify highest and lowest performing classes
- Calculate school-wide average for comparison

**Example Output**:
```
Class Performance Overview - AP2 (Winter 2025-2026)

Overall RIT Score Rankings:

Rank  Class      Students  Avg RIT  Median  Std Dev  School Avg  Status
1     Period 06     25      233.2    234     8.1      220.5      ⭐ Top Performer (+12.7)
2     Period 04     18      228.4    229     6.9      220.5      ⭐ Above Average (+7.9)
3     Period 02     26      224.1    225     9.3      220.5      ✓ Above Average (+3.6)
4     Period 07     29      221.8    222     11.2     220.5      → At Average (+1.3)
5     Period 03     20      219.3    220     7.8      220.5      → At Average (-1.2)
6     Period 01     14      217.6    218     10.4     220.5      ⚠️ Below Average (-2.9)
7     Period 08     20      215.2    216     8.9      220.5      ⚠️ Below Average (-5.3)
8     DLA-02        15      208.4    209     12.6     220.5      ⚠️ Needs Support (-12.1)

School Average: 220.5
Highest-Lowest Gap: 24.8 points (Period 06 vs DLA-02)

Insights:
- Period 06 significantly outperforming school average
- DLA-02 needs intensive intervention and support
- Wide performance range (208-233) suggests differentiated needs
```

### 2. Growth Rate Comparison
**Input**: Two assessment periods (e.g., AP1→AP2)
**Output**:
- Calculate average growth for each class
- Rank classes by growth rate
- Identify accelerating and stagnating classes
- Show percentage of students growing in each class

**Example Output**:
```
Class Growth Comparison - AP1 to AP2

Growth Rankings (Average RIT Point Gain):

Rank  Class      Avg Growth  % Students Growing  % Declining  Fastest Growth  Slowest Growth
1     Period 03    +6.2         85% (17/20)          10%       +18 (EUGENE)     -3 (BUSTOS)
2     Period 07    +5.8         79% (23/29)          14%       +15 (SMITH)      -5 (JONES)
3     Period 02    +4.9         73% (19/26)          19%       +12 (LAFOND)     -8 (PIERRE)
4     Period 01    +4.1         71% (10/14)          21%       +10 (CHARLES)    -4 (IDRIS)
5     Period 06    +3.5         68% (17/25)          20%       +11 (BONNET)     -2 (DULCIO)
6     Period 04    +2.8         61% (11/18)          28%       +9 (ROGERS)      -7 (HAMILTON)
7     Period 08    +1.2         55% (11/20)          35%       +8 (JEAN)        -10 (MITCHELL)
8     DLA-02       +0.8         47% (7/15)           40%       +6 (WILLIAMS)    -12 (BROWN)

School Average Growth: +3.7 points

Insights:
- Period 03 showing exceptional growth despite moderate starting scores
- Period 08 and DLA-02 have high percentages of declining students - PRIORITY
- Period 06 has highest scores but lower growth - may need enrichment challenge
```

### 3. Reporting Category Comparison by Class
**Input**: Specific reporting category
**Output**:
- Compare all classes on one category
- Show class strengths and weaknesses
- Identify which classes excel/struggle in each category

**Example Output**:
```
Reading Informational Text - Class Comparison (AP2)

Category Rankings:

Rank  Class      Avg Score  AP1→AP2 Growth  % High Performers  % Low Performers
1     Period 06    232.5        +7.2            60%                8%
2     Period 04    226.3        +5.8            50%               11%
3     Period 02    221.7        +4.5            42%               19%
4     Period 03    219.1        +6.1            35%               25%
5     Period 07    217.8        +3.2            31%               28%
6     Period 01    215.4        +2.8            29%               36%
7     Period 08    212.9        +1.1            25%               45%
8     DLA-02       206.3        +0.9            13%               60%

School Average: 218.5

Category Strengths by Class:
✓ Period 06: Text structure analysis
✓ Period 04: Argument evaluation
✓ Period 02: Central idea identification

Category Weaknesses by Class:
⚠️ Period 08: Text features, author's purpose
⚠️ DLA-02: All informational text skills - needs systematic intervention

Instructional Recommendations:
- Period 08: Focus on text structure and author's purpose
- DLA-02: Implement foundational informational text reading strategies
- Period 06: Provide advanced argument analysis and synthesis tasks
```

### 4. Four-Category Profile by Class
**Input**: Class period
**Output**:
- Show all 4 reporting categories for that class
- Identify class-specific strengths and weaknesses
- Suggest targeted instruction priorities

**Example Output**:
```
Period 01 - Four-Category Profile (AP2)

Category Performance:

Category                        Avg Score  School Avg  Diff    Rank  Status
Reading Across Genres              218.3      220.1    -1.8     6/8   → At Average
Reading Informational Text         215.4      218.5    -3.1     6/8   ⚠️ Below Average
Prose and Poetry                   221.7      219.8    +1.9     3/8   ✓ Above Average
Vocabulary                         219.2      220.0    -0.8     5/8   → At Average

Class Strengths:
1. Prose and Poetry (+1.9 above school avg) - 3rd best class
   - Strong literary analysis skills
   - Effective theme and character work

Class Weaknesses:
1. Reading Informational Text (-3.1 below school avg) - 6th of 8 classes
   - Struggles with text structure
   - Needs more argument analysis practice

Growth Opportunities:
- Leverage Prose & Poetry strength to improve Reading Across Genres
- Prioritize informational text exposure and analysis
- Build cross-genre comparison skills

Instructional Focus for Next Cycle:
1. HIGH PRIORITY: Reading Informational Text
   - Use IR units focused on informational texts
   - Text structure organizers
   - Argument analysis activities

2. MEDIUM PRIORITY: Reading Across Genres
   - Cross-genre comparison activities
   - Intertextual connections

3. MAINTAIN: Prose & Poetry
   - Continue current literature-based instruction
```

### 5. Class Demographics & Subgroup Performance
**Input**: Class period
**Output**:
- Show class demographic composition
- Compare ELL, ESE, 504 performance to general education
- Identify equity gaps within class

**Example Output**:
```
Period 02 - Demographics & Subgroup Performance (AP2)

Class Composition (26 students):
- General Education: 18 students (69%)
- ELL: 13 students (50%)
- ESE: 5 students (19%)
- 504: 2 students (8%)

Subgroup Performance Comparison:

Subgroup         Count  Avg RIT  School Avg  Gap    % Growing
General Ed         18     228.3     224.5    +3.8     78%
ELL                13     219.6     217.2    +2.4     69%
ESE                 5     212.4     210.8    +1.6     60%
504                 2     221.5     220.0    +1.5     50%

Class Average: 224.1

Insights:
- ELL students performing above school-wide ELL average (+2.4)
- ESE students also above school-wide ESE average (+1.6)
- Strong differentiation and support in this class
- 12-point gap between General Ed and ESE needs monitoring

Recommendations:
- Continue current ELL scaffolding strategies
- Consider peer tutoring to close General Ed/ESE gap
- Celebrate inclusive classroom culture
```

### 6. Cross-Class Comparison Matrix
**Input**: All classes
**Output**:
- Side-by-side comparison of all metrics
- Heat map visualization showing high/low performers
- Identify outlier classes

**Example Output**:
```
Full Class Comparison Matrix - AP2

                    Overall  Growth  Reading   Reading    Prose &   Vocabulary  % ELL  % ESE
Class               RIT      AP1→AP2 Across    Info Text  Poetry
Period 01           217.6    +4.1    218.3     215.4      221.7     219.2       21%    14%
Period 02           224.1    +4.9    223.5     221.7      224.8     223.1       50%    19%
Period 03           219.3    +6.2    220.1     219.1      219.5     218.8       30%    10%
Period 04           228.4    +2.8    229.2     226.3      228.1     229.5       11%    22%
Period 06           233.2    +3.5    234.1     232.5      233.8     231.2       16%    12%
Period 07           221.8    +5.8    222.4     217.8      223.2     220.9       28%    17%
Period 08           215.2    +1.2    216.8     212.9      215.7     214.3       35%    25%
DLA-02              208.4    +0.8    209.1     206.3      208.9     207.2       40%    47%

Color Key: 🟢 Top 3 | 🟡 Middle | 🔴 Bottom 3

Outlier Analysis:
- Period 06: Highest scores across all categories - model class
- Period 03: Moderate scores but highest growth - effective instruction
- DLA-02: Lowest scores, lowest growth, highest % ESE - needs intensive support
- Period 08: Below average with low growth - review instructional approach
```

### 7. Best Practices Identification
**Input**: High-performing classes
**Output**:
- Identify what high-performing classes are doing differently
- Suggest peer observations
- Recommend strategies to replicate

**Example Output**:
```
Best Practices from Top-Performing Classes

Period 06 (Highest Overall Performance):
- StrongRoutineS and procedures
- Consistent use of reading strategies
- High text complexity exposure
- Effective grouping and differentiation

Observable Strategies:
- Daily close reading with annotation
- Weekly vocabulary pre-teaching
- Small-group rotation structure
- Regular formative assessment

Recommended Peer Observations:
- Period 08 → Observe Period 06 (learn differentiation strategies)
- DLA-02 → Observe Period 03 (learn growth-focused instruction)

Period 03 (Highest Growth Rate):
- Strong gradual release model
- Targeted intervention for struggling students
- Celebration of progress and growth mindset
- Frequent progress monitoring

Transferable Practices:
- Weekly growth tracking with students
- Strategy instruction with modeling
- Flexible grouping based on data
```

### 8. Administrative Summary Report
**Input**: Assessment period
**Output**:
- Executive summary for reading coach/principal
- Highlight key trends and needs
- Resource allocation recommendations

**Example Output**:
```
Administrative Summary - AP2 Winter Assessment
Intensive Reading Program - 8 Classes, 121 Students

EXECUTIVE SUMMARY:
Overall school RIT average: 220.5 (up from 216.8 at AP1, +3.7 growth)
78% of students showed growth from AP1 to AP2
3 classes above school average, 5 classes at or below

KEY HIGHLIGHTS:
✓ Period 06: Exceptional performance (233.2 avg, +12.7 above school avg)
✓ Period 03: Highest growth rate (+6.2 points, 85% of students growing)
✓ Reading Across Genres: Strongest category school-wide (220.1 avg)

AREAS OF CONCERN:
⚠️ Period 08: Below average with low growth (+1.2 points, 35% declining)
⚠️ DLA-02: Significantly below average (208.4, 40% declining students)
⚠️ Reading Informational Text: Weakest category school-wide (218.5 avg)

RESOURCE ALLOCATION RECOMMENDATIONS:
1. IMMEDIATE: Provide coaching support to Period 08 and DLA-02
2. MEDIUM-TERM: School-wide PD on informational text instruction
3. ONGOING: Peer observation program (Period 03/06 mentor other classes)

INTERVENTION NEEDS:
- 28 students (23%) scored below 210 RIT - Tier 3 intervention needed
- 45 students (37%) showed declining scores AP1→AP2 - monitor closely
- Reading Informational Text: 31 students (26%) in "Low" category

PREDICTED AP3 OUTCOMES (if trends continue):
- School average projected: 224.2 (+3.7 growth)
- Period 06 projected: 236.7
- DLA-02 projected: 209.2 (minimal growth - intervention critical)

NEXT STEPS:
1. Meet with Period 08 teacher to review instructional strategies
2. Assign instructional coach to DLA-02 for embedded support
3. Plan school-wide focus on Reading Informational Text (Feb-Mar)
4. Implement flexible grouping based on category needs
5. Schedule peer observations from Period 03 and Period 06
```

## Comparison Metrics Tracked

### Performance Metrics
- Average overall RIT score
- Median RIT score
- Standard deviation (class variability)
- Percentage of students in each performance level (High/Middle/Low)

### Growth Metrics
- Average growth rate (AP1→AP2, AP2→AP3)
- Percentage of students growing
- Percentage of students declining
- Individual student growth trajectories

### Category Metrics
- Average score per reporting category
- Category growth rates
- Percentage in High/Middle/Low per category
- Strongest and weakest categories

### Demographic Metrics
- Class size
- ELL percentage and performance
- ESE percentage and performance
- 504 percentage and performance

## Visualization Options

### Charts to Generate
1. **Bar Chart**: Class overall RIT comparison
2. **Line Graph**: Growth trajectories by class (AP1→AP2→AP3)
3. **Heat Map**: Four-category performance across classes
4. **Scatter Plot**: Class size vs. average RIT (check for correlation)
5. **Stacked Bar**: Percentage High/Middle/Low students per class

## Integration with Other Skills

**Works with**:
- `student-data-processor`: Requires processed multi-class data
- `reporting-category-tracker`: Uses category-level analysis
- `intervention-planner`: Identifies classes needing support

## File Paths Reference

**Input**:
- NWEA Master Tracker: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/NWEA_Master_Tracker_2025-2026.xlsx`
- Student Data Table: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Student Data Table ELA-2.xlsx`

**Output**:
- Class comparison reports: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Class_Comparisons/`
- Admin summary reports: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Admin_Reports/`

## Dependencies

**Required files**:
- NWEA Master Tracker with all class data
- Student Data Table with demographics
- Previous assessment data for growth calculations

**Python libraries**:
- pandas (data analysis)
- matplotlib/seaborn (visualizations)
- openpyxl (Excel export)
