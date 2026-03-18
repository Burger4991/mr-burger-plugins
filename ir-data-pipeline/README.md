# ir-data-pipeline

Student assessment data processing and analysis for 10th grade Intensive Reading.

10 skills for ingesting FAST PM and NWEA data, validating quality, calculating growth, assigning intervention tiers, tracking benchmark mastery, generating reports, and building visualizations. 2 agents for pipeline orchestration and parent communications.

## Install

### Claude Code

```
/plugin marketplace add Burger4991/mr-burger-plugins
/plugin install ir-data-pipeline@mr-burger-plugins
```

### Cowork

1. Download `ir-data-pipeline.plugin` from [Releases](https://github.com/Burger4991/mr-burger-plugins/tree/main/packages)
2. Open Cowork settings → Plugins → Install from file

### Development (local symlinks)

```bash
cd mr-burger-plugins && ./scripts/setup.sh
```

## What's included

### Skills
- **student-data-processor** — Import and normalize FAST PM + NWEA exports
- **data-quality-checker** — Validate data before analysis
- **growth-analyzer** — Calculate growth, assign RTI tiers, project proficiency
- **benchmark-mastery-analyzer** — Analyze per-benchmark performance from FAST PM
- **intervention-planner** — Create flexible groups (High/Middle/Low + Tier 1/2/3)
- **reporting-category-tracker** — Track NWEA reporting category performance
- **class-comparison-generator** — Compare across periods for admin meetings
- **report-builder** — Multi-sheet Excel workbooks with KPI dashboards
- **data-visualization-builder** — Charts and graphs for presentations
- **student-data-workflow** — Master workflow guide for the full year

### Agents
- **data-analyst** — Orchestrates the full ingest → validate → analyze → report pipeline
- **parent-reporter** — Generates parent-facing progress letters and conference prep

## Version

1.2.0
