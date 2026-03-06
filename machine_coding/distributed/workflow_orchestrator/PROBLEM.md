# ⛓️ Distributed System: Enterprise Workflow Orchestrator (DAG Engine)

## 📝 Overview
A **Workflow Orchestrator** manages the execution of complex tasks defined as a **Directed Acyclic Graph (DAG)**. It handles dependency resolution, parallel execution, and fault tolerance, similar to tools like Apache Airflow or Temporal.

!!! abstract "Core Concepts"
    - **DAG Resolution:** Ensuring tasks run only after their dependencies are successfully completed.
    - **Parallelism:** Executing independent branches of the graph simultaneously to minimize total runtime.
    - **Retries & Backoff:** Automatically handling transient failures with smart timing.

## 🚀 Problem Statement
Design an engine capable of executing non-linear workflows. The system must be able to parse a set of tasks, detect circular dependencies, and manage the state of execution across a potentially distributed environment.

### Technical Constraints
- **Idempotency:** Ensure that retrying a task doesn't cause inconsistent system states.
- **Cycle Detection:** Prevent infinite loops by validating the graph structure before execution.
- **State Observability:** Provide real-time tracking of every task's lifecycle.

## 🛠️ Requirements
1.  **DAG Engine:** Represent tasks/dependencies and prevent circular links.
2.  **Execution Logic:** Run tasks in parallel where possible and support exponential backoff retries.
3.  **Control Flow:** Support conditional branching (e.g., Run B on success, C on failure).
4.  **Observability:** Maintain global workflow state and detailed audit logs.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/distributed/workflow_orchestrator/PROBLEM.md"
```

!!! success "Why this works"
    Decoupling task logic from execution management allows for complex business processes to be modeled clearly and scaled reliably across many worker nodes.
