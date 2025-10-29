#!/usr/bin/env python3
"""
Claude Code Ecosystem Architect Tools
Helper utilities for generating Claude Code ecosystem components
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ComponentSpec:
    """Specification for a Claude Code ecosystem component"""
    component_type: str  # skill, command, hook, subagent
    name: str
    description: str
    domain: str
    complexity: str  # simple, medium, complex
    frequency: str  # daily, weekly, monthly, occasional
    token_budget: str
    integration_points: List[str]
    requirements: List[str]

class ComponentGenerator:
    """Generates Claude Code ecosystem components"""

    def __init__(self, base_path: str = ".claude"):
        self.base_path = Path(base_path)
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, str]:
        """Load component templates"""
        return {
            "skill": self._get_skill_template(),
            "command": self._get_command_template(),
            "hook": self._get_hook_template(),
            "subagent": self._get_subagent_template()
        }

    def generate_component(self, spec: ComponentSpec) -> str:
        """Generate a component based on specification"""
        template = self.templates.get(spec.component_type)
        if not template:
            raise ValueError(f"Unknown component type: {spec.component_type}")

        # Replace template variables
        content = template.replace("{{NAME}}", spec.name)
        content = content.replace("{{DESCRIPTION}}", spec.description)
        content = content.replace("{{DOMAIN}}", spec.domain)
        content = content.replace("{{COMPLEXITY}}", spec.complexity)
        content = content.replace("{{FREQUENCY}}", spec.frequency)
        content = content.replace("{{TOKEN_BUDGET}}", spec.token_budget)
        content = content.replace("{{REQUIREMENTS}}", "\n".join(f"- {req}" for req in spec.requirements))
        content = content.replace("{{INTEGRATION_POINTS}}", "\n".join(f"- {point}" for point in spec.integration_points))
        content = content.replace("{{DATE}}", datetime.now().strftime("%Y-%m-%d"))

        return content

    def save_component(self, spec: ComponentSpec, content: str) -> Path:
        """Save component to appropriate location"""
        if spec.component_type == "skill":
            dir_path = self.base_path / "skills" / spec.name
            file_path = dir_path / "SKILL.md"
        elif spec.component_type == "command":
            dir_path = self.base_path / "commands"
            file_path = dir_path / f"{spec.name}.md"
        elif spec.component_type == "hook":
            dir_path = self.base_path / "hooks"
            file_path = dir_path / f"{spec.name}.md"
        elif spec.component_type == "subagent":
            dir_path = self.base_path / "agents"
            file_path = dir_path / f"{spec.name}.md"
        else:
            raise ValueError(f"Unknown component type: {spec.component_type}")

        dir_path.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return file_path

    def _get_skill_template(self) -> str:
        return """---
name: {{NAME}}
description: {{DESCRIPTION}}
keywords: [{{DOMAIN}}, automation, {{COMPLEXITY}}, {{FREQUENCY}}]
---

# {{NAME}}

## What This Skill Does
{{DESCRIPTION}}

## Domain Focus
This skill specializes in {{DOMAIN}} with {{COMPLEXITY}} complexity and {{FREQUENCY}} usage patterns.

## When This Skill Auto-Triggers
Claude will automatically use this skill when detecting:
{{REQUIREMENTS}}

## Core Capabilities

### 1. Primary Function
- [Main capability based on requirements]

### 2. Integration Points
{{INTEGRATION_POINTS}}

### 3. Error Handling
- Comprehensive error detection and recovery
- Graceful degradation on failures
- Clear error messaging and user guidance

## Usage Examples

### Example 1: Basic Usage
[Brief example of primary use case]

### Example 2: Advanced Usage
[Complex usage scenario with multiple features]

## Token Usage
Estimated token budget: {{TOKEN_BUDGET}}
- Metadata load: ~30 tokens
- Full content load: ~200-500 tokens
- Context management: Optimized for {{FREQUENCY}} usage

## Best Practices
- Use for {{DOMAIN}} tasks with {{COMPLEXITY}} complexity
- Integrate with other components for complete workflows
- Monitor token usage for {{FREQUENCY}} operations

## Integration with Other Components
{{INTEGRATION_POINTS}}

## Generated: {{DATE}}
"""

    def _get_command_template(self) -> str:
        return """---
name: {{NAME}}
description: {{DESCRIPTION}}
keywords: [{{DOMAIN}}, workflow, manual, {{COMPLEXITY}}]
arguments:
  - name: action
    description: Action to perform
    required: false
    default: default
---

# {{NAME}}

## What This Command Does
{{DESCRIPTION}}

## Usage
`/{{NAME}} [action]`

## Arguments
- **action**: Type of action to perform (default: default)

## Workflow Steps

### 1. Input Validation
- Validate provided arguments
- Check required conditions
- Verify permissions and access

### 2. Core Processing
- Execute primary {{DOMAIN}} workflow
- Handle {{COMPLEXITY}} logic
- Process according to {{FREQUENCY}} patterns

### 3. Integration Coordination
{{INTEGRATION_POINTS}}

### 4. Output Generation
- Format results appropriately
- Provide clear success/failure indication
- Include relevant metrics and status

## Examples

### Basic Usage
`/{{NAME}}`
Performs default action with standard configuration.

### With Arguments
`/{{NAME}} custom`
Performs custom action with specialized handling.

## Error Handling
- Invalid arguments: Clear error message with usage examples
- Permission issues: Guidance on required access
- Processing failures: Recovery suggestions and next steps

## Integration Points
{{INTEGRATION_POINTS}}

## Generated: {{DATE}}
"""

    def _get_hook_template(self) -> str:
        return """---
type: pre-commit
name: {{NAME}}
description: {{DESCRIPTION}}
enabled: true
blocking: true
timeout: 60
---

# {{NAME}}

## What This Hook Does
{{DESCRIPTION}}

## When It Runs
Automatically triggered on commit events for {{DOMAIN}} validation.

## Event Context Available
- Changed files list
- Commit message and metadata
- Branch information
- Author details

## Validation Workflow

### 1. Pre-Checks
- Verify {{DOMAIN}} file patterns
- Check for required configurations
- Validate syntax and structure

### 2. Core Validation
{{REQUIREMENTS}}

### 3. Integration Validation
{{INTEGRATION_POINTS}}

### 4. Reporting
- Generate detailed validation report
- Provide clear pass/fail indication
- Include remediation suggestions for failures

## Success Criteria
- All {{DOMAIN}} validations pass
- Integration points function correctly
- No blocking issues detected

## Failure Handling
- **Blocking Issues**: Prevent commit with clear error messages
- **Warning Issues**: Allow commit with detailed warnings
- **Recovery Guidance**: Provide specific fix recommendations

## Bypass Mechanism
In emergency situations, this hook can be bypassed with:
```bash
git commit --no-verify
```

Use bypass sparingly and address validation issues promptly.

## Configuration
Hook behavior can be configured in `.claude/hooks/config.yaml`:
```yaml
hooks:
  pre-commit:
    enabled: true
    timeout: 60
    hooks:
      - {{NAME}}
```

## Generated: {{DATE}}
"""

    def _get_subagent_template(self) -> str:
        return """---
name: {{NAME}}
description: {{DESCRIPTION}}
keywords: [{{DOMAIN}}, specialist, isolated, {{COMPLEXITY}}]
---

# {{NAME}}

## Specialization Domain
This subagent specializes in {{DOMAIN}} with {{COMPLEXITY}} complexity level.

## What This Subagent Does
{{DESCRIPTION}}

## When to Use This Subagent
Delegate to this subagent when you need:
{{REQUIREMENTS}}

## Core Capabilities

### 1. Expert Knowledge
- Deep {{DOMAIN}} expertise
- Specialized tool access
- Advanced pattern recognition

### 2. Isolated Context
- Dedicated context window for {{DOMAIN}} tasks
- Focused attention without distractions
- Persistent state across complex workflows

### 3. Specialized Tools
{{INTEGRATION_POINTS}}

## Interaction Patterns

### Delegation
Use `@{{NAME}}` to delegate {{DOMAIN}} tasks:
- Clear task specification
- Required context and resources
- Expected deliverables and timeline

### Escalation
This subagent will escalate to main agent when:
- Task scope exceeds specialization
- External authorization required
- Cross-domain coordination needed

## Best Practices for Delegation

### 1. Clear Task Definition
- Specify exact {{DOMAIN}} requirements
- Provide relevant context and constraints
- Define success criteria

### 2. Appropriate Context
- Include necessary background information
- Provide access to required resources
- Set clear boundaries and constraints

### 3. Expectation Management
- Define realistic timelines
- Specify deliverable formats
- Plan for review and iteration

## Integration with Main Agent
{{INTEGRATION_POINTS}}

## Limitations
- Focused on {{DOMAIN}} domain only
- Cannot access tools outside specialization
- Requires main agent for cross-domain tasks

## Generated: {{DATE}}
"""

class RequirementsAnalyzer:
    """Analyzes user requirements to recommend component types"""

    def __init__(self):
        self.trigger_patterns = {
            "skill": [
                r"automatically",
                r"auto-trigger",
                r"when.*detect",
                r"monitor.*and.*act",
                r"continuously"
            ],
            "command": [
                r"/\w+",
                r"run.*workflow",
                r"execute.*command",
                r"user.*triggered",
                r"manual.*control"
            ],
            "hook": [
                r"validate",
                r"check.*before",
                r"prevent.*commit",
                r"quality.*gate",
                r"event.*driven"
            ],
            "subagent": [
                r"specialist",
                r"expert.*in",
                r"isolated.*context",
                r"focused.*task",
                r"dedicated.*agent"
            ]
        }

    def analyze_requirements(self, user_input: str) -> List[str]:
        """Analyze user input to determine required components"""
        user_input = user_input.lower()
        recommendations = []

        for component_type, patterns in self.trigger_patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    if component_type not in recommendations:
                        recommendations.append(component_type)

        return recommendations

    def extract_complexity(self, user_input: str) -> str:
        """Extract complexity level from user input"""
        user_input = user_input.lower()

        if any(word in user_input for word in ["simple", "basic", "straightforward"]):
            return "simple"
        elif any(word in user_input for word in ["complex", "advanced", "sophisticated"]):
            return "complex"
        else:
            return "medium"

    def extract_frequency(self, user_input: str) -> str:
        """Extract usage frequency from user input"""
        user_input = user_input.lower()

        if any(word in user_input for word in ["daily", "constantly", "continuously"]):
            return "daily"
        elif any(word in user_input for word in ["weekly", "regularly"]):
            return "weekly"
        elif any(word in user_input for word in ["monthly", "periodically"]):
            return "monthly"
        else:
            return "occasional"

def estimate_token_budget(component_type: str, complexity: str, frequency: str) -> str:
    """Estimate token budget for a component"""
    base_tokens = {
        "skill": 200,
        "command": 150,
        "hook": 100,
        "subagent": 300
    }

    complexity_multipliers = {
        "simple": 0.7,
        "medium": 1.0,
        "complex": 1.5
    }

    frequency_multipliers = {
        "daily": 0.8,
        "weekly": 1.0,
        "monthly": 1.2,
        "occasional": 1.0
    }

    base = base_tokens.get(component_type, 200)
    complexity_factor = complexity_multipliers.get(complexity, 1.0)
    frequency_factor = frequency_multipliers.get(frequency, 1.0)

    estimated = int(base * complexity_factor * frequency_factor)
    return f"{estimated}-{estimated + 100} tokens"

# Example usage and testing
if __name__ == "__main__":
    # Create a sample component specification
    spec = ComponentSpec(
        component_type="skill",
        name="test-automation",
        description="Automated testing workflow for CI/CD pipelines",
        domain="testing",
        complexity="medium",
        frequency="daily",
        token_budget="200-300 tokens",
        integration_points=["Jenkins integration", "Docker containers", "Test reporting"],
        requirements=["Run unit tests", "Generate coverage reports", "Validate build quality"]
    )

    generator = ComponentGenerator()
    content = generator.generate_component(spec)
    print("Generated component content:")
    print(content[:500] + "..." if len(content) > 500 else content)