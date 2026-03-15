---
name: parent-contact-log
description: >
  This skill should be used when "logging parent contacts", "tracking parent communication",
  "documenting phone calls home", or recording any parent/guardian interaction.
  Use when the /log command detects a parent contact or when generating contact histories.
version: 1.0.0
---

# parent-contact-log Skill

## Purpose

Track all parent and guardian communications for documentation, conference preparation, RTI meetings, IEP meetings, and administrative accountability.

## Log Location

`~/Documents/Teaching/logs/parent-contacts.md`

## Entry Format

Entries are stored in a markdown table with the most recent entries first.

### Table Columns

| Date | Student | Parent/Guardian | Method | Topic | Follow-Up | Notes |
|------|---------|-----------------|--------|-------|-----------|-------|
| MM/DD | [Name] | [Name] | Phone/Email/In-Person/Note Sent | [Brief topic] | Y/N | [Additional details] |

### Entry Details

- **Date**: MM/DD (same year assumed unless cross-year)
- **Student**: First and last name
- **Parent/Guardian**: First and last name if provided; if unknown, note "Unknown" or describe relationship
- **Method**:
  - Phone (include approximate time if helpful)
  - Email (include if you sent or received)
  - In-Person (conference, pickup, hallway chat)
  - Note Sent (physical or digital)
  - Text (if school-approved)
- **Topic**: One-line summary (e.g., "Missing assignment inquiry", "Progress update", "Behavioral concern discussion")
- **Follow-Up**:
  - Y = action needed (callback, grade update, meeting, etc.)
  - N = information only
- **Notes**: Details like what was discussed, agreements made, promised actions, parent concerns, tone/responsiveness

## File Structure

### Header Section
```markdown
# Parent Contact Log

## Quick Stats
- Total contacts this month: [#]
- Total contacts this year: [#]
- Follow-ups pending: [#]
- Students with no contacts: [#]

## Contact Log
```

### New File Template

```markdown
# Parent Contact Log

## Quick Stats
- Total contacts this month: 0
- Total contacts this year: 0
- Follow-ups pending: 0
- Students with no contacts: [Count of total students]

## Contact Log

| Date | Student | Parent/Guardian | Method | Topic | Follow-Up | Notes |
|------|---------|-----------------|--------|-------|-----------|-------|
```

## Usage in /log Command

When `/log` detects a parent contact:

1. **Parse** input for:
   - Student name
   - Parent/guardian name (if given)
   - Contact method (phone/email/in-person/note)
   - Topic (brief summary)
   - Follow-up needed (yes/no)
   - Additional notes

2. **Examples of inputs that trigger this skill**:
   - "called Maria's mom about missing work"
   - "emailed Mr. Chen — sent reading level update"
   - "parent conference with Jose's guardians, discussed behavior expectations"
   - "left voicemail for David's dad re: after-school tutoring"
   - "Sophia's mom emailed, asking about reading level"

3. **Create or append** entry to `~/Documents/Teaching/logs/parent-contacts.md`

4. **Update Quick Stats** section:
   - Increment "Total contacts this month" (if same month)
   - Increment "Total contacts this year"
   - If follow-up = Y, increment "Follow-ups pending"
   - Decrement "Students with no contacts" (if first contact with that student)

## Generating Contact History

When asked to "pull contact history for [Student]":

1. **Filter** all entries for that student
2. **Sort** chronologically (most recent first)
3. **Compile** into a summary:
   ```markdown
   # Contact History: [Student Name]

   **Total contacts**: [#]
   **Last contact**: MM/DD via [method]
   **Follow-ups pending**: Y/N

   ## Chronological Log
   [filtered table]

   ## Summary
   [Tone, patterns, key topics, parent responsiveness, agreements made]
   ```

## Use Cases

- **Parent conference prep**: Pull contact history, identify concerns/progress
- **RTI documentation**: Show evidence of parent communication and partnerships
- **IEP meeting**: Document all communications leading up to and after meetings
- **Administrative request**: "Show me your parent contact log for [student]"
- **Accountability**: Demonstrate regular communication home
- **Behavior documentation**: Evidence of parent involvement in addressing concerns
- **Positive recognition**: Note when parents report student growth at home

## Important Notes

- **Confidentiality**: This log contains sensitive information; store securely
- **Professional tone**: Document objectively; avoid judgmental language
- **Two-way communication**: Note when parents initiate contact
- **Follow-up integrity**: Don't mark "N" for follow-up if you actually need to take action
- **Timestamp details**: Include time of day if contact was attempted multiple times or at odd hours
- **Responsiveness tracking**: Note if parent was available, left voicemail, got callback, etc.

## Monthly/Yearly Maintenance

At end of each month:
1. **Count total contacts** and update "Total contacts this month"
2. **Identify follow-ups** still pending and note reminders
3. **Calculate students contacted**: Compare to total roster
4. **Identify students** with no contacts (may need priority communication)

At end of school year:
1. **Archive** the log: `~/Documents/Teaching/logs/parent-contacts-2026.md` (if archiving)
2. **Generate annual summary** for evaluation or recertification
3. **Identify trends**: Which parents/guardians most responsive, most common topics, follow-up rates

## Integration

- **With /log command**: Primary entry point for quick logging
- **With behavior-tracker skill**: Cross-reference behavior notes when contacting parents
- **With observation-prep**: Can mention parent communication in "Professional Responsibility" domain
- **With classroom-notes**: Link general events to parent communication if relevant
