# 💧 Strategy: Dynamic Sprinkler Scheduler

## 📝 Overview
The **Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. This allows the system to switch between different behaviors (like watering schedules) without modifying the main context.

!!! abstract "Core Concepts"

    - **Interchangeable Algorithms:** Switch between different logic sets (e.g., Weekday vs. Weekend) seamlessly.
        - **Behavioral Decoupling:** The `Sprinkler` doesn't need to know the details of the watering schedule it's running.

!!! info "Why Use This Pattern?"

    - **Defines a family of interchangeable algorithms**
    - **Allows switching behavior at runtime**
    - **Avoids multiple conditional statements**


## 🚀 Problem Statement
You are building a smart sprinkler system that needs to support different watering schedules based on the day of the week or local water restrictions. Hardcoding these rules into the main controller would make it difficult to add new schedules or change existing ones.

## 🛠️ Requirements

1.  **Strategy Interface:** Define the contract for all watering schedules.
2.  **Concrete Strategies:** Implement different schedules (e.g., `WeekdaySchedule`, `WeekendSchedule`).
3.  **Context:** The `Sprinkler` class that uses a strategy to determine its behavior.

### Technical Constraints

- **Runtime Flexibility:** The system must be able to change its active schedule without restarting or re-instantiating the `Sprinkler`.
- **Standardized Interface:** All schedules must follow a common `get_watering_duration()` contract.

## 🧠 Thinking Process & Approach
When we have interchangeable algorithms (like watering schedules), we avoid hardcoding them. The approach uses a Strategy interface that can be swapped at runtime, allowing the main system to behave differently based on the current context.

### Key Observations:

- Runtime algorithmic flexibility.
- Elimination of complex switch statements.
- Decoupling of the execution context from the algorithmic implementation.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/strategy/sprinkler_system/sprinkler_system.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns. It allows for easy extension of system behavior by adding new strategies without touching existing code.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [State](../../state/document_workflow/PROBLEM.md) — State is like Strategy, but the 'strategies' (states) can change the context's state.
- [Template Method](../../template/data_exporter/PROBLEM.md) — Template Method uses inheritance to vary parts of an algorithm; Strategy uses composition.
- [Flyweight](../../../structural/flyweight/forest_simulator/PROBLEM.md) — Strategy objects can be shared as Flyweights.
