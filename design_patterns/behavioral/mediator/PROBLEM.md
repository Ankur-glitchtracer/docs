# ✈️ Mediator: ATC Flight Coordination

## 📝 Overview
The **Mediator Pattern** reduces chaotic dependencies between objects by forcing them to communicate via a central mediator. This prevents objects from referring to each other explicitly, allowing for a loosely coupled system.

!!! abstract "Core Concepts"

    - **Centralized Coordination:** A single point of truth (ATC) for managing complex interactions.
        - **Loose Coupling:** Aircraft don't need to know about each other; they only talk to the mediator.

!!! info "Why Use This Pattern?"

    - **Reduces chaotic dependencies between objects**
    - **Encapsulates how objects interact**
    - **Simplifies object communication via a central point**


## 🚀 Problem Statement
Design an Air Traffic Control (ATC) system where multiple aircraft interact. If every aircraft had to communicate directly with every other aircraft to coordinate take-offs and landings, the network would become unmanageably complex and dangerous.

## 🛠️ Requirements

1.  **Mediator Interface:** Define the contract for communication between aircraft.
2.  **Concrete Mediator:** Implement the `ATCMediator` to manage runway access.
3.  **Colleague Classes:** Implement aircraft types like `Boeing`, `Airbus`, and `PrivateJet`.
4.  **Concurrency Control:** Ensure only one aircraft can use the runway at a time.

### Technical Constraints

- **Safety Isolation:** Aircraft must never talk to another aircraft directly.
- **Runway Management:** The mediator must strictly control access to the shared runway resource.

## 🧠 Thinking Process & Approach
In complex systems where many objects must interact, direct communication leads to "Spaghetti" coupling. The approach is to introduce a Mediator that encapsulates the interaction logic, allowing participants (colleagues) to remain independent and focused on their own state.

### Key Observations:

- Reduces the number of connections between objects from $O(N^2)$ to $O(N)$.
- Centralizes control logic for easier maintenance.
- Enhances safety by isolating participants from direct interaction.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/mediator/mediator.py"
```

!!! success "Why this works"
    It simplifies the communication logic by centralizing it. The aircraft are simplified because they don't need to handle collision avoidance logic themselves—they simply follow instructions from the mediator.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Facade](../../structural/facade/smart_home_facade/PROBLEM.md) — Mediator centralizes communication; Facade centralizes an interface to a subsystem.
- [Observer](../observer/basic_observer/PROBLEM.md) — Mediator can use Observer to dynamically register colleagues.
