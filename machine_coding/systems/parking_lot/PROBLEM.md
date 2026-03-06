# 🅿️ Machine Coding: High-Concurrency Parking Lot

## 📝 Overview
Design and implement a **Multi-Floor Parking Lot** system. This challenge focuses on resource allocation, specialized spot management, and thread-safe operations in a high-traffic environment.

!!! abstract "Core Concepts"
    - **Resource Partitioning:** Categorizing spots by vehicle type (Bike, Car, Truck) and proximity.
    - **Concurrency Control:** Ensuring that multiple entry gates don't "double-book" the same parking spot.

## 🚀 Problem Statement
Build a system that manages a parking lot with multiple floors and gates. It must automatically assign the closest available spot to an incoming vehicle based on its type and then calculate fees upon exit.

## 🧠 Thinking Process & Approach
The core of a parking lot is resource allocation. The approach uses a list of spots and a matching algorithm to find the nearest available one. Concurrency control is vital to ensure multiple entry gates don't double-book a spot.

### Key Observations:
- Efficient resource matching.
- Thread-safe allocation logic.

### Technical Constraints
- **Thread Safety:** Multiple vehicles entering via different gates simultaneously must be handled without race conditions.
- **Pricing Rules:** Support configurable rates based on time spent and vehicle category.

