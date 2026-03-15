---
name: data-quality-checker
description: Validate student assessment data completeness and flag quality issues. Works with FAST PM, NWEA, or any multi-period assessment data. Use before running growth analysis or building reports.
---

# Data Quality Checker

## Purpose

Runs comprehensive data quality checks on student assessment data including completion rates, score validity, extreme changes, duplicates, and benchmark coverage. Generates a structured quality report with actionable findings.

## Configuration

This skill was originally built for FAST PM data. To use with other assessments, adjust these parameters in the implementation:

| Parameter | PM Default | What to Change |
|-----------|-----------|----------------|
| Score range | 100-300 | Update `VALID_SCORE_MIN`/`MAX` for your scale |
| Growth threshold | ±20 | Update `EXTREME_GROWTH_THRESHOLD` |
| Column names | PM1_Score, PM2_Score | Map to your assessment column names |
| Benchmark file | benchmark_data_reshaped.csv | Point to your benchmark data file |

## Input Requirements

**Files:**
- Cleaned assessment data CSV (default: `_intermediate/cleaned_pm_data.csv`)
- Benchmark data for coverage validation (optional)

**Prerequisites:**
- student-data-processor skill must be complete
- Input files must exist in expected locations

## Output Artifacts

**File:** `_intermediate/quality_report.csv`

**Columns (5 total):**
1. `Check` - Name of quality check performed
2. `Status` - ✅ Pass or ⚠️ Warning
3. `Finding` - Summary of what was found
4. `Details` - Specific details (e.g., student names, counts)
5. `Action` - Recommended next step

## Implementation

```python
#!/usr/bin/env python3
"""PM Data Quality Checker.

Validates data completeness and flags quality issues in PM data.
"""

import logging
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
SCORE_MIN: int = 100
SCORE_MAX: int = 300
EXTREME_GROWTH_THRESHOLD: int = 20
EXTREME_DECLINE_THRESHOLD: int = -20
MAX_DETAILS_STUDENTS: int = 5

STATUS_PASS: str = "✅ Pass"
STATUS_WARNING: str = "⚠️ Warning"

# File paths
INPUT_PM_DATA: Path = Path("_intermediate/cleaned_pm_data.csv")
INPUT_BENCHMARK_DATA: Path = Path("benchmark_data_reshaped.csv")
OUTPUT_QUALITY_REPORT: Path = Path("_intermediate/quality_report.csv")


class QualityCheckResult:
    """Represents a single quality check result."""

    def __init__(
        self,
        check: str,
        status: str,
        finding: str,
        details: str,
        action: str
    ):
        """Initialize quality check result.

        Args:
            check: Name of the quality check
            status: Pass or Warning status
            finding: Summary of what was found
            details: Specific details
            action: Recommended next step
        """
        self.check = check
        self.status = status
        self.finding = finding
        self.details = details
        self.action = action

    def to_dict(self) -> Dict[str, str]:
        """Convert result to dictionary.

        Returns:
            Dictionary representation of the result
        """
        return {
            'Check': self.check,
            'Status': self.status,
            'Finding': self.finding,
            'Details': self.details,
            'Action': self.action
        }


def validate_input_files() -> Tuple[bool, str]:
    """Validate that required input files exist.

    Returns:
        Tuple of (success, error_message)
    """
    if not INPUT_PM_DATA.exists():
        return False, f"Required file not found: {INPUT_PM_DATA}"

    if not INPUT_PM_DATA.stat().st_size > 0:
        return False, f"Input file is empty: {INPUT_PM_DATA}"

    return True, ""


def load_pm_data() -> Optional[pd.DataFrame]:
    """Load and validate PM data.

    Returns:
        DataFrame with PM data or None if loading fails
    """
    try:
        df = pd.read_csv(INPUT_PM_DATA)

        required_columns = ['Student_ID', 'Student_Name', 'PM1', 'PM2', 'Growth']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            return None

        logger.info(f"Loaded {len(df)} records from {INPUT_PM_DATA}")
        return df

    except Exception as e:
        logger.error(f"Failed to load PM data: {e}")
        return None


def load_benchmark_data() -> Optional[pd.DataFrame]:
    """Load benchmark data if available.

    Returns:
        DataFrame with benchmark data or None if not available
    """
    if not INPUT_BENCHMARK_DATA.exists():
        logger.warning(f"Benchmark data not found: {INPUT_BENCHMARK_DATA}")
        return None

    try:
        df = pd.read_csv(INPUT_BENCHMARK_DATA)
        logger.info(f"Loaded {len(df)} records from {INPUT_BENCHMARK_DATA}")
        return df

    except Exception as e:
        logger.warning(f"Could not load benchmark data: {e}")
        return None


def check_pm2_completion(df: pd.DataFrame) -> QualityCheckResult:
    """Check for missing PM2 scores.

    Args:
        df: PM data DataFrame

    Returns:
        QualityCheckResult with findings
    """
    missing_pm2 = df[df['PM2'].isna()]
    count = len(missing_pm2)

    if count == 0:
        return QualityCheckResult(
            check="PM2 Completion",
            status=STATUS_PASS,
            finding="All students have PM2 scores",
            details=f"0 missing out of {len(df)} students",
            action="No action needed"
        )

    # Get top students for details
    student_names = missing_pm2['Student_Name'].head(MAX_DETAILS_STUDENTS).tolist()
    details_text = f"{count} students missing PM2: {', '.join(student_names)}"
    if count > MAX_DETAILS_STUDENTS:
        details_text += f" (and {count - MAX_DETAILS_STUDENTS} more)"

    return QualityCheckResult(
        check="PM2 Completion",
        status=STATUS_WARNING,
        finding=f"{count} students missing PM2 scores ({count/len(df)*100:.1f}%)",
        details=details_text,
        action="Follow up with missing students to complete PM2"
    )


def check_score_validity(df: pd.DataFrame) -> QualityCheckResult:
    """Check for scores outside valid range.

    Args:
        df: PM data DataFrame

    Returns:
        QualityCheckResult with findings
    """
    # Check PM1 scores
    invalid_pm1 = df[
        df['PM1'].notna() &
        ((df['PM1'] < SCORE_MIN) | (df['PM1'] > SCORE_MAX))
    ]

    # Check PM2 scores
    invalid_pm2 = df[
        df['PM2'].notna() &
        ((df['PM2'] < SCORE_MIN) | (df['PM2'] > SCORE_MAX))
    ]

    total_invalid = len(invalid_pm1) + len(invalid_pm2)

    if total_invalid == 0:
        return QualityCheckResult(
            check="Score Validity",
            status=STATUS_PASS,
            finding=f"All scores within valid range ({SCORE_MIN}-{SCORE_MAX})",
            details=f"Checked {len(df)*2} total scores (PM1 and PM2)",
            action="No action needed"
        )

    # Build details
    details_parts = []
    if len(invalid_pm1) > 0:
        pm1_names = invalid_pm1['Student_Name'].head(MAX_DETAILS_STUDENTS).tolist()
        details_parts.append(f"PM1: {', '.join(pm1_names)}")
    if len(invalid_pm2) > 0:
        pm2_names = invalid_pm2['Student_Name'].head(MAX_DETAILS_STUDENTS).tolist()
        details_parts.append(f"PM2: {', '.join(pm2_names)}")

    details_text = " | ".join(details_parts)
    if total_invalid > MAX_DETAILS_STUDENTS:
        details_text += f" (showing {MAX_DETAILS_STUDENTS} of {total_invalid})"

    return QualityCheckResult(
        check="Score Validity",
        status=STATUS_WARNING,
        finding=f"{total_invalid} scores outside valid range ({SCORE_MIN}-{SCORE_MAX})",
        details=details_text,
        action=f"Review and correct scores outside {SCORE_MIN}-{SCORE_MAX} range"
    )


def check_extreme_changes(df: pd.DataFrame) -> QualityCheckResult:
    """Check for extreme score changes.

    Args:
        df: PM data DataFrame

    Returns:
        QualityCheckResult with findings
    """
    # Filter for students with both PM1 and PM2
    complete = df[df['PM1'].notna() & df['PM2'].notna()].copy()

    if len(complete) == 0:
        return QualityCheckResult(
            check="Extreme Score Changes",
            status=STATUS_PASS,
            finding="No complete PM pairs to analyze",
            details="Cannot check growth without both PM1 and PM2",
            action="Wait for PM2 completion"
        )

    # Check for extreme changes
    extreme = complete[
        (complete['Growth'] > EXTREME_GROWTH_THRESHOLD) |
        (complete['Growth'] < EXTREME_DECLINE_THRESHOLD)
    ]

    count = len(extreme)

    if count == 0:
        return QualityCheckResult(
            check="Extreme Score Changes",
            status=STATUS_PASS,
            finding="No extreme score changes detected",
            details=f"All growth between {EXTREME_DECLINE_THRESHOLD} and {EXTREME_GROWTH_THRESHOLD}",
            action="No action needed"
        )

    # Get top students with growth values
    extreme_sorted = extreme.nlargest(MAX_DETAILS_STUDENTS, 'Growth', keep='all')
    student_details = [
        f"{row['Student_Name']} ({row['Growth']:+.0f})"
        for _, row in extreme_sorted.iterrows()
    ][:MAX_DETAILS_STUDENTS]

    details_text = f"{count} students with extreme changes: {', '.join(student_details)}"
    if count > MAX_DETAILS_STUDENTS:
        details_text += f" (and {count - MAX_DETAILS_STUDENTS} more)"

    return QualityCheckResult(
        check="Extreme Score Changes",
        status=STATUS_WARNING,
        finding=f"{count} students with growth > {EXTREME_GROWTH_THRESHOLD} or < {EXTREME_DECLINE_THRESHOLD}",
        details=details_text,
        action="Review extreme changes for data entry errors or exceptional cases"
    )


def check_duplicate_records(df: pd.DataFrame) -> QualityCheckResult:
    """Check for duplicate Student_ID values.

    Args:
        df: PM data DataFrame

    Returns:
        QualityCheckResult with findings
    """
    duplicates = df[df.duplicated(subset=['Student_ID'], keep=False)]
    duplicate_ids = duplicates['Student_ID'].unique()
    count = len(duplicate_ids)

    if count == 0:
        return QualityCheckResult(
            check="Duplicate Records",
            status=STATUS_PASS,
            finding="No duplicate Student_IDs found",
            details=f"All {len(df)} records have unique Student_IDs",
            action="No action needed"
        )

    # Get details for top duplicates
    duplicate_details = []
    for student_id in list(duplicate_ids)[:MAX_DETAILS_STUDENTS]:
        student_records = duplicates[duplicates['Student_ID'] == student_id]
        student_name = student_records['Student_Name'].iloc[0]
        duplicate_details.append(f"{student_name} (ID: {student_id}, {len(student_records)} copies)")

    details_text = f"{count} duplicate IDs: {'; '.join(duplicate_details)}"
    if count > MAX_DETAILS_STUDENTS:
        details_text += f" (and {count - MAX_DETAILS_STUDENTS} more)"

    return QualityCheckResult(
        check="Duplicate Records",
        status=STATUS_WARNING,
        finding=f"{count} Student_IDs appear multiple times",
        details=details_text,
        action="Remove duplicate records, keeping most recent/complete entry"
    )


def check_benchmark_coverage(
    pm_df: pd.DataFrame,
    benchmark_df: Optional[pd.DataFrame]
) -> QualityCheckResult:
    """Check for students missing benchmark data.

    Args:
        pm_df: PM data DataFrame
        benchmark_df: Benchmark data DataFrame or None

    Returns:
        QualityCheckResult with findings
    """
    if benchmark_df is None:
        return QualityCheckResult(
            check="Benchmark Coverage",
            status=STATUS_PASS,
            finding="Benchmark data not available",
            details="Skipping benchmark coverage check",
            action="Optional: Provide benchmark_data_reshaped.csv for coverage analysis"
        )

    # Get Student_IDs from both datasets
    pm_students = set(pm_df['Student_ID'].dropna())
    benchmark_students = set(benchmark_df['Student_ID'].dropna())

    missing_benchmark = pm_students - benchmark_students
    count = len(missing_benchmark)

    if count == 0:
        return QualityCheckResult(
            check="Benchmark Coverage",
            status=STATUS_PASS,
            finding="All PM students have benchmark data",
            details=f"{len(pm_students)} students matched in both datasets",
            action="No action needed"
        )

    # Get student names
    missing_students = pm_df[pm_df['Student_ID'].isin(missing_benchmark)]
    student_names = missing_students['Student_Name'].head(MAX_DETAILS_STUDENTS).tolist()

    details_text = f"{count} students in PM data but missing from benchmarks: {', '.join(student_names)}"
    if count > MAX_DETAILS_STUDENTS:
        details_text += f" (and {count - MAX_DETAILS_STUDENTS} more)"

    return QualityCheckResult(
        check="Benchmark Coverage",
        status=STATUS_WARNING,
        finding=f"{count} students missing benchmark data ({count/len(pm_students)*100:.1f}%)",
        details=details_text,
        action="Add benchmark data for missing students or verify Student_IDs match"
    )


def run_quality_checks(
    pm_df: pd.DataFrame,
    benchmark_df: Optional[pd.DataFrame]
) -> List[QualityCheckResult]:
    """Run all quality checks.

    Args:
        pm_df: PM data DataFrame
        benchmark_df: Benchmark data DataFrame or None

    Returns:
        List of QualityCheckResult objects
    """
    logger.info("Running quality checks...")

    results = [
        check_pm2_completion(pm_df),
        check_score_validity(pm_df),
        check_extreme_changes(pm_df),
        check_duplicate_records(pm_df),
        check_benchmark_coverage(pm_df, benchmark_df)
    ]

    # Count warnings
    warnings = sum(1 for r in results if r.status == STATUS_WARNING)
    logger.info(f"Quality checks complete: {len(results)} checks, {warnings} warnings")

    return results


def save_quality_report(results: List[QualityCheckResult]) -> bool:
    """Save quality check results to CSV.

    Args:
        results: List of QualityCheckResult objects

    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure output directory exists
        OUTPUT_QUALITY_REPORT.parent.mkdir(parents=True, exist_ok=True)

        # Convert results to DataFrame
        results_dicts = [r.to_dict() for r in results]
        df = pd.DataFrame(results_dicts)

        # Save to CSV
        df.to_csv(OUTPUT_QUALITY_REPORT, index=False)
        logger.info(f"Quality report saved to {OUTPUT_QUALITY_REPORT}")

        return True

    except Exception as e:
        logger.error(f"Failed to save quality report: {e}")
        return False


def print_quality_summary(results: List[QualityCheckResult]) -> None:
    """Print summary of quality check results.

    Args:
        results: List of QualityCheckResult objects
    """
    logger.info("\n" + "="*80)
    logger.info("QUALITY CHECK SUMMARY")
    logger.info("="*80)

    for result in results:
        logger.info(f"\n{result.status} {result.check}")
        logger.info(f"  Finding: {result.finding}")
        if result.status == STATUS_WARNING:
            logger.info(f"  Details: {result.details}")
            logger.info(f"  Action: {result.action}")

    warnings = sum(1 for r in results if r.status == STATUS_WARNING)
    logger.info("\n" + "="*80)
    logger.info(f"Total Checks: {len(results)} | Warnings: {warnings}")
    logger.info("="*80 + "\n")


def main() -> int:
    """Main execution function.

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    logger.info("Starting PM Data Quality Checker")

    # Validate input files
    valid, error = validate_input_files()
    if not valid:
        logger.error(error)
        return 1

    # Load PM data
    pm_df = load_pm_data()
    if pm_df is None:
        return 1

    # Load benchmark data (optional)
    benchmark_df = load_benchmark_data()

    # Run quality checks
    results = run_quality_checks(pm_df, benchmark_df)

    # Save quality report
    if not save_quality_report(results):
        return 1

    # Print summary
    print_quality_summary(results)

    logger.info("PM Data Quality Checker complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Usage Examples

### Basic Usage

```bash
# Run quality checker after processing student data
python data-quality-checker.py
```

### Expected Output

```
2026-01-20 10:30:00 - INFO - Starting PM Data Quality Checker
2026-01-20 10:30:00 - INFO - Loaded 45 records from _intermediate/cleaned_pm_data.csv
2026-01-20 10:30:00 - INFO - Loaded 43 records from benchmark_data_reshaped.csv
2026-01-20 10:30:00 - INFO - Running quality checks...
2026-01-20 10:30:00 - INFO - Quality checks complete: 5 checks, 2 warnings

================================================================================
QUALITY CHECK SUMMARY
================================================================================

✅ Pass PM2 Completion
  Finding: All students have PM2 scores

⚠️ Warning Score Validity
  Finding: 2 scores outside valid range (100-300)
  Details: PM1: Student A (95), Student B (305)
  Action: Review and correct scores outside 100-300 range

✅ Pass Extreme Score Changes
  Finding: No extreme score changes detected

✅ Pass Duplicate Records
  Finding: No duplicate Student_IDs found

⚠️ Warning Benchmark Coverage
  Finding: 2 students missing benchmark data (4.4%)
  Details: 2 students in PM data but missing from benchmarks: Student C, Student D
  Action: Add benchmark data for missing students or verify Student_IDs match

================================================================================
Total Checks: 5 | Warnings: 2
================================================================================

2026-01-20 10:30:00 - INFO - Quality report saved to _intermediate/quality_report.csv
2026-01-20 10:30:00 - INFO - PM Data Quality Checker complete
```

### Output File Format

`_intermediate/quality_report.csv`:
```csv
Check,Status,Finding,Details,Action
PM2 Completion,✅ Pass,All students have PM2 scores,0 missing out of 45 students,No action needed
Score Validity,⚠️ Warning,2 scores outside valid range (100-300),PM1: Student A (95) | PM2: Student B (305),Review and correct scores outside 100-300 range
Extreme Score Changes,✅ Pass,No extreme score changes detected,All growth between -20 and 20,No action needed
Duplicate Records,✅ Pass,No duplicate Student_IDs found,All 45 records have unique Student_IDs,No action needed
Benchmark Coverage,⚠️ Warning,2 students missing benchmark data (4.4%),2 students in PM data but missing from benchmarks: Student C and Student D,Add benchmark data for missing students or verify Student_IDs match
```

## Quality Standards Applied

1. **Constants Extraction**: All thresholds (100, 300, 20, -20, 5) defined as typed constants
2. **Type Annotations**: Complete type hints for all functions and parameters
3. **Input Validation**: File existence, size, and column validation
4. **Error Handling**: Specific try-except blocks with informative error messages
5. **Documentation**: Google-style docstrings for all functions and classes
6. **Edge Cases**: Handles missing data, empty datasets, NaN values
7. **Logging**: Structured logging instead of print statements
8. **Path Safety**: Uses pathlib.Path for all file operations
9. **No Magic Numbers**: All numeric thresholds defined as named constants
10. **Modular Design**: Separate function for each check type with QualityCheckResult class

## Integration with Workflow

This skill is part of the PM data analysis pipeline:

1. **student-data-processor** → Cleans and prepares PM data
2. **data-quality-checker** → Validates data quality (this skill)
3. Next steps depend on quality report findings

Use the quality report to identify and resolve data issues before proceeding with analysis.
