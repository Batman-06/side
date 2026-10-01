# Agentic AI — Components Index (interview prep)

A study map of agentic AI components (excluding deployment/infra). Grouped by
area. ✅ = built in Phase 1 of this repo (see `README.md`).

## 1. Reasoning & control (the "brain")
- **LLM / model choice** — the reasoning engine; capability vs cost/latency, small vs large.
- **System prompt / instructions** — role, constraints, behavior shaping.
- **The agent loop** — perceive → reason → act → observe → repeat (the core control cycle).
- **Reasoning patterns** — ReAct (reason+act), Chain-of-Thought, Tree-of-Thoughts, Reflexion/self-reflection, Plan-and-Execute, ReWOO.
- **Planning & task decomposition** — breaking a goal into ordered subtasks; static vs dynamic replanning.
- **Routing** — deciding which model/tool/sub-agent handles a request.
- **Termination / stopping conditions** — when the loop ends (max steps, goal met, no more tool calls).

## 2. Tools & actions (the "hands")
- **Tool / function calling** ✅ — schemas, when the model decides to call, executing + feeding results back.
- **MCP** ✅ — standard protocol to publish/discover tools across servers.
- **Code execution / sandboxing** — running generated code safely.
- **Computer use / browser automation** — GUI/web interaction.
- **Retrieval as a tool** — search/lookup exposed as a callable.

## 3. Memory & state
- **Short-term / working memory** — the context window; the current conversation.
- **Long-term memory** — persisted across sessions: **episodic** (past events), **semantic** (facts), **procedural** (how-to/skills).
- **Context management / engineering** — summarization, **compaction**, context editing, what to keep vs drop.
- **State management** — tracking progress, scratchpad, intermediate results.

## 4. Knowledge & grounding
- **RAG (retrieval-augmented generation)** — inject external knowledge at query time.
- **Embeddings & vector databases** — semantic search backbone.
- **Chunking, indexing, re-ranking** — the retrieval pipeline.
- **Knowledge graphs** — structured/relational grounding (GraphRAG).
- **Hallucination mitigation / grounding + citations**.

## 5. Multi-agent systems
- **Orchestration patterns** — supervisor/worker, hierarchical, sequential, parallel.
- **Roles & specialization** — planner, researcher, coder, critic.
- **Handoffs & delegation** — passing control/subtasks.
- **Agent-to-agent communication** — A2A protocols, shared memory/blackboard.

## 6. Safety, guardrails & security
- **Guardrails** — input/output validation and filtering.
- **Content moderation / policy checks**.
- **Prompt-injection & jailbreak defense**.
- **Permissions / authorization / least privilege** — what a tool is allowed to do.
- **Human-in-the-loop / approval gates** — confirm before irreversible actions.
- **Sandboxing & isolation**.

## 7. Structured I/O & reliability
- **Structured outputs** — JSON schema / constrained decoding, output parsing.
- **Error handling** — retries, fallbacks, timeouts, graceful degradation.
- **Idempotency & rollback** — safe re-execution of actions.

## 8. Evaluation & observability
- **Evals** — task success rate, **trajectory/step evaluation**, not just final answer.
- **LLM-as-judge** — model-graded evaluation.
- **Tracing / logging / observability** — inspecting the full run (spans, tool calls, tokens).
- **Monitoring & feedback loops** — production drift, cost/latency dashboards.
- **Benchmarks** — SWE-bench, GAIA, etc.

## 9. Cost, latency & efficiency
- **Prompt caching** — reuse stable prefixes.
- **Token budgets / effort control** — bounding spend per task.
- **Streaming** — responsiveness.
- **Batching**.

## 10. Learning & adaptation
- **Fine-tuning / instruction tuning**.
- **RLHF / preference optimization**.
- **Self-correction / critique loops**.
- **Skill acquisition / memory-based learning** — agent improving from past runs.

---

## Interview-favorite deep dives
Be ready to whiteboard these:
- The **ReAct loop** end-to-end.
- The **RAG pipeline** (chunk → embed → index → retrieve → re-rank → generate).
- **Memory types** and when to use each.
- **Multi-agent orchestration** trade-offs.
- **Guardrails + prompt-injection** defense.
- **How you'd evaluate an agent** — trajectory vs outcome.
