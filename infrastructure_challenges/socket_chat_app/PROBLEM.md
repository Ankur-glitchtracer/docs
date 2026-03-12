# 💬 Infrastructure Challenge: Real-Time Socket Chat Application

## 📝 Overview
Modern real-time communication relies on **TCP Sockets** for persistent, bi-directional data flow. This challenge focuses on low-level network programming, moving away from high-level abstractions like HTTP to understand how servers manage multiple simultaneous connections.

!!! abstract "Core Concepts"

    - **TCP Handshake:** Establishing and maintaining reliable connections between clients and a server.
    - **Socket Buffers:** Handling the flow of raw bytes over the wire.
    - **Concurrency Models:** Managing multiple active sockets using multi-threading or non-blocking I/O.

!!! info "Why This Challenge?"

    - **Low-level Networking Knowledge:** Move beyond HTTP to understand how persistent TCP connections actually work.
    - **Concurrency Patterns:** Master multi-threading or non-blocking I/O for managing high-volume simultaneous connections.
    - **Protocol Design:** Learn to design and implement your own lightweight communication protocols for specific use cases.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Multi-threaded Server:** Listen on `localhost:8888` and maintain a registry of active clients.
2.  **Broadcast Logic:** Efficiently relay messages from one client to all others.
3.  **Client CLI:** Create a script that can both send messages and display incoming messages asynchronously.
4.  **Resilience:** Handle `ConnectionResetError` and clean up the client registry on disconnect.

### Technical Constraints

- **Multi-threading:** The server must handle new connections without blocking existing ones.
- **Protocol Design:** Implementing a simple text-based protocol for joining, messaging, and quitting.
- **Error Handling:** Managing "Dirty Disconnects" (e.g., when a client crashes or the network drops).

## 🧠 The Engineering Story

**The Villain:** "The Ghost Connection." A user loses Wi-Fi in a tunnel. Your server still thinks they are "Online," wasting a thread and memory until the OS eventually times out the socket 2 hours later.

**The Hero:** "The Heartbeat & Keep-Alive." A protocol-level ping/pong that ensures inactive or dead connections are purged immediately.

**The Plot:**

1. Open a `ServerSocket` on a high-numbered port.
2. Use a `Thread-per-Connection` or `Select/Poll` (Non-blocking) model.
3. Broadcast messages by iterating through a `ClientRegistry`.
4. Implement a "Welcome" and "Quit" protocol.

**The Twist (Failure):** **The Thundering Herd.** When the server restarts, 10,000 clients all try to reconnect at the exact same millisecond, crashing the auth service.

**Interview Signal:** Mastery of **Network Programming**, **Concurrency Models**, and **Resource Management**.

## 🚀 Thinking Process & Approach
Low-level networking requires a deep understanding of resource management and connection lifecycles. The approach uses a multi-threaded server model to handle concurrent client connections and an event-driven broadcast mechanism to distribute messages in real-time.

### Key Observations:

- Maintaining persistent connections requires efficient thread or I/O management.
- Protocol design is essential for handling various client lifecycle events (join, leave, crash).

## 💻 Solution Implementation

```python
--8<-- "infrastructure_challenges/socket_chat_app/socket_chat.py"
```

!!! success "Why this works"
    Building a socket-level application provides deep insight into networking fundamentals like latency, packet loss, and the overhead of maintaining persistent connections.

## 🎤 Interview Follow-ups

- **Scalability:** How would you scale this chat app to 100,000 concurrent users using `select` or `epoll` instead of threads?
- **Security:** How would you implement TLS/SSL to encrypt the socket communication?
- **State Management:** How would you handle message history if a user reconnects?

## 🔗 Related Challenges

- [Dockerized Job Scheduler](../dockerized_job_scheduler/PROBLEM.md) — Learn how to containerize and deploy your chat server.
- [Redis Rate Limiter](../redis_rate_limiter/PROBLEM.md) — Implement rate limiting for your chat messages to prevent spam.
