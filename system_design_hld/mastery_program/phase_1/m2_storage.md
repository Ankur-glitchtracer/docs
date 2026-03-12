# Module 2: Storage & Database Systems

### 🚀 Problem Statement
A RAG system stores 50M document chunks with embeddings. If PostgreSQL is used for everything — metadata, vector search (pgvector), conversation history, user sessions — queries that were 20ms may eventually take 3 seconds. The single database becomes the bottleneck of the entire GenAI platform.

### 🧠 The Engineering Story

**The Villain:** "The One-Database-To-Rule-Them-All." A postgres instance handles OLTP writes, vector similarity search, full-text search, and analytics. It's a Swiss Army knife being used as a forklift.

**The Hero:** "The Polyglot Persistence Architect." Each data access pattern gets the storage engine optimized for it — vector DB for similarity, KV store for sessions, RDBMS for transactional metadata.

**The Plot:**

1. Profile query patterns: point lookups vs range scans vs similarity search
2. Understand B-Tree vs LSM-Tree vs HNSW indexing trade-offs
3. Model data for each store: normalize for RDBMS, denormalize for document stores
4. Design a coherent data architecture with clear ownership boundaries

**The Twist (Failure):** **The Consistency Nightmare.** Splitting data across multiple stores can lead to challenges; for example, a document update might require writing to postgres (metadata), Pinecone (vectors), Redis (cache invalidation), and Elasticsearch (full-text). If one fails, the system may end up in an inconsistent state.

**Interview Signal:** Can justify storage engine choices based on access patterns, not brand names.

### 🧠 Key Concepts to Master

| Storage Type | When to Use | GenAI Example |
|-------------|-------------|---------------|
| **PostgreSQL** (B-Tree) | Transactional, relational data | Document metadata, user accounts, system data |
| **pgvector / Pinecone / Weaviate** | High-dimensional similarity | Embedding search for RAG retrieval |
| **Redis / Memcached** | Low-latency key-value | Session cache, LLM response cache |
| **Elasticsearch** | Full-text search + inverted index | Hybrid search (keyword + semantic) |
| **S3 / Blob Storage** | Large immutable objects | Raw PDFs, generated reports |
| **ClickHouse / DuckDB** | Columnar analytics (OLAP) | Token usage analytics, cost tracking |

### 📝 Design Exercise
> Design the data layer for a document management system that supports: CRUD on documents, vector search over document chunks, full-text keyword search, real-time collaboration comments, and analytics on usage patterns. Justify every storage choice.
