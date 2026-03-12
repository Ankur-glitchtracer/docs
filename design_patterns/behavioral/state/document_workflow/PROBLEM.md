# 📑 State Pattern: Enterprise Document Workflow

## 📝 Overview
The **State Pattern** allows an object to alter its behavior when its internal state changes. This is particularly useful for managing complex lifecycles where the same action (e.g., `publish()`) has completely different outcomes depending on the current stage.

!!! abstract "Core Concepts"

    - **State Transition:** Logic for moving between stages (Draft -> Review -> Published) is encapsulated within state objects.
        - **Context Delegation:** The `Document` remains a simple wrapper that delegates all behavior to its current `State`.

!!! info "Why Use This Pattern?"

    - **Allows an object to alter its behavior when state changes**
    - **Removes complex conditional logic (if/else)**
    - **Localizes state-specific behavior**


## 🚀 Problem Statement
Imagine a document editor where a file can be in `Draft`, `Moderation`, or `Published` states. Using a giant `switch` or `if-else` block to handle permissions and transitions for each state makes the code brittle and hard to test as new states are added.

## 🛠️ Requirements

1. State Interface.
2. Concrete States.
3. Context: State management.

### Technical Constraints

- **Admin Overrides:** Transitions in the `Moderation` state should only proceed to `Published` if the user has admin privileges.
- **Action Idempotency:** Calling `publish()` on a document that is already `Published` should have no effect.

## 🧠 Thinking Process & Approach
Massive if-else blocks for status-based logic are hard to maintain. The approach is to represent each state as a class. Transitions are handled by the state objects themselves, effectively 'swapping' the behavior of the main context object.

### Key Observations:

- State-specific logic encapsulation.
- Clean removal of complex conditional branches.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/state/document_workflow/document_workflow.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Strategy](../../strategy/sprinkler_system/PROBLEM.md) — State is like Strategy, but the 'strategies' (states) can change the context's state.
- [Singleton](../../../creational/singleton/singleton_pattern/PROBLEM.md) — State objects are often Singletons.
- [Flyweight](../../../structural/flyweight/forest_simulator/PROBLEM.md) — State objects can be shared as Flyweights.
