# Multi-Platform AI Ecosystem Architect

**Universal skill for creating AI CLI ecosystem components across multiple platforms**

## Overview

The `multi-platform-architect` skill is a universal solution that works with Claude Code, Gemini CLI, KiloCode, Goose, OpenAI CLI, and any other AI CLI platform. It automatically detects the current platform and generates appropriate components tailored to each platform's architecture and conventions.

## Supported Platforms

### ✅ Currently Supported
- **Claude Code** (Anthropic) - Token-based ecosystem with skills, commands, hooks, agents
- **Gemini CLI** (Google) - Official `@google/gemini-cli` with JavaScript workflows and prompts
- **KiloCode** - AI-assisted development CLI using OpenAI API with JavaScript automation
- **Goose** - Rust-based AI agent platform (github.com/block/goose) with modular extensions
- **OpenAI CLI** - Third-party OpenAI CLI tools with JavaScript/Python automation

### 🔧 Extensible Architecture
The skill is designed to easily support new platforms:
- Add platform detection patterns
- Create platform-specific templates
- Define component types and structures
- Implement integration patterns

## Key Features

### 🎯 **Automatic Platform Detection**
- Scans for platform-specific directories and files
- Identifies platform capabilities and limitations
- Detects command patterns and syntax
- Falls back to generic templates for unknown platforms

### 🏗️ **Multi-Platform Component Generation**
- Generates platform-appropriate file structures
- Creates platform-specific configuration schemas
- Handles different resource models (tokens vs context)
- Adapts component types to each platform's conventions

### 🔗 **Cross-Platform Integration**
- Designs components that work across multiple platforms
- Creates migration guides between platforms
- Establishes interoperability patterns
- Handles platform-specific limitations gracefully

### 📊 **Resource Optimization**
- Optimizes for platform-specific resource constraints
- Adapts token/context budgets per platform
- Implements progressive disclosure strategies
- Plans efficient loading sequences

## When to Use

### For Cross-Platform Projects
- "Create a workflow that works in Claude Code and Goose"
- "Build components that work across multiple AI CLIs"
- "Generate documentation for both Codex and Gemini-CLI"
- "Design automation that's platform-agnostic"

### For Platform Migration
- "Help me migrate from Claude Code to Goose"
- "Convert my Codex setup to work with Auggie"
- "Migrate components between platforms"
- "Create platform migration tools"

### For Multi-Team Environments
- "Set up workflows for teams using different AI CLIs"
- "Create components that work regardless of platform choice"
- "Build platform-agnostic automation systems"
- "Establish universal best practices"

## Component Types by Platform

| Component Type | Claude Code | Gemini CLI | KiloCode | Goose | OpenAI CLI |
|---------------|-------------|-------------|-----------|-------|------------|
| **Automation** | SKILL.md | JavaScript Workflow | JS Automation | Rust Module | JS/Python Script |
| **User Control** | Command | Context | JSON Task | Command | Task |
| **Validation** | Hook | Config | Config | Extension | Config |
| **Specialization** | Agent | Prompt | Module | Agent | Script |
| **Configuration** | Plugin | Config | YAML Config | Config | YAML Config |

## Usage Examples

### Example 1: Cross-Platform Testing
**Input:** "Create testing automation for Claude Code and Gemini CLI"

**Generated:**
- **Claude Code:** Testing skill + slash commands + quality hooks
- **Gemini CLI:** JavaScript workflow + context configuration + prompts

### Example 2: Multi-Platform Documentation
**Input:** "Build documentation system for Claude Code, KiloCode, and OpenAI CLI"

**Generated:**
- **Claude Code:** Documentation skill + generation commands
- **KiloCode:** JavaScript automation + JSON tasks
- **OpenAI CLI:** Python script + API integration

### Example 3: AI-Assisted Development
**Input:** "Create deployment automation with Docker integration using KiloCode"

**Generated:**
- Migration analysis tools
- Component conversion scripts
- Bridge components for compatibility
- Validation testing framework

## File Structure

```
~/.claude/skills/multi-platform-architect/
├── SKILL.md              # Main skill documentation
├── README.md              # This file
├── tools.py               # Core generation utilities
├── examples.py            # Example generator script
└── templates/             # Platform-specific templates
    ├── claude-code/
    ├── codex/
    ├── auggie/
    ├── kilocode/
    ├── goose/
    ├── gemini-cli/
    └── generic/
```

## Platform Detection

### Directory-Based Detection
```python
def detect_platform():
    platform_checks = [
        ('claude-code', ['.claude/']),
        ('gemini-cli', ['.gemini/', 'gemini-workspace/']),
        ('kilocode', ['.kilocode/', 'kilocode-workspace/']),
        ('goose', ['.goose/', 'goose-workspace/']),
        ('openai-cli', ['.openai/', 'openai-workspace/'])
    ]

    for platform, paths in platform_checks:
        if any(os.path.exists(path) for path in paths):
            return platform
    return 'generic'
```

### Command Pattern Detection
- **Claude Code:** `/command`, `@agent`, automatic
- **Gemini CLI:** `gemini:`, context, workflow
- **KiloCode:** `kilo:`, task, automation
- **Goose:** `goose:`, agent, module
- **OpenAI CLI:** `openai:`, ai, task

## Installation and Setup

### Global Installation (Recommended)
```bash
# Install globally for use in any project
cp -r /path/to/skill ~/.claude/skills/multi-platform-architect/
```

### Project-Specific Installation
```bash
# Install for current project only
cp -r /path/to/skill ./.claude/skills/multi-platform-architect/
```

### Verification
```bash
# Test the skill
python3 ~/.claude/skills/multi-platform-architect/examples.py

# Check platform detection
python3 -c "from tools import PlatformDetector; print(f'Detected: {PlatformDetector.detect_platform()}')"
```

## Using the Skill

### Basic Usage
1. **Describe your needs** in natural language
2. **Let the skill detect your platform** automatically
3. **Receive platform-specific components** tailored to your setup
4. **Follow the generated instructions** for implementation

### Example Interactions
```
User: "I need a testing workflow for my React project"

AI: [Auto-detects platform, generates appropriate components]

User: "Create documentation generation that works in both Claude Code and Goose"

AI: [Generates cross-platform components with integration guides]

User: "Help me migrate my setup from Claude Code to Auggie"

AI: [Analyzes current setup, generates migration tools and bridge components]
```

### Advanced Usage
```
User: "Build a CI/CD pipeline that works across Claude Code, Codex, and Kilocode"

AI: [Generates platform-specific components with cross-platform orchestration]

User: "Create a monitoring system that provides unified alerts regardless of platform"

AI: [Designs platform-agnostic components with unified interfaces]
```

## Platform-Specific Best Practices

### Claude Code
- Focus on token efficiency and progressive loading
- Use slash commands for user-controlled workflows
- Implement hooks for quality gates
- Leverage subagents for specialized tasks

### Codex
- Integrate with Visual Studio ecosystem
- Use workspace configurations for team settings
- Leverage extensions for IDE integration
- Focus on automation within development workflows

### Auggie
- Design agent-based architectures
- Use YAML configurations for declarative workflows
- Implement modular integration patterns
- Focus on task automation and orchestration

### Kilocode
- Create task-based automation systems
- Use JSON configurations for structured data
- Implement workflow orchestration patterns
- Focus on process automation and tool integration

### Goose
- Design modular agent systems
- Use Python modules for extensibility
- Implement memory-efficient workflows
- Focus on command-based interactions

### Gemini-CLI
- Create context-based expertise systems
- Use YAML for structured prompts
- Implement workflow-based automation
- Focus on conversation and context management

## Cross-Platform Features

### 1. Universal Templates
- Generic templates that work with any platform
- Platform-agnostic file structures
- Universal component patterns and best practices

### 2. Migration Tools
- Automated component conversion between platforms
- Bridge components for maintaining functionality
- Validation frameworks for ensuring compatibility
- Migration guides and best practices

### 3. Interoperability Patterns
- Shared configuration formats (YAML, JSON)
- Standardized interfaces between platforms
- Fallback mechanisms for platform failures
- Hybrid component systems leveraging multiple platforms

### 4. Progressive Enhancement
- Basic: Generic templates for universal compatibility
- Intermediate: Platform-specific optimizations
- Advanced: Full platform-native capabilities

## Troubleshooting

### Platform Detection Issues
```bash
# Check what platform is detected
python3 -c "from tools import PlatformDetector; print('Detected:', PlatformDetector.detect_platform())"

# List platform directories
ls -la | grep -E "\.(claude|codex|auggie|kilocode|goose|gemini)"
```

### Component Generation Issues
- **Template not found:** Check platform templates directory
- **File permission errors:** Ensure directory permissions are correct
- **Invalid syntax:** Validate platform-specific syntax requirements

### Cross-Platform Issues
- **Component incompatibility:** Use bridge components
- **Resource limits:** Adapt to platform-specific constraints
- **Integration failures:** Check platform-specific integration patterns

## Extending the Skill

### Adding New Platforms
1. **Add Detection Logic:** Update `PlatformDetector.detect_platform()`
2. **Create Templates:** Build platform-specific template directory
3. **Define Components:** Specify component types and structures
4. **Test Integration:** Verify component generation works correctly

### Creating Custom Components
1. **Analyze Platform:** Understand platform conventions
2. **Design Template:** Create appropriate template format
3. **Implement Generator:** Add generation logic to tools.py
4. **Test Validation:** Ensure components work as expected

### Contributing Templates
1. **Follow Platform Patterns:** Use platform-specific conventions
2. **Include Examples:** Provide clear usage examples
3. **Document Integration:** Explain cross-platform compatibility
4. **Test Thoroughly:** Validate with multiple scenarios

## Community and Support

### Contributing
- **Templates:** Create templates for new platforms
- **Components:** Define new component types
- **Patterns:** Document integration best practices
- **Migration:** Share platform migration experiences

### Getting Help
- **Documentation:** Review this README and SKILL.md
- **Examples:** Run examples.py for demonstration
- **Issues:** Report platform-specific problems
- **Discussions:** Join platform-specific conversations

### Platform Resources
- **Claude Code:** [Official Documentation](https://docs.anthropic.com/claude/docs/)
- **Codex:** [VS Code Marketplace](https://marketplace.visualstudio.com/)
- **Auggie:** [GitHub Repository](https://github.com/auggie-ai/)
- **Kilocode:** [Documentation](https://kilocode.dev/docs/)
- **Goose:** [GitHub Repository](https://github.com/goose-ai/)
- **Gemini-CLI:** [Documentation](https://ai.google.dev/cli)

## Version History

- **v1.0**: Initial release with 6 supported platforms
- Support for automatic platform detection
- Comprehensive template library for all platforms
- Cross-platform integration and migration tools
- Example generation and demonstration scripts

---

This multi-platform architect skill enables you to build powerful AI CLI ecosystem components that work seamlessly across multiple platforms, providing universal automation and integration capabilities regardless of your preferred AI CLI tool.