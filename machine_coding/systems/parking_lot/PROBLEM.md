# 🅿️ Machine Coding: High-Concurrency Parking Lot

## 📝 Overview
Design and implement a **Multi-Floor Parking Lot** system. This challenge focuses on resource allocation, specialized spot management, and thread-safe operations in a high-traffic environment.

!!! abstract "Core Concepts"
    - **Resource Partitioning:** Categorizing spots by vehicle type (Bike, Car, Truck) and proximity.
    - **Concurrency Control:** Ensuring that multiple entry gates don't "double-book" the same parking spot.

## 🚀 Problem Statement
Build a system that manages a parking lot with multiple floors and gates. It must automatically assign the closest available spot to an incoming vehicle based on its type and then calculate fees upon exit.

### Technical Constraints
- **Thread Safety:** Multiple vehicles entering via different gates simultaneously must be handled without race conditions.
- **Pricing Rules:** Support configurable rates based on time spent and vehicle category.

## 🛠️ Requirements
1.  **Spot Assignment:** Find the nearest spot for `Car`, `Bike`, or `Truck`.
2.  **Multi-Gate Support:** Handle concurrent entry and exit operations.
3.  **Pricing Engine:** Calculate fees dynamically based on duration.
4.  **Live Monitoring:** Provide real-time occupancy counts for each floor and vehicle type.

!!! success "Why this works"
    The system uses a centralized `ParkingManager` to coordinate between floors, while each `Floor` manages its own spots. This hierarchical design, combined with robust locking, ensures that spot allocation is both fast and accurate, even under heavy load.

## Solution Implementation

```python
--8<-- "machine_coding/systems/parking_lot/parking_lot.py"
```
