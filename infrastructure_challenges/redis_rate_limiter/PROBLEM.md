# 📦 Infrastructure Challenge: Redis-Backed Distributed Rate Limiter

## 📝 Overview
While an in-memory rate limiter works for a single instance, a **Redis-Backed Rate Limiter** is essential for distributed systems. It uses Redis as a centralized, high-performance store to maintain consistent request counts across an entire cluster of application servers.

!!! abstract "Core Concepts"
    - **Atomic Operations:** Using Redis commands like `INCR` and `EXPIRE` to prevent race conditions.
    - **Lua Scripting:** Offloading logic to Redis to ensure atomicity and minimize network round-trips.
    - **Time Windows:** Managing counters that automatically reset after a fixed duration.

## 🚀 Problem Statement
Move beyond local simulations. Implement a rate limiter that uses a real Redis instance. The system must ensure that a user cannot exceed their quota, even if their requests are distributed across multiple server nodes.

### Technical Constraints
- **Performance:** Benchmarking the overhead added by the Redis network call.
- **Consistency:** Ensuring that no request is allowed through if the global limit has been reached.
- **Network Resilience:** Gracefully handling cases where the Redis server is temporarily unreachable.

## 🛠️ Requirements
1.  **Algorithm Implementation:** Use "Fixed Window" or "Sliding Window Log" via Redis atomic operations.
2.  **Distributed Simulation:** Run two independent Python scripts hitting the same `user_id` to prove the limit is enforced globally.
3.  **Benchmarking:** Measure the latency of the "check-and-update" logic.

## 💻 Solution Implementation

```python
--8<-- "infrastructure_challenges/redis_rate_limiter/PROBLEM.md"
```

!!! success "Why this works"
    Using Redis allows for near-instant global state synchronization with minimal latency, providing a single source of truth for traffic control in a distributed environment.
