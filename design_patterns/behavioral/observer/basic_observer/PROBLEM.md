# 👀 Observer Pattern: Core Subscription Mechanics

## 📝 Overview
The **Observer Pattern** is the fundamental building block for reactive programming. It allows a "Subject" to maintain a list of interested "Observers" and notify them whenever an interesting event occurs.

!!! abstract "Core Concepts"
    - **Subject Registry:** A simple mechanism to `attach()` and `detach()` listeners.
    - **Broadcast Mechanism:** Iterating through the registry to call a notification method on each listener.

## 🚀 Problem Statement
Implement a minimal version of the observer pattern to demonstrate the core mechanics of registration and notification. The goal is to show how a change in a `Subject` can trigger actions in multiple `Observers` without direct coupling.

### Technical Constraints
- **Simplicity:** Focus on the "bare-bones" structure: a list of listeners and a `notify()` loop.
- **Reliability:** Ensure that removing an observer during a notification loop doesn't crash the system.

## 🛠️ Requirements
1.  **Simple Subject:** A class that manages a collection of observer objects.
2.  **Simple Observer:** An interface with a basic `update()` method.
3.  **Notification Test:** Demonstrate one subject triggering updates across multiple observer instances.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/observer/basic_observer/basic_observer.py"
```

!!! success "Why this works"
    It establishes a clean communication channel. The Subject remains focused on its state, while the Observers focus on their reaction, fulfilling the Single Responsibility Principle and enabling highly flexible system architectures.
