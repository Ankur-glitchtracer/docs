# 🏗️ Machine Coding: Custom CI/CD Pipeline

## 📝 Overview
A **CI/CD (Continuous Integration / Continuous Deployment) Pipeline** automates the process of moving code from a repository to a production environment. This challenge focuses on building a modular, extensible engine that can execute a series of validation and deployment steps.

!!! info "Why This Challenge?"

    - **Operational Reliability:** Learning how to build systems that automate business-critical processes with high confidence.
    - **Transactional Workflows:** Understanding how to encapsulate individual steps as commands to support rollbacks and retries.
    - **Pattern Integration:** Mastering the combination of Template Method, Command, and Chain of Responsibility patterns.

!!! abstract "Core Concepts"

    - **Pipeline as Code:** Defining execution steps via a configuration (like YAML).
    - **Validation Chains:** Ensuring code passes every quality gate before reaching production.
    - **Task Encapsulation:** Treating individual build steps as independent, undoable operations.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Command Pattern:** Encapsulate steps like `GitPull`, `RunTests`, and `Deploy` as objects.
2.  **Chain of Responsibility:** Use a pipeline of validators (`Syntax` -> `Unit` -> `Integration`).
3.  **Template Method:** Define the standard deployment skeleton while allowing custom steps.
4.  **Observer:** Stream build logs to the console or a file in real-time.

### Technical Constraints

- **Sequential Execution:** Steps must run in a specific order; failure in one step must halt the pipeline.
- **Rollback Support:** The system should ideally be able to undo a deployment if a post-deploy check fails.
- **Logging:** All step outputs must be captured and streamed for observability.

## 🧠 The Engineering Story

**The Villain:** "The Brittle Script." A single bash script that handles pulling, testing, and deploying. One failure in the middle leaves the server in a half-deployed, broken state.

**The Hero:** "The Transactional Pipeline." Encapsulates each step as a Command and uses a Template Method to enforce a safe, standard workflow.

**The Plot:**

1. Define a `Pipeline` template with hooks for `setup`, `test`, `build`, and `deploy`.
2. Encapsulate each step into a `Command` object.
3. Use a `Chain of Responsibility` to validate requirements at each gate.
4. Notify observers (Slack/Logs) of the pipeline status.

**The Twist (Failure):** **The Rollback Loop.** A deployment fails, triggers a rollback, which also fails, entering an infinite loop of recovery attempts.

**Interview Signal:** Mastery of **Operational Reliability** and **Pattern Integration**.

## 🚀 Thinking Process & Approach
Pipeline automation requires strict sequencing and error handling. The approach uses the **Template Method** to define the invariant lifecycle, while the **Command Pattern** allows individual steps to be swapped or retried independently.

### Key Observations:

- Invariant workflow vs variant steps.
- Failure propagation and rollback requirements.

## 🏗️ Design Patterns Used

- **Template Method Pattern**: To define the fixed skeleton of the CI/CD process (Pull -> Test -> Build -> Deploy).
- **Command Pattern**: To encapsulate each build/test step as an object that can be executed, logged, and potentially undone.
- **Chain of Responsibility Pattern**: For sequential validation gates where each gate must pass before the next begins.
- **Observer Pattern**: To notify external systems (Slack, Email, Dashboards) about the pipeline's progress and final status.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/real_world_systems/ci_cd_pipeline/ci_cd_pipeline.py"
```

!!! success "Why this works"
    The Template Method ensures consistent deployment standards across the organization, while the Command and Chain patterns provide the granular control and validation needed for safe automation.

## 🎤 Interview Follow-ups

- **Parallelism:** How would you modify the engine to run independent test suites in parallel?
- **Artifact Management:** How would you handle the storage and versioning of build artifacts (e.g., Docker images, JAR files)?
- **Environment Isolation:** How do you ensure that the pipeline execution doesn't pollute the host environment? (Containers/Virtualenvs)

## 🔗 Related Challenges

- [Workflow Orchestrator](../../distributed/workflow_orchestrator/PROBLEM.md) — For more complex DAG-based dependency management.
- [Job Scheduler](../../distributed/job_scheduler/PROBLEM.md) — For distributing pipeline tasks across a cluster of workers.
