# 🛗 Machine Coding: Multi-Elevator Dispatcher

## 📝 Overview
Design an **Elevator Management System** for a high-rise building. This challenge involves complex state management, real-time request handling, and optimization algorithms to minimize passenger wait times.

!!! info "Why This Challenge?"

    - **Complex State Management:** Learning how to manage multiple interacting state machines (elevators) that share a common request pool.
    - **Optimization Algorithms:** Understanding how to implement real-world scheduling algorithms like SCAN or LOOK to optimize system throughput.
    - **Concurrency & Event Handling:** Mastering the coordination of asynchronous requests from multiple floors and cabin panels.

!!! abstract "Core Concepts"

    - **Request Scheduling:** Efficiently assigning `N` elevators to handle `M` floor requests.
    - **State Control:** Managing the direction (Up, Down, Idle) and current floor for multiple independent units.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Multi-Elevator Coordination:** Efficiently assign `N` elevators to handle incoming requests.
2.  **Internal/External Requests:** Handle requests from both floor panels and elevator cabin panels.
3.  **Real-Time Monitoring:** Track the floor, direction, and load of every elevator.
4.  **Emergency Handling:** Provide mechanisms for fire alarms or manual overrides.

### Technical Constraints

- **Directional Logic:** An elevator moving Up should prioritize all Up requests on floors above it before switching directions.
- **Load Balancing:** Avoid sending all elevators to the same floor for a single request.
- **Starvation Prevention:** Ensure that requests from lower-traffic floors are eventually served.

## 🧠 The Engineering Story

**The Villain:** "The Starvation." People on the 50th floor wait forever because the elevator keeps oscillating between floors 1 and 5 to serve a high volume of lobby requests.

**The Hero:** "The SCAN Algorithm." A strategy that ensures the elevator moves in one direction until it hits the furthest request, picking up everyone along the way.

**The Plot:**

1. Represent `Elevator` as a state machine (IDLE, UP, DOWN).
2. Use a `Dispatcher` to assign requests based on proximity and direction.
3. Manage a `RequestQueue` for internal and external button presses.

**The Twist (Failure):** **The Ping-Pong Effect.** If two elevators are both assigned to the same floor, they arrive empty while other floors remain unserved.

**Interview Signal:** Expertise in **State Machines** and **Optimization Algorithms** (LOOK/SCAN).

## 🚀 Thinking Process & Approach
Elevator scheduling is a classic optimization problem. The approach uses an event-driven system to handle floor requests and a strategy pattern to determine the most efficient moving direction to minimize wait time.

### Key Observations:

- State-based movement logic.
- Optimized scheduling algorithms.

## 🏗️ Design Patterns Used

- **State Pattern**: To manage the individual states of each elevator (IDLE, MOVING_UP, MOVING_DOWN, DOOR_OPEN).
- **Strategy Pattern**: For implementing different dispatching algorithms (SCAN, LOOK, Shortest Seek Time First).
- **Observer Pattern**: To notify the Dispatcher when a new floor request is made.
- **Singleton Pattern**: For the central Elevator Controller/Dispatcher.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/elevator/elevator_management_system.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Energy Optimization:** How would you modify the dispatcher to minimize energy consumption (e.g., minimizing elevator movement)?
- **VIP/Emergency Mode:** How would you implement a priority override for emergency services?
- **Load Sensing:** How do you handle the case where an elevator is full and should skip floor requests?

## 🔗 Related Challenges

- [Parking Lot](../parking_lot/PROBLEM.md) — For another resource management system.
- [Job Scheduler](../../distributed/job_scheduler/PROBLEM.md) — For distributing tasks (requests) across multiple workers (elevators).
