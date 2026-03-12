# 🍬 State Pattern: Intelligent Gumball Vendor

## 📝 Overview
The **State Pattern** allows an object to alter its behavior when its internal state changes. The object will appear to change its class, as its logic is encapsulated into separate state objects rather than a massive `if-else` or `switch` statement.

!!! abstract "Core Concepts"

    - **State Encapsulation:** Each state (e.g., "Has Quarter") is its own class with its own rules.
        - **Automatic Transitions:** The machine moves from one state to another based on user actions.

!!! info "Why Use This Pattern?"

    - **Allows an object to alter its behavior when state changes**
    - **Removes complex conditional logic (if/else)**
    - **Localizes state-specific behavior**


## 🚀 Problem Statement
Building a gumball machine with traditional conditional logic (e.g., `if state == HAS_QUARTER and action == TURN_CRANK`) leads to "spaghetti code" that is impossible to maintain or extend with new states like "Winner" or "Out of Gumballs."

## 🛠️ Requirements

1. State Interface.
2. Concrete States.
3. Context: State management.

### Technical Constraints

- **Action Consistency:** Every action (e.g., `insert_quarter`) must be defined for every possible state.
- **No Global Logic:** The machine's core should only delegate to the current state object.

## 🧠 Thinking Process & Approach
Massive if-else blocks for status-based logic are hard to maintain. The approach is to represent each state as a class. Transitions are handled by the state objects themselves, effectively 'swapping' the behavior of the main context object.

### Key Observations:

- State-specific logic encapsulation.
- Clean removal of complex conditional branches.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/state/gumball_machine_vending/gumball_machine_vending.py"
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
