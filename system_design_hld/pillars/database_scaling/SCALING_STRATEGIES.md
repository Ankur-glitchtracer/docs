# 🗄️ HLD: Database Scaling & Caching

## 📝 Overview
Scaling a database is one of the hardest challenges in HLD. This module covers techniques for handling massive read/write loads and ensuring high availability.

!!! abstract "Core Concepts"
    - **Sharding:** Horizontal partitioning. Choosing a shard key and avoiding hotspots.
    - **Consistent Hashing:** Minimizing data movement during re-sharding.
    - **Replication:** Active-Passive vs. Active-Active setups.
    - **Indexing:** B-Trees, LSM Trees, and how they impact query speed vs. write speed.

## 🚀 Strategies
### 1. Caching Strategies
- **Cache-Aside:** Application manages cache.
- **Write-Through:** Cache updated synchronously with DB.
- **Write-Back:** Cache updated first, DB updated asynchronously (high performance, risk of data loss).

### 2. Distributed Transactions
- **Two-Phase Commit (2PC):** Strong consistency, high latency, blocking.
- **Three-Phase Commit (3PC):** Non-blocking but higher complexity.

### 3. Concurrency Control
- **Optimistic Concurrency:** Versioning (e.g., `version_id`). Best for low contention.
- **Pessimistic Concurrency:** Locks (e.g., `SELECT FOR UPDATE`). Best for high contention.
- **Two-Phase Locking (2PL):** Ensuring serializability.
