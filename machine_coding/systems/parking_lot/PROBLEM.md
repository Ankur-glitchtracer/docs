# 🅿️ Machine Coding: High-Concurrency Parking Lot

## 📝 Overview
Design and implement a **Multi-Floor Parking Lot** system. This challenge focuses on resource allocation, specialized spot management, and thread-safe operations in a high-traffic environment.

!!! info "Why This Challenge?"

    - **Resource Allocation Mastery:** Learning how to efficiently match different resources (parking spots) with varied requests (vehicle types).
    - **Concurrency & Synchronization:** Mastering the use of locks and thread-safe collections to prevent double-booking in multi-gate systems.
    - **Clean Domain Modeling:** Understanding how to represent a physical system (Floors, Spots, Vehicles, Tickets) with a clean object-oriented hierarchy.

!!! abstract "Core Concepts"

    - **Resource Partitioning:** Categorizing spots by vehicle type (Bike, Car, Truck) and proximity.
    - **Concurrency Control:** Ensuring that multiple entry gates don't "double-book" the same parking spot.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Multiple Floors & Spots:** Manage a hierarchy of levels and specialized parking spaces.
2.  **Vehicle Support:** Handle various vehicle types (Motorcycles, Cars, Buses) with matching spots.
3.  **Ticket Issuance:** Generate unique tickets on entry with timestamps and spot details.
4.  **Fee Calculation:** Implement configurable pricing models based on duration and vehicle type.

### Technical Constraints

- **Thread Safety:** Multiple vehicles entering via different gates simultaneously must be handled without race conditions.
- **Efficiency:** Finding the "nearest" available spot should be optimized to minimize entry time.
- **Persistence:** (Optional) Support saving and restoring the parking lot state.

## 🧠 The Engineering Story

**The Villain:** "The Double-Booker." Two cars enter from different gates at the exact same millisecond. Without synchronization, both are assigned "Spot #42," leading to a literal gridlock at the space.

**The Hero:** "The Thread-Safe Allocator." A central manager using locks or concurrent queues to ensure every spot is granted to exactly one vehicle.

**The Plot:**

1. Model the `ParkingLot` with multiple `Floors`.
2. Categorize `Spots` (Small, Medium, Large) to match vehicle types.
3. Use a `Strategy` to find the "nearest" available spot.
4. Issue a `Ticket` on entry and calculate `Fees` on exit.

**The Twist (Failure):** **The Deadlock.** If the entry and exit gates both try to lock the entire `Floor` object at the same time, the system freezes during peak hours.

**Interview Signal:** Mastery of **Concurrency (Thread Safety)** and **Clean Object-Oriented Modeling**.

## 🚀 Thinking Process & Approach
The core of a parking lot is resource allocation. The approach uses a list of spots and a matching algorithm to find the nearest available one. Concurrency control is vital to ensure multiple entry gates don't double-book a spot.

### Key Observations:

- Efficient resource matching.
- Thread-safe allocation logic.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: To implement different spot-finding algorithms (e.g., nearest-to-elevator, lowest-floor-first) and fee calculation models.
- **Singleton Pattern**: To ensure a single `ParkingLot` manager handles all entry/exit gates.
- **Factory Pattern**: To create different vehicle objects (Car, Bike, Truck) and their corresponding spot types.
- **Command Pattern**: To encapsulate entry and exit operations as transactional commands.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/parking_lot/parking_lot.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Valet Parking:** How would you modify the system to handle valet services where the spot is assigned after the vehicle enters?
- **Dynamic Pricing:** How would you implement surge pricing for the parking lot during high-demand events?
- **Handicapped/EV Spots:** How would you add specialized spots with different priority rules?

## 🔗 Related Challenges

- [Multi-Elevator Dispatcher](../elevator/PROBLEM.md) — For another resource allocation and scheduling problem.
- [High-Performance Cache](../cache_system/PROBLEM.md) — For managing a fixed-capacity resource pool with eviction/release logic.
