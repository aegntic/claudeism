---
name: deploy-app
description: Orchestrates application deployment across multiple environments with validation and rollback
keywords: [deployment, workflow, manual, medium]
arguments:
  - name: action
    description: Action to perform
    required: false
    default: default
---

# deploy-app

## What This Command Does
Orchestrates application deployment across multiple environments with validation and rollback

## Usage
`/deploy-app [action]`

## Arguments
- **action**: Type of action to perform (default: default)

## Workflow Steps

### 1. Input Validation
- Validate provided arguments
- Check required conditions
- Verify permissions and access

### 2. Core Processing
- Execute primary deployment workflow
- Handle medium logic
- Process according to daily patterns

### 3. Integration Coordination
- Docker container management
- Kubernetes orchestration
- Environment configuration management
- Monitoring and alerting systems

### 4. Output Generation
- Format results appropriately
- Provide clear success/failure indication
- Include relevant metrics and status

## Examples

### Basic Usage
`/deploy-app`
Performs default action with standard configuration.

### With Arguments
`/deploy-app custom`
Performs custom action with specialized handling.

## Error Handling
- Invalid arguments: Clear error message with usage examples
- Permission issues: Guidance on required access
- Processing failures: Recovery suggestions and next steps

## Integration Points
- Docker container management
- Kubernetes orchestration
- Environment configuration management
- Monitoring and alerting systems

## Generated: 2025-10-29
