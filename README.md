# Phase 1 — Agentic AI: tool calling & MCP

A hands-on path that builds the core mechanics **from first principles**, then
shows **how the SOTA libraries package the same thing**. Work through the
notebooks in order.

| # | Notebook | What you learn |
|---|----------|----------------|
| 01 | `01_tool_calling_from_scratch.ipynb` | Tool calling is just: a protocol prompt + a parser + a dispatch loop. Built by hand, driven first by a scripted fake model (no API key), then a real LLM over raw HTTP. |
| 02 | `02_tool_calling_with_sdk.ipynb` | The same loop, but the OpenAI SDK's native structured tool calling — no hand-parsing. |
| 03 | `03_mcp_from_scratch.ipynb` | MCP is JSON-RPC 2.0 over a transport. Build the server (`initialize`/`tools/list`/`tools/call`) and a stdio client by hand. |
| 04 | `04_mcp_with_library.ipynb` | The `mcp` library doing the same in a fraction of the code, plus wiring MCP tools to the LLM. |

### Supporting files
- `mcp_server_raw.py` — MCP server built from scratch (raw JSON-RPC over stdio), used by `03`.
- `mcp_server.py` — MCP server using the `mcp` library, used by `04`.

## Setup

```bash
pip install openai "mcp[cli]" jupyterlab
export OPENAI_API_KEY="sk-..."     # needed for the LLM cells (02, 04, and the real-model cell in 01)
jupyter lab
```

Notebooks `01` (fake-model path) and `03` run **without** any API key.

## The one idea

An LLM is text-in → text-out; it can't run code. "Tool calling" is a loop *you*
run around the model: **describe tools → let the model request one → run it →
feed the result back → repeat.** MCP just standardizes *where the tools live* so
any client can discover and call them. Everything else is ergonomics.
