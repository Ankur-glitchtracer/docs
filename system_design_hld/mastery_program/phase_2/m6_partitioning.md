# Module 6: Consistent Hashing & Data Partitioning

### 🚀 Problem Statement
A vector database holds 200M embeddings across 20 nodes. Adding a 21st node might cause 95% of the data to reshuffle if `hash(key) % N` is used. During reshuffling, the RAG system might return incomplete results for several hours.

### 🧠 The Engineering Story

**The Villain:** "The Modulo Fallacy." Simple hash-mod partitioning means adding or removing a single node remaps almost every key.

**The Hero:** "The Hash Ring." Consistent hashing maps both keys and nodes onto a ring, so adding a node only remaps `K/N` keys (where K = total keys, N = total nodes).

**The Plot:**

1. Understand the hash ring with virtual nodes for uniform distribution
2. Implement range-based vs hash-based partitioning trade-offs
3. Design a rebalancing strategy that maintains availability during scaling
4. Handle hot partitions (popular documents have 100x more chunks)

**The Twist (Failure):** **The Hot Partition.** A viral compliance document generates 50% of all queries. All its chunks live on 2 nodes. Consistent hashing guarantees even data distribution but not necessarily even load distribution.

**Interview Signal:** Can explain consistent hashing and knows when range partitioning is better (e.g., for time-series data or range scans).

### 📝 Design Exercise
> Design a partitioning strategy for a vector store where:
> 
> 1. embeddings must be co-located by document for batch retrieval
> 2. the system scales from 5 to 50 nodes gracefully
> 3. popular documents don't create hot spots.
