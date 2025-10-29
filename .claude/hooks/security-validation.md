---
type: pre-commit
name: security-validation
description: Pre-commit security validation that scans for vulnerabilities, secrets, and security anti-patterns
enabled: true
blocking: true
timeout: 60
---

# security-validation

## What This Hook Does
Pre-commit security validation that scans for vulnerabilities, secrets, and security anti-patterns

## When It Runs
Automatically triggered on commit events for security validation.

## Event Context Available
- Changed files list
- Commit message and metadata
- Branch information
- Author details

## Validation Workflow

### 1. Pre-Checks
- Verify security file patterns
- Check for required configurations
- Validate syntax and structure

### 2. Core Validation
- Scan for exposed secrets and credentials
- Check dependencies for known vulnerabilities
- Validate security coding practices
- Prevent insecure code from being committed
- Provide security remediation guidance

### 3. Integration Validation
- Secret scanning tools
- Dependency vulnerability databases
- Security pattern analysis
- Compliance checking frameworks

### 4. Reporting
- Generate detailed validation report
- Provide clear pass/fail indication
- Include remediation suggestions for failures

## Success Criteria
- All security validations pass
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
      - security-validation
```

## Generated: 2025-10-29
