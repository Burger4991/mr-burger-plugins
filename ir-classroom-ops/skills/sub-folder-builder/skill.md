---
name: sub-folder-builder
description: >
  Use when building a substitute teacher folder. Use this when "creating substitute materials",
  "preparing emergency sub plans", or assembling the permanent reference binder a sub needs.
  Trigger when: setting up new classroom, semester starts, updating sub materials.
  Builds a PERMANENT reference folder with all materials a sub needs (class lists, seating charts,
  procedures), distinct from the sub-plan-generator agent which creates daily lesson plans.
  Use when setting up a sub folder or compiling substitute materials. For daily sub plans,
  use the sub-plan-generator agent instead.
version: 1.0.0
---

# sub-folder-builder Skill

## Purpose

Generate a complete substitute teacher reference folder — the permanent binder/resource that gives a substitute teacher all the context they need to teach your classroom successfully.

**Important distinction**:
- **Sub Folder** (this skill): The permanent reference manual. Created once, updated each semester.
- **Daily Sub Plan** (separate agent): The specific lesson plan for a particular day. Created as-needed for each absence.

The sub folder provides the "how does this classroom work?" context. Daily sub plans provide the "what are we doing today?" specifics.

## Output Location

`~/Documents/Teaching/sub-folder/`

## Folder Contents

### 1. Cover Page / Welcome Letter

```markdown
# [Your Name]'s Classroom
## Room [#] | [School Name]

Dear Substitute Teacher,

Thank you for being here! My classroom operates on clear routines and procedures.
This folder has everything you need. If something is unclear, ask at the front office.

**Key contacts**: [See "Key Contacts" section below]

**Biggest wins if you can**:
1. Follow the daily schedule closely
2. Use positive praise frequently (these students respond well)
3. If anything feels out of control, don't hesitate to send for an administrator

You've got this!

— [Your Name]
```

### 2. Daily Schedule

```markdown
## Daily Schedule

| Period | Time | Class/Activity | Location |
|--------|------|----------------|----------|
| Duty | 7:45-8:00 | Hallway supervision | [Location] |
| 1st Period | 8:00-8:55 | Intensive Reading [period #] | Room [#] |
| Passing | 8:55-9:00 | [student transition] | [hallway] |
| 2nd Period | 9:00-9:55 | Intensive Reading [period #] | Room [#] |
| ... | ... | ... | ... |
| Lunch | [time] | [Your lunch duty or duty-free] | [Location] |
| ... | ... | ... | ... |

**Note**: This is a [6-day rotation / traditional week] schedule. Friday is [anything special?]
```

### 3. Class Rosters

Create a roster for each period with:
- Student names (alphabetical or seating order)
- Any known accommodations or notes (optional, based on privacy considerations)
- Groupings (who works well together, who needs separation)

```markdown
## Period [#] Roster

**Total students**: [#]

### Student List
1. [First & Last Name]
2. [First & Last Name]
...

### Groupings (for stations or activities)
**Group 1 (Station A)**: [Names]
**Group 2 (Station B)**: [Names]
**Group 3 (Station C)**: [Names]

### Notes
- [Student name]: ESOL Level [#], [accommodation if public]
- [Student name]: Works best with [peer names]
```

### 4. Seating Charts

If you have a seating chart, include it. If not, create a template:

```markdown
## Seating Chart: Period [#]

```
[Table 1]        [Table 2]
A  B  C  D       E  F  G  H

[Table 3]
I  J  K  L

[Teacher Desk]  [Door]
```

**Reference**:
- A = [Student name]
- B = [Student name]
...
```

### 5. Classroom Procedures

```markdown
## Classroom Procedures

### Arrival & Dismissal
- **Start of class**: Students put phones away, sit at assigned seats. Take attendance on [system].
- **What students do**: Open their books/notebooks, look at the bellringer on the board.
- **Late arrivals**: [Do they need a late pass? Do they come in quietly? Sit in back?]
- **End of period**: [Do they pack up 2 min before? Pack nothing?] Pack up when the bell rings. Dismissal is quiet — students leave when dismissed, not before.

### Bathroom/Phone Policy
- **Bathroom**: [How many students can go? Do they need a pass? Is it a certain time only?]
- **Phone**: [Are phones allowed? When? Where do they go?]

### Participation/Engagement
- **Expectation**: Students should be reading, writing, discussing, or completing tasks.
- **How to praise**: "I notice [name] is making great predictions about the text!" Works better than general praise.
- **Off-task students**: Use the "See-Say-Do" approach: notice the behavior, give the student a choice, follow through quietly.

### Rotations (if applicable — IR classrooms)
- **What it is**: Students rotate between 3 stations every [15-20] minutes.
- **How it works**: I give a signal, students wrap up, move to the next station. [Describe how you signal and manage transitions.]
- **If it's too complex**: You can put everyone whole-class and do a single activity instead. Rotations are ideal but not required if it's confusing.
- **Stations**:
  - **Teacher-Led** (my table): This is where I work with a small group. Sub can supervise and help with reading or tasks.
  - **Independent** (usually quieter area): Students read, annotate, or complete a graphic organizer alone.
  - **Collaborative** (grouped area): Students work in pairs or small groups — literature circles, partner read-alouds, discussion.

### Attendance & Tardies
- **Taking attendance**: [Explain your attendance system — is it digital? Paper? Where is the roster?]
- **Marking tardies**: [If student arrives after [time], mark tardy. Send to office if [criteria].]

### Materials & Supplies
- **Pencils/pens**: Students should have their own. Extras are in [location].
- **Handouts**: Blank copies of [graphic organizer / exit ticket / etc.] are in [location].
- **Technology**: [If you use Chromebooks/smartboard/projector, give brief instructions.]

### Transitions Between Activities
- **Signal for attention**: [How do you get students' attention? Whistle? Lights? Hand raise?]
- **Cleanup**: Students push in chairs, organize materials, and sit down within 2 minutes.
- **Time warnings**: "5 minutes left" helps students wrap up.
```

### 6. Behavior Management

```markdown
## Behavior Management

### Positive Reinforcement
- **What works**: Specific praise ("I notice you're using the RACE framework correctly"), classroom dojo points [if applicable], verbal acknowledgment
- **Frequent praising**: Aim for 5+ positive comments in a 50-minute period
- **Don't use**: Sarcasm, comparing to other students, humiliation

### Off-Task Behavior
1. **First**: Proximity and eye contact (move near the student, make eye contact)
2. **Second**: Quiet redirection ("Marcus, eyes on your text" — said privately, not publicly)
3. **Third**: Offer a choice ("You can [on-task option A] or [on-task option B]. Your choice.")
4. **If still off-task**: Move student seat, have them step outside for a 2-min reset, or send to [admin/principal] if behavior is serious

### Concerning Behaviors (What to Do)
- **Disrespect to you**: Stay calm. Don't match energy. Say: "I understand you're frustrated, but I need you to [expected behavior]." If escalates, send to office.
- **Student conflict**: Separate students immediately. Have each explain quietly to you. Don't solve it alone — get admin if needed.
- **Refusal to work**: Offer choices, check if student understands the task, offer help. If refusal continues, document and send to office.
- **Leaving the room without permission**: Follow student into hallway. Calmly say: "Please come back to class." If student won't return, get admin immediately.

### Contact for Help
- **Small behavior issues**: Handle in class using the steps above
- **Medium issues** (repeated off-task, talking back, not following directions): Contact [admin/dean/counselor]
- **Big issues** (violence, serious disrespect, refusal to comply): Get admin/principal immediately. Use your radio or walk to the office.

### Crisis Protocol
- **If a student has an emotional crisis**: Don't isolate them. Get another adult. [School crisis procedures].
- **If you feel unsafe**: Leave the room and get help immediately.

**Important**: This classroom is safe. These students are generally cooperative and kind. Don't be afraid to redirect firmly but kindly.
```

### 7. Emergency Procedures

```markdown
## Emergency Procedures

### Fire Drill
- **Procedure**: When alarm sounds, line students up at the [door/window].
- **Route**: Exit through [door], go to [assembly area].
- **Headcount**: Once outside, count students and report to [admin/site commander].
- **Return**: Wait for all-clear signal. Return to classroom in line.
- **Time needed**: ~[5] minutes.

### Lockdown
- **Procedure**: When announcement is made, immediately lock the door and turn off lights.
- **Student positioning**: Gather students away from windows, in [area of classroom].
- **Silence**: Students are silent. No talking. No movement unless directed.
- **Weapons/threats**: Don't assume anything. Treat every lockdown as serious.
- **Exit**: Wait for all-clear announcement and directions from [admin].

### Severe Weather (Tornado/Hurricane)
- **Procedure**: Students move to [designated room/hallway], sit against [interior wall].
- **Gathering**: Bring [roster, first aid kit] with you.
- **Wait**: Stay in position until all-clear or further instruction.

### Medical Emergency
- **Injury in classroom**: Don't move injured student. Call the office or use your radio: "[Name], I need the nurse in [Room #]. We have a [minor/serious] injury."
- **Diabetic emergency / seizure**: Don't be a hero. Call for help immediately.
- **Serious injury or unresponsiveness**: Call 911 (your radio will direct you or do this).
- **First aid kit**: Located in [location].
```

### 8. Key Contacts

```markdown
## Key Contacts

### School Information
- **School Name**: [Name]
- **Address**: [Address]
- **Main Office**: [Phone]
- **School Hours**: [Times]

### People to Contact
| Role | Name | Room/Location | Phone/Extension |
|------|------|---------------|-----------------|
| Principal | [Name] | [Loc] | [Phone] |
| Assistant Principal | [Name] | [Loc] | [Phone] |
| Dean of Students | [Name] | [Loc] | [Phone] |
| School Counselor | [Name] | [Office] | [Ext] |
| School Nurse | [Name] | [Health Office] | [Ext] |
| Department Chair | [Name] | [Loc] | [Ext] |
| Neighboring Teacher (for help) | [Name] | [Room] | [Ext] |
| My Email | [Your Email] | — | — |

### Front Office
- **Attendance/Tardies**: Main office, extension [X]
- **Passes**: Ask front office staff
- **Bathrooms/Emergencies**: Use your radio or phone to call main office

### Technology Help
- **Chromebook issues**: [Tech support contact or your instructions]
- **Smartboard/Projector**: [Contact or troubleshooting steps]
- **WiFi problems**: Tell the office
```

### 9. IR-Specific Notes (Intensive Reading)

```markdown
## Intensive Reading: What You Should Know

### What Is IR?
Intensive Reading is a targeted reading intervention for students reading below grade level. The focus is on:
- **Foundational skills**: Decoding, fluency, phonemic awareness (if needed)
- **Comprehension**: Understanding what they read using strategies like RACE (Restate, Answer, Cite, Explain)
- **Vocabulary**: Building word knowledge and strategy use
- **Student choice**: Some autonomy in what they read (choice within structure)

### The Rotation Model (3 Stations)
Your classroom likely runs on a 3-station rotation:

**Station 1: Teacher-Led (15-20 min)**
- I work with a small group (4-6 students)
- We read together, I model strategies, we discuss
- Students have support and immediate feedback
- This is the most intensive station

**Station 2: Independent (15-20 min)**
- Students work alone on a task
- Usually: reading at their level, annotating, completing a graphic organizer
- They should be quiet and focused
- Check in occasionally, answer questions

**Station 3: Collaborative (15-20 min)**
- Students work in pairs or small groups
- Literature circles, partner read-alouds, peer discussions, peer editing
- They should be engaged and talking about the text
- Monitor for on-task behavior

**Rotation Rules**:
- At [signal], students wrap up their work
- Students move to the next station
- Transition should take 2 minutes max
- If one group is still reading intensely, let them finish — don't abruptly stop them

### If Rotations Feel Too Complex
**You have permission to go whole-class instead.** It's better to have all students doing the same activity successfully than to manage rotations chaotically. Do what keeps students engaged and safe.

### Daily Sub Plan
**The lesson plan for today is attached** (see "Daily Sub Plan" document). It has:
- Today's objective
- Today's activity/text
- Groupings for stations (or instructions if going whole-class)
- Materials you'll need
- Exit ticket or closing activity

### Data Matters
I use FAST scores (state reading assessment) and NWEA scores to group students. Higher-performing students can handle more complex texts. Struggling students need more support. Groups change based on progress.

### Vocabulary & Frameworks You'll See
- **FAST**: Florida Assessment of Student Thinking (state reading test)
- **NWEA/MAP**: Reading growth measures
- **RACE**: Restate (the question), Answer (your response), Cite (evidence), Explain (why) — the writing/comprehension framework we use
- **Annotation**: Notes students write on the text itself (highlighter, circles, margins)
- **Fluency**: Reading smoothly and at a good pace
- **Comprehension check**: "Do you understand what you just read?"

### What Success Looks Like
- Students are focused on reading/tasks
- Talking is about the text (not off-topic)
- Students use RACE framework language
- Students can answer comprehension questions with evidence
- Transitions happen smoothly
- Positive energy and mutual respect

---

**The bottom line**: This is a warm, structured classroom. Students want to succeed. You've got this!
```

### 10. Where to Find Daily Sub Plans

```markdown
## Daily Sub Plans

Each day I teach, I prepare a detailed sub plan. If I'm absent, the plan is:
- **Printed and left on my desk** (or in this folder as an attachment)
- **Digital copy**: Sent to front office / your email
- **What it includes**: Today's objective, activity, materials, groupings, bell-ringers/exit tickets, any special notes

**If you don't have a daily plan**:
1. Check my desk
2. Check the front office
3. Call [admin/contact] — they may have it
4. Use the "No-Plan Day" activity list below

---

## No-Plan Day Activities (If There's No Daily Sub Plan)

If for some reason there's no daily sub plan, choose one of these:

### Option 1: Read & Respond
- **Materials**: Any level-appropriate texts (classroom library, next unit books, passages on the shelf)
- **Activity**: Students read independently for 25-30 minutes, then complete an exit ticket: "What was the main idea? What's one thing [character/author] did?"
- **Grouping**: Whole class or rotations if you want to supervise reading

### Option 2: Review & Reflect
- **Materials**: Previous unit graphic organizers, reading passages from this month
- **Activity**: Students review past work, complete a reflection: "What strategies have you learned? What's challenging?"
- **Grouping**: Whole class discussion, then independent writing

### Option 3: Vocabulary Building
- **Materials**: Vocabulary words from current unit (should be listed on a poster or in materials folder)
- **Activity**: Review words, students use them in sentences, play vocabulary games (Hangman, quick-draw, synonym match)
- **Grouping**: Whole class games or partner work

### Option 4: Audiobook & Response
- **Materials**: Audiobook access (computer/projector or student devices), response sheet template
- **Activity**: Listen to an audiobook chapter or short story, respond to comprehension questions
- **Grouping**: Whole class, then small-group discussion

**Key rule**: Whatever you choose, students should be engaged with reading or reading-related tasks. Avoid videos, games, or busy work unrelated to reading.
```

## Skill Usage

When invoked to build a sub folder, Claude will:

1. **Ask for context**:
   - School name, grade, subject (IR)
   - Period numbers/times
   - Number of students per period
   - Any special procedures (rotations, specific behavior systems, technology)
   - Your key contacts at the school
   - Emergency procedures specific to your school

2. **Gather from available files**:
   - Student rosters (if available in Documents/Teaching/)
   - Seating charts (if available)
   - Unit materials (to understand what content substitutes should know)
   - Any existing procedures documents

3. **Generate** a complete markdown folder with all 10 sections above

4. **Save to** `~/Documents/Teaching/sub-folder/` with clear naming:
   - `sub-folder-master.md` (combined document)
   - Or separate files: `01-cover-page.md`, `02-schedule.md`, etc.

## Best Practices

1. **Accuracy**: Double-check names, times, procedures
2. **Clarity**: Write for someone unfamiliar with your room
3. **Honesty**: Tell subs what will actually work, not what you wish would work
4. **Updates**: Refresh rosters, schedules, and contacts at start of semester
5. **Accessibility**: Make sure subs can find this folder (email, printed in binder, on your desk)
6. **Printing**: This should be printable as a booklet (single-sided or double-sided)

## Maintenance Schedule

- **Start of school year**: Create or completely refresh sub folder
- **After roster changes** (mid-year): Update rosters and groupings
- **Before long absence**: Verify all information is current
- **Start of second semester**: Update schedule if it changes; update rosters

## Integration

- **Complements**: Daily sub plans (which provide specific lesson details)
- **Uses context from**: Your classroom files, roster information, school procedures
- **Feeds into**: Emergency absence planning, peace of mind when you're sick
- **Supports**: Substitute teacher success, student continuity, reduced class disruption
