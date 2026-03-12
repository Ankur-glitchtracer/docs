# Module 11: Observability, Reliability & SRE

### 🚀 Problem Statement
A GenAI platform experienced a 2-hour outage where users reported significant slowness, even though the dashboard showed 99.5% uptime. The root cause was a slow memory leak in the embedding service that gradually degraded response times from 200ms to 12s over three days. No alerts were triggered because the service never crashed; it simply slowed down.

### 🧠 The Engineering Story

**The Villain:** "The Dashboard Liar." Uptime monitoring may report 99.9% because a service returns HTTP 200. However, if those responses take 12 seconds or contain incorrect embeddings because the model ran out of GPU memory, the system is effectively failing.

**The Hero:** "The Observability Triad." Metrics (what), Logs (why), Traces (where) — combined with SLIs/SLOs that measure what users actually experience.

**The Plot:**

1. Define SLIs: latency P50/P95/P99, error rate, throughput, embedding quality score
2. Set SLOs: "99.5% of RAG queries complete in < 3s with relevance > 0.7"
3. Implement distributed tracing across the full RAG pipeline
4. Build alerts on error budgets, not on individual metrics

**The Twist (Failure):** **Alert Fatigue.** Setting too many alerts (e.g., 200) can lead to critical warnings being ignored. A vital alert regarding embedding quality degradation might be buried among dozens of minor warnings like "disk usage > 70%."

**Interview Signal:** Can define meaningful SLIs/SLOs for an ML system and explain error budget policies.

### 🧠 Observability for GenAI Systems

| Signal | What to Measure | Tool |
|--------|----------------|------|
| **Latency** | P50/P99 per pipeline stage (embed, retrieve, generate) | Prometheus + Grafana |
| **Quality** | Relevance score (cosine similarity), faithfulness | Custom metrics + LLM-as-judge |
| **Cost** | Token usage per query, cache hit ratio | Custom counters |
| **Errors** | Rate limit hits, model timeouts, hallucination detection | Structured logging |
| **Traces** | Full request path: API → embed → retrieve → rerank → generate | Jaeger / OpenTelemetry |
