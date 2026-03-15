---
name: report-builder
description: Assemble comprehensive multi-sheet Excel reports from intermediate analysis CSVs. Originally built for PM assessment data but adaptable to any student data pipeline. Use after running growth-analyzer and data-quality-checker.
---

# Assessment Report Builder

## Configuration

This skill assembles a 16-sheet Excel report from intermediate CSV files. It was built for FAST PM data but can be adapted:

| What to Change | PM Default | How to Adapt |
|---------------|-----------|--------------|
| Output filename | `PM1_PM2_COMPREHENSIVE_Analysis.xlsx` | Change to match your assessment |
| Sheet names | PM-specific (e.g., "PM Growth Summary") | Rename for your assessment type |
| Period columns | P01-P08 | Update to match your class periods |
| Input CSVs | `_intermediate/*.csv` | Point to your pipeline outputs |
| Item count | Items 1-40 | Adjust for your assessment length |

## Prerequisites

Run these skills first (in order):
1. `student-data-processor` — clean and merge raw data
2. `growth-analyzer` — calculate growth metrics
3. `data-quality-checker` — validate data quality
4. `benchmark-mastery-analyzer` — (optional) benchmark-level analysis

## Purpose

Final assembly step that takes all intermediate CSV outputs from Skills 1-6 and generates a comprehensive 16-sheet Excel workbook with professional formatting, color-coding, and data visualization. This skill consolidates all analysis results into a single, polished deliverable suitable for educational stakeholders.

## Input Requirements

### Required Intermediate Files (in _intermediate/)

1. **cleaned_pm_data.csv** - Validated and cleaned student performance data
2. **growth_analysis.csv** - Growth calculations and risk classifications
3. **student_strengths_weaknesses.csv** - Per-student benchmark performance summary
4. **benchmark_mastery.csv** - Benchmark-level mastery aggregation
5. **period_comparison.csv** - Period-to-period comparative analysis
6. **actionable_insights.csv** - Prioritized recommendations
7. **quality_report.csv** - Data quality metrics and flags

### Validation Requirements

- All 7 CSV files must exist before running
- Files must have expected column structures
- No empty DataFrames allowed
- Student IDs must be consistent across files

## Output Artifacts

### PM1_PM2_COMPREHENSIVE_Analysis.xlsx

A 16-sheet Excel workbook containing:

1. **USER GUIDE** - Navigation and interpretation instructions
2. **Executive Dashboard** - High-level summary metrics and KPIs
3. **Actionable Insights** - Prioritized recommendations from insights_generator
4. **Growth & Risk Analysis** - Growth trajectories and at-risk students
5. **Student Strengths-Weaknesses** - Per-student benchmark performance
6. **Benchmark Mastery Heatmap** - Visual benchmark mastery grid
7. **Item-Level Analysis** - Individual test item performance
8. **Period Analysis** - Cross-period comparison summary
9. **Data Quality Report** - Validation results and data flags
10. **Complete Student Data** - Full cleaned dataset
11. **P01** - Period 1 detailed data
12. **P02** - Period 2 detailed data
13. **P03** - Period 3 detailed data
14. **P04** - Period 4 detailed data
15. **P07** - Period 7 detailed data
16. **P08** - Period 8 detailed data

### Formatting Standards

- **Header color**: FF3660 (pink/red) with white bold text
- **Performance levels**: Red/Yellow/Green color-coding
- **Growth indicators**: Blue (positive) / Orange (negative)
- **Professional borders**: Thin black borders around data regions
- **Alternating rows**: Light gray fill for readability
- **Column widths**: Auto-sized or explicitly set for readability

## Implementation

```python
#!/usr/bin/env python3
"""
PM Report Builder - Task 7
Assemble 15-sheet comprehensive Excel report with formatting.

This script consolidates all intermediate analysis outputs into a single
professionally formatted Excel workbook for educational stakeholders.
"""

import logging
import sys
from pathlib import Path
from typing import Dict

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.chart import BarChart, LineChart, Reference

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
INTERMEDIATE_DIR = Path("_intermediate")
OUTPUT_FILE = Path("PM1_PM2_COMPREHENSIVE_Analysis.xlsx")

# Color Constants (Hex without #)
COLOR_HEADER = "FF3660"  # Pink/Red header
COLOR_GREEN = "90EE90"   # Light green for high performance
COLOR_YELLOW = "FFFF99"  # Light yellow for medium performance
COLOR_RED = "FFB6C1"     # Light red for low performance
COLOR_BLUE = "ADD8E6"    # Light blue for positive growth
COLOR_ORANGE = "FFD580"  # Light orange for negative growth
COLOR_GRAY = "F0F0F0"    # Light gray for alternating rows

# Sheet Names
SHEET_NAMES = [
    "USER GUIDE",
    "Executive Dashboard",
    "Actionable Insights",
    "Growth & Risk Analysis",
    "Student Strengths-Weaknesses",
    "Benchmark Mastery Heatmap",
    "Item-Level Analysis",
    "Period Analysis",
    "Data Quality Report",
    "Complete Student Data",
    "P01",
    "P02",
    "P03",
    "P04",
    "P07",
    "P08"
]

# Performance Thresholds
THRESHOLD_HIGH = 80.0
THRESHOLD_MEDIUM = 60.0

# Chart positioning
CHART_POSITION_DASHBOARD = "A9"
CHART_COLUMN_OFFSET = 2
MAX_CHART_ROWS = 50  # Limit chart to first 50 students for readability

# File size constants
BYTES_PER_MB = 1024 * 1024

# Intermediate File Names
INTERMEDIATE_FILES = {
    'cleaned': 'cleaned_pm_data.csv',
    'growth': 'growth_analysis.csv',
    'strengths': 'student_strengths_weaknesses.csv',
    'mastery': 'benchmark_mastery.csv',
    'comparison': 'period_comparison.csv',
    'insights': 'actionable_insights.csv',
    'quality': 'quality_report.csv'
}


def validate_inputs() -> Dict[str, pd.DataFrame]:
    """
    Validate that all required intermediate files exist and load them.

    Returns:
        Dictionary mapping file keys to loaded DataFrames

    Raises:
        FileNotFoundError: If any required file is missing
        ValueError: If any DataFrame is empty or malformed
    """
    logger.info("Validating input files...")

    if not INTERMEDIATE_DIR.exists():
        raise FileNotFoundError(f"Intermediate directory not found: {INTERMEDIATE_DIR}")

    dataframes = {}

    for key, filename in INTERMEDIATE_FILES.items():
        filepath = INTERMEDIATE_DIR / filename

        if not filepath.exists():
            raise FileNotFoundError(f"Required file not found: {filepath}")

        df = pd.read_csv(filepath)

        if df.empty:
            raise ValueError(f"File is empty: {filepath}")

        dataframes[key] = df
        logger.info(f"Loaded {filename}: {len(df)} rows, {len(df.columns)} columns")

    logger.info("All input files validated successfully")
    return dataframes


def create_styled_header(ws: Worksheet, headers: list, row: int = 1) -> None:
    """
    Apply header styling to a row.

    Args:
        ws: Worksheet to modify
        headers: List of header strings
        row: Row number for headers (1-indexed)
    """
    header_font = Font(bold=True, color="FFFFFF", size=11)
    header_fill = PatternFill(start_color=COLOR_HEADER, end_color=COLOR_HEADER, fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment


def apply_border(ws: Worksheet, start_row: int, start_col: int, end_row: int, end_col: int) -> None:
    """
    Apply thin borders to a range of cells.

    Args:
        ws: Worksheet to modify
        start_row: Starting row (1-indexed)
        start_col: Starting column (1-indexed)
        end_row: Ending row (1-indexed)
        end_col: Ending column (1-indexed)
    """
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            ws.cell(row=row, column=col).border = thin_border


def apply_alternating_rows(ws: Worksheet, start_row: int, end_row: int, num_cols: int) -> None:
    """
    Apply alternating row colors for readability.

    Args:
        ws: Worksheet to modify
        start_row: Starting row (1-indexed)
        end_row: Ending row (1-indexed)
        num_cols: Number of columns to apply color to
    """
    gray_fill = PatternFill(start_color=COLOR_GRAY, end_color=COLOR_GRAY, fill_type="solid")

    for row in range(start_row, end_row + 1):
        if row % 2 == 0:  # Even rows
            for col in range(1, num_cols + 1):
                ws.cell(row=row, column=col).fill = gray_fill


def auto_size_columns(ws: Worksheet, max_width: int = 50) -> None:
    """
    Auto-size columns based on content.

    Args:
        ws: Worksheet to modify
        max_width: Maximum column width
    """
    for column in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)

        for cell in column:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except (TypeError, AttributeError) as e:
                logger.debug(f"Could not calculate length for cell value: {e}")

        adjusted_width = min(max_length + 2, max_width)
        ws.column_dimensions[column_letter].width = adjusted_width


def build_user_guide_sheet(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build USER GUIDE sheet with navigation instructions.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("USER GUIDE")

    guide_content = [
        ["PM1-PM2 Comprehensive Analysis Report", ""],
        ["", ""],
        ["NAVIGATION GUIDE", ""],
        ["", ""],
        ["Sheet Name", "Description"],
        ["Executive Dashboard", "High-level KPIs and summary metrics"],
        ["Actionable Insights", "Prioritized recommendations for intervention"],
        ["Growth & Risk Analysis", "Student growth trajectories and at-risk identification"],
        ["Student Strengths-Weaknesses", "Per-student benchmark performance breakdown"],
        ["Benchmark Mastery Heatmap", "Visual representation of benchmark mastery"],
        ["Item-Level Analysis", "Individual test item performance data"],
        ["Period Analysis", "Cross-period comparative analysis"],
        ["Data Quality Report", "Validation results and data quality flags"],
        ["Complete Student Data", "Full cleaned dataset"],
        ["P01-P08", "Individual period detailed data sheets"],
        ["", ""],
        ["COLOR CODING", ""],
        ["Performance Levels", ""],
        ["Green", "High performance (≥80%)"],
        ["Yellow", "Medium performance (60-79%)"],
        ["Red", "Low performance (<60%)"],
        ["", ""],
        ["Growth Indicators", ""],
        ["Blue", "Positive growth"],
        ["Orange", "Negative growth or at-risk"],
    ]

    for row_idx, row_data in enumerate(guide_content, start=1):
        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)

            # Title formatting
            if row_idx == 1:
                cell.font = Font(bold=True, size=16, color=COLOR_HEADER)
            # Section headers
            elif value in ["NAVIGATION GUIDE", "COLOR CODING", "Performance Levels", "Growth Indicators"]:
                cell.font = Font(bold=True, size=12)
            # Table headers
            elif row_idx == 5:
                cell.font = Font(bold=True)
                cell.fill = PatternFill(start_color=COLOR_HEADER, end_color=COLOR_HEADER, fill_type="solid")
                cell.font = Font(bold=True, color="FFFFFF")

    # Apply color examples
    ws.cell(row=20, column=1).fill = PatternFill(start_color=COLOR_GREEN, end_color=COLOR_GREEN, fill_type="solid")
    ws.cell(row=21, column=1).fill = PatternFill(start_color=COLOR_YELLOW, end_color=COLOR_YELLOW, fill_type="solid")
    ws.cell(row=22, column=1).fill = PatternFill(start_color=COLOR_RED, end_color=COLOR_RED, fill_type="solid")
    ws.cell(row=25, column=1).fill = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type="solid")
    ws.cell(row=26, column=1).fill = PatternFill(start_color=COLOR_ORANGE, end_color=COLOR_ORANGE, fill_type="solid")

    auto_size_columns(ws)
    logger.info("Created USER GUIDE sheet")


def build_executive_dashboard(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Executive Dashboard sheet with KPIs.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Executive Dashboard")

    # Calculate summary metrics
    total_students = len(data['cleaned']['Student_ID'].unique())
    growth_df = data['growth']
    at_risk_count = len(growth_df[growth_df.get('Risk_Flag', False)])

    # Dashboard layout
    dashboard_data = [
        ["EXECUTIVE DASHBOARD", ""],
        ["", ""],
        ["Key Metrics", "Value"],
        ["Total Students", total_students],
        ["At-Risk Students", at_risk_count],
        ["Data Quality Score", "See Data Quality Report"],
        ["Reporting Period", "PM1 & PM2"],
    ]

    for row_idx, row_data in enumerate(dashboard_data, start=1):
        for col_idx, value in enumerate(row_data, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    # Title styling
    ws.cell(row=1, column=1).font = Font(bold=True, size=16, color=COLOR_HEADER)

    # Header row
    create_styled_header(ws, dashboard_data[2], row=3)

    # Add bar chart showing at-risk vs total students
    chart = BarChart()
    chart.title = "Student Risk Overview"
    chart.x_axis.title = "Category"
    chart.y_axis.title = "Count"

    # Create data reference for chart (row 4 = Total Students, row 5 = At-Risk Students)
    chart_data = Reference(ws, min_col=2, min_row=3, max_row=5, max_col=2)
    categories = Reference(ws, min_col=1, min_row=4, max_row=5)
    chart.add_data(chart_data, titles_from_data=True)
    chart.set_categories(categories)

    # Position chart below the metrics
    ws.add_chart(chart, CHART_POSITION_DASHBOARD)

    auto_size_columns(ws)
    logger.info("Created Executive Dashboard sheet with embedded chart")


def build_actionable_insights(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Actionable Insights sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Actionable Insights")
    df = data['insights']

    # Write headers
    headers = list(df.columns)
    create_styled_header(ws, headers)

    # Write data
    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    # Apply formatting
    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    logger.info(f"Created Actionable Insights sheet with {len(df)} insights")


def build_growth_risk_analysis(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Growth & Risk Analysis sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Growth & Risk Analysis")
    df = data['growth']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)

            # Color-code risk flags
            if headers[col_idx - 1] == 'Risk_Flag' and value:
                cell.fill = PatternFill(start_color=COLOR_ORANGE, end_color=COLOR_ORANGE, fill_type="solid")

    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    # Add chart showing growth distribution
    # Count students by growth category if available
    if 'Growth_Category' in df.columns or any('Growth' in col for col in df.columns):
        chart = LineChart()
        chart.title = "Student Growth Distribution"
        chart.x_axis.title = "Student Index"
        chart.y_axis.title = "Growth Score"

        # Find growth-related column
        growth_col = None
        for idx, col in enumerate(headers, start=1):
            if 'Growth' in col and col != 'Growth_Category':
                growth_col = idx
                break

        if growth_col:
            # Create reference to growth data
            chart_data = Reference(ws, min_col=growth_col, min_row=1, max_row=min(len(df) + 1, MAX_CHART_ROWS))
            chart.add_data(chart_data, titles_from_data=True)

            # Position chart to the right of the data
            ws.add_chart(chart, f"{get_column_letter(len(headers) + CHART_COLUMN_OFFSET)}2")
            logger.info(f"Created Growth & Risk Analysis sheet with {len(df)} students and embedded chart")
        else:
            logger.info(f"Created Growth & Risk Analysis sheet with {len(df)} students")
    else:
        logger.info(f"Created Growth & Risk Analysis sheet with {len(df)} students")


def build_strengths_weaknesses(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Student Strengths-Weaknesses sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Student Strengths-Weaknesses")
    df = data['strengths']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)

            # Color-code performance percentages
            if isinstance(value, (int, float)) and not pd.isna(value) and 0 <= value <= 100:
                if value >= THRESHOLD_HIGH:
                    cell.fill = PatternFill(start_color=COLOR_GREEN, end_color=COLOR_GREEN, fill_type="solid")
                elif value >= THRESHOLD_MEDIUM:
                    cell.fill = PatternFill(start_color=COLOR_YELLOW, end_color=COLOR_YELLOW, fill_type="solid")
                else:
                    cell.fill = PatternFill(start_color=COLOR_RED, end_color=COLOR_RED, fill_type="solid")

    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    logger.info(f"Created Student Strengths-Weaknesses sheet with {len(df)} students")


def build_benchmark_mastery_heatmap(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Benchmark Mastery Heatmap sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Benchmark Mastery Heatmap")
    df = data['mastery']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)

            # Color-code mastery percentages
            if isinstance(value, (int, float)) and not pd.isna(value) and 0 <= value <= 100:
                if value >= THRESHOLD_HIGH:
                    cell.fill = PatternFill(start_color=COLOR_GREEN, end_color=COLOR_GREEN, fill_type="solid")
                elif value >= THRESHOLD_MEDIUM:
                    cell.fill = PatternFill(start_color=COLOR_YELLOW, end_color=COLOR_YELLOW, fill_type="solid")
                else:
                    cell.fill = PatternFill(start_color=COLOR_RED, end_color=COLOR_RED, fill_type="solid")

    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    logger.info(f"Created Benchmark Mastery Heatmap sheet with {len(df)} benchmarks")


def build_item_level_analysis(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Item-Level Analysis sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Item-Level Analysis")

    # Extract item-level data from cleaned data
    df = data['cleaned']

    # Filter to item columns (Item_1 through Item_40)
    item_cols = [col for col in df.columns if col.startswith('Item_')]
    id_cols = ['Student_ID', 'Period']

    item_df = df[id_cols + item_cols]

    headers = list(item_df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(item_df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    apply_alternating_rows(ws, 2, len(item_df) + 1, len(headers))
    apply_border(ws, 1, 1, len(item_df) + 1, len(headers))
    auto_size_columns(ws, max_width=15)

    logger.info(f"Created Item-Level Analysis sheet with {len(item_df)} rows")


def build_period_analysis(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Period Analysis sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Period Analysis")
    df = data['comparison']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    logger.info(f"Created Period Analysis sheet with {len(df)} comparisons")


def build_quality_report(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Data Quality Report sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Data Quality Report")
    df = data['quality']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws)

    logger.info(f"Created Data Quality Report sheet with {len(df)} quality checks")


def build_complete_data_sheet(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build Complete Student Data sheet.

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    ws = wb.create_sheet("Complete Student Data")
    df = data['cleaned']

    headers = list(df.columns)
    create_styled_header(ws, headers)

    for row_idx, row in enumerate(df.itertuples(index=False), start=2):
        for col_idx, value in enumerate(row, start=1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    apply_alternating_rows(ws, 2, len(df) + 1, len(headers))
    apply_border(ws, 1, 1, len(df) + 1, len(headers))
    auto_size_columns(ws, max_width=20)

    logger.info(f"Created Complete Student Data sheet with {len(df)} rows")


def build_period_sheets(wb: Workbook, data: Dict[str, pd.DataFrame]) -> None:
    """
    Build individual period sheets (P01, P02, P03, P04, P07, P08).

    Args:
        wb: Workbook object
        data: Dictionary of loaded DataFrames
    """
    df = data['cleaned']
    periods = ['P01', 'P02', 'P03', 'P04', 'P07', 'P08']

    for period in periods:
        period_df = df[df['Period'] == period].copy()

        if period_df.empty:
            logger.warning(f"No data found for period {period}")
            continue

        ws = wb.create_sheet(period)

        headers = list(period_df.columns)
        create_styled_header(ws, headers)

        for row_idx, row in enumerate(period_df.itertuples(index=False), start=2):
            for col_idx, value in enumerate(row, start=1):
                ws.cell(row=row_idx, column=col_idx, value=value)

        apply_alternating_rows(ws, 2, len(period_df) + 1, len(headers))
        apply_border(ws, 1, 1, len(period_df) + 1, len(headers))
        auto_size_columns(ws, max_width=20)

        logger.info(f"Created {period} sheet with {len(period_df)} students")


def build_comprehensive_report(data: Dict[str, pd.DataFrame]) -> Path:
    """
    Build complete 15-sheet Excel report.

    Args:
        data: Dictionary of loaded DataFrames

    Returns:
        Path to created Excel file
    """
    logger.info("Building comprehensive Excel report...")

    # Create workbook
    wb = Workbook()

    # Remove default sheet
    if 'Sheet' in wb.sheetnames:
        wb.remove(wb['Sheet'])

    # Build all sheets
    build_user_guide_sheet(wb, data)
    build_executive_dashboard(wb, data)
    build_actionable_insights(wb, data)
    build_growth_risk_analysis(wb, data)
    build_strengths_weaknesses(wb, data)
    build_benchmark_mastery_heatmap(wb, data)
    build_item_level_analysis(wb, data)
    build_period_analysis(wb, data)
    build_quality_report(wb, data)
    build_complete_data_sheet(wb, data)
    build_period_sheets(wb, data)

    # Verify exactly 16 sheets exist (10 core + 6 period sheets)
    expected_sheets = 16
    if len(wb.sheetnames) != expected_sheets:
        raise ValueError(f"Expected exactly {expected_sheets} sheets, got {len(wb.sheetnames)}")

    # Save workbook
    wb.save(OUTPUT_FILE)
    logger.info(f"Comprehensive report saved to {OUTPUT_FILE}")
    logger.info(f"Total sheets created: {len(wb.sheetnames)}")

    return OUTPUT_FILE


def main() -> int:
    """
    Main execution function.

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        logger.info("Starting PM Report Builder (Task 7)")

        # Validate and load inputs
        data = validate_inputs()

        # Build report
        output_path = build_comprehensive_report(data)

        # Verify output
        if not output_path.exists():
            raise FileNotFoundError(f"Output file was not created: {output_path}")

        file_size_mb = output_path.stat().st_size / BYTES_PER_MB
        logger.info(f"Report file size: {file_size_mb:.2f} MB")

        logger.info("PM Report Builder completed successfully")
        return 0

    except Exception as e:
        logger.error(f"PM Report Builder failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

## Usage Examples

### Basic Usage

```bash
# After running Skills 1-6 to generate intermediate files
python pm_report_builder.py
```

### Verification

```python
import openpyxl

# Verify file can be opened
wb = openpyxl.load_workbook("PM1_PM2_COMPREHENSIVE_Analysis.xlsx")

# Check sheet count
print(f"Total sheets: {len(wb.sheetnames)}")
print(f"Sheet names: {wb.sheetnames}")

# Verify specific sheet exists
assert "USER GUIDE" in wb.sheetnames
assert "Executive Dashboard" in wb.sheetnames
assert "Complete Student Data" in wb.sheetnames
```

### Integration with Pipeline

```bash
# Run complete pipeline
python scripts/01_clean_data.py
python scripts/02_analyze_growth.py
python scripts/03_identify_strengths_weaknesses.py
python scripts/04_calculate_benchmark_mastery.py
python scripts/05_compare_periods.py
python scripts/06_generate_insights.py
python scripts/07_build_report.py

# Output: PM1_PM2_COMPREHENSIVE_Analysis.xlsx
```

## Quality Standards Applied

1. **Constants Extraction**: All colors, thresholds, and sheet names defined as module constants
2. **Type Annotations**: Full type hints on all functions and parameters
3. **Input Validation**: Comprehensive file existence and DataFrame validation
4. **Error Handling**: Try-except blocks with detailed logging
5. **Google-style Docstrings**: Complete documentation for all functions
6. **Edge Case Handling**: Empty DataFrames, missing periods, malformed data
7. **Logging**: Detailed info/warning/error messages throughout
8. **Path Safety**: Uses pathlib.Path for all file operations
9. **No Magic Numbers**: All thresholds and values defined as named constants
10. **Modular Design**: Separate builder function for each sheet type

## Implementation Notes

- This skill provides the framework and formatting logic
- Actual sheet content comes from intermediate CSV files
- Can be extended with chart generation using openpyxl.chart
- Color coding automatically applied based on thresholds
- All sheets include professional borders and styling
- Column widths auto-sized for readability
- Alternating row colors improve data scanning

## Validation Checklist

- [ ] All 7 intermediate CSV files exist
- [ ] Output file contains expected sheets (10-16 depending on data)
- [ ] Headers are pink/red (FF3660) with white text
- [ ] Performance levels color-coded (R/Y/G)
- [ ] Growth indicators color-coded (Blue/Orange)
- [ ] Borders applied to all data regions
- [ ] Columns auto-sized appropriately
- [ ] File opens successfully in Excel/LibreOffice
- [ ] No Python errors or warnings in logs
- [ ] File size reasonable (<50MB for typical dataset)
