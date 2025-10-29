#!/usr/bin/env python3
"""
Multi-Platform AI Ecosystem Architect - Examples and Demonstrations

This script demonstrates the capabilities of the multi-platform architect skill
by generating example components for different platforms and use cases.
"""

import os
import sys
import json
from pathlib import Path
from tools import (
    MultiPlatformGenerator,
    PlatformDetector,
    RequirementsAnalyzer,
    ComponentSpec
)

def demo_platform_detection():
    """Demonstrate platform detection capabilities"""
    print("🔍 Platform Detection Demo")
    print("=" * 50)

    detected = PlatformDetector.detect_platform()
    print(f"Detected platform: {detected}")

    # Show all supported platforms
    print("\nSupported platforms:")
    for platform in PlatformDetector.PLATFORMS.keys():
        config = PlatformDetector.get_platform_config(platform)
        print(f"  • {platform}: {config.base_dir}")

    print(f"\nCurrent working directory: {os.getcwd()}")
    print()

def demo_requirements_analysis():
    """Demonstrate requirements analysis capabilities"""
    print("📝 Requirements Analysis Demo")
    print("=" * 50)

    test_inputs = [
        "Create a comprehensive testing automation workflow for our React project",
        "Build a simple deployment script with Docker integration",
        "Design an advanced API documentation generator with GitHub integration",
        "Set up a basic code quality validation tool"
    ]

    platform = PlatformDetector.detect_platform()
    analyzer = RequirementsAnalyzer()

    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nExample {i}: {user_input}")
        requirements = analyzer.analyze_input(user_input, platform)
        print(f"  • Component types: {requirements['component_types']}")
        print(f"  • Complexity: {requirements['complexity']}")
        print(f"  • Name: {requirements['name']}")
        print(f"  • Integration needs: {requirements['integration_needs']}")

def demo_component_generation():
    """Demonstrate component generation for current platform"""
    print("\n🏗️ Component Generation Demo")
    print("=" * 50)

    generator = MultiPlatformGenerator()
    platform = PlatformDetector.detect_platform()

    # Test different types of requests
    test_cases = [
        {
            "input": "Create a deployment automation tool with Docker and Kubernetes integration",
            "description": "Complex automation with multiple integrations"
        },
        {
            "input": "Build a simple code quality validator",
            "description": "Simple validation tool"
        },
        {
            "input": "Design an API documentation generator with GitHub integration",
            "description": "Medium complexity specialist tool"
        }
    ]

    output_dir = Path.cwd() / "generated-examples"
    output_dir.mkdir(exist_ok=True)

    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case['description']}")
        print(f"Input: {test_case['input']}")

        try:
            components = generator.generate_from_input(test_case['input'])

            for j, (platform_name, filename, content) in enumerate(components, 1):
                print(f"  • Generated {platform_name} component: {filename}")

                # Save to file for inspection
                platform_dir = output_dir / f"{platform_name}-{i}"
                platform_dir.mkdir(exist_ok=True)

                filepath = platform_dir / filename
                with open(filepath, 'w') as f:
                    f.write(content)

                # Show first few lines of content
                lines = content.split('\n')[:5]
                print(f"    Preview: {lines[0]}")
                for line in lines[1:]:
                    if line.strip():
                        print(f"             {line}")
                print(f"    Full file saved to: {filepath}")

        except Exception as e:
            print(f"  ❌ Error: {e}")

def demo_cross_platform_generation():
    """Demonstrate cross-platform component generation"""
    print("\n🌐 Cross-Platform Generation Demo")
    print("=" * 50)

    generator = MultiPlatformGenerator()

    # A single test case for all platforms
    test_input = "Create a deployment automation tool with Docker integration"
    platforms = ['claude-code', 'github-copilot', 'goose', 'generic']

    print(f"Input: {test_input}")
    print(f"Generating for platforms: {', '.join(platforms)}")

    output_dir = Path.cwd() / "cross-platform-examples"
    output_dir.mkdir(exist_ok=True)

    try:
        components = generator.generate_cross_platform(test_input, platforms)

        platform_groups = {}
        for platform_name, filename, content in components:
            if platform_name not in platform_groups:
                platform_groups[platform_name] = []
            platform_groups[platform_name].append((filename, content))

        for platform_name, files in platform_groups.items():
            print(f"\n📁 {platform_name.upper()}:")
            platform_dir = output_dir / platform_name
            platform_dir.mkdir(exist_ok=True)

            for filename, content in files:
                print(f"  • {filename}")

                # Save file
                filepath = platform_dir / filename
                with open(filepath, 'w') as f:
                    f.write(content)

                # Show file size
                size = len(content)
                print(f"    Size: {size} characters")

    except Exception as e:
        print(f"❌ Error in cross-platform generation: {e}")

def demo_platform_specific_features():
    """Demonstrate platform-specific features and capabilities"""
    print("\n⚡ Platform-Specific Features Demo")
    print("=" * 50)

    platforms = ['claude-code', 'github-copilot', 'goose', 'generic']

    for platform in platforms:
        config = PlatformDetector.get_platform_config(platform)
        print(f"\n🔧 {platform.upper()}:")
        print(f"  • Base directory: {config.base_dir}")
        print(f"  • Resource model: {config.resource_model}")
        print(f"  • Syntax format: {config.syntax_format}")
        print(f"  • Trigger patterns: {', '.join(config.trigger_patterns)}")
        print(f"  • Component types: {len(config.component_types)} defined")

        # Show component mapping
        for comp_type, comp_file in config.component_types.items():
            print(f"    - {comp_type}: {comp_file}")

def demo_integration_detection():
    """Demonstrate integration detection capabilities"""
    print("\n🔗 Integration Detection Demo")
    print("=" * 50)

    test_inputs = [
        "Create a CI/CD pipeline with Docker, Kubernetes, and GitHub Actions",
        "Build a monitoring system with database and API integrations",
        "Design a deployment tool with container orchestration",
        "Set up a simple local development environment"
    ]

    analyzer = RequirementsAnalyzer()

    for i, user_input in enumerate(test_inputs, 1):
        print(f"\nTest {i}: {user_input}")
        integrations = analyzer._detect_integration_needs(user_input)
        print(f"  • Detected integrations: {integrations}")

def demo_file_generation_preview():
    """Preview what files would be generated"""
    print("\n📄 File Generation Preview Demo")
    print("=" * 50)

    generator = MultiPlatformGenerator()

    # Create a detailed test case
    test_input = 'Create a "deploy-app" automation tool with Docker and Kubernetes integration'
    platform = PlatformDetector.detect_platform()

    print(f"Input: {test_input}")
    print(f"Target platform: {platform}")

    try:
        components = generator.generate_from_input(test_input)

        for platform_name, filename, content in components:
            print(f"\n📄 {filename} ({platform_name}):")
            print("-" * 40)

            # Show key sections of the file
            lines = content.split('\n')

            # Show YAML frontmatter if present
            if lines and lines[0].startswith('---'):
                print("Frontmatter:")
                for i, line in enumerate(lines):
                    if line == '---' and i > 0:
                        break
                    print(f"  {line}")
                print()

            # Show description section
            for line in lines:
                if any(keyword in line.lower() for keyword in ['description:', 'what this', '## description']):
                    print(f"Description: {line.strip()}")
                    break

            # Show file size
            print(f"File size: {len(content)} characters")
            print(f"Lines: {len(lines)}")

    except Exception as e:
        print(f"❌ Error: {e}")

def run_interactive_demo():
    """Run an interactive demo where user can input their own requests"""
    print("\n🎮 Interactive Demo")
    print("=" * 50)
    print("Enter your own component descriptions (or 'quit' to exit)")

    generator = MultiPlatformGenerator()
    output_dir = Path.cwd() / "interactive-examples"
    output_dir.mkdir(exist_ok=True)

    while True:
        try:
            user_input = input("\n> ").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                break

            if not user_input:
                continue

            print(f"\nGenerating components for: {user_input}")

            components = generator.generate_from_input(user_input)

            for i, (platform_name, filename, content) in enumerate(components, 1):
                print(f"  {i}. {platform_name}: {filename}")

                # Save file
                timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
                interactive_dir = output_dir / f"session-{timestamp}"
                interactive_dir.mkdir(exist_ok=True)

                filepath = interactive_dir / filename
                with open(filepath, 'w') as f:
                    f.write(content)

                print(f"     Saved: {filepath}")

        except KeyboardInterrupt:
            print("\n\nExiting interactive demo...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main function to run all demos"""
    print("🚀 Multi-Platform AI Ecosystem Architect - Examples")
    print("=" * 60)
    print("This script demonstrates the multi-platform architect capabilities")
    print("by generating example components for different AI CLI platforms.\n")

    # Check if we're in the right directory
    skill_dir = Path(__file__).parent
    if skill_dir.name != "multi-platform-architect":
        print("⚠️ Warning: Run this script from the multi-platform-architect directory")

    # Run all demos
    demo_platform_detection()
    demo_requirements_analysis()
    demo_component_generation()
    demo_cross_platform_generation()
    demo_platform_specific_features()
    demo_integration_detection()
    demo_file_generation_preview()

    # Offer interactive demo
    try:
        response = input("\n🎮 Run interactive demo? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            run_interactive_demo()
    except KeyboardInterrupt:
        pass

    print("\n✅ Demo completed!")
    print("\nGenerated files are saved in:")
    print("  • generated-examples/ - Single platform examples")
    print("  • cross-platform-examples/ - Multi-platform examples")
    print("  • interactive-examples/ - Interactive session output")

if __name__ == "__main__":
    # Import datetime for the interactive demo
    from datetime import datetime

    main()