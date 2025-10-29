# Claude Code Ecosystem Architect (cc-eco-techt)

**Master skill for creating Claude Code ecosystem components**

## Overview

The `cc-eco-techt` skill transforms Claude into a comprehensive ecosystem architect capable of analyzing requirements and generating production-ready components including skills, commands, hooks, and subagents.

## What This Skill Does

### 🔍 **Requirements Analysis**
- Analyzes user requests to determine optimal component types
- Maps requirements to appropriate ecosystem components
- Estimates complexity, frequency, and token requirements
- Designs integration patterns between components

### 🏗️ **Component Generation**
- Generates properly structured SKILL.md files with auto-triggering patterns
- Creates slash commands with argument handling and workflows
- Designs hooks with event context and validation logic
- Architects subagents with specialized expertise domains

### 🔗 **Integration & Optimization**
- Ensures components work together harmoniously
- Optimizes for token usage and performance
- Creates proper file structures and naming conventions
- Designs escalation patterns and error recovery

## When It Auto-Triggers

Claude will automatically use this skill when detecting requests containing:

- "create a workflow for"
- "build a skill to"
- "design an agent for"
- "automate this process"
- "set up project structure"
- "optimize my claude setup"
- "create templates for"
- "generate claude code components"
- "design slash commands"
- "create hooks for"

## Usage Examples

### Example 1: Testing Automation
**User Input:** "I need a comprehensive testing workflow for our React TypeScript project"

**Generated Solution:**
- **Skill:** `react-testing-automation` (auto-triggers on test changes)
- **Command:** `/run-tests [type] [coverage]` (manual execution)
- **Hook:** `pre-commit-test-validation` (commit blocking validation)

### Example 2: Documentation System
**User Input:** "Create a system to automatically generate and update API documentation"

**Generated Solution:**
- **Skill:** `api-documentation-generator` (analyzes code changes)
- **Command:** `/update-docs [section] [format]` (manual updates)
- **Hook:** `post-commit-doc-update` (non-blocking updates)
- **MCP Integration:** GitHub API for deployment

### Example 3: Deployment Pipeline
**User Input:** "I need to automate deployments with safety checks"

**Generated Solution:**
- **Command:** `/deploy [environment] [version]` (workflow automation)
- **Hook:** `pre-deploy-validation` (blocking safety checks)
- **Hook:** `post-deploy-notification` (status updates)

## Component Types Generated

| Component | When to Use | Key Features |
|-----------|-------------|--------------|
| **Skill** | Automatic triggers needed | Auto-detection, progressive loading |
| **Command** | User-controlled workflows | Manual invocation, arguments |
| **Hook** | Event-driven validation | Automatic, can block actions |
| **Subagent** | Specialized expertise needed | Isolated context, focused domain |

## File Structure

```
.claude/skills/cc-eco-techt/
├── SKILL.md              # Main skill documentation
├── README.md              # This file
├── tools.py               # Core generation utilities
├── examples.py            # Example generator script
└── examples/              # Generated example components
    ├── skills/
    ├── commands/
    ├── hooks/
    └── agents/
```

## Tools and Utilities

### tools.py
Core utilities for component generation:
- `ComponentGenerator`: Generates components from specifications
- `RequirementsAnalyzer`: Analyzes user requirements
- `ComponentSpec`: Data structure for component specifications
- Token estimation and optimization utilities

### examples.py
Demonstration script that:
- Generates example components for common use cases
- Shows requirements analysis capabilities
- Provides usage patterns and best practices

## Running Examples

To see the skill in action:

```bash
cd .claude/skills/cc-eco-techt
python examples.py
```

This will generate example components demonstrating:
- Testing automation workflows
- Documentation generation systems
- Deployment pipelines
- Code review specialists
- Security validation hooks
- Performance monitoring commands

## Component Templates

The skill includes comprehensive templates for each component type:

### Skill Template
- Progressive disclosure architecture
- Auto-triggering patterns
- Token optimization
- Integration hooks

### Command Template
- Argument handling with YAML schema
- Step-by-step workflows
- Error handling procedures
- Integration patterns

### Hook Template
- Event context configuration
- Validation logic flows
- Success/failure paths
- User feedback mechanisms

### Subagent Template
- Specialization domain definition
- Isolation boundaries
- Interaction protocols
- Escalation procedures

## Best Practices

### For Generated Components

1. **Progressive Complexity**
   - Start simple, add features incrementally
   - Maintain backward compatibility
   - Plan clear upgrade paths

2. **Token Efficiency**
   - Use progressive disclosure
   - Optimize loading sequences
   - Plan context cleanup

3. **Error Handling**
   - Anticipate common failures
   - Provide clear error messages
   - Implement graceful degradation

4. **User Experience**
   - Intuitive interactions
   - Clear feedback mechanisms
   - Comprehensive examples

### For Using This Skill

1. **Clear Requirements**
   - Specify exactly what you need
   - Provide context about your project
   - Mention frequency and complexity

2. **Integration Planning**
   - Consider how components will work together
   - Plan for existing tools and workflows
   - Think about team adoption

3. **Testing and Validation**
   - Test generated components thoroughly
   - Validate integration with existing setup
   - Monitor performance and token usage

## Advanced Features

### Self-Improving Patterns
Components can include analytics to optimize based on usage patterns.

### Template Library
Growing library of proven templates for common patterns.

### Automated Testing
Components can generate their own validation procedures.

### Performance Monitoring
Built-in token usage tracking and optimization recommendations.

## Troubleshooting

### Common Issues

**Skill Not Auto-Triggering**
- Check that trigger keywords are present in your request
- Ensure skill metadata is properly formatted
- Verify file placement in correct directory

**Generated Components Not Working**
- Validate YAML frontmatter syntax
- Check file paths and naming conventions
- Test with Claude Code session restart

**Token Usage Too High**
- Use progressive disclosure patterns
- Optimize component loading sequences
- Consider breaking complex components into smaller parts

### Getting Help

1. **Check Examples**: Run `python examples.py` to see working examples
2. **Review Templates**: Examine templates in `tools.py`
3. **Validate Structure**: Ensure proper YAML and markdown formatting
4. **Test Incrementally**: Start with simple components before complex ones

## Contributing

To extend this skill:

1. **Add New Templates**: Update `tools.py` with new component types
2. **Enhance Analysis**: Improve requirements analysis patterns
3. **Add Examples**: Create new example generators in `examples.py`
4. **Update Documentation**: Keep this README current with new features

## Version History

- **v1.0**: Initial release with core component generation
- Support for skills, commands, hooks, and subagents
- Comprehensive template library
- Requirements analysis and optimization
- Example generation and demonstration tools

---

This skill transforms Claude into a powerful ecosystem architect, enabling rapid creation of sophisticated Claude Code components tailored to your specific needs and workflows.