# Claude Code Ecosystem: Navigation Index

**Quick navigation to find exactly what you need, fast**

---

## 📑 Document Overview

| Document | Purpose | Time to Read | Best For |
|----------|---------|--------------|----------|
| **[Full Guide](./CLAUDE_ECOSYSTEM_GUIDE.md)** | Complete architecture reference | 30-45 min | Deep understanding |
| **[Quick Ref](./CLAUDE_ECOSYSTEM_QUICK_REF.md)** | Cheat sheet & templates | 5-10 min | Daily use |
| **[Visual Guide](./CLAUDE_ECOSYSTEM_VISUAL_GUIDE.md)** | Diagrams & flowcharts | 10-15 min | Visual learners |
| **[README](./README_ECOSYSTEM.md)** | Getting started overview | 2-5 min | Beginners |

---

## 🎯 Quick Navigation by Use Case

### "I'm new to Claude Code ecosystem"
1. **Start here:** README_ECOSYSTEM.md (2 min)
2. **Then:** Full Guide → "Quick Start Reference" (5 min)
3. **Finally:** Quick Ref → "Decision Tree" (2 min)

**Total Time: 10 minutes**

### "I need to set up a new project"
1. **Quick Ref** → "I'm Starting a New Project" (3 min)
2. **Full Guide** → "Component Details" (10 min)
3. **Templates** → Copy relevant templates (5 min)
4. **Visual Guide** → #1 "Overall Architecture" (2 min)

**Total Time: 20 minutes**

### "I want to create a workflow shortcut"
1. Read: **Quick Ref** → "I Want to Create a Workflow Shortcut"
2. Copy: **Quick Ref** → "Slash Command Template"
3. Create: `.claude/commands/my-command.md`
4. Test: Type `/my-command` in Claude Code

**Total Time: 10 minutes**

### "I want to automate quality checks"
1. Read: **Full Guide** → "Hooks: Deep Dive"
2. Copy: **Quick Ref** → "Hook Template"
3. Create: `.claude/hooks/pre-commit.md`
4. Configure: `.claude/hooks/config.yaml`
5. Test: Attempt a commit

**Total Time: 15 minutes**

### "I need to decide: Command or Hook?"
1. **Visual Guide** → #15 (Commands vs Hooks)
2. **Quick Ref** → Updated "Decision Tree"
3. **Full Guide** → "Comparison Matrix" (updated)

**Time: 5 minutes**

### "Something's not working - debugging"
1. **Visual Guide** → #12 "Common Gotchas" (5 min)
2. **Quick Ref** → "Commonly Used Commands" (2 min)
3. **Full Guide** → "Best Practices" (10 min)

**Total Time: 17 minutes**

### "I want to understand how everything fits together"
1. **Visual Guide** → #1 "Overall Architecture" (5 min)
2. **Visual Guide** → #6 "Slash Commands & Hooks in Action" (5 min)
3. **Full Guide** → "Component Architecture" (10 min)

**Total Time: 20 minutes**

### "I'm teaching my team about Claude Code"
1. **README** → Overview (5 min)
2. **Visual Guide** → Key diagrams (#1, #5, #6, #15) (15 min)
3. **Quick Ref** → "Decision Tree" (5 min)
4. **Full Guide** → "Real-World Workflows" (15 min)

**Total Time: 40 minutes**

---

## 📚 Section-by-Section Guide

### FULL GUIDE (CLAUDE_ECOSYSTEM_GUIDE.md)

**Getting Started (15 min)**
- Quick Start Reference → 5 min
- Core Components Overview → 10 min

**Component Details (45 min)**
- AGENTS.md Deep Dive → 10 min
- SKILLS Deep Dive → 10 min
- Subagents Deep Dive → 5 min
- Slash Commands Deep Dive → 15 min
- Hooks Deep Dive → 15 min
- Plugins Deep Dive → 10 min
- MCP Servers Deep Dive → 10 min

**Integration (20 min)**
- Integration Patterns → 10 min
- Real-World Workflows → 10 min

**Reference (15 min)**
- Comparison Matrix → 5 min
- Best Practices → 10 min

### QUICK REF (CLAUDE_ECOSYSTEM_QUICK_REF.md)

**Essential Info (10 min)**
- File Locations → 2 min
- Component At-A-Glance → 5 min
- Common Tasks → 3 min

**Working Templates (15 min)**
- AGENTS.md Template → 3 min
- SKILL.md Template → 5 min
- Subagent Template → 3 min
- Slash Command Template → 2 min
- Hook Template → 2 min

**Daily Use (5 min)**
- Decision Tree → 2 min
- Commonly Used Commands → 3 min

### VISUAL GUIDE (CLAUDE_ECOSYSTEM_VISUAL_GUIDE.md)

**Core Understanding (15 min)**
- #1 Overall Architecture → 5 min
- #2 Component Lifecycle → 5 min
- #3 When Components Load → 5 min

**Decision Making (10 min)**
- #5 Decision Tree → 5 min
- #15 Commands vs Hooks → 5 min

**Practical Examples (15 min)**
- #6 Slash Commands & Hooks in Action → 10 min
- #8 Integration Patterns → 5 min

---

## 🔍 Finding Specific Information

### Finding info about: **AGENTS.md**
→ **Quick Ref** → "AGENTS.md" at-a-glance (2 min)
OR
→ **Full Guide** → "AGENTS.md (Project Agent Configuration)" (10 min)
OR
→ **Visual Guide** → #1 "Overall Architecture" (5 min)

### Finding info about: **SKILLS**
→ **Quick Ref** → "SKILLS" at-a-glance (2 min)
OR
→ **Full Guide** → "SKILLS (Agent Expertise Packages)" (10 min)
OR
→ **Visual Guide** → #2 "Component Lifecycle" (5 min)

### Finding info about: **Subagents**
→ **Quick Ref** → "SUBAGENTS" at-a-glance (2 min)
OR
→ **Full Guide** → "Subagents (Specialized Workers)" (5 min)
OR
→ **Visual Guide** → #8 "Integration Patterns" (5 min)

### Finding info about: **Slash Commands**
→ **Quick Ref** → "Slash Commands" at-a-glance (2 min)
OR
→ **Full Guide** → "Slash Commands: Deep Dive" (15 min)
OR
→ **Visual Guide** → #6 "Slash Commands in Action" (5 min)

### Finding info about: **Hooks**
→ **Quick Ref** → "Hooks" at-a-glance (2 min)
OR
→ **Full Guide** → "Hooks: Deep Dive" (15 min)
OR
→ **Visual Guide** → #6 "Event-Driven Workflow" (5 min)

### Finding info about: **Commands vs Hooks**
→ **Visual Guide** → #15 "Commands vs Hooks" (5 min)
OR
→ **Full Guide** → "Comparison Matrix" (updated) (5 min)

### Finding info about: **Plugins**
→ **Quick Ref** → "PLUGINS" at-a-glance (2 min)
OR
→ **Full Guide** → "Plugins (Bundled Extension Packages)" (10 min)

### Finding info about: **MCP Servers**
→ **Quick Ref** → "MCP SERVERS" at-a-glance (2 min)
OR
→ **Full Guide** → "MCP Servers (External Tool/Data Integrations)" (10 min)
OR
→ **Visual Guide** → #8 "MCP Integration Architecture" (5 min)

### Finding info about: **Token Usage**
→ **Visual Guide** → #4 "Token Usage Comparison" (5 min)
OR
→ **Full Guide** → Comparison Matrix (2 min)

### Finding info about: **Best Practices**
→ **Full Guide** → "Best Practices" (10 min)
OR
→ **Visual Guide** → #13 "Performance Optimization Path" (5 min)

### Finding info about: **Troubleshooting**
→ **Visual Guide** → #12 "Common Gotchas" (5 min)
OR
→ **Quick Ref** → "Commonly Used Commands" (3 min)

---

## 🎯 Learning Paths

### 🚀 **Beginner Path** (45 minutes total)
**Goal:** Understand the basics and get started

1. **README_ECOSYSTEM.md** → Overview (5 min)
2. **Quick Ref** → File locations + Components (10 min)
3. **Visual Guide** → #1 Architecture + #5 Decision Tree (10 min)
4. **Full Guide** → Quick Start Reference (5 min)
5. **Quick Ref** → Templates (copy for future use) (10 min)
6. **Quick Ref** → Decision Tree (5 min)

**Outcome:** Ready to set up basic projects and understand components

### 🔧 **Practitioner Path** (90 minutes total)
**Goal:** Daily use and efficient workflows

1. **Quick Ref** → All sections (30 min)
2. **Visual Guide** → All diagrams (45 min)
3. **Full Guide** → Real-World Workflows (15 min)

**Outcome:** Efficient daily use, can create components, troubleshoot issues

### 🏗️ **Advanced Path** (2 hours total)
**Goal:** Complex setups and team leadership

1. **Full Guide** → Complete read-through (60 min)
2. **Visual Guide** → All diagrams + analysis (30 min)
3. **Quick Ref** → All templates + customization (20 min)
4. **README** → Teaching overview (10 min)

**Outcome:** Can architect complex setups, teach others, optimize performance

### 👥 **Team Lead Path** (60 minutes total)
**Goal:** Set up team workflows and standards

1. **Full Guide** → AGENTS.md + Best Practices (20 min)
2. **Visual Guide** → #1, #6, #8, #15 (20 min)
3. **Quick Ref** → Decision Tree + Templates (15 min)
4. **README** → Overview for sharing (5 min)

**Outcome:** Can set up team standards, create shared components

---

## 📋 Checklists for Common Tasks

### Checklist: Setting Up a New Project
```
□ Read: Quick Ref → "I'm Starting a New Project"
□ Create: .claude/AGENTS.md (use template)
□ Identify: Relevant skills from ~/.claude/skills/
□ Plan: Subagents needed (if any)
□ Consider: Plugins for domain
□ Configure: MCP servers (if needed)
□ Test: Load Claude Code, verify context
□ Document: Project setup for team
□ Time: 20-30 minutes
```

### Checklist: Creating a Skill
```
□ Read: Full Guide → "SKILLS Deep Dive"
□ Copy: Quick Ref → "SKILL.md Template"
□ Define: Clear use case and triggers
□ Create: .claude/skills/my-skill/SKILL.md
□ Test: Trigger skill in conversation
□ Verify: Auto-loading works correctly
□ Document: Examples and best practices
□ Time: 15-20 minutes
```

### Checklist: Creating a Subagent
```
□ Read: Full Guide → "Subagents Deep Dive"
□ Copy: Quick Ref → "Subagent Template"
□ Define: Specific domain and boundaries
□ Create: .claude/agents/my-agent.md
□ Test: @my-agent invocation
□ Verify: Isolated context works
□ Document: When and how to use
□ Time: 10-15 minutes
```

### Checklist: Creating a Slash Command
```
□ Read: Quick Ref → Slash Command section
□ Copy: Slash Command template
□ Create: .claude/commands/[name].md
□ Define: Command name, description, keywords
□ Specify: Arguments (if any)
□ Document: Workflow steps
□ Add: Examples of usage
□ Test: Run /[name] in Claude Code
□ Commit: Add to version control
□ Share: Document in team README
□ Time: 10-15 minutes
```

### Checklist: Creating a Hook
```
□ Read: Full Guide → Hooks: Deep Dive
□ Decide: Hook type (pre-commit, post-deploy, etc.)
□ Copy: Hook template
□ Create: .claude/hooks/[type]-[name].md
□ Define: Event type and name
□ Set: enabled: true, blocking (if needed)
□ Document: Workflow and validation logic
□ Test: Trigger the event manually
□ Configure: .claude/hooks/config.yaml
□ Verify: Hook runs automatically
□ Document: In project documentation
□ Time: 15-20 minutes
```

### Checklist: Setting Up MCP
```
□ Read: Full Guide → "MCP Servers Deep Dive"
□ Choose: Required MCP servers
□ Configure: ~/.claude/config.json
□ Install: MCP server dependencies
□ Test: Connection and tools
□ Document: Available tools for team
□ Train: Team on usage patterns
□ Time: 20-30 minutes
```

### Checklist: Creating a Plugin
```
□ Read: Full Guide → "Plugins Deep Dive"
□ Plan: Component structure
□ Create: .claude-plugin/marketplace.json
□ Develop: Agents, commands, skills
□ Write: install.sh script
□ Test: Installation and functionality
□ Document: README + usage examples
□ Version: Proper versioning
□ Distribute: GitHub or marketplace
□ Time: 60-120 minutes
```

---

## 🔧 Quick Reference: Common Issues

### **"Claude isn't using my AGENTS.md"**
→ Quick Ref: File locations → Check path is `.claude/AGENTS.md`
→ Visual Guide: #3 "When Each Component Is Loaded"

### **"My skill isn't auto-loading"**
→ Full Guide: SKILLS → Check metadata formatting
→ Visual Guide: #7 "Skill Auto-Loading Flowchart"

### **"Subagent not found"**
→ Quick Ref: "Commonly Used Commands" → `/agents`
→ Visual Guide: #2 "Component Lifecycle"

### **"Command not working"**
→ Quick Ref: Slash Command template → Check syntax
→ Visual Guide: #6 "Slash Commands in Action"

### **"Hook not triggering"**
→ Full Guide: Hooks → Check configuration
→ Visual Guide: #6 "Event-Driven Workflow"

### **"Performance is slow"**
→ Visual Guide: #4 "Token Usage Comparison"
→ Full Guide: "Best Practices"

---

## 📞 How to Get Help

### **Quick Questions (2-5 min)**
→ **Quick Ref** → Relevant section
→ **Visual Guide** → Appropriate diagram

### **Detailed Understanding (15-30 min)**
→ **Full Guide** → Detailed section
→ **Visual Guide** → Related diagrams

### **Complex Issues (30+ min)**
→ **Full Guide** → Complete relevant sections
→ **Visual Guide** → All related diagrams
→ **Quick Ref** → Templates and checklists

### **Teaching Others**
→ **README** → Starting point
→ **Visual Guide** → Key diagrams
→ **Quick Ref** → Decision trees and templates

---

## 📈 What to Read Next

### **After Reading README (Beginner)**
1. **Quick Ref** → File locations + Components (10 min)
2. **Visual Guide** → #1 Architecture (5 min)

### **After Basic Setup (Practitioner)**
1. **Full Guide** → Component deep dives (30 min)
2. **Visual Guide** → Integration patterns (15 min)

### **After Daily Use (Advanced)**
1. **Full Guide** → Real-world workflows (15 min)
2. **Visual Guide** → Performance optimization (10 min)

### **When Stuck (Everyone)**
1. **Visual Guide** → #12 Common Gotchas (5 min)
2. **Quick Ref** → Relevant section (5 min)

---

**💡 Tip:** Bookmark this index page! It's your fastest way to find exactly what you need in the Claude Code ecosystem documentation.