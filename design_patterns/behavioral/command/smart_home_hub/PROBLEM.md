# 🕹️ Command Pattern: Programmable Smart Home Hub

## 📝 Overview
The **Command Pattern** encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations. This implementation focuses on a **Universal Smart Home Remote** that must control diverse devices (Lights, TVs, Thermostats) with a uniform interface.

!!! abstract "Core Concepts"
    - **Uniform Interface:** Slots for buttons that can be assigned any device action.
    - **Undo Functionality:** A single button to reverse the last executed command.
    - **Macro Commands:** "Party Mode" to execute a sequence of commands in one click.

## 🚀 Problem Statement
You are building a backend for a programmable remote. The remote should not know the internal mechanics of each device (e.g., whether a light uses `on()` or a stereo uses `setVolume()`). Instead, it should interact solely with `Command` objects.

### Technical Constraints
- **Receivers (Devices):** Implement `Light`, `Stereo`, and `TV` with unique method names to simulate heterogeneous hardware.
- **Invoker (Remote):** Must hold 4 programmable slots and a reference to the last command for undoing.
- **Decoupling:** Adding a new device should require a new `Command` class, not modifications to the `Remote` class.

## 🛠️ Requirements
1.  **Command Interface:** Define a standard `execute()` and `undo()` contract.
2.  **Concrete Commands:** Implement wrappers for specific actions (e.g., `LightOnCommand`, `GarageMuteCommand`).
3.  **Macro Command:** Implement a `PartyCommand` that holds a list of other commands.
4.  **Hardware Simulation:** Ensure the `Remote` (Invoker) triggers the `Receiver` (Hardware) via the command.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/command/smart_home_hub/smart_home_hub.py"
```

!!! success "Why this works"
    The `RemoteControl` remains closed for modification but open for extension. To support a new "Smart Blinds" device, you simply create a `BlindsOpenCommand` without touching the core Remote logic.
