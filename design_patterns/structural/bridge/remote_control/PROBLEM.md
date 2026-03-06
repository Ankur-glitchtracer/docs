# 🌉 Bridge Pattern: Multi-Platform Remote Control

## 📝 Overview
The **Bridge Pattern** decouples an abstraction from its implementation so that the two can vary independently. It is the preferred alternative to inheritance when you face a "Cartesian Product" class explosion.

!!! abstract "Core Concepts"
    - **Composition over Inheritance:** Instead of being a `SonyTVRemote`, a `Remote` *has* a `Device`.
    - **Two Independent Hierarchies:** Separating the "Control Logic" (Remotes) from the "Hardware Logic" (TVs, Radios).

## 🚀 Problem Statement
You have `Shape` subclasses like `Circle` and `Square`. Adding colors like `Red` and `Blue` via inheritance leads to `RedCircle`, `BlueCircle`, `RedSquare`, `BlueSquare`, etc. Adding one new shape or color requires creating multiple new classes, leading to a "Class Explosion."

### Technical Constraints
- **Independence:** Adding a new `AdvancedRemoteControl` should not require any changes to the `TV` or `Radio` classes.
- **Extensibility:** You should be able to add a `SonyTV` or a `BoseRadio` (new implementations) without touching the `RemoteControl` logic.

## 🛠️ Requirements
1.  **Implementation Interface:** A `Device` interface with low-level controls like `enable()` and `set_volume()`.
2.  **Concrete Implementations:** Implement `TV` and `Radio` classes.
3.  **Abstraction:** A `RemoteControl` class that holds a reference to a `Device`.
4.  **Refined Abstraction:** An `AdvancedRemoteControl` that adds features like `mute()` using existing `Device` methods.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/bridge/remote_control/remote_control.py"
```

!!! success "Why this works"
    It breaks the binding between abstraction and implementation at compile time, allowing them to be swapped or extended at runtime. This keeps the class hierarchy flat and manageable, even as the number of features and platforms grows.
