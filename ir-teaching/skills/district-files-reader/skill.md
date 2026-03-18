---
name: district-files-reader
description: Reads and extracts content from district-provided PDFs, Word docs, and text files. Use when starting a new unit to pull benchmark info, text passages, or planning materials.
---

# District Files Reader

## Purpose
Extract and organize content from district materials including:
- Unit texts (passages, stories, articles)
- Benchmark organizers
- Planning guides
- Assessment templates
- Vocabulary lists

## How to Use

**Step 1: Locate Files**
District files should be in: `Teaching/Units/[UnitName]/05-District-Files/`

**Step 2: Identify File Types**
- **PDFs**: Use Read tool to extract text and images
- **Word docs (.md)**: Convert to text or read directly
- **Text files (.txt, .md)**: Read directly with Read tool
- **Images (.png, .jpg)**: Read tool can view images directly

**Step 3: Extract Key Information**
When reading district files, look for:
- **Benchmark codes** (e.g., ELA.10.R.1.2)
- **Unit texts** (passages, poems, articles)
- **Vocabulary words** with definitions
- **Question stems** from Planning Cards
- **Organizer templates** with column headers
- **Assessment formats** and rubrics

**Step 4: Organize Extracted Content**
Create working documents in appropriate folders:
- Text passages → Use in StudentPacket
- Benchmark codes → Align with `benchmarks` skill (see standards/)
- Vocabulary → Create Day 1-2 activities
- Organizers → Build into Day 3-4 lesson plans
- Question stems → Use for margin questions and assessments

## Common District File Patterns

### Reading Passages
- Usually in PDF format
- May include margin questions
- Check for text complexity information
- Note any pre-marked vocabulary

### Benchmark Organizers
- Often in Word doc format
- Column headers indicate benchmark focus
- May have example rows filled in
- Adapt for gradual release structure

### Planning Guides
- Lists standards and objectives
- Suggests pacing (may need adjustment for 6-day cycle)
- Includes recommended resources
- Extract question stems for use in lessons

## Workflow Example
1. User uploads district files to `05-District-Files/`
2. Use Glob to find all files in that directory
3. Read each file to extract content
4. Summarize key elements (text, benchmarks, vocab)
5. Use extracted info to build Day 1-6 materials
6. Reference district files in teacher plans for transparency

## File Reading Commands
```bash
# List all district files
ls -la Teaching/Units/[UnitName]/05-District-Files/

# Find specific file types
find Teaching/Units/[UnitName]/05-District-Files/ -name "*.pdf"
```

## Concrete Example: Extract Flow

**Input**: District PDF file titled "The-Giver-Unit-Guide.pdf"

**Extracted sections**:

### 1. Full Text
```
Chapter 3, The Ceremony of Twelve (excerpt)
"At the age of twelve, all children receive their life assignments..."
[Full passage text extracted]
```

### 2. Margin Questions
```
- What does the Ceremony of Twelve represent?
- How do the characters feel about their assignments?
- What is the author's purpose in using this ritual?
```

### 3. Vocabulary Words
```
- ceremony (noun): official religious or formal event
- assignment (noun): task or role given to someone
- apprehensive (adj): anxious, worried about something
```

### 4. Benchmark Alignment Info
```
ELA.10.R.1.2 (Theme): Trace how dystopian themes develop through ceremony/control
ELA.10.R.1.1 (Literary Elements): Analyze character reactions to assignments
ELA.10.V.1.3 (Context & Connotation): Determine meaning of "assignment" from context
```

## Output Specification

The extraction produces structured sections that other skills consume:

### Full Text Section
- **Content**: Complete passage text with paragraph numbers
- **Use**: Provides source material for student packets, margin questions, evidence locations
- **Format**: Plain text with ¶ symbols marking paragraph breaks
- **Consumers**: teaching-templates, assessment-design (for question creation)

### Margin Questions Section
- **Content**: District-provided or suggested comprehension questions
- **Use**: Adapt to margin questions on student packets, create exit tickets
- **Format**: Numbered list with benchmark alignment
- **Consumers**: ir-framework (Day 1-4 comprehension checks), assessment-design (formative questions)

### Vocabulary Section
- **Content**: Words pre-identified by district or selected for grade level
- **Use**: Compare with vocabulary-instruction selections, integrate into Day 1-2 activities
- **Format**: List with part of speech and context
- **Consumers**: vocabulary-instruction (refine Tier 2 word selection), teaching-templates

### Benchmark Info Section
- **Content**: Explicit standard codes and alignment notes
- **Use**: Validate unit focus, align organizers and assessment
- **Format**: Code + brief explanation of connection
- **Consumers**: benchmarks (reference full guides), organizer-design (align column structure)

## Error Handling

**File is Corrupted or Unreadable**:
- If PDF is scanned image-only (no extractable text): "This PDF appears to be image-based. I can see the content visually but cannot extract searchable text. Alternative: manually type key passages or upload a text version."
- If Word doc has formatting issues: "Document contains formatting that prevents clean text extraction. I can read sections but may need manual verification of structure."

**Wrong File Format**:
- If user uploads unsupported format (video, audio, spreadsheet): "This skill works with PDFs, Word docs (.md), and text files. Please upload a district material in one of these formats."

**No Extractable Content**:
- If file is blank or has no readable content: "This file appears empty or contains only images/graphics with no readable text. Please verify the file is the correct unit material."

**Benchmark Codes Not Found**:
- If district file doesn't mention specific benchmarks: "No benchmark codes were found in this file. I've extracted the content structure. You can manually align it to benchmarks using the benchmarks skill."

**Partial Extraction**:
- If only some sections extract successfully: "Successfully extracted [X sections]. Note: [section name] had extraction issues and may need manual review."

## Integration with Other Skills
- **benchmarks**: Match district benchmark codes to Planning Card stems and full guides
- **ir-framework**: Adapt district materials to 6-day cycle structure
- **teaching-templates**: Use district content in properly named deliverables
- **vocabulary-instruction**: Compare district vocabulary selections with Tier 2/3 criteria
- **organizer-design**: Map district organizer columns to benchmark analytical processes
- **assessment-design**: Use district passage for question creation and assessment alignment
