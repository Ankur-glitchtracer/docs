# 🐳 Infrastructure Challenge: Dockerized Distributed Job Cluster

## 📝 Overview
**Containerization** is the standard for deploying distributed systems. This challenge involves taking a complex application (the Job Scheduler) and orchestrating it using **Docker** and **Docker Compose** to simulate a production cluster on your local machine.

!!! abstract "Core Concepts"
    - **Container Orchestration:** Managing the lifecycle and networking of multiple services (Master, Workers, Redis).
    - **Environment Isolation:** Ensuring the application runs identically regardless of the underlying host OS.
    - **Service Discovery:** Allowing containers to communicate with each other using service names instead of static IPs.

## 🚀 Problem Statement
Transform the "Scalable Job Scheduler" into a fully dockerized environment. You must define an architecture where a Master node schedules work into a Redis queue, and multiple independent Worker containers consume and process those jobs.

### Technical Constraints
- **Multi-Container Networking:** Configuring a shared network for the Master, Workers, and Redis.
- **Resource Management:** Limiting CPU/Memory per container to simulate a constrained environment.
- **Volume Persistence:** Ensuring job status logs survive container restarts.

## 🛠️ Requirements
1.  **Architecture Setup:** Create a FastAPI Master, 3 Python Workers, a Redis queue, and a PostgreSQL/SQLite database.
2.  **Docker Compose:** Write a `docker-compose.yml` to spin up the cluster with a single command.
3.  **Fault Tolerance Simulation:** Prove that if a worker container is killed, another worker picks up the job from the Redis queue.

## 💻 Solution Implementation

```python
--8<-- "infrastructure_challenges/dockerized_job_scheduler/PROBLEM.md"
```

!!! success "Why this works"
    Docker Compose allows you to replicate complex, multi-service production environments locally, making it trivial to test scaling, networking, and system resilience.
