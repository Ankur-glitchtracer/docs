# 🏠 Facade Pattern: One-Touch Smart Home

## 📝 Overview
The **Facade Pattern** provides a simplified interface to a complex set of classes, library, or framework. It hides the "messy" inner workings of a subsystem behind a single, easy-to-use "front" class.

!!! abstract "Core Concepts"
    - **Simplified API:** Reducing a 10-step process into a single method call.
    - **Subsystem Decoupling:** Shielding the client from the complexities and frequent changes within the underlying components.

## 🚀 Problem Statement
Setting up a "Movie Night" in a modern smart home is a chore. You have to turn on the projector, set the input, power up the sound system, adjust the volume, and dim the lights. Doing this manually via separate remote calls is tedious and error-prone.

### Technical Constraints
- **Coordination:** The Facade must ensure that subsystem actions happen in the correct logical sequence (e.g., dimming lights before starting the projector).
- **Dependency Injection:** The Facade should ideally receive subsystem instances rather than creating them, allowing for easier testing and swapping.

## 🛠️ Requirements
1.  **Complex Subsystems:** Create `Projector`, `SoundSystem`, and `SmartLights` with unique control methods.
2.  **Facade Class:** Implement `SmartHomeFacade` to coordinate these subsystems.
3.  **Unified Methods:** Provide high-level actions like `watch_movie()` and `end_movie()`.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/facade/smart_home_facade/smart_home_facade.py"
```

!!! success "Why this works"
    It dramatically improves developer and user experience. By wrapping complex interactions into a Facade, you create a "high-level" language for your system, making the client code much cleaner and easier to maintain.
