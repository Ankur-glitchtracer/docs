# 🦄 Singleton Pattern: Centralized Resource Manager

## 📝 Overview
The **Singleton Pattern** ensures that a class has only one instance and provides a global point of access to it. This is the gold standard for managing shared resources like database connections or global configuration settings.

!!! abstract "Core Concepts"
    - **Instance Control:** Overriding `__new__` or using a decorator to strictly manage object lifecycle.
    - **Global State:** Providing a single, predictable source of truth for the entire application.

## 🚀 Problem Statement
Certain components in an application, such as a database connection pool or a logger, must have exactly one instance. Creating multiple instances can lead to resource exhaustion, inconsistent state, or conflicting file access.

## 🧠 Thinking Process & Approach
The core challenge is ensuring a single instance across the entire application. In Python, the `__new__` method is the constructor that creates the instance, making it the perfect place to intercept and return an existing one. To handle concurrency, a thread lock ensures that two threads don't create separate instances at the same time.

### Key Observations:
- Use `__new__` for instance control.
- Double-checked locking for thread safety.

### Technical Constraints
- **Identity Guarantee:** Multiple calls to the constructor must return the exact same memory address.
- **Thread Safety:** In a concurrent environment, the instance must be created safely without race conditions.

## 🛠️ Requirements
1. Unique Instance: The class must guarantee that only one instance is created.
2. Global Access: Provide a static method or property to retrieve the instance.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/singleton/singleton_pattern/singleton_pattern.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
