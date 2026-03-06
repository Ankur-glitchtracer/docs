# 🔔 Observer Pattern: Smart IoT Event Bus

## 📝 Overview
The **Observer Pattern** defines a one-to-many dependency between objects. When one object (the Subject) changes state, all its dependents (Observers) are notified and updated automatically, making it ideal for event-driven systems.

!!! abstract "Core Concepts"
    - **Pub-Sub Decoupling:** The `Subject` doesn't need to know who is listening; it just broadcasts updates.
    - **Dynamic Subscription:** Observers can be added or removed at runtime without affecting the `Subject`.

## 🚀 Problem Statement
In a smart home system, multiple devices (Sirens, Phone Apps, Smart Lights) need to respond instantly to a security sensor (Motion Detector). Hardcoding each device's alert logic into the sensor would create a maintenance nightmare.

## 🧠 Thinking Process & Approach
Hardcoding notifications into a sensor makes it rigid. The approach uses an Event Bus or a Subject that maintains a dynamic list of subscribers. This allows any part of the system to 'react' to an event without the source ever knowing who they are.

### Key Observations:
- Loose coupling through event dispatching.
- Dynamic subscription management at runtime.

### Technical Constraints
- **Asynchronous Notification:** The notification process should ideally not block the `Subject`'s core loop.
- **Interface Uniformity:** All alert devices must implement a standard `update()` or `notify()` method.

