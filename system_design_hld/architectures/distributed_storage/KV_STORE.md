# 🗝️ System Design: Distributed Key-Value Store

## 📝 Overview
A Distributed Key-Value Store is a highly scalable NoSQL database designed for extreme high-throughput, low-latency access to simple data structures. Unlike traditional relational databases, it prioritizes horizontal scalability, operational simplicity, and partition tolerance over complex multi-row queries and strict ACID transactions.

!!! abstract "Core Concepts"
    - **Consistent Hashing:** Distributing data evenly across thousands of nodes using a hash ring, minimizing data movement when nodes join or leave.
    - **Replication & Quorum:** Ensuring data durability and tuning consistency levels by requiring a specific number of nodes ($W$ and $R$) out of the total replicas ($N$) to acknowledge an operation.
    - **Eventual Consistency:** Embracing the CAP Theorem by prioritizing Availability and Partition Tolerance (AP) over strict consistency, using anti-entropy mechanisms to heal divergent data in the background.

---

## 🏭 The Scenario & Requirements

### 😡 The Problem (The Villain)
"The Metadata Bottleneck." Attempting to store 1 Petabyte of session data or user profiles in a single monolithic SQL table. As the data grows, the B-Tree index no longer fits in memory, disk I/O grinds to a halt, and performance drops to zero. Furthermore, a single server crash takes down the entire application, resulting in a catastrophic global outage.

### 🦸 The Solution (The Hero)
"The Distributed Ring." By mapping keys to a theoretical ring and utilizing **Consistent Hashing**, the system spreads 1 PB of data across 1,000 independent commodity nodes. No single node becomes a bottleneck, and read/write loads are perfectly distributed. Data is replicated automatically, and transient failures are handled gracefully using Hinted Handoffs.

### 📜 Requirements
- **Functional Requirements:**
    1. Clients can `put(key, value)`, `get(key)`, and `delete(key)`.
    2. The system must support configurable consistency levels (e.g., Strong vs Eventual) per operation.
    3. The system must handle versioning (e.g., Vector Clocks) to resolve concurrent update conflicts.
- **Non-Functional Requirements:**
    1. **Linear Scalability:** Adding $X$ nodes should increase storage and throughput by $X$ without downtime.
    2. **High Availability:** 99.999% uptime. The system should prioritize responding to requests over strict consistency (AP system).
    3. **Low Latency:** Single-digit millisecond latency for reads and writes at the 99th percentile (p99).

!!! info "Capacity Estimation (Back-of-the-envelope)"
    - **Traffic:** 100 Million Active Users generating **100,000 writes/sec** and **1,000,000 reads/sec**.
    - **Storage:** 100,000 writes/sec * 1 KB per record = 100 MB/sec. Over a year, this requires **~3.1 PB of raw storage**.
    - **Replication:** With a standard replication factor of 3 ($N=3$), the total storage footprint scales to **~9.3 PB/year**.
    - **Hardware:** To handle 9.3 PB and distribute the 1.1M total IOPS, the cluster requires roughly **~500-1000 commodity nodes** (assuming standard SSD throughput and CPU bounds).

---

## 📊 API Design & Data Model

=== "REST APIs"
    - **`PUT /api/v1/kv/{key}`**
        - **Request:** `{ "value": { "session_data": "...", "theme": "dark" }, "context": "v2" }`
        - **Query Params:** `?w=2` (Wait for 2 nodes to acknowledge)
        - **Response:** `200 OK`
    - **`GET /api/v1/kv/{key}`**
        - **Query Params:** `?r=2` (Read from 2 nodes to ensure freshness)
        - **Response:** `{ "value": {...}, "context": "v3" }`
    - **`DELETE /api/v1/kv/{key}`**
        - **Response:** `200 OK`

=== "Database Schema (Logical)"
    - **Table:** `key_value_store`
        - `key` (String / Byte Array) - *Hashed to determine partition location*
        - `value` (Binary / JSON Blob) - *Opaque payload to the database*
        - `context/version` (Vector Clock or Timestamp) - *e.g., `[NodeA:2, NodeB:1]`*
        - `ttl` (Integer) - *Optional Time-To-Live in seconds*

---

## 🏗️ High-Level Architecture



### Architecture Diagram
```mermaid
graph TD
    Client -->|get/put| Router[Client / Gateway Node]
    Router -->|Hash(Key) = K| Coordinator[Coordinator Node]
    
    subgraph "Consistent Hashing Ring"
        Coordinator -->|1. Write Primary| NodeA[Node A]
        Coordinator -->|2. Replicate| NodeB[Node B]
        Coordinator -->|3. Replicate| NodeC[Node C]
        
        NodeD[Node D] -.->|Gossip Protocol| NodeA
    end
```

### Component Walkthrough

1.  **Client / Gateway Node:** Receives the request. Using the cluster's topology map, it hashes the key (e.g., MD5 or MurmurHash) to determine which physical node owns that segment of the hash ring.
2.  **Coordinator Node:** Any node can act as a coordinator. It receives the request, identifies the primary owner and the $N-1$ replica nodes on the ring, and forwards the read/write requests to them in parallel.
3.  **Consistent Hashing Ring:** The logical arrangement of nodes. To prevent uneven data distribution when nodes have different hardware capabilities, physical servers are assigned multiple "Virtual Nodes" (vNodes) scattered across the ring.
4.  **Storage Engine:** The local disk architecture on each node. High-throughput KV stores typically use Log-Structured Merge-Trees (LSM Trees) consisting of in-memory MemTables and on-disk SSTables to ensure writes are strictly sequential and blazing fast.

-----

## 🔬 Deep Dive & Scalability

### Handling Bottlenecks

**Tunable Consistency & Quorums**
Because data is replicated across $N$ nodes, network delays can cause replicas to hold stale data. The system allows clients to tune consistency using a Quorum formula: $R + W > N$.

  - **Strong Consistency:** If $N=3$, setting $W=2$ and $R=2$ guarantees that a read will always overlap with the latest write.
  - **High Availability (Eventual Consistency):** Setting $W=1$ means the write succeeds as long as *one* node accepts it, drastically reducing latency but risking stale reads if $R=1$.

**The Hot Shard (Celebrity Problem)**
A single key (e.g., a viral product ID or a celebrity's profile) gets 1 million hits/sec. Because a single key hashes to a specific node, that physical server is crushed, while the rest of the 1,000-node cluster sits idle.

  - *Solution:* For read-heavy hot shards, place an aggressive LRU Cache (e.g., Redis or Memcached) in front of the KV store. For write-heavy hot shards, the application layer must implement "Salted Keys" (e.g., appending a random number `user:bieber:1`, `user:bieber:2`) to artificially force the data to distribute across multiple nodes, aggregating the results on read.

**Handling Failures (Hinted Handoff & Anti-Entropy)**
If Node B goes offline during a write, the Coordinator writes the data to Node D instead, wrapping it in a "hint" indicating it belongs to Node B. When Node B comes back online, Node D automatically hands the data over. If nodes are offline for extended periods, background "Anti-Entropy" processes use Merkle Trees to quickly identify and synchronize divergent data between replicas.

### ⚖️ Trade-offs

| Decision | Pros | Cons / Limitations |
| :--- | :--- | :--- |
| **Vector Clocks vs Last Write Wins (LWW)** | Vector Clocks mathematically detect concurrent update conflicts and prevent silent data loss. | Pushes the complexity of merging conflicting data back to the client application. |
| **LSM Trees vs B-Trees** | LSM Trees easily absorb 100,000+ writes/sec due to sequential appending. | Suffer from Read Amplification. A single `get()` might require scanning the MemTable and multiple SSTables. |
| **Consistent Hashing vs Range Partitioning** | Evenly distributes load and minimizes data shuffling when scaling the cluster. | Does not support range queries (e.g., `SELECT * WHERE key BETWEEN 1 AND 100`). Keys are purely random access. |

-----

## 🎤 Interview Toolkit

  - **Scale Question:** "You are adding 100 new servers to your 1,000-node cluster. How does data rebalance without downtime?" -\> *Because of Consistent Hashing and Virtual Nodes (vNodes), the new servers are assigned random positions on the ring. They quietly stream tiny fractions of data from hundreds of existing nodes in the background. Once synchronized, the ring topology updates, and the new nodes begin serving traffic.*
  - **Failure Probe:** "A network partition splits your cluster in half. Clients can reach both halves. What happens to a write request?" -\> *If the system is AP (Eventual Consistency), it accepts writes on both sides, causing conflicting versions that must be resolved via Vector Clocks later. If it is CP (Strong Consistency), the side without the majority quorum will reject the write to prevent a split-brain scenario.*
  - **Edge Case:** "Why use a Vector Clock `[NodeA: 1, NodeB: 2]` instead of just a timestamp generated by the client?" -\> *Client device clocks are notoriously out of sync (Clock Drift). If you rely purely on timestamps (Last Write Wins), a client with a delayed clock might overwrite newer data, causing irreversible and silent data loss.*

## 🔗 Related Architectures

  - [System Design: NoSQL Internals](https://www.google.com/search?q=./NOSQL_INTERNALS.md) — Deep dive into LSM-Trees, Bloom Filters, and SSTables.
  - [System Design: S3 Lite](https://www.google.com/search?q=./S3_LITE.md) — How massive distributed object stores partition data.
  - [Machine Coding: Cache System](../../../machine_coding/systems/cache_system/PROBLEM.md) — Localized KV store implementations (LRU/LFU).
