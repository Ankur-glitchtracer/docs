# Distributed Systems Theorems & Constraints

Before designing large-scale systems, architects must understand the foundational theorems and mathematical constraints that govern distributed computing. These principles dictate the unavoidable trade-offs between **latency**, **consistency**, and **availability**.

---

## 1. The CAP Theorem

In a distributed system, network partitions are inevitable (e.g., hardware failures, packet loss). The **CAP theorem** states that a distributed data store can only provide **two of the following three guarantees simultaneously**:

**Consistency (C):**  
Every read receives the most recent write or an error. All nodes see the same data at the same time.

**Availability (A):**  
Every request receives a (non-error) response, without the guarantee that it contains the most recent write.

**Partition Tolerance (P):**  
The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

Because **Partition Tolerance (P)** is a hard requirement over WANs, the real choice is always between **CP** and **AP**.

| System Type | Description | Examples |
|---|---|---|
| **CP** | Chooses consistency over availability. Waits for partitioned nodes, which may result in timeouts. | MongoDB, HBase, Redis, Zookeeper |
| **AP** | Chooses availability over consistency. Returns the most recent local data, which may be stale. | Cassandra, DynamoDB, CouchDB |
| **CA** | Technically impossible in WAN distributed systems. Exists only in local, single-node contexts. | RDBMS (MySQL, Postgres) |

---

## 2. The PACELC Theorem

The **PACELC theorem** extends CAP by addressing system behavior during normal operations (when no partition exists).

**Definition:**

If there is a **Partition (P)**, a distributed system must trade off between **Availability (A)** and **Consistency (C)**;  
**Else (E)**, when the system is running normally, it must trade off between **Latency (L)** and **Consistency (C)**.

### Trade-off Matrix

| Model | Explanation | Examples |
|---|---|---|
| **PA/EL** | In a partition choose **Availability**, otherwise choose **Latency**. Replication is usually asynchronous. | Dynamo, Cassandra |
| **PC/EC** | In a partition choose **Consistency**, otherwise still prefer **Consistency**. Replication is synchronous. | BigTable, HBase |
| **PA/EC** | In a partition choose **Availability**, otherwise prefer **Consistency**. | MongoDB |

---

## 3. Capacity Estimation & Back-of-the-Envelope Math

Designing scalable systems requires estimating resource requirements using rough calculations.

### Core Constants & Time Estimates

- **Seconds in a Day:** 86,400  
- **Seconds in a Year:** ~31.5 Million  
- **Seconds in 50 Years:** ~1.6 Billion (important for generating unique **Epoch-based IDs**)  
- **80/20 Rule:** 20% of data (hot data) typically accounts for 80% of the traffic  

---

### Standard Storage Metrics

- **1 Char** = 1 Byte (ASCII) / 2 Bytes (Unicode)  
- **1 Integer** = 4 Bytes  
- **1 UNIX Timestamp** = 4 Bytes (or 8 Bytes for 64-bit)  
- **1 UUID** = 16 Bytes  

---

### Jeff Dean’s Latency Numbers

Understanding the **orders of magnitude difference** between operations is critical for identifying bottlenecks.

| Operation | Latency | Note |
|---|---|---|
| L1 Cache Reference | 0.5 ns | Fastest |
| Mutex Lock/Unlock | 100 ns | |
| Main Memory Reference | 100 ns | |
| Read 1 MB sequentially from memory | 250 µs | |
| Round trip within same datacenter | 500 µs | |
| Disk seek | 10 ms | Slow |
| Read 1 MB sequentially from disk | 30 ms | |
| Send packet CA → Netherlands → CA | 150 ms | Speed of light limit |
