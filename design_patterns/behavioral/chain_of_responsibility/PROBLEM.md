# ⛓️ Chain of Responsibility: Middleware Pipeline

## 📝 Overview
The **Chain of Responsibility** pattern lets you pass requests along a chain of handlers. Upon receiving a request, each handler either processes it or passes it to the next handler in the chain, allowing for flexible processing pipelines.

!!! abstract "Core Concepts"

    - **Handler Chaining:** Linking objects so they can pass requests down the line.
        - **Single Responsibility:** Each handler only cares about one thing (e.g., Auth, Logging, or Throttling).

!!! info "Why Use This Pattern?"

    - **Decouples sender of a request from its receivers**
    - **Allows multiple objects to handle a request**
    - **Enables dynamic addition of new handlers**


## 🚀 Problem Statement
You are building a web server middleware pipeline. Incoming requests need to be authenticated, logged, throttled, and then processed. Hardcoding this sequence into a single giant function makes the pipeline difficult to reorder or extend with new steps.

## 🛠️ Requirements

1.  **Handler Interface:** Define a standard `handle(request)` method and a `set_next()` mechanism.
2.  **Concrete Handlers:** Implement `AuthHandler`, `LoggingHandler`, and `ThrottlingHandler`.
3.  **Request Object:** A simple container for `url`, `token`, and `timestamp`.
4.  **Extensibility:** Add a `ContentValidationHandler` at any point in the chain without modifying existing code.

### Technical Constraints

- **Flexible Ordering:** Handlers should be able to be rearranged easily without breaking the pipeline.
- **Early Exit:** A handler (like `AuthHandler`) must be able to stop the request from proceeding further if validation fails.

## 🧠 Thinking Process & Approach
(To be detailed...)

## 💻 Solution Implementation

```python
# (To be detailed...)
```

!!! success "Why this works"
    It decouples the sender of a request from its receivers. By using a chain, you can dynamically build pipelines at runtime, making the system highly modular and easily testable by isolating each processing step.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Composite](../../structural/composite/organisation_chart/PROBLEM.md) — Chain of Responsibility can be implemented using Composite.
- [Command](../command/smart_home_hub/PROBLEM.md) — Handlers in Chain of Responsibility can be implemented as Commands.
