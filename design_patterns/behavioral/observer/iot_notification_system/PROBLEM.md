# 🔔 Observer Pattern: Smart IoT Event Bus

## 📝 Overview
The **Observer Pattern** defines a one-to-many dependency between objects. When one object (the Subject) changes state, all its dependents (Observers) are notified and updated automatically, making it ideal for event-driven systems.

!!! abstract "Core Concepts"
    - **Pub-Sub Decoupling:** The `Subject` doesn't need to know who is listening; it just broadcasts updates.
    - **Dynamic Subscription:** Observers can be added or removed at runtime without affecting the `Subject`.

## 🚀 Problem Statement
In a smart home system, multiple devices (Sirens, Phone Apps, Smart Lights) need to respond instantly to a security sensor (Motion Detector). Hardcoding each device's alert logic into the sensor would create a maintenance nightmare.

### Technical Constraints
- **Asynchronous Notification:** The notification process should ideally not block the `Subject`'s core loop.
- **Interface Uniformity:** All alert devices must implement a standard `update()` or `notify()` method.

## 🛠️ Requirements
1.  **Subject/EventBus:** A class to manage the list of subscribers and trigger notifications.
2.  **Observer Interface:** Define standard methods for different alert levels (e.g., `alert()`, `critical()`).
3.  **Concrete Observers:** Implement `Siren`, `PhoneApp`, and `SmartLight` responders.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/observer/iot_notification_system/iot_notification_system.py"
```

!!! success "Why this works"
    It promotes loose coupling between the event source and the event consumers. You can add a new "Security Company Notification" service by simply creating a new observer class and subscribing it to the bus, without ever touching the sensor code.
