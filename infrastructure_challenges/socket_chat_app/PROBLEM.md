# 💬 Infrastructure Challenge: Real-Time Socket Chat Application

## 📝 Overview
Modern real-time communication relies on **TCP Sockets** for persistent, bi-directional data flow. This challenge focuses on low-level network programming, moving away from high-level abstractions like HTTP to understand how servers manage multiple simultaneous connections.

!!! abstract "Core Concepts"
    - **TCP Handshake:** Establishing and maintaining reliable connections between clients and a server.
    - **Socket Buffers:** Handling the flow of raw bytes over the wire.
    - **Concurrency Models:** Managing multiple active sockets using multi-threading or non-blocking I/O.

## 🚀 Problem Statement
Build a command-line chat application where multiple clients can send and receive messages in real-time. The server must act as a central hub, broadcasting incoming messages to all other connected users.

### Technical Constraints
- **Multi-threading:** The server must handle new connections without blocking existing ones.
- **Protocol Design:** Implementing a simple text-based protocol for joining, messaging, and quitting.
- **Error Handling:** Managing "Dirty Disconnects" (e.g., when a client crashes or the network drops).

## 🛠️ Requirements
1.  **Multi-threaded Server:** Listen on `localhost:8888` and maintain a registry of active clients.
2.  **Broadcast Logic:** Efficiently relay messages from one client to all others.
3.  **Client CLI:** Create a script that can both send messages and display incoming messages asynchronously.
4.  **Resilience:** Handle `ConnectionResetError` and clean up the client registry on disconnect.

## 💻 Solution Implementation

```python
--8<-- "infrastructure_challenges/socket_chat_app/PROBLEM.md"
```

!!! success "Why this works"
    Building a socket-level application provides deep insight into networking fundamentals like latency, packet loss, and the overhead of maintaining persistent connections.
