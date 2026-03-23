# Distributed Systems Theorems & Patterns

Before designing large-scale systems, architects must understand the foundational theorems and mathematical constraints that govern distributed computing. These principles dictate the unavoidable trade-offs between **latency**, **consistency**, and **availability**.

---

## 1. The CAP Theorem

In a distributed system, network partitions are inevitable (e.g., hardware failures, packet loss). The **CAP theorem** states that a distributed data store can only provide **two of the following three guarantees simultaneously**:

* **Consistency (C):** Every read receives the most recent write or an error. All nodes see the same data at the same time.
* **Availability (A):** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
* **Partition Tolerance (P):** The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

Because networks aren't reliable, distributed systems must support partition tolerance. You will need to make a software tradeoff between consistency and availability.

| System Type | Description | Examples |
|---|---|---|
| **CP** | Chooses consistency over availability. Waits for a response from the partitioned node, which might result in a timeout error. | MongoDB, HBase, Redis, Zookeeper |
| **AP** | Chooses availability over consistency. Responses return the most readily available version of the data available on any node, which might not be the latest. | Cassandra, DynamoDB, CouchDB |
| **CA** | Technically impossible in WAN distributed systems. Exists only in local, single-node contexts. | RDBMS (MySQL, Postgres) |

---

## 2. Consistency Patterns

With multiple copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data:

* **Weak Consistency:** After a write, reads may or may not see it. A best effort approach is taken. This approach is seen in systems such as memcached and works well in real time use cases such as VoIP, video chat, and realtime multiplayer games.
* **Eventual Consistency:** After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously. This approach is seen in systems such as DNS and email, and works well in highly available systems.
* **Strong Consistency:** After a write, reads will see it. Data is replicated synchronously. This approach is seen in file systems and RDBMSes, and works well in systems that need transactions.

---

## 3. Availability Patterns

There are two complementary patterns to support high availability: fail-over and replication.

### Fail-over Architectures
* **Active-Passive:** With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.
* **Active-Active:** In active-active, both servers are managing traffic, spreading the load between them. If the servers are public-facing, the DNS would need to know about the public IPs of both servers.

### Availability in Numbers
Availability is often quantified by uptime (or downtime) as a percentage of time the service is available. 

| Metric | 99.9% Availability ("Three 9s") | 99.99% Availability ("Four 9s") |
|---|---|---|
| **Downtime per year** | 8h 45min 57s | 52min 35.7s |
| **Downtime per month** | 43m 49.7s | 4m 23s |
| **Downtime per week** | 10m 4.8s | 1m 5s |
| **Downtime per day** | 1m 26.4s | 8.6s |

*Note:* The above downtime figures are standard industry metrics.

**Calculating Overall Availability:**
* **In Sequence:** Overall availability decreases when two components with availability < 100% are in sequence. The formula is: `Availability (Total) = Availability (Foo) * Availability (Bar)`.
* **In Parallel:** Overall availability increases when two components with availability < 100% are in parallel. The formula is: `Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))`.

---

## 4. The PACELC Theorem

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

## 5. Capacity Estimation & Back-of-the-Envelope Math

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
