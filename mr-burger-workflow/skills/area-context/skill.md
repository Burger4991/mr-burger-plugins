---
name: area-context
description: >
  This skill provides context for personal life AREAS (teaching, personal, tech) and project
  file locations. Use when determining which life area a task or note belongs to, or when
  needing context about the user's projects and file locations. About personal life areas
  and project file organization, not plugin ownership or inter-plugin routing.
version: 2.0.0
---

# Area Context Skill

## Overview

Mr. Burger's life and work are organized into 6 distinct areas. This skill provides context for each area, including file locations, active projects, and keyword routing to help identify where new content belongs.

---

## The Six Life Areas

### 1. Teaching

**Purpose**: 10th grade Intensive Reading instruction in Miami-Dade County Public Schools (MDCPS)

**Primary Files & Locations**:
- Main folder: `~/Documents/Teaching/`
- Notes: `~/Documents/Teaching/notes.md`
- File types: lesson plans, unit plans, assessment data, ESOL adaptations, rubrics, benchmarks

**Active Projects**:
- Building complete short story unit with ESOL adaptations and assessments
- Weekly lesson planning (6-day rotation cycle)
- PM (Progress Monitoring) data analysis for student tracking
- ESOL support and scaffolding strategies for levels 1-5
- Beginning band materials and trumpet instruction
- Claude Code teaching skills (55+) and agents (11)

**Context**:
- **Class**: IR (Intensive Reading) for 10th graders with diverse needs
- **Standards Framework**: Florida BEST (Benchmarks for Excellent Student Thinking) ELA standards
- **Student Population**: High ESOL population (levels 1-5); diverse learning needs
- **Cycle**: 6-day rotation (not traditional 5-day week)
- **Key Assessments**: FAST (Florida Assessment of Student Thinking), PM (Progress Monitoring), NWEA/MAP tests
- **Key Frameworks**: Gradual Release (I Do / We Do / You Do), RACE (Restate, Answer, Cite, Explain), CER (Claim-Evidence-Reasoning) writing
- **Music Role**: Teaches trumpet in beginning band; jazz vocabulary, Adam routine (jazz fundamentals)

**Keywords for Routing**:
- "unit", "lesson", "benchmark", "ESOL", "students", "classroom", "assessment", "PM data", "FAST", "10th grade", "IR", "teaching"

---

### 2. Career

**Purpose**: Active job search for teaching positions or tech-adjacent roles in education

**Primary Files & Locations**:
- Main folder: `~/Documents/Career/`
- Notes: `~/Documents/Career/notes.md`
- File types: resume, cover letters, job applications tracker, interview notes, portfolio materials

**Active Projects**:
- Job applications: 2-3 per week target
- Resume updates and tailoring per position
- Portfolio building (teaching examples, Claude Code projects, unit examples)
- Interview prep and salary negotiation
- Networking and company research (K-12 schools, edtech companies, tech integration roles)

**Context**:
- **Current Role**: 10th grade IR teacher, MDCPS
- **Desired Roles**: Full-time teaching position (ideally with tech integration), or tech-adjacent education roles (instructional design, ed tech, curriculum development)
- **Timeline**: Actively applying through end of school year
- **Strengths to Highlight**: Teaching experience, Claude Code expertise, tech skills, ESOL proficiency, unit building
- **Target Companies/Sectors**: Miami-Dade schools, edtech startups, curriculum companies, international schools

**Keywords for Routing**:
- "resume", "application", "interview", "job", "cover letter", "portfolio", "salary", "career", "hired", "applied to"

---

### 3. Music

**Purpose**: Personal musicianship and development (trumpet, guitar, jazz)

**Primary Files & Locations**:
- Main folder: `~/Documents/Music/`
- Notes: `~/Documents/Music/notes.md`
- File types: practice logs, song charts, technique notes, teaching materials (beginning band)

**Active Projects**:
- Trumpet: Jazz vocabulary development, Adam routine daily practice
- Guitar: Basic exploration and learning
- Beginning band: Teaching trumpet to students (part of teaching role)
- Practice routine: Consistent daily practice with focused skill goals

**Context**:
- **Trumpet**: Main instrument. Focuses on jazz vocabulary and fundamentals. Adam routine is a structured daily practice approach.
- **Guitar**: Hobbyist, beginner level, learning basics
- **Teaching**: Uses trumpet knowledge to teach beginning band students at school
- **Practice Philosophy**: Consistent, focused practice over long sessions
- **Style Focus**: Jazz vocabulary, improvisation, musicianship

**Keywords for Routing**:
- "trumpet", "jazz", "band", "guitar", "practice", "music", "song", "Adam routine", "scales", "improvisation"

---

### 4. Dog Training

**Purpose**: Training Olive (his dog) using Susan Garrett methods and completing structured courses

**Primary Files & Locations**:
- Main folder: `~/Documents/Dog-Training/`
- Notes: `~/Documents/Dog-Training/notes.md`
- File types: training logs, course notes, progress tracking, behavior notes

**Active Projects**:
- Recallers course: In progress (building reliable recall with Olive)
- J Walking: Upcoming course focus
- HSTD (Handling Skills Teaching Dogs or similar): Planned course
- Building Olive's foundation skills using Susan Garrett framework

**Context**:
- **Dog**: Olive
- **Training Philosophy**: Susan Garrett methods (positive reinforcement, foundation building)
- **Focus Areas**: Recall (reliable, strong response), leash walking, handling skills
- **Course Structure**: Structured programs with submissions and feedback
- **Pace**: Ongoing, regular training practice with Olive

**Keywords for Routing**:
- "Olive", "training", "Susan Garrett", "dog", "Recallers", "J Walking", "HSTD", "puppy", "behavior", "recall"

---

### 5. Personal

**Purpose**: Life logistics, health, finance, wellness, and miscellaneous personal matters

**Primary Files & Locations**:
- Main folder: `~/Documents/Personal/`
- Notes: `~/Documents/Personal/notes.md`
- File types: finance tracking, health records, wellness notes, legal documents, life planning

**Active Projects**:
- Finance: Monthly budgeting, expense tracking, financial planning
- Health/Wellness: Regular checkups, fitness, nutrition, sleep hygiene
- Personal development: Reading, learning, habits
- Life logistics: Bills, appointments, housekeeping, family

**Context**:
- **Location**: Miami, Florida
- **Employment**: Teacher (MDCPS), active in job search
- **Lifestyle**: Health-conscious, active (dog training, music, fitness)
- **Values**: Continuous learning, wellness, work-life balance

**Keywords for Routing**:
- "finance", "money", "budget", "health", "doctor", "fitness", "wellness", "personal", "appointment", "bill", "family", "house"

---

### 6. Tech

**Purpose**: Technology skills, coding, tools, and personal tech projects

**Primary Files & Locations**:
- Main folder: `~/Documents/Tech/`
- Notes: `~/Documents/Tech/notes.md`
- File types: code, configs, plugin documentation, GitHub project notes

**Active Projects**:
- Claude Code: Master teaching skills library (55+), agents (11), hooks
- mr-burger-plugins: Personal productivity plugin ecosystem (`~/Documents/Tech/mr-burger-plugins/`)
- GitHub projects: Teaching tools, personal projects, code samples

**Context**:
- **Expertise**: Claude Code power user, prompt engineering, agent building
- **Tools Used**: Claude Code, GitHub, keyboard automation
- **Focus**: Automation for teaching efficiency, personal productivity plugins
- **Philosophy**: Build systems that reduce manual overhead, keep tools simple

**Keywords for Routing**:
- "plugin", "Claude", "code", "GitHub", "JavaScript", "keyboard", "config", "tool", "automation", "agent", "skill"

---

## Routing Decision Tree

When you encounter new content (task, note, idea, question), use this tree to determine the area:

1. **Is it about classroom, students, lesson planning, standards, ESOL, or assessments?**
   → **Teaching**

2. **Is it about resumes, job applications, interviews, portfolio, or career moves?**
   → **Career**

3. **Is it about trumpet, guitar, jazz, practice, or music teaching?**
   → **Music**

4. **Is it about Olive, dog training, Susan Garrett methods, or behavioral training?**
   → **Dog Training**

5. **Is it about money, health, appointments, personal logistics, or life stuff?**
   → **Personal**

6. **Is it about code, plugins, tools, automation, GitHub, or tech projects?**
   → **Tech**

7. **If multiple areas apply**: Tag with the PRIMARY area, note secondary areas in content if helpful.
   - "Build a Claude Code skill for lesson planning" → Primary: **Tech**, secondary: Teaching
   - "Teaching experience for job portfolio" → Primary: **Career**, secondary: Teaching

---

## Area Tags

When storing tasks in TASKS.md or notes, always tag the area in square brackets:

- `[Teaching]` — Classroom work, lesson planning, student assessment
- `[Career]` — Job search, resume, applications, interviews
- `[Music]` — Practice, performance, instruction
- `[Dog Training]` — Training, courses, Olive's progress
- `[Personal]` — Finance, health, life logistics
- `[Tech]` — Code, plugins, tool building, automation

Examples:
- `- [ ] [Teaching] Grade PM2 data for Week 4`
- `- [ ] [Career] Finalize portfolio updates for position #5`
- `- [ ] [Music] Practice Adam routine (30 min)`
- `- [ ] [Dog Training] Submit Recallers project`
- `- [ ] [Personal] Schedule doctor appointment`
- `- [ ] [Tech] Debug capture-detector.js hook`

---

## File Location Quick Reference

| Area | Main Folder | Notes | Knowledge |
|------|-------------|-------|-----------|
| **Teaching** | ~/Documents/Teaching/ | ~/Documents/Teaching/notes.md | ~/Documents/Knowledge/teaching.md |
| **Career** | ~/Documents/Career/ | ~/Documents/Career/notes.md | ~/Documents/Knowledge/career.md |
| **Music** | ~/Documents/Music/ | ~/Documents/Music/notes.md | ~/Documents/Knowledge/music.md |
| **Dog Training** | ~/Documents/Dog-Training/ | ~/Documents/Dog-Training/notes.md | ~/Documents/Knowledge/dog-training.md |
| **Personal** | ~/Documents/Personal/ | ~/Documents/Personal/notes.md | — |
| **Tech** | ~/Documents/Tech/ | ~/Documents/Tech/notes.md | ~/Documents/Knowledge/tech-systems.md |

---

## Context Summary for Claude

When helping Mr. Burger with any request, keep this in mind:

- **Busy but Organized**: Teaching full-time, job searching, maintaining personal projects (music, dog training, tech)
- **Tool-Savvy**: Power user of Claude Code, GitHub, automation
- **Systems-Minded**: Prefers simple, organized systems over complex tools
- **Values**: Efficiency, clarity, minimal context-switching
- **Communication Style**: Direct, structured, action-oriented
- **Growth Mindset**: Always learning and improving (teaching, music, training, tech)

---

## Integration with Commands

- **`/capture`**: Uses area-context to route brain dumps to the correct notes.md and TASKS.md
- **`/wrap`**: Uses area-context to understand what was worked on when writing HANDOFF.md
- **`/reflect`**: Uses area-context to find the right Knowledge/ file to update
- **`/checkpoint`**: Uses area-context across all save operations

This skill is referenced by all commands that need to determine where content belongs or understand Mr. Burger's context and priorities.
