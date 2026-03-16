---
name: growth-analyzer
description: >
  This skill should be used when "calculating student growth", "assigning RTI intervention tiers",
  "projecting proficiency probability", or "analyzing progress between PM1/PM2/PM3". Use when
  "identifying at-risk students", "preparing growth data for conferences", "flagging acceleration
  or regression patterns", or "building tier assignment recommendations". Supports FAST PM, NWEA,
  and custom assessments.
---

## Purpose

Calculates comprehensive growth metrics (Period 1→Period 2 delta, level changes, quartiles), assigns risk scores (0-100), determines intervention tiers (1/2/3), categorizes growth with emojis, and projects next-period proficiency probability.

## Configuration

All thresholds are defined as constants at the top of the implementation. **Adjust these for your assessment type:**

| Parameter | PM Default | NWEA Example | What It Controls |
|-----------|-----------|--------------|-----------------|
| `PROFICIENCY_THRESHOLD` | 247 | 221 (RIT) | Score considered proficient |
| `RISK_PM2_VERY_LOW` | 200 | 190 | Highest risk score threshold |
| `RISK_PM2_LOW` | 225 | 205 | Medium risk threshold |
| `RAPID_GROWTH_THRESHOLD` | 10 | 5 | Points to count as rapid growth |
| `MODERATE_GROWTH_THRESHOLD` | 5 | 3 | Points for moderate growth |

**To use with a different assessment:** Change the threshold constants and rename column references in `required_cols` to match your data (e.g., `AP1_Score`/`AP2_Score` for NWEA).

## Input Requirements

**File:** Assessment data CSV or pandas DataFrame

**Required columns** (rename to match your data):
- Student_Name, Student_ID, Period
- PM1_Score, PM2_Score, PM1_Level, PM2_Level

**Prerequisites:** Data must be cleaned and merged (see `student-data-processor` skill)

## Output Artifacts

**File:** `_intermediate/growth_analysis.csv` or enriched DataFrame

**Added columns:**
- Growth (numeric delta)
- Level_Movement (numeric level change)
- Growth_Category (emoji + text: 🚀 Rapid, 📈 Moderate, ➡️ Steady, ⏸️ Flat, 📉 Declining, ⚠️ Alert)
- Growth_Quartile (Q1/Q2/Q3/Q4)
- Projected_PM3 (linear projection)
- Risk_Score (0-100)
- RTI_Tier (1/2/3 numeric)
- Proficiency_Probability (0-100%)

## Implementation

```python
import pandas as pd
import numpy as np

# Growth Category Thresholds
RAPID_GROWTH_THRESHOLD = 10
MODERATE_GROWTH_THRESHOLD = 5
STEADY_THRESHOLD = 0
DECLINING_THRESHOLD = -5

# Risk Score Thresholds
RISK_PM2_VERY_LOW = 200
RISK_PM2_LOW = 225
RISK_PM2_MEDIUM = 247
RISK_GROWTH_SEVERE = -10
RISK_GROWTH_MODERATE = -5
RISK_GROWTH_SLIGHT = 0

# Risk Score Weights
RISK_PM2_WEIGHT_MAX = 40
RISK_GROWTH_WEIGHT_MAX = 30
RISK_REGRESSION_WEIGHT_MAX = 20

# RTI Tier Thresholds
RTI_TIER_3_THRESHOLD = 60
RTI_TIER_2_THRESHOLD = 30

# Proficiency Thresholds
PROFICIENCY_THRESHOLD = 247
PROFICIENCY_APPROACHING_THRESHOLD = 240
PROFICIENCY_DEVELOPING_THRESHOLD = 230

# Proficiency Probability Percentages
PROB_ALREADY_PROFICIENT = 95  # Student already at Level 3+
PROB_PROJECTED_PROFICIENT = 75  # Linear projection reaches 247+
PROB_APPROACHING_PROFICIENT = 50  # Projection 240-246
PROB_DEVELOPING = 25  # Projection 230-239
PROB_MINIMAL = 10  # Projection < 230
PROB_NO_GROWTH_DATA = 30  # Can't project without growth trend

def categorize_growth(growth: float) -> str:
    """Categorize growth amount with emoji indicators.

    Args:
        growth: Point change from PM1 to PM2

    Returns:
        Growth category string with emoji
    """
    if pd.isna(growth):
        return "⏸️ No Data"
    elif growth >= RAPID_GROWTH_THRESHOLD:
        return "🚀 Rapid Growth"
    elif growth >= MODERATE_GROWTH_THRESHOLD:
        return "📈 Moderate Growth"
    elif growth >= STEADY_THRESHOLD:
        return "➡️ Steady"
    elif growth >= DECLINING_THRESHOLD:
        return "📉 Declining"
    else:
        return "⚠️ Alert"

def calculate_risk_score(row: pd.Series) -> int:
    """Calculate student risk score (0-100 scale).

    Args:
        row: DataFrame row with PM scores, growth, and level movement

    Returns:
        Risk score from 0-100 (higher = more at-risk)

    Scoring factors:
        - PM2 score (max 40 points)
        - Growth (max 30 points)
        - Level regression (max 20 points)
    """
    risk = 0

    # PM2 score factor (max 40 points)
    if pd.notna(row['PM2_Score']):
        if row['PM2_Score'] < RISK_PM2_VERY_LOW:
            risk += 40
        elif row['PM2_Score'] < RISK_PM2_LOW:
            risk += 30
        elif row['PM2_Score'] < RISK_PM2_MEDIUM:
            risk += 20

    # Growth factor (max 30 points)
    if pd.notna(row['Growth']):
        if row['Growth'] < RISK_GROWTH_SEVERE:
            risk += 30
        elif row['Growth'] < RISK_GROWTH_MODERATE:
            risk += 20
        elif row['Growth'] < RISK_GROWTH_SLIGHT:
            risk += 10

    # Level regression (max 20 points)
    if pd.notna(row.get('Level_Movement')) and row['Level_Movement'] < 0:
        risk += 20

    return min(risk, 100)

def assign_rti_tier(risk_score: float, pm2_score: float) -> float:
    """Assign RTI tier based on risk score.

    Args:
        risk_score: Calculated risk score (0-100)
        pm2_score: PM2 scale score

    Returns:
        RTI tier number (1, 2, or 3) or NaN if no data

    Tiers:
        3: risk_score >= 60 (Intensive intervention)
        2: risk_score >= 30 OR pm2_score < 225 (Targeted intervention)
        1: Lower risk (Universal/core instruction)
    """
    if pd.isna(risk_score):
        return np.nan
    elif risk_score >= RTI_TIER_3_THRESHOLD:
        return 3
    elif risk_score >= RTI_TIER_2_THRESHOLD or (pd.notna(pm2_score) and pm2_score < RISK_PM2_LOW):
        return 2
    else:
        return 1

def calculate_proficiency_probability(row: pd.Series) -> float:
    """Calculate probability of reaching proficiency on PM3.

    Args:
        row: DataFrame row with PM2_Score and Growth

    Returns:
        Probability percentage (0-100) or None

    Probability thresholds:
        95%: Already proficient (PM2 >= 247)
        75%: Projected to reach proficiency (PM3 >= 247)
        50%: Approaching proficiency (PM3 >= 240)
        25%: Developing toward proficiency (PM3 >= 230)
        10%: Below developing threshold
        30%: No growth data available
    """
    if pd.isna(row['PM2_Score']):
        return None

    # Already proficient
    if row['PM2_Score'] >= PROFICIENCY_THRESHOLD:
        return PROB_ALREADY_PROFICIENT

    # No growth data to project from
    if pd.isna(row['Growth']):
        return PROB_NO_GROWTH_DATA

    # Project PM3 based on linear growth
    projected_pm3 = row['PM2_Score'] + row['Growth']

    if projected_pm3 >= PROFICIENCY_THRESHOLD:
        return PROB_PROJECTED_PROFICIENT
    elif projected_pm3 >= PROFICIENCY_APPROACHING_THRESHOLD:
        return PROB_APPROACHING_PROFICIENT
    elif projected_pm3 >= PROFICIENCY_DEVELOPING_THRESHOLD:
        return PROB_DEVELOPING
    else:
        return PROB_MINIMAL

def calculate_growth_quartile(growth_series: pd.Series) -> pd.Series:
    """Assign growth quartiles (Q1-Q4) based on distribution.

    Args:
        growth_series: Series of growth values

    Returns:
        Series of quartile labels (Q1, Q2, Q3, Q4)

    Note: Handles edge cases where there are fewer than 4 unique
    values by falling back to equal-width bins.
    """
    valid_growth = growth_series.dropna()

    # Need at least 4 values to create quartiles
    if len(valid_growth) < 4:
        return pd.Series('Q2', index=growth_series.index, dtype='object')

    try:
        # Try quantile-based quartiles first (preferred)
        quartiles = pd.qcut(
            valid_growth,
            q=4,
            labels=['Q1', 'Q2', 'Q3', 'Q4']
        )
    except ValueError:
        # Fall back to equal-width bins if not enough unique values
        quartiles = pd.cut(
            valid_growth,
            bins=4,
            labels=['Q1', 'Q2', 'Q3', 'Q4'],
            include_lowest=True
        )

    return quartiles.reindex(growth_series.index)

def analyze_pm_growth(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate comprehensive growth metrics for PM data.

    Args:
        data: DataFrame with PM1/PM2 scores and levels

    Returns:
        DataFrame enriched with growth analysis columns

    Raises:
        ValueError: If required columns are missing

    Added columns:
        - Growth: PM2 - PM1 delta
        - Level_Movement: Level change
        - Growth_Category: Emoji-labeled category
        - Growth_Quartile: Q1-Q4 ranking
        - Projected_PM3: Linear projection
        - Risk_Score: 0-100 scale
        - RTI_Tier: Tier 1/2/3 (numeric)
        - Proficiency_Probability: 0-100%
    """
    # Validate required columns
    required_cols = ['PM1_Score', 'PM2_Score', 'PM1_Level', 'PM2_Level']
    missing = [col for col in required_cols if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = data.copy()

    # Calculate basic growth metrics
    df['Growth'] = df['PM2_Score'] - df['PM1_Score']
    df['Level_Movement'] = df['PM2_Level'] - df['PM1_Level']

    # Categorize growth
    df['Growth_Category'] = df['Growth'].apply(categorize_growth)

    # Calculate growth quartiles
    df['Growth_Quartile'] = calculate_growth_quartile(df['Growth'])

    # Project PM3 scores (linear projection)
    df['Projected_PM3'] = df['PM2_Score'] + df['Growth']

    # Calculate risk scores
    df['Risk_Score'] = df.apply(calculate_risk_score, axis=1)

    # Assign RTI tiers
    df['RTI_Tier'] = df.apply(
        lambda row: assign_rti_tier(row['Risk_Score'], row['PM2_Score']),
        axis=1
    )

    # Calculate proficiency probability
    df['Proficiency_Probability'] = df.apply(calculate_proficiency_probability, axis=1)

    return df
```

## Example

```python
# Load cleaned PM data
data = pd.read_csv('_intermediate/cleaned_pm_data.csv')

# Analyze growth
enriched_data = analyze_pm_growth(data)

# View RTI tier distribution
print(enriched_data['RTI_Tier'].value_counts())

# View growth categories
print(enriched_data['Growth_Category'].value_counts())

# Save enriched data
enriched_data.to_csv('_intermediate/growth_analysis.csv', index=False)
```
