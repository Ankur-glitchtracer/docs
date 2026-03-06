# ⏲️ Distributed System: Scalable Job Scheduler

## 📝 Overview
A **Distributed Job Scheduler** is responsible for managing the execution of tasks across a cluster of machines. It optimizes resource utilization by matching job requirements (priority, dependencies) with available worker capacity.

!!! abstract "Core Concepts"
    - **Priority Queuing:** Ensuring high-importance jobs are processed before lower-priority ones.
    - **Worker Distribution:** Balancing the load across multiple execution nodes.
    - **Fault Tolerance:** Detecting worker failure and re-queuing orphaned jobs.

## 🚀 Problem Statement
Design a system that can scale to 1 million jobs per day. The system must accept jobs with DAG-based dependencies, distribute them across a pool of workers, and provide robust monitoring and retry mechanisms.

### Technical Constraints
- **High Throughput:** Design for minimal scheduling overhead.
- **Idempotency:** Prevent duplicate executions of the same job.
- **Worker Heartbeats:** Maintain a mechanism to detect and handle node failures.

## 🛠️ Requirements
1.  **Job Dependencies:** Support Directed Acyclic Graphs (DAGs).
2.  **Priority Levels:** Execute jobs based on assigned priority.
3.  **Worker Distribution:** Distribute tasks across multiple workers.
4.  **Fault Tolerance:** Handle worker failures and automatic job retries.
5.  **Monitoring:** Track job status and overall system health.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/job_scheduler/job_scheduling_system.py"
```

!!! success "Why this works"
    Centralized scheduling with distributed execution allows the system to handle massive volumes of work while maintaining strict control over execution order and error recovery.
