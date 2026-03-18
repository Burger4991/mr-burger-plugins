# superpowers

Agentic workflow discipline for Claude Code and Cowork. Packaged from [obra/superpowers](https://github.com/obra/superpowers) (MIT license).

14 skills covering brainstorming, planning, execution, verification, parallel dispatch, code review, TDD, debugging, and git worktrees. 1 agent, 3 commands, and session hooks.

## Install

### Claude Code (official — recommended)

The original is available from the official marketplace:

```
/plugin install superpowers@claude-plugins-official
```

### Claude Code (from this marketplace)

```
/plugin marketplace add Burger4991/mr-burger-plugins
/plugin install superpowers@mr-burger-plugins
```

### Cowork

1. Download `superpowers.plugin` from [packages/](https://github.com/Burger4991/mr-burger-plugins/tree/main/packages)
2. Open Cowork settings → Plugins → Install from file

## What's included

### Skills (14)
- **brainstorming** — Collaborative design refinement before implementation
- **writing-plans** — Break work into bite-sized tasks with exact specs
- **executing-plans** — Execute plans with checkpoints and verification
- **subagent-driven-development** — Fresh agent per task with two-stage review
- **dispatching-parallel-agents** — Coordinate independent tasks concurrently
- **verification-before-completion** — Evidence before claims, always
- **using-superpowers** — Meta-skill for when and how to invoke skills
- **writing-skills** — Create new skills using TDD principles
- **test-driven-development** — RED-GREEN-REFACTOR cycles
- **systematic-debugging** — Root-cause investigation before fixes
- **using-git-worktrees** — Isolated development workspaces
- **finishing-a-development-branch** — Branch completion and merge decisions
- **requesting-code-review** — Request focused reviews with context
- **receiving-code-review** — Respond to feedback with technical rigor

### Agent
- **code-reviewer** — Reviews completed work across 6 dimensions

### Commands
- `/brainstorm` — Start a brainstorming session
- `/write-plan` — Create an implementation plan
- `/execute-plan` — Execute a plan with checkpoints

### Hooks
- **SessionStart** — Loads superpowers context on startup

## Credit

Original by [Jesse Vincent](https://github.com/obra/superpowers). MIT license. v5.0.5.
