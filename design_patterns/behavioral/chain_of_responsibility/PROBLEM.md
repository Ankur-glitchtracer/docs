# ⛓️ Chain of Responsibility: Middleware Pipeline

## 📝 Overview
The **Chain of Responsibility** pattern lets you pass requests along a chain of handlers. Upon receiving a request, each handler either processes it or passes it to the next handler in the chain, allowing for flexible processing pipelines.

!!! abstract "Core Concepts"
    - **Handler Chaining:** Linking objects so they can pass requests down the line.
    - **Single Responsibility:** Each handler only cares about one thing (e.g., Auth, Logging, or Throttling).

## 🚀 Problem Statement
You are building a web server middleware pipeline. Incoming requests need to be authenticated, logged, throttled, and then processed. Hardcoding this sequence into a single giant function makes the pipeline difficult to reorder or extend with new steps.

### Technical Constraints
- **Flexible Ordering:** Handlers should be able to be rearranged easily without breaking the pipeline.
- **Early Exit:** A handler (like `AuthHandler`) must be able to stop the request from proceeding further if validation fails.

## 🛠️ Requirements
1.  **Handler Interface:** Define a standard `handle(request)` method and a `set_next()` mechanism.
2.  **Concrete Handlers:** Implement `AuthHandler`, `LoggingHandler`, and `ThrottlingHandler`.
3.  **Request Object:** A simple container for `url`, `token`, and `timestamp`.
4.  **Extensibility:** Add a `ContentValidationHandler` at any point in the chain without modifying existing code.

!!! success "Why this works"
    It decouples the sender of a request from its receivers. By using a chain, you can dynamically build pipelines at runtime, making the system highly modular and easily testable by isolating each processing step.
