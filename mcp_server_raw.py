"""
Phase 1 — MCP server built FROM SCRATCH (no `mcp` library).

The point of this file: show that an MCP server is not magic. It is just a
program that speaks JSON-RPC 2.0 over a transport. Here the transport is stdio
(newline-delimited JSON on stdin/stdout), which is the most common MCP transport
and the one Claude Desktop / IDEs use to launch a local server.

The same `handle_message` function is imported by 03_mcp_from_scratch.ipynb to
demonstrate the protocol with plain dicts (no transport), then this file is run
as a subprocess to demonstrate it over a real pipe.

Run standalone:   python mcp_server_raw.py   (then type JSON-RPC lines on stdin)
"""

import sys
import json


# --- the actual tools: plain Python functions -----------------------------
def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


# A tool registry: the function + the JSON schema we advertise to clients.
# (The `mcp` library generates these schemas from type hints; here we write
#  them by hand so nothing is hidden.)
_NUM = {"type": "number"}
TOOLS = {
    "add": {
        "fn": add,
        "description": "Add two numbers and return the sum.",
        "schema": {
            "type": "object",
            "properties": {"a": _NUM, "b": _NUM},
            "required": ["a", "b"],
        },
    },
    "multiply": {
        "fn": multiply,
        "description": "Multiply two numbers and return the product.",
        "schema": {
            "type": "object",
            "properties": {"a": _NUM, "b": _NUM},
            "required": ["a", "b"],
        },
    },
}


def handle_message(msg: dict):
    """Take one JSON-RPC message dict, return a response dict (or None).

    None means "this was a notification, don't reply" — that's part of the
    JSON-RPC spec: messages without an `id` get no response.
    """
    method = msg.get("method")
    msg_id = msg.get("id")

    # 1) Handshake. The client says hello; we announce our capabilities.
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "math-raw", "version": "0.1.0"},
            },
        }

    # 2) A notification (no `id`) — the client confirms it's ready. No reply.
    if method == "notifications/initialized":
        return None

    # 3) Discovery: list every tool with its schema.
    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [
                    {
                        "name": name,
                        "description": t["description"],
                        "inputSchema": t["schema"],
                    }
                    for name, t in TOOLS.items()
                ]
            },
        }

    # 4) Execution: run the requested tool, wrap the result in MCP's content shape.
    if method == "tools/call":
        params = msg.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        if name not in TOOLS:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32602, "message": f"Unknown tool: {name}"},
            }
        result = TOOLS[name]["fn"](**args)
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"content": [{"type": "text", "text": str(result)}]},
        }

    # Anything else: standard JSON-RPC "method not found".
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


def serve_stdio() -> None:
    """Read JSON-RPC requests as lines on stdin; write responses to stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        response = handle_message(json.loads(line))
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    serve_stdio()
