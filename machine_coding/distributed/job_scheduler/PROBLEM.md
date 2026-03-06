# ⏲️ Distributed System: Scalable Job Scheduler

## 📝 Overview
A **Distributed Job Scheduler** is responsible for managing the execution of tasks across a cluster of machines. It optimizes resource utilization by matching job requirements (priority, dependencies) with available worker capacity.

!!! abstract "Core Concepts"
    - **Priority Queuing:** Ensuring high-importance jobs are processed before lower-priority ones.
    - **Worker Distribution:** Balancing the load across multiple execution nodes.
    - **Fault Tolerance:** Detecting worker failure and re-queuing orphaned jobs.

## 🚀 Problem Statement
Design a system that can scale to 1 million jobs per day. The system must accept jobs with DAG-based dependencies, distribute them across a pool of workers, and provide robust monitoring and retry mechanisms.

## 🧠 Thinking Process & Approach
Distributed scheduling requires handling dependencies and node failures. The approach uses a DAG-based dependency resolver (Topological Sort) and a shared task queue to distribute work among multiple worker processes.

### Key Observations:
- DAG dependency resolution.
- Fault-tolerant task distribution.

### Technical Constraints
- **High Throughput:** Design for minimal scheduling overhead.
- **Idempotency:** Prevent duplicate executions of the same job.
- **Worker Heartbeats:** Maintain a mechanism to detect and handle node failures.

## 🛠️ Requirements
1. Implement the core logic as described in the overview.
2. Ensure proper decoupling and adherence to the pattern.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/job_scheduler/job_scheduling_system.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
