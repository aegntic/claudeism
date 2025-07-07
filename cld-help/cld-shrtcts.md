# Claude CLI Shortcuts

A comprehensive list of Claude CLI shortcuts and aliases for enhanced productivity.

## Basic Commands

| Shortcut | Command | Description |
|----------|---------|-------------|
| `cld` | `claude` | Start Claude (main command) |
| `cldp` | `claude -p` | Print mode (non-interactive) |
| `cldc` | `claude --continue` | Continue conversation |
| `cldr` | `claude --resume` | Resume a session |
| `cldv` | `claude -v` | Verbose mode |
| `cldd` | `claude --debug` | Debug mode |

## Quick Combinations

| Shortcut | Command | Description |
|----------|---------|-------------|
| `cldpc` | `claude -p --continue` | Print + continue |
| `cldpr` | `claude -p --resume` | Print + resume |
| `cldvc` | `claude -v --continue` | Verbose + continue |

## Model Selection

| Shortcut | Command | Description |
|----------|---------|-------------|
| `clds` | `claude --model sonnet` | Use Sonnet model |
| `cldo` | `claude --model opus` | Use Opus model |
| `cldo1` | `claude --model claude-3-opus-20240229` | Specific Opus model |
| `clds1` | `claude --model claude-3-5-sonnet-20241022` | Specific Sonnet model |

## Configuration & Management

| Shortcut | Command | Description |
|----------|---------|-------------|
| `cldconf` | `claude config` | Configuration management |
| `cldmcp` | `claude mcp` | MCP server management |
| `cldup` | `claude update` | Update Claude |
| `clddoc` | `claude doctor` | Health check |
| `restcldd` | `pkill -f 'Claude.app' && sleep 2 && open -a Claude` | Restart Claude Desktop |

## Advanced Features

| Shortcut | Command | Description |
|----------|---------|-------------|
| `cldide` | `claude --auto-connect-ide` | Auto-connect to IDE |
| `cldsafe` | `claude --dangerously-skip-permissions` | Skip permissions (use carefully!) |
| `cldae` | `claude --auto-execute` | Auto-execute for safe operations |
| `cldaep` | `claude -p --auto-execute` | Auto-execute + print mode |
| `cldaec` | `claude --auto-execute --continue` | Auto-execute + continue |
| `cldjson` | `claude -p --output-format json` | JSON output mode |
| `cldstream` | `claude -p --output-format stream-json` | Streaming JSON output |

## Utility Functions

### `cld-session()`
Interactive session picker using `fzf` to select from previous conversations.

### `cld-quick()`
Quick one-liner function for fast Claude queries.
```bash
cld-quick "your question here"
```

### `cld-continue-print()`
Continue the conversation in print mode.

### `cld-auto()`
Smart auto-execute function with safety guidance:
```bash
cld-auto "describe what you want Claude to do"
```

### `cld-help()`
Display all available Claude shortcuts and functions.

## Experimental Development

| Shortcut | Command | Description |
|----------|---------|-------------|
| `cldex` | Complex function | Start multi-approach experiment |
| `cldlist` | `ls ~/.claude-experiments/` | List all experiments |
| `cldshow` | Function | Show experiment report |
| `cldexhelp` | Echo help | Experiment system help |

## Usage Tips

1. **Quick Queries**: Use `cld-quick "question"` for fast one-off questions
2. **Safe Auto-Execute**: Use `cld-auto` when you want Claude to perform actions with safety checks
3. **Session Management**: Use `cld-session` to quickly jump between conversations
4. **Model Selection**: Use `clds` for Sonnet (faster) or `cldo` for Opus (more capable)

## Installation

Add these aliases to your shell configuration file (`.zshrc`, `.bashrc`, etc.):

```bash
# Source from: https://github.com/aegntic/claudeism/cld-help/cld-shrtcts.md
# Basic Claude shortcuts
alias cld="claude"
alias cldp="claude -p"
# ... (add all aliases from above)
```

Then reload your shell configuration:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

## Contributing

Feel free to submit PRs with additional useful shortcuts at [aegntic/claudeism](https://github.com/aegntic/claudeism).