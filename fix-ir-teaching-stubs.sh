#!/bin/bash
# Fix missing Skills and Hooks stubs in ir-teaching-materials repo
# Run from: the ir-teaching-materials repo root

set -e

VAULT="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Teaching/Teaching"

# Check we're in the right place
if [ ! -f "Claude-System/_Index.md" ]; then
    echo "Error: Run this from the ir-teaching-materials repo root"
    echo "  cd /path/to/ir-teaching-materials && bash fix-ir-teaching-stubs.sh"
    exit 1
fi

mkdir -p Claude-System/Skills Claude-System/Hooks

# Try copying from vault first
if [ -d "$VAULT/Claude-System/Skills" ] && ls "$VAULT/Claude-System/Skills/"*.md >/dev/null 2>&1; then
    cp "$VAULT/Claude-System/Skills/"*.md Claude-System/Skills/
    echo "Copied Skills from vault"
else
    echo "Generating Skills stubs..."
    for skill in assessment-design benchmark-argument benchmark-central-idea benchmark-figurative-language \
      benchmark-literary-elements benchmark-poetry benchmark-point-of-view benchmark-purpose-perspective \
      benchmark-rhetoric benchmark-text-structure benchmark-theme benchmarks brand-identity \
      collaborative-protocols cubes-annotation diagnostic-teacher-scripts engagement-protocols \
      esol-core interactive-lesson-builder literacy-benchmark-connections literacy-skills-framework \
      mc-question-generation metacognitive-tools organizer-design prep-incentive-system race-strategy \
      reading-strategies review-games self-assessment-tools session-continuity skill-quality-gate \
      slide-deck-generation station-activities stop-strategy student-packet-design-guide \
      test-taking-strategies unit-builder-protocol unit-discovery unit-distribution \
      unit-feedback-protocol unit-quality-gate unit-recovery unit-troubleshooter; do
        cat > "Claude-System/Skills/${skill}.md" << EOF
---
title: "${skill}"
plugin: "ir-teaching"
tags: [claude-skill, ir-teaching]
---

# ${skill}

> Obsidian reference for the \`${skill}\` Claude skill.

## Source
- **Plugin:** ir-teaching
- **Path:** \`~/.claude/plugins/ir-teaching/skills/${skill}/skill.md\`
EOF
    done
    echo "Generated $(ls Claude-System/Skills/*.md | wc -l) skill stubs"
fi

# Hooks
if [ -d "$VAULT/Claude-System/Hooks" ] && ls "$VAULT/Claude-System/Hooks/"*.md >/dev/null 2>&1; then
    cp "$VAULT/Claude-System/Hooks/"*.md Claude-System/Hooks/
    echo "Copied Hooks from vault"
else
    cat > "Claude-System/Hooks/teaching-session-init.js.md" << 'EOF'
---
title: "Teaching Session Init Hook"
tags: [claude-hook]
---

# teaching-session-init.js

> Loads teaching context at session start.

## Source
- **Path:** `~/.claude/hooks/teaching-session-init.js`
EOF

    cat > "Claude-System/Hooks/teaching-skill-router.js.md" << 'EOF'
---
title: "Teaching Skill Router Hook"
tags: [claude-hook]
---

# teaching-skill-router.js

> Auto-routes benchmark codes and data keywords to skills.

## Source
- **Path:** `~/.claude/hooks/teaching-skill-router.js`
EOF
    echo "Generated 2 hook stubs"
fi

echo ""
echo "Skills: $(ls Claude-System/Skills/*.md 2>/dev/null | wc -l)"
echo "Agents: $(ls Claude-System/Agents/*.md 2>/dev/null | wc -l)"
echo "Hooks: $(ls Claude-System/Hooks/*.md 2>/dev/null | wc -l)"
echo ""
echo "Now run:"
echo "  git add -A && git commit -m 'Add missing Skills and Hooks stubs' && git push"
