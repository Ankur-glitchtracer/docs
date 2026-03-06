# 🏗️ High-Level Design (HLD) Pillars

At this level, you don't just "add a database"—you justify *which* database and *how* it scales.

## 1. Networking & Load Balancing
- **Load Balancers:** L4 (Transport) vs L7 (Application) load balancing. Consistent Hashing.
- **API Gateways:** Rate limiting, Auth, Request aggregation, Circuit Breaking.
- **Protocols:** HTTP/2 vs gRPC vs WebSockets vs QUIC.
- **DNS:** How global traffic is routed (Anycast, Geolocation).

## 2. Data Persistence & Scaling
- **SQL vs NoSQL:** RDBMS (ACID) vs NoSQL (BASE). Key-Value, Document, Columnar, Graph.
- **Sharding & Partitioning:** Horizontal vs Vertical scaling. Sharding keys and hotspots.
- **Scaling:** Horizontal Sharding, Vertical Scaling, Sharding keys and hotspots.
- **Replication:** Multi-leader, Single-leader, Leaderless (Quorums).
- **Consistency Models:** Eventual, Strong, Causal, and Read-your-writes.

## 3. Caching Strategies
- **Eviction Policies:** LRU, LFU, FIFO.
- **Cache Invalidation:** Write-through, Write-around, Write-back.
- **Content Delivery:** CDNs, Push vs Pull CDN models.
- **Distributed Cache:** Redis Cluster vs Memcached. 

## 4. Asynchronous & Messaging
- **Message Queues:** Kafka vs RabbitMQ (Pull vs Push, ordered vs unordered).
- **Architecture:** Event Sourcing, Change Data Capture (CDC), Pub-Sub.

## 5. Security & Identity
- **Authentication:** OAuth2, OIDC, JWT vs Session-based.
- **Authorization:** RBAC (Role-Based) vs ABAC (Attribute-Based).
- **Encryption:** At rest (AES-256) and In-transit (TLS 1.3).

## 6. Observability & Reliability
- **The Three Pillars:** Metrics, Logging, and Distributed Tracing.
- **CAP Theorem:** Navigating the trade-offs in distributed data.
- **Coordination:** Zookeeper (Leader Election, Distributed Locks).
- **Resilience:** Circuit Breakers, Bulkheads, Retries with Exponential Backoff.
- **Consensus:** Raft vs Paxos (Leader Election).
