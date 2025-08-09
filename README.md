# MCP Maku Tools

MCP server with daily tools used by maku.

## Features

- **generate_random_id**: Generate random IDs using charset `23456789abcdefghijkmnopqrstuvwxyz`
  - Default length: 7 characters
  - Excludes confusing characters (0, 1, l, o)

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

Add this MCP server to your Claude Code:

```bash
claude mcp add mcp-maku-tools uv run main.py --directory /path/to/mcp-maku-tools
```

### Standalone

```bash
uv run main.py
```

## Available Tools

### generate_random_id

Generate a random ID using safe characters.

**Parameters:**
- `length` (int, optional): Length of the generated ID (default: 7)

**Example:**
```
generate_random_id(8)  // Returns: "a3k7m9df"
```

## Development

```bash
# Install development dependencies
uv sync --dev

# Run the server
uv run main.py
```