# Module 7: Replication, Consensus & CAP Theorem

### 🚀 Problem Statement
An Enterprise CMS requires that when a project lead approves a data record, that approval must never be lost (durability) and must be immediately visible to all users (consistency). However, the system must also be available 24/7 for end users on potentially flaky mobile networks.

### 🧠 The Engineering Story

**The Villain:** "The Split Brain." A network partition isolates a primary database from its replica. If both accept writes, the partition healing might reveal two conflicting versions of the same Core Engine approval.

**The Hero:** "The Consensus Protocol." Using Raft/Paxos, the system elects a single leader, and writes only succeed if a majority of replicas acknowledge — guaranteeing no divergence.

**The Plot:**

1. Deep dive into CAP theorem — understand it as a spectrum, not a binary choice
2. Study leader-based replication (Postgres streaming) vs leaderless (DynamoDB/Cassandra)
3. Understand Raft consensus: leader election, log replication, safety
4. Mapping system consistency requirements per data type

**The Twist (Failure):** **Latent Stale Reads.** Using async replication for performance may result in a read replica serving an old version of an enterprise document for several seconds after an update. An end user might then download an outdated standard procedure.

**Interview Signal:** Can map business requirements to consistency levels (strong, eventual, causal).

### 🧠 Consistency Spectrum

| Level | Guarantee | Cost | GenAI Use Case |
|-------|-----------|------|----------------|
| **Strong (Linearizable)** | Reads always see latest write | High latency | system approvals, sign-offs |
| **Causal** | Respects cause-effect ordering | Medium | Comment threads on documents |
| **Eventual** | Will converge, no timing guarantee | Low latency | Analytics dashboards, usage stats |
| **Read-Own-Writes** | User sees own writes immediately | Medium | Document edits by same user |
