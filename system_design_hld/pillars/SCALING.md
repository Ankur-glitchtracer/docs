# 🏗️ HLD Concept: Scaling Reads & Writes

## 📝 Definition
Scaling Reads & Writes encompasses the architectural patterns and techniques used to handle increasing volumes of data retrieval and data ingestion in a distributed system. Because read and write traffic scale at different rates and stress systems in different ways, they require distinct strategies. Scaling reads focuses on returning data to users with low latency, whereas scaling writes focuses on durably and efficiently capturing large volumes of data without overwhelming the storage layer.

## 🚀 Why it matters
As an application grows from hundreds to millions of users, traffic bottlenecks will inevitably emerge. For most applications, read traffic grows much faster than write traffic, frequently reaching a read-to-write ratio of 10:1, 100:1, or even higher. For example, a user on Instagram might post one photo a day (a single write) but view dozens of photos requiring hundreds of database queries for metadata, user info, and engagement metrics (massive reads). Conversely, data-intensive applications like an Ad Click Aggregator might experience a peak of 10,000 clicks per second, creating severe write bottlenecks that can cause individual database servers to hit hard limits, leading to dropped data or system crashes. Understanding how to decouple and independently scale these operations is critical for maintaining system availability and performance.

## ⚖️ Trade-offs & Decisions

| Choice A | Choice B | When to use what? |
| :--- | :--- | :--- |
| **Read Replicas** | **External Cache (e.g., Redis)** | Use **Read Replicas** to horizontally scale read throughput directly at the database layer while maintaining querying flexibility. Use an **External Cache** for heavily accessed, relatively static data to reduce database load and achieve sub-millisecond latencies, but you must accept the complexity of cache invalidation. |
| **Synchronous Writes** | **Asynchronous Writes (Queues)** | Use **Synchronous Writes** when the client requires immediate confirmation that data has been durably persisted to the database. Use **Asynchronous Writes** (via Kafka/Kinesis) to buffer temporary spikes, handle write bursts, or perform load shedding when write volumes overwhelm the database. |
| **Individual Inserts** | **Batching** | Use **Individual Inserts** for low-throughput systems where immediate consistency is necessary. Use **Batching** to group multiple writes together, drastically reducing the per-operation overhead and connection load on the database (often paired with stream processors like Flink). |

## 🛠️ Implementation Strategies

- **Strategy 1: Scaling Reads through a Natural Progression:** When optimizing read paths, start simple and increase complexity only when necessary. First, optimize read performance within your database through indexing and denormalization. Next, scale horizontally by adding read replicas, though you must account for potential replication lag. Finally, for high-volume or global traffic, introduce external caching layers like Redis and CDNs, which requires careful management of cache invalidation strategies and hot keys (where millions of users request the exact same content simultaneously).
- **Strategy 2: Scaling Writes through Partitioning and Sharding:** When single database instances cannot handle the write load, you must partition the data. Horizontal sharding distributes data across multiple servers, while vertical partitioning separates different types of data. The most critical decision here is selecting a good partition key that distributes the load evenly to prevent "hot shards" while keeping related data together for efficient querying.
- **Strategy 3: Mitigating Hot Shards in High-Throughput Ingestion:** In heavily skewed write scenarios (e.g., a viral ad receiving all the clicks), a single shard can become overwhelmed, increasing latency and causing data loss. You can resolve this by updating the partition key to append a random number suffix (e.g., `AdId:0-N`). This spreads the writes for that specific hot entity across multiple partitions, which can later be recombined during aggregation or query time.
- **Strategy 4: Stream Buffering and Pre-aggregation:** For extreme write volumes, place a stream (like Kafka or Kinesis) in front of your storage layer to buffer writes. You can then use a stream processor (like Flink) to aggregate the data in real-time before writing a much smaller, batched payload to the final database (e.g., an OLAP database).

## 🧠 Interview Talk-Track
- **Key Insight:** Always establish the read-to-write ratio early in the interview. Acknowledging that reads and writes require completely different scaling paths demonstrates maturity. For example, explicitly stating that you are separating your read and write services to scale them independently based on asymmetric workloads is a strong senior signal.
- **Common Pitfall:** Jumping immediately to complex distributed architectures like database sharding or external caching clusters before doing the basics. You should always start by mentioning database-level optimizations like proper indexing, as this solves many read bottlenecks without adding distributed system complexity.

!!! abstract "Core Takeaway"
    Scaling reads and writes effectively requires separating the two concerns. Scale reads by moving from database indexes to read replicas to external caches, managing replication lag and cache invalidation along the way. Scale writes by buffering traffic with queues, batching operations, and sharding databases with carefully chosen partition keys to avoid hot spots.
