# ✈️ Mediator Pattern: ATC Flight Coordination

## 📝 Overview
The **Mediator Pattern** reduces chaotic dependencies between objects by forcing them to communicate via a central mediator. This prevents objects from referring to each other explicitly, allowing for a loosely coupled system.

!!! abstract "Core Concepts"
    - **Centralized Coordination:** A single point of truth (ATC) for managing complex interactions.
    - **Loose Coupling:** Aircraft don't need to know about each other; they only talk to the mediator.

## 🚀 Problem Statement
Design an Air Traffic Control (ATC) system where multiple aircraft interact. If every aircraft had to communicate directly with every other aircraft to coordinate take-offs and landings, the network would become unmanageably complex and dangerous.

### Technical Constraints
- **Safety Isolation:** Aircraft must never talk to another aircraft directly.
- **Runway Management:** The mediator must strictly control access to the shared runway resource.

## 🛠️ Requirements
1.  **Aircraft Types:** Implement `Boeing`, `Airbus`, and `PrivateJet`.
2.  **Mediation Logic:** Aircraft must request permission from the `ATCMediator` to land or take off.
3.  **State Management:** The mediator must track runway status and manage a queue of aircraft.
4.  **Concurrency:** Only one aircraft can have landing/take-off permission at a time.

!!! success "Why this works"
    It simplifies the communication logic by centralizing it. The aircraft are simplified because they don't need to handle collision avoidance logic themselves—they simply follow instructions from the mediator.
