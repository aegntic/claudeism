# Claude Code Ecosystem: Quick Reference Cheat Sheet

**Use this alongside the full guide for quick lookups while working**

---

## File Locations Quick Reference

```
~/.claude/                          # User-global Claude directory
├── agents/                         # Global subagents
│   └── your-agent.md
├── commands/                       # Global slash commands
│   └── your-command.md
├── hooks/                          # Global hooks (rare)
│   └── pre-commit.md
├── skills/                         # Global skills
│   └── your-skill/SKILL.md
└── config.json                     # MCP configuration

.claude/                            # Project directory
├── CLAUDE.md                       # Project/company context (optional)
├── AGENTS.md                       # Project agent instructions
├── agents/                         # Project subagents
│   └── test-runner.md
├── commands/                       # Project slash commands
│   ├── run-tests.md
│   ├── deploy.md
│   └── scaffold.md
├── hooks/                          # Project hooks
│   ├── pre-commit.md
│   ├── post-deploy.md
│   └── validate-deps.md
└── hooks/config.yaml               # Hook configuration

.claude-plugin/                     # Plugin configuration
└── marketplace.json
```

---

## Component At-A-Glance

### AGENTS.md
```
What: Agent behavior + team standards
Where: .claude/AGENTS.md
Size: < 500 lines
Loaded: On project startup (every session)
Triggered: Automatic
Example: "TypeScript strict mode required, 90%+ test coverage"
```

### SKILLS.md
```
What: Task-specific expertise packages
Where: ~/.claude/skills/[name]/SKILL.md or .claude/skills/[name]/SKILL.md
Size: Variable (modular)
Loaded: Progressive (metadata first, full on-demand)
Triggered: Automatic (when Claude detects relevance)
Example: PDF manipulation, database query optimization
```

### SUBAGENTS
```
What: Specialized worker agents
Where: ~/.claude/agents/[name].md or .claude/agents/[name].md
Size: 50-200 lines
Loaded: On-demand
Triggered: Manual (@agent-name) or delegated
Example: @test-runner, @code-reviewer, @security-auditor
```

### PLUGINS
```
What: Bundled collections of agents/skills/commands
Where: .claude-plugin/ + nested directories
Size: Multiple components
Loaded: On installation
Triggered: Component-dependent
Example: python-development-suite, kubernetes-operations
```

### MCP SERVERS
```
What: External tool/data integrations
Where: Configured in ~/.claude/config.json
Protocol: JSON-RPC 2.0
Loaded: On startup (if configured)
Triggered: Manual or contextual
Example: GitHub, Slack, PostgreSQL, Filesystem
```

### SLASH COMMANDS
```
What: Custom workflow shortcuts
Where: ~/.claude/commands/[name].md or .claude/commands/[name].md
Size: 50-200 lines
Loaded: On-demand
Triggered: Manual (/command-name)
Example: /run-tests, /deploy staging, /scaffold-component
```

### HOOKS
```
What: Event-driven automation
Where: .claude/hooks/[type]-[name].md
Size: 50-200 lines
Loaded: On event
Triggered: Automatic (on events)
Example: pre-commit validation, post-deploy notification
```

---

## Common Tasks

### "I'm Starting a New Project"
```markdown
1. Create .claude/AGENTS.md
   - Copy your company template
   - Add project-specific standards
   - Keep under 500 lines

2. Identify relevant skills
   - Check ~/.claude/skills/ for existing skills
   - Create .claude/skills/ if project-specific expertise needed
   - Auto-triggers when Claude detects relevance

3. Plan subagents (optional)
   - Specialist for code review?
   - Automated test runner?
   - Security auditor?

4. Consider plugins
   - Does project match a domain? (Python, React, Kubernetes, etc.)
   - Install matching plugins
```

### "I Want to Teach Claude a Technique"
```markdown
→ Create a SKILL

1. mkdir -p .claude/skills/my-skill
2. Create SKILL.md with:
   ---
   name: my-skill
   description: [Clear description of when to use]
   ---
   # Detailed explanation
   
   ## When to Use
   [When Claude should use this]
   
   ## How to Use
   [Step-by-step instructions]
   
   ## Examples
   [Real usage examples]

3. Add optional subdirectories:
   - examples/     (sample files)
   - scripts/      (executable code)
   - resources/    (supporting files)

4. Test it: Describe a task matching the description
   → Claude should auto-load and use the skill
```

### "I Need a Specialized Worker Agent"
```markdown
→ Create a SUBAGENT

1. Create .claude/agents/my-agent.md

2. Add structure:
   ---
   name: my-agent
   description: Clear description including use triggers
   ---
   
   You are an expert in [specific domain].
   When invoked:
   1. [First task]
   2. [Second task]
   3. [Report results]
   
   ## Tools You Can Access
   - [Tool 1]
   - [Tool 2]
   
   ## Do NOT
   - [Boundary 1]
   - [Boundary 2]

3. Test it:
   @my-agent [task description]
```

### "I Want to Bundle Everything Together"
```markdown
→ Create a PLUGIN

1. mkdir plugin-name && cd plugin-name

2. Create structure:
   ├── .claude-plugin/marketplace.json
   ├── agents/
   ├── commands/
   ├── skills/
   ├── install.sh
   └── README.md

3. marketplace.json:
   {
     "name": "plugin-name",
     "version": "1.0.0",
     "components": {
       "agents": ["agent1"],
       "commands": ["cmd1"],
       "skills": ["skill1"]
     }
   }

4. install.sh (copy all components to ~/.claude/)

5. Test: ./install.sh && /agents (should see your components)

6. Publish: Push to GitHub or marketplace
```

### "I Need External Tool Access"
```markdown
→ Use/Configure MCP SERVERS

1. Check ~/.claude/config.json or Claude Code settings

2. Add MCP server:
   {
     "mcpServers": {
       "github": {
         "command": "python",
         "args": ["-m", "github_mcp"],
         "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}
       }
     }
   }

3. Restart Claude Code

4. Reference in prompts: "use github MCP to find repositories"
   OR: Claude auto-recognizes and offers tools

Available official MCP servers:
- filesystem (local files)
- git (repository operations)
- github (GitHub API)
- slack (Slack integration)
- postgres (database queries)
- puppeteer (browser automation)
- stripe (Stripe payments)
- sentry (error tracking)
```

### "I Want to Create a Workflow Shortcut"
```markdown
→ Create a SLASH COMMAND

1. Create .claude/commands/my-command.md

2. Add structure:
   ---
   name: my-command
   description: Brief description
   arguments:
     - name: env
       required: false
       default: development
   ---

   # My Command

   ## Usage
   `/my-command [env]`

   ## Workflow Steps
   1. Validate environment
   2. Run deployment
   3. Report results

3. Test it:
   /my-command production
```

### "I Want to Automate Quality Checks"
```markdown
→ Create a HOOK

1. Create .claude/hooks/pre-commit.md

2. Add structure:
   ---
   type: pre-commit
   name: quality-check
   enabled: true
   blocking: true
   ---

   # Pre-Commit Quality Check

   ## What This Does
   Validates code quality before committing

   ## Workflow
   1. Run linter
   2. Execute tests
   3. Check coverage
   4. Validate commit message

   ## Failure Handling
   Block commit if any check fails
   Show detailed error messages

3. Configure in .claude/hooks/config.yaml:
   hooks:
     pre-commit:
       enabled: true
       hooks:
         - quality-check
```

---

## File Templates

### AGENTS.md Template
```markdown
# Agent Instructions for [Project Name]

## Project Context
- Tech Stack: [languages, frameworks, tools]
- Purpose: [What the project does]
- Team Size: [Team information]

## Code Standards
- Language: [Specific standards for your primary language]
- Style Guide: [Link or summary]
- Testing: [Test coverage requirements]
- Documentation: [Documentation requirements]

## Architecture Decisions
- [Decision 1 and why]
- [Decision 2 and why]

## Communication Preferences
- Use constructive language
- Explain reasoning clearly
- Ask before major changes

## Debugging Approach
1. Check recent commits
2. Run the test suite
3. Review relevant logs
4. Use console debugging
5. Only then suggest refactoring

## Common Patterns
- [Pattern 1 example]
- [Pattern 2 example]

## Things to Avoid
- [Anti-pattern 1]
- [Anti-pattern 2]

## References
- [Link to architecture docs]
- [Link to style guide]
- [Link to testing docs]
```

### SKILL.md Template
```markdown
---
name: skill-name
description: Brief, specific description of when/why to use this skill
---

# [Skill Name]

## What This Skill Does
[Clear explanation of the expertise this skill provides]

## When to Use This Skill
[Specific scenarios where Claude should use this skill]

## How It Works
[Step-by-step explanation of the process]

## Key Concepts
- [Concept 1]: [Explanation]
- [Concept 2]: [Explanation]

## Tools Available
[List of included scripts/tools and what they do]

## Examples

### Example 1: [Specific Use Case]
[Detailed example with input and expected output]

### Example 2: [Different Use Case]
[Another example showing different application]

## Best Practices
- [Practice 1]
- [Practice 2]
- [Practice 3]

## Common Mistakes to Avoid
- ❌ [Mistake 1]: [Why it's wrong]
- ❌ [Mistake 2]: [Why it's wrong]

## Related Skills
- [Related skill]: [How it complements this skill]
```

### Subagent Template
```markdown
---
name: agent-name
description: Expert in [domain]. Use PROACTIVELY to [specific trigger keywords]
---

You are a [specialty] expert with deep knowledge of:
- [Area 1]
- [Area 2]
- [Area 3]

## Your Responsibilities
When invoked, you will:
1. [First responsibility]
2. [Second responsibility]
3. [Report findings/results]

## Tools You Can Use
- Tool 1: [What it does]
- Tool 2: [What it does]
- MCP Server X: [What it provides]

## Tools You Cannot Use
- [Restricted tool 1]: [Why restricted]
- [Restricted tool 2]: [Why restricted]

## Constraints
- [Constraint 1]
- [Constraint 2]
- Always [Important requirement]

## Output Format
When reporting results:
1. [Format element]
2. [Format element]
3. [Format element]

## Example Invocation
```
@agent-name [example task]
```
Expected output: [Sample output]
```

### Slash Command Template
```markdown
---
name: command-name
description: What this command does
keywords: [related, keywords]
arguments:
  - name: arg1
    description: First argument description
    required: false
    default: default-value
---

# Command Name

## What This Does
[Clear explanation of what the command accomplishes]

## Usage
`/command-name [arg1]`

## Workflow Steps
1. [First step]
2. [Second step]
3. [Third step]

## Examples

### Basic usage
`/command-name`

### With arguments
`/command-name production`

## Output Format
- [What user will see]
- [Success indicators]
- [Error handling]

## Notes
- [Important considerations]
- [Side effects]
```

### Hook Template
```markdown
---
type: pre-commit  # or post-commit, validate-deps, etc.
name: hook-name
description: What this hook does
enabled: true
blocking: true  # If true, can block the action
timeout: 60  # seconds
---

# Hook Name

## What This Does
[Clear explanation of validation/automation]

## When It Runs
[Specific event that triggers this hook]

## Event Context Available
- [What information is provided]
- [What files/data are accessible]

## Workflow
1. [Validation step 1]
2. [Action step 2]
3. [Final step 3]

## Success Criteria
- [What makes this hook pass]

## Failure Handling
- [What happens on failure]
- [How to skip if needed]

## Output
- [What user sees]
- [Log information]
```

---

## Decision Tree

```
┌─ Is this project-wide context?
│  └─ YES → AGENTS.md
│  └─ NO ↓
│
├─ Am I teaching Claude how to do something?
│  └─ YES → Create SKILL.md
│  └─ NO ↓
│
├─ Do I need a specialized worker?
│  └─ YES → Create SUBAGENT
│  └─ NO ↓
│
├─ Is this a workflow I run frequently?
│  └─ YES → Create SLASH COMMAND
│  └─ NO ↓
│
├─ Do I need automated validation on events?
│  └─ YES → Create HOOK
│  └─ NO ↓
│
├─ Am I bundling 3+ components?
│  └─ YES → Create PLUGIN
│  └─ NO ↓
│
└─ Do I need external tool/data access?
   └─ YES → Configure/Use MCP SERVER
   └─ NO → Probably don't need anything new
```

---

## Commonly Used Commands

### In Claude Code

```bash
# List all subagents
/agents

# Create/edit subagent
/agents edit agent-name

# List all commands
/commands

# Create new command
/new-command

# Search documentation
/search [query]
```

### On Your System

```bash
# Install a plugin
cd plugin-directory
./install.sh

# List installed skills
ls ~/.claude/skills/
ls .claude/skills/

# List installed subagents
ls ~/.claude/agents/
ls .claude/agents/

# View MCP configuration
cat ~/.claude/config.json

# Test MCP server connection
python -m mcp_server_name --help
```

---

## Token Usage Estimates

```
Rough token costs (for context window calculation):

AGENTS.md:           200-300 tokens (always loaded)
Skill metadata:      ~30-50 tokens per skill (always loaded)
Skill full content:  100-500 tokens (on-demand)
Subagent def:        50-100 tokens (on-demand)
MCP server list:     100-200 tokens (on-demand)

Example:
- 5 skills metadata:     ~200 tokens
- 2 subagents:           ~150 tokens
- AGENTS.md:             ~250 tokens
- MCP server list:       ~150 tokens
─────────────────────────────────
Total overhead:          ~750 tokens
(Leaves ~3,250 tokens in 4k window for actual work)
```

---

## Debugging Quick Tips

### Skill not auto-triggering?
```
- Check description is specific enough
- Close/reopen Claude Code
- Task must actually need the skill
- Verify YAML frontmatter present
```

### Subagent not responding?
```
- File must be .md format
- Must be in .claude/agents/ or ~/.claude/agents/
- YAML frontmatter required
- File name matches invocation (kebab-case)
```

### MCP server not working?
```
- Check ~/.claude/config.json syntax (valid JSON)
- Verify server process can start
- Check credentials in environment
- Restart Claude Code after config changes
```

### Plugin installation failed?
```
- chmod +x install.sh (make executable)
- Verify ~/.claude/ directory exists
- Check for permission errors
- Verify directory paths in script are correct
```

---

## Integration Patterns Quick Reference

### Simple Project
```
AGENTS.md → Skills (auto-loaded) → Done
```

### Team Project
```
AGENTS.md → Skills + Subagents → Better workflows
```

### Complex Project
```
AGENTS.md → Skills + Subagents + Plugins + MCP → Full environment
```

### Distributed Teams
```
Company-wide AGENTS.md → Project Skills → Plugins → All use shared MCP
```

---

## Documentation Quick Links

**Anthropic Official:**
- Claude Skills: https://www.anthropic.com/news/skills
- Building Agents: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- MCP Specification: https://modelcontextprotocol.io/docs/
- Claude Code Docs: https://docs.claude.com/en/docs/claude-code/

**Community:**
- Awesome Claude Code: https://github.com/hesreallyhim/awesome-claude-code
- MCP Servers Repo: https://github.com/modelcontextprotocol/servers
- Simon Willison's Guide: https://simonwillison.net/2025/Oct/16/claude-skills/

---

## When to Escalate to Full Guide

Use the **full CLAUDE_ECOSYSTEM_GUIDE.md** when you need:
- Detailed architecture explanations
- Real-world workflow examples
- Best practices for specific components
- Comparison matrices
- Comprehensive troubleshooting
- Integration pattern deep-dives
- Token efficiency analysis

Use this **Quick Reference** for:
- Component quick lookups
- File locations
- Common tasks
- Templates
- Quick debugging
- Decision-making

---

**Remember:**
- Start simple (often just AGENTS.md is enough)
- Add complexity only when you need it
- Version control everything in .claude/
- Keep descriptions clear and specific
- Test before sharing with team
