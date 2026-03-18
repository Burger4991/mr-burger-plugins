---
name: student-data-workflow
description: >
  This skill should be used as the "master workflow guide" for "coordinating all student data analysis" throughout the school year. Use when "establishing assessment protocols", "orchestrating data analysis skills", or "referencing step-by-step procedures" for each assessment period.
version: 0.1.0
---
# Student Data Analysis Workflow - Master Guide

## Purpose
This is the master workflow guide that orchestrates all student data analysis skills. Reference this skill when working with assessment data throughout the 2025-2026 school year. It provides step-by-step protocols for each assessment period and coordinates all specialized data analysis skills.

## Skills Ecosystem

### Core Skills (Use in Order)
1. **`student-data-processor`**: Import and process raw NWEA/FAST data
2. **`reporting-category-tracker`**: Analyze 4 NWEA reporting categories
3. **`benchmark-mastery-analyzer`**: Deep-dive into FAST benchmarks
4. **`intervention-planner`**: Create flexible groups and intervention plans
5. **`class-comparison-generator`**: Compare classes for admin reports
6. **`data-visualization-builder`**: Generate charts and visual reports

### Supporting Skills
- **`ir-framework`**: Align data analysis to 6-day IR cycle
- **`esol-core`**: Differentiate for ELL students based on data
- **`benchmarks` skill**: Design organizers based on data needs (see standards/)

## Assessment Calendar 2025-2026

| Assessment | Window | Purpose | Skills to Use |
|------------|--------|---------|---------------|
| **AP1 (NWEA)** | Aug/Sep ✓ | Baseline data | processor, tracker, comparator |
| **PM1 (FAST)** | Sep/Oct | Benchmark baselines | processor, benchmark-analyzer |
| **AP2 (NWEA)** | Dec/Jan | Mid-year progress | ALL skills |
| **PM2 (FAST)** | Jan/Feb | Benchmark progress | benchmark-analyzer, intervention |
| **AP3 (NWEA)** | Mar/Apr | End-year outcomes | ALL skills |
| **PM3 (FAST)** | Apr/May | Final benchmarks | benchmark-analyzer, visualization |

## Complete Workflow by Assessment Period

### WORKFLOW 1: After Receiving NWEA Assessment (AP1, AP2, or AP3)

#### Step 1: Data Import & Processing
**Use Skill**: `student-data-processor`

**Actions**:
1. Locate NWEA class CSV files in district export folder
2. Invoke skill: Ask me to "Process NWEA AP[X] data"
3. Skill will:
   - Import all class files
   - Merge with existing data (if AP2 or AP3)
   - Calculate deltas (growth scores)
   - Assign High/Middle/Low performance levels
   - Create multi-tab tracking file by class
   - Generate validation report

**Outputs**:
- Updated master tracker: `NWEA_Master_Tracker_2025-2026.xlsx`
- Validation report highlighting missing data or issues

**Time**: ~10-15 minutes

---

#### Step 2: Reporting Category Analysis
**Use Skill**: `reporting-category-tracker`

**Actions**:
1. Invoke skill: Ask me to "Analyze reporting categories for all classes"
2. Skill will:
   - Track student progress across 4 categories
   - Identify top/bottom performers per category
   - Flag students with declining scores
   - Generate category strength/weakness profiles by class
   - Identify students with high category variance

**Outputs**:
- Category analysis report by class
- Student intervention lists (category-specific)
- Class strength/weakness summaries

**Time**: ~15-20 minutes

---

#### Step 3: Class Comparison (for Admin)
**Use Skill**: `class-comparison-generator`

**Actions**:
1. Invoke skill: Ask me to "Generate class comparison report for AP[X]"
2. Skill will:
   - Rank all classes by overall performance
   - Compare growth rates across classes
   - Analyze category performance by class
   - Create administrative summary report
   - Identify best practices from high-performing classes

**Outputs**:
- Executive summary for reading coach/principal
- Class comparison charts
- Intervention recommendations by class

**Time**: ~20 minutes

---

#### Step 4: Student Grouping & Intervention Planning
**Use Skill**: `intervention-planner`

**Actions**:
1. Invoke skill: Ask me to "Create flexible groups for [Class Period]"
2. Skill will:
   - Generate High/Middle/Low groups for each reporting category
   - Create grouping rosters with student details
   - Suggest differentiated instruction by group
   - Identify Tier 2 and Tier 3 intervention students
   - Design cross-category rotation schedules

**Outputs**:
- Grouping rosters for each class by category
- Intervention priority lists
- Flexible grouping rotation schedules

**Time**: ~25-30 minutes per class (or 3-4 hours for all classes)

---

#### Step 5: Visual Reports for Meetings
**Use Skill**: `data-visualization-builder`

**Actions**:
1. Invoke skill: Ask me to "Create visualizations for admin meeting"
2. Skill will:
   - Generate class comparison bar charts
   - Create student growth trajectory line graphs
   - Build category heat maps by class
   - Design executive dashboard for presentation

**Outputs**:
- PowerPoint-ready charts (PNG format)
- PDF reports for distribution
- Excel files with interactive visualizations

**Time**: ~20 minutes

---

### WORKFLOW 2: After Receiving FAST PM Assessment (PM1, PM2, or PM3)

#### Step 1: Data Import & Benchmark Mapping
**Use Skill**: `student-data-processor`

**Actions**:
1. Locate FAST PM export file
2. Invoke skill: Ask me to "Process FAST PM[X] data"
3. Skill will:
   - Import FAST scale scores
   - Extract benchmark-level performance (ELA.10.R.x.x)
   - Parse top strengths and weaknesses
   - Map benchmarks to NWEA reporting categories
   - Link with student demographics

**Outputs**:
- Updated FAST master tracker
- Benchmark-to-category mapping file

**Time**: ~10 minutes

---

#### Step 2: Benchmark Mastery Analysis
**Use Skill**: `benchmark-mastery-analyzer`

**Actions**:
1. Invoke skill: Ask me to "Analyze benchmark mastery for [Class Period]"
2. Skill will:
   - Generate student benchmark profiles
   - Calculate class mastery rates by benchmark
   - Identify priority benchmarks for instruction
   - Correlate NWEA categories with FAST benchmarks
   - Create benchmark-based flexible groups

**Outputs**:
- Class benchmark mastery report
- Priority benchmark list for instruction
- Benchmark grouping recommendations
- NWEA-FAST correlation analysis

**Time**: ~20 minutes per class

---

#### Step 3: Align Benchmarks to IR Units
**Use Skill**: `benchmark-mastery-analyzer` + IR framework skills

**Actions**:
1. Identify weakest benchmarks from analysis
2. Ask me to "Suggest IR unit sequence for [benchmarks]"
3. Use `benchmarks` skill (see standards/):
   - standards/theme.md for ELA.10.R.1.2
   - standards/argument.md for ELA.10.R.2.4
   - standards/central-idea.md for ELA.10.R.2.1
   - etc.

**Outputs**:
- Recommended unit sequence (6-12 weeks)
- Benchmark-aligned organizers for units
- Integration with 6-day IR cycle

**Time**: ~30 minutes

---

#### Step 4: Update Intervention Groups
**Use Skill**: `intervention-planner`

**Actions**:
1. Invoke skill: Ask me to "Update intervention groups based on FAST PM[X]"
2. Skill will:
   - Revise groups based on benchmark performance
   - Identify students moving up or down
   - Create benchmark-specific intervention groups
   - Design targeted instruction plans

**Outputs**:
- Updated grouping rosters
- Benchmark intervention plans
- Progress monitoring protocols

**Time**: ~20 minutes per class

---

### WORKFLOW 3: Mid-Cycle Progress Monitoring (Weekly/Bi-Weekly)

#### Quick Check-Ins
**Use Skill**: `reporting-category-tracker`

**Actions**:
1. Ask me to "Show progress for [Student Name]"
2. Skill will display:
   - Current category scores
   - Growth trends since last assessment
   - Group assignment
   - Intervention recommendations

**Time**: ~2-3 minutes per student

---

#### Regrouping Based on Formative Data
**Use Skill**: `intervention-planner`

**Actions**:
1. After 4-6 weeks of instruction, reassess students informally
2. Ask me to "Regroup [Class Period] based on recent progress"
3. Update grouping rosters

**Time**: ~15 minutes

---

### WORKFLOW 4: Before Admin Meetings

#### Complete Meeting Prep
**Use Skills**: `class-comparison-generator` + `data-visualization-builder`

**Actions**:
1. Ask me to "Prepare admin report for [Assessment Period]"
2. I will:
   - Generate executive summary
   - Create comparison charts
   - Build presentation-ready visualizations
   - Highlight key trends and concerns
   - Provide data-driven recommendations

**Outputs**:
- Executive summary (1-2 pages)
- PowerPoint slides with charts
- Talking points for discussion

**Time**: ~30 minutes

---

## Example Workflow Scenarios

### Scenario 1: "I just received AP2 (Winter NWEA) data. What should I do?"

**Step-by-step**:
1. **Day 1**: Process data
   - Use `student-data-processor` to import and merge AP2 data
   - Review validation report for issues

2. **Day 2**: Analyze categories and classes
   - Use `reporting-category-tracker` for category analysis
   - Use `class-comparison-generator` for class comparisons

3. **Day 3-4**: Plan interventions and grouping
   - Use `intervention-planner` to create new groups
   - Print grouping rosters

4. **Day 5**: Create visuals and reports
   - Use `data-visualization-builder` for admin meeting
   - Prepare presentation

5. **Week 2**: Implement new groupings
   - Begin instruction with new flexible groups
   - Use IR framework for differentiation

---

### Scenario 2: "I need to prepare for a meeting with my principal tomorrow about how classes are performing."

**Quick Workflow** (1-2 hours):
1. Use `class-comparison-generator`:
   - "Generate admin summary report for current assessment"

2. Use `data-visualization-builder`:
   - "Create class comparison charts for presentation"

3. Review outputs and add narrative:
   - What's working (high-growth classes)
   - What needs support (low-growth or declining classes)
   - Specific action steps

**Deliverables**:
- Executive summary (1 page)
- 3-5 PowerPoint slides with charts
- Talking points

---

### Scenario 3: "I want to regroup my Period 01 class based on their Reading Informational Text performance."

**Quick Workflow** (30 minutes):
1. Use `intervention-planner`:
   - "Create Reading Informational Text groups for Period 01"

2. Review roster and plan differentiation:
   - Group 1 (High): Extension activities
   - Group 2 (Middle): Guided practice
   - Group 3 (Low): Intensive intervention

3. Use `ir-framework` to integrate into 6-day cycle

---

### Scenario 4: "A student's parent wants to see their progress. I need a visual report."

**Quick Workflow** (15 minutes):
1. Use `reporting-category-tracker`:
   - "Show progress for [Student Name]"

2. Use `data-visualization-builder`:
   - "Create student dashboard for [Student Name]"

**Deliverable**:
- 1-page student dashboard with:
  - Growth trajectory chart
  - Category performance
  - Benchmark strengths/weaknesses
  - Recommendations

---

## Data-Driven Instruction Integration

### How Data Informs Instruction (Continuous Cycle)

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA-DRIVEN CYCLE                        │
└─────────────────────────────────────────────────────────────┘
        │
        ↓
  [1] ASSESS → (NWEA AP1, FAST PM1)
        │
        ↓
  [2] ANALYZE → (Use skills: processor, tracker, comparator)
        │
        ↓
  [3] GROUP → (Use skill: intervention-planner)
        │
        ↓
  [4] PLAN → (Align to IR framework, select benchmarks)
        │
        ↓
  [5] INSTRUCT → (Differentiated lessons, flexible groups)
        │
        ↓
  [6] MONITOR → (Formative assessments, exit tickets)
        │
        ↓
  [7] ADJUST → (Regroup, modify instruction)
        │
        └──→ Return to [1] ASSESS (next period)
```

### Connecting Data to Daily Instruction

**Monday (Review Data)**:
- Check student progress from previous week
- Adjust groups if needed

**Tuesday-Thursday (Differentiated Instruction)**:
- Group 1: Extension/enrichment
- Group 2: Guided practice with scaffolds
- Group 3: Intensive small-group intervention

**Friday (Formative Assessment)**:
- Exit tickets aligned to target benchmarks
- Informal progress checks
- Plan next week based on results

---

## Key Decision Points

### When to Regroup Students
- Every 4-6 weeks (formal regrouping)
- After each major assessment (AP1, AP2, AP3)
- When students show significant growth or decline
- When transitioning to new reporting category focus

### When to Escalate to Tier 3 Intervention
- NWEA score <200 AND FAST benchmarks <40%
- Declining scores across 2+ assessment periods
- Student in "Low" group across all 4 categories
- Minimal growth despite Tier 2 intervention

### When to Move Students to Extension Activities
- Consistently in "High" group across all categories
- FAST benchmarks ≥90% proficiency
- Showing boredom or off-task behavior
- Peer teaching opportunities available

---

## Troubleshooting

### "Data doesn't match between NWEA and FAST"
**Use Skill**: `benchmark-mastery-analyzer` → NWEA-FAST Correlation Analysis
- High NWEA but low FAST = test-taking skills masking content gaps
- Low NWEA but high FAST = unusual, investigate testing conditions

### "Student in different groups for different categories"
**This is normal and expected!**
- Use cross-category flexible grouping
- Celebrate category-specific strengths
- Target category-specific weaknesses

### "Too many students need Tier 3 intervention"
**Options**:
1. Prioritize most critical students
2. Consider whole-class instructional adjustments
3. Request additional support (paraprofessional, reading coach)
4. Implement more intensive Tier 2 first

---

## File Organization

### Recommended Directory Structure
```
Student Data Folder (user-provided location)/
├── AP1/ (class CSV files)
├── AP2/
├── AP3/
├── FAST_PM_Files/ (or PM1/, PM2/, PM3/ subfolders)
├── Master_Trackers/
│   ├── NWEA_Master_Tracker_2025-2026.xlsx
│   ├── FAST_Master_Tracker_2025-2026.xlsx
│   └── Student_Data_Master.xlsx
├── Reports/
│   ├── AP1_Reports/
│   ├── AP2_Reports/
│   ├── AP3_Reports/
│   ├── Category_Analysis/
│   ├── Class_Comparisons/
│   ├── Benchmark_Analysis/
│   ├── Visualizations/
│   └── Grouping/
└── Student Data Table/ (or individual roster files)
```

**Important**: At the start of each session, ask the user for the path to their student data folder. All files will be saved relative to this location.

---

## Quick Reference Commands

### Most Common Requests
- "Process NWEA AP2 data"
- "Analyze reporting categories for Period 01"
- "Create flexible groups for Period 01"
- "Generate class comparison report"
- "Show progress for [Student Name]"
- "Create admin presentation for AP2"
- "Identify students needing Tier 3 intervention"
- "Analyze benchmark mastery for Period 01"

---

## Success Metrics

### How to Know the Workflow is Working
✓ Grouping is fluid and responsive to data
✓ Intervention is targeted and specific
✓ Instructional planning is benchmark-aligned
✓ Admin meetings are data-rich and productive
✓ Student growth is visible and celebrated
✓ Equity gaps are identified and addressed
✓ Teacher decision-making is faster and more confident

---

## Dependencies

This workflow orchestrates ALL data analysis skills:
- `student-data-processor`
- `reporting-category-tracker`
- `benchmark-mastery-analyzer`
- `intervention-planner`
- `class-comparison-generator`
- `data-visualization-builder`

Plus supporting skills:
- `ir-framework`
- `esol-core`
- Benchmark-specific skills (theme, argument, etc.)

---

## Contact & Support

**For workflow questions**: Ask me "How do I [task] with student data?"
**For skill-specific help**: Invoke the specific skill (e.g., `/intervention-planner`)
**For troubleshooting**: Describe the issue and I'll guide you through

**Remember**: This workflow is designed to SAVE YOU TIME and make data analysis EASY. Don't hesitate to ask me to handle any part of this process!
