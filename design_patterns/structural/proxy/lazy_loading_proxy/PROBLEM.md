# 🕵️ Proxy Pattern: Smart Lazy-Loading Video Player

## 📝 Overview
The **Proxy Pattern** provides a surrogate or placeholder for another object to control access to it. It is commonly used to delay the creation of "expensive" objects until they are absolutely necessary, a technique known as lazy loading.

!!! abstract "Core Concepts"
    - **Access Control:** The proxy acts as a gatekeeper, intercepting calls to the real object.
    - **Lifecycle Management:** The real object is instantiated only when its first method is invoked.

## 🚀 Problem Statement
Loading high-resolution video files from disk is a heavy operation that consumes significant CPU and memory. If a user has a library of 100 videos, creating all 100 `Video` objects at startup will crash the app, even if they only watch one.

## 🧠 Thinking Process & Approach
Creating heavy objects (like video files) at startup wastes resources. The approach uses a lightweight Proxy that stands in for the real object. The heavy creation only happens at the moment of first use (Lazy Loading).

### Key Observations:
- On-demand resource allocation.
- Controlled access to the real subject.

### Technical Constraints
- **Transparency:** The `ProxyVideo` must implement the exact same interface as the `RealVideo` so the client can't tell the difference.
- **Deferred Instantiation:** The "Loading..." message must only appear when `display()` is actually called, not when the object is created.

## 🛠️ Requirements
1. Subject Interface.
2. Real Subject.
3. Proxy placeholder.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/proxy/lazy_loading_proxy/lazy_loading_proxy.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
