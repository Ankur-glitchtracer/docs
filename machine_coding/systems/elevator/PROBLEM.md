# 🛗 Machine Coding: Multi-Elevator Dispatcher

## 📝 Overview
Design an **Elevator Management System** for a high-rise building. This challenge involves complex state management, real-time request handling, and optimization algorithms to minimize passenger wait times.

!!! abstract "Core Concepts"
    - **Request Scheduling:** Efficiently assigning `N` elevators to handle `M` floor requests.
    - **State Control:** Managing the direction (Up, Down, Idle) and current floor for multiple independent units.

## 🚀 Problem Statement
You need to coordinate multiple elevators across many floors. The system must handle both "External" requests (someone on a floor wanting to go up/down) and "Internal" requests (a passenger inside selecting a destination).

## 🧠 Thinking Process & Approach
Elevator scheduling is a classic optimization problem. The approach uses an event-driven system to handle floor requests and a strategy pattern to determine the most efficient moving direction to minimize wait time.

### Key Observations:
- State-based movement logic.
- Optimized scheduling algorithms.

### Technical Constraints
- **Directional Logic:** An elevator moving Up should prioritize all Up requests on floors above it before switching directions.
- **Load Balancing:** Avoid sending all elevators to the same floor for a single request.

