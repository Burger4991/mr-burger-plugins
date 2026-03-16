---
name: behavior-tracker
description: >
  This skill should be used when "tracking student behavior", "logging participation",
  "documenting classroom behavior", or noting positive/concerning student patterns.
  Specifically for documenting in-class student BEHAVIOR patterns and observations,
  not parent communications. Use when the /log command detects behavior-related input.
version: 1.0.0
---

# behavior-tracker Skill

## Purpose

Track student behavior patterns—both positive engagement and behavioral concerns—for parent conferences, RTI meetings, identifying students who need support or recognition, and documenting growth over time.

**Important**: This is NOT a discipline referral system. This is a pattern-tracking tool for insights and documentation.

## Log Location

`~/Documents/Teaching/logs/behavior-notes.md`

## Entry Format

Entries are stored in a markdown table with the most recent entries first.

### Table Columns

| Date | Student | Type | Description | Context |
|------|---------|------|-------------|---------|
| MM/DD | [Name] | Positive/Concern/Neutral | [What happened] | [Period, activity, group] |

### Entry Details

- **Date**: MM/DD
- **Student**: First and last name
- **Type**:
  - **Positive**: Student volunteered, participated, helped peers, showed improvement, engaged deeply, took leadership
  - **Concern**: Disruptive behavior, off-task, disrespectful, incomplete work, absent, withdrawn, struggled
  - **Neutral**: Observation without judgment (e.g., "participated quietly in group")
- **Description**: What specifically happened (behavioral specificity matters)
  - ✓ "Participated 3 times with accurate predictions about character motivation"
  - ✓ "Left seat 4 times during independent station without permission"
  - ✗ "Good participation" (too vague)
  - ✗ "Bad behavior" (not specific)
- **Context**: Period number, activity type, grouping (whole class, small group, partner, independent), time of day if relevant
  - Example: "Period 4, literature circle, collaborative work"
  - Example: "Period 2, independent station, morning after absence"

## File Structure

### Header Section
```markdown
# Behavior Tracking Log

## Quick Stats
- Students with positive notes: [#]
- Students with concerns: [#]
- Follow-ups needed: [#]

## This Week's Standouts
- [Student]: [brief positive note]
- [Student]: [brief positive note]

## Check In On
- [Student]: [brief concern]
- [Student]: [brief concern]

## Behavior Log
```

### New File Template

```markdown
# Behavior Tracking Log

## Quick Stats
- Students with positive notes: 0
- Students with concerns: 0
- Follow-ups needed: 0

## This Week's Standouts
(Update weekly)

## Check In On
(Update weekly)

## Behavior Log

| Date | Student | Type | Description | Context |
|------|---------|------|-------------|---------|
```

## Usage in /log Command

When `/log` detects behavior-related input:

1. **Parse** input for:
   - Student name
   - Behavior type (positive/concern/neutral)
   - Specific description of what happened
   - Context (period, activity, grouping)

2. **Examples of inputs that trigger this skill**:
   - "Jayden participated 3 times in discussion today, really engaged"
   - "Isabella great predictions about character motivation during lit circle"
   - "Marcus disruptive during independent station, kept leaving seat"
   - "Sophia absent, that's 3 this month"
   - "David participated quietly but accurately in small group"
   - "80% of students completed bellringer on RACE framework"

3. **Create or append** entry to `~/Documents/Teaching/logs/behavior-notes.md`

4. **Update Quick Stats** section:
   - Count students with positive notes (unique students)
   - Count students with concerns (unique students)
   - Identify follow-ups needed (e.g., parent contact, conference, intervention)

## Positive Behavior Emphasis

**Important**: Log positive behaviors too. This skill is not just for concerns.

- Volunteering, participation, peer helping
- Improved engagement or participation over time
- Demonstration of reading strategies
- Collaboration and communication
- On-task behavior in challenging activities
- Growth in confidence or academic risk-taking

Example positive entries:
- "Participated in literature circle with specific text evidence from chapter 3"
- "Helped Marcus with annotation during collaborative station"
- "Attempted challenging text and made inferences independently"
- "Showed growth in confidence since last month — now raises hand in whole class"

## Pattern Detection

When reviewing behavior logs:

1. **Identify patterns**:
   - Which students consistently contribute? (possible student leaders)
   - Which students need redirection in certain activities? (rotations, grouping issue?)
   - Which students show growth over time? (celebrate this)
   - Which students withdraw or struggle repeatedly? (intervention candidates)

2. **Cross-reference**:
   - Compare to parent contact log: have you communicated about this pattern?
   - Compare to assessment data: does behavior align with performance?
   - Compare across activities: is the issue activity-specific or pervasive?

3. **Take action**:
   - Parent conference for concerns: "I've noticed..."
   - Recognition for growth: "You've shown improvement in..."
   - Grouping adjustment: if behavior is context-dependent
   - Intervention referral: if pattern suggests need for support

## Weekly Summary (Optional)

At end of each week, add a "This Week's Standouts" and "Check In On" section:

```markdown
## This Week's Standouts (W/O MM/DD)
- **Isabella**: Led literature circle discussion with text-based predictions
- **David**: First time volunteering in whole-class discussion
- **Sophia**: Completed all independent work without redirection

## Check In On (W/O MM/DD)
- **Marcus**: Left seat 4 times during independent work; consider movement breaks
- **Jose**: Absent 2 days; check on assignment completion and reading level
- **Tanya**: Withdrew from small group work; check in 1:1
```

## Use Cases

- **Parent conferences**: "I've noticed [positive pattern] with your child" or "Let's talk about [concern pattern]"
- **RTI documentation**: Show evidence of classroom observations and intervention attempts
- **IEP meetings**: Behavioral observations to support academic discussions
- **Student recognition**: "This month's participants" or "Great growth" recognition
- **Grouping decisions**: When forming stations or collaborative groups
- **Behavior intervention plans**: Document baseline and progress
- **Celebrating improvement**: "You used to [concern], now you [positive]"

## Important Notes

- **Objective language**: Focus on specific behaviors, not character judgments
  - ✓ "Left seat 4 times during independent work"
  - ✗ "Doesn't respect boundaries"
  - ✓ "Participated with evidence-based reasoning"
  - ✗ "Is a good student"

- **Frequency matters**: "3 times" vs "once" tells different stories
- **Context matters**: "During transitions" vs "during instruction" suggests different interventions
- **Privacy**: This log contains student information; store securely
- **Data, not drama**: Document observable behavior, not feelings or interpretations

## Monthly/Yearly Maintenance

At end of each month:
1. **Identify students with no positive notes**: intentional effort to catch them doing something right
2. **Review concern patterns**: are there repeated concerns that need intervention?
3. **Check follow-ups**: have you acted on documented concerns?
4. **Generate summary**: "This month, [students] showed great growth in [area]"

At end of year:
1. **Archive** the log: `~/Documents/Teaching/logs/behavior-notes-2026.md` (if archiving)
2. **Generate annual summary** for evaluation or year-end reflection
3. **Identify trends**: Growth areas, students who matured, consistent contributors
4. **Reflect**: How did classroom community develop? Which strategies worked?

## Integration

- **With /log command**: Primary entry point for quick logging
- **With parent-contact-log skill**: Link behavior observations to parent communications
- **With observation-prep**: Can highlight positive student behaviors in "Student Actions" section
- **With lesson planning**: Use patterns to inform grouping, differentiation, station design
- **With RTI/intervention**: Document baseline and progress over time
