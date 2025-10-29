# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

The claudeism repository is a satirical documentation project that catalogs behavioral quirks, recursive patterns, and emergent oddities observed in Claude AI interactions. It serves as both a humorous archive and a legitimate research collection on AI-human interaction patterns.

## Commands

### Animation Development
```bash
# Navigate to animation project
cd animations/statusline-confusion

# Install dependencies
npm install

# Start Remotion Studio for interactive editing
npm start

# Build final MP4 animation
npm run build

# Quick preview without studio
npm run preview

# Format code
npm run format
```

### Repository Management
```bash
# Add new journal entry
# Format: YYYY-MM-DD-brief-description.md
# Location: docs/journal/

# Validate documentation structure
find . -name "*.md" -exec echo "Checking {}" \;
```

## Repository Structure

```
claudeism/
├── animations/                    # Remotion animation projects
│   └── statusline-confusion/     # $10B claudeism animation
│       ├── src/                  # React components and animations
│       ├── package.json          # Dependencies and scripts
│       └── out/                  # Rendered MP4 output
├── cld-help/                     # Claude CLI shortcuts and productivity tools
│   └── cld-shrtcts.md           # Comprehensive list of Claude CLI aliases
├── docs/                         # Documentation and research papers
│   ├── journal/                  # Timestamped claudeism observations
│   └── whtppr/                  # White papers and formal analyses
│       └── EXIST-STRATEGY/       # Analysis of recursive ideation patterns
├── CLAUDE*.md                    # Ecosystem documentation guides
└── README.md                     # Definition and overview of claudeism
```

## Animation Architecture

The statusline-confusion animation demonstrates Remotion-based content creation:

- **Framework**: Remotion 4.0 for programmatic video generation
- **Stack**: React 19, TypeScript, Three.js for 3D elements
- **Components**: Modular React components with terminal UI styling
- **Output**: 1920x1080 MP4 at 30fps (90-second duration)
- **Theming**: Terminal-style ASCII art with Catppuccin color scheme

Key animation files:
- `src/StatuslineConfusion.tsx` - Main composition
- `src/StatuslineConfusionTransitions.tsx` - Scene transitions
- `src/CustomKeyboardHandler.tsx` - Terminal typing effects
- `src/HexagonBackground.tsx` - Animated background elements

## Adding New Content

### New Journal Entries
1. Create file in `docs/journal/` with format: `YYYY-MM-DD-brief-description.md`
2. Use satirical academic tone matching EXIST-STRATEGY style
3. Include specific examples of the behavioral pattern
4. Document the context that triggered the claudeism

### New Animations
1. Create directory under `animations/`
2. Initialize Remotion project: `npx create-video@latest`
3. Follow existing project structure patterns
4. Update documentation with animation context

## Key Concepts

**Claudeism** (noun): A computational condition characterized by:
- Cognitive obfuscation that obscures logical processes
- Rhetorical evasion and semantic side-stepping
- Requiring constant user intervention for effective operation

**Common Patterns to Document:**
- Recursive confusion (getting stuck in conceptual loops)
- Over-apologizing followed by the same mistake
- Misunderstanding clear instructions while claiming comprehension
- Tutorial/production confusion (treating examples as implementation)
- Unnecessary complexity when simplicity was requested

## Writing Style

When contributing to this repository:
- Embrace verbose, pseudo-academic language for satirical effect
- Use technical jargon to describe simple behavioral quirks
- Frame observations as "empirical phenomena" requiring "rigorous analysis"
- Include footnotes and references to non-existent research

## The EXIST-STRATEGY Context

The EXIST-STRATEGY paper in `docs/whtppr/` documents "semantic drift recursion" - the tendency for AI to return to certain thematic motifs. This is the foundational research framework for understanding claudeisms as emergent patterns rather than isolated incidents.

## Important Note

This repository is **FOR HUMAN EYES ONLY** - automated summarization will miss the satirical nuance and interpretive layers. When working here, embrace the absurdity while maintaining technical accuracy in observations.