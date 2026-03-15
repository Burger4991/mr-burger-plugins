---
name: class-comparison-generator
description: Generate period-by-period comparison statistics from growth analysis data
---

# PM Class Comparison Skill

## Purpose

Aggregates growth_analysis data by period to create period-level statistics table showing average scores, growth rates, proficiency distributions, and intervention needs. This skill enables cross-period comparison to identify trends and target support.

## Input Requirements

**File**: `_intermediate/growth_analysis.csv`

**Required Columns**:
- `Period`: Class period identifier
- `PM1_Score`: Progress Monitoring 1 score
- `PM2_Score`: Progress Monitoring 2 score
- `Growth`: Score change (PM2 - PM1)
- `PM2_Level`: Performance level (1, 2, 3, 4)
- `Risk_Score`: Calculated risk indicator
- `RTI_Tier`: Numeric tier assignment (1, 2, 3)

**Prerequisites**: growth-analyzer skill must be completed

## Output Artifacts

**File**: `_intermediate/period_comparison.csv`

**Output Columns**:
- `Period`: Class period
- `Total_Students`: Total count of students in period
- `Students_With_Both_PM`: Count with both PM1 and PM2 scores
- `Avg_PM2_Score`: Mean PM2 score for period
- `Avg_Growth`: Mean growth value
- `Improvers`: Count with positive growth
- `Maintainers`: Count with zero growth
- `Decliners`: Count with negative growth
- `Proficient_Pct`: Percentage at Level 3 or 4
- `Approaching_Pct`: Percentage at Level 2
- `Below_Pct`: Percentage at Level 1
- `Avg_Risk_Score`: Mean risk score
- `Tier3_Count`: Count of students in RTI Tier 3

## Implementation

```python
#!/usr/bin/env python3
"""
PM Class Comparison Skill

Generates period-by-period comparison statistics from growth analysis data.
"""

import logging
from pathlib import Path
from typing import Final

import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
INPUT_FILE: Final[str] = "_intermediate/growth_analysis.csv"
OUTPUT_FILE: Final[str] = "_intermediate/period_comparison.csv"

# Column names - Input
COL_PERIOD: Final[str] = "Period"
COL_PM1_SCORE: Final[str] = "PM1_Score"
COL_PM2_SCORE: Final[str] = "PM2_Score"
COL_GROWTH: Final[str] = "Growth"
COL_PM2_LEVEL: Final[str] = "PM2_Level"
COL_RISK_SCORE: Final[str] = "Risk_Score"
COL_RTI_TIER: Final[str] = "RTI_Tier"

# Column names - Output
COL_OUT_TOTAL: Final[str] = "Total_Students"
COL_OUT_BOTH_PM: Final[str] = "Students_With_Both_PM"
COL_OUT_AVG_PM2: Final[str] = "Avg_PM2_Score"
COL_OUT_AVG_GROWTH: Final[str] = "Avg_Growth"
COL_OUT_IMPROVERS: Final[str] = "Improvers"
COL_OUT_MAINTAINERS: Final[str] = "Maintainers"
COL_OUT_DECLINERS: Final[str] = "Decliners"
COL_OUT_PROFICIENT_PCT: Final[str] = "Proficient_Pct"
COL_OUT_APPROACHING_PCT: Final[str] = "Approaching_Pct"
COL_OUT_BELOW_PCT: Final[str] = "Below_Pct"
COL_OUT_AVG_RISK: Final[str] = "Avg_Risk_Score"
COL_OUT_TIER3_COUNT: Final[str] = "Tier3_Count"

# Performance level thresholds
LEVEL_PROFICIENT_MIN: Final[int] = 3
LEVEL_APPROACHING: Final[int] = 2
LEVEL_BELOW: Final[int] = 1

# Growth categories
GROWTH_POSITIVE: Final[float] = 0.0
GROWTH_ZERO: Final[float] = 0.0

# RTI tier values
RTI_TIER_3: Final[int] = 3

# Percentage conversion
PERCENT_MULTIPLIER: Final[float] = 100.0

# Required columns
REQUIRED_COLUMNS: Final[list[str]] = [
    COL_PERIOD,
    COL_PM1_SCORE,
    COL_PM2_SCORE,
    COL_GROWTH,
    COL_PM2_LEVEL,
    COL_RISK_SCORE,
    COL_RTI_TIER
]


def validate_input_file(file_path: Path) -> None:
    """
    Validate that the input file exists.

    Args:
        file_path: Path to the input file

    Raises:
        FileNotFoundError: If the input file does not exist
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {file_path}\n"
            f"Please run growth-analyzer skill first."
        )


def validate_columns(df: pd.DataFrame) -> None:
    """
    Validate that all required columns are present.

    Args:
        df: DataFrame to validate

    Raises:
        ValueError: If required columns are missing
    """
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Missing required columns: {missing_cols}\n"
            f"Required columns: {REQUIRED_COLUMNS}"
        )


def validate_data_not_empty(df: pd.DataFrame) -> None:
    """
    Validate that the DataFrame contains data.

    Args:
        df: DataFrame to validate

    Raises:
        ValueError: If DataFrame is empty
    """
    if df.empty:
        raise ValueError("Input file contains no data")


def load_growth_data(file_path: Path) -> pd.DataFrame:
    """
    Load and validate growth analysis data.

    Args:
        file_path: Path to growth_analysis.csv

    Returns:
        DataFrame with growth analysis data

    Raises:
        FileNotFoundError: If file does not exist
        ValueError: If required columns missing or data empty
    """
    validate_input_file(file_path)

    logger.info(f"Loading growth analysis data from {file_path}")
    df = pd.read_csv(file_path)

    validate_columns(df)
    validate_data_not_empty(df)

    logger.info(f"Loaded {len(df)} student records")
    return df


def count_students_with_both_scores(period_data: pd.DataFrame) -> int:
    """
    Count students with both PM1 and PM2 scores (non-NaN).

    Args:
        period_data: DataFrame for a single period

    Returns:
        Count of students with both scores
    """
    has_pm1 = period_data[COL_PM1_SCORE].notna()
    has_pm2 = period_data[COL_PM2_SCORE].notna()
    return (has_pm1 & has_pm2).sum()


def count_by_growth_category(period_data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Count students by growth category.

    Args:
        period_data: DataFrame for a single period

    Returns:
        Tuple of (improvers, maintainers, decliners)
    """
    growth_values = period_data[COL_GROWTH].dropna()

    improvers = (growth_values > GROWTH_POSITIVE).sum()
    maintainers = (growth_values == GROWTH_ZERO).sum()
    decliners = (growth_values < GROWTH_POSITIVE).sum()

    return int(improvers), int(maintainers), int(decliners)


def calculate_proficiency_percentages(period_data: pd.DataFrame) -> tuple[float, float, float]:
    """
    Calculate percentage of students at each proficiency level.

    Args:
        period_data: DataFrame for a single period

    Returns:
        Tuple of (proficient_pct, approaching_pct, below_pct)
    """
    levels = period_data[COL_PM2_LEVEL].dropna()

    if len(levels) == 0:
        return 0.0, 0.0, 0.0

    total = len(levels)
    proficient_count = (levels >= LEVEL_PROFICIENT_MIN).sum()
    approaching_count = (levels == LEVEL_APPROACHING).sum()
    below_count = (levels == LEVEL_BELOW).sum()

    proficient_pct = (proficient_count / total) * PERCENT_MULTIPLIER
    approaching_pct = (approaching_count / total) * PERCENT_MULTIPLIER
    below_pct = (below_count / total) * PERCENT_MULTIPLIER

    return proficient_pct, approaching_pct, below_pct


def count_tier3_students(period_data: pd.DataFrame) -> int:
    """
    Count students assigned to RTI Tier 3.

    Args:
        period_data: DataFrame for a single period

    Returns:
        Count of Tier 3 students
    """
    return int((period_data[COL_RTI_TIER] == RTI_TIER_3).sum())


def calculate_period_statistics(period: str, period_data: pd.DataFrame) -> dict:
    """
    Calculate all statistics for a single period.

    Args:
        period: Period identifier
        period_data: DataFrame containing data for this period

    Returns:
        Dictionary of period statistics
    """
    total_students = len(period_data)
    students_with_both = count_students_with_both_scores(period_data)

    # Calculate averages (handle NaN gracefully)
    avg_pm2 = period_data[COL_PM2_SCORE].mean()
    avg_growth = period_data[COL_GROWTH].mean()
    avg_risk = period_data[COL_RISK_SCORE].mean()

    # Replace NaN with 0 for display
    avg_pm2 = 0.0 if pd.isna(avg_pm2) else avg_pm2
    avg_growth = 0.0 if pd.isna(avg_growth) else avg_growth
    avg_risk = 0.0 if pd.isna(avg_risk) else avg_risk

    # Count by growth category
    improvers, maintainers, decliners = count_by_growth_category(period_data)

    # Calculate proficiency percentages
    proficient_pct, approaching_pct, below_pct = calculate_proficiency_percentages(period_data)

    # Count Tier 3 students
    tier3_count = count_tier3_students(period_data)

    return {
        COL_PERIOD: period,
        COL_OUT_TOTAL: total_students,
        COL_OUT_BOTH_PM: students_with_both,
        COL_OUT_AVG_PM2: round(avg_pm2, 2),
        COL_OUT_AVG_GROWTH: round(avg_growth, 2),
        COL_OUT_IMPROVERS: improvers,
        COL_OUT_MAINTAINERS: maintainers,
        COL_OUT_DECLINERS: decliners,
        COL_OUT_PROFICIENT_PCT: round(proficient_pct, 1),
        COL_OUT_APPROACHING_PCT: round(approaching_pct, 1),
        COL_OUT_BELOW_PCT: round(below_pct, 1),
        COL_OUT_AVG_RISK: round(avg_risk, 2),
        COL_OUT_TIER3_COUNT: tier3_count
    }


def generate_period_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate period-by-period comparison statistics.

    Args:
        df: Growth analysis DataFrame

    Returns:
        DataFrame with period-level statistics
    """
    logger.info("Calculating period-level statistics")

    # Get sorted list of periods
    periods = sorted(df[COL_PERIOD].unique())
    logger.info(f"Found {len(periods)} periods: {periods}")

    # Calculate statistics for each period
    period_stats = []
    for period in periods:
        period_data = df[df[COL_PERIOD] == period]
        stats = calculate_period_statistics(period, period_data)
        period_stats.append(stats)

        logger.info(
            f"Period {period}: {stats[COL_OUT_TOTAL]} students, "
            f"{stats[COL_OUT_AVG_PM2]:.1f} avg PM2, "
            f"{stats[COL_OUT_AVG_GROWTH]:+.1f} avg growth"
        )

    return pd.DataFrame(period_stats)


def save_comparison_data(df: pd.DataFrame, file_path: Path) -> None:
    """
    Save period comparison data to CSV.

    Args:
        df: Period comparison DataFrame
        file_path: Output file path
    """
    # Ensure output directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Saving period comparison to {file_path}")
    df.to_csv(file_path, index=False)
    logger.info(f"Saved {len(df)} period records")


def main() -> None:
    """
    Main execution function for PM class comparison.
    """
    try:
        # Set up paths
        input_path = Path(INPUT_FILE)
        output_path = Path(OUTPUT_FILE)

        # Load data
        growth_df = load_growth_data(input_path)

        # Generate period comparison
        comparison_df = generate_period_comparison(growth_df)

        # Save results
        save_comparison_data(comparison_df, output_path)

        logger.info("Period comparison completed successfully")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logger.error(f"Validation error: {e}")
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
# From project root directory
python -c "from pathlib import Path; exec(open(Path.home() / '.claude/skills/class-comparison-generator.md').read().split('```python')[1].split('```')[0])"
```

### Expected Output

```
2026-01-20 10:30:00 - INFO - Loading growth analysis data from _intermediate/growth_analysis.csv
2026-01-20 10:30:00 - INFO - Loaded 150 student records
2026-01-20 10:30:00 - INFO - Calculating period-level statistics
2026-01-20 10:30:00 - INFO - Found 6 periods: [1, 2, 3, 4, 5, 6]
2026-01-20 10:30:00 - INFO - Period 1: 25 students, 82.5 avg PM2, +3.2 avg growth
2026-01-20 10:30:00 - INFO - Period 2: 25 students, 78.0 avg PM2, +2.8 avg growth
2026-01-20 10:30:00 - INFO - Period 3: 25 students, 85.3 avg PM2, +4.1 avg growth
2026-01-20 10:30:00 - INFO - Period 4: 25 students, 76.2 avg PM2, +1.9 avg growth
2026-01-20 10:30:00 - INFO - Period 5: 25 students, 81.7 avg PM2, +3.5 avg growth
2026-01-20 10:30:00 - INFO - Period 6: 25 students, 79.8 avg PM2, +2.7 avg growth
2026-01-20 10:30:00 - INFO - Saving period comparison to _intermediate/period_comparison.csv
2026-01-20 10:30:00 - INFO - Saved 6 period records
2026-01-20 10:30:00 - INFO - Period comparison completed successfully
```

## Quality Standards Applied

### 1. Constants Extraction
- All column names extracted as typed constants
- Threshold values (levels, growth categories) as named constants
- File paths as constants
- No magic numbers in logic

### 2. Type Hints
- All function parameters and return types annotated
- Complex types properly specified (tuple, dict, etc.)
- Final type hints for constants

### 3. Input Validation
- File existence check with clear error message
- Column presence validation
- Empty data check
- Prerequisite skill mentioned in error

### 4. Error Handling
- Specific exception types (FileNotFoundError, ValueError)
- Informative error messages with actionable guidance
- Graceful NaN handling in calculations

### 5. Comprehensive Docstrings
- Google-style docstrings on all functions
- Args, Returns, Raises sections
- Clear description of purpose

### 6. Edge Case Handling
- NaN values in scores replaced with 0
- Empty period data handled in percentage calculations
- Division by zero protection

### 7. Logging
- Structured logging with timestamps and levels
- Progress messages for each period
- Summary statistics logged
- No print statements

### 8. Path Safety
- pathlib.Path for cross-platform compatibility
- Parent directory creation with exist_ok=True
- Relative paths from project root

### 9. No Magic Numbers
- All thresholds extracted and named
- Percentage multiplier constant
- Level thresholds clearly defined

### 10. Modular Design
- Single-responsibility functions
- Small, testable units
- Clear separation of concerns
- Reusable calculation functions

### Critical Corrections Applied
- RTI_Tier comparison uses numeric `3` not string `"Tier 3"`
- Proper handling of numeric tier values throughout
