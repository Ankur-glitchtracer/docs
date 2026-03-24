# 🏗️ HLD Concept: Networking Essentials

## 📝 Definition
Networking forms the foundation of distributed systems, enabling independent devices to communicate and coordinate. It relies on layered architectures (often modeled after the OSI model), which provide abstractions that allow application developers to exchange data without managing hardware-level electronic signals or routing mechanics. 

In system design interviews, the focus primarily revolves around three key layers:
*   **Layer 3 (Network Layer):** Handled by IP (Internet Protocol), responsible for routing, addressing, and providing best-effort delivery to destination IPs across the internet.
*   **Layer 4 (Transport Layer):** Handled by protocols like TCP and UDP, which establish end-to-end communication services and govern reliability, ordering, and flow control.
*   **Layer 7 (Application Layer):** Handled by protocols like HTTP, WebSockets, and WebRTC, which provide high-level abstractions for different types of web application data and APIs.

## 🚀 Why it matters
Networking decisions impact every aspect of a distributed system, from latency and throughput to reliability and security. Because you will almost always be designing systems comprised of independent components communicating over a network, your choices around transport protocols, API paradigms, load balancing, and failure handling will dictate whether your architecture can survive real-world scale and internet volatility.

## ⚖️ Trade-offs & Decisions

### Transport Protocols (Layer 4)
| TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) | When to use what? |
| :--- | :--- | :--- |
| Connection-oriented, guarantees ordered and reliable delivery, includes flow and congestion control, but carries higher latency overhead. | Connectionless, fast "spray and pray" delivery with no guarantees on ordering, delivery, or flow control. | **TCP** is the default for almost everything where data integrity matters. Use **UDP** when speed is more important than reliability (e.g., live video streaming, VoIP, gaming). |

### API Paradigms (Layer 7)
| REST | GraphQL | gRPC | When to use what? |
| :--- | :--- | :--- | :--- |
| Simple, stateless, and relies on standard HTTP methods operating on resources. Uses JSON, which can be inefficient to serialize. | Allows clients to flexibly request exactly the data they need, preventing over-fetching and under-fetching. | High-performance RPC using HTTP/2 and Protocol Buffers. Uses a binary, strongly-typed schema that is extremely efficient. | Default to **REST** for public-facing APIs. Use **GraphQL** when complex frontends need flexible data fetching from multiple domains. Use **gRPC** for internal service-to-service communication where performance is critical. |

### Real-Time Communication
| Server-Sent Events (SSE) | WebSockets | WebRTC | When to use what? |
| :--- | :--- | :--- | :--- |
| Unidirectional push from server to client over a single HTTP connection. | Bi-directional, persistent connection upgraded from HTTP, enabling real-time binary or text message exchange. | Direct peer-to-peer communication over UDP, requiring STUN/TURN servers for NAT traversal. | Use **SSE** for simple push notifications. Use **WebSockets** for high-frequency, bi-directional features like chat apps. Use **WebRTC** exclusively for peer-to-peer audio/video calling. |

### Load Balancing
| Layer 4 (Network) Load Balancing | Layer 7 (Application) Load Balancing | Client-Side Load Balancing |
| :--- | :--- | :--- |
| Operates on IP/Port without inspecting packet contents. Maintains persistent TCP connections between client and server. | Terminates connections, inspects HTTP content (URLs, cookies), and intelligently routes requests to backend servers. | Clients query a registry (or DNS) and connect directly to servers. |
| **When to use:** Great for persistent connections like WebSockets or raw performance needs. | **When to use:** Ideal for standard HTTP/REST traffic and API Gateway routing. | **When to use:** Ideal for internal microservices or when using distributed clusters like Redis. |

## 🛠️ Implementation Strategies

- **Handling Network Failures:** The assumption that "the network is reliable" is a dangerous fallacy. Implement **Timeouts** to avoid hanging requests, and use **Retries with Exponential Backoff and Jitter** to safely handle transient failures without creating a "thundering herd" that overwhelms recovering services. 
- **Ensuring Safe Retries:** Because network retries can result in duplicate actions, design APIs to be **Idempotent**. For write operations, require clients to pass an *Idempotency Key* so the server can guarantee the action is only processed once.
- **Preventing Cascading Failures:** Use the **Circuit Breaker** pattern when calling external dependencies. If failures exceed a threshold, the circuit "trips" open to fail fast, reducing load on the struggling service and preventing the failure from consuming resources across your entire system.
- **Reducing Latency:** Speed of light limitations mean geographic distance causes unavoidable latency. Use **Content Delivery Networks (CDNs)** to cache static assets at edge locations close to users. For dynamic data, use **Regional Partitioning** to co-locate users, services, and databases within the same geographic area.
- **Maintaining High Availability:** Use load balancers configured with **Health Checks** to continuously monitor backend servers via TCP or HTTP. If a server crashes, the load balancer will automatically route traffic away from it to healthy nodes.

## 🧠 Interview Talk-Track
- **Key Insight:** Do not over-engineer your communication protocols prematurely. Most systems should default to TCP and REST unless specific non-functional requirements dictate otherwise. You can earn strong signals by correctly anticipating failures and stating, "I am adding retries with exponential backoff and jitter to handle transient network faults".
- **Common Pitfall:** Candidates frequently try to jump to specialized protocols like WebSockets, gRPC, or WebRTC just to sound impressive, which often alienates interviewers if the core system doesn't actually need them. For instance, proposing WebRTC for generic collaborative applications is usually a mistake, as WebRTC is highly complex and mostly reserved for video/audio conferencing.

!!! abstract "Core Takeaway"
    Networking in HLD interviews is about choosing the simplest protocol that meets the requirements (usually HTTP/REST over TCP) and pairing it with robust failure handling mechanisms (Idempotency, Circuit Breakers, Exponential Backoff) and intelligent scaling (L4/L7 Load Balancing, CDNs) to create a resilient architecture.
