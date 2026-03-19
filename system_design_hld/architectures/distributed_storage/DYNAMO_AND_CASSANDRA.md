# 🗄️ System Design: Distributed NoSQL (Dynamo & Cassandra)

## 📝 Overview
Dynamo (Amazon) and Cassandra (Apache) are foundational distributed NoSQL databases designed to provide extreme high availability, partition tolerance, and massive write throughput at a global scale. By abandoning rigid relational constraints and master-slave architectures, they utilize a peer-to-peer ring topology to ensure the system is "always writeable," even during severe network partitions.

!!! abstract "Core Concepts"
    - **Consistent Hashing:** A distributed routing technique using a ring topology to distribute data evenly across nodes while minimizing data movement when servers are added or removed.
    - **Tunable Consistency (Sloppy Quorum):** Allowing developers to dynamically configure the number of nodes that must acknowledge a read/write operation (`N`, `R`, `W`), trading strict consistency for lower latency.
    - **Anti-Entropy (Merkle Trees):** A background gossip protocol that uses cryptographic hash trees to detect and repair data inconsistencies between replicas.

---

## 🏭 The Scenario & Requirements

### 😡 The Problem (The Villain)
Traditional Relational Databases (RDBMS) enforcing ACID properties cannot easily scale writes horizontally. They rely on complex sharding and Master-Slave replication. If the Master node fails or a network partition isolates a datacenter, the database stops accepting writes to prevent data corruption. For high-scale e-commerce shopping carts or massive IoT ingestion pipelines, rejecting a user's write request is unacceptable and directly impacts revenue.

### 🦸 The Solution (The Hero)
A masterless, highly available distributed data store (AP in the CAP theorem). By utilizing **Consistent Hashing**, every node in the cluster is functionally equal and can accept read/write requests. If a replica node is offline, the system uses **Hinted Handoff** to temporarily store the data on a healthy neighbor, ensuring the application's write operation always succeeds. 

### 📜 Requirements
- **Functional Requirements:**
    1. Clients must be able to securely Put (write) and Get (read) data based on a Primary Key.
    2. The system must support flexible or schema-less data structures (Wide-Column or Key-Value).
    3. The system must automatically replicate data across multiple physical nodes.
- **Non-Functional Requirements:**
    1. **High Availability (Always Writeable):** 99.999% uptime for write operations.
    2. **High Write Throughput:** Capable of absorbing millions of writes per second globally.
    3. **Partition Tolerance:** The cluster must continue to function even if multiple nodes or entire datacenters lose network connectivity.

!!! info "Capacity Estimation (Back-of-the-envelope)"
    - **Traffic:** 100 Million Active Users generating **100,000 writes/sec** and **300,000 reads/sec**.
    - **Storage:** 100,000 writes/sec * 1 KB per record = 100 MB/sec. Over a year, this requires **~3.1 PB of raw storage**.
    - **Replication:** With a standard replication factor of 3 (`N=3`), the total storage footprint scales to **~9.3 PB/year**.
    - **Hardware:** To handle 9.3 PB and distribute the 400k total IOPS, the cluster requires roughly **~500-1000 commodity nodes** (assuming standard SSD throughput and CPU bounds).

---

## 📊 API Design & Data Model

=== "REST APIs / Client Drivers"
    - **`PUT /api/v1/store/{table}`** *(Dynamo/KV style)*
        - **Request:** `{ "key": "user:123:cart", "context": "v2", "value": { "item": "laptop" } }`
        - **Response:** `200 OK` (Acknowledged by `W` nodes)
    - **`GET /api/v1/store/{table}/{key}`**
        - **Response:** `{ "key": "user:123:cart", "context": "v3", "value": {...} }`
    - **`POST /api/v1/query`** *(Cassandra CQL style)*
        - **Request:** `SELECT * FROM users WHERE user_id = '123' AND timestamp > '2023-01-01'`
        - **Response:** `[ { "user_id": "123", "event": "login", ... } ]`

=== "Database Schema"
    - **Dynamo (Key-Value):**
        - `Key` (String, Hashed for partition routing)
        - `Value` (Binary / JSON Blob)
        - `Context` (Vector Clock metadata for conflict resolution)
    - **Cassandra (Wide-Column):**
        - `Partition Key` (String) - *Determines the physical node storing the data.*
        - `Clustering Key` (Timestamp/UUID) - *Determines the sorted order of data on disk.*
        - `Columns` (Dynamic Key-Value pairs)

---

## 🏗️ High-Level Architecture

### Architecture Diagram

```mermaid
graph TD
    Client[Client App] -->|Hash(Key) = 45| LB[Load Balancer / Driver]
    
    LB --> Coordinator[Coordinator Node]
    
    subgraph "Consistent Hashing Ring"
        Coordinator -->|1. Write| N1[Node A <br/> Primary]
        Coordinator -->|2. Replicate| N2[Node B <br/> Replica 1]
        Coordinator -->|3. Replicate| N3[Node C <br/> Replica 2]
        N4[Node D] -.-> N1
    end
    
    N2 -.->|Gossip / Anti-Entropy| N3
```

### Component Walkthrough

1.  **Client / Driver:** The client library hashes the Primary Key to determine exactly where on the ring the data belongs. It can send the request directly to the appropriate node.
2.  **Coordinator Node:** Any node that receives a client request acts as the Coordinator. It identifies the Primary node for the key and the subsequent `N-1` replica nodes on the ring, forwarding the read/write requests to them.
3.  **Sloppy Quorum & Hinted Handoff:** If the Coordinator tries to write to Node B, but Node B is down, the Coordinator writes the data to Node D instead, adding a "hint". When Node B recovers, Node D hands the data back. This ensures the write succeeds even during partial outages.
4.  **Gossip Protocol:** A lightweight, decentralized communication protocol where nodes constantly ping random neighbors to share cluster state, detect failures, and trigger Merkle tree comparisons to heal divergent data.

-----

## 🔬 Deep Dive & Scalability

### Handling Bottlenecks

**Cassandra's High-Throughput Write Path (LSM Tree)**
Cassandra leverages a Log-Structured Merge-Tree to absorb massive write spikes.

1.  **Commit Log:** Data is appended to a sequential log on disk for immediate durability.
2.  **MemTable:** Data is written to an in-memory, sorted binary tree structure. *The write is now complete from the client's perspective.*
3.  **SSTable:** When the MemTable is full, it is flushed to disk as an immutable Sorted String Table (SSTable). Because writes are strictly sequential and never require random disk seeks, write throughput is bound only by network and disk bandwidth.

**Cassandra's Read Path Optimizations**
Because data is spread across multiple immutable SSTables, reading is complex. Cassandra uses a multi-stage filter to prevent unnecessary disk I/O:

1.  **Bloom Filter:** A probabilistic data structure in RAM instantly checks if the key *might* exist in an SSTable or *definitely does not*.
2.  **Key Cache:** Checks RAM for the exact byte offset of the key on disk.
3.  **Partition Index:** Locates the physical partition on disk.
4.  **SSTable Scan:** Reads and merges the actual data fragments.

**Conflict Resolution: Dynamo vs Cassandra**
Because these systems allow writes to multiple replicas simultaneously (during partitions), conflicts are inevitable.

  - **Dynamo (Vector Clocks):** Uses an array of counters `[NodeA: 1, NodeB: 2]` to track version history. If concurrent, conflicting versions are detected (e.g., Alice and Bob update the same shopping cart simultaneously), Dynamo refuses to guess. It returns *both* versions to the client and forces the application layer to reconcile them.
  - **Cassandra (Last-Write-Wins):** Takes a simpler approach. It relies on timestamps generated by the client. If two conflicting writes occur, the one with the highest timestamp simply overwrites the other (LWW).

### ⚖️ Trade-offs

| Feature | Amazon Dynamo | Apache Cassandra |
| :--- | :--- | :--- |
| **Data Model** | Pure Key-Value. Values are opaque blobs. | Wide-Column. Highly structured, allows querying by Clustering Keys. |
| **Conflict Resolution** | Vector Clocks. Pushes reconciliation complexity to the client/application. | Last-Write-Wins (LWW). Simple, but risks silent data loss if client clocks are skewed. |
| **Storage Engine** | Pluggable (e.g., Berkeley DB, MySQL). | Deeply integrated LSM-Tree (MemTables & SSTables) optimized for write-heavy workloads. |

-----

## 🎤 Interview Toolkit

  - **Scale Question:** "Adding a new node to a traditional sharded database requires massive data rebalancing. How does Cassandra avoid this?" -\> *Virtual Nodes (vNodes). Instead of assigning one large token range to a physical machine, the ring is divided into hundreds of smaller vNodes. When a new physical server is added, it assumes ownership of random vNodes scattered across the ring, pulling a tiny fraction of data from many existing servers in parallel, drastically reducing network saturation during scale-up.*
  - **Failure Probe:** "A replica node goes offline for 3 days and misses thousands of writes. Hinted handoffs have expired. How does it catch up when it reboots?" -\> *Anti-Entropy using Merkle Trees. The recovering node compares its Merkle Tree (a cryptographic hash of its data ranges) with a healthy replica. It quickly drills down the tree branches to identify the exact corrupted or missing blocks and transfers only those specific records, minimizing network overhead.*
  - **Edge Case:** "A user deletes a record in Cassandra, but after a node failure and recovery, the deleted record "resurrects" and reappears. Why?" -\> *Tombstone Eviction. Because SSTables are immutable, deletes are actually writes (called Tombstones). If a node is offline longer than the `gc_grace_seconds` setting, the healthy nodes garbage-collect the Tombstone. When the offline node returns, it still has the original data, and because the Tombstone is gone, the data propagates back into the cluster. The fix is to ensure nodes are repaired before the grace period expires.*

## 🔗 Related Architectures

  - [System Design: NoSQL Internals](../../deep_dives/NOSQL_INTERNALS.md) — Deep dive into LSM-Trees, Bloom Filters, and SSTables.
  - [System Design: Conflict Resolution](../../deep_dives/CONFLICT_RESOLUTION.md) — Understanding Vector Clocks, CRDTs, and LWW.
  - [Machine Coding: Kafka Lite](../../../machine_coding/distributed/pub_sub/PROBLEM.md) — Understanding the sequential commit logs that power these storage engines.
