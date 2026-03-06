# 🏊 Object Pool: High-Frequency Database Proxy

## 📝 Overview
The **Object Pool** pattern manages a cache of "recycled" objects. Instead of creating and destroying expensive resources (like DB connections) repeatedly, they are borrowed from a pool, used, and then returned for others.

!!! abstract "Core Concepts"
    - **Resource Recycling:** Avoiding the overhead of TCP handshakes and authentication for every query.
    - **Throttling:** Naturally limiting the number of concurrent connections to prevent system overload.

## 🚀 Problem Statement
In a high-frequency trading application, creating a new database connection for every small query is too slow due to the heavy overhead of memory allocation and network handshakes. This leads to high latency and potential port exhaustion on the server.

### Technical Constraints
- **Thread Safety:** Managing "Acquire" and "Release" operations across multiple threads simultaneously.
- **State Reset:** Ensuring a connection is "cleaned" of any leftover session data before being handed to the next user.
- **Capacity Limits:** Handling requests when the pool is empty and the maximum connection limit is reached.

## 🛠️ Requirements
1.  **Expensive Product:** A `DBConnection` class with a simulated creation delay.
2.  **Pool Manager:** A `ConnectionPool` with `acquire()` and `release()` methods.
3.  **Fixed Capacity:** Limit the pool to a specific number of connections (e.g., 5).
4.  **Concurrency Test:** Simulate multiple workers competing for a limited set of connections.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/object_pool/db_connection_pool/db_connection_pool.py"
```

!!! success "Why this works"
    It dramatically improves performance by amortizing the cost of object creation. It also provides a built-in "backpressure" mechanism; if all connections are in use, the system waits rather than crashing or overwhelming the database.
