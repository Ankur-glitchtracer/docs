# 🕵️ Proxy Pattern: Smart Lazy-Loading Video Player

## 📝 Overview
The **Proxy Pattern** provides a surrogate or placeholder for another object to control access to it. It is commonly used to delay the creation of "expensive" objects until they are absolutely necessary, a technique known as lazy loading.

!!! abstract "Core Concepts"
    - **Access Control:** The proxy acts as a gatekeeper, intercepting calls to the real object.
    - **Lifecycle Management:** The real object is instantiated only when its first method is invoked.

## 🚀 Problem Statement
Loading high-resolution video files from disk is a heavy operation that consumes significant CPU and memory. If a user has a library of 100 videos, creating all 100 `Video` objects at startup will crash the app, even if they only watch one.

### Technical Constraints
- **Transparency:** The `ProxyVideo` must implement the exact same interface as the `RealVideo` so the client can't tell the difference.
- **Deferred Instantiation:** The "Loading..." message must only appear when `display()` is actually called, not when the object is created.

## 🛠️ Requirements
1.  **Subject Interface:** A `Video` interface with a `display()` method.
2.  **Real Subject:** `RealVideo` which simulates a heavy disk load in its constructor.
3.  **Proxy Subject:** `ProxyVideo` which holds a `None` reference to `RealVideo` until needed.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/proxy/lazy_loading_proxy/lazy_loading_proxy.py"
```

!!! success "Why this works"
    It optimizes resource usage by ensuring that heavy objects are only "paid for" when they are used. It also allows for additional logic, such as caching, logging, or security checks, to be added without modifying the original class.
