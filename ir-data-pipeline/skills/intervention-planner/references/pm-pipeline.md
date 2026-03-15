---
name: intervention-planner
description: Generate prioritized actionable insights with recommendations from growth and benchmark data
version: 1.0.0
prerequisites:
  - growth-analyzer
  - benchmark-mastery-analyzer
input_files:
  - _intermediate/growth_analysis.csv
  - _intermediate/benchmark_mastery.csv
output_files:
  - _intermediate/actionable_insights.csv
tags:
  - intervention
  - insights
  - recommendations
  - priority
---

# PM Intervention Planner

## Purpose

Analyzes growth and benchmark mastery data to generate prioritized actionable insights with specific recommendations for intervention planning. Identifies critical needs, at-risk students, growth patterns, and opportunities for targeted instruction.

## Input Requirements

### Required Files

1. **_intermediate/growth_analysis.csv**
   - From growth-analyzer
   - Contains: Student_Name, Risk_Score, RTI_Tier, Growth_Rate, Achievement_Change, EOY_Projection, etc.

2. **_intermediate/benchmark_mastery.csv**
   - From benchmark-mastery-analyzer
   - Contains: Benchmark, Total_Items, Mastery_Pct, Student names with item-level detail

### Expected Columns

**growth_analysis.csv:**
- Student_Name (str)
- Risk_Score (float)
- RTI_Tier (int) - NUMERIC: 1, 2, or 3
- Growth_Rate (float)
- Achievement_Change (str)
- EOY_Projection (str)
- Current_Achievement (str)

**benchmark_mastery.csv:**
- Benchmark (str)
- Total_Items (int)
- Mastery_Pct (float)
- Individual student columns with mastery percentages

## Output Artifacts

### _intermediate/actionable_insights.csv

Columns:
- **Category** (str): Type of insight
  - "Benchmark Priority"
  - "At-Risk Students"
  - "Growth Trends"
  - "Achievement Gains"
  - "EOY Projection"
  - "Strength Area"
- **Insight** (str): Specific observation
- **Priority** (str): Critical, High, Medium, Positive
- **Recommendation** (str): Specific actionable step

## Implementation

```python
#!/usr/bin/env python3
"""
PM Intervention Planner

Generates prioritized actionable insights with specific recommendations
from growth and benchmark mastery data.

Quality Standards Applied:
- Constants extraction with type hints
- Comprehensive type annotations
- Robust input validation
- Specific error handling
- Google-style docstrings
- Edge case handling (NaN, empty data)
- Logging instead of print
- Path safety with pathlib
- No magic numbers
- Modular design
"""

import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONSTANTS
# ============================================================================

# File paths
INTERMEDIATE_DIR: Path = Path("_intermediate")
GROWTH_ANALYSIS_FILE: Path = INTERMEDIATE_DIR / "growth_analysis.csv"
BENCHMARK_MASTERY_FILE: Path = INTERMEDIATE_DIR / "benchmark_mastery.csv"
OUTPUT_FILE: Path = INTERMEDIATE_DIR / "actionable_insights.csv"

# Threshold constants
CRITICAL_MASTERY_THRESHOLD: float = 30.0  # Below this is critical priority
HIGH_MASTERY_THRESHOLD: float = 50.0      # Below this is high priority
STRENGTH_MASTERY_THRESHOLD: float = 70.0  # Above this is strength

CRITICAL_RISK_THRESHOLD: float = 70.0     # Risk score indicating critical need
TIER_3_VALUE: int = 3                     # RTI Tier 3 (NUMERIC, not string)

RAPID_DECLINE_THRESHOLD: float = -10.0    # Growth rate indicating rapid decline
RAPID_GROWTH_THRESHOLD: float = 10.0      # Growth rate indicating rapid growth

TOP_N_BENCHMARKS: int = 3                 # Number of top/bottom benchmarks to report
TOP_N_STUDENTS: int = 3                   # Number of students to name in recommendations

# Category names
CATEGORY_BENCHMARK_PRIORITY: str = "Benchmark Priority"
CATEGORY_AT_RISK: str = "At-Risk Students"
CATEGORY_GROWTH_TRENDS: str = "Growth Trends"
CATEGORY_ACHIEVEMENT_GAINS: str = "Achievement Gains"
CATEGORY_EOY_PROJECTION: str = "EOY Projection"
CATEGORY_STRENGTH_AREA: str = "Strength Area"

# Priority levels
PRIORITY_CRITICAL: str = "Critical"
PRIORITY_HIGH: str = "High"
PRIORITY_MEDIUM: str = "Medium"
PRIORITY_POSITIVE: str = "Positive"

# Required columns
REQUIRED_GROWTH_COLS: List[str] = [
    'Student_Name', 'Risk_Score', 'RTI_Tier', 'Growth_Rate',
    'Achievement_Change', 'EOY_Projection', 'Current_Achievement'
]
REQUIRED_BENCHMARK_COLS: List[str] = ['Benchmark', 'Total_Items', 'Mastery_Pct']

# ============================================================================
# DATA VALIDATION
# ============================================================================

def validate_file_exists(file_path: Path) -> None:
    """
    Validate that required file exists.

    Args:
        file_path: Path to file to check

    Raises:
        FileNotFoundError: If file does not exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")
    logger.info(f"Validated file exists: {file_path}")


def validate_required_columns(df: pd.DataFrame, required_cols: List[str],
                              file_name: str) -> None:
    """
    Validate that DataFrame contains required columns.

    Args:
        df: DataFrame to validate
        required_cols: List of required column names
        file_name: Name of file for error message

    Raises:
        ValueError: If required columns are missing
    """
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Missing required columns in {file_name}: {missing_cols}"
        )
    logger.info(f"Validated required columns in {file_name}")


def validate_numeric_column(df: pd.DataFrame, col_name: str,
                           file_name: str) -> None:
    """
    Validate that column contains numeric data.

    Args:
        df: DataFrame containing column
        col_name: Name of column to validate
        file_name: Name of file for error message

    Raises:
        ValueError: If column is not numeric
    """
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        raise ValueError(
            f"Column '{col_name}' in {file_name} must be numeric, "
            f"got dtype: {df[col_name].dtype}"
        )
    logger.info(f"Validated numeric column '{col_name}' in {file_name}")


# ============================================================================
# DATA LOADING
# ============================================================================

def load_growth_data() -> pd.DataFrame:
    """
    Load and validate growth analysis data.

    Returns:
        DataFrame with growth analysis data

    Raises:
        FileNotFoundError: If file not found
        ValueError: If required columns missing or invalid data types
    """
    validate_file_exists(GROWTH_ANALYSIS_FILE)

    df = pd.read_csv(GROWTH_ANALYSIS_FILE)
    logger.info(f"Loaded growth data: {len(df)} rows")

    validate_required_columns(df, REQUIRED_GROWTH_COLS, "growth_analysis.csv")
    validate_numeric_column(df, 'Risk_Score', "growth_analysis.csv")
    validate_numeric_column(df, 'RTI_Tier', "growth_analysis.csv")
    validate_numeric_column(df, 'Growth_Rate', "growth_analysis.csv")

    return df


def load_benchmark_data() -> pd.DataFrame:
    """
    Load and validate benchmark mastery data.

    Returns:
        DataFrame with benchmark mastery data

    Raises:
        FileNotFoundError: If file not found
        ValueError: If required columns missing or invalid data types
    """
    validate_file_exists(BENCHMARK_MASTERY_FILE)

    df = pd.read_csv(BENCHMARK_MASTERY_FILE)
    logger.info(f"Loaded benchmark data: {len(df)} rows")

    validate_required_columns(df, REQUIRED_BENCHMARK_COLS, "benchmark_mastery.csv")
    validate_numeric_column(df, 'Total_Items', "benchmark_mastery.csv")
    validate_numeric_column(df, 'Mastery_Pct', "benchmark_mastery.csv")

    return df


# ============================================================================
# INSIGHT GENERATION
# ============================================================================

def generate_benchmark_priority_insights(
    benchmark_df: pd.DataFrame
) -> List[Dict[str, str]]:
    """
    Generate insights for lowest-performing benchmarks.

    Args:
        benchmark_df: DataFrame with benchmark mastery data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Sort by mastery percentage to find lowest performers
    sorted_benchmarks = benchmark_df.sort_values('Mastery_Pct')

    for idx, row in sorted_benchmarks.head(TOP_N_BENCHMARKS).iterrows():
        benchmark = row['Benchmark']
        mastery_pct = row['Mastery_Pct']
        total_items = row['Total_Items']

        # Determine priority level
        if mastery_pct < CRITICAL_MASTERY_THRESHOLD:
            priority = PRIORITY_CRITICAL
        elif mastery_pct < HIGH_MASTERY_THRESHOLD:
            priority = PRIORITY_HIGH
        else:
            priority = PRIORITY_MEDIUM

        insight = (
            f"Benchmark {benchmark} shows {mastery_pct:.1f}% mastery "
            f"across {total_items} items"
        )

        recommendation = (
            f"Prioritize small-group intervention on {benchmark}. "
            f"Focus on core skills and provide scaffolded practice."
        )

        insights.append({
            'Category': CATEGORY_BENCHMARK_PRIORITY,
            'Insight': insight,
            'Priority': priority,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} benchmark priority insights")
    return insights


def generate_at_risk_insights(growth_df: pd.DataFrame) -> List[Dict[str, str]]:
    """
    Generate insights for at-risk students.

    Args:
        growth_df: DataFrame with growth analysis data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Critical risk scores (70+)
    critical_risk = growth_df[
        growth_df['Risk_Score'] >= CRITICAL_RISK_THRESHOLD
    ].sort_values('Risk_Score', ascending=False)

    if not critical_risk.empty:
        student_names = critical_risk.head(TOP_N_STUDENTS)['Student_Name'].tolist()
        avg_risk = critical_risk['Risk_Score'].mean()

        insight = (
            f"{len(critical_risk)} students with critical risk scores "
            f"(average: {avg_risk:.1f})"
        )

        recommendation = (
            f"Immediate intervention needed for: {', '.join(student_names)}. "
            f"Provide daily targeted support and progress monitoring."
        )

        insights.append({
            'Category': CATEGORY_AT_RISK,
            'Insight': insight,
            'Priority': PRIORITY_CRITICAL,
            'Recommendation': recommendation
        })

    # Tier 3 students - CRITICAL: Use numeric comparison
    tier_3 = growth_df[growth_df['RTI_Tier'] == TIER_3_VALUE]

    if not tier_3.empty:
        student_names = tier_3.head(TOP_N_STUDENTS)['Student_Name'].tolist()

        insight = f"{len(tier_3)} students in RTI Tier 3 requiring intensive support"

        recommendation = (
            f"Coordinate intensive interventions for: {', '.join(student_names)}. "
            f"Consider individualized learning plans and additional resources."
        )

        insights.append({
            'Category': CATEGORY_AT_RISK,
            'Insight': insight,
            'Priority': PRIORITY_CRITICAL,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} at-risk insights")
    return insights


def generate_growth_trend_insights(
    growth_df: pd.DataFrame
) -> List[Dict[str, str]]:
    """
    Generate insights for growth trends.

    Args:
        growth_df: DataFrame with growth analysis data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Rapid decline (<-10)
    rapid_decline = growth_df[
        growth_df['Growth_Rate'] < RAPID_DECLINE_THRESHOLD
    ].sort_values('Growth_Rate')

    if not rapid_decline.empty:
        student_names = rapid_decline.head(TOP_N_STUDENTS)['Student_Name'].tolist()
        avg_decline = rapid_decline['Growth_Rate'].mean()

        insight = (
            f"{len(rapid_decline)} students showing rapid decline "
            f"(average: {avg_decline:.1f} points)"
        )

        recommendation = (
            f"Investigate causes of decline for: {', '.join(student_names)}. "
            f"Review attendance, engagement, and prerequisite skills."
        )

        insights.append({
            'Category': CATEGORY_GROWTH_TRENDS,
            'Insight': insight,
            'Priority': PRIORITY_CRITICAL,
            'Recommendation': recommendation
        })

    # Rapid growth (>=10)
    rapid_growth = growth_df[
        growth_df['Growth_Rate'] >= RAPID_GROWTH_THRESHOLD
    ].sort_values('Growth_Rate', ascending=False)

    if not rapid_growth.empty:
        student_names = rapid_growth.head(TOP_N_STUDENTS)['Student_Name'].tolist()
        avg_growth = rapid_growth['Growth_Rate'].mean()

        insight = (
            f"{len(rapid_growth)} students showing rapid growth "
            f"(average: {avg_growth:.1f} points)"
        )

        recommendation = (
            f"Celebrate success with: {', '.join(student_names)}. "
            f"Document effective strategies and share with team."
        )

        insights.append({
            'Category': CATEGORY_GROWTH_TRENDS,
            'Insight': insight,
            'Priority': PRIORITY_POSITIVE,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} growth trend insights")
    return insights


def generate_achievement_gain_insights(
    growth_df: pd.DataFrame
) -> List[Dict[str, str]]:
    """
    Generate insights for students who jumped achievement levels.

    Args:
        growth_df: DataFrame with growth analysis data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Students who jumped levels
    level_jumpers = growth_df[
        growth_df['Achievement_Change'].str.contains('jumped', case=False, na=False)
    ]

    if not level_jumpers.empty:
        student_names = level_jumpers.head(TOP_N_STUDENTS)['Student_Name'].tolist()

        insight = (
            f"{len(level_jumpers)} students jumped achievement levels "
            f"between assessments"
        )

        recommendation = (
            f"Recognize achievement gains for: {', '.join(student_names)}. "
            f"Analyze instructional methods that led to success."
        )

        insights.append({
            'Category': CATEGORY_ACHIEVEMENT_GAINS,
            'Insight': insight,
            'Priority': PRIORITY_POSITIVE,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} achievement gain insights")
    return insights


def generate_eoy_projection_insights(
    growth_df: pd.DataFrame
) -> List[Dict[str, str]]:
    """
    Generate insights for EOY proficiency projections.

    Args:
        growth_df: DataFrame with growth analysis data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Students projected to reach proficiency
    proficiency_track = growth_df[
        growth_df['EOY_Projection'].str.contains('Proficient|Advanced',
                                                  case=False, na=False)
    ]

    if not proficiency_track.empty:
        student_names = proficiency_track.head(TOP_N_STUDENTS)['Student_Name'].tolist()

        insight = (
            f"{len(proficiency_track)} students projected to reach "
            f"proficiency by EOY"
        )

        recommendation = (
            f"Maintain momentum for: {', '.join(student_names)}. "
            f"Provide enrichment opportunities and sustained support."
        )

        insights.append({
            'Category': CATEGORY_EOY_PROJECTION,
            'Insight': insight,
            'Priority': PRIORITY_POSITIVE,
            'Recommendation': recommendation
        })

    # Students not projected to reach proficiency
    at_risk_eoy = growth_df[
        growth_df['EOY_Projection'].str.contains('Below Basic|Far Below',
                                                  case=False, na=False)
    ]

    if not at_risk_eoy.empty:
        student_names = at_risk_eoy.head(TOP_N_STUDENTS)['Student_Name'].tolist()

        insight = (
            f"{len(at_risk_eoy)} students not projected to reach "
            f"proficiency by EOY"
        )

        recommendation = (
            f"Intensify interventions for: {', '.join(student_names)}. "
            f"Adjust instructional strategies and increase support frequency."
        )

        insights.append({
            'Category': CATEGORY_EOY_PROJECTION,
            'Insight': insight,
            'Priority': PRIORITY_HIGH,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} EOY projection insights")
    return insights


def generate_strength_area_insights(
    benchmark_df: pd.DataFrame
) -> List[Dict[str, str]]:
    """
    Generate insights for highest-performing benchmarks.

    Args:
        benchmark_df: DataFrame with benchmark mastery data

    Returns:
        List of insight dictionaries
    """
    insights = []

    # Find strength areas (>70% mastery)
    strengths = benchmark_df[
        benchmark_df['Mastery_Pct'] >= STRENGTH_MASTERY_THRESHOLD
    ].sort_values('Mastery_Pct', ascending=False)

    for idx, row in strengths.head(TOP_N_BENCHMARKS).iterrows():
        benchmark = row['Benchmark']
        mastery_pct = row['Mastery_Pct']

        insight = (
            f"Benchmark {benchmark} shows strong mastery at {mastery_pct:.1f}%"
        )

        recommendation = (
            f"Leverage successful strategies from {benchmark} instruction. "
            f"Use as model for improving weaker benchmark areas."
        )

        insights.append({
            'Category': CATEGORY_STRENGTH_AREA,
            'Insight': insight,
            'Priority': PRIORITY_POSITIVE,
            'Recommendation': recommendation
        })

    logger.info(f"Generated {len(insights)} strength area insights")
    return insights


# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def generate_all_insights(
    growth_df: pd.DataFrame,
    benchmark_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate all categories of actionable insights.

    Args:
        growth_df: DataFrame with growth analysis data
        benchmark_df: DataFrame with benchmark mastery data

    Returns:
        DataFrame with all insights
    """
    all_insights = []

    # Generate each category of insights
    all_insights.extend(generate_benchmark_priority_insights(benchmark_df))
    all_insights.extend(generate_at_risk_insights(growth_df))
    all_insights.extend(generate_growth_trend_insights(growth_df))
    all_insights.extend(generate_achievement_gain_insights(growth_df))
    all_insights.extend(generate_eoy_projection_insights(growth_df))
    all_insights.extend(generate_strength_area_insights(benchmark_df))

    insights_df = pd.DataFrame(all_insights)
    logger.info(f"Generated {len(insights_df)} total insights across all categories")

    return insights_df


def save_insights(insights_df: pd.DataFrame) -> None:
    """
    Save actionable insights to CSV file.

    Args:
        insights_df: DataFrame with insights to save

    Raises:
        IOError: If file cannot be written
    """
    try:
        INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)
        insights_df.to_csv(OUTPUT_FILE, index=False)
        logger.info(f"Saved {len(insights_df)} insights to {OUTPUT_FILE}")
    except Exception as e:
        raise IOError(f"Failed to save insights to {OUTPUT_FILE}: {e}")


def main() -> None:
    """
    Main execution function for PM Intervention Planner.

    Loads growth and benchmark data, generates actionable insights,
    and saves results to CSV.
    """
    try:
        logger.info("Starting PM Intervention Planner")

        # Load data
        growth_df = load_growth_data()
        benchmark_df = load_benchmark_data()

        # Generate insights
        insights_df = generate_all_insights(growth_df, benchmark_df)

        # Save results
        save_insights(insights_df)

        logger.info("PM Intervention Planner completed successfully")
        logger.info(f"Output file: {OUTPUT_FILE}")

        # Summary statistics
        priority_counts = insights_df['Priority'].value_counts()
        logger.info("Insights by priority:")
        for priority, count in priority_counts.items():
            logger.info(f"  {priority}: {count}")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logger.error(f"Data validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
```

## Usage Examples

### Basic Usage

```bash
# Run the intervention planner
python -c "
from pathlib import Path
exec(Path('.claude/skills/intervention-planner.md').read_text().split('```python')[1].split('```')[0])
"
```

### As Part of Workflow

```bash
# After running growth analyzer and benchmark mastery analyzer
python pm_growth_analyzer.py
python pm_benchmark_mastery_analyzer.py
python pm_intervention_planner.py  # This skill

# Check output
cat _intermediate/actionable_insights.csv
```

### Programmatic Usage

```python
from pathlib import Path
import pandas as pd

# Load and execute skill
skill_code = Path('.claude/skills/intervention-planner.md').read_text()
exec(skill_code.split('```python')[1].split('```')[0])

# Read results
insights = pd.read_csv('_intermediate/actionable_insights.csv')

# Filter by priority
critical = insights[insights['Priority'] == 'Critical']
print(f"Critical insights: {len(critical)}")
```

## Quality Standards Applied

### 1. Constants Extraction with Type Hints
- All thresholds defined as typed constants
- File paths defined as Path objects
- Category and priority names centralized

### 2. Comprehensive Type Annotations
- All function signatures fully typed
- Return types specified
- Type hints for complex structures (List[Dict[str, str]])

### 3. Robust Input Validation
- File existence checks
- Required column validation
- Data type validation for numeric columns
- CRITICAL: RTI_Tier validated as numeric

### 4. Specific Error Handling
- FileNotFoundError for missing files
- ValueError for validation failures
- IOError for write failures
- Informative error messages

### 5. Google-Style Docstrings
- Module-level documentation
- Function-level Args/Returns/Raises
- Clear purpose statements

### 6. Edge Case Handling
- Empty DataFrames handled with `if not df.empty`
- NaN values handled in string operations with `na=False`
- Division by zero prevented with safe aggregations

### 7. Logging Instead of Print
- Structured logging with timestamps
- Appropriate log levels (INFO, ERROR)
- Progress tracking throughout execution

### 8. Path Safety with Pathlib
- All paths use Path objects
- Directory creation with exist_ok=True
- Platform-independent path handling

### 9. No Magic Numbers
- All thresholds defined as named constants
- Configurable values at top of file
- Clear semantic meaning

### 10. Modular Design
- Separate validation functions
- One insight category per function
- Clear separation of concerns
- Reusable components

## CRITICAL RTI_Tier Correction

**IMPORTANT:** This skill correctly handles RTI_Tier as numeric:

```python
# CORRECT (used in this skill)
tier_3 = growth_df[growth_df['RTI_Tier'] == 3]

# WRONG (DO NOT USE)
tier_3 = growth_df[growth_df['RTI_Tier'] == 'Tier 3']
```

The RTI_Tier column is numeric (1, 2, 3), not string ("Tier 1", "Tier 2", "Tier 3").
