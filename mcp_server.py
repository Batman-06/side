"""
Phase 1 — MCP server with multiple math tools.

MCP (Model Context Protocol) lets you expose a set of "tools" from a server
that any MCP-aware client (a notebook, Claude Desktop, an IDE, an LLM app...)
can discover and call. Instead of hard-coding tool functions inside one script,
you publish them once here and reuse them everywhere.

This file is imported by 02_mcp.ipynb (in-process demo) AND can be run as a
real standalone server over stdio:

    python mcp_server.py

Uses mcp 2.x  ->  MCPServer (was called FastMCP in mcp 1.x).
"""

from mcp.server.mcpserver import MCPServer

# The server object. The name shows up when a client inspects the server.
mcp = MCPServer("math-tools")


# Each @mcp.tool() turns a plain typed Python function into an MCP tool.
# The type hints (a: float, b: float) become the tool's JSON input schema
# automatically, and the docstring becomes the tool description the LLM reads.

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a (a - b)."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the product."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the given exponent (base ** exponent)."""
    return base ** exponent


if __name__ == "__main__":
    # Run as a real MCP server over stdio. A client (or Claude Desktop, etc.)
    # launches this process and talks to it over stdin/stdout.
    mcp.run(transport="stdio")
