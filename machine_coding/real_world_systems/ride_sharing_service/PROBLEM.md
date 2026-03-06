# 🚗 Real-World Challenge: Ride-Sharing Backend (Uber Lite)

## 📝 Overview
A **Ride-Sharing Service** is a complex system that matches demand (riders) with supply (drivers) in real-time. This challenge focuses on the orchestration of location tracking, matching algorithms, and dynamic pricing strategies within a highly concurrent environment.

!!! abstract "Core Concepts"
    - **Real-Time Matching:** Connecting users with the closest available drivers using spatial indexing.
    - **Dynamic Pricing:** Adjusting fares based on supply/demand ratios (Surge Pricing).
    - **Event-Driven Architecture:** Using the Observer pattern to notify drivers of nearby requests.

## 🚀 Problem Statement
Design the core backend logic for a service like Uber or Lyft. The system must efficiently manage driver availability, handle ride requests from multiple users simultaneously, and ensure fair and transparent pricing.

### Technical Constraints
- **Concurrency:** Multiple drivers must not be assigned to the same rider, and vice versa.
- **Scalability:** The matching logic must remain efficient as the number of active users grows.
- **Thread Safety:** Use appropriate synchronization for global state management (e.g., `RideManager`).

## 🛠️ Requirements
1.  **Observer Pattern:** Drivers listen for `RideRequest` events based on their location.
2.  **Strategy Pattern:** Implement various `PricingStrategy` (Standard, Surge, Discount).
3.  **Composite Pattern:** Represent the city as a hierarchy of zones and sub-zones.
4.  **State Management:** Manage the transition of ride states from `Requested` to `Completed`.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/real_world_systems/ride_sharing_service/PROBLEM.md"
```

!!! success "Why this works"
    Combining specialized patterns like Strategy and Observer allows the system to remain flexible (new pricing rules) and responsive (real-time notifications) while maintaining a clean, decoupled architecture.
