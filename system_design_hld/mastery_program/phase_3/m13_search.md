# Module 13: Search & Retrieval Systems (Hybrid Search)

### 🚀 Problem Statement
A RAG system that uses pure vector search might struggle with specific queries. For instance, when a user asks "What is the RCD for Task 3 in DOC-2024-0087?", the system might retrieve chunks about general "task management" — semantically similar but factually incorrect. In such cases, exact keyword matching for document reference numbers is essential.

### 🧠 The Engineering Story

**The Villain:** "The Semantic Zealot." Vector search finds "meaning-similar" content but often fails on exact identifiers, code references, acronyms, and proper nouns. A reference like "DOC-2024-0087" may have little semantic meaning to an embedding model.

**The Hero:** "The Hybrid Retriever." Combines BM25 keyword search (exact matches) with vector similarity (semantic understanding), using Reciprocal Rank Fusion to merge results.

**The Plot:**

1. Understand inverted indexes (BM25/TF-IDF) vs vector indexes (HNSW/IVF)
2. Implement Hybrid Search: keyword + semantic with RRF or weighted fusion
3. Add metadata filtering: filter by document type, date range, project
4. Implement re-ranking with a cross-encoder for final result quality

**The Twist (Failure):** **The Re-ranking Bottleneck.** A cross-encoder re-ranker (e.g., a 400M parameter model) might take 500ms to score 100 candidates. At high query volumes (e.g., 50 QPS), this stage can become a significant bottleneck, potentially requiring more GPU resources than the actual LLM generation.

**Interview Signal:** Can explain the retrieval pipeline stages (retrieve → filter → rerank) and justify choices at each stage.

### 🧠 Retrieval Pipeline

| Stage | Method | Candidates | Latency |
|-------|--------|-----------|---------|
| **Stage 1: Sparse Retrieval** | BM25 on inverted index | 10,000 → 1,000 | ~5ms |
| **Stage 2: Dense Retrieval** | ANN on HNSW index | 10M → 1,000 | ~10ms |
| **Stage 3: Fusion** | RRF or weighted merge | 2,000 → 200 | ~1ms |
| **Stage 4: Metadata Filter** | SQL/filter predicates | 200 → 50 | ~2ms |
| **Stage 5: Re-rank** | Cross-encoder model | 50 → 10 | ~100ms |
| Stage 6: Generation | LLM with top-k context | 10 → 1 response | ~2s |

### 🔗 Case Study References
- [S3 Lite Architecture](../../architectures/distributed_storage/S3_LITE.md) — For distributed storage and retrieval patterns.
