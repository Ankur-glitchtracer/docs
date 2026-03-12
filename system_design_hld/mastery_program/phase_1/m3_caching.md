# Module 3: Caching — The Art of Not Repeating Work

### 🚀 Problem Statement
A typical RAG query to a GenAI system costs roughly $0.03 (embedding + LLM inference). If 40% of queries are near-identical variations ("What is the system protocol?" vs "Tell me about system protocols"), significant monthly costs can be incurred due to redundant LLM calls.

### 🧠 The Engineering Story

**The Villain:** "The Stateless Amnesiac." Every request is treated as brand new. The system re-embeds the same query, re-retrieves the same documents, and re-generates the same answer — 100 times per day.

**The Hero:** "The Semantic Memory Layer." A multi-tier cache that remembers at every level: exact query matches, semantic near-matches, retrieved context, and generated responses.

**The Plot:**

1. **L1 — Browser/Client Cache:** Cache static assets, previously rendered answers
2. **L2 — CDN/Edge:** Cache common API responses geographically
3. **L3 — Application Cache (Redis):** Exact query → response mapping
4. **L4 — Semantic Cache:** Embedding similarity for near-duplicate queries
5. **L5 — Database Query Cache:** Materialized views for common aggregations

**The Twist (Failure):** **Stale Semantic Cache.** An answer to "What PPE is required for Task 7?" might be cached, but then the enterprise document is revised. The cache could serve outdated information. Cache invalidation for semantic similarity remains a significant challenge.

**Interview Signal:** Can articulate cache invalidation strategies beyond simple TTL.

### 🧠 Key Concepts to Master

| Pattern | Description | GenAI Application |
|---------|-------------|-------------------|
| **Cache-Aside** | App checks cache first, loads from DB on miss | Standard pattern for metadata |
| **Write-Through** | Write to cache + DB simultaneously | Session state consistency |
| **Write-Behind** | Write to cache, async flush to DB | High-throughput logging |
| **Semantic Caching** | Match queries by embedding similarity (cosine > 0.95) | Deduplicate similar LLM queries |
| **Cache Stampede Prevention** | Lock/lease on cache misses | Prevent 1000 concurrent LLM calls for same query |
| **Versioned Cache Keys** | Include document version in cache key | Automatic invalidation on document revisions |

### 📝 Design Exercise
> Design a caching strategy for a RAG pipeline that handles: exact query dedup, semantic near-match dedup, document revision invalidation, and cost tracking of cache hit vs miss savings.
