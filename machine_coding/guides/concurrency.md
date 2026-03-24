---
impact: "Medium"
nr: false
confidence: 4
---

# 🔄 Guide: Concurrency

## 📝 Overview
Concurrency occurs when multiple operations or execution paths attempt to progress at the same time, often interacting with the exact same shared memory within a single process. In Low-Level Design (LLD) interviews, mastering concurrency is essential for building thread-safe systems, handling producer-consumer workflows, and managing limited resources without data corruption or deadlocks.

!!! info "Why This Matters?"
    - **Core Skill:** The ability to reason about thread safety, shared state, and unpredictable instruction interleaving.
    - **Interview Relevance:** Frequently introduced as a follow-up twist to a standard design (e.g., two cars fighting for the same parking spot), or serves as the core prompt for systems like rate limiters and thread pools.
    - **Real-world Use:** Multi-threaded execution is the default in modern production systems; managing it prevents nondeterministic bugs that only surface under heavy load.
    - **Common Mistake:** Trying to invent custom synchronization mechanisms from scratch rather than reaching for standard, built-in language primitives.

---

## 🧠 Core Concepts

In interviews, concurrency problems almost always fall into one of three fundamental categories. 

### 🔑 Correctness
- **Definition:** Ensuring that shared state is not corrupted when accessed simultaneously by multiple threads.
- **Key Idea:** Operations that look atomic in source code often compile to multiple machine instructions. Without coordination, concurrent reads and writes overlap, leading to lost updates or invalid states. 
- **Example:** Two users simultaneously check if a flight seat is available, both see it as empty, and both successfully book it.
- **When to Use:** Whenever multiple threads perform "check-then-act" or "read-modify-write" operations on shared variables.

### 🔑 Coordination
- **Definition:** Managing the flow of control when threads need to wait for each other or hand off work.
- **Key Idea:** Threads must wait efficiently without constantly spinning and burning CPU cycles. 
- **Example:** A producer thread adds tasks to a queue, while consumer threads pull from it. If the queue is empty, consumers must wait; if full, producers must slow down.
- **When to Use:** Async request processing, bursty traffic handling, and producer-consumer workflows.

### 🔑 Scarcity
- **Definition:** Enforcing limits when concurrent demand exceeds the available system resources.
- **Key Idea:** You must restrict the number of concurrent operations to prevent the system from being overwhelmed.
- **Example:** A system has 10 database connections but receives 100 concurrent requests; 90 requests must wait their turn.
- **When to Use:** Building resource pools (e.g., connection pools) or setting concurrent operation limits (e.g., rate limiting).

---

## 🏗️ Mental Models & Intuition

Think of a process as an isolated container that holds a program's memory. Inside that container, threads act as independent workers. Each worker has its own private notepad (the stack and registers), but they all share the exact same whiteboard (the heap and globals). Because the operating system rapidly switches between these workers, their actions at the whiteboard overlap unpredictably. Concurrency primitives are the rules and locks you place around the whiteboard to stop workers from overwriting each other's work.

> 💡 **Rule of Thumb:** Identify the problem type first. Is state getting corrupted? That's a *Correctness* problem. Do threads need to pass data to one another? That's a *Coordination* problem. Are there too many threads for the available resources? That's a *Scarcity* problem.

---

## 🚧 Common Problems & Tools

### ⚠️ Common Problems
* **Check-Then-Act / Race Conditions:** A thread checks a condition (e.g., `if count > 0`) and acts on it (`count--`), but another thread changes the state in between those two instructions.
* **Resource Exhaustion:** Unbounded threads consume all memory or connections, crashing the process.

### 🛠️ Tools & Primitives
You do not need to invent new ways to synchronize data; you just need to apply the correct primitive.

- **Atomics:** Hardware-level instructions (like compare-and-swap) that perform thread-safe operations on single variables in one uninterruptible step. Highly performant but limited to single fields.
- **Locks (Mutexes):** Provide mutual exclusion. When a thread holds a lock, it creates a critical section where no other thread can execute, forcing others to block and wait. Used for multi-field updates.
- **Semaphores:** Think of these as "counting locks." They hold a set number of permits ($N$). Threads acquire a permit to proceed and release it when done. Ideal for *Scarcity* problems.
- **Condition Variables:** Allow threads to temporarily release a lock and go to sleep until another thread signals that a specific condition is now true. 
- **Blocking Queues:** A high-level primitive combining queues with condition variables. It natively handles thread-safe producer-consumer handoffs (blocking when empty/full).

---

## ⚙️ Practical Examples

### 🪶 Simple Example: Correctness via Locks
Python lacks native atomics, so a standard Lock is required to safely increment a shared counter across multiple threads.

```python
import threading

class ThreadSafeCounter:
    def __init__(self):
        self._count = 0
        self._lock = threading.Lock()

    def increment(self):
        # The lock prevents a read-modify-write race condition
        with self._lock:
            self._count += 1
```

### 🏢 Real-World Example: Task Processing (Coordination)
In a real system, you rarely use raw condition variables. Instead, you use a **Blocking Queue** to manage coordination. A web server receives user requests and instantly puts them onto a queue (Producer). A fixed pool of background worker threads constantly polls the queue (Consumers). The queue intrinsically handles the concurrency: if there are no requests, the workers sleep efficiently; if requests spike, they are safely buffered. 

---

## ⚖️ Trade-offs & Limitations

| Aspect | Pros | Cons / Limitations |
| :--- | :--- | :--- |
| **Atomics vs Locks** | Atomics are incredibly fast and never block the thread entirely. | Atomics only work for single variables. If you must update two variables atomically, you *must* use a Lock. |
| **Coarse vs Fine-Grained Locks** | A single, coarse-grained lock is easy to implement and prevents deadlocks. | Limits throughput. If every operation locks the entire system, threads execute sequentially, defeating the purpose of concurrency. |
| **Language Differences** | Idiomatic solutions exist (e.g., Go Channels replace raw Blocking Queues). | Python's Global Interpreter Lock (GIL) prevents true parallelism for CPU-bound threads, limiting them to I/O concurrency. |

---

## 🔄 Comparison / Related Concepts

| Concept | Difference |
| :--- | :--- |
| **Mutex vs Semaphore** | A Mutex implies ownership: only the thread that locked it can unlock it, making it binary (1 or 0). A Semaphore is a counting mechanism for permits and doesn't strictly track thread ownership. |
| **Concurrency vs Parallelism** | Concurrency is about *dealing* with multiple things at once (interleaving instructions). Parallelism is about *doing* multiple things at once (running simultaneously on multiple CPU cores). |

---

## 🎤 Interview Focus

* **Definition Check:** Can you clearly articulate that concurrency in LLD refers to threads sharing memory within a single process, leading to unpredictable instruction interleaving?
* **Deep Dive:** Be prepared to transition an initially synchronous design (like an inventory manager) to a concurrent one. You will be asked what breaks when two requests arrive at the exact same millisecond.
* **Application:** Using a Blocking Queue for producer-consumer workflows, or utilizing a Semaphore to cap API calls in a Rate Limiter.
* **Gotcha:** Reinventing the wheel. Do not try to manually manage thread sleep states; simply leverage standard language primitives like `queue.Queue` in Python or buffered channels in Go.

---

## 🚀 How to Apply This

1. **Classify the Problem:** When an interviewer asks "what if this happens concurrently?", identify if it is a *Correctness*, *Coordination*, or *Scarcity* issue.
2. **Select the Primitive:** 
   - State corruption (Correctness) -> Use a Lock or Atomic.
   - Need to pass work around (Coordination) -> Use a Blocking Queue.
   - Resource limits (Scarcity) -> Use a Semaphore.
3. **Minimize the Critical Section:** When using a lock, acquire it just before the shared state is accessed and release it immediately after. Do not perform heavy I/O or network calls while holding a lock.

---

## 🔗 Related Topics

* [Rate Limiter LLD](../distributed/rate_limiter/PROBLEM.md) — A classic problem deeply rooted in Scarcity and Correctness where concurrency must be carefully managed.
* [Low-Level Design Delivery Framework](./delivery_framework.md) — How to integrate questions about concurrent behavior logically into your 35-minute interview pacing without derailing the core object design.
