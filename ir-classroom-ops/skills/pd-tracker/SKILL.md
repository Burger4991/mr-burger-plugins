---
name: pd-tracker
description: >
  This skill should be used when "logging PD hours", "tracking professional development",
  "recording workshop attendance", or managing certification/recertification requirements.
  Use when the user mentions PD, inservice, workshops, or certification hours.
version: 1.0.0
---

# pd-tracker Skill

## Purpose

Track all professional development (PD) hours, workshops, conferences, online learning, and PLCs for Florida teaching certificate recertification and personal career development.

## Log Location

`~/Documents/Teaching/pd-log.md`

## Florida Recertification Requirements

- **Requirement**: 120 inservice points per 5-year certificate renewal cycle
- **Point value**: Typically 1 point = 1 hour of documented PD
- **Categories**:
  - Reading/Literacy (especially relevant for IR assignment)
  - ESOL (required if pursuing ESOL endorsement)
  - General PD (classroom management, assessment, technology)
  - Technology/Innovation
  - Leadership/Advanced work
  - College/University coursework

## Entry Format

Entries are stored in a markdown table.

### Table Columns

| Date | Title/Topic | Provider | Hours | Type | Certificate | Notes |
|------|-------------|----------|-------|------|-------------|-------|
| MM/DD/YYYY | [Workshop name] | [Organization] | [#] | Workshop/PLC/Online/Conference/Inservice | Y/N | [Details] |

### Entry Details

- **Date**: MM/DD/YYYY of completion or attendance
- **Title/Topic**: Full name of the workshop/course (e.g., "Structured Literacy: Evidence-Based Decoding Strategies", "ESOL Level 1 Foundations")
- **Provider**: Who offered it (school, district, state, university, conference, organization)
  - Examples: Miami-Dade County Public Schools, Florida Reading Association, Coursera, University of Florida, Reading Recovery, Fountas & Pinnell
- **Hours**: Number of contact hours or PD hours
- **Type**:
  - **Workshop**: One-time professional learning session
  - **PLC**: Professional Learning Community (ongoing collaborative work)
  - **Online**: Self-paced or instructor-led online course
  - **Conference**: Multi-day conference (count total hours)
  - **Inservice**: Required district inservice day(s)
  - **Coursework**: University or accredited college course (count semester hours)
- **Certificate**: Y/N — did you receive a completion certificate? (needed for recertification)
- **Notes**: Details like specific topics, relevance to teaching, speaker, outcomes, or links to materials

## File Structure

### Header Section

```markdown
# Professional Development Log

## Recertification Status

**Certificate Renewal Cycle**: [Year to Year]
**Hours Required**: 120
**Hours Completed**: [#]
**Hours Remaining**: [#]
**Status**: On Track / At Risk / Completed

### Breakdown by Category
| Category | Hours | Count |
|----------|-------|-------|
| Reading/Literacy | [#] | [#] |
| ESOL | [#] | [#] |
| General PD | [#] | [#] |
| Technology | [#] | [#] |
| Leadership | [#] | [#] |
| Coursework | [#] | [#] |
| **TOTAL** | **[#]** | **[#]** |

### Certificates Received This Year
- [Title] — [Date] — [Provider]
- [Title] — [Date] — [Provider]

## Full PD Log
```

### New File Template

```markdown
# Professional Development Log

## Recertification Status

**Certificate Renewal Cycle**: 2024-2029
**Hours Required**: 120
**Hours Completed**: 0
**Hours Remaining**: 120
**Status**: On Track

### Breakdown by Category
| Category | Hours | Count |
|----------|-------|-------|
| Reading/Literacy | 0 | 0 |
| ESOL | 0 | 0 |
| General PD | 0 | 0 |
| Technology | 0 | 0 |
| Leadership | 0 | 0 |
| Coursework | 0 | 0 |
| **TOTAL** | **0** | **0** |

### Certificates Received
(Will update as you complete workshops)

## Full PD Log

| Date | Title/Topic | Provider | Hours | Type | Certificate | Notes |
|------|-------------|----------|-------|------|-------------|-------|
```

## Usage Examples

### Adding a Workshop Entry

```
Title: "Structured Literacy: Phonemic Awareness & Decoding"
Provider: Miami-Dade County Public Schools
Hours: 6 (full-day workshop)
Type: Workshop
Certificate: Y
Notes: Focused on sound-sequencing activities and decoding strategies for struggling readers. Provided sample lesson plans. Highly relevant to IR instruction with ESOL learners.
```

### Adding a Conference Entry

```
Title: "Florida Reading Association Annual Conference 2026"
Provider: Florida Reading Association
Hours: 16 (2-day conference)
Type: Conference
Certificate: Y
Notes: Attended sessions on: (1) Multilingual literacy strategies, (2) Assessment and progress monitoring, (3) Technology in the reading classroom. Received FRA conference packet with resources.
```

### Adding a PLC Entry

```
Title: "Weekly IR Teacher PLC — Analyzing Student Data"
Provider: School District (ongoing)
Hours: 2 (weekly 1-hour meetings, logged as 2-hour entry)
Type: PLC
Certificate: N
Notes: Collaborative meeting with other IR teachers analyzing FAST data, discussing differentiation strategies, sharing student progress. Ongoing — will update monthly.
```

### Adding an Online Course

```
Title: "ESOL Strategies for Reading Instruction"
Provider: Coursera (University course)
Hours: 3
Type: Online
Certificate: Y
Notes: Self-paced course on incorporating ESOL-specific strategies into reading instruction. Covers comprehensible input, vocabulary development, and assessment modifications. Applied concepts to current lesson planning.
```

### Adding Coursework

```
Title: "Advanced Reading Instruction (GRE 6340)"
Provider: University of Florida, College of Education
Hours: 3 (semester credit hours)
Type: Coursework
Certificate: Y (official transcript)
Notes: Graduate-level course on evidence-based reading interventions, assessment, and data-driven instruction. Completed for master's degree. Counts as 3 hours per semester credit.
```

## Tracking & Maintenance

### Monthly/Quarterly Review

1. **Update totals**:
   - Add hours from entries since last update
   - Recalculate hours remaining
   - Update status

2. **Categorize new entries**:
   - Assign category based on content
   - If multiple categories, split hours (e.g., "Reading/Literacy: 4 hours, ESOL: 2 hours")

3. **Check certificates**:
   - File any certificates received
   - Update "Certificates Received" section
   - Note certificate numbers or dates if needed for recertification

### Quarterly Status Report

Generate at end of each quarter:

```markdown
## Q[X] Status Report

**Hours completed this quarter**: [#]
**Total hours to date**: [#]
**Hours remaining**: [#]
**On track**: Y/N

**Highlights**:
- [Most impactful PD this quarter]
- [New skills or knowledge gained]
- [Application to classroom]
```

### End-of-Year Summary

At end of each school year, create a summary:

```markdown
## 2025-26 Annual PD Summary

**Total hours completed**: [#]
**Certificates earned**: [#]
**Workshops attended**: [#]
**Conferences**: [#]
**PLC participation**: [#]
**Online courses**: [#]
**University coursework**: [#]

**Strongest areas of focus**:
- [Category with most hours]
- [Most relevant to current teaching]

**Goals for next year**:
- [Areas to develop further]
- [Certification/endorsement targets]
```

## Use Cases

1. **Recertification Application** (Florida DOE):
   - Pull complete list with certificates
   - Verify 120 hours in 5-year cycle
   - Submit required documentation

2. **Annual Teacher Evaluation**:
   - Show professional learning and growth
   - Demonstrate commitment to development
   - Discuss how PD improved practice

3. **Job Applications/Resume**:
   - List significant workshops, conferences, certifications
   - Show specialized training (ESOL, reading, technology)
   - Document advanced degrees or coursework

4. **ESOL Endorsement**:
   - Track ESOL-specific hours
   - Document hours toward ESOL add-on certification
   - Show pathway to endorsement completion

5. **Reading Specialization**:
   - Track reading/literacy PD
   - Document expertise in structured literacy, comprehension, ESOL reading strategies
   - Support literacy coaching or reading specialist role

6. **Funding/Reimbursement**:
   - Document PD funded by school/grant
   - Justify professional expenses
   - Show ROI from conference attendance

## Important Notes

- **Certificates matter**: Keep original certificates or screenshots for 5-year cycle (required for recertification)
- **Documentation**: Note dates, provider, and proof of completion for compliance
- **Relevance**: Prioritize PD aligned to your teaching assignment and growth goals
- **Timing**: Plan PD strategically across the 5-year cycle (don't cram at the end)
- **ESOL requirement**: If pursuing ESOL endorsement, ensure ESOL-specific training
- **Reading focus**: As an IR teacher, prioritize reading/literacy PD

## Integration

- **With resume/portfolio**: Use for professional accomplishment documentation
- **With job applications**: Reference relevant PD when applying for literacy coaching, reading specialist, or curriculum roles
- **With classroom goals**: PD informs teaching practice and student outcomes
- **With Second Brain**: Link significant PD to relevant projects or goals (e.g., "Structured Literacy workshop → update lesson plans")
- **With observation-prep**: Can mention recent PD in Domain 4 (Professional Responsibility) section
