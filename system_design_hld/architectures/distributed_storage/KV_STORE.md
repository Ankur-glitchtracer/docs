# 🗝️ System Design: Distributed Key-Value Store

## 📝 Overview
A **Distributed Key-Value Store** is a NoSQL database designed for high-throughput, low-latency access to simple data structures. Unlike relational databases, it prioritizes horizontal scalability and partition tolerance over complex queries and strict ACID transactions.

!!! abstract "Core Concepts"

    - **Partitioning:** Distributing data across multiple nodes using Consistent Hashing.
    - **Replication:** Ensuring data durability and availability through Quorum consensus.
    - **Eventual Consistency:** Prioritizing availability over strong consistency (BASE vs ACID).

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1.  **Core API:** `put(key, value)`, `get(key)`, and `delete(key)`.
2.  **Configurability:** Ability to set consistency levels per operation or per bucket.
3.  **Versioning:** Support for vector clocks or timestamps to resolve conflicts.

### Non-Functional Requirements

1.  **Scalability:** Linear scalability; adding nodes increases capacity proportionally.
2.  **Availability:** 99.999% uptime; the system should prioritize responding to requests over strict consistency (AP system).
3.  **Performance:** Single-digit millisecond latency for reads and writes at the 99th percentile (p99).

## 🧠 The Engineering Story

**The Villain:** "The Metadata Bottleneck." Trying to store 1PB of data in a single SQL table. Performance drops to zero as the index no longer fits in memory, and a single server crash takes down the entire company.

**The Hero:** "The Distributed Ring." Using **Consistent Hashing** to spread data across 1,000 nodes, where no single node is a bottleneck.

**The Plot:**

1. Map Keys and Nodes to a circular hash space ($0$ to $2^{128}-1$).
2. Use **Quorum (N, W, R)** to tune the balance between speed and consistency.
3. Implement **Hinted Handoff** to handle temporary node failures without downtime.
4. Use **LSM Trees** (Log-Structured Merge-Trees) for high-speed writes.

**The Twist (Failure):** **The Hot Shard.** A single key (e.g., "Justin Bieber") gets 1M hits/sec, crushing the specific node responsible for that hash range.

**Interview Signal:** Mastery of **Partitioning Strategy**, **Replication Models**, and the **CAP Theorem**.

## 🏗️ High-Level Architecture
Design a highly scalable and available Key-Value store, similar to DynamoDB, Cassandra, or Riak. The system must be able to handle millions of operations per second with predictable low latency.

### Key Design Challenges:

- **Data Partitioning:** Utilizing Consistent Hashing to minimize data movement when scaling the cluster up or down.
- **Data Replication:** Configuring Quorum parameters (N, W, R) to achieve desired consistency levels (e.g., Strong vs Eventual).
- **Handling Failures:** Implementing Hinted Handoff and Read Repair to recover from transient network partitions.
- **Storage Engine:** Choosing between B-Trees (Read-optimized) vs. LSM Trees (Write-optimized).
- **Consistency:** Navigating the CAP Theorem (AP vs CP) based on business requirements.

## 🔍 Deep Dives
(To be detailed...)

## 📊 Data Modeling & API Design
### Data Model

- **(To be detailed...)**: (To be detailed...)

### API Design

- **(To be detailed...)**: (To be detailed...)

## 📈 Scalability & Bottlenecks
(To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** (To be detailed...)
- **Scale Question:** (To be detailed...)
- **Edge Case Probe:** (To be detailed...)

## Practical Implementation

Explore the low-level implementations of distributed key-value stores and conflict resolution:

* [System Design: S3 Lite](./S3_LITE.md)
* [System Design: NoSQL Internals](./NOSQL_INTERNALS.md)
* [Machine Coding: Cache System](../../../machine_coding/systems/cache_system/PROBLEM.md)
