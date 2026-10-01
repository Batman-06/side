# Resources — Agentic AI course

Curated references per unit. Each `unitN_*.ipynb` component also links its key
resources inline; this file is the consolidated, growing index. Updated as new
units are added.

---

## Unit 1 — Reasoning & control (`unit1_reasoning_and_control.ipynb`)

- **ReAct (reason + act)** — Yao et al., 2022 · https://arxiv.org/abs/2210.03629
- **Chain-of-Thought** — Wei et al., 2022 · https://arxiv.org/abs/2201.11903
- **Tree of Thoughts** — Yao et al., 2023 · https://arxiv.org/abs/2305.10601
- **Reflexion (self-reflection)** — Shinn et al., 2023 · https://arxiv.org/abs/2303.11366
- **Plan-and-Solve prompting** — Wang et al., 2023 · https://arxiv.org/abs/2305.04091
- **ReWOO (reasoning without observation)** — Xu et al., 2023 · https://arxiv.org/abs/2305.18323
- **Anthropic — Building Effective Agents** · https://www.anthropic.com/engineering/building-effective-agents
- **LangGraph** (agent loops as graphs) · https://langchain-ai.github.io/langgraph/
- **OpenAI Agents SDK** · https://openai.github.io/openai-agents-python/

## Unit 2 — Memory & state (`unit2_memory_and_state.ipynb`)

- **MemGPT** (memory hierarchy / paging) — Packer et al., 2023 · https://arxiv.org/abs/2310.08560
- **Generative Agents** (episodic memory + reflection) — Park et al., 2023 · https://arxiv.org/abs/2304.03442
- **mem0** (drop-in agent memory) · https://github.com/mem0ai/mem0
- **LangGraph memory concepts** · https://langchain-ai.github.io/langgraph/concepts/memory/
- **Anthropic — Effective context engineering for agents** · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Unit 3 — Knowledge & grounding / RAG (`unit3_knowledge_and_grounding.ipynb`)

- **Original RAG paper** — Lewis et al., 2020 · https://arxiv.org/abs/2005.11401
- **OpenAI embeddings guide** · https://platform.openai.com/docs/guides/embeddings
- **Chunking strategies** (Pinecone) · https://www.pinecone.io/learn/chunking-strategies/
- **Cohere Rerank** (re-ranking) · https://docs.cohere.com/docs/rerank-overview
- **LlamaIndex** (RAG pipelines) · https://docs.llamaindex.ai/
- **Microsoft GraphRAG** · https://github.com/microsoft/graphrag

## Unit 4 — Multi-agent systems (`unit4_multi_agent_systems.ipynb`)

- **OpenAI Agents SDK — handoffs** · https://openai.github.io/openai-agents-python/handoffs/
- **CrewAI** (role-based crews) · https://docs.crewai.com/
- **AutoGen** (Microsoft, conversable agents) · https://microsoft.github.io/autogen/
- **LangGraph multi-agent** · https://langchain-ai.github.io/langgraph/concepts/multi_agent/
- **Google A2A (Agent-to-Agent) protocol** · https://github.com/google/A2A
- **Anthropic — Building Effective Agents** (orchestrator-workers) · https://www.anthropic.com/engineering/building-effective-agents

## Unit 5 — Safety, guardrails & security (`unit5_safety_guardrails_security.ipynb`)

- **OWASP Top 10 for LLM Applications** · https://genai.owasp.org/
- **NIST AI Risk Management Framework** · https://www.nist.gov/itl/ai-risk-management-framework
- **Guardrails AI** · https://github.com/guardrails-ai/guardrails
- **NVIDIA NeMo Guardrails** · https://github.com/NVIDIA/NeMo-Guardrails
- **OpenAI Moderation guide** · https://platform.openai.com/docs/guides/moderation
- **Meta Llama Guard / Purple Llama** · https://github.com/meta-llama/PurpleLlama
- **OWASP LLM01: Prompt Injection** · https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- **Simon Willison — prompt injection** · https://simonwillison.net/tags/prompt-injection/
- **Anthropic tool use docs** · https://docs.anthropic.com/en/docs/build-with-claude/tool-use
- **Model Context Protocol (MCP)** · https://modelcontextprotocol.io/
- **LangGraph human-in-the-loop** · https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
- **E2B code sandbox** · https://e2b.dev/ · **gVisor** · https://gvisor.dev/ · **RestrictedPython** · https://github.com/zopefoundation/RestrictedPython

## Unit 6 — Structured I/O & reliability (`unit6_structured_io_and_reliability.ipynb`)

- **OpenAI Structured Outputs** · https://platform.openai.com/docs/guides/structured-outputs
- **Pydantic** · https://docs.pydantic.dev/
- **Instructor** (structured LLM outputs) · https://github.com/567-labs/instructor
- **Outlines** (constrained decoding) · https://github.com/dottxt-ai/outlines
- **tenacity** (retry library) · https://tenacity.readthedocs.io/
- **OpenAI SDK — retries & timeouts** · https://github.com/openai/openai-python#retries
- **AWS — timeouts, retries & backoff with jitter** · https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- **Stripe — Idempotent requests** · https://docs.stripe.com/api/idempotent_requests
- **microservices.io — Saga pattern** · https://microservices.io/patterns/data/saga.html

## Unit 7 — Evaluation & observability (`unit7_evaluation_and_observability.ipynb`)

- **OpenAI Evals** · https://github.com/openai/evals
- **promptfoo** · https://www.promptfoo.dev/
- **LangSmith — evaluation & tracing** · https://docs.smith.langchain.com/
- **Judging LLM-as-a-Judge / MT-Bench** — Zheng et al., 2023 · https://arxiv.org/abs/2306.05685
- **Anthropic — develop tests & graders** · https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests
- **OpenTelemetry — GenAI semantic conventions** · https://opentelemetry.io/docs/specs/semconv/gen-ai/
- **Langfuse** (tracing, analytics, online eval) · https://langfuse.com/
- **Arize Phoenix** · https://github.com/Arize-ai/phoenix
- **Evidently AI** (drift detection) · https://github.com/evidentlyai/evidently
- **SWE-bench** — Jimenez et al., 2023 · https://arxiv.org/abs/2310.06770
- **GAIA** — Mialon et al., 2023 · https://arxiv.org/abs/2311.12983
- **HELM** (holistic evaluation) · https://crfm.stanford.edu/helm/

## Unit 8 — Cost, latency & efficiency (`unit8_cost_latency_efficiency.ipynb`)

- **OpenAI — Prompt caching** · https://platform.openai.com/docs/guides/prompt-caching
- **Anthropic — Prompt caching** · https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- **OpenAI — Reasoning & effort control** · https://platform.openai.com/docs/guides/reasoning
- **OpenAI — Streaming responses** · https://platform.openai.com/docs/guides/streaming-responses
- **OpenAI — Batch API** · https://platform.openai.com/docs/guides/batch
- **AWS — timeouts, retries & backoff with jitter** · https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

## Unit 9 — Learning & adaptation (`unit9_learning_and_adaptation.ipynb`)

- **OpenAI — Fine-tuning guide** · https://platform.openai.com/docs/guides/fine-tuning
- **InstructGPT (RLHF)** — Ouyang et al., 2022 · https://arxiv.org/abs/2203.02155
- **DPO (Direct Preference Optimization)** — Rafailov et al., 2023 · https://arxiv.org/abs/2305.18290
- **HuggingFace TRL** (SFT/DPO/PPO trainers) · https://github.com/huggingface/trl
- **Self-Refine** — Madaan et al., 2023 · https://arxiv.org/abs/2303.17651
- **Reflexion** — Shinn et al., 2023 · https://arxiv.org/abs/2303.11366
- **Voyager** (skill library / lifelong learning) — Wang et al., 2023 · https://arxiv.org/abs/2305.16291
- **Generative Agents** — Park et al., 2023 · https://arxiv.org/abs/2304.03442
