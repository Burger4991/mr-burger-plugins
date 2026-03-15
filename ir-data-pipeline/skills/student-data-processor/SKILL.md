---
name: student-data-processor
description: >
  This skill should be used when "importing raw assessment data" or "processing NWEA and FAST exports". Use when "after receiving new assessment results", "creating master tracking files", or "preparing data for analysis and reporting".
version: 0.1.0
---
# Student Data Processor Skill

## Purpose
Import, validate, merge, and process NWEA and FAST assessment data for 10th grade Intensive Reading classes. This skill automates the workflow of converting raw assessment exports into structured tracking files with reporting categories, benchmarks, and student groupings.

## When to Use
- After receiving new NWEA (AP1, AP2, AP3) class CSV exports
- After receiving FAST PM (PM1, PM2, PM3) results
- When creating or updating master tracking files
- When preparing data for analysis and reporting

## Key Functions

### 1. Import NWEA Data
**Input**: Individual class CSV files from NWEA export
**Process**:
- Read all class CSV files from a specified directory
- Extract student demographics (ID, name, period)
- Extract overall RIT scores and Lexile ranges
- Extract 4 reporting category scores:
  - InstructionalArea1: Reading Across Genres
  - InstructionalArea2: Reading Informational Text
  - InstructionalArea3: Prose and Poetry
  - InstructionalArea4: Vocabulary
- Merge all classes into single master file

**Output**: Consolidated NWEA data ready for tracking

### 2. Import FAST Data
**Input**: FAST PM export file (Excel or CSV)
**Process**:
- Read FAST scale scores
- Extract benchmark-level performance data (ELA.10.R.x.x codes)
- Parse strength/weakness indicators with percentages
- Map benchmarks to NWEA reporting categories:
  - ELA.10.R.1.x → Prose and Poetry
  - ELA.10.R.2.x → Reading Informational Text
  - ELA.10.R.3.x → Reading Across Genres
  - ELA.10.V.1.x → Vocabulary
- Link with student demographics (ELL, ESE, 504 status)

**Output**: FAST data mapped to reporting category structure

### 3. Calculate Deltas (Growth Metrics)
**Input**: Student data with multiple assessment periods (e.g., AP1 and AP2 scores)
**Process**:
- Calculate overall RIT score differences (AP1→AP2, AP2→AP3)
- Calculate reporting category differences for each area
- Calculate Lexile range changes
- Identify growth trends:
  - Positive growth (improvement)
  - Stagnation (±2 points)
  - Regression (decline)

**Output**: Delta columns added to tracking file

### 4. Assign Performance Levels
**Input**: Student scores in each reporting category
**Process**:
- Calculate class-level thresholds for High/Middle/Low
  - **High**: Top 33% of class in that category
  - **Middle**: Middle 34% of class
  - **Low**: Bottom 33% of class
- Assign performance level to each student per category
- Format Winter/Spring scores as: "Score (Level)" (e.g., "228.0 (High)")
- Assign overall group based on average RIT score

**Output**: Performance level annotations for each category

### 5. Validate Data Quality
**Input**: Imported assessment data
**Process**:
- Check for missing student IDs
- Identify students missing assessment scores
- Flag duplicate entries
- Verify all classes are represented
- Check for outliers (scores >3 SD from mean)
- Report data quality issues

**Output**: Validation report with warnings/errors

### 6. Create Multi-Tab Tracking File
**Input**: Processed student data with class assignments
**Process**:
- Group students by class period
- Create separate sheet for each class
- Include columns:
  - Student ID, Last Name, First Name
  - RitScore_Fall, RitScore_Winter, RitScore_Spring
  - OverallScore_Difference (between periods)
  - Lexile scores and differences
  - 4 Reporting Categories (Fall, Winter, Spring, Differences)
  - Overall_Group (High/Middle/Low)
- Sort students by Overall_Group, then by overall RIT score
- Apply consistent formatting

**Output**: Excel file with tabs for each class period

## Data Structure Requirements

### NWEA CSV Format (Input)
Expected columns from NWEA export:
- StudentID
- StudentLastName, StudentFirstName
- ClassName (to identify period)
- RitScore (overall)
- Lexile (range)
- InstructionalArea1Name, InstructionalArea1RIT
- InstructionalArea2Name, InstructionalArea2RIT
- InstructionalArea3Name, InstructionalArea3RIT
- InstructionalArea4Name, InstructionalArea4RIT

### Master Tracking File Format (Output)
Per-class sheet columns:
```
StudentID | StudentLastName | StudentFirstName |
RitScore_Fall | RitScore_Winter | RitScore_Spring | OverallScore_Difference |
Lexile_Fall | Lexile_Winter | Lexile_Spring | Lexile_Difference |
InstructionalArea1RIT_Fall | InstructionalArea1RIT_Winter | InstructionalArea1RIT_Spring | InstructionalArea1_Difference |
InstructionalArea2RIT_Fall | InstructionalArea2RIT_Winter | InstructionalArea2RIT_Spring | InstructionalArea2_Difference |
InstructionalArea3RIT_Fall | InstructionalArea3RIT_Winter | InstructionalArea3RIT_Spring | InstructionalArea3_Difference |
InstructionalArea4RIT_Fall | InstructionalArea4RIT_Winter | InstructionalArea4RIT_Spring | InstructionalArea4_Difference |
Overall_Group
```

## Workflow Example

**Scenario**: Teacher receives AP2 (Winter) NWEA data

1. User invokes skill: `/student-data-processor`
2. Skill prompts: "Which assessment period are you importing? (AP1/AP2/AP3)"
3. User: "AP2"
4. Skill asks: "Path to NWEA class CSV files?"
5. User provides directory path
6. Skill:
   - Reads all CSV files in directory
   - Merges with existing AP1 data from master tracker
   - Calculates AP1→AP2 deltas
   - Assigns High/Middle/Low levels for Winter scores
   - Updates master tracking file with new data
   - Generates validation report
7. Skill outputs: "AP2 data imported successfully. 118 students updated across 8 classes. 3 students missing AP2 scores (see validation report)."

## Advanced Features

### Benchmark-to-Category Mapping
When importing FAST data, map individual benchmarks to reporting categories:

**Prose and Poetry** (InstructionalArea3):
- ELA.10.R.1.1: Plot, setting, conflict
- ELA.10.R.1.2: Theme development
- ELA.10.R.1.3: Character development
- ELA.10.R.1.4: Figurative language & tone

**Reading Informational Text** (InstructionalArea2):
- ELA.10.R.2.1: Central idea
- ELA.10.R.2.2: Text structure & features
- ELA.10.R.2.3: Author's purpose & rhetoric
- ELA.10.R.2.4: Argument analysis

**Reading Across Genres** (InstructionalArea1):
- ELA.10.R.3.1: Figurative language
- ELA.10.R.3.3: Intertextual connections
- ELA.10.R.3.4: Word choice, tone, mood

**Vocabulary** (InstructionalArea4):
- ELA.10.V.1.2: Morphology
- ELA.10.V.1.3: Context clues

### Smart Grouping
- Calculate thresholds dynamically per class (accounts for class composition)
- Option for school-wide thresholds (consistent across classes)
- Track group movement over time (High→Middle, Middle→Low, etc.)

## Error Handling

**Missing Students**:
- If student in AP1 not found in AP2, flag as "Missing AP2 Score"
- If new student appears in AP2, add to roster with blank AP1 data

**Class Changes**:
- If student changes periods between assessments, note in "Notes" column
- Track current period assignment

**Invalid Scores**:
- Flag scores outside expected range (150-260 for grade 10)
- Check for duplicate student IDs

## Integration Points

**Works with these skills**:
- `reporting-category-tracker`: Provides clean data for category analysis
- `class-comparison-generator`: Provides structured data for cross-class reports
- `benchmark-mastery-analyzer`: Provides FAST benchmark mappings
- `intervention-planner`: Provides student performance groups

## File Paths Reference

**Input locations**:
- NWEA class CSVs: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/AP1 25-26/` (or AP2, AP3)
- FAST PM files: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/`
- Student roster: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Student Data Table ELA-2.xlsx`

**Output locations**:
- Master tracking file: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/NWEA_Master_Tracker_2025-2026.xlsx`
- Validation reports: `/Users/alexanderburger/Desktop/2025-2026/Student Data 2025-2026/Reports/`

## Dependencies

**Python libraries**:
- pandas (data manipulation)
- openpyxl (Excel file handling)
- numpy (calculations)

**Required files**:
- Student Data Table (master roster with demographics)
- NWEA class CSV exports
- Previous assessment data (for delta calculations)
