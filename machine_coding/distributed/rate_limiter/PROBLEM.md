# 🚦 Machine Coding: Distributed Rate Limiter

## 📝 Overview
A **Distributed Rate Limiter** controls the rate of traffic sent or received by a network interface or service. In a distributed environment, the limit must be enforced across a cluster of servers, requiring shared state management.

!!! info "Why This Challenge?"

    - **Shared State Management:** Learning how to synchronize counters and limits across multiple server nodes using Redis or shared memory.
    - **Concurrency & Atomicity:** Mastering the use of atomic operations to prevent race conditions in high-throughput environments.
    - **Algorithm Implementation:** Deep diving into rate-limiting algorithms like Token Bucket and Sliding Window.

!!! abstract "Core Concepts"

    - **Algorithms:** Token Bucket, Leaky Bucket, Fixed Window, and Sliding Window.
    - **Shared State:** Using a central store (like Redis) to maintain counters across nodes.
    - **Latency Optimization:** Minimizing the overhead of the "check-and-increment" operation.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Algorithms:** Support "Sliding Window" and "Token Bucket."
2.  **Shared State:** Simulate a distributed state (e.g., via thread-safe shared memory or Redis).
3.  **Performance:** Ensure minimal latency and handle high concurrency per user.
4.  **Configuration:** Support dynamic limits per endpoint and user role.

### Technical Constraints

- **Consistency:** Strict enforcement of limits across all nodes.
- **Low Latency:** The rate-limiting check should not significantly impact API response times.
- **Race Conditions:** Handle concurrent updates to shared counters correctly.

## 🧠 The Engineering Story

**The Villain:** "The Noisy Neighbor." A single user scripts 10,000 requests per second, taking down your app nodes. Local rate limiting fails because you have 5 different server nodes.

**The Hero:** "The Centralized Arbiter." Using a shared high-speed store to enforce limits across all instances.

**The Plot:**

1. Key the user in a shared store (e.g., `rate:user_id`).
2. Use atomic operations to track and increment requests.
3. Manage time-based windows for rolling resets.

**The Twist (Failure):** **The Race Condition.** If you check the value and then increment in two steps, multiple nodes might read "1" and both think they are safe to allow, even if the limit is "2". Use **Atomic Increments**.

**Interview Signal:** Mastery of **Distributed State Management** and atomic operations.

## 🚀 Thinking Process & Approach
Rate limiting in a distributed context requires balancing accuracy and performance. The approach involves selecting an appropriate algorithm (like Sliding Window) and implementing it using atomic operations on a shared memory layer to ensure consistency across nodes.

### Key Observations:

- Distributed consistency vs latency trade-offs.
- Atomic operations for thread-safe state management.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: For switching between different rate-limiting algorithms (Token Bucket, Sliding Window).
- **Decorator Pattern**: To wrap API handlers with rate-limiting logic.
- **Singleton Pattern**: For managing the connection to the shared state store (e.g., Redis client).
- **Factory Pattern**: For creating rate limiter instances based on configuration.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/rate_limiter/rate_limiter.py"
```

!!! success "Why this works"
    Centralizing the state allows for accurate enforcement of global limits, protecting downstream services from being overwhelmed by a distributed surge in traffic.

## 🎤 Interview Follow-ups

- **Hard vs Soft Limits:** How would you implement "bursting" where users can temporarily exceed their limit?
- **Global vs Local:** When would you use local (in-memory) rate limiting instead of distributed?
- **Resilience:** What happens if the central Redis store goes down? (Fail-open vs Fail-closed)

## 🔗 Related Challenges

- [Pub-Sub](../pub_sub/PROBLEM.md) — To throttle message production or consumption.
- [Job Scheduler](../job_scheduler/PROBLEM.md) — To limit the rate of job submissions.
