# 🦄 Singleton Pattern: Centralized Resource Manager

## 📝 Overview
The **Singleton Pattern** ensures that a class has only one instance and provides a global point of access to it. This is the gold standard for managing shared resources like database connections or global configuration settings.

!!! abstract "Core Concepts"
    - **Instance Control:** Overriding `__new__` or using a decorator to strictly manage object lifecycle.
    - **Global State:** Providing a single, predictable source of truth for the entire application.

## 🚀 Problem Statement
Certain components in an application, such as a database connection pool or a logger, must have exactly one instance. Creating multiple instances can lead to resource exhaustion, inconsistent state, or conflicting file access.

### Technical Constraints
- **Identity Guarantee:** Multiple calls to the constructor must return the exact same memory address.
- **Thread Safety:** In a concurrent environment, the instance must be created safely without race conditions.

## 🛠️ Requirements
1.  **Singleton Class:** Implement a `DatabaseConnection` class.
2.  **Identity Check:** Use the `id()` function to verify that all variables point to the same instance.
3.  **Lifecycle Management:** Use Python's `__new__` method to intercept object creation.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/singleton/singleton_pattern/singleton_pattern.py"
```

!!! success "Why this works"
    It provides a controlled access point to a shared resource. By restricting instantiation, you prevent "split-brain" scenarios where different parts of the app are talking to different instances of what should be a singular global service.
