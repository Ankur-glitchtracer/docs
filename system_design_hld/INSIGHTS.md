# 🌐 HLD Insights: Scaling to Millions

## 🟢 Database Scaling

**The Villain:** "The Monolith DB." A single SQL instance hitting CPU/IO limits during a flash sale.

**The Hero:** "Sharding & Read Replicas."

**The Plot:**
1. Horizontal partitioning by `user_id`.
2. Offload reads to replicas.

**The Twist:** "The Hot Shard." One celebrity user causing all traffic to hit a single database shard.

## 🟡 Real-time Messaging (WhatsApp)

**The Villain:** "The Polling Storm." 10M users asking "any new messages?" every second, crashing the API gateway.

**The Hero:** "WebSockets & Pub/Sub."

**The Plot:**
1. Maintain a persistent bi-directional connection.
2. Use Redis Pub/Sub to route messages to the correct server.

**The Twist:** "The Fan-out Explosion." Sending a message to a group with 1,000 users.

## 🔴 Distributed Storage (S3 Lite)

**The Villain:** "The Metadata Bottleneck." Searching 1PB of files in a traditional filesystem is $O(N)$.

**The Hero:** "The LSM Tree & Bloom Filters."

**The Plot:**
1. Write to memory (Memtable) first.
2. Flush to sorted strings (SSTables).
3. Use Bloom Filters to skip unnecessary disk reads.

**The Twist:** "The Write Amplification." Compaction taking up all disk bandwidth.
