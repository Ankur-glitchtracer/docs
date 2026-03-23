# 🏗️ HLD: Microservices & Distributed Patterns

## 📝 Overview
Microservices architecture decomposes a monolithic application into small, independent services that communicate over a network. This module covers patterns for decomposition, migration, and resilience.

!!! abstract "Core Concepts"
    - **Decomposition:** Business Capability vs. Domain-Driven Design (DDD).
    - **Migration:** Strangler Fig Pattern (gradual replacement of monolith).
    - **Data Consistency:** Saga Pattern (Choreography vs. Orchestration) and CQRS (Command Query Responsibility Segregation).
    - **Resilience:** Circuit Breaker, Bulkhead, and Retry patterns.

## 🚀 Key Patterns
### 1. The Saga Pattern
How to handle distributed transactions without 2PC.     
    - **Goal:** Maintain data consistency across multiple microservices.    
    - **Trade-off:** Eventual Consistency vs. Complexity.

### 2. CQRS & Event Sourcing
- **CQRS:** Separating read and write models to optimize performance.
- **Dual Write Problem:** Why updating a DB and sending a message simultaneously is dangerous.

### 3. Infrastructure
- **API Gateway:** Single entry point, request aggregation, and cross-cutting concerns (Auth, Rate Limiting).
- **Service Discovery:** How services find each other (Client-side vs. Server-side).
- **Service Mesh:** Sidecar proxies (Istio/Linkerd) for observability and traffic control.
