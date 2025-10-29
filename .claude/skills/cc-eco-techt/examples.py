#!/usr/bin/env python3
"""
Claude Code Ecosystem Architect - Example Generator
Demonstrates how to use the cc-eco-techt skill to generate various components
"""

import os
import sys
from pathlib import Path

# Add the skill directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from tools import ComponentGenerator, RequirementsAnalyzer, ComponentSpec, estimate_token_budget

class ExampleGenerator:
    """Generates example components for the cc-eco-techt skill"""

    def __init__(self):
        self.generator = ComponentGenerator()
        self.analyzer = RequirementsAnalyzer()

    def generate_all_examples(self):
        """Generate all example components"""
        examples = [
            self.example_testing_workflow(),
            self.example_documentation_generator(),
            self.example_deployment_pipeline(),
            self.example_code_review_agent(),
            self.example_security_validation_hook(),
            self.example_performance_monitoring_command()
        ]

        created_files = []
        for spec, description in examples:
            try:
                content = self.generator.generate_component(spec)
                file_path = self.generator.save_component(spec, content)
                created_files.append((file_path, description))
                print(f"✅ Created: {file_path}")
                print(f"   {description}")
                print()
            except Exception as e:
                print(f"❌ Failed to create {spec.name}: {e}")
                print()

        return created_files

    def example_testing_workflow(self):
        """Example: Comprehensive testing workflow skill"""
        return ComponentSpec(
            component_type="skill",
            name="testing-automation",
            description="Automated testing workflow that orchestrates unit, integration, and E2E tests with CI/CD integration",
            domain="testing",
            complexity="medium",
            frequency="daily",
            token_budget="250-350 tokens",
            integration_points=[
                "Jenkins/GitHub Actions CI/CD",
                "Docker container orchestration",
                "Test reporting and coverage tools",
                "Slack notifications for test results"
            ],
            requirements=[
                "Automatically detect test file changes",
                "Run appropriate test suites based on changes",
                "Generate comprehensive test reports",
                "Integrate with CI/CD pipeline gates",
                "Provide actionable failure analysis"
            ]
        ), "Complete testing automation skill for CI/CD pipelines"

    def example_documentation_generator(self):
        """Example: API documentation generation skill"""
        return ComponentSpec(
            component_type="skill",
            name="api-docs-generator",
            description="Automatically generates and updates API documentation from code changes with multiple format support",
            domain="documentation",
            complexity="complex",
            frequency="weekly",
            token_budget="300-400 tokens",
            integration_points=[
                "OpenAPI specification generation",
                "Markdown documentation rendering",
                "GitHub Pages deployment",
                "Code analysis and parsing tools"
            ],
            requirements=[
                "Analyze code changes for documentation impact",
                "Generate OpenAPI specifications from source code",
                "Update Markdown documentation files",
                "Deploy to documentation hosting",
                "Maintain consistency across formats"
            ]
        ), "API documentation generation and maintenance system"

    def example_deployment_pipeline(self):
        """Example: Deployment workflow command"""
        return ComponentSpec(
            component_type="command",
            name="deploy-app",
            description="Orchestrates application deployment across multiple environments with validation and rollback",
            domain="deployment",
            complexity="medium",
            frequency="daily",
            token_budget="200-300 tokens",
            integration_points=[
                "Docker container management",
                "Kubernetes orchestration",
                "Environment configuration management",
                "Monitoring and alerting systems"
            ],
            requirements=[
                "Validate deployment prerequisites",
                "Build and package application",
                "Deploy to specified environment",
                "Run post-deployment validation",
                "Provide rollback capabilities"
            ]
        ), "Multi-environment deployment command with safety validations"

    def example_code_review_agent(self):
        """Example: Code review specialist subagent"""
        return ComponentSpec(
            component_type="subagent",
            name="code-reviewer",
            description="Specialist subagent for comprehensive code review with focus on best practices, security, and maintainability",
            domain="code-review",
            complexity="medium",
            frequency="daily",
            token_budget="350-450 tokens",
            integration_points=[
                "Static analysis tools integration",
                "Security vulnerability scanning",
                "Code style and pattern analysis",
                "Documentation quality assessment"
            ],
            requirements=[
                "Review code for best practices compliance",
                "Identify potential security vulnerabilities",
                "Assess code maintainability and readability",
                "Provide actionable improvement suggestions",
                "Validate architectural patterns"
            ]
        ), "Specialized code review subagent with security and quality focus"

    def example_security_validation_hook(self):
        """Example: Security validation hook"""
        return ComponentSpec(
            component_type="hook",
            name="security-validation",
            description="Pre-commit security validation that scans for vulnerabilities, secrets, and security anti-patterns",
            domain="security",
            complexity="medium",
            frequency="daily",
            token_budget="150-250 tokens",
            integration_points=[
                "Secret scanning tools",
                "Dependency vulnerability databases",
                "Security pattern analysis",
                "Compliance checking frameworks"
            ],
            requirements=[
                "Scan for exposed secrets and credentials",
                "Check dependencies for known vulnerabilities",
                "Validate security coding practices",
                "Prevent insecure code from being committed",
                "Provide security remediation guidance"
            ]
        ), "Pre-commit security validation hook for vulnerability prevention"

    def example_performance_monitoring_command(self):
        """Example: Performance monitoring command"""
        return ComponentSpec(
            component_type="command",
            name="monitor-performance",
            description="Monitors application and system performance with real-time metrics and alerting",
            domain="monitoring",
            complexity="simple",
            frequency="daily",
            token_budget="150-200 tokens",
            integration_points=[
                "Application performance monitoring (APM)",
                "System metrics collection",
                "Alerting and notification systems",
                "Log aggregation and analysis"
            ],
            requirements=[
                "Collect performance metrics",
                "Analyze performance trends",
                "Generate performance reports",
                "Alert on performance anomalies",
                "Provide optimization recommendations"
            ]
        ), "Performance monitoring and analysis command"

def generate_skill_demonstration():
    """Generate a demonstration of the skill's capabilities"""
    print("🏗️  Claude Code Ecosystem Architect - Skill Demonstration")
    print("=" * 60)
    print()

    # Create example generator
    example_gen = ExampleGenerator()

    print("📋 Generating example components...")
    print()

    # Generate all examples
    created_files = example_gen.generate_all_examples()

    print("📊 Summary:")
    print(f"   Total components created: {len(created_files)}")
    print()

    # Show breakdown by type
    component_types = {}
    for file_path, _ in created_files:
        component_type = file_path.parent.name
        component_types[component_type] = component_types.get(component_type, 0) + 1

    print("   By component type:")
    for comp_type, count in component_types.items():
        print(f"   - {comp_type}: {count}")
    print()

    print("🎯 Generated Files:")
    for file_path, description in created_files:
        rel_path = file_path.relative_to(Path.cwd())
        print(f"   📄 {rel_path}")
        print(f"      {description}")
    print()

    print("✨ The cc-eco-techt skill has successfully demonstrated its capability")
    print("   to generate comprehensive Claude Code ecosystem components!")
    print()

    return created_files

def analyze_requirements_examples():
    """Demonstrate requirements analysis capabilities"""
    print("🔍 Requirements Analysis Examples")
    print("=" * 40)
    print()

    analyzer = RequirementsAnalyzer()

    examples = [
        "I need a workflow that automatically tests my React app when files change",
        "Create a command to deploy my application to different environments",
        "I want to validate code quality before commits to prevent bad code",
        "Need a specialist agent to review security vulnerabilities in our code",
        "Build a system that generates API docs from our codebase automatically"
    ]

    for i, example in enumerate(examples, 1):
        print(f"Example {i}: {example}")
        recommendations = analyzer.analyze_requirements(example)
        complexity = analyzer.extract_complexity(example)
        frequency = analyzer.extract_frequency(example)

        print(f"   Recommended components: {', '.join(recommendations)}")
        print(f"   Complexity: {complexity}")
        print(f"   Frequency: {frequency}")
        print()

if __name__ == "__main__":
    print("🚀 Claude Code Ecosystem Architect - Example Generator")
    print("=" * 60)
    print()

    # Demonstrate requirements analysis
    analyze_requirements_examples()

    # Generate example components
    generated_files = generate_skill_demonstration()

    print("💡 Next Steps:")
    print("   1. Review the generated components in .claude/ directories")
    print("   2. Test the components with your Claude Code setup")
    print("   3. Customize the templates based on your specific needs")
    print("   4. Use the skill to generate your own custom components")
    print()
    print("📚 Documentation Reference:")
    print("   - SKILL.md: Complete skill documentation")
    print("   - tools.py: Core generation utilities")
    print("   - examples.py: This demonstration script")
    print()