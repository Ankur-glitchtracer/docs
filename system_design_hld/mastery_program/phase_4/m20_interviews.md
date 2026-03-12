# Module 20: The Interview Battleground — System Design Cases

### 🚀 Purpose
This module ties everything together with 10 system design problems calibrated for senior/staff-level interviews, each with a GenAI twist relevant to real-world engineering challenges.

### 📋 Practice Problems

| # | Problem | Core Concepts Tested | Time |
|---|---------|---------------------|------|
| 1 | **Design a Document Processing Pipeline** | Event streaming, data pipelines, saga patterns | 45 min |
| 2 | **Design a RAG-based Q&A System at Scale** | Vector search, hybrid retrieval, caching, LLM orchestration | 45 min |
| 3 | **Design a Multi-Tenant AI Platform** | Tenant isolation, rate limiting, cost allocation, data residency | 45 min |
| 4 | **Design a Real-Time Collaborative Document Editor** | CRDTs/OT, WebSocket, conflict resolution | 45 min |
| 5 | **Design a URL Shortener** (classic, warm-up) | Hashing, caching, analytics, rate limiting | 30 min |
| 6 | **Design a Notification System** | Queue, fan-out, delivery guarantees, user preferences | 30 min |
| 7 | **Design an AI-Powered Code Review System** | ML serving, streaming, feedback loops | 45 min |
| 8 | **Design a Semantic Search Engine** | Inverted index, HNSW, hybrid search, re-ranking | 45 min |
| 9 | **Design an LLM Gateway / AI Proxy** | Rate limiting, model routing, cost controls, fallback chains | 45 min |
| 10 | **Design a Compliance Audit System** | Event sourcing, immutable logs, access control, versioning | 45 min |

### 🎯 Interview Framework (Use for Every Problem)

```

1. CLARIFY (2 min)
   → Users, scale, latency requirements, cost constraints

2. HIGH-LEVEL DESIGN (5 min)
   → Draw 5-7 boxes, label data flows, identify the "hard part"

3. DEEP DIVE (20 min)
   → Focus on 2-3 components the interviewer cares about
   → Always discuss: data model, API design, scaling bottleneck

4. TRADE-OFFS (5 min)
   → "We could also do X, but Y is better here because..."
   → Demonstrate that alternatives were considered and rejected

5. OPERATIONAL CONCERNS (3 min)
   → Monitoring, failure modes, deployment strategy
   → "If this component fails, here's what happens and how we recover"
```

### 🔗 Case Study References
- [URL Shortener Architecture](../../architectures/utilities/URL_SHORTENER.md) — For fundamental hashing and storage scaling.
- [Ticket Booking Architecture](../../architectures/utilities/TICKET_BOOKING.md) — For high-concurrency reservation systems.
