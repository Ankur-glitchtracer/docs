# 🏗️ HLD Concept: Real-time Updates

## 📝 Definition
The Real-time Updates pattern addresses the architectural challenge of pushing data from a server to a client immediately as events happen, rather than waiting for the client to explicitly request the information. This pattern encompasses both the client-server protocol used to maintain a persistent connection and the server-side infrastructure (like Pub/Sub systems or consistent hashing) required to route messages to the specific server holding the user's active connection.

## 🚀 Why it matters
For standard synchronous APIs, communication is straightforward: a client sends a request, and the server returns a response once the task is completed. However, modern applications like chat platforms (WhatsApp), live leaderboards, collaborative editors, and notifications require low-latency, real-time data delivery. Implementing this pattern efficiently ensures that millions of concurrent users can receive instantaneous updates without overwhelming the backend infrastructure with constant, resource-intensive requests.

## ⚖️ Trade-offs & Decisions

| Server-Sent Events (SSE) | WebSockets | When to use what? |
| :--- | :--- | :--- |
| Unidirectional push from server to client over a single HTTP connection. It streams multiple messages as "chunks" in a single HTTP response. | Bi-directional, persistent TCP connection established via an HTTP upgrade. Allows both server and client to push binary or text data at any time. | Use **SSE** for simple push notifications or live feeds where data only flows one way. Use **WebSockets** for high-frequency, persistent, bi-directional communication, such as chat applications or multiplayer games. Default to simple **HTTP Polling** if a slight delay (e.g., 5 seconds) is acceptable, as it avoids complex connection management. |

## 🛠️ Implementation Strategies

- **Strategy 1: Decoupling via Pub/Sub:** When managing millions of connections, users will be distributed across hundreds of different servers. To route a message to the correct recipient, you must decouple the publisher from the subscriber using a Pub/Sub service like Redis or Kafka. When a message is sent, the server writes it to the database and publishes it to a Pub/Sub topic (partitioned by user or chat ID). The specific server holding the recipient's active WebSocket connection subscribes to this topic and pushes the payload directly to the client.
- **Strategy 2: Ensuring Reliability and Fallbacks:** Persistent connections frequently drop due to poor network conditions, and TCP keepalives can take minutes to detect a severed connection. Furthermore, Pub/Sub systems like Redis offer "at most once" delivery, meaning messages can be lost during transient failures. To guarantee deliverability, always persist the message to a database or "Inbox" table *before* publishing to the real-time channel. Clients should acknowledge receipt of the message. If the connection fails, combine application-level heartbeats (to detect dead sockets) with periodic background polling as a final backstop to fetch any missed messages.
- **Strategy 3: Stateful Servers & Consistent Hashing:** For applications requiring heavy real-time processing (like collaborative text editing), you may route clients to stateful servers using a consistent hash ring. This ensures all users collaborating on the same entity (e.g., a specific document) maintain connections to the exact same server, keeping synchronization logic localized and efficient.

## 🧠 Interview Talk-Track
- **Key Insight:** Start simple. Determine if true real-time delivery is actually a strict requirement. For example, a live competition leaderboard can often be satisfied with a client polling the server every 5 seconds. This avoids the massive infrastructure overhead of maintaining hundreds of thousands of stateful WebSocket connections.
- **Common Pitfall:** Proposing WebSockets prematurely without justifying the need for high-frequency, bi-directional communication. WebSockets require specialized infrastructure (like Layer 4 load balancers) and introduce significant complexity around connection state management, firewalls, and proxy compatibility.

!!! abstract "Core Takeaway"
    The Real-time Updates pattern is essential for low-latency push communication but introduces significant state management complexity. Always evaluate if simple polling suffices; if not, choose between SSE for unidirectional pushes and WebSockets for bi-directional flows, scaling the backend using Pub/Sub mechanisms to route messages to the correct active connections.
