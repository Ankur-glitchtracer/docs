# Module 1: Network Fundamentals & Protocols

### 🚀 Problem Statement
A GenAI application makes 200 API calls per user request — embedding lookups, LLM calls, vector DB queries. Users may complain about 8-second latencies. It is often unclear where time is being lost when treating the network as a "magic pipe."

### 🧠 The Engineering Story

**The Villain:** "The Black-Box Network." Engineers may assume HTTP calls are instant and TCP connections are free. A single LLM inference call hides 3 DNS lookups, 2 TLS handshakes, and 4 TCP round-trips.

**The Hero:** "The Protocol-Aware Architect." Understands every millisecond spent in the network stack and designs connection pooling, HTTP/2 multiplexing, and gRPC streaming to eliminate redundancy.

**The Plot:**

1. Map the full lifecycle: DNS → TCP → TLS → HTTP → Response
2. Identify the cost of each hop in a multi-service GenAI pipeline
3. Apply connection reuse, keep-alive, HTTP/2, and gRPC where each excels
4. Understand when WebSockets beat polling (streaming token output)

**The Twist (Failure):** **Head-of-Line Blocking.** Switching to HTTP/2 for LLM streaming might reveal that a single slow response blocks all multiplexed streams on the same TCP connection. HTTP/3 (QUIC) solves this but introduces UDP complexity.

**Interview Signal:** Can articulate the latency breakdown of a single API call and justify protocol choices.

### 🧠 Key Concepts to Master

| Concept | Why It Matters |
|---------|----------------------|
| TCP 3-way handshake | Every new connection to OpenAI/Azure = 1.5 RTT overhead |
| TLS 1.3 | Reduces handshake from 2-RTT to 1-RTT (0-RTT for repeat) |
| HTTP/2 multiplexing | Stream multiple embeddings on single connection |
| gRPC + Protobuf | 10x smaller payloads vs JSON for internal microservices |
| WebSocket | Streaming LLM token-by-token output to frontend |
| DNS resolution caching | Avoid 50ms DNS per API call in container environments |

### 📚 Study Resources
- **Read:** "High Performance Browser Networking" by Ilya Grigorik (Ch 1-4, 11-12)
- **Practice:** Use `curl -w` timing breakdown to profile API calls
- **Lab:** Compare latency of REST vs gRPC vs WebSocket for an embedding service
