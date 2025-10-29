# Claude Code Ecosystem: Complete Architecture Guide

**Last Updated:** October 29, 2025  
**Purpose:** Comprehensive reference for understanding how AGENTS.md, SKILLS.md, Plugins, Subagents, and MCP work together

---

## Table of Contents

1. [Quick Start Reference](#quick-start-reference)
2. [Core Components Overview](#core-components-overview)
3. [Component Architecture](#component-architecture)
4. [Detailed Component Breakdown](#detailed-component-breakdown)
5. [Integration Patterns](#integration-patterns)
6. [Best Practices](#best-practices)
7. [Comparison Matrix](#comparison-matrix)
8. [Real-World Workflows](#real-world-workflows)

---

## Quick Start Reference

### Component Roles at a Glance

| Component | Purpose | Where Stored | Auto-Triggered | Scope |
|-----------|---------|--------------|-----------------|-------|
| **CLAUDE.md** | Project-level context and instructions | `.claude/CLAUDE.md` | Yes, on startup | Project |
| **AGENTS.md** | Agent behavior customization | `.claude/AGENTS.md` | Yes, contextually | Project |
| **SKILLS** | Task-specific expertise packages | `~/.claude/skills/` or `.claude/skills/` | Yes, when relevant | Global or Project |
| **Subagents** | Specialized worker agents | `.claude/agents/` or `~/.claude/agents/` | Manual or delegated | Project or User |
| **Plugins** | Bundled agent ecosystems | `.claude-plugin/` | Manual installation | Project |
| **MCP Servers** | External tool/data integrations | Configured separately | When called | External |

---

## Core Components Overview

### 1. AGENTS.md (Project Agent Configuration)
**What It Is:** Your project's agent personality and capability baseline  
**File Location:** `.claude/AGENTS.md` in your project root  
**Scope:** Project-specific (version control friendly)  
**When It Runs:** Automatically loaded on project startup  

**Key Characteristics:**
- Single, master agent instructions
- Loaded into every Claude Code session for your project
- Cannot be auto-invoked by Claude (unlike Skills)
- Foundation for all other agent behaviors

**What Goes Here:**
- Project goals and philosophy
- Your coding standards and preferences
- Team workflows and communication style
- Project-specific architectural decisions
- Debug and troubleshooting guidelines

**Example Structure:**
```
# Agent Instructions for [ProjectName]

You are the primary agent for this TypeScript/React project.

## Project Context
- Building a real-time collaboration tool
- Strict adherence to TypeScript strict mode
- All components must be accessible (WCAG AA)

## Communication Style
- Use constructive terminology
- Explain decisions clearly
- Ask clarifying questions before major changes

## Code Standards
- Use conventional commits
- 80% test coverage minimum
- ESLint configuration in .eslintrc.json

## Debugging Approach
1. First, check recent changes
2. Run the test suite
3. Use console logging for tracing
4. Only then suggest refactoring
```

### 2. SKILLS (Agent Expertise Packages)
**What They Are:** Specialized knowledge modules Claude auto-loads when relevant  
**File Location:** `~/.claude/skills/` (user-global) or `.claude/skills/` (project)  
**Scope:** Both global and project-specific  
**When They Run:** Automatically, when Claude detects they're relevant to the task  

**Key Characteristics:**
- Modular and composable
- Progressive disclosure (metadata loads before full content)
- Execute code (Python, Node.js, etc.)
- Model-controlled activation (Claude decides when to use them)
- Work across ALL Claude products (web, API, Claude Code)

**Required Structure:**
```
your-skill/
├── SKILL.md              # Markdown with YAML frontmatter
├── examples/             # Usage examples
├── scripts/              # Executable code
└── resources/            # Supporting files
```

**SKILL.md Format:**
```yaml
---
name: pdf-manipulation
description: Create, edit, and fill PDF forms with precise formatting
---

# PDF Manipulation Skill

## When to Use This Skill
- Creating or editing PDF documents
- Filling form fields
- Extracting data from PDFs
- Merging or splitting PDFs

## Available Tools
- `read_pdf.py`: Extract PDF structure and content
- `create_pdf.py`: Generate PDFs from scratch
- `fill_forms.py`: Populate form fields programmatically

## Best Practices
1. Always validate form structure before filling
2. Test with sample PDFs first
3. Preserve original formatting where possible

## Examples
[Detailed examples of how to use each tool]
```

**Progressive Disclosure in Skills:**
1. **Metadata Level** (always loaded in system prompt):
   - Name and description
   - ~30-50 tokens per skill

2. **Detailed Level** (loaded on-demand):
   - Full SKILL.md content
   - Scripts and examples
   - Only loaded when Claude recognizes relevance

### 3. Subagents (Specialized Worker Agents)
**What They Are:** Focused agents you delegate specific tasks to  
**File Location:** `.claude/agents/` (project) or `~/.claude/agents/` (user-global)  
**Scope:** Project-specific or user-global  
**When They Run:** Manual invocation or delegated by main agent  

**Key Characteristics:**
- Independent context window (prevents main context pollution)
- Explicit tool and MCP server access control
- Useful for parallelization
- Can be proactively triggered with keywords

**Creating a Subagent:**
```yaml
---
name: test-runner
description: Use PROACTIVELY to run tests and fix failures
---

You are a testing automation expert. When you see code changes:
1. Run appropriate tests proactively
2. Analyze any failures
3. Fix issues while preserving test intent
4. Report results to main agent

## Tools You Can Use
- Run bash commands
- Execute test frameworks
- Access project files

## Do NOT
- Make architectural changes
- Modify non-test files unless fixing them to pass tests
- Commit changes without approval
```

**Invoking a Subagent:**
- Type: `@test-runner` or `@subagent-name`
- Use slash command: `/agents` to list/manage all subagents
- Through Task tool for delegated work

### 4. Plugins (Bundled Extension Packages)
**What They Are:** Cohesive bundles of agents, commands, and skills distributed as units  
**File Location:** `.claude-plugin/` configuration + nested agent/command/skill directories  
**Scope:** Project-specific, installable from marketplaces  
**When They Run:** On manual installation, component-dependent on invocation  

**Key Characteristics:**
- Bundle multiple components (agents, commands, skills, MCP servers)
- Single, focused purpose
- Minimal token overhead (progressive loading)
- Installable via install scripts
- Version controlled within project

**Typical Plugin Structure:**
```
plugin-name/
├── .claude-plugin/
│   └── marketplace.json       # Plugin metadata
├── agents/
│   ├── architect-agent.md
│   └── reviewer-agent.md
├── commands/
│   ├── scaffold.md
│   └── validate.md
├── skills/
│   ├── database-schema/SKILL.md
│   └── performance-tuning/SKILL.md
├── install.sh               # Installation script
└── README.md
```

**marketplace.json Example:**
```json
{
  "name": "python-development",
  "version": "1.0.0",
  "description": "Complete Python development environment",
  "components": {
    "agents": ["python-expert", "test-automator"],
    "commands": ["scaffold-project", "run-tests"],
    "skills": ["async-patterns", "testing-best-practices"]
  }
}
```

**Installation:**
```bash
# Clone or download plugin
git clone https://github.com/user/plugin-name
cd plugin-name

# Run install script (copies agents, commands, skills to proper locations)
./install.sh

# Verify installation
/agents
```

### 5. MCP Servers (External Tool/Data Integrations)
**What They Are:** Standardized protocol servers that provide tools, resources, and prompts to Claude  
**Configuration:** Defined in Claude desktop config or Claude Code settings  
**Scope:** External (can be local or remote)  
**When They Run:** When explicitly called or when Claude determines they're needed  

**Key Characteristics:**
- Open, standardized protocol (like USB for AI)
- Client-server architecture
- Support Tools, Resources, and Prompts
- Multiple transport options (stdio, HTTP, SSE)
- Reduces "M×N integration problem"

**MCP Architecture:**
```
┌─────────────────────────────────────────┐
│  Host Application (Claude Code, IDE)    │
├─────────────────────────────────────────┤
│  MCP Client 1      MCP Client 2         │ (1:1 relationship)
├─────────────────────────────────────────┤
│        ↓                    ↓            │
├─────────────────────────────────────────┤
│  MCP Server A        MCP Server B       │ (External)
│  (Filesystem,        (GitHub,          │
│   Git)               Slack, etc.)       │
└─────────────────────────────────────────┘
```

**Available Official MCP Servers (from Anthropic):**
- **filesystem**: Read/write local files
- **git**: Git repository operations
- **github**: GitHub API access
- **slack**: Slack workspace integration
- **postgres**: PostgreSQL database access
- **puppeteer**: Browser automation
- **stripe**: Stripe API integration
- **sentry**: Error tracking

**Community MCP Servers:**
- Context7: Versioned API documentation
- Brave-Search: Web search capabilities
- Custom integrations via SDKs (Python, TypeScript, Java, C#, Ruby)

**Configuring MCP in Claude Code:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "node",
      "args": ["/path/to/filesystem/index.js"]
    },
    "github": {
      "command": "python",
      "args": ["-m", "mcp_github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Using MCP in Claude Code:**
- Direct reference: Claude automatically lists available tools from connected MCP servers
- Explicit mention: `use github-search MCP to find repositories`
- Through subagents: Subagents inherit or have specific MCP access

### 6. Slash Commands (Custom Workflows)
**What They Are:** User-defined command shortcuts for frequently-run workflows
**File Location:** `.claude/commands/` (project) or `~/.claude/commands/` (user-global)
**Scope:** Project-specific or user-global
**When They Run:** Manual invocation via `/command-name`

**Key Characteristics:**
- Quick access via `/` prefix
- Can execute multi-step workflows
- Pass arguments for customization
- No separate context (runs in main Claude session)
- Version control friendly
- Composable with other components

**Creating a Slash Command:**
```yaml
---
name: run-tests
description: Execute test suite and generate coverage report
keywords: [testing, ci, coverage]
arguments:
  - name: suite
    description: Test suite to run (unit, integration, e2e)
    required: false
    default: all
---

# Run Tests Command

## What This Does
Runs the project test suite with coverage reporting and failure analysis.

## Usage
`/run-tests [suite]`

## Workflow Steps
1. Check for uncommitted changes
2. Run specified test suite
3. Generate coverage report
4. Analyze failures (if any)
5. Suggest fixes for failed tests
6. Display summary

## Examples

### Run all tests
`/run-tests`

### Run specific suite
`/run-tests unit`

## Output Format
- Test results summary
- Coverage percentage
- Failed test details (if any)
- Suggested fixes
```

**Slash Commands vs Other Components:**

| Aspect | Slash Command | Subagent | Skill | Plugin |
|--------|---------------|----------|-------|--------|
| **Invocation** | `/command` | `@agent` | Auto | Install |
| **Context** | Main session | Isolated | Main | Varies |
| **Best For** | Workflows | Specialists | Knowledge | Bundles |
| **Arguments** | Yes | Via prompt | No | N/A |
| **Multi-step** | Yes | Yes | No | Varies |
| **Token Cost** | Per use | Per use | Auto | Varies |

**Common Slash Command Patterns:**

1. **Testing Workflows:**
```yaml
/run-tests [suite]
/test-coverage
/fix-failing-tests
```

2. **Code Generation:**
```yaml
/scaffold-component [name] [type]
/generate-api-endpoint [resource]
/create-migration [description]
```

3. **Project Management:**
```yaml
/create-ticket [title]
/update-docs
/changelog [version]
```

4. **Deployment:**
```yaml
/deploy [environment]
/rollback [version]
/check-deployment-status
```

**Best Practices for Slash Commands:**

✅ **DO:**
- Create commands for workflows you run weekly or more
- Use descriptive names (kebab-case)
- Document expected arguments clearly
- Include examples in the command definition
- Make commands idempotent when possible
- Handle errors gracefully

❌ **DON'T:**
- Duplicate subagent functionality
- Create commands for one-off tasks
- Make commands too generic ("do-stuff")
- Forget to document side effects
- Hardcode environment-specific values

**Slash Command Distribution:**

1. **Project Commands** (`.claude/commands/`)
   - Shared with team via git
   - Project-specific workflows
   - Examples: deployment, testing, scaffolding

2. **User Commands** (`~/.claude/commands/`)
   - Personal productivity tools
   - Cross-project utilities
   - Examples: note-taking, time tracking

3. **Plugin Commands**
   - Bundled with plugins
   - Domain-specific workflows
   - Examples: python-plugin includes `/create-python-package`

### 7. Hooks (Event-Driven Automation)
**What They Are:** Automated actions triggered by specific events in Claude Code
**File Location:** `.claude/hooks/` directory
**Scope:** Project-specific
**When They Run:** Automatically on specific events

**Key Characteristics:**
- Event-driven (no manual invocation)
- Run before/after specific actions
- Can validate, modify, or enhance workflows
- Access to event context
- Can prevent actions (validation hooks)

**Available Hook Types:**

1. **Pre-Action Hooks** (run before action)
   - `pre-commit` - Before committing changes
   - `pre-deploy` - Before deployment
   - `pre-generate` - Before code generation

2. **Post-Action Hooks** (run after action)
   - `post-commit` - After successful commit
   - `post-deploy` - After successful deployment
   - `post-generate` - After code generation

3. **Validation Hooks** (can block actions)
   - `validate-commit` - Validate commit message/content
   - `validate-config` - Validate configuration changes
   - `validate-deps` - Validate dependency updates

**Creating a Hook:**
```yaml
---
type: pre-commit
name: lint-and-test
description: Run linting and tests before commit
enabled: true
blocking: true  # If true, commit fails if hook fails
---

# Pre-Commit Validation

## What This Does
Ensures code quality before committing by:
1. Running linter
2. Executing test suite
3. Checking for TODO/FIXME comments
4. Validating commit message format

## Event Context Available
- Changed files list
- Commit message
- Branch name
- Author information

## Workflow
1. Run ESLint on changed files
2. Execute related tests
3. Check for debugging code (console.log, debugger)
4. Validate conventional commit format
5. Block commit if any check fails

## Output
- Lint results
- Test results
- List of issues found
- Suggestions for fixes
```

**Hook Event Context:**

Hooks receive context about the triggering event:

```javascript
{
  event: 'pre-commit',
  timestamp: '2025-10-29T10:30:00Z',
  files: {
    added: ['src/new-file.js'],
    modified: ['src/existing.js'],
    deleted: ['src/old-file.js']
  },
  commit: {
    message: 'feat: add new feature',
    branch: 'feature/new-feature',
    author: 'developer@example.com'
  }
}
```

**Common Hook Patterns:**

1. **Quality Gates:**
```yaml
pre-commit:
  - lint-code
  - run-tests
  - check-coverage
  - validate-commit-message
```

2. **Documentation:**
```yaml
post-generate:
  - update-readme
  - generate-api-docs
  - update-changelog
```

3. **Security:**
```yaml
validate-deps:
  - check-vulnerabilities
  - validate-licenses
  - scan-secrets
```

4. **Deployment:**
```yaml
pre-deploy:
  - run-integration-tests
  - check-env-config
  - verify-migrations

post-deploy:
  - smoke-test
  - notify-team
  - update-status-page
```

**Best Practices for Hooks:**

✅ **DO:**
- Keep hooks fast (< 30 seconds)
- Make hooks idempotent
- Provide clear error messages
- Allow hooks to be skipped (emergency deploys)
- Log hook execution for debugging
- Test hooks before enabling

❌ **DON'T:**
- Make hooks that take minutes to run
- Perform destructive operations without confirmation
- Block critical workflows with flaky checks
- Forget to handle hook failures gracefully
- Create circular dependencies between hooks

**Hook Configuration File (.claude/hooks/config.yaml):**
```yaml
hooks:
  enabled: true

  pre-commit:
    enabled: true
    timeout: 60  # seconds
    parallel: false
    hooks:
      - lint-and-test
      - check-secrets

  post-commit:
    enabled: true
    hooks:
      - update-docs

  validate-deps:
    enabled: true
    blocking: true
    hooks:
      - security-scan
      - license-check
```

**Hooks vs Slash Commands:**

| Aspect | Hooks | Slash Commands |
|--------|-------|----------------|
| **Trigger** | Automatic (events) | Manual (`/cmd`) |
| **When** | On specific actions | On demand |
| **Purpose** | Validation/automation | Workflow shortcuts |
| **Blocking** | Can block actions | No |
| **Arguments** | Event context | User-provided |
| **Best For** | Quality gates | Frequent tasks |

---

## Component Architecture

### The Hierarchy and Relationships

```
┌────────────────────────────────────────────────────────────────────────┐
│                    CLAUDE CODE PROJECT                                 │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │ CLAUDE.md (Project Foundation)                                   │ │
│  │ Sets baseline capabilities, style, preferences                   │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                              ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │ AGENTS.md (Agent Personality & Standards)                        │ │
│  │ Project-specific agent behavior & coding standards               │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                         ↙              ↖                               │
│  ┌─────────────────────────────    ──────────────────────────────┐    │
│  │ SKILLS (Expertise)          │    │ SUBAGENTS (Workers)        │    │
│  │ • Auto-triggered            │    │ • Manual delegation        │    │
│  │ • Modular                   │    │ • Isolated context         │    │
│  │ • Composable                │    │ • Task-specific            │    │
│  └─────────────────────────────┘    └────────────────────────────┘    │
│           ▼                                   ▼                        │
│  ┌─────────────────────────────    ──────────────────────────────┐    │
│  │ SLASH COMMANDS              │    │ HOOKS                      │    │
│  │ • Manual workflows          │    │ • Event-driven             │    │
│  │ • /command invocation       │    │ • Auto-triggered           │    │
│  │ • Can pass arguments        │    │ • Validation/automation    │    │
│  └─────────────────────────────┘    └────────────────────────────┘    │
│                              ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │ PLUGINS (Feature Bundles)                                        │ │
│  │ Organized collections of agents, skills, commands, hooks         │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                              ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │ MCP SERVERS (External Tools & Data)                             │ │
│  │ Access external APIs, databases, tools                          │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Information Flow

**Task Request → Resolution Path:**

1. **Task Arrives in Claude Code**
   ↓
2. **CLAUDE.md + AGENTS.md Loaded** (foundational context)
   ↓
3. **Skills Evaluated** (relevant skills auto-loaded)
   ↓
4. **Subagents Considered** (if task matches a subagent's expertise)
   ↓
5. **MCP Servers Queried** (if external data/tools needed)
   ↓
6. **Plugin Components Activated** (if using plugin-based workflow)
   ↓
7. **Execution & Result Return**

---

## Detailed Component Breakdown

### AGENTS.md: Deep Dive

**When to Create/Update:**
- Setting up a new project
- Changing team standards
- Introducing new architectural patterns
- Creating onboarding for new team members

**What NOT to Put Here:**
- Task-specific instructions (use SKILLS.md)
- Temporary debugging notes (use slash commands)
- External tool configurations (use MCP)

**Anti-Patterns to Avoid:**
```markdown
❌ WRONG:
# Too generic, won't help Claude understand your project
You are a helpful coding assistant. Help with any task.

❌ WRONG:
# Too long - loads on every session, wastes tokens
[500-line comprehensive guide to everything...]

✅ CORRECT:
# Specific, token-efficient guidance
## Project: Real-Time Analytics Dashboard

### Tech Stack
- React 18, TypeScript, Vite
- Node.js backend with Express
- PostgreSQL with migrations

### Key Decisions
- Server-side rendering for initial load
- Client-side caching for performance
- No external UI libraries (custom styling)

### Code Review Criteria
- 90%+ TypeScript coverage (no `any`)
- Accessibility: WCAG AA minimum
- Performance: Lighthouse 90+ on all metrics
```

### SKILLS.md: Deep Dive

**Skill Lifecycle:**

1. **Discovery Phase** (Claude sees task description)
   - Reads skill name and description from metadata
   - Decides if skill might be relevant

2. **Loading Phase** (Claude decides skill is needed)
   - Reads full SKILL.md file
   - Examines examples
   - Prepares to use available scripts

3. **Execution Phase** (Claude invokes skill)
   - Calls available scripts/tools
   - Processes results
   - Returns to user with enhanced capabilities

4. **Memory Phase** (Within conversation)
   - Skill remains in context for this session
   - Can be referenced in follow-up tasks
   - Automatically unloaded when session ends

**Token Efficiency Pattern:**
```
Metadata (always loaded):     30 tokens
├─ name: "pdf-creation"
└─ description: "Create professional PDFs..."

Full Content (on-demand):     200+ tokens
├─ Detailed instructions
├─ Examples
└─ Scripts

Total for 50 skills:          ~1,500 tokens + 10,000 on-demand
(Compared to 50,000+ if all were always loaded)
```

**Skill Distribution Methods:**

1. **Local User Skills**
   ```
   ~/.claude/skills/
   ├── pdf-creation/SKILL.md
   ├── database-analysis/SKILL.md
   └── test-automation/SKILL.md
   ```
   - Shared across all projects
   - Personal productivity tools

2. **Project Skills**
   ```
   .claude/skills/
   ├── project-standards/SKILL.md
   ├── deployment-process/SKILL.md
   └── qa-checklist/SKILL.md
   ```
   - Shared with team via git
   - Project-specific expertise

3. **Plugin Distribution**
   - Installed via marketplace
   - Bundled with other components
   - Easy versioning and updates

### Subagents: Deep Dive

**When to Create a Subagent:**

| Use Case | Why Subagent |
|----------|-------------|
| Long-running tests | Isolate from main context |
| Web scraping/searching | Dedicated resource gathering |
| Security auditing | Specialized expertise + isolation |
| Parallel code reviews | Multiple aspects simultaneously |
| Documentation generation | Consistent formatting |

**Subagent vs Main Agent:**

| Aspect | Main Agent | Subagent |
|--------|-----------|----------|
| **Context Window** | Full project context | Clean slate per invocation |
| **Latency** | Lower (existing context) | Higher (gather context) |
| **Tool Access** | All available tools | Configurable, limited access |
| **When Used** | Always running | On-demand delegation |
| **Best For** | Orchestration, decisions | Specialized tasks |

**Subagent Configuration:**

```yaml
---
name: security-auditor
description: Use PROACTIVELY to audit new code for security vulnerabilities
keywords:
  - security
  - vulnerability
  - authentication
  - encryption
---

You are a security-focused code reviewer with expertise in:
- OWASP Top 10
- Node.js/Express security patterns
- Database query sanitization
- Authentication/authorization

When invoked:
1. Scan code for common vulnerabilities
2. Check dependencies for known CVEs
3. Validate authentication flows
4. Report findings with severity levels
5. Suggest fixes with examples

## Tools You Can Access
- GitHub MCP (for dependency checking)
- Filesystem access
- Web search for CVE database

## Do NOT
- Make breaking changes to application logic
- Remove functionality without approval
- Change architectural patterns
```

**Proactive Trigger Keywords:**
Include phrases in description to encourage Claude to use the subagent:
- "use PROACTIVELY"
- "MUST BE USED for"
- "automatically when"

**Invocation Methods:**

```bash
# Manual invocation
@security-auditor

# Via slash command
/agents              # List all subagents
/agents edit security-auditor

# Programmatic delegation
[Use @security-auditor to audit this function]
```

### Plugins: Deep Dive

**When to Create a Plugin:**

- Bundling 3+ related agents/skills/commands
- Sharing complete workflows with teams
- Publishing to marketplace
- Complex, multi-feature extensions

**Plugin Development Workflow:**

1. **Create directory structure:**
```bash
mkdir plugin-name
cd plugin-name
mkdir -p agents commands skills .claude-plugin
```

2. **Write agents:** `.md` files with agent definitions

3. **Write commands:** `.md` files with slash commands

4. **Write skills:** Skill directories with SKILL.md

5. **Create marketplace.json:**
```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "author": "Your Name",
  "description": "What this plugin does",
  "components": {
    "agents": ["agent1", "agent2"],
    "commands": ["cmd1", "cmd2"],
    "skills": ["skill1", "skill2"]
  }
}
```

6. **Write install script:**
```bash
#!/bin/bash
# install.sh

CLAUDE_DIR="$HOME/.claude"
PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Copy agents
mkdir -p "$CLAUDE_DIR/agents"
cp -r "$PLUGIN_DIR/agents"/* "$CLAUDE_DIR/agents/"

# Copy commands
mkdir -p "$CLAUDE_DIR/commands"
cp -r "$PLUGIN_DIR/commands"/* "$CLAUDE_DIR/commands/"

# Copy skills
mkdir -p "$CLAUDE_DIR/skills"
cp -r "$PLUGIN_DIR/skills"/* "$CLAUDE_DIR/skills/"

echo "✅ Plugin installed successfully"
```

7. **Create README.md** with setup instructions

8. **Publish to marketplace** (GitHub, etc.)

**Token Efficiency in Plugins:**
- Only install plugins you need
- Each plugin loads ~2-8 components
- Average: 300 tokens per plugin when used
- Compare to 5,000+ if all components loaded separately

### MCP Servers: Deep Dive

**MCP Architecture Simplified:**

```
Claude Code (Host)
    ↓
MCP Client(s) [Managed by Claude Code]
    ↓
MCP Server(s) [External/Local Programs]
    ↓
External Systems (GitHub, Slack, Databases, etc.)
```

**What MCP Provides:**

1. **Tools:** Functions Claude can call
   ```
   Example: fetch_github_pr_comments(repo, pr_number)
   ```

2. **Resources:** Data Claude can read
   ```
   Example: GitHub PR #123 context
   ```

3. **Prompts:** Pre-configured interaction templates
   ```
   Example: "Code review template for Python projects"
   ```

**MCP vs Alternative Approaches:**

| Feature | MCP | Custom Scripts | Functions API |
|---------|-----|----------|---------------|
| **Standard Protocol** | ✅ | ❌ | Vendor-specific |
| **Authentication** | Built-in | Manual | Vendor-specific |
| **Multiple Hosts** | ✅ | ❌ | ❌ |
| **Server-side** | ✅ (can be) | ❌ | ✅ |
| **Setup Complexity** | Low | High | Medium |

**Transport Options:**

1. **STDIO (Recommended for local)**
   - Server runs as subprocess
   - Perfect for: local development, quick setup
   - Example: filesystem, git servers

2. **HTTP/SSE**
   - Server runs separately
   - Perfect for: remote services, scalability
   - Example: Sentry, Stripe integration

3. **WebSocket**
   - Bi-directional communication
   - Perfect for: real-time updates
   - Less common, emerging use cases

**Security Considerations:**
- Only use MCP servers from trusted sources
- Review what permissions each server requests
- Use environment variables for secrets
- Subagent isolation can limit damage from compromised servers

---

## Integration Patterns

### Pattern 1: Foundation + Skills + Subagents

**Scenario:** Team project with shared standards and specialized workers

```
.claude/CLAUDE.md
├─ Project philosophy & tech stack

.claude/AGENTS.md
├─ Team coding standards
├─ Code review criteria
└─ Debugging approach

.claude/skills/
├─ typescript-patterns/SKILL.md
├─ testing-strategies/SKILL.md
└─ deployment-safety/SKILL.md

.claude/agents/
├─ code-reviewer.md (auto-triggered on PR reviews)
├─ test-runner.md (proactive test execution)
└─ security-auditor.md (vulnerability checking)

↓ Result:
- Main Claude handles orchestration
- Skills auto-load when relevant
- Subagents handle specialized tasks
- Context stays focused
```

### Pattern 2: Plugin-Based Workflow

**Scenario:** Multiple development domains, shared across team

```
Install Plugins:
├─ python-development/
├─ kubernetes-operations/
├─ database-migrations/
└─ security-scanning/

Each Plugin Contains:
├─ Specialized agents
├─ Domain-specific commands
├─ Task expertise (skills)
└─ MCP server configurations

↓ Result:
- Single `/agents` command shows all available domains
- Load only needed expertise
- Token-efficient composition
- Easy updates via plugin marketplace
```

### Pattern 3: MCP-Enhanced Workflow

**Scenario:** External system integration for real-time data

```
MCP Servers Configured:
├─ GitHub MCP (PR context, issues)
├─ Slack MCP (team communication)
├─ PostgreSQL MCP (database queries)
└─ Brave-Search MCP (web research)

Subagent Delegation:
├─ GitHub Agent: Fetches PR details, reviews changes
├─ Documentation Agent: Updates Slack with summaries
├─ Data Agent: Queries analytics database
└─ Research Agent: Searches for solutions online

↓ Result:
- Real-time external data access
- Subagents coordinate complex workflows
- Automatic tool invocation based on context
- Minimal manual configuration
```

### Pattern 4: Comprehensive Development Environment

**Scenario:** Enterprise project with all components

```
Foundation:
├─ CLAUDE.md (company standards)
├─ AGENTS.md (project guidelines)
└─ ~/.claude/skills/ (company-wide expertise)

Project-Specific:
├─ .claude/agents/ (specialized workers)
├─ .claude/skills/ (domain expertise)
└─ .claude/commands/ (frequent workflows)

Plugins (Installed):
├─ plugin-python-ml/
├─ plugin-react-frontend/
└─ plugin-devops-deployment/

External:
├─ MCP GitHub (repository operations)
├─ MCP Slack (team notifications)
├─ MCP PostgreSQL (data layer)
├─ MCP Sentry (error tracking)
└─ MCP Context7 (current docs)

↓ Result:
Complete, composable development environment
```

---

## Best Practices

### AGENTS.md Best Practices

✅ **DO:**
- Keep it under 500 lines
- Focus on project-specific context, not general instructions
- Update annually or when architecture changes
- Version control it
- Be specific about standards, not generic

❌ **DON'T:**
- Make it a tutorial (that's for SKILLS.md)
- Include authentication credentials
- Document every single rule (reference docs instead)
- Change it on every commit

### SKILLS.md Best Practices

✅ **DO:**
- Create one skill per major capability
- Write descriptive names and descriptions
- Include practical examples
- Test skills before distributing
- Version control your skills
- Group skills into categories (database/, frontend/, etc.)

❌ **DON'T:**
- Mix unrelated concepts into one skill
- Include credentials in skills
- Make skills too generic
- Create unused skills that never get auto-triggered
- Embed large datasets (link to external resources instead)

**Skill Naming Convention:**
```
✅ pdf-form-filling
✅ typescript-strict-patterns
✅ database-query-optimization
❌ pdf-stuff
❌ ts-patterns
❌ database-things
```

### Subagent Best Practices

✅ **DO:**
- Create subagents for distinct, focused responsibilities
- Use descriptive names that indicate function
- Document what tools the subagent can/cannot access
- Test subagents with example tasks
- Version control subagent definitions
- Include proactive trigger keywords in descriptions

❌ **DON'T:**
- Create generic "helper" subagents
- Give subagents access to all tools
- Expect subagents to modify main project configuration
- Forget to communicate subagent results back to main agent
- Create too many subagents (3-5 is typically optimal)

**Subagent Responsibility Examples:**
```
✅ test-runner: Run tests, analyze failures, suggest fixes
✅ code-reviewer: Review code against standards, check best practices
✅ security-auditor: Scan for vulnerabilities, check dependencies
✅ documentation-generator: Create docs, keep them current
✅ performance-analyzer: Benchmark, profile, optimize

❌ do-everything: Bad—loses focus
❌ helper: Bad—too vague
❌ fixer: Bad—unclear scope
```

### Plugin Best Practices

✅ **DO:**
- Create plugins for related component bundles (3+ items)
- Follow semantic versioning
- Include comprehensive README
- Write clear install scripts
- Test installation on clean environment
- Document dependencies between components
- Make plugins composable (work with other plugins)

❌ **DON'T:**
- Create single-component "plugins"
- Bundle unrelated functionality
- Assume users know how to install
- Create plugins that conflict with each other
- Forget to version your plugins
- Skip documentation

**Plugin Quality Checklist:**
```
- [ ] Clear marketplace.json metadata
- [ ] Tested install script
- [ ] README with setup instructions
- [ ] Example usage documented
- [ ] Components work independently
- [ ] No hardcoded paths
- [ ] Follows naming conventions
- [ ] Includes LICENSE file
```

### MCP Best Practices

✅ **DO:**
- Only add MCP servers you actively use
- Review server code/source before adding
- Document which MCP servers your project needs
- Use environment variables for credentials
- Test MCP tools before relying on them
- Keep MCP servers updated
- Consider server reliability and latency

❌ **DON'T:**
- Add every available MCP server "just in case"
- Hardcode credentials in config files
- Use untrusted or unverified MCP servers
- Expect MCP calls to always succeed (add error handling)
- Run MCP servers without understanding what they access

**MCP Configuration Security:**
```yaml
# ✅ CORRECT
mcpServers:
  github:
    command: python
    args: ["-m", "github_mcp"]
    env:
      GITHUB_TOKEN: ${GITHUB_TOKEN}  # Load from env var

# ❌ WRONG
mcpServers:
  github:
    env:
      GITHUB_TOKEN: "ghp_xxxxxxxxxxxx"  # Never hardcode!
```

---

## Comparison Matrix

### When to Use What

**Need to provide foundational project context?**
→ CLAUDE.md / AGENTS.md

**Need to teach Claude a specific technique or workflow?**
→ SKILLS.md

**Need a specialized worker for a focused task?**
→ SUBAGENT

**Need a frequently-run workflow with custom arguments?**
→ SLASH COMMAND

**Need automated validation or actions on events?**
→ HOOKS

**Need to bundle and distribute complete workflows?**
→ PLUGIN

**Need to integrate external tools/data sources?**
→ MCP SERVER

**Detailed Comparison Table:**

| Dimension | AGENTS.md | SKILLS | Subagents | Commands | Hooks | Plugins | MCP |
|-----------|----------|--------|-----------|----------|-------|---------|-----|
| **Scope** | Project | Global + Project | Project | Project | Project | Project | External |
| **Auto-Triggered** | Yes (startup) | Yes (relevant) | No | No | Yes (events) | No | No |
| **Isolation** | No | No | Yes | No | No | No | Yes |
| **Distribution** | Git | Git/API | Git | Git | Git | Marketplace | Config |
| **Token Cost** | Always | 30 base + demand | Per invoke | Per use | Per event | Progressive | Per call |
| **Execution** | Instruction | Code capable | Full Claude | Workflow | Code capable | Component-dependent | Protocol |
| **Arguments** | No | No | Via prompt | Yes | Event context | Varies | Yes |
| **Blocking** | No | No | No | No | Can block | No | No |
| **Best For** | Standards | Teaching | Specialization | Workflows | Validation | Bundling | Integration |
| **Examples** | "Review checklist" | "PDF manipulation" | "Test runner" | "/deploy staging" | "pre-commit lint" | "Python dev suite" | "GitHub API" |

---

## Real-World Workflows

### Workflow 1: Full Development Cycle with All Components

**Scenario:** Adding a new feature to a TypeScript/React app

**Setup:**
```
1. CLAUDE.md: React 18 + TypeScript guidelines
2. AGENTS.md: Team code standards & testing requirements
3. Skills: react-patterns, typescript-types, testing-strategies
4. Subagents: code-reviewer, test-runner, security-auditor
5. MCP: GitHub (PR context), Slack (notifications)
```

**Execution:**

1. **Feature Specification** (Main Claude)
   - Reads AGENTS.md for standards
   - Skills auto-load if pattern matches
   - Questions clarified via chat

2. **Code Generation** (Main Claude)
   - Applies AGENTS.md standards
   - Uses react-patterns skill
   - Generates TypeScript-strict code

3. **Test Automation** (Subagent: test-runner)
   - Delegates to @test-runner
   - Tests run in isolated context
   - Results reported back

4. **Code Review** (Subagent: code-reviewer)
   - Delegates to @code-reviewer
   - Reviews against standards
   - Suggests improvements

5. **Security Scan** (Subagent: security-auditor)
   - Delegates to @security-auditor
   - Checks dependencies via MCP GitHub
   - Reports vulnerabilities

6. **PR Update** (Main Claude)
   - Incorporates feedback
   - Updates GitHub PR via MCP
   - Posts summary to Slack via MCP

### Workflow 2: Cross-Functional Project Setup

**Scenario:** New microservices project with Python backend + React frontend

**Setup:**

**Install Plugins:**
```bash
# Backend environment
./plugin-python-microservices/install.sh
./plugin-database-migrations/install.sh
./plugin-kubernetes-ops/install.sh

# Frontend environment  
./plugin-react-frontend/install.sh
./plugin-performance-optimization/install.sh

# Shared
./plugin-dev-operations/install.sh
./plugin-security-scanning/install.sh
```

**MCP Configuration:**
```json
{
  "mcpServers": {
    "github": {"command": "..."},
    "slack": {"command": "..."},
    "postgres": {"command": "..."},
    "sentry": {"command": "..."}
  }
}
```

**Project Files:**
```
.claude/CLAUDE.md          # Company standards
.claude/AGENTS.md          # Project architecture
.claude/agents/
  ├─ backend-architect.md
  ├─ frontend-architect.md
  └─ infra-engineer.md
.claude/skills/
  ├─ microservices-patterns/
  ├─ api-design/
  └─ kubernetes-best-practices/
```

**Usage Flow:**
- Backend features → @backend-architect + python-microservices plugin
- Frontend features → @frontend-architect + react-frontend plugin  
- Infrastructure → @infra-engineer + kubernetes-ops plugin
- All use github MCP for context, slack MCP for updates
- Security checks via plugin-security-scanning automatically

### Workflow 3: Team Onboarding with Skills

**Scenario:** New developer joining team

**Resources Provided:**

1. **CLAUDE.md** - Read first: company standards, tech stack
2. **AGENTS.md** - Project-specific: architecture, decisions, debugging
3. **Skills Directory:**
   - local-setup/SKILL.md (environment setup)
   - coding-standards/SKILL.md (conventions)
   - testing-requirements/SKILL.md (test structure)
   - debugging-tools/SKILL.md (common tools)
   - deployment-process/SKILL.md (release procedure)

4. **Subagents** - Available helpers:
   - @code-reviewer (learn what to review)
   - @test-runner (see how tests work)
   - @security-auditor (understand security checks)

5. **First Task:**
   ```
   "I'm new to the team and want to add a simple feature to [component].
   Guide me through the process."
   ```

**What Claude Does:**
- Loads AGENTS.md automatically
- Auto-loads relevant skills based on task
- Explains standards while coding
- Delegates complex reviews to subagents
- Results in well-trained developer + quality code

---

## Quick Decision Tree

**Question: How should I package this?**

```
Is it foundational project context?
  → YES: AGENTS.md or CLAUDE.md
  → NO: Continue

Is it teaching a technique or workflow?
  → YES: Create SKILL.md
  → NO: Continue

Is it a focused, specialized task?
  → YES: Create SUBAGENT
  → NO: Continue

Is it a bundle of related components (3+)?
  → YES: Create PLUGIN
  → NO: Continue

Is it external tool/data access?
  → YES: Use/Configure MCP SERVER
  → NO: Continue

Uncertain? Probably SKILLS.md (most flexible)
```

---

## Resources & Links

**Official Documentation:**
- [Claude Skills (Anthropic)](https://www.anthropic.com/news/skills)
- [Building Agents with Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Equipping Agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/docs/)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/)

**Community Resources:**
- [Awesome Claude Code (GitHub)](https://github.com/hesreallyhim/awesome-claude-code)
- [Claude Skills vs MCP Analysis (Simon Willison)](https://simonwillison.net/2025/Oct/16/claude-skills/)
- [Claude Skills Complete Guide (Tyler Folkman)](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills)
- [Understanding Claude Code Extensions](https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins)

**Official MCP Servers:**
- https://github.com/modelcontextprotocol/servers

---

## Troubleshooting

### Skills Not Auto-Triggering

**Problem:** Created a skill but Claude isn't using it

**Checklist:**
- [ ] Skill has YAML frontmatter with `name:` and `description:`
- [ ] Description clearly indicates when to use it
- [ ] Skill is in correct location (`~/.claude/skills/` or `.claude/skills/`)
- [ ] Folder name matches name in SKILL.md
- [ ] Closed and reopened Claude Code (forces skill refresh)
- [ ] Task actually requires the skill

**Fix:** Make description more specific:
```yaml
# ❌ Too vague
description: "A skill for PDFs"

# ✅ Clear trigger
description: "Create, edit, and fill PDF forms with precise field placement and formatting"
```

### Subagent Not Responding

**Problem:** Subagent invocation (`@agent-name`) not working

**Checklist:**
- [ ] Subagent file is `.md` format (not `.yaml` or `.txt`)
- [ ] Location is `.claude/agents/` or `~/.claude/agents/`
- [ ] File name matches invocation name (kebab-case)
- [ ] File starts with YAML frontmatter
- [ ] Description is meaningful
- [ ] Claude Code restarted after adding subagent

**Fix:** Verify subagent file:
```bash
# Check file exists and has correct format
cat .claude/agents/test-runner.md | head -5
# Should show:
# ---
# name: test-runner
# description: ...
# ---
```

### MCP Server Not Connecting

**Problem:** Configured MCP server but Claude can't access tools

**Checklist:**
- [ ] MCP configuration syntax is correct (valid JSON)
- [ ] Server command path is absolute (not relative)
- [ ] Credentials are loaded from environment variables
- [ ] Server is installed/available
- [ ] Port not in use (for HTTP servers)
- [ ] No firewall blocks access

**Fix:** Test MCP server manually:
```bash
# Test if server can start
python -m mcp_server_name --help

# Check configuration
cat ~/.claude/config.json | grep -A5 mcpServers
```

### Plugin Installation Failing

**Problem:** Install script not working

**Checklist:**
- [ ] Install script has execute permission: `chmod +x install.sh`
- [ ] Script uses absolute or properly relative paths
- [ ] `.claude/` directories exist
- [ ] No permission errors on copy
- [ ] Script tested on clean environment

**Fix:** Debug installation:
```bash
# Run install with verbose output
bash -x ./install.sh

# Verify files copied
ls -la ~/.claude/agents/
ls -la ~/.claude/commands/
ls -la ~/.claude/skills/
```

---

## Summary

The Claude Code ecosystem provides a **layered, composable system** for extending AI capabilities:

- **AGENTS.md**: Foundation (project standards, not executable)
- **SKILLS**: Expertise modules (auto-triggered, code-capable)
- **SUBAGENTS**: Specialized workers (manual, isolated contexts)
- **PLUGINS**: Distribution bundles (composable collections)
- **MCP**: External integration (standardized protocol)

**Key Insight:** Use the **minimum necessary layers** for your use case. A simple project might only need AGENTS.md. A complex team environment might use all components.

**Next Steps:**
1. Read this guide when questions arise
2. Reference the "When to Use What" matrix
3. Refer to "Best Practices" before creating new components
4. Use the "Real-World Workflows" for inspiration
5. Check "Troubleshooting" if components aren't working

---

**Document Version:** 1.0  
**Last Updated:** October 29, 2025  
**Status:** Complete Reference
