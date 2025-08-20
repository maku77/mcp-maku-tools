# MCP Maku Tools

An MCP server providing daily tools used by maku.

## Features

- **generate_random_id**: Generate random IDs using charset `23456789abcdefghijkmnopqrstuvwxyz`
  - Default length: 7 characters
  - Excludes easily confused characters (0, 1, l, o)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd mcp-maku-tools

# Install dependencies
uv sync
```

## Usage

### With Claude Code

Add this MCP server to Claude Code:

```bash
claude mcp add mcp-maku-tools uv run main.py --directory /path/to/mcp-maku-tools
```


Or manually edit the ~/.claude.json file:

```js
{
  "mcpServers": {
    "mcp-maku-tools": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/maku/gitwork/maku77/mcp-maku-tools",
        "main.py"
      ]
    }
  },
  // ...
```


### Standalone Usage

```bash
uv run main.py
```

## Available Tools

### generate_random_id

Generates a random ID using safe characters.


**Parameters:**
- `length` (int, optional): Length of the generated ID (default: 7)

generate_random_id(8)  // Returns: "a3k7m9df"
**Example:**

```
generate_random_id(8)  # Returns: "a3k7m9df"
```

## Development

```bash
# Install development dependencies
uv sync --dev

# Run the server
uv run main.py
```
