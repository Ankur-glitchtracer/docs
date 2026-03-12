# ⏲️ Machine Coding: Scalable Job Scheduler

## 📝 Overview
A **Distributed Job Scheduler** is responsible for managing the execution of tasks across a cluster of machines. It optimizes resource utilization by matching job requirements (priority, dependencies) with available worker capacity.

!!! info "Why This Challenge?"

    - **Distributed Systems Mastery:** Building a job scheduler requires handling node failures, heartbeats, and consistency across a cluster.
    - **DAG Processing:** Implementing dependency resolution through topological sorting is a core skill for workflow orchestration.
    - **Fault Tolerance & Reliability:** Designing mechanisms for job retries and handling "zombie" jobs ensures high system availability.

!!! abstract "Core Concepts"

    - **Priority Queuing:** Ensuring high-importance jobs are processed before lower-priority ones.
    - **Worker Distribution:** Balancing the load across multiple execution nodes.
    - **Fault Tolerance:** Detecting worker failure and re-queuing orphaned jobs.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1. **Job Submission:** Accept jobs with priority and DAG-based dependencies.
2. **Distribution:** Distribute jobs across a pool of workers.
3. **Monitoring:** Provide robust monitoring and retry mechanisms.
4. **Scale:** Handle up to 1 million jobs per day.

### Technical Constraints

- **High Throughput:** Design for minimal scheduling overhead.
- **Idempotency:** Prevent duplicate executions of the same job.
- **Worker Heartbeats:** Maintain a mechanism to detect and handle node failures.

## 🧠 The Engineering Story

**The Villain:** "The Double Execution." Two workers pick up the same high-priority job from the database at the exact same millisecond. The job (e.g., "Send Invoice") runs twice, double-charging the customer.

**The Hero:** "The Distributed Lock & State Machine." Using Redis/Zookeeper to ensure "At-Most-Once" or "At-Least-Once" execution semantics.

**The Plot:**

1. Use a `PriorityQueue` to manage the job backlog.
2. Implement `Workers` that pull jobs and heartbeat their status.
3. Use a `Topological Sort` to handle DAG-based job dependencies.
4. Handle retries with exponential backoff.

**The Twist (Failure):** **The Zombie Job.** A worker crashes mid-job without releasing the lock, blocking that job ID forever until a "Janitor" process reclaims it.

**Interview Signal:** Mastery of **Distributed Consistency**, **Fault Tolerance**, and **DAG processing**.

## 🚀 Thinking Process & Approach
Distributed scheduling requires handling dependencies and node failures. The approach uses a DAG-based dependency resolver (Topological Sort) and a shared task queue to distribute work among multiple worker processes.

### Key Observations:

- DAG dependency resolution.
- Fault-tolerant task distribution.

## 🏗️ Design Patterns Used

- **Command Pattern**: Encapsulating jobs as objects that can be queued and executed.
- **Strategy Pattern**: Different scheduling algorithms (Priority, FIFO, Round-robin).
- **State Pattern**: Tracking job lifecycle (PENDING, RUNNING, COMPLETED, FAILED).
- **Observer Pattern**: Monitoring worker health and job status updates.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/job_scheduler/job_scheduling_system.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability:** How would you scale the scheduler to handle 10 million jobs per day?
- **Consistency:** How do you handle the case where a job is completed but the worker crashes before reporting success?
- **Resource Isolation:** How would you ensure one type of job doesn't starve others?

## 🔗 Related Challenges

- [Workflow Orchestrator](../workflow_orchestrator/PROBLEM.md) — For more complex multi-step dependencies.
- [Rate Limiter](../rate_limiter/PROBLEM.md) — To control the rate of job submissions.
