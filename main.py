#!/usr/bin/env python3
"""
MCP Maku Tools - A Model Context Protocol server with useful tools
"""

import random

from fastmcp import FastMCP


def create_server() -> FastMCP:
    """MCPサーバーを生成します"""
    server = FastMCP("mcp-maku-tools")

    @server.tool()
    def generate_random_id(length: int = 7) -> str:
        """指定された文字数のランダムID生成ツールです

        Args:
            length: 生成するIDの長さ（デフォルト: 7）

        Returns:
            生成されたランダムID
        """
        chars = "23456789abcdefghijkmnopqrstuvwxyz"
        return "".join(random.choice(chars) for _ in range(length))

    return server


if __name__ == "__main__":
    # MCPサーバーを起動
    mcp = create_server()
    mcp.run(transport="stdio")
