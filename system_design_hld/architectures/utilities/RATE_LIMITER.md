# 🚦 System Design: Rate Limiter

## 📝 Overview
A **Rate Limiter** is a critical security and stability component that controls the rate of traffic sent by a client to a server. It protects services from being overwhelmed by a "noisy neighbor" or malicious attacks, ensuring fair resource distribution across all users.

!!! abstract "Core Concepts"

    - **Token Bucket Algorithm:** A flexible algorithm allowing for bursts while maintaining a steady average rate.
    - **Distributed State:** Using centralized stores like Redis to synchronize limits across multiple API nodes.
    - **Atomic Operations:** Utilizing Redis Lua scripts to prevent race conditions during concurrent request processing.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **Request Throttling:** Limit requests based on user ID, IP address, or API key.
2. **Customizable Rules:** Support different rate limits for different API endpoints or user tiers.
3. **Informative Headers:** Provide standard `X-RateLimit-*` headers to inform clients of their current status.

### Non-Functional Requirements

1. **Low Latency:** Minimal overhead (e.g., < 2ms) added to the request path.
2. **Fault Tolerance:** If the rate limiter service fails, it should fail-open to ensure service availability.
3. **Accuracy:** Precise tracking of request counts even in a distributed environment.

## 🧠 The Engineering Story

**The Villain:** "The DDoS/Noisy Neighbor." One rogue script taking down the entire API for everyone.

**The Hero:** "The Token Bucket."

**The Plot:**

1. Refill tokens at a fixed rate.
2. Allow bursts if tokens are available.

**The Twist:** "The Distributed Race Condition." Multiple API nodes updating the same bucket in Redis.

**Interview Signal:** Mastery of **Traffic Control**, **Distributed State Management**, and **Redis Lua Scripting**.

## 🏗️ High-Level Architecture
Design a rate limiter that can be deployed at the edge (API Gateway) to protect services from being overwhelmed.

### Key Design Challenges:
#### Algorithms to Evaluate

1. **Token Bucket:** Allows bursts, simple to implement.
2. **Leaky Bucket:** Constant output rate, smooths traffic.
3. **Fixed Window Counter:** Simple but has "edge" problems (double traffic at window borders).
4. **Sliding Window Logs:** Precise but memory-heavy.
5. **Sliding Window Counter:** Best trade-off between precision and memory.

#### Distributed Challenges

- **Shared State:** Using Redis for centralized counting.
- **Performance:** Minimizing latency added to every request.
- **Race Conditions:** Using Lua scripts in Redis for atomic "check-and-increment."

## 🔍 Deep Dives
(To be detailed...)

## 📊 Data Modeling & API Design
### Data Model

- **(To be detailed...)**: (To be detailed...)

### API Design

- **(To be detailed...)**: (To be detailed...)

## 📈 Scalability & Bottlenecks
(To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** (To be detailed...)
- **Scale Question:** (To be detailed...)
- **Edge Case Probe:** (To be detailed...)

## 🔗 Related Architectures

- [Ticket Booking](./TICKET_BOOKING.md) — For concurrency and reservation patterns.
