# 💧 Strategy Pattern: Dynamic Sprinkler Scheduler

## 📝 Overview
The **Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. This allows the system to switch between different behaviors (like watering schedules) without modifying the main context.

!!! abstract "Core Concepts"
    - **Interchangeable Algorithms:** Switch between different logic sets (e.g., Weekday vs. Weekend) seamlessly.
    - **Behavioral Decoupling:** The `Sprinkler` doesn't need to know the details of the watering schedule it's running.

## 🚀 Problem Statement
You are building a smart sprinkler system that needs to support different watering schedules based on the day of the week or local water restrictions. Hardcoding these rules into the main controller would make it difficult to add new schedules or change existing ones.

### Technical Constraints
- **Runtime Flexibility:** The system must be able to change its active schedule without restarting or re-instantiating the `Sprinkler`.
- **Standardized Interface:** All schedules must follow a common `get_watering_duration()` contract.

## 🛠️ Requirements
1.  **Strategy Interface:** Create a common `WateringSchedule` interface.
2.  **Concrete Strategies:** Implement `WeekdaySchedule` and `WeekendSchedule`.
3.  **Context Class:** Implement the `Sprinkler` that uses the current strategy to execute watering.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/strategy/sprinkler_system/sprinkler_system.py"
```

!!! success "Why this works"
    It adheres to the Open/Closed Principle. To add a "Drought Mode" or "Heavy Rain" schedule, you simply create a new strategy class without touching the core `Sprinkler` logic, making the system highly extensible.
