# 🛗 Machine Coding: Multi-Elevator Dispatcher

## 📝 Overview
Design an **Elevator Management System** for a high-rise building. This challenge involves complex state management, real-time request handling, and optimization algorithms to minimize passenger wait times.

!!! abstract "Core Concepts"
    - **Request Scheduling:** Efficiently assigning `N` elevators to handle `M` floor requests.
    - **State Control:** Managing the direction (Up, Down, Idle) and current floor for multiple independent units.

## 🚀 Problem Statement
You need to coordinate multiple elevators across many floors. The system must handle both "External" requests (someone on a floor wanting to go up/down) and "Internal" requests (a passenger inside selecting a destination).

### Technical Constraints
- **Directional Logic:** An elevator moving Up should prioritize all Up requests on floors above it before switching directions.
- **Load Balancing:** Avoid sending all elevators to the same floor for a single request.

## 🛠️ Requirements
1.  **Floor Configuration:** Support a configurable number of floors and elevator units.
2.  **Request Handling:** Implement both hall calls and car calls.
3.  **Elevator Logic:** Elevators must move, open/close doors, and update their state based on assigned tasks.
4.  **Optimization:** Minimize total wait time and power consumption.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/elevator/elevator_management_system.py"
```

!!! success "Why this works"
    By treating each elevator as an autonomous state machine and using a central "Dispatcher" to assign tasks, the system achieves high reliability and scalability. The dispatcher can be swapped with different algorithms (like SCAN or Look-Ahead) without affecting the elevator's core movement logic.
