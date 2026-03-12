# ⛓️ Machine Coding: Enterprise Workflow Orchestrator (DAG Engine)

## 📝 Overview
A **Workflow Orchestrator** manages the execution of complex tasks defined as a **Directed Acyclic Graph (DAG)**. It handles dependency resolution, parallel execution, and fault tolerance, similar to tools like Apache Airflow or Temporal.

!!! info "Why This Challenge?"

    - **Advanced Data Structures:** Mastering the use of Directed Acyclic Graphs (DAGs) for representing complex workflows.
    - **Parallel Execution Management:** Understanding how to execute independent branches of a graph concurrently to optimize runtime.
    - **Robust Error Handling:** Implementing retry mechanisms and failure recovery at the engine level for business-critical tasks.

!!! abstract "Core Concepts"

    - **DAG Resolution:** Ensuring tasks run only after their dependencies are successfully completed.
    - **Parallelism:** Executing independent branches of the graph simultaneously to minimize total runtime.
    - **Retries & Backoff:** Automatically handling transient failures with smart timing.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **DAG Engine:** Represent tasks/dependencies and prevent circular links.
2.  **Execution Logic:** Run tasks in parallel where possible and support exponential backoff retries.
3.  **Control Flow:** Support conditional branching (e.g., Run B on success, C on failure).
4.  **Observability:** Maintain global workflow state and detailed audit logs.

### Technical Constraints

- **Idempotency:** Ensure that retrying a task doesn't cause inconsistent system states.
- **Cycle Detection:** Prevent infinite loops by validating the graph structure before execution.
- **State Observability:** Provide real-time tracking of every task's lifecycle.

## 🧠 The Engineering Story

**The Villain:** "The Spaghetti Workflow." Intertwining business logic with task execution, leading to a system where adding a single new step breaks the entire chain.

**The Hero:** "The DAG Engine." Decoupling task logic from the execution lifecycle.

**The Plot:**

1. Model tasks as nodes in a graph.
2. Use a `DependencyResolver` to ensure tasks only run after their requirements are met.
3. Implement a `Scheduler` to run independent branches in parallel.
4. Handle retries and failures at the engine level.

**The Twist (Failure):** **The Circular Dependency.** Task A depends on B, which depends on A, causing the engine to hang forever. Use **Topological Sort** for cycle detection.

**Interview Signal:** Mastery of **Graph Theory (DAGs)** and **Concurrent execution management**.

## 🚀 Thinking Process & Approach
Workflow orchestration is essentially a graph traversal problem. The approach uses a Directed Acyclic Graph to represent task dependencies and a scheduler to manage the parallel execution of independent tasks.

### Key Observations:

- Cycle detection is critical for system stability.
- State management must be durable to handle engine restarts.

## 🏗️ Design Patterns Used

- **Command Pattern**: Encapsulating each workflow task as a command object.
- **Composite Pattern**: Building complex workflows out of smaller, reusable task components.
- **State Pattern**: Managing the transition of tasks through various states (SCHEDULED, RUNNING, COMPLETED, FAILED).
- **Observer Pattern**: For monitoring and logging task progress and state changes.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/workflow_orchestrator/dag_engine.py"
```

!!! success "Why this works"
    Decoupling task logic from execution management allows for complex business processes to be modeled clearly and scaled reliably across many worker nodes.

## 🎤 Interview Follow-ups

- **Dynamic DAGs:** How would you handle workflows where the graph structure changes based on the output of an earlier task?
- **Distributed Scheduling:** How do you coordinate task execution across multiple worker machines?
- **Exactly-Once Execution:** How do you ensure a task is executed exactly once even if the worker crashes mid-execution?

## 🔗 Related Challenges

- [Job Scheduler](../job_scheduler/PROBLEM.md) — For executing individual jobs within the workflow.
- [Pub-Sub](../pub_sub/PROBLEM.md) — To trigger workflows based on event streams.
