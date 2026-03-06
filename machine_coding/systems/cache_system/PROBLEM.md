# ⚡ Machine Coding: High-Performance In-Memory Cache

## 📝 Overview
Design and implement a thread-safe, **In-Memory Cache** with a fixed capacity. This challenge focuses on data structure optimization and concurrency control to achieve constant-time performance for cache operations.

!!! abstract "Core Concepts"
    - **Eviction Policies:** Implementing LRU (Least Recently Used) and LFU (Least Frequently Used) to manage limited space.
    - **O(1) Access:** Combining HashMaps with Doubly Linked Lists to achieve lightning-fast lookups and updates.

## 🚀 Problem Statement
Modern applications require fast access to frequently used data. Your task is to build a cache that stores key-value pairs and automatically evicts items when it reaches its fixed capacity, based on a configurable policy.

### Technical Constraints
- **Time Complexity:** Both `get` and `put` operations must be $O(1)$.
- **Thread Safety:** The cache must handle concurrent access from multiple threads without data corruption or deadlocks.

## 🛠️ Requirements
1.  **Policy Support:** Implement `LRU` and `LFU` eviction strategies.
2.  **Core API:** Provide `put(key, value)` and `get(key)` methods.
3.  **Capacity Management:** Automatically remove the least relevant item when the limit is exceeded.
4.  **Concurrency:** Use appropriate locking mechanisms to ensure thread safety.

!!! success "Why this works"
    By using a HashMap for $O(1)$ lookups and a Doubly Linked List to maintain access order, we can reorder and evict elements in constant time. This hybrid approach is the industry standard for implementing high-performance caching layers.
