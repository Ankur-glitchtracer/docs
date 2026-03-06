# HLD: Design a Distributed Key-Value Store

## 🚀 Problem Statement
Design a highly scalable and available Key-Value store, similar to DynamoDB or Cassandra.

## 🧠 Key Design Challenges
- **Data Partitioning:** Consistent Hashing to minimize movement during scaling.
- **Data Replication:** Quorum-based consistency (N, W, R).
- **Handling Failures:** Hinted Handoff and Read Repair.
- **Storage Engine:** B-Trees vs. LSM Trees (optimized for writes).
- **Consistency:** Navigating the CAP Theorem (AP vs CP).
