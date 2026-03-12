# Module 5: API Design & Gateway Patterns

### 🚀 Problem Statement
A GenAI platform exposes 47 microservice endpoints. The mobile app makes 12 API calls to render a single enterprise document view. Each call has its own auth check, rate limit logic, and error format. Adding a new client (Teams bot, email integration) requires coordinating with 8 teams.

### 🧠 The Engineering Story

**The Villain:** "The Spaghetti Integration." Every client talks directly to every microservice. Each service implements its own auth, rate limiting, and versioning. A change in the embedding service breaks the mobile app.

**The Hero:** "The API Gateway." A single entry point that handles cross-cutting concerns and composes backend calls into client-optimized responses.

**The Plot:**

1. Design RESTful APIs with proper resource modeling (not RPC-over-REST)
2. Implement an API Gateway for auth, rate limiting, request aggregation
3. Use BFF (Backend-for-Frontend) pattern for mobile vs web vs bot clients
4. Design streaming APIs for LLM token output (SSE vs WebSocket)
5. Version APIs without breaking existing clients

**The Twist (Failure):** **The God Gateway.** Placing too much logic in the gateway can turn it into a single point of failure with significant latency overhead. It may become harder to deploy than the microservices themselves.

**Interview Signal:** Can articulate the difference between API Gateway, BFF, and Service Mesh — and when each is appropriate.

### 🧠 Key Patterns

| Pattern | Use Case | Context |
|---------|----------|--------------|
| **API Gateway** | Cross-cutting concerns | Auth, rate-limit, logging for all services |
| **BFF** | Client-specific aggregation | Mobile gets minimal payload, web gets full document view |
| **SSE (Server-Sent Events)** | Uni-directional streaming | LLM token streaming to browser |
| **GraphQL** | Flexible client queries | Dashboard with customizable document report views |
| Idempotency Keys | Safe retries | Prevent duplicate document revisions on network retry |

### 🔗 Case Study References
- [Rate Limiter Architecture](../../architectures/utilities/RATE_LIMITER.md) — For deep dive on traffic control and distributed state.
