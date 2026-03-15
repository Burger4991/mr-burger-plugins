---
name: student-data-processor
description: Load and standardize PM1-PM2 merged data for analysis
---

## Purpose
Loads PM1_PM2_Merged_Data.xlsx (created by GSD Phase 1), standardizes column names to simplified format, and returns clean DataFrame ready for analysis.

## Usage
Call this skill when you need to load PM data for any analysis task.

## Parameters
- **file_path**: Path to PM1_PM2_Merged_Data.xlsx (default: current directory)

## Output
Returns pandas DataFrame with standardized columns:
- Student_ID
- Student_Name
- Period
- PM1_Score, PM2_Score
- PM1_Level, PM2_Level
- Growth (PM2 - PM1)
- Growth_Category (Significant Gain, Moderate Gain, Minimal Change, Decline)
- Risk_Score (0-100 scale)
- RTI_Tier (1, 2, or 3)
- All demographic columns preserved

## Implementation

```python
import pandas as pd
import numpy as np
import os

# Achievement Level Thresholds
LEVEL_1_THRESHOLD = 225
LEVEL_2_THRESHOLD = 247
LEVEL_3_THRESHOLD = 264

# Growth Category Thresholds
SIGNIFICANT_GAIN_THRESHOLD = 10
MODERATE_GAIN_THRESHOLD = 5
MINIMAL_CHANGE_THRESHOLD = -5

# Risk Score Weights
RISK_SCORE_MAX = 100
RISK_PM2_SCORE_WEIGHT_MAX = 40
RISK_GROWTH_WEIGHT_MAX = 30
RISK_LEVEL_REGRESSION_WEIGHT_MAX = 20
RISK_CURRENT_LEVEL_WEIGHT_MAX = 10

# PM2 Score Risk Thresholds
PM2_VERY_LOW_THRESHOLD = 225
PM2_LOW_THRESHOLD = 240
PM2_MEDIUM_LOW_THRESHOLD = 247
PM2_MEDIUM_THRESHOLD = 255

# Growth Risk Thresholds
GROWTH_SEVERE_DECLINE_THRESHOLD = -10

# RTI Tier Thresholds
RTI_TIER_3_THRESHOLD = 60
RTI_TIER_2_THRESHOLD = 30

def get_achievement_level(score: float) -> float:
    """Calculate achievement level from score.

    Args:
        score: PM test scale score

    Returns:
        Achievement level (1-4) or NaN if score is missing

    Levels:
        1: < 225 (Below Proficient)
        2: 225-246 (Approaching Proficient)
        3: 247-263 (Proficient)
        4: 264+ (Advanced)
    """
    if pd.isna(score):
        return np.nan
    elif score < LEVEL_1_THRESHOLD:
        return 1
    elif score < LEVEL_2_THRESHOLD:
        return 2
    elif score < LEVEL_3_THRESHOLD:
        return 3
    else:
        return 4

def categorize_growth(growth: float) -> str:
    """Categorize growth amount.

    Args:
        growth: Point change from PM1 to PM2

    Returns:
        Growth category string
    """
    if pd.isna(growth):
        return 'No Data'
    elif growth >= SIGNIFICANT_GAIN_THRESHOLD:
        return 'Significant Gain'
    elif growth >= MODERATE_GAIN_THRESHOLD:
        return 'Moderate Gain'
    elif growth >= MINIMAL_CHANGE_THRESHOLD:
        return 'Minimal Change'
    else:
        return 'Decline'

def calculate_risk_score(row: pd.Series) -> int:
    """Calculate student risk score (0-100 scale).

    Args:
        row: DataFrame row with PM scores, growth, and levels

    Returns:
        Risk score from 0-100 (higher = more at-risk)

    Scoring factors:
        - PM2 score (max 40 points)
        - Growth (max 30 points)
        - Level regression (max 20 points)
        - Current level (max 10 points)
    """
    score = 0

    # PM2 score factor (max 40 points)
    if pd.notna(row['PM2_Score']):
        if row['PM2_Score'] < PM2_VERY_LOW_THRESHOLD:
            score += 40
        elif row['PM2_Score'] < PM2_LOW_THRESHOLD:
            score += 30
        elif row['PM2_Score'] < PM2_MEDIUM_LOW_THRESHOLD:
            score += 20
        elif row['PM2_Score'] < PM2_MEDIUM_THRESHOLD:
            score += 10

    # Growth factor (max 30 points)
    if pd.notna(row['Growth']):
        if row['Growth'] < GROWTH_SEVERE_DECLINE_THRESHOLD:
            score += 30
        elif row['Growth'] < 0:
            score += 20
        elif row['Growth'] < MODERATE_GAIN_THRESHOLD:
            score += 10

    # Level regression (max 20 points)
    if pd.notna(row['PM1_Level']) and pd.notna(row['PM2_Level']):
        if row['PM2_Level'] < row['PM1_Level']:
            score += 20

    # Current level factor (max 10 points)
    if pd.notna(row['PM2_Level']):
        if row['PM2_Level'] == 1:
            score += 10
        elif row['PM2_Level'] == 2:
            score += 5

    return min(score, RISK_SCORE_MAX)

def assign_rti_tier(risk_score: float, pm2_score: float) -> float:
    """Assign RTI tier based on risk score.

    Args:
        risk_score: Calculated risk score (0-100)
        pm2_score: PM2 scale score (used for additional context)

    Returns:
        RTI tier (1, 2, or 3) or NaN if no data

    Tiers:
        3: risk_score >= 60 (Intensive intervention)
        2: risk_score >= 30 (Targeted intervention)
        1: risk_score < 30 (Universal/core instruction)
    """
    if pd.isna(risk_score):
        return np.nan
    elif risk_score >= RTI_TIER_3_THRESHOLD:
        return 3
    elif risk_score >= RTI_TIER_2_THRESHOLD:
        return 2
    else:
        return 1

def load_pm_data(file_path: str = 'PM1_PM2_Merged_Data.xlsx') -> pd.DataFrame:
    """Load and standardize PM1-PM2 merged data for analysis.

    Args:
        file_path: Path to PM1_PM2_Merged_Data.xlsx file

    Returns:
        DataFrame with standardized columns:
            - Student_ID, Student_Name, Period
            - PM1_Score, PM2_Score
            - PM1_Level, PM2_Level
            - Growth, Growth_Category
            - Risk_Score, RTI_Tier
            - All demographic columns preserved

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If required columns are missing

    Example:
        >>> data = load_pm_data('PM1_PM2_Merged_Data.xlsx')
        >>> print(f"Loaded {len(data)} students")
        >>> print(data['RTI_Tier'].value_counts())
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PM data file not found: {file_path}")

    # Load the merged data
    df = pd.read_excel(file_path)

    # Define required columns (at least one variant must exist)
    required_score_cols = [
        'Grade 10 FAST ELA Reading Scale Score_PM1',
        'Grade 10 FAST ELA Reading Scale Score_PM2'
    ]

    # Check for required columns
    missing = [col for col in required_score_cols if col not in df.columns]
    if len(missing) == len(required_score_cols):
        raise ValueError(
            f"Missing required score columns. Need at least one of: {required_score_cols}"
        )

    # Standardize column names
    column_mapping = {
        'Student Name_PM1': 'Student_Name',
        'Student Name_PM2': 'Student_Name',
        'Grade 10 FAST ELA Reading Scale Score_PM1': 'PM1_Score',
        'Grade 10 FAST ELA Reading Scale Score_PM2': 'PM2_Score',
        'Period_PM1': 'Period',
        'Period_PM2': 'Period'
    }

    # Apply mappings
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns and new_col not in df.columns:
            df[new_col] = df[old_col]

    # Handle Student_Name (prefer PM1, fallback to PM2, fill NaN values)
    if 'Student_Name' not in df.columns:
        if 'Student Name_PM1' in df.columns:
            df['Student_Name'] = df['Student Name_PM1']
        elif 'Student Name_PM2' in df.columns:
            df['Student_Name'] = df['Student Name_PM2']
        else:
            raise ValueError("No student name column found (need 'Student Name_PM1' or 'Student Name_PM2')")

    # Fill any remaining NaN values in Student_Name
    if 'Student Name_PM2' in df.columns:
        df['Student_Name'] = df['Student_Name'].fillna(df['Student Name_PM2'])
    if 'Student Name_PM1' in df.columns:
        df['Student_Name'] = df['Student_Name'].fillna(df['Student Name_PM1'])

    # Convert scores to numeric
    df['PM1_Score'] = pd.to_numeric(df.get('PM1_Score'), errors='coerce')
    df['PM2_Score'] = pd.to_numeric(df.get('PM2_Score'), errors='coerce')

    # Calculate achievement levels
    df['PM1_Level'] = df['PM1_Score'].apply(get_achievement_level)
    df['PM2_Level'] = df['PM2_Score'].apply(get_achievement_level)

    # Calculate growth
    df['Growth'] = df['PM2_Score'] - df['PM1_Score']

    # Categorize growth
    df['Growth_Category'] = df['Growth'].apply(categorize_growth)

    # Calculate risk score
    df['Risk_Score'] = df.apply(calculate_risk_score, axis=1)

    # Assign RTI tier
    df['RTI_Tier'] = df.apply(
        lambda row: assign_rti_tier(row['Risk_Score'], row['PM2_Score']),
        axis=1
    )

    return df
```

## Example

```python
# Load PM data
data = load_pm_data('PM1_PM2_Merged_Data.xlsx')

# View summary
print(f"Loaded {len(data)} student records")
print(f"Periods: {data['Period'].unique()}")
print(f"RTI Tier distribution:\n{data['RTI_Tier'].value_counts()}")
```
