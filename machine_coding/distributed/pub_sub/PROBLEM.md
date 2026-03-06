# 📡 Distributed System: Persistent Pub-Sub (Kafka Lite)

## 📝 Overview
A **Pub-Sub (Publisher-Subscriber) System** is a messaging pattern where senders (publishers) do not send messages directly to specific receivers (subscribers). Instead, messages are categorized into topics. This implementation focuses on durability, scalability via partitions, and consumer group semantics.

!!! abstract "Core Concepts"
    - **Topics & Partitions:** Logic grouping of messages split into multiple streams for parallelism.
    - **Consumer Groups:** Scaling mechanism where partition data is balanced among group members.
    - **Offset Management:** Tracking the "read position" to allow for message replay and fault tolerance.

## 🚀 Problem Statement
Build a message queue that behaves like a simplified Kafka. The system must ensure that messages are stored persistently and can be consumed by multiple independent groups of workers without duplication within a group.

### Technical Constraints
- **Persistence:** Messages must survive system restarts (simulate with file I/O).
- **Concurrency:** Support multiple producers and consumers hitting the same topic simultaneously.
- **Ordering:** Maintain strict message ordering within a single partition.

## 🛠️ Requirements
1.  **Topics & Partitions:** Producers send messages to specific topics; topics are divided into partitions.
2.  **Consumer Groups:** Support multiple consumer groups; within a group, a message in a partition is delivered to only one consumer.
3.  **Persistence:** Store messages on disk and support "message replay" by resetting offsets.
4.  **Delivery Guarantees:** Implement at-least-once delivery via acknowledgments.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/pub_sub/PROBLEM.md"
```

!!! success "Why this works"
    Partitioning allows the system to scale horizontally, while persistence and offset tracking make the system resilient to consumer failures and enable historical data processing.
