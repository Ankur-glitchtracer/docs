# 👀 Observer Pattern: Core Subscription Mechanics

## 📝 Overview
The **Observer Pattern** is the fundamental building block for reactive programming. It allows a "Subject" to maintain a list of interested "Observers" and notify them whenever an interesting event occurs.

!!! abstract "Core Concepts"

    - **Subject Registry:** A simple mechanism to `attach()` and `detach()` listeners.
        - **Broadcast Mechanism:** Iterating through the registry to call a notification method on each listener.

!!! info "Why Use This Pattern?"

    - **Implements a one-to-many dependency**
    - **Automatically notifies all dependents of changes**
    - **Promotes loose coupling between objects**


## 🚀 Problem Statement
Implement a minimal version of the observer pattern to demonstrate the core mechanics of registration and notification. The goal is to show how a change in a `Subject` can trigger actions in multiple `Observers` without direct coupling.

## 🛠️ Requirements

1. Subject/EventBus.
2. Observer Interface.
3. Concrete Observers.

### Technical Constraints

- **Simplicity:** Focus on the "bare-bones" structure: a list of listeners and a `notify()` loop.
- **Reliability:** Ensure that removing an observer during a notification loop doesn't crash the system.

## 🧠 Thinking Process & Approach
Hardcoding notifications into a sensor makes it rigid. The approach uses an Event Bus or a Subject that maintains a dynamic list of subscribers. This allows any part of the system to 'react' to an event without the source ever knowing who they are.

### Key Observations:

- Loose coupling through event dispatching.
- Dynamic subscription management at runtime.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/observer/basic_observer/basic_observer.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Mediator](../../mediator/PROBLEM.md) — Observer distributes communication; Mediator centralizes it.
- [Singleton](../../../creational/singleton/singleton_pattern/PROBLEM.md) — Observer managers are often Singletons.
- [MVC](../../mvc/PROBLEM.md) — The Model-View relationship in MVC is often implemented using Observer.
