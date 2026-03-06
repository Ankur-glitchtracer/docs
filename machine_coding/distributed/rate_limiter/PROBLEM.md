# 🚦 Distributed System: Rate Limiter

## 📝 Overview
A **Distributed Rate Limiter** controls the rate of traffic sent or received by a network interface or service. In a distributed environment, the limit must be enforced across a cluster of servers, requiring shared state management.

!!! abstract "Core Concepts"
    - **Algorithms:** Token Bucket, Leaky Bucket, Fixed Window, and Sliding Window.
    - **Shared State:** Using a central store (like Redis) to maintain counters across nodes.
    - **Latency Optimization:** Minimizing the overhead of the "check-and-increment" operation.

## 🚀 Problem Statement
Implement a rate limiter that restricts API requests per user/token. The system must behave consistently regardless of which server node receives the request, preventing "burst" violations across the cluster.

### Technical Constraints
- **Consistency:** Strict enforcement of limits across all nodes.
- **Low Latency:** The rate-limiting check should not significantly impact API response times.
- **Race Conditions:** Handle concurrent updates to shared counters correctly.

## 🛠️ Requirements
1.  **Algorithms:** Support "Sliding Window" and "Token Bucket."
2.  **Shared State:** Simulate a distributed state (e.g., via thread-safe shared memory or Redis).
3.  **Performance:** Ensure minimal latency and handle high concurrency per user.
4.  **Configuration:** Support dynamic limits per endpoint and user role.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/rate_limiter/PROBLEM.md"
```

!!! success "Why this works"
    Centralizing the state allows for accurate enforcement of global limits, protecting downstream services from being overwhelmed by a distributed surge in traffic.
