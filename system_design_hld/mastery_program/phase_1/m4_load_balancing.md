# Module 4: Load Balancing & Reverse Proxies

### 🚀 Problem Statement
A GenAI application has 10 inference worker pods. Short queries (simple lookups) complete in 200ms but may get stuck behind long-running RAG queries (15s). P99 latency can spike to 30s even though average CPU utilization is only 40%.

### 🧠 The Engineering Story

**The Villain:** "The Round-Robin Roulette." A load balancer sends requests in strict rotation. If Worker 3 receives 5 heavy RAG queries in a row, they are queued while workers 7-10 sit idle.

**The Hero:** "The Aware Dispatcher." Uses health-aware, latency-weighted routing with separate queues for fast vs slow operations.

**The Plot:**

1. Understand L4 (TCP) vs L7 (HTTP) load balancing trade-offs
2. Implement health checks that go beyond "is the port open" — check GPU memory, queue depth
3. Separate traffic lanes: lightweight API calls vs heavy inference requests
4. Use consistent hashing for stateful workloads (user sessions, model shards)

**The Twist (Failure):** **The Thundering Herd.** All 10 workers health-check as "healthy" simultaneously. A traffic spike hits, all workers get overwhelmed, all fail health checks, and the load balancer has zero healthy backends.

**Interview Signal:** Can design a load balancing strategy that accounts for heterogeneous request costs.

### 🧠 Key Concepts

| Strategy | Best For | GenAI Scenario |
|----------|----------|----------------|
| **Round Robin** | Homogeneous, fast requests | Static API serving |
| **Least Connections** | Variable processing times | Mixed query complexity |
| **Weighted** | Heterogeneous hardware | GPU vs CPU workers |
| **Consistent Hashing** | Stateful routing | Model shard affinity, KV-cache locality |
| **Queue-based** | Expensive async work | Batch LLM inference jobs |
