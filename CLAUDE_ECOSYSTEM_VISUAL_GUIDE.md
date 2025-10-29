# Claude Code Ecosystem: Visual Reference Guide

**Diagrams, flowcharts, and visual explanations of how components interact**

---

## 1. Overall Architecture Diagram

```
╔════════════════════════════════════════════════════════════════════════╗
║                        CLAUDE CODE SESSION                             ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  ┌──────────────────────────────────────────────────────────────┐    ║
║  │ CLAUDE.md / AGENTS.md                                         │    ║
║  │ (Project Foundation - Loaded Every Session)                  │    ║
║  └──────────────────────────────────────────────────────────────┘    ║
║                              ▼                                         ║
║  ┌──────────────────────────────────────────────────────────────┐    ║
║  │ SKILLS (Auto-Discovered & Loaded On-Demand)                  │    ║
║  │ • Metadata: 30-50 tokens (always loaded)                     │    ║
║  │ • Full Content: 100-500 tokens (when needed)                 │    ║
║  └──────────────────────────────────────────────────────────────┘    ║
║                              ▼                                         ║
║          ┌───────────────────────────────────────────┐                ║
║          │  MAIN CLAUDE AGENT                        │                ║
║          │  • Orchestrates tasks                     │                ║
║          │  • Makes decisions                        │                ║
║          │  • Delegates when needed                  │                ║
║          └───────────────────────────────────────────┘                ║
║          ▲              │              │              ▲               ║
║          │              ▼              ▼              │               ║
║          │      ┌─────────────────────────────────┐   │               ║
║          │      │ Can Invoke:                      │   │               ║
║          │      │ • Subagents (@agent-name)       │   │               ║
║          │      │ • Slash Commands (/command)     │   │               ║
║          │      │ • MCP Tools (auto or manual)     │   │               ║
║          │      └─────────────────────────────────┘   │               ║
║          │              │              │              │               ║
║    ┌─────┴──────────────┴──────────────┴─────┐        │               ║
║    │                                         │        │               ║
║    ▼                                         ▼        ▼               ║
║  SUBAGENTS                  SLASH COMMANDS    MCP SERVERS             ║
║  (Isolated)                 (Workflows)       (External)              ║
║  • test-runner          • /run-tests       • filesystem              ║
║  • code-reviewer        • /deploy          • github                  ║
║  • security             • /scaffold        • slack                   ║
║                                                                        ║
║    ▲                         ▲                                        ║
║    │                         │                                        ║
║  HOOKS (Event-Driven)        │                                        ║
║  (Auto-triggered)            │                                        ║
║  • pre-commit  ──────────────┘                                        ║
║  • post-deploy                                                        ║
║  • validate-deps                                                      ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## 2. Component Lifecycle

```
┌────────────────────────────────────────────────────────────────────┐
│ SKILL LIFECYCLE                                                     │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  DISCOVERY              LOADING              EXECUTION   UNLOAD    │
│      ▼                   ▼                      ▼          ▼       │
│                                                                    │
│  Claude reads      Claude fully      Claude invokes   Session     │
│  skill name &      loads SKILL.md    available tools  ends        │
│  description       and examples                                   │
│  (~30 tokens)      (~100-500 more)   (code runs)     (cleared)    │
│                                                                    │
│  Decides if        Prepares to                                     │
│  skill might       use the skill                                   │
│  be relevant                                                       │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────┐
│ SUBAGENT LIFECYCLE                                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  CREATION            INVOCATION          EXECUTION      RETURN    │
│      ▼                   ▼                   ▼            ▼       │
│                                                                    │
│  .md file         @agent-name or    Separate context  Returns     │
│  created          delegated task    loads & runs      specific    │
│                                     Full Claude       results     │
│  Defines:         Claude decides    capabilities      back to     │
│  • Purpose        subagent can      (code execution,  main        │
│  • Tools          help              file access)      agent       │
│  • Boundaries                                                     │
│                   Spawns new        Tools limited                 │
│                   context window    per config                    │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────┐
│ MCP SERVER LIFECYCLE                                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  CONFIGURATION      INITIALIZATION    EXECUTION       CLEANUP     │
│      ▼                   ▼               ▼              ▼         │
│                                                                    │
│  ~/.claude/       MCP Client   Claude calls MCP    Server stops   │
│  config.json      spawns       tool with args      (or remains    │
│  defines server   server       Server executes     running)       │
│  details          Server       Returns result                     │
│                   and host     Result passed                      │
│  Including:       handshake    back to Claude                     │
│  • Command path   (capabilities                                   │
│  • Arguments      negotiation)                                    │
│  • Environment                                                    │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 3. When Each Component Is Loaded

```
Timeline of a Claude Code Session:

T=0s    PROJECT OPENS
        │
        ├─ Load CLAUDE.md (if exists)
        ├─ Load AGENTS.md
        │
        └─ Cache skill metadata (~100-200 tokens)
           ├─ skill-1: name, description
           ├─ skill-2: name, description
           └─ ... more skills ...

T=0.5s  USER ENTERS PROMPT
        │
        ├─ Claude reads task
        │
        ├─ Check which skills might be relevant
        │  ├─ YES: Load full SKILL.md (~100-500 tokens)
        │  └─ NO: Keep only metadata
        │
        └─ Prepare MCP tool list (if configured)

T=1-5s  CLAUDE PROCESSES TASK
        │
        ├─ If using @subagent-name
        │  └─ Load subagent definition
        │     Spawn isolated context
        │     Execute with assigned tools
        │
        ├─ If using MCP tool
        │  └─ Call configured MCP server
        │     Server executes remotely/locally
        │     Return results
        │
        └─ Main agent continues orchestration

T=∞     SESSION ENDS
        │
        └─ Skills: Unloaded
           Subagents: Stopped
           MCP servers: Keep running (unless local)
           New session starts fresh
```

---

## 4. Token Usage Comparison

```
SCENARIO A: Without Structure (All in AGENTS.md)
┌────────────────────────────────────┐
│ .claude/AGENTS.md                  │
│ (3,000 lines)                      │
│ ≈ 4,500 tokens                     │
│                                    │
│ Loaded every session:              │
│ Wastes context on unused info      │
│                                    │
│ → 4,500 tokens always in use       │
│ → 0 tokens available for work      │
└────────────────────────────────────┘
        (4,000 token window example)


SCENARIO B: With Progressive Disclosure (Skills-based)
┌──────────────────────────────────┐
│ AGENTS.md:                       │
│ ≈ 300 tokens (always)            │
│                                  │
│ Skill Metadata (5 skills):       │
│ ≈ 200 tokens (always)            │
│                                  │
│ Active Skill Content:            │
│ ≈ 300 tokens (on-demand)         │
│                                  │
│ MCP Tool List:                   │
│ ≈ 100 tokens (on-demand)         │
│ ─────────────────────────────────│
│ Used for this task:              │
│ ≈ 900 tokens                     │
│                                  │
│ → 3,100 tokens available for work│
└──────────────────────────────────┘

SAVINGS: 75% more context for actual work!
```

---

## 5. Decision Tree (Visual)

```
                    ┌─ START YOUR TASK ─┐
                    │                   │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼────────────┐
                    │   Is this project-   │
                    │   wide or team-wide  │
                    │   information?       │
                    └──┬──────────────┬────┘
                      YES            NO
                       │              │
            ┌──────────▼─────────────┐ │
            │  Use AGENTS.md         │ │
            │  (Or CLAUDE.md)        │ │
            │                        │ │
            │ Examples:              │ │
            │ • Tech stack           │ │
            │ • Code standards       │ │
            │ • Team preferences     │ │
            └────────────────────────┘ │
                                       │
                    ┌──────────────────▼───────┐
                    │  Are you teaching Claude │
                    │  how to do something?    │
                    └──┬──────────────────┬────┘
                      YES               NO
                       │                 │
         ┌─────────────▼──────────────┐  │
         │  Create a SKILL            │  │
         │  (.claude/skills/)         │  │
         │                            │  │
         │ Features:                  │  │
         │ • Auto-triggered           │  │
         │ • Reusable across tasks    │  │
         │ • Token-efficient          │  │
         │ • Code-capable             │  │
         └────────────────────────────┘  │
                                        │
                  ┌─────────────────────▼──────┐
                  │  Do you need a specialized │
                  │  worker agent?             │
                  └──┬────────────────────┬────┘
                    YES                 NO
                     │                   │
        ┌────────────▼────────────────┐  │
        │  Create a SUBAGENT         │  │
        │  (.claude/agents/)         │  │
        │                            │  │
        │ Use when:                  │  │
        │ • Isolated context needed  │  │
        │ • Specialized focus        │  │
        │ • Parallel tasks           │  │
        │ • Complex workflows        │  │
        └────────────────────────────┘  │
                                        │
                ┌──────────────────────▼─────┐
                │  Is this a workflow you     │
                │  run frequently?           │
                └──┬──────────────────┬──────┘
                   YES               NO
                    │                │
      ┌─────────────▼────────────────┐ │
      │  Create a SLASH COMMAND      │ │
      │  (.claude/commands/)         │ │
      │                             │ │
      │ Examples:                   │ │
      │ • /deploy [env]             │ │
      │ • /run-tests [suite]        │ │
      │ • /scaffold [name]          │ │
      └─────────────────────────────┘ │
                                      │
                ┌──────────────────────▼─────┐
                │  Do you need automated      │
                │  validation on events?     │
                └──┬──────────────────┬──────┘
                   YES               NO
                    │                │
      ┌─────────────▼────────────────┐ │
      │  Create a HOOK              │ │
      │  (.claude/hooks/)           │ │
      │                             │ │
      │ Examples:                   │ │
      │ • pre-commit (validation)  │ │
      │ • post-deploy (notify)     │ │
      │ • validate-deps (security) │ │
      └─────────────────────────────┘ │
                                      │
                ┌──────────────────────▼─────┐
                │  Are you bundling 3+       │
                │  related components?       │
                └──┬──────────────────┬──────┘
                   YES               NO
                    │                │
       ┌────────────▼───────────────┐│
       │  Create a PLUGIN           ││
       │  (.claude-plugin/)         ││
       │                            ││
       │ Benefits:                  ││
       │ • Cohesive distribution    ││
       │ • Version control          ││
       │ • Marketplace sharing      ││
       └────────────────────────────┘│
                                     │
               ┌─────────────────────▼──────┐
               │  Do you need external      │
               │  tool/data access?        │
               └──┬──────────────────┬──────┘
                 YES               NO
                  │                 │
      ┌───────────▼─────────────┐   │
      │  Use/Configure MCP      │   │
      │  SERVER                 │   │
      │                         │   │
      │ Examples:               │   │
      │ • GitHub               │   │
      │ • Slack                │   │
      │ • PostgreSQL           │   │
      │ • Filesystem           │   │
      └─────────────────────────┘   │
                                    │
                        ┌───────────▼──────┐
                        │  ✓ You're done!  │
                        │  Start working   │
                        └──────────────────┘
```

---

## 6. Slash Commands & Hooks in Action

```
USER INTERACTION FLOWS
════════════════════════════════════════════════════════════

MANUAL WORKFLOW (Slash Commands):
──────────────────────────────────

User types: /deploy staging
       ↓
Claude Code parses command
       ↓
Loads: .claude/commands/deploy.md
       ↓
Extracts: arguments (staging)
       ↓
Executes workflow:
  1. Validate environment config
  2. Run pre-deployment tests
  3. Build application
  4. Deploy to staging
  5. Run smoke tests
  6. Report results
       ↓
Output to user:
  ✓ Deployment successful
  ✓ All smoke tests passed
  → URL: https://staging.example.com


EVENT-DRIVEN WORKFLOW (Hooks):
────────────────────────────────

User attempts: git commit
       ↓
Claude Code detects: commit event
       ↓
Triggers: .claude/hooks/pre-commit.md
       ↓
Hook workflow:
  1. Run linter on changed files
  2. Execute related tests
  3. Check for debug code
  4. Validate commit message format
       ↓
       ├─ ALL PASS → Allow commit
       │              Show summary
       │              Continue workflow
       │
       └─ ANY FAIL → Block commit
                     Show errors
                     Suggest fixes
                     Prevent commit


COMBINED WORKFLOW:
───────────────────

User: Makes code changes
  ↓
Hook: pre-save → Auto-format code
  ↓
User: Attempts commit
  ↓
Hook: pre-commit → Run validations
  ↓ (if pass)
Command: User runs /deploy staging
  ↓
Hook: pre-deploy → Final checks
  ↓ (if pass)
Command workflow executes
  ↓
Hook: post-deploy → Notifications
  ↓
Complete! 🎉


ARGUMENT PASSING (Slash Commands):
────────────────────────────────────

/deploy [environment] [version]
   ↓         ↓            ↓
 command    arg1        arg2

Example: /deploy staging v1.2.3

Parsed as:
{
  command: 'deploy',
  args: {
    environment: 'staging',
    version: 'v1.2.3'
  }
}

Workflow uses args:
  → Deploy version v1.2.3
  → To staging environment
  → With staging config


EVENT CONTEXT (Hooks):
────────────────────────

Commit triggered
  ↓
Hook receives context:
{
  event: 'pre-commit',
  files: {
    added: ['new-feature.js'],
    modified: ['existing.js'],
    deleted: ['old-file.js']
  },
  commit: {
    message: 'feat: add new feature',
    branch: 'feature/new',
    author: 'dev@example.com'
  },
  timestamp: '2025-10-29T10:30:00Z'
}
  ↓
Hook can:
  → Validate specific files
  → Check commit message format
  → Verify branch naming
  → Run targeted tests
```

## 7. Commands vs Hooks: When to Use Which

```
DECISION MATRIX
═══════════════════════════════════════════════════════

┌─────────────────────────────────────────────────┐
│  IS THIS TRIGGERED BY USER ACTION?             │
│  (User explicitly runs something)              │
└──────────┬──────────────────────────────────────┘
           │
     YES   │   NO
      ↓    │    ↓
┌──────────┴───────────┐  ┌─────────────────────┐
│  SLASH COMMAND       │  │  IS IT AUTOMATIC?   │
│                      │  │  (Runs on events)   │
│  Use when:           │  └──────┬──────────────┘
│  • User decides when │         │
│  • Needs arguments   │    YES  │  NO
│  • On-demand         │         ↓  ↓
│                      │  ┌──────────────────┐
│  Examples:           │  │  HOOK            │
│  /deploy staging     │  │                  │
│  /run-tests unit     │  │  Use when:       │
│  /scaffold Component │  │  • Auto-validate │
│                      │  │  • On events     │
└──────────────────────┘  │  • Quality gates │
                          │                  │
                          │  Examples:       │
                          │  pre-commit      │
                          │  post-deploy     │
                          │  validate-deps   │
                          └──────────────────┘


WORKFLOW COMPARISON
═══════════════════════════════════════════════════════

Slash Command Flow:
User → /command → Workflow → Result
  ↑                              ↓
  └──────── User controls ───────┘

Hook Flow:
Event → Hook → Validate/Act → Continue/Block
  ↑                                ↓
  └────── Automatic guard ─────────┘


USE CASE EXAMPLES
═══════════════════════════════════════════════════════

SCENARIO: Deploying Code
─────────────────────────

Option A: Slash Command
  User: "/deploy staging"
  ✓ User controls timing
  ✓ Can pass environment
  ✓ Optional (user might skip)

Option B: Hook
  Event: "git push origin main"
  Hook: "pre-push validation"
  ✓ Always runs
  ✓ Can block bad code
  ✗ Can't skip easily


SCENARIO: Running Tests
────────────────────────

Option A: Slash Command
  User: "/run-tests unit"
  ✓ Run specific suites
  ✓ On-demand testing
  ✓ Quick feedback

Option B: Hook
  Event: "file saved"
  Hook: "on-save test"
  ✓ Always catches breaks
  ✓ Continuous validation
  ✗ May slow workflow


BEST PRACTICE: USE BOTH
────────────────────────

Commands for:
  → Manual workflows
  → User-controlled timing
  → Flexible arguments

Hooks for:
  → Quality gates
  → Automatic validation
  → Preventing mistakes

Example:
  Hook: pre-commit (always validate)
  Command: /deploy (when user decides)
```

---

## 8. Integration Patterns Visual

```
PATTERN 1: Simple Project
═══════════════════════════

    AGENTS.md
       ↓
    Tasks
       ↓
    Skills auto-load if relevant
       ↓
    Done


PATTERN 2: Team Project with Workflows
═════════════════════════════════════════

    AGENTS.md + CLAUDE.md
           ↓
    Skills (auto-loaded)
           ↓
    Main Claude orchestrates
           │
      ┌────┼────┬────┐
      ▼    ▼    ▼    ▼
     Task A  B  C  D
      │     │  │  │
      └─────┼──┤  │
           @test-  │
           runner  │
              └────@code-
                   reviewer


PATTERN 3: Complex Project (All Components)
═════════════════════════════════════════════

    CLAUDE.md ← AGENTS.md
          ↓        ↓
          └────┬───┘
               ↓
         Skills (5+)
               ↓
         Main Claude
         ┌─────┼─────┬──────┐
         ▼     ▼     ▼      ▼
    @test  @review @audit Plugins
    runner        security
         ▼     ▼     ▼      ▼
    Subagents (isolated contexts)
         │     │     │      │
         └─────┼─────┼──────┤
               ▼     ▼      ▼
            MCP Servers
           (GitHub, Slack,
            PostgreSQL,
            Sentry, etc.)


PATTERN 4: Distributed Team
═════════════════════════════

    Company-wide:
    ~/.claude/
    ├─ CLAUDE.md
    ├─ skills/ (shared)
    └─ agents/ (global)
            ↓ (shared via git)
            
    Project A              Project B
    .claude/               .claude/
    ├─ AGENTS.md          ├─ AGENTS.md
    ├─ skills/            ├─ skills/
    └─ agents/            └─ agents/
            ↓                    ↓
         Uses shared         Uses shared
         company skills      company skills
         AND project-        AND project-
         specific skills     specific skills
            ↓                    ↓
         Plugins            Plugins
         + MCP              + MCP
```

---

## 7. Skill Auto-Loading Flowchart

```
┌──────────────────────────────────────────────────────────────┐
│  New Task Arrives at Claude                                  │
└─────────────────────────┬──────────────────────────────────┘
                          │
                          ▼
      ┌────────────────────────────────────────┐
      │ Claude reads task description           │
      └─────────────┬──────────────────────────┘
                    │
                    ▼
      ┌────────────────────────────────────────┐
      │ Iterate through skill metadata:        │
      │ (name + description for each skill)    │
      └─────────────┬──────────────────────────┘
                    │
                    ▼
      ┌─────────────────────────────────────┐
      │ For each skill:                      │
      │ "Does this skill's description      │
      │  match the current task?"            │
      └──┬──────────────────────────┬────────┘
         │ YES                      │ NO
         ▼                          ▼
    ┌────────────────┐  ┌─────────────────────┐
    │ Load full      │  │ Keep metadata only  │
    │ SKILL.md       │  │ (~30-50 tokens)     │
    │ (~100-500      │  │                     │
    │ tokens)        │  │ Move to next skill  │
    │                │  └─────────────────────┘
    │ Include:       │
    │ • Examples     │
    │ • Scripts      │
    │ • Resources    │
    │                │
    │ Claude can now │
    │ use skill      │
    │ within this    │
    │ session        │
    └────────────────┘


Token Efficiency:
─────────────────
With 5 skills and only 2 relevant:

Metadata always:     ~150 tokens
├─ Skill 1: ~30
├─ Skill 2: ~30
├─ Skill 3: ~30
├─ Skill 4: ~30
└─ Skill 5: ~30

Load skill 2 content:  ~200 tokens
Load skill 4 content:  ~200 tokens

Total for this task:   ~550 tokens
Used: ~550 tokens
Saved: ~600 tokens worth of unused skill content

(If all 5 were always loaded, 
would cost ~1,150 tokens)
```

---

## 8. MCP Integration Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ Claude Code (MCP Host)                                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Configuration:                                             │
│  ~/.claude/config.json specifies MCP servers               │
│                                                              │
│  When Claude Code starts:                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Create MCP Client for each configured server        │   │
│  │                                                     │   │
│  │ Client 1 ← → Server 1 (GitHub)                     │   │
│  │ Client 2 ← → Server 2 (Slack)                      │   │
│  │ Client 3 ← → Server 3 (PostgreSQL)                 │   │
│  │ Client N ← → Server N (...)                        │   │
│  │                                                     │   │
│  │ Each client-server pair has 1:1 relationship       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  Claude automatically:                                      │
│  • Discovers available tools from each server              │
│  • Presents them as options to use                         │
│  • Calls them when needed                                  │
│  • Returns results to main context                         │
│                                                              │
└────────────────┬──────────────────────────────────────────┘
                 │
          ┌──────┴──────────┬─────────┬──────────┐
          │                 │         │          │
          ▼                 ▼         ▼          ▼
    ┌──────────┐    ┌──────────┐  ┌───────┐  ┌────────┐
    │  GitHub  │    │  Slack   │  │ Postgres PostgreSQL
    │  MCP     │    │  MCP     │  │  MCP    │ Database
    │ Server   │    │ Server   │  │ Server  │
    │          │    │          │  │         │
    │ Tools:   │    │ Tools:   │  │ Tools:  │
    │ • list   │    │ • send   │  │ • query │
    │   repos  │    │   message│  │ • exec  │
    │ • create │    │ • read   │  │ • update│
    │   issue  │    │ • thread │  │         │
    └──────────┘    └──────────┘  └─────────┘
         │                │            │
         ▼                ▼            ▼
    GitHub API       Slack API    PostgreSQL
                                   Connection
```

---

## 9. Component Relationships Matrix

```
              │ AGENTS │ SKILLS │ SUBAGENTS │ PLUGINS │ MCP
──────────────┼────────┼────────┼───────────┼─────────┼─────
Can call?     │   No   │  Yes*  │    Yes    │   No*   │ Auto
Auto-trigger? │  Yes   │  Yes   │    No     │   No    │  Sel
Isolated ctx? │   No   │   No   │   Yes     │   No    │  Sel
Code exec?    │   No   │  Yes   │    Yes    │   Var   │  Yes
Version ctrl? │  Yes   │  Yes   │   Yes     │   Yes   │   No
Share team?   │  Yes   │  Yes   │   Yes     │   Yes   │  Cfg
Token cost    │ Fixed  │ Prog   │  On-dem   │ Comp    │ Call

* Skills are auto-triggered but can be manually invoked
  Plugins are bundled but components within are individual
  MCP is typically auto-offered or manually specified
```

---

## 10. Context Window Management

```
4,000 token window (example)

WITHOUT Skills:
┌────────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓ AGENTS.md (3,000)              │
│ ░░░░░░░░░░ Headroom (1,000)               │
│ NOT ENOUGH SPACE FOR ACTUAL WORK!          │
└────────────────────────────────────────────┘


WITH Skills (Progressive Disclosure):
┌────────────────────────────────────────────┐
│ ▓ AGENTS metadata (300)                   │
│ ▓ Skill meta (5 skills) (200)             │
│ ▓ MCP list (150)                          │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░ Work (3,350)   │
│ PLENTY OF SPACE FOR ACTUAL WORK!           │
│                                            │
│ If one skill needed: Load (300)            │
│ ░░░░░░░░░░░░░ Still have (3,050)         │
└────────────────────────────────────────────┘


Dynamic Loading Example:
─────────────────────────
Start:     300 (base) + 200 (skill meta) + 150 (MCP) = 650 used
Available:                                         3,350 tokens

User requests PDF creation:
Load PDF skill:            +300 tokens
Available:                 3,050 tokens

User requests code review:
Load code-review skill:    +300 tokens
Available:                 2,750 tokens

User needs GitHub access:
MCP GitHub call:           +100 tokens
Available:                 2,650 tokens

Still lots of room for conversation and work!
```

---

## 11. Setup Checklist Visual

```
NEW PROJECT SETUP
════════════════════════════════════════════

Step 1: Foundation
  ┌─ Create .claude/ directory
  ├─ Write CLAUDE.md (if company-wide)
  ├─ Write AGENTS.md (project specific)
  └─ ✓

Step 2: Expertise (Skills)
  ┌─ Identify needed expertise areas
  ├─ Check ~/.claude/skills/ for existing
  ├─ Create new skills if needed
  │  └─ .claude/skills/[name]/SKILL.md
  └─ ✓

Step 3: Specialists (Subagents)
  ┌─ Identify if specialist workers needed
  ├─ If test automation: Create test-runner.md
  ├─ If code review: Create code-reviewer.md
  ├─ If security: Create security-auditor.md
  └─ ✓

Step 4: Plugins (Optional)
  ┌─ Check if domain-specific plugin exists
  ├─ Install if applicable
  └─ ✓

Step 5: External Integration (MCP)
  ┌─ Identify external tools/data needed
  ├─ Check available MCP servers
  ├─ Configure in ~/.claude/config.json
  └─ ✓

Step 6: Version Control
  ┌─ Add .claude/ to git
  ├─ Commit AGENTS.md + skills + agents
  ├─ Share with team
  └─ ✓

SETUP COMPLETE! 
Each team member now has consistent environment.
```

---

## 12. Common Gotchas (Visual)

```
GOTCHA 1: Skill Not Auto-Triggering
───────────────────────────────────
What you wrote:
  description: "PDF skill"         ← TOO VAGUE

What Claude reads:
  "Maybe relevant... 
   Maybe not... skip for now"

What works:
  description: "Create, edit, and fill PDF forms 
               with field placement and formatting"
               ↑ Specific enough to trigger

Fix: Be descriptive. Claude needs to recognize relevance.


GOTCHA 2: Subagent "Not Working"
──────────────────────────────────
Wrong location:
  ~/.claude/test_runner.md ✗ (underscore, wrong location)

Right location:
  ~/.claude/agents/test-runner.md ✓ (kebab-case, right place)
  or
  .claude/agents/test-runner.md ✓ (project-specific)

Fix: Check filename and location match invocation name.


GOTCHA 3: Plugin Install Script Fails
──────────────────────────────────────
Forgot to make executable:
  $ ./install.sh
  bash: ./install.sh: Permission denied

Fix:
  $ chmod +x install.sh
  $ ./install.sh ✓


GOTCHA 4: MCP Server Not Connecting
─────────────────────────────────────
Hardcoded token in config:
  "env": {"GITHUB_TOKEN": "ghp_xxxx"}  ✗
  Security risk! Token visible in config file!

Correct approach:
  "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}  ✓
  Loads from environment variable

Fix: Use environment variables, never hardcode secrets.


GOTCHA 5: Skills All Loaded
────────────────────────────
Problem: Installed 50 skills, token budget exploded

Metadata loaded:
  50 skills × 30 tokens = 1,500 tokens

You wanted:
  Only skills for Python, but got all 50

Fix: 
  1. Keep only actively used skills
  2. Archive others
  3. Or use plugins to organize by domain
```

---

## 13. Performance Optimization Path

```
Current Setup → Optimized Setup
═════════════════════════════════════════════

BEFORE:
.claude/
└─ AGENTS.md (2,000 lines!)
   Everything jammed in one file
   
   Cost: ~3,000 tokens always
   Result: Almost no room for work


REFACTOR STEP 1:
Extract expertise into skills
.claude/
├─ AGENTS.md (500 lines, project focus)
├─ skills/
│  ├─ react-patterns/SKILL.md
│  ├─ testing-strategies/SKILL.md
│  └─ deploy-safely/SKILL.md

Cost: 300 (AGENTS) + 100 (skill meta) = 400
Loaded: 3,600 tokens for actual work
Improvement: +600 tokens (20%)


REFACTOR STEP 2:
Extract workers into subagents
.claude/
├─ AGENTS.md (300 lines)
├─ skills/ (expert)
└─ agents/
   ├─ test-runner.md
   ├─ code-reviewer.md
   └─ security-auditor.md

Cost: 300 (AGENTS) + 100 (skill meta) + 50 (subagent list)
Loaded: 3,550 tokens for actual work
Improvement: +50 tokens (2%) but better delegation


REFACTOR STEP 3:
Extract reusable commands
.claude/
├─ AGENTS.md (300 lines)
├─ skills/
├─ agents/
└─ commands/
   ├─ run-tests.md
   ├─ scaffold.md
   └─ deploy.md

Cost: Same
Benefit: Faster access to common workflows
Shortcut: Type /run-tests instead of describing


REFACTOR STEP 4:
Bundle and distribute as plugin
plugin-name/
├─ .claude-plugin/marketplace.json
├─ agents/ (3 agents)
├─ commands/ (3 commands)
├─ skills/ (3 skills)
└── install.sh

Cost: Same (progressive loading)
Benefit: Shareable, versioned, easy to install
  ./install.sh → Everything set up


FINAL OPTIMIZED SETUP:
──────────────────────
~/.claude/                    (User global)
  ├─ skills/ (shared expertise)
  └─ agents/ (shared workers)

.claude/                      (Project)
  ├─ AGENTS.md (300 lines)
  ├─ agents/ (project-specific)
  ├─ skills/ (project-specific)
  └─ commands/ (workflows)

Installed:
  ├─ Plugin 1: python-dev
  ├─ Plugin 2: kubernetes-ops
  └─ Plugin 3: security-scanning

MCP configured:
  ├─ GitHub
  ├─ Slack
  └─ PostgreSQL

Result:
────────
Metadata: ~400 tokens
Active content: ~800 tokens (on-demand)
Available for work: ~2,800 tokens

Perfect balance of capability and headroom!
```

---

## 14. Quick Lookup: "Should I Use This?"

```
Task: Add a new feature to React component

┌─ Does project have code standards?
│  └─ YES: Check AGENTS.md exists ✓
│
├─ Need to remember how to write React components?
│  └─ YES: Use react-patterns SKILL ✓
│
├─ Need someone to test the code?
│  └─ YES: Use @test-runner SUBAGENT ✓
│
├─ Need GitHub context (branches, PRs)?
│  └─ YES: Use GitHub MCP SERVER ✓
│
├─ All in one workflow worth repeating?
│  └─ YES: Create /create-feature COMMAND ✓
│
└─ Result: High-quality feature, quickly! ✓


Task: Debug failing test

┌─ Know how to run tests?
│  └─ NO: Check testing-strategies SKILL ✓
│
├─ Could use automation?
│  └─ YES: Delegate to @test-runner SUBAGENT ✓
│
├─ Need error tracking context?
│  └─ YES: Use Sentry MCP SERVER ✓
│
└─ Test fixed! ✓


Task: Deploy to production

┌─ Have deployment standards?
│  └─ NO: Check AGENTS.md for process ✓
│
├─ Need a checklist?
│  └─ YES: Use deployment-checklist SKILL ✓
│
├─ Want automation?
│  └─ YES: Delegate to @deployment-engineer SUBAGENT ✓
│
├─ Post update to team?
│  └─ YES: Use Slack MCP SERVER ✓
│
└─ Deployment complete! ✓
```

---

**Use these visual references alongside the main guide for quick understanding!**

---

Recommended viewing order:
1. Start with **#1 Overall Architecture** to understand relationships
2. Look at **#13 Performance Optimization** to understand why structure matters
3. Reference **#5 Decision Tree** when making choices
4. Check **#12 Common Gotchas** when things aren't working
5. Use **#14 Quick Lookup** for everyday decisions
