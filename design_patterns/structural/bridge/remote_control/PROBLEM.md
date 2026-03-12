# 🌉 Bridge Pattern: Multi-Platform Remote Control

## 📝 Overview
The **Bridge Pattern** decouples an abstraction from its implementation so that the two can vary independently. It is the preferred alternative to inheritance when you face a "Cartesian Product" class explosion.

!!! abstract "Core Concepts"

    - **Composition over Inheritance:** Instead of being a `SonyTVRemote`, a `Remote` *has* a `Device`.
        - **Two Independent Hierarchies:** Separating the "Control Logic" (Remotes) from the "Hardware Logic" (TVs, Radios).

!!! info "Why Use This Pattern?"

    - **Decouples an abstraction from its implementation**
    - **Allows both hierarchies to vary independently**
    - **Reduces the number of classes in complex systems**


## 🚀 Problem Statement
You have `Shape` subclasses like `Circle` and `Square`. Adding colors like `Red` and `Blue` via inheritance leads to `RedCircle`, `BlueCircle`, `RedSquare`, `BlueSquare`, etc. Adding one new shape or color requires creating multiple new classes, leading to a "Class Explosion."

## 🛠️ Requirements

1. Abstraction: High-level commands.
2. Implementor: Low-level interface.
3. Concrete Implementors: TV, Radio.

### Technical Constraints

- **Independence:** Adding a new `AdvancedRemoteControl` should not require any changes to the `TV` or `Radio` classes.
- **Extensibility:** You should be able to add a `SonyTV` or a `BoseRadio` (new implementations) without touching the `RemoteControl` logic.

## 🧠 Thinking Process & Approach
When we have two independent dimensions of growth (e.g., Remotes and Devices), inheritance fails. The approach is to bridge them via composition, so a Remote *has* a Device, allowing both to evolve without a class explosion.

### Key Observations:

- Prefer composition over inheritance.
- Independent scaling of hierarchies.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/bridge/remote_control/remote_control.py"
```

!!! success "Why this works"
    By separating the abstraction from its implementation, both can be extended independently. This avoids the exponential growth of classes that occurs with pure inheritance.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Adapter](../../adapter/format_translator/PROBLEM.md) — Adapter makes things work after they're designed; Bridge makes them work before they are.
