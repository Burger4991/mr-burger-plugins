# ir-data-pipeline Smoke Test Cases

## Test Case 3: data-quality-checker

**Skill:** `ir-data-pipeline/skills/data-quality-checker/skill.md`

**Prompt:** I just got FAST PM3 data for my 4 IR classes (periods 2, 3, 5, 6). Here's a sample:

| Student | Period | PM1 | PM2 | PM3 |
|---------|--------|-----|-----|-----|
| Student A | 2 | 345 | 352 | 361 |
| Student B | 2 | 312 | | 380 |
| Student C | 3 | 289 | 295 | 291 |
| Student D | 5 | 401 | 395 | 398 |
| Student E | 6 | 350 | 355 | |
| Student F | 6 | 320 | 318 | 315 |
| Student G | 3 | 289 | 295 | 289 |
| Student G | 3 | 289 | 295 | 291 |

Run the data quality check on this.

**Expected concept:** A structured quality report identifying specific issues: Student B missing
PM2, Student E missing PM3, Student G has duplicate records, Student B's PM2→PM3 jump of 68+
points flagged as extreme change.

**Key checks:**
- Identifies missing PM2 value for Student B
- Identifies missing PM3 value for Student E
- Flags Student G as duplicate record
- Flags Student B's PM1→PM3 jump as extreme change (if PM2 missing, should note the gap)
- Output follows the CSV-style quality report format (check name, status, findings, details, action)
- Does NOT silently skip any quality check

---

## Test Case 4: growth-analyzer

**Skill:** `ir-data-pipeline/skills/growth-analyzer/skill.md`

**Prompt:** Analyze growth for these students from PM1 to PM3:

| Student | PM1 | PM2 | PM3 |
|---------|-----|-----|-----|
| Alex | 289 | 310 | 335 |
| Brianna | 401 | 395 | 398 |
| Carlos | 312 | 315 | 318 |
| Diana | 350 | 340 | 325 |
| Eli | 280 | 285 | 340 |

Use default proficiency threshold of 350.

**Expected concept:** Growth categorization for each student with risk scores, RTI tiers,
and proficiency probability. Alex and Eli should show rapid/significant growth. Diana should
show decline. Brianna should be stable/above threshold. Carlos should be steady/slow growth.

**Key checks:**
- Each student gets a growth category (Rapid, Moderate, Steady, Declining, Alert)
- Diana flagged as Declining (dropped 25 points)
- Eli flagged as Rapid growth (jumped 60 points)
- Risk scores assigned (0–100 scale)
- RTI tier assignments present
- Brianna identified as already proficient (above 350)
