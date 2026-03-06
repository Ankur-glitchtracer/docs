# 🏠 Facade Pattern: One-Touch Smart Home

## 📝 Overview
The **Facade Pattern** provides a simplified interface to a complex set of classes, library, or framework. It hides the "messy" inner workings of a subsystem behind a single, easy-to-use "front" class.

!!! abstract "Core Concepts"
    - **Simplified API:** Reducing a 10-step process into a single method call.
    - **Subsystem Decoupling:** Shielding the client from the complexities and frequent changes within the underlying components.

## 🚀 Problem Statement
Setting up a "Movie Night" in a modern smart home is a chore. You have to turn on the projector, set the input, power up the sound system, adjust the volume, and dim the lights. Doing this manually via separate remote calls is tedious and error-prone.

## 🧠 Thinking Process & Approach
Interacting with a complex subsystem (e.g., Home Theater) requires calling multiple methods in order. The approach is to provide a single, higher-level interface that coordinates the subsystem components, simplifying life for the client.

### Key Observations:
- Unified entry point for complex subsystems.
- Subsystem isolation and decoupling.

### Technical Constraints
- **Coordination:** The Facade must ensure that subsystem actions happen in the correct logical sequence (e.g., dimming lights before starting the projector).
- **Dependency Injection:** The Facade should ideally receive subsystem instances rather than creating them, allowing for easier testing and swapping.

## 🛠️ Requirements
1. Subsystems: Complex classes.
2. Facade: Unified entry point.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/facade/smart_home_facade/smart_home_facade.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
