# 🚗 Real-World Challenge: Ride-Sharing Backend (Uber Lite)

## 📝 Overview
A **Ride-Sharing Service** is a complex system that matches demand (riders) with supply (drivers) in real-time. This challenge focuses on the orchestration of location tracking, matching algorithms, and dynamic pricing strategies within a highly concurrent environment.

!!! info "Why This Challenge?"

    - **Real-Time Orchestration:** Learning how to manage highly dynamic state (driver locations, ride requests) in a concurrent environment.
    - **Spatial Matching Logic:** Understanding how to efficiently connect users with nearby resources using strategy patterns.
    - **Dynamic Pricing Systems:** Implementing complex business rules (Surge Pricing) that respond to real-time supply and demand.

!!! abstract "Core Concepts"

    - **Real-Time Matching:** Connecting users with the closest available drivers using spatial indexing.
    - **Dynamic Pricing:** Adjusting fares based on supply/demand ratios (Surge Pricing).
    - **Event-Driven Architecture:** Using the Observer pattern to notify drivers of nearby requests.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **Observer Pattern:** Drivers listen for `RideRequest` events based on their location.
2.  **Strategy Pattern:** Implement various `PricingStrategy` (Standard, Surge, Discount).
3.  **Composite Pattern:** Represent the city as a hierarchy of zones and sub-zones.
4.  **State Management:** Manage the transition of ride states from `Requested` to `Completed`.

### Technical Constraints

- **Atomicity:** Driver assignment must be atomic to prevent over-subscription.
- **Fairness:** The matching algorithm should be fair to both riders (proximity) and drivers (idle time).
- **Thread Safety:** Ensure all global state updates (e.g., `RideManager`) are synchronized.

## 🧠 The Engineering Story

**The Villain:** "The Double-Assigned Driver." Two riders in the same area request a ride at the same time. Without atomic checks, the same driver is assigned to both, leaving one rider stranded and the driver confused.

**The Hero:** "The Distributed Lock & Spatial Index." Using Geo-hashing to quickly find nearby drivers and a transactional lock to ensure a driver is only assigned to one ride at a time.

**The Plot:**

1. Maintain a `DriverPool` with real-time location and status (AVAILABLE, BUSY).
2. Use a `Strategy` pattern to match riders with the nearest available driver.
3. Calculate fares dynamically using a `PricingStrategy` (Surge vs. Standard).
4. Use the **Observer Pattern** to notify drivers of nearby ride requests.

**The Twist (Failure):** **The Race Condition.** If a driver accepts a ride but their status isn't updated in the shared store instantly, they might still appear "Available" for another incoming request.

**Interview Signal:** Mastery of **Real-Time Systems**, **Spatial Matching**, and **Concurrency Control**.

## 🚀 Thinking Process & Approach
Matching riders and drivers in real-time requires low-latency location tracking and consistent state management. The approach uses spatial indexing for discovery and a state-machine to manage the ride lifecycle from request to completion.

### Key Observations:

- Real-time location updates for a dynamic driver pool.
- Transactional integrity during the driver assignment process.

## 🏗️ Design Patterns Used

- **Strategy Pattern**: To implement different driver matching algorithms and dynamic pricing strategies.
- **Observer Pattern**: To broadcast ride requests to all available drivers within a certain radius.
- **State Pattern**: To manage the various stages of a ride (REQUESTED -> ASSIGNED -> IN_PROGRESS -> COMPLETED).
- **Singleton Pattern**: For the central Ride Manager that coordinates the matching process.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/real_world_systems/ride_sharing_service/ride_sharing_service.py"
```

!!! success "Why this works"
    Combining specialized patterns like Strategy and Observer allows the system to remain flexible (new pricing rules) and responsive (real-time notifications) while maintaining a clean, decoupled architecture.

## 🎤 Interview Follow-ups

- **Spatial Indexing:** How would you scale the driver search to millions of drivers across a whole country? (Geo-hashing, Quad-trees)
- **Payment Integration:** How would you integrate a payment gateway to charge riders after a trip is completed?
- **Driver Incentives:** How would you modify the matching algorithm to prioritize drivers who have been waiting the longest?

## 🔗 Related Challenges

- [E-Commerce Order System](../e_commerce_order_system/PROBLEM.md) — For another complex state-driven workflow.
- [Parking Lot](../../systems/parking_lot/PROBLEM.md) — For managing a pool of resources (parking spots) similar to a driver pool.
