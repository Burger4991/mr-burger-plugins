---
name: benchmark-mastery-analyzer
description: Calculate student strengths/weaknesses and benchmark mastery matrix
tags:
  - ir-data-pipeline
---

## Purpose

Analyzes benchmark-level performance from reshaped item data, calculates top 3 strengths and weaknesses per student using 80% mastery threshold, creates benchmark mastery matrix for heatmap visualization.

## Input Requirements

**Files:**
- `benchmark_data_reshaped.csv` (from GSD Phase 4-01)
- `_intermediate/cleaned_pm_data.csv` (optional, for validation)

**Required columns in benchmark_data_reshaped.csv:**
- student_id, student_name, period, benchmark, points_earned, points_possible

**Prerequisites:** GSD Phase 4-01 complete, student-data-processor complete

## Output Artifacts

**File 1:** `_intermediate/benchmark_mastery.csv`
- Rows: student_id, student_name, period, benchmark, mastery_pct, mastered (boolean)
- One row per student-benchmark combination

**File 2:** `_intermediate/student_strengths_weaknesses.csv`
- Columns: Student_Name, Top_Strength_1, Top_Strength_2, Top_Strength_3, Top_Weakness_1, Top_Weakness_2, Top_Weakness_3
- Each strength/weakness formatted as "Benchmark (XX%)"

## Implementation

```python
"""PM Benchmark Mastery Analyzer

Analyzes benchmark-level performance, calculates student strengths/weaknesses,
and creates benchmark mastery matrix for data conference reports.
"""

import pandas as pd
import numpy as np
import os
import logging
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path

# Initialize logger
logger = logging.getLogger(__name__)


# ============================================================================
# CONSTANTS - Mastery Thresholds
# ============================================================================
MASTERY_THRESHOLD_PCT: float = 80.0  # Percentage threshold for benchmark mastery
MIN_POINTS_POSSIBLE: float = 1.0  # Minimum points possible to calculate mastery
PERCENTAGE_MULTIPLIER: float = 100.0  # Multiplier to convert decimal to percentage


# ============================================================================
# CONSTANTS - Output Format
# ============================================================================
NUM_STRENGTHS: int = 3  # Number of top strengths to identify
NUM_WEAKNESSES: int = 3  # Number of bottom weaknesses to identify
DEFAULT_DECIMAL_PLACES: int = 0  # Default decimal places for percentage formatting
MISSING_VALUE_PLACEHOLDER: str = "N/A"  # Placeholder for missing strength/weakness data


# ============================================================================
# CONSTANTS - Column Names
# ============================================================================
# Input columns
COL_STUDENT_ID: str = 'student_id'
COL_STUDENT_NAME: str = 'student_name'
COL_PERIOD: str = 'period'
COL_BENCHMARK: str = 'benchmark'
COL_POINTS_EARNED: str = 'points_earned'
COL_POINTS_POSSIBLE: str = 'points_possible'

# Output columns - Mastery
COL_MASTERY_PCT: str = 'mastery_pct'
COL_MASTERED: str = 'mastered'

# Output columns - Strengths/Weaknesses
COL_STUDENT_NAME_OUTPUT: str = 'Student_Name'
COL_TOP_STRENGTH_1: str = 'Top_Strength_1'
COL_TOP_STRENGTH_2: str = 'Top_Strength_2'
COL_TOP_STRENGTH_3: str = 'Top_Strength_3'
COL_TOP_WEAKNESS_1: str = 'Top_Weakness_1'
COL_TOP_WEAKNESS_2: str = 'Top_Weakness_2'
COL_TOP_WEAKNESS_3: str = 'Top_Weakness_3'


# ============================================================================
# CONSTANTS - File Paths
# ============================================================================
DEFAULT_BENCHMARK_FILE: str = 'benchmark_data_reshaped.csv'
DEFAULT_OUTPUT_DIR: str = '_intermediate'
OUTPUT_MASTERY_FILE: str = 'benchmark_mastery.csv'
OUTPUT_STRENGTHS_WEAKNESSES_FILE: str = 'student_strengths_weaknesses.csv'


# ============================================================================
# CONSTANTS - Validation
# ============================================================================
REQUIRED_INPUT_COLUMNS: List[str] = [
    COL_STUDENT_NAME,
    COL_BENCHMARK,
    COL_POINTS_EARNED,
    COL_POINTS_POSSIBLE
]

MASTERY_OUTPUT_COLUMNS: List[str] = [
    COL_STUDENT_ID,
    COL_STUDENT_NAME,
    COL_PERIOD,
    COL_BENCHMARK,
    COL_MASTERY_PCT,
    COL_MASTERED
]


# ============================================================================
# Core Calculation Functions
# ============================================================================

def calculate_benchmark_mastery(
    points_earned: float,
    points_possible: float,
    min_points: float = MIN_POINTS_POSSIBLE
) -> float:
    """Calculate mastery percentage for a benchmark.

    Args:
        points_earned: Points earned on benchmark items
        points_possible: Total points possible for benchmark
        min_points: Minimum points possible to calculate mastery

    Returns:
        Mastery percentage (0-100) or NaN if invalid

    Raises:
        TypeError: If inputs are not numeric
        ValueError: If points_earned > points_possible
    """
    # Type validation
    if not isinstance(points_earned, (int, float, np.number)) and not pd.isna(points_earned):
        raise TypeError(f"points_earned must be numeric, got {type(points_earned)}")
    if not isinstance(points_possible, (int, float, np.number)) and not pd.isna(points_possible):
        raise TypeError(f"points_possible must be numeric, got {type(points_possible)}")

    # Handle missing values
    if pd.isna(points_earned) or pd.isna(points_possible):
        return np.nan

    # Validate minimum threshold
    if points_possible < min_points:
        return np.nan

    # Validate logical consistency
    if points_earned > points_possible:
        raise ValueError(
            f"points_earned ({points_earned}) cannot exceed points_possible ({points_possible})"
        )

    # Calculate mastery percentage
    mastery_pct = (points_earned / points_possible) * PERCENTAGE_MULTIPLIER

    return mastery_pct


def is_mastered(
    mastery_pct: float,
    threshold: float = MASTERY_THRESHOLD_PCT
) -> bool:
    """Determine if a benchmark is mastered based on threshold.

    Args:
        mastery_pct: Mastery percentage (0-100)
        threshold: Minimum percentage for mastery

    Returns:
        True if mastered, False otherwise (including NaN)
    """
    if pd.isna(mastery_pct):
        return False

    return mastery_pct >= threshold


def format_benchmark_label(
    benchmark_name: str,
    mastery_pct: float,
    decimal_places: int = DEFAULT_DECIMAL_PLACES
) -> str:
    """Format benchmark with mastery percentage for display.

    Args:
        benchmark_name: Name of the benchmark
        mastery_pct: Mastery percentage (0-100)
        decimal_places: Number of decimal places for percentage

    Returns:
        Formatted string like "ELA.10.R.1.1 (85%)"
    """
    if pd.isna(mastery_pct):
        return f"{benchmark_name} (N/A)"

    return f"{benchmark_name} ({mastery_pct:.{decimal_places}f}%)"


# ============================================================================
# Analysis Functions
# ============================================================================

def identify_strengths_weaknesses(
    benchmark_scores: Dict[str, float],
    num_strengths: int = NUM_STRENGTHS,
    num_weaknesses: int = NUM_WEAKNESSES
) -> Tuple[List[str], List[str]]:
    """Identify top strengths and bottom weaknesses from benchmark scores.

    Args:
        benchmark_scores: Dictionary mapping benchmark names to mastery percentages
        num_strengths: Number of top strengths to identify
        num_weaknesses: Number of bottom weaknesses to identify

    Returns:
        Tuple of (strengths_list, weaknesses_list) with formatted strings

    Raises:
        ValueError: If num_strengths or num_weaknesses is negative
        TypeError: If benchmark_scores is not a dictionary
    """
    # Input validation
    if not isinstance(benchmark_scores, dict):
        raise TypeError(f"benchmark_scores must be dict, got {type(benchmark_scores)}")

    if num_strengths < 0:
        raise ValueError(f"num_strengths must be non-negative, got {num_strengths}")

    if num_weaknesses < 0:
        raise ValueError(f"num_weaknesses must be non-negative, got {num_weaknesses}")

    # Handle empty scores
    if not benchmark_scores:
        return [], []

    # Filter out NaN values
    valid_scores = {
        benchmark: pct
        for benchmark, pct in benchmark_scores.items()
        if pd.notna(pct)
    }

    if not valid_scores:
        return [], []

    # Sort benchmarks by mastery percentage (highest first)
    sorted_benchmarks = sorted(
        valid_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Extract top N strengths
    strengths = [
        format_benchmark_label(benchmark, pct)
        for benchmark, pct in sorted_benchmarks[:num_strengths]
    ]

    # Extract bottom N weaknesses (reversed so worst is first)
    weaknesses = [
        format_benchmark_label(benchmark, pct)
        for benchmark, pct in sorted_benchmarks[-num_weaknesses:]
    ]
    weaknesses.reverse()

    return strengths, weaknesses


def aggregate_benchmark_scores(
    student_data: pd.DataFrame,
    benchmark_col: str = COL_BENCHMARK,
    earned_col: str = COL_POINTS_EARNED,
    possible_col: str = COL_POINTS_POSSIBLE
) -> Dict[str, float]:
    """Aggregate mastery scores across multiple items per benchmark.

    Args:
        student_data: DataFrame with student's benchmark items
        benchmark_col: Column name for benchmark identifier
        earned_col: Column name for points earned
        possible_col: Column name for points possible

    Returns:
        Dictionary mapping benchmark names to average mastery percentages

    Raises:
        ValueError: If required columns are missing
    """
    # Validate columns exist
    required = [benchmark_col, earned_col, possible_col]
    missing = [col for col in required if col not in student_data.columns]
    if missing:
        raise ValueError(f"Missing required columns in student_data: {missing}")

    # Aggregate mastery by benchmark
    benchmark_mastery: Dict[str, List[float]] = {}

    for _, row in student_data.iterrows():
        benchmark = row[benchmark_col]

        # Skip if benchmark is missing
        if pd.isna(benchmark):
            continue

        # Calculate mastery for this item
        mastery_pct = calculate_benchmark_mastery(
            row[earned_col],
            row[possible_col]
        )

        # Store valid mastery scores
        if pd.notna(mastery_pct):
            if benchmark in benchmark_mastery:
                benchmark_mastery[benchmark].append(mastery_pct)
            else:
                benchmark_mastery[benchmark] = [mastery_pct]

    # Average mastery per benchmark (some benchmarks may have multiple items)
    avg_mastery = {
        benchmark: np.mean(scores)
        for benchmark, scores in benchmark_mastery.items()
    }

    return avg_mastery


def analyze_student_benchmarks(
    benchmark_data: pd.DataFrame,
    student_name: str,
    num_strengths: int = NUM_STRENGTHS,
    num_weaknesses: int = NUM_WEAKNESSES
) -> Dict[str, Any]:
    """Analyze benchmark mastery for a single student.

    Args:
        benchmark_data: Full benchmark dataset
        student_name: Name of student to analyze
        num_strengths: Number of top strengths to identify
        num_weaknesses: Number of bottom weaknesses to identify

    Returns:
        Dictionary with student analysis results including:
        - Student_Name
        - Top_Strength_1/2/3
        - Top_Weakness_1/2/3

    Raises:
        ValueError: If student_name is not found in data
    """
    # Filter to student's data
    student_data = benchmark_data[benchmark_data[COL_STUDENT_NAME] == student_name]

    if student_data.empty:
        raise ValueError(f"Student '{student_name}' not found in benchmark data")

    # Aggregate mastery scores by benchmark
    avg_mastery = aggregate_benchmark_scores(student_data)

    # Identify strengths and weaknesses
    strengths, weaknesses = identify_strengths_weaknesses(
        avg_mastery,
        num_strengths=num_strengths,
        num_weaknesses=num_weaknesses
    )

    # Pad strengths/weaknesses to ensure consistent output
    while len(strengths) < num_strengths:
        strengths.append(MISSING_VALUE_PLACEHOLDER)

    while len(weaknesses) < num_weaknesses:
        weaknesses.append(MISSING_VALUE_PLACEHOLDER)

    return {
        COL_STUDENT_NAME_OUTPUT: student_name,
        COL_TOP_STRENGTH_1: strengths[0],
        COL_TOP_STRENGTH_2: strengths[1],
        COL_TOP_STRENGTH_3: strengths[2],
        COL_TOP_WEAKNESS_1: weaknesses[0],
        COL_TOP_WEAKNESS_2: weaknesses[1],
        COL_TOP_WEAKNESS_3: weaknesses[2],
    }


# ============================================================================
# Mastery Matrix Creation
# ============================================================================

def create_benchmark_mastery_matrix(
    benchmark_data: pd.DataFrame,
    output_file: Optional[str] = None,
    mastery_threshold: float = MASTERY_THRESHOLD_PCT
) -> pd.DataFrame:
    """Create benchmark mastery matrix with one row per student-benchmark.

    Args:
        benchmark_data: Reshaped benchmark data
        output_file: Optional path to save output CSV
        mastery_threshold: Percentage threshold for mastery

    Returns:
        DataFrame with columns: student_id, student_name, period, benchmark,
        mastery_pct, mastered

    Raises:
        ValueError: If required columns are missing
    """
    # Validate required columns
    required = [COL_STUDENT_ID, COL_STUDENT_NAME, COL_PERIOD, COL_BENCHMARK,
                COL_POINTS_EARNED, COL_POINTS_POSSIBLE]
    missing = [col for col in required if col not in benchmark_data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Group by student-benchmark and aggregate
    mastery_rows = []

    group_cols = [COL_STUDENT_ID, COL_STUDENT_NAME, COL_PERIOD, COL_BENCHMARK]

    for group_keys, group_data in benchmark_data.groupby(group_cols):
        student_id, student_name, period, benchmark = group_keys

        # Calculate total points across all items for this benchmark
        total_earned = group_data[COL_POINTS_EARNED].sum()
        total_possible = group_data[COL_POINTS_POSSIBLE].sum()

        # Calculate mastery percentage
        mastery_pct = calculate_benchmark_mastery(total_earned, total_possible)
        mastered = is_mastered(mastery_pct, mastery_threshold)

        mastery_rows.append({
            COL_STUDENT_ID: student_id,
            COL_STUDENT_NAME: student_name,
            COL_PERIOD: period,
            COL_BENCHMARK: benchmark,
            COL_MASTERY_PCT: mastery_pct,
            COL_MASTERED: mastered
        })

    # Create DataFrame
    mastery_df = pd.DataFrame(mastery_rows, columns=MASTERY_OUTPUT_COLUMNS)

    # Save if output file specified
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        mastery_df.to_csv(output_file, index=False)

    return mastery_df


# ============================================================================
# Main Analysis Pipeline
# ============================================================================

def calculate_strengths_weaknesses(
    benchmark_file: str = DEFAULT_BENCHMARK_FILE,
    output_file: Optional[str] = None,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    mastery_threshold: float = MASTERY_THRESHOLD_PCT,
    num_strengths: int = NUM_STRENGTHS,
    num_weaknesses: int = NUM_WEAKNESSES
) -> pd.DataFrame:
    """Calculate student strengths and weaknesses from benchmark data.

    Args:
        benchmark_file: Path to reshaped benchmark data CSV
        output_file: Path for output strengths/weaknesses CSV (if None, uses default)
        output_dir: Directory for output files
        mastery_threshold: Percentage threshold for mastery
        num_strengths: Number of top strengths to identify
        num_weaknesses: Number of bottom weaknesses to identify

    Returns:
        DataFrame with student strengths and weaknesses

    Raises:
        FileNotFoundError: If benchmark file doesn't exist
        ValueError: If required columns are missing
    """
    # Validate input file exists
    benchmark_path = Path(benchmark_file)
    if not benchmark_path.exists():
        raise FileNotFoundError(
            f"Benchmark file not found: {benchmark_file}\n"
            f"Expected at: {benchmark_path.absolute()}"
        )

    # Load benchmark data
    try:
        benchmark_data = pd.read_csv(benchmark_file)
    except Exception as e:
        raise ValueError(f"Failed to read benchmark file: {e}")

    # Validate required columns
    missing = [col for col in REQUIRED_INPUT_COLUMNS if col not in benchmark_data.columns]
    if missing:
        raise ValueError(
            f"Missing required columns: {missing}\n"
            f"Available columns: {list(benchmark_data.columns)}"
        )

    # Create output directory
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    # Determine output file path
    if output_file is None:
        output_file = str(output_dir_path / OUTPUT_STRENGTHS_WEAKNESSES_FILE)

    # Analyze each student
    results = []
    student_names = benchmark_data[COL_STUDENT_NAME].unique()

    for student_name in student_names:
        if pd.notna(student_name):
            try:
                student_analysis = analyze_student_benchmarks(
                    benchmark_data,
                    student_name,
                    num_strengths=num_strengths,
                    num_weaknesses=num_weaknesses
                )
                results.append(student_analysis)
            except ValueError as e:
                logger.warning(f"Failed to analyze student '{student_name}': {e}")
                continue
            except Exception as e:
                logger.error(f"Unexpected error analyzing student '{student_name}': {e}")
                raise  # Don't silently swallow unexpected errors

    # Create output DataFrame
    if not results:
        raise ValueError("No student analyses succeeded")

    strengths_weaknesses_df = pd.DataFrame(results)

    # Write output
    strengths_weaknesses_df.to_csv(output_file, index=False)
    logger.info(f"Wrote strengths/weaknesses for {len(strengths_weaknesses_df)} students to: {output_file}")

    return strengths_weaknesses_df


def analyze_benchmark_mastery(
    benchmark_file: str = DEFAULT_BENCHMARK_FILE,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    mastery_threshold: float = MASTERY_THRESHOLD_PCT,
    num_strengths: int = NUM_STRENGTHS,
    num_weaknesses: int = NUM_WEAKNESSES
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Complete benchmark mastery analysis pipeline.

    Generates both the benchmark mastery matrix and student strengths/weaknesses.

    Args:
        benchmark_file: Path to reshaped benchmark data CSV
        output_dir: Directory for output files
        mastery_threshold: Percentage threshold for mastery
        num_strengths: Number of top strengths to identify
        num_weaknesses: Number of bottom weaknesses to identify

    Returns:
        Tuple of (mastery_matrix_df, strengths_weaknesses_df)

    Raises:
        FileNotFoundError: If benchmark file doesn't exist
        ValueError: If required columns are missing or analysis fails
    """
    # Validate input file
    benchmark_path = Path(benchmark_file)
    if not benchmark_path.exists():
        raise FileNotFoundError(f"Benchmark file not found: {benchmark_file}")

    # Load data
    benchmark_data = pd.read_csv(benchmark_file)

    # Create output directory
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    # Generate mastery matrix
    mastery_file = str(output_dir_path / OUTPUT_MASTERY_FILE)
    mastery_df = create_benchmark_mastery_matrix(
        benchmark_data,
        output_file=mastery_file,
        mastery_threshold=mastery_threshold
    )
    logger.info(f"Created mastery matrix with {len(mastery_df)} rows: {mastery_file}")

    # Generate strengths/weaknesses
    sw_file = str(output_dir_path / OUTPUT_STRENGTHS_WEAKNESSES_FILE)
    sw_df = calculate_strengths_weaknesses(
        benchmark_file=benchmark_file,
        output_file=sw_file,
        output_dir=output_dir,
        mastery_threshold=mastery_threshold,
        num_strengths=num_strengths,
        num_weaknesses=num_weaknesses
    )

    return mastery_df, sw_df
```

## Usage Examples

### Basic Analysis

```python
# Run complete benchmark mastery analysis
mastery_df, sw_df = analyze_benchmark_mastery(
    benchmark_file='benchmark_data_reshaped.csv',
    output_dir='_intermediate'
)

# View summary statistics
print(f"Analyzed {len(sw_df)} students")
print(f"Students with 3 strengths: {(sw_df['Top_Strength_3'] != '').sum()}")
print(f"Students with 3 weaknesses: {(sw_df['Top_Weakness_3'] != '').sum()}")
```

### Custom Mastery Threshold

```python
# Use 75% mastery threshold instead of 80%
mastery_df, sw_df = analyze_benchmark_mastery(
    benchmark_file='benchmark_data_reshaped.csv',
    mastery_threshold=75.0
)
```

### Top Performers Analysis

```python
# Calculate strengths/weaknesses
sw_df = calculate_strengths_weaknesses(
    benchmark_file='benchmark_data_reshaped.csv',
    output_file='_intermediate/student_strengths_weaknesses.csv'
)

# View students with strong performance
print("\nStudents with all 3 strengths identified:")
strong_students = sw_df[sw_df['Top_Strength_3'] != ''][
    ['Student_Name', 'Top_Strength_1', 'Top_Strength_2', 'Top_Strength_3']
]
print(strong_students.head())
```

### Individual Student Analysis

```python
# Load benchmark data
benchmark_data = pd.read_csv('benchmark_data_reshaped.csv')

# Analyze specific student
student_analysis = analyze_student_benchmarks(
    benchmark_data,
    student_name='Smith, John'
)

# View results
print(f"Student: {student_analysis['Student_Name']}")
print(f"\nTop Strengths:")
print(f"  1. {student_analysis['Top_Strength_1']}")
print(f"  2. {student_analysis['Top_Strength_2']}")
print(f"  3. {student_analysis['Top_Strength_3']}")
print(f"\nTop Weaknesses:")
print(f"  1. {student_analysis['Top_Weakness_1']}")
print(f"  2. {student_analysis['Top_Weakness_2']}")
print(f"  3. {student_analysis['Top_Weakness_3']}")
```

## Quality Standards Applied

This implementation follows production-quality standards:

1. **Constants Extraction**: All magic numbers extracted to named constants
2. **Type Hints**: Comprehensive type annotations on all functions
3. **Input Validation**: Robust validation of all inputs with clear error messages
4. **Error Handling**: Specific error types with actionable messages
5. **Comprehensive Docstrings**: Google-style docstrings for all functions
6. **Edge Case Handling**: NaN values, empty data, missing students
7. **Consistent Output**: Standardized column names and formats
8. **Path Safety**: Uses pathlib for cross-platform compatibility
9. **Logging**: Informative print statements for pipeline progress
10. **Modular Design**: Small, testable functions with single responsibilities
