# 📡 Machine Coding: Persistent Pub-Sub (Kafka Lite)

## 📝 Overview
A **Pub-Sub (Publisher-Subscriber) System** is a messaging pattern where senders (publishers) do not send messages directly to specific receivers (subscribers). Instead, messages are categorized into topics. This implementation focuses on durability, scalability via partitions, and consumer group semantics.

!!! info "Why This Challenge?"

    - **Persistence & Durability:** Learning how to design systems that survive restarts by using append-only logs and disk I/O.
    - **Scalability through Partitioning:** Understanding how to scale a message broker by splitting topics into parallel streams.
    - **Consumer Group Semantics:** Mastering the complexity of balancing message delivery across multiple workers in a group.

!!! abstract "Core Concepts"

    - **Topics & Partitions:** Logic grouping of messages split into multiple streams for parallelism.
    - **Consumer Groups:** Scaling mechanism where partition data is balanced among group members.
    - **Offset Management:** Tracking the "read position" to allow for message replay and fault tolerance.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Topics & Partitions:** Producers send messages to specific topics; topics are divided into partitions.
2.  **Consumer Groups:** Support multiple consumer groups; within a group, a message in a partition is delivered to only one consumer.
3.  **Persistence:** Store messages on disk and support "message replay" by resetting offsets.
4.  **Delivery Guarantees:** Implement at-least-once delivery via acknowledgments.

### Technical Constraints

- **Persistence:** Messages must survive system restarts (simulate with file I/O).
- **Concurrency:** Support multiple producers and consumers hitting the same topic simultaneously.
- **Ordering:** Maintain strict message ordering within a single partition.

## 🧠 The Engineering Story

**The Villain:** "The Memory Overflow." Storing every message in a single list in RAM. If subscribers are slow or disconnected, the broker's memory fills up and the entire system crashes.

**The Hero:** "The Persistent Append-Only Log." Treating topics as durable files on disk rather than temporary buffers.

**The Plot:**

1. Organize messages into `Topics` and `Partitions`.
2. Use an `Append-Only` log to store messages sequentially.
3. Decouple message production from consumption via `Consumer Groups`.
4. Manage `Offsets` to allow consumers to track their own progress.

**The Twist (Failure):** **The Duplicate Delivery.** A consumer processes a message but crashes before acknowledging its offset, leading to the same message being re-read. This is why "Idempotency" is vital.

**Interview Signal:** Mastery of **High-Throughput IO** and **Distributed Consistency**.

## 🚀 Thinking Process & Approach
Scalable messaging systems rely on durability and parallel processing. The approach involves partitioning topics to allow horizontal scaling and using persistent logs to ensure that no messages are lost even if the system restarts.

### Key Observations:

- Disk I/O must be sequential for performance.
- Offsets allow for independent consumer group tracking.

## 🏗️ Design Patterns Used

- **Observer Pattern**: To handle message broadcasting to multiple subscribers or groups.
- **Iterator Pattern**: To provide a clean interface for reading messages from the log using offsets.
- **Singleton/Factory Pattern**: For managing topic and partition lifecycles.
- **Strategy Pattern**: For implementing different partition allocation strategies among consumers.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/pub_sub/kafka_lite.py"
```

!!! success "Why this works"
    Partitioning allows the system to scale horizontally, while persistence and offset tracking make the system resilient to consumer failures and enable historical data processing.

## 🎤 Interview Follow-ups

- **Throughput:** How would you optimize the system for millions of messages per second? (Batching, Zero-copy)
- **Compaction:** How would you implement log compaction to save disk space for key-based messages?
- **Broker Coordination:** How would you handle broker failures and leader election for partitions?

## 🔗 Related Challenges

- [Job Scheduler](../job_scheduler/PROBLEM.md) — For executing tasks triggered by messages.
- [Rate Limiter](../rate_limiter/PROBLEM.md) — To prevent overwhelming the message broker.
