# 📦 Infrastructure Challenge: Redis-Backed Distributed Rate Limiter

## 📝 Overview
While an in-memory rate limiter works for a single instance, a **Redis-Backed Rate Limiter** is essential for distributed systems. It uses Redis as a centralized, high-performance store to maintain consistent request counts across an entire cluster of application servers.

!!! abstract "Core Concepts"

    - **Atomic Operations:** Using Redis commands like `INCR` and `EXPIRE` to prevent race conditions.
    - **Lua Scripting:** Offloading logic to Redis to ensure atomicity and minimize network round-trips.
    - **Time Windows:** Managing counters that automatically reset after a fixed duration.

!!! info "Why This Challenge?"

    - **Distributed State Management:** Understand how to maintain a single source of truth across multiple application nodes.
    - **Atomic Operations Mastery:** Learn to use Redis Lua scripting to prevent race conditions in high-concurrency scenarios.
    - **System Reliability:** Implement a critical infrastructure component that protects services from overload and abuse.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Algorithm Implementation:** Use "Fixed Window" or "Sliding Window Log" via Redis atomic operations.
2.  **Distributed Simulation:** Run two independent Python scripts hitting the same `user_id` to prove the limit is enforced globally.
3.  **Benchmarking:** Measure the latency of the "check-and-update" logic.

### Technical Constraints

- **Performance:** Benchmarking the overhead added by the Redis network call.
- **Consistency:** Ensuring that no request is allowed through if the global limit has been reached.
- **Network Resilience:** Gracefully handling cases where the Redis server is temporarily unreachable.

## 🧠 The Engineering Story

**The Villain:** "The Noisy Neighbor." A single user scripts 10,000 requests per second, taking down your app nodes. Local rate limiting fails because you have 5 different server nodes.

**The Hero:** "The Centralized Arbiter." Using Redis as a high-speed global counter to enforce limits across all instances.

**The Plot:**

1. Key the user in Redis (e.g., `rate:user_id`).
2. Use `INCR` to track requests.
3. Set an `EXPIRE` on the key to reset the window.

**The Twist (Failure):** **The Race Condition.** If you check the value and *then* set the expiry in two steps, the user could hit the limit without the key ever expiring, blocking them forever. Use **Lua Scripting** for atomicity.

**Interview Signal:** Mastery of **Distributed State Management** and Redis atomic operations.

## 🚀 Thinking Process & Approach
Distributed rate limiting requires a centralized source of truth that is both fast and consistent. The approach leverages Redis's atomic operations and Lua scripting to perform "check-and-update" logic in a single network round-trip, ensuring that limits are enforced accurately across multiple application nodes.

### Key Observations:

- Redis provides the low-latency shared state needed for real-time traffic control.
- Lua scripts ensure that the logic is executed atomically, preventing race conditions between concurrent requests.

## 💻 Solution Implementation

```python
--8<-- "infrastructure_challenges/redis_rate_limiter/redis_rate_limiter.py"
```

!!! success "Why this works"
    Using Redis allows for near-instant global state synchronization with minimal latency, providing a single source of truth for traffic control in a distributed environment.

## 🎤 Interview Follow-ups

- **Hard vs Soft Limits:** How would you implement a "soft limit" that allows occasional bursts but enforces a strict "hard limit"?
- **Redis Availability:** What happens if Redis goes down? How do you implement a fallback to local rate limiting?
- **Multi-tier Limiting:** How would you design a system that has both per-user and per-IP rate limits?

## 🔗 Related Challenges

- [Dockerized Job Scheduler](../dockerized_job_scheduler/PROBLEM.md) — Orchestrate the Redis instance alongside your application.
- [Socket Chat App](../socket_chat_app/PROBLEM.md) — Explore real-time communication protocols.
