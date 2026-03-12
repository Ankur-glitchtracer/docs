# 🐳 Infrastructure Challenge: Dockerized Distributed Job Cluster

## 📝 Overview
**Containerization** is the standard for deploying distributed systems. This challenge involves taking a complex application (the Job Scheduler) and orchestrating it using **Docker** and **Docker Compose** to simulate a production cluster on your local machine.

!!! abstract "Core Concepts"

    - **Container Orchestration:** Managing the lifecycle and networking of multiple services (Master, Workers, Redis).
    - **Environment Isolation:** Ensuring the application runs identically regardless of the underlying host OS.
    - **Service Discovery:** Allowing containers to communicate with each other using service names instead of static IPs.

!!! info "Why This Challenge?"

    - **Mastery of Container Orchestration:** Learn how to manage the lifecycle and networking of multiple interdependent services.
    - **Production-grade Local Development:** Bridge the gap between "it works on my machine" and "it works in production" using Docker Compose.
    - **Service Resilience Testing:** Gain hands-on experience in simulating and handling service failures in a distributed environment.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Architecture Setup:** Create a FastAPI Master, 3 Python Workers, a Redis queue, and a PostgreSQL/SQLite database.
2.  **Docker Compose:** Write a `docker-compose.yml` to spin up the cluster with a single command.
3.  **Fault Tolerance Simulation:** Prove that if a worker container is killed, another worker picks up the job from the Redis queue.

### Technical Constraints

- **Resource Management:** Limiting CPU/Memory per container to simulate a constrained environment.
- **Volume Persistence:** Ensuring job status logs survive container restarts.
- **Networking:** Configuring a shared network for the Master, Workers, and Redis.

## 🧠 The Engineering Story

**The Villain:** "The Configuration Hell." Your Python scheduler works on macOS but fails on Linux because of a missing `libpq` version. Your teammate can't even run it because they have Python 3.12 and you used 3.9.

**The Hero:** "The Immutable Container." A Docker image that packages the code, runtime, and OS dependencies into a single, portable unit.

**The Plot:**

1. Define `Dockerfiles` for the Master and Worker nodes.
2. Use `Docker Compose` to orchestrate Master, Worker, Redis, and DB.
3. Set up a `Virtual Network` so containers can communicate by name.
4. Use `Volumes` to persist job logs even if containers are wiped.

**The Twist (Failure):** **The Image Bloat.** A 2GB Docker image that takes 10 minutes to pull, making "Rapid Auto-scaling" impossible. Use Multi-stage builds to trim it down.

**Interview Signal:** Mastery of **Infrastructure-as-Code**, **Service Orchestration**, and **Deployment Portability**.

## 🚀 Thinking Process & Approach
Moving a distributed system to a containerized model requires careful consideration of networking and persistence. The approach involves defining a multi-container architecture where services are decoupled and can scale independently using Docker Compose as the orchestrator.

### Key Observations:

- Multi-container networking allows for seamless service discovery.
- Resource management (CPU/Memory limits) ensures system stability in constrained environments.

## 💻 Solution Implementation

```yaml
--8<-- "infrastructure_challenges/dockerized_job_scheduler/docker_compose.yml"
```

!!! success "Why this works"
    Docker Compose allows you to replicate complex, multi-service production environments locally, making it trivial to test scaling, networking, and system resilience.

## 🎤 Interview Follow-ups

- **Scaling Probe:** How would you scale the workers dynamically based on the Redis queue length?
- **Health Checks:** How would you implement Docker health checks to ensure the Master only sends jobs to healthy workers?
- **Security:** What are the security implications of running containers as root, and how would you mitigate them?

## 🔗 Related Challenges

- [Redis Rate Limiter](../redis_rate_limiter/PROBLEM.md) — Learn how to handle distributed state.
- [Socket Chat App](../socket_chat_app/PROBLEM.md) — Deep dive into low-level networking.
