# 💧 Strategy Pattern: Dynamic Sprinkler Scheduler

## 📝 Overview
The **Strategy Pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. This allows the system to switch between different behaviors (like watering schedules) without modifying the main context.

!!! abstract "Core Concepts"
    - **Interchangeable Algorithms:** Switch between different logic sets (e.g., Weekday vs. Weekend) seamlessly.
    - **Behavioral Decoupling:** The `Sprinkler` doesn't need to know the details of the watering schedule it's running.

## 🚀 Problem Statement
You are building a smart sprinkler system that needs to support different watering schedules based on the day of the week or local water restrictions. Hardcoding these rules into the main controller would make it difficult to add new schedules or change existing ones.

## 🧠 Thinking Process & Approach
When we have interchangeable algorithms (like watering schedules), we avoid hardcoding them. The approach uses a Strategy interface that can be swapped at runtime, allowing the main system to behave differently based on the current context.

### Key Observations:
- Runtime algorithmic flexibility.
- Elimination of complex switch statements.

### Technical Constraints
- **Runtime Flexibility:** The system must be able to change its active schedule without restarting or re-instantiating the `Sprinkler`.
- **Standardized Interface:** All schedules must follow a common `get_watering_duration()` contract.

