---
name: data-visualization-builder
description: >
  Use to generate presentation-ready visual reports (charts, graphs, dashboards) from assessment data.
  Creates PNG/PDF/PowerPoint-formatted visualizations for visual storytelling. Use when creating data-driven
  presentations, conducting parent conferences, showcasing growth trajectories, preparing for meetings
  where visual impact matters, or when you need charts (not spreadsheet format).

  Note: For comprehensive multi-sheet Excel workbooks with formatted tables and KPI dashboards, use
  report-builder instead.
version: 0.1.0
---
# Data Visualization Builder Skill

## Purpose
Generate professional charts, graphs, and visual reports from NWEA and FAST assessment data. Create presentation-ready visualizations for meetings with administration, parents, and instructional planning sessions. Make complex data accessible and actionable through clear, compelling visuals.

## When to Use
- Before meetings with reading coach or principal
- Creating data-driven presentations
- Parent conferences requiring visual progress reports
- Department meetings showcasing student growth
- End-of-year reports and program evaluations

## Key Functions

### 1. Student Growth Trajectory Charts
**Input**: Individual student or group of students
**Output**: Line graph showing RIT score progression across AP1, AP2, AP3
**Use Case**: Student conferences, progress monitoring, celebrating growth

**Visualization**:
```
Student Growth Trajectory: CHARLES, Devani

RIT Score Over Time
240 ┤                                        ● (AP2: 232)
235 ┤                               ╱
230 ┤                      ╱
225 ┤             ╱
220 ┤    ╱
215 ┤
210 ┤
205 ┤ ● (AP1: 207)
    └────────────────────────────────────────
      AP1       AP2       AP3
    (Fall)   (Winter)  (Spring)

Growth: +25 points (+12%)
Trajectory: ACCELERATING ↗
Projected AP3: 245 (if trend continues)
```

**Features**:
- Multiple students overlaid for comparison
- Color-coded by performance level (Green=High, Yellow=Middle, Red=Low)
- Trend lines and projections
- Annotations for key events (interventions, absences)

### 2. Class Comparison Bar Charts
**Input**: All classes, specific metric (overall RIT, category scores, growth rate)
**Output**: Horizontal or vertical bar chart comparing classes
**Use Case**: Admin meetings, identifying classes needing support

**Visualization**:
```
Class Performance Comparison - Overall RIT (AP2)

Period 06  ████████████████████████████ 233.2 ⭐
Period 04  ██████████████████████████ 228.4 ⭐
Period 02  ████████████████████ 224.1 ✓
Period 07  ██████████████████ 221.8 →
Period 03  █████████████████ 219.3 →
Period 01  ████████████████ 217.6 ⚠️
Period 08  ██████████████ 215.2 ⚠️
DLA-02     ████████████ 208.4 ⚠️
           ├────┬────┬────┬────┬────┬────┬────┐
          200  210  220  230  240  250  260
                Average RIT Score

School Average: 220.5 (dotted line)
Color Key: 🟢 Above Avg | 🟡 At Avg | 🔴 Below Avg
```

**Features**:
- School-wide average reference line
- Color-coded performance tiers
- Data labels showing exact values
- Ranking indicators

### 3. Reporting Category Heat Maps
**Input**: All students in a class, all 4 reporting categories
**Output**: Heat map showing student performance across categories
**Use Case**: Identifying patterns, planning differentiation

**Visualization**:
```
Period 01 - Reporting Category Heat Map (AP2)

Student Name         Reading   Reading    Prose &   Vocabulary
                     Across    Info Text  Poetry
                     Genres

LAFOND, Kehana        🟢 236    🟢 241    🟢 247    🟢 243
JEAN-CLAUDE, Werleigh 🟢 229    🟢 248    🟢 228    🟢 225
CHARLES, Devani       🟢 225    🟢 232    🟢 232    🟡 219
FERNANDEZ, Mathias    🟢 228    🟡 217    🟢 235    🟢 221
GONZALEZRODRIG, Gen.  🟢 221    🟢 235    🟡 213    🟡 218
JEAN, Judith          🟢 221    🟢 226    🔴 195    🟡 213
ROGERS, Ailin         🟡 217    🟢 227    🟡 218    🟢 227
PIERRE, Kervin        🟡 216    🔴 200    🟢 227    🟢 223
BOURGUILLON, Feneisha 🟡 207    🔴 203    🔴 196    🟡 216
LAWRENCE, Raheem      🟡 207    🔴 201    🟡 209    🟡 219
IDRIS, Sirag          🟡 211    🔴 204    🟡 208    🔴 202
HERNANDEZ, Adelanic   🟡 207    🔴 203    🔴 196    🟡 216
LAROCHE, Fabrice      🟡 215    🔴 202    🔴 198    🔴 193
MITCHELL, Kamaiyah    🔴 171    🔴 191    🔴 180    🔴 184

Color Key:
🟢 High (Top 33%)  🟡 Middle (Mid 34%)  🔴 Low (Bottom 33%)

Pattern Analysis:
- Reading Informational Text: Most common weakness (7 students low)
- Prose & Poetry: Mixed performance (4 students low, 7 high/middle)
- Vocabulary: Relatively balanced (only 2 students low)
```

**Features**:
- Color-coded cells for quick visual scanning
- Sortable by student name or specific category
- Pattern highlights (which categories are weakest class-wide)
- Export to Excel with conditional formatting

### 4. Growth Rate Distribution Charts
**Input**: Class or cohort, assessment period comparison (AP1→AP2)
**Output**: Histogram or box plot showing distribution of growth
**Use Case**: Evaluating intervention effectiveness, identifying outliers

**Visualization**:
```
Period 01 - Growth Distribution (AP1 → AP2)

Number of Students
6 ┤               ████
  │               ████
5 ┤          ████ ████
  │          ████ ████
4 ┤     ████ ████ ████
  │     ████ ████ ████
3 ┤ ████ ████ ████ ████
  │ ████ ████ ████ ████
2 ┤ ████ ████ ████ ████ ████
  │ ████ ████ ████ ████ ████
1 ┤ ████ ████ ████ ████ ████ ████
  └─────┬─────┬─────┬─────┬─────┬─────
      -10   -5    0    +5   +10  +15+
                Growth (RIT Points)

Statistics:
- Average Growth: +4.1 points
- Median Growth: +3.5 points
- Range: -4 to +25 points
- % Students Growing: 71% (10/14)
- % Students Declining: 21% (3/14)

Outliers:
- CHARLES, Devani: +25 points (exceptional growth) ⭐
- HERNANDEZ, Adelanic: -4 points (declining) ⚠️
```

**Features**:
- Normal distribution curve overlay
- Average and median indicators
- Outlier identification
- Percentile markings

### 5. Benchmark Mastery Radar Charts
**Input**: Student or class, FAST benchmark percentages
**Output**: Radar/spider chart showing proficiency across all benchmarks
**Use Case**: Visualizing benchmark strengths/weaknesses for unit planning

**Visualization**:
```
ROGERS, Ailin - Benchmark Mastery Profile (FAST PM1)

        R.1.1 (Plot)
         100% ●
              │╲
              │ ╲
     R.3.4    │  ╲    R.1.2 (Theme)
   (Word      │   ●    100%
    Choice)   │   │
     75%  ●───┼───●───●  R.1.3 (Character)
              │   │        67%
              │   │
     V.1.3    │   │        R.2.1 (Central)
   (Context)  │   │         33%
     33%  ●   │   ●
          ╲   │  ╱
           ╲  │ ╱
            ╲ │╱
             ●
        R.2.3 (Purpose)
            33%

Strengths: Literature benchmarks (R.1.x) - 89% avg
Weaknesses: Informational benchmarks (R.2.x) - 33% avg
Priority: Focus on R.2.1 and R.2.3
```

**Features**:
- All benchmarks visible at once
- Easy identification of gaps
- Comparison overlays (multiple students or class average)
- Benchmark categories color-coded

### 6. Progress Monitoring Dashboards
**Input**: Student or class, all available data points
**Output**: Comprehensive dashboard with multiple visualizations
**Use Case**: Comprehensive progress reports for admin or parents

**Dashboard Layout**:
```
═══════════════════════════════════════════════════════════════
STUDENT PROGRESS DASHBOARD: CHARLES, Devani (0557620)
Period 01 | Generated: [Date]
═══════════════════════════════════════════════════════════════

┌─────────────────────────────┐  ┌─────────────────────────────┐
│  Overall RIT Trajectory     │  │  Category Performance (AP2) │
│                             │  │                             │
│  240 ┤           ● (232)    │  │  Reading Across: 225 🟢     │
│  230 ┤      ╱               │  │  Reading Info:   232 🟢     │
│  220 ┤ ╱                    │  │  Prose & Poetry: 232 🟢     │
│  210 ┤                      │  │  Vocabulary:     219 🟡     │
│  200 ┤                      │  │                             │
│      └────────────────      │  │  Overall: STRONG            │
│        AP1      AP2         │  │  Growth:  +25 pts (+12%)    │
└─────────────────────────────┘  └─────────────────────────────┘

┌─────────────────────────────┐  ┌─────────────────────────────┐
│  FAST Benchmark Strengths   │  │  Intervention Grouping      │
│                             │  │                             │
│  Top 3:                     │  │  Reading Across: Group 1    │
│  • R.1.4 (Fig Lang): 100%   │  │  Reading Info:   Group 1    │
│  • R.3.4 (Tone):     100%   │  │  Prose & Poetry: Group 1    │
│  • V.1.3 (Context):  100%   │  │  Vocabulary:     Group 2    │
│                             │  │                             │
│  Focus Areas:               │  │  Role: Peer tutor, extend   │
│  • Theme (R.1.2): 0%        │  │  Next Steps: Advanced texts │
│  • Argument (R.2.4): 0%     │  │                             │
└─────────────────────────────┘  └─────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│  Recommendations                                              │
│                                                               │
│  ✓ Exceptional growth (+25 points) - Celebrate success!      │
│  ✓ Ready for advanced/honors-level texts                     │
│  → Focus: Theme analysis and argument evaluation             │
│  → Provide leadership opportunities (peer teaching)          │
│  → Consider grouping with LAFOND for collaborative projects  │
└───────────────────────────────────────────────────────────────┘
```

### 7. Class-Level Category Comparison (Stacked Bar)
**Input**: Class period, all 4 categories
**Output**: Stacked bar chart showing % High/Middle/Low in each category
**Use Case**: Identifying category-specific needs for the class

**Visualization**:
```
Period 01 - Category Performance Distribution (AP2)

Reading Across     ████████ 40%  ████████ 35%  ██████ 25%
Genres             High           Middle        Low

Reading Info      ██████ 25%   ████████ 30%   ████████████ 45%
Text               High          Middle         Low

Prose &           ████████████ 45%  ████████ 35%  ██████ 20%
Poetry             High              Middle        Low

Vocabulary        ████████████████ 65%  ██████ 25%  ███ 10%
                   High                 Middle       Low

                  └──────┬──────┬──────┬──────┬──────┬──────┐
                        20%    40%    60%    80%   100%

Insight:
- Vocabulary: Strongest category (65% High)
- Reading Informational Text: Weakest (45% Low) - PRIORITY
- Prose & Poetry: Balanced distribution
```

### 8. Subgroup Equity Gap Visualizations
**Input**: Subgroup (ELL, ESE, Gen Ed), comparison metric
**Output**: Side-by-side comparison charts highlighting gaps
**Use Case**: Monitoring equity, identifying disproportionate outcomes

**Visualization**:
```
Equity Gap Analysis - Reading Informational Text (AP2)

Average RIT Scores by Subgroup:

General Ed    ████████████████████████ 228.3
ELL           ███████████████████ 219.6  ⚠️ Gap: -8.7
ESE           ████████████████ 212.4    ⚠️ Gap: -15.9
504           ████████████████████ 221.5  ⚠️ Gap: -6.8

              └────┬────┬────┬────┬────┬────┬────┐
                 200  210  220  230  240  250  260

════════════════════════════════════════════════════════════

Percentage in Each Performance Level:

            High (≥225)  Middle (210-224)  Low (<210)
General Ed   ████████████████████ 61%  ████ 28%  ██ 11%
ELL          ████ 19%  ████████████ 50%  ████████ 31%
ESE          █ 8%   ██████ 33%  ████████████ 59%
504          ████ 25%  ████████ 50%  ████ 25%

Insight:
- ESE students face significant equity gap (-15.9 points)
- 59% of ESE students in Low category vs. 11% of Gen Ed
- ELL students performing better than ESE but still below Gen Ed
- Intensive intervention needed for ESE subgroup
```

### 9. Scatter Plots (Correlation Analysis)
**Input**: Two variables (e.g., NWEA score vs. attendance, NWEA vs. FAST)
**Output**: Scatter plot showing correlation
**Use Case**: Identifying factors affecting performance

**Visualization**:
```
Correlation: NWEA Overall RIT vs. Attendance (Period 01)

RIT Score
250 ┤
240 ┤                    ●
230 ┤              ●  ●
220 ┤         ●  ●  ●
210 ┤      ●  ●
200 ┤   ●  ●
190 ┤ ●
180 ┤●
    └────┬────┬────┬────┬────┬────┬────┐
        60%  70%  80%  90%  95%  98% 100%
                Attendance Rate

Correlation: r = 0.72 (Strong Positive)
Insight: Students with higher attendance show significantly higher RIT scores.
Students below 80% attendance are struggling (all in Low category).

Action: Target attendance interventions for students with <85% attendance.
```

### 10. Exportable Summary Tables
**Input**: Any data set
**Output**: Formatted table ready for reports or presentations
**Use Case**: Including data in written reports, emails to admin

**Example Table**:
```
Period 01 Summary Table - AP2 (Winter 2025-2026)

┌────────────────────┬────────┬──────────┬────────┬───────────┐
│ Student Name       │ Ovr RIT│ AP1→AP2  │ Group  │ Priority  │
├────────────────────┼────────┼──────────┼────────┼───────────┤
│ LAFOND, Kehana     │   242  │   +1     │ High   │ Extension │
│ JEAN-CLAUDE, W.    │   229  │   +8     │ High   │ Maintain  │
│ CHARLES, Devani    │   232  │  +25 ⭐  │ High   │ Celebrate │
│ FERNANDEZ, Mathias │   226  │   +4     │ Middle │ Monitor   │
│ GONZALEZRODRIG, G. │   221  │   +5     │ Middle │ Monitor   │
│ JEAN, Judith       │   216  │   +3     │ Middle │ Monitor   │
│ ROGERS, Ailin      │   222  │   +4     │ Middle │ Monitor   │
│ PIERRE, Kervin     │   217  │  +10     │ Middle │ Progress  │
│ BOURGUILLON, F.    │   207  │   +1     │ Low    │ Tier 2    │
│ LAWRENCE, Raheem   │   208  │  +11     │ Low    │ Progress  │
│ IDRIS, Sirag       │   206  │   -2     │ Low    │ Tier 2    │
│ HERNANDEZ, A.      │   203  │   -4 ⚠️  │ Low    │ Tier 3    │
│ LAROCHE, Fabrice   │   202  │   +0     │ Low    │ Tier 3    │
│ MITCHELL, Kamaiyah │   183  │   +8     │ Low    │ Tier 3    │
└────────────────────┴────────┴──────────┴────────┴───────────┘

Class Average: 217.6 (School Avg: 220.5)
% Growing: 71%  |  % Declining: 21%  |  % Stable: 8%
```

## Visualization Types Summary

| Visualization | Best For | Output Format |
|---------------|----------|---------------|
| Line Graph | Growth over time, trajectories | PNG, PDF, Excel |
| Bar Chart | Class comparisons, rankings | PNG, PDF, PPT |
| Heat Map | Multi-category performance | Excel (conditional formatting) |
| Histogram | Growth distribution | PNG, PDF |
| Radar Chart | Benchmark profiles | PNG, PDF |
| Dashboard | Comprehensive overview | PDF, PPT |
| Stacked Bar | Category distributions | PNG, PDF, PPT |
| Scatter Plot | Correlations | PNG, PDF |
| Table | Detailed data for reports | Excel, Word, PDF |

## Color Conventions

### Performance Levels
- 🟢 **Green**: High performers (top 33%)
- 🟡 **Yellow**: Middle performers (middle 34%)
- 🔴 **Red**: Low performers (bottom 33%)

### Growth Indicators
- ⭐ **Star**: Exceptional growth (≥10 points)
- ↗ **Up Arrow**: Positive growth (+3 to +9 points)
- → **Right Arrow**: Stable (±2 points)
- ↘ **Down Arrow**: Declining (-3 or more points)
- ⚠️ **Warning**: Critical concern (significant decline or very low score)

### Accessibility
- All charts include text labels (not color-only)
- High-contrast color schemes
- Alternative formats available (tables for screen readers)

## Export Formats

### For Presentations (PowerPoint, Google Slides)
- High-resolution PNG images (300 DPI)
- Transparent backgrounds
- Consistent sizing (16:9 aspect ratio)

### For Reports (Word, PDF)
- Vector graphics (PDF) for scalability
- Embedded Excel tables
- Caption-ready with titles and legends

### For Interactive Use (Excel, Google Sheets)
- Conditional formatting
- Interactive filters
- Sortable tables
- Embedded charts

## Integration with Other Skills

**Works with**:
- `student-data-processor`: Visualizes processed data
- `reporting-category-tracker`: Creates category-specific charts
- `class-comparison-generator`: Visualizes class comparisons
- `intervention-planner`: Creates grouping visualizations

## File Paths Reference

**Input**:
- NWEA Master Tracker: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/NWEA_Master_Tracker_2025-2026.xlsx`
- FAST PM Data: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/`

**Output**:
- Visualizations: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Visualizations/`
- Dashboards: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/Dashboards/`

## Technical Implementation

### Python Libraries to Use
- **matplotlib**: Static charts (line graphs, bar charts, histograms)
- **seaborn**: Advanced visualizations with better styling, heat maps
- **plotly**: Interactive dashboards and HTML-based visualizations
- **pandas**: Data manipulation and transformation
- **openpyxl**: Excel export with conditional formatting

### Top 3 Chart Types for Student Data

**1. Growth Trajectory Line Chart (Primary)**
Purpose: Visualize individual or group progress across assessment periods
Best for: Student conferences, progress monitoring, celebrating growth
Key features: Multiple students overlaid, trend lines, projections, benchmark lines

**2. Class Distribution Histogram**
Purpose: Show score distributions across the class with quartile markers
Best for: Identifying intervention needs, understanding class-wide performance patterns
Key features: Normal distribution overlay, quartile lines, average/median indicators

**3. Risk Tier Bar Chart**
Purpose: Quickly show how many students are in each intervention tier
Best for: Admin meetings, identifying classes needing intensive support
Key features: Color-coded by tier (green/yellow/red), stacked by ELL/ESE if relevant

### Growth Trajectory Chart - Code Skeleton

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_growth_trajectory(student_data, benchmark_line=220):
    """
    Plot RIT score growth across assessment periods.

    Args:
        student_data: DataFrame with columns [student_name, AP1, AP2, AP3]
        benchmark_line: Grade-level benchmark (default 220)
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    periods = ['AP1 (Fall)', 'AP2 (Winter)', 'AP3 (Spring)']
    x_pos = np.arange(len(periods))

    # Plot each student as a line
    for idx, row in student_data.iterrows():
        scores = [row['AP1'], row['AP2'], row['AP3']]
        color = 'green' if row['AP3'] >= benchmark_line else 'orange' if row['AP2'] >= benchmark_line else 'red'
        ax.plot(x_pos, scores, marker='o', label=row['student_name'], color=color, linewidth=2)

    # Add benchmark line
    ax.axhline(y=benchmark_line, color='blue', linestyle='--', linewidth=2, label='Grade-Level Benchmark')

    # Formatting
    ax.set_xticks(x_pos)
    ax.set_xticklabels(periods)
    ax.set_ylabel('RIT Score', fontsize=12)
    ax.set_title('Student Growth Trajectory', fontsize=14, fontweight='bold')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig

# Usage:
# fig = plot_growth_trajectory(student_df)
# fig.savefig('growth_trajectory.png', dpi=300, bbox_inches='tight')
```

### Output Formats

**Static Reports & Presentations**
- PNG (300 DPI) for PowerPoint, Google Slides, Word documents
- PDF for printed reports and admin submissions
- File naming: `[Period]_[ChartType]_[Date].png`

**Interactive Dashboards**
- HTML with Plotly for exploratory analysis
- Self-contained files with embedded JavaScript
- Can be emailed or shared via web links

**Data Tables**
- Excel (.xlsx) with conditional formatting
- CSV for data import into other tools
- Include metadata (date created, data source, notes)
