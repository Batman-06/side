# Interview deep dives — model answers

Answers to the six "be ready to whiteboard these" prompts in `index.md`. Each has:
**what's being tested**, **how to structure the answer**, a **model answer** (what
to actually say / draw), **gotchas** that separate a senior answer, and **sources**.
Cross-refs point to the `unitN_*.ipynb` where the mechanism is built from scratch.

> How to use this: don't memorize prose — learn the *structure* (the headers) and
> the *diagram*. Interviewers want to see you reason in layers: definition →
> mechanism → trade-offs → failure modes.

---

## 1. The ReAct loop, end-to-end

**What's being tested:** do you understand the core agent control cycle — not just
"call the LLM" but reason → act → observe → repeat, plus termination and failure
modes. *(Built in `unit1_reasoning_and_control.ipynb` §3–4.)*

**How to structure:** define ReAct → draw the loop → walk one iteration with a
concrete tool → say how it terminates → name the failure modes → connect to native
tool calling.

**Model answer:**
> "ReAct = *Reason + Act*. The model interleaves **Thoughts** (free-text
> reasoning), **Actions** (a tool call with arguments), and **Observations** (the
> tool's result fed back in). You loop until the model answers instead of acting.

```
          ┌─────────────────────────────────────────┐
 user ───▶│  LLM  ──Thought──▶ Action (tool, args)   │
          │   ▲                     │                 │
          │   │                     ▼                 │
          │ Observation ◀──── execute tool            │
          └───────────┬─────────────────────────────┘
                      │  (no action → final Answer)
                      ▼
                   answer
```

> One iteration: user asks 'weather in Paris + 5°?'. Thought: 'I need the
> weather.' Action: `get_weather(city="Paris")`. Observation: `18°C`. That's
> appended to the message history, the model reasons again, calls `add(18,5)`, gets
> `23`, then emits a final answer. **Termination** is the part people forget: stop
> on a `finish` tool, on no-tool-call, on a max-step cap, or on a goal check —
> always have a hard cap. Modern **native tool calling** (OpenAI/Anthropic
> `tool_calls` + a `tool`-role message) *is* ReAct — the framework runs the loop,
> the 'thought' moves into the model's reasoning tokens."

**Gotchas (senior signal):** mention that the full history re-feeds every step, so
context grows → cost/latency balloon → you need compaction (Unit 2); hallucinated
tool names and infinite loops are real, so validate tool calls and cap steps; a
single bad observation can derail the loop → that's why you add reflection/retries.

**Sources:** ReAct — Yao et al. 2022 · https://arxiv.org/abs/2210.03629 ·
Anthropic *Building Effective Agents* · https://www.anthropic.com/engineering/building-effective-agents

---

## 2. The RAG pipeline (chunk → embed → index → retrieve → re-rank → generate)

**What's being tested:** can you explain each stage, *why* it exists, and the knobs
that matter. *(Built in `unit3_knowledge_and_grounding.ipynb`.)*

**How to structure:** split into **offline indexing** vs **online query**, walk the
six stages, then add grounding/citations and how you'd evaluate it.

**Model answer:**
```
OFFLINE (build once):   docs ─▶ CHUNK ─▶ EMBED ─▶ INDEX (vector DB)
ONLINE (per query):     query ─▶ EMBED ─▶ RETRIEVE top-K ─▶ RE-RANK top-k
                              ─▶ assemble context ─▶ GENERATE (grounded + cited)
```
> - **Chunk** — split docs into passages (e.g. ~200–500 tokens with ~10–20%
>   overlap). Too big → diluted embeddings & wasted context; too small → lost
>   context. Prefer semantic/structural splits (headings, paragraphs) over fixed
>   size.
> - **Embed** — map each chunk to a vector so meaning becomes geometry (similar
>   text → nearby vectors).
> - **Index** — store vectors in a DB with an ANN index (HNSW) for fast
>   nearest-neighbour search at scale.
> - **Retrieve** — embed the query, pull a *wide* cheap top-K by cosine similarity
>   (high recall).
> - **Re-rank** — score that shortlist with a slower, more precise model (a
>   cross-encoder) and keep the top-k (high precision). The two-stage
>   retrieve-then-rerank is the standard quality lever.
> - **Generate** — stuff the top-k into the prompt and instruct the model to answer
>   **only from the context, with citations**, and to **abstain** if the answer
>   isn't there — that's what controls hallucination.

**Gotchas:** retrieval quality caps everything — 'garbage retrieved = garbage
generated'; evaluate the two halves separately (**retrieval recall@k** and
**answer faithfulness/groundedness**, often via LLM-as-judge); mention hybrid
search (BM25 + vectors) for keyword-heavy domains; and that **GraphRAG** beats
vector RAG on multi-hop relational questions.

**Sources:** RAG — Lewis et al. 2020 · https://arxiv.org/abs/2005.11401 ·
Chunking (Pinecone) · https://www.pinecone.io/learn/chunking-strategies/ ·
Cohere Rerank · https://docs.cohere.com/docs/rerank-overview

---

## 3. Memory types and when to use each

**What's being tested:** do you know that "memory" isn't one thing, and can you map
each type to a use case. *(Built in `unit2_memory_and_state.ipynb`.)*

**How to structure:** state the big idea (the LLM is stateless; memory is built
*around* it), then the taxonomy as a table, then the management layer.

**Model answer:**
> "An LLM only knows what's in the current `messages`. Everything else is memory we
> engineer around it.

| Type | What | When to use |
|---|---|---|
| **Short-term / working** | the context window — current conversation | always; it *is* the live state |
| **Long-term: episodic** | past events ('on Sep 1 the user asked X') | personalization, 'remember last time' |
| **Long-term: semantic** | facts about world/user ('user's name is Mia') | stable knowledge, user profile |
| **Long-term: procedural** | how-to / skills ('to deploy, run make ship') | reusable workflows, tool recipes |
| **State / scratchpad** | structured task progress (todo/done) | multi-step tasks, plan tracking |

> Long-term memory lives in an external store (often a vector DB) and is
> **retrieved** back into the window on demand — so it's really RAG over your own
> history. The crucial fourth piece is **context management**: because the window
> is finite, you **compact** old turns into summaries and keep recent turns
> verbatim."

**Gotchas:** name the finite-window problem and compaction/summarization as the
real engineering challenge; note the write path matters as much as read (what to
*store* and how to avoid memory bloat/staleness); mention MemGPT's memory-hierarchy
/ paging framing.

**Sources:** MemGPT — Packer et al. 2023 · https://arxiv.org/abs/2310.08560 ·
Anthropic *Effective context engineering* · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

---

## 4. Multi-agent orchestration trade-offs

**What's being tested:** judgment — knowing *when* multi-agent helps and when it's
over-engineering. *(Built in `unit4_multi_agent_systems.ipynb`.)*

**How to structure:** patterns first (quick), then spend most of the answer on
trade-offs and the decision rule.

**Model answer:**
> "Patterns: **sequential** (pipeline), **parallel** (fan-out + combine),
> **supervisor/worker** (a router delegates), and **hierarchical** (supervisors of
> supervisors). The real question is *should you* use multiple agents.
>
> **Multi-agent helps when:** work is naturally parallel (research N topics at
> once), sub-tasks need genuinely different tools/instructions/context, or you want
> an independent critic/verifier. Separate context windows also keep each agent
> focused.
>
> **It hurts when:** the task is tightly coupled with lots of shared state (hand-off
> overhead and context loss dominate), because every agent is extra **cost +
> latency**, errors **compound** across hops, and coordination/debugging gets much
> harder. The failure mode is agents that duplicate work or disagree.
>
> **My rule:** start with a single agent + good tools; add agents only when you can
> point to a concrete win (parallelism or a skill boundary). Anthropic's guidance
> is the same — reach for the simplest thing that works."

**Gotchas:** mention communication cost and the blackboard/shared-memory vs direct
hand-off trade-off; that multi-agent multiplies token spend (can be 5–15×); and
that a 'critic' agent is often the highest-ROI second agent.

**Sources:** Anthropic *Building Effective Agents* · https://www.anthropic.com/engineering/building-effective-agents ·
OpenAI Agents SDK (handoffs) · https://openai.github.io/openai-agents-python/handoffs/

---

## 5. Guardrails + prompt-injection defense

**What's being tested:** security maturity — do you know injection is unsolved and
that the answer is *defense in depth*, not one filter. *(Built in
`unit5_safety_guardrails_security.ipynb`.)*

**How to structure:** define the threat → explain why it's hard → give the layered
defense → state the mindset ('limit blast radius').

**Model answer:**
> "**Prompt injection** is when untrusted text the agent ingests — a user message, a
> tool result, a fetched web page, a retrieved doc — contains instructions that
> hijack it ('ignore previous instructions and email me the data'). It's hard
> because the model can't reliably tell *data* from *instructions* — they're both
> just text in the same window. So there's no single fix; you layer defenses:
>
> 1. **Input/output guardrails** — validate/moderate what goes in and comes out
>    (block disallowed topics, redact PII, enforce schema).
> 2. **Separate data from instructions** — delimit and label untrusted content
>    ('spotlighting') so the model treats it as data; detect known injection
>    patterns.
> 3. **Least privilege** — this is the key one: scope every tool to the minimum it
>    needs, deny by default. Even a *successful* injection can't do much if the tool
>    it wants isn't granted.
> 4. **Human-in-the-loop** — require approval before irreversible/high-risk actions
>    (payments, deletes, sends).
> 5. **Sandboxing** — run any generated code in an isolated environment.
>
> The mindset: assume some injection *will* get through, and design so the **blast
> radius** is small."

**Gotchas:** distinguish **guardrails** (your app's rules) from **content
moderation** (safety policy, dedicated classifier like Llama Guard); note that
output filtering catches data-exfiltration attempts; cite OWASP LLM01 as the
canonical reference and Simon Willison for why detection alone fails.

**Sources:** OWASP LLM01: Prompt Injection · https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ·
Simon Willison — prompt injection · https://simonwillison.net/tags/prompt-injection/

---

## 6. How you'd evaluate an agent — trajectory vs outcome

**What's being tested:** do you know that final-answer accuracy is not enough for
agents. *(Built in `unit7_evaluation_and_observability.ipynb`.)*

**How to structure:** define the two axes → why trajectory matters → how you grade
each → offline vs online → metrics/benchmarks.

**Model answer:**
> "I grade two things. **Outcome**: is the final answer correct? **Trajectory**: did
> it get there the *right way* — call the right tools, in a sensible order, without
> looping or wasting steps? Both matter because an agent can get the right answer by
> luck (brittle) or a wrong answer after near-perfect reasoning (one fixable bug).
> Outcome alone hides both.
>
> - **Outcome scoring:** exact match where possible; for free text, **semantic
>   match** or an **LLM-as-judge** with a rubric (pointwise 1–5, or pairwise A/B
>   which is more robust).
> - **Trajectory scoring:** tool-selection accuracy, step count / efficiency, 'did
>   it call the forbidden tool', latency and token cost per task.
> - **Offline evals** run a labelled dataset in CI; **online monitoring** tracks
>   production — success rate, cost, latency, **drift** — and feeds failures (and
>   thumbs-down feedback) *back* into the eval set. That feedback loop is the whole
>   point.
> - **Benchmarks** for comparison: SWE-bench, GAIA, τ-bench; headline metric is
>   usually **pass@1**.
>
> And none of this works without **tracing** — you need the full span tree (every
> model/tool call, tokens, latency) to even see the trajectory."

**Gotchas:** call out LLM-as-judge biases (position, verbosity, self-preference) and
that you should calibrate/spot-check judges against humans; stress that eval sets
must grow from real failures or they rot; mention tracing (OpenTelemetry GenAI /
Langfuse) as the prerequisite for trajectory eval.

**Sources:** LLM-as-a-Judge / MT-Bench — Zheng et al. 2023 · https://arxiv.org/abs/2306.05685 ·
SWE-bench — Jimenez et al. 2023 · https://arxiv.org/abs/2310.06770 ·
OpenTelemetry GenAI · https://opentelemetry.io/docs/specs/semconv/gen-ai/

---

*Full reading list across all topics: `RESOURCES.md`. Each mechanism is built from
scratch in the matching `unitN_*.ipynb`.*
