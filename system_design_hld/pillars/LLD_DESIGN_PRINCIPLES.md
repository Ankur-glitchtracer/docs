# Low-Level Design (LLD): SOLID Principles & Python Protocols

While High-Level Design (HLD) dictates the overarching architecture of a distributed system, Low-Level Design (LLD) or "Machine Coding" focuses on the internal extensibility, maintainability, and type safety of the micro-components themselves.

This document outlines how to bridge HLD concepts into production-grade Python code using SOLID principles and modern architectural patterns.

## 1. The Core Architectural Philosophy

To achieve maximum extensibility, a Principal Systems Architect must decouple the core business logic (e.g., controlling an elevator bank or a parking lot) from the algorithmic logic (e.g., finding the nearest spot, picking the fastest elevator).

### Dependency Inversion Principle (DIP)

High-level modules must not depend on low-level modules. Instead, both must depend on abstractions.

In modern Python, this is achieved using `typing.Protocol` to define strict, type-safe interfaces (often referred to as "Duck Typing" with static verification).

## 2. Architecting with Python Protocols

Unlike traditional abstract base classes (`abc.ABC`), Protocols do not require explicit inheritance. If a class implements the required methods, it implicitly satisfies the Protocol. This ensures that any new strategy passed into your systems guarantees the correct API signature at lint/compile time, preventing runtime crashes.

### Example: The Strategy Pattern

Consider an Elevator system. The `ElevatorController` should not care how an elevator is selected; it just needs to know that the provided algorithm will return the best elevator.

```python
from typing import Protocol

# 1. Define the Strict Abstraction
class ElevatorDispatchStrategy(Protocol):
    def select_elevator(self, request: ElevatorRequest, elevators: list[Elevator]) -> Elevator:
        """Must return the most optimal elevator for the given request."""
        ...

# 2. Implement Low-Level Algorithmic Modules
class ShortestSeekTimeStrategy:
    def select_elevator(self, request: ElevatorRequest, elevators: list[Elevator]) -> Elevator:
        # Complex logic to calculate closest elevator...
        return best_elevator

class EnergySaverStrategy:
    def select_elevator(self, request: ElevatorRequest, elevators: list[Elevator]) -> Elevator:
        # Logic prioritizing idle elevators to save power...
        return best_elevator
```

### Strategy Swapping (Open-Closed Principle)

By adhering to the **Open-Closed Principle (OCP)**—software entities should be open for extension, but closed for modification—the core state machine becomes incredibly robust.

If the business requires a new dispatch algorithm, you do not modify the `ElevatorController`. You simply write a new Strategy class and pass it in.

```python
class ElevatorController:
    def __init__(self, elevators: list[Elevator], dispatch_strategy: ElevatorDispatchStrategy):
        self.elevators = elevators
        self._dispatch_strategy = dispatch_strategy

    # Dynamic Strategy Swapping at Runtime
    def set_dispatch_strategy(self, new_strategy: ElevatorDispatchStrategy):
        self._dispatch_strategy = new_strategy

    def handle_request(self, request: ElevatorRequest):
        # DIP in action: Controller relies entirely on the abstract protocol
        best_elevator = self._dispatch_strategy.select_elevator(request, self.elevators)
        best_elevator.add_destination(request.floor)
```

## 4. Architectural Benefits

By enforcing **Protocols** and **Strategy Patterns** in your LLD:

- **Type Safety:** `mypy` and modern IDEs will instantly flag if a new strategy breaks the API contract.

- **Extensibility:** New features require new files, entirely eliminating the risk of breaking existing core logic.

- **Testability:** Because the high-level managers accept strategies via dependency injection, you can seamlessly pass in mock strategies to unit test your controllers in isolation.

## Practical Implementation

Explore the complete Python implementations of these extensible patterns in the repository:

- **Elevator System:** [Machine Coding: Elevator Controller](../../machine_coding/systems/elevator/elevator_management_system.py)  
- **Parking Lot System:** [Machine Coding: Parking Lot Allocation](../../machine_coding/systems/parking_lot/parking_lot.py)
