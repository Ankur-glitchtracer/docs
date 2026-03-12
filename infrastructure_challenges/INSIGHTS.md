# 🏗️ Infrastructure & DevOps Insights

## 🟢 Containerization (Docker)

**The Villain:** "The Dependency Hell." "It works on my machine" but fails in production due to different library versions.

**The Hero:** "The Immutable Image."

**The Plot:**

1. Package everything (OS, Runtimes, Code) into a single layer.

**The Twist:** "The Bloated Image." A 2GB image that takes 10 minutes to pull during an auto-scale event.

## 🟡 Traffic Control (Rate Limiter)

**The Villain:** "The DDoS/Noisy Neighbor." One rogue script taking down the entire API for everyone.

**The Hero:** "The Token Bucket."

**The Plot:**

1. Refill tokens at a fixed rate.
2. Allow bursts if tokens are available.

**The Twist:** "The Distributed Race Condition." Multiple API nodes updating the same bucket in Redis.

## 🔴 Real-time Networking (Socket Chat)

**The Villain:** "The Ghost Connection." A user disconnects (tunnels/train), but the server still thinks they are online, wasting resources.

**The Hero:** "Heartbeats & TTL."

**The Plot:**

1. Clients ping every 30s.
2. Server purges connections without a ping.

**The Twist:** "The Thundering Herd." 1M clients all trying to reconnect at the exact same millisecond after a network hiccup.
