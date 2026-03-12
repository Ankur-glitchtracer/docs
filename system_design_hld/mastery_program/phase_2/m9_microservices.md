# Module 9: Microservices, Service Mesh & Communication

### 🚀 Problem Statement
A GenAI monolith might handle document management, Core Engine logic, embedding generation, LLM orchestration, user auth, notifications, and analytics. Deploying a fix to the document revision logic in such a system requires redeploying everything, including GPU-intensive services.

### 🧠 The Engineering Story

**The Villain:** "The Monolith That Knew Too Much." Every component shares the same database, the same deployment pipeline, and the same Python process. A memory leak in the analytics module crashes the LLM inference.

**The Hero:** "The Bounded Context." Each business domain becomes an independent service with its own data store, deployment lifecycle, and scaling characteristics.

**The Plot:**

1. Decompose by business capability (DDD bounded contexts)
2. Choose communication: sync (gRPC) vs async (events) per boundary
3. Implement service discovery and circuit breakers
4. Deploy a service mesh (Istio/Linkerd) for observability and traffic control

**The Twist (Failure):** **Distributed Monolith.** Splitting into 15 services that all share the same database and must be deployed together results in the operational complexity of microservices with none of the benefits.

**Interview Signal:** Can identify when NOT to use microservices — and explain the "modular monolith" alternative.

### 🧠 Service Decomposition for the technical stack

| Service | Responsibility | Communication | Scaling Profile |
|---------|---------------|---------------|----------------|
| **Document Service** | CRUD, versions, revisions | REST/gRPC (sync) | CPU-light, I/O bound |
| **Core Engine** | data record logic | gRPC (sync) | CPU-medium |
| **Embedding Service** | Text → vector embedding | gRPC (sync, batch) | GPU-heavy, bursty |
| **LLM Orchestrator** | Prompt → response | Async queue + SSE | GPU-heavy, long-running |
| **Comment Service** | Comments, threads | REST (sync) | CPU-light |
| **Search Service** | Hybrid vector + keyword | gRPC (sync) | Memory-heavy |
| **Notification Service** | Email, Teams, push | Async events | I/O bound |
