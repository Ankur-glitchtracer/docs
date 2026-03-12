# ⚡ Machine Coding: High-Performance In-Memory Cache

## 📝 Overview
Design and implement a thread-safe, **In-Memory Cache** with a fixed capacity. This challenge focuses on data structure optimization and concurrency control to achieve constant-time performance for cache operations.

!!! info "Why This Challenge?"

    - **Data Structure Composition:** Learning how to combine HashMaps and Doubly Linked Lists to achieve $O(1)$ performance for multiple operations.
    - **Concurrency Control:** Mastering thread-safe access to shared in-memory state without compromising on performance.
    - **Eviction Algorithm Implementation:** Deep diving into the mechanics of LRU (Least Recently Used) and LFU (Least Frequently Used) policies.

!!! abstract "Core Concepts"

    - **Eviction Policies:** Implementing LRU (Least Recently Used) and LFU (Least Frequently Used) to manage limited space.
    - **O(1) Access:** Combining HashMaps with Doubly Linked Lists to achieve lightning-fast lookups and updates.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Policy Support:** Implement `LRU` and `LFU` eviction strategies.
2.  **Core API:** Provide `put(key, value)` and `get(key)` methods.
3.  **Capacity Management:** Automatically remove the least relevant item when the limit is exceeded.
4.  **Concurrency:** Use appropriate locking mechanisms to ensure thread safety.

### Technical Constraints

- **Time Complexity:** Both `get` and `put` operations must be $O(1)$.
- **Thread Safety:** The cache must handle concurrent access from multiple threads without data corruption or deadlocks.

## 🧠 The Engineering Story

**The Villain:** "The $O(N)$ Eviction." Keeping a list of used items is easy. Moving an item to the front or finding the least recently used item usually takes $O(N)$. We need $O(1)$.

**The Hero:** "The HashMap + Doubly Linked List."

**The Plot:**

1. Use a `HashMap` for $O(1)$ access to any key.
2. Use a `Doubly Linked List` to maintain the order of usage.
3. On `get`, move the node to the front (head) of the list.
4. On `put`, add to the front. If over capacity, remove from the tail.

**The Twist (Failure):** **The Deadlock.** If multiple threads try to update the list and the map simultaneously without proper synchronization, the pointers get corrupted.

**Interview Signal:** Mastery of **Data Structure Composition** and **Concurrency Control**.

## 🚀 Thinking Process & Approach
The core of a high-performance cache is minimizing the time complexity of both retrieval and eviction. The approach uses a combination of a hash map for fast lookup and a doubly linked list for fast reordering and eviction.

### Key Observations:

- Hybrid data structures are needed for multi-objective optimization.
- Thread safety must be prioritized for in-memory shared state.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: For switching between different eviction policies (LRU, LFU, FIFO).
- **Singleton Pattern**: To ensure a single global cache instance if required by the application.
- **Proxy Pattern**: To add logging, monitoring, or remote access to the cache.
- **Factory Pattern**: To create cache instances with specific policies and capacities.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/cache_system/cache.py"
```

!!! success "Why this works"
    By using a HashMap for $O(1)$ lookups and a Doubly Linked List to maintain access order, we can reorder and evict elements in constant time. This hybrid approach is the industry standard for implementing high-performance caching layers.

## 🎤 Interview Follow-ups

- **LFU Implementation:** How would you modify the data structures to support Least Frequently Used (LFU) in $O(1)$ time?
- **Distributed Caching:** How would you extend this to a distributed environment (like Redis)?
- **Persistence:** How would you add a "Write-Through" or "Write-Behind" mechanism to persist data to disk?

## 🔗 Related Challenges

- [Distributed Rate Limiter](../../distributed/rate_limiter/PROBLEM.md) — For using a cache-like structure to enforce limits.
- [Instagram-Lite Feed](../instagram/PROBLEM.md) — For caching personalized user feeds.
