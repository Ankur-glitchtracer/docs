# 🕹️ Command Pattern: Programmable Smart Home Hub

## 📝 Overview
The **Command Pattern** encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations. This implementation focuses on a **Universal Smart Home Remote** that must control diverse devices (Lights, TVs, Thermostats) with a uniform interface.

!!! abstract "Core Concepts"
    - **Uniform Interface:** Slots for buttons that can be assigned any device action.
    - **Undo Functionality:** A single button to reverse the last executed command.
    - **Macro Commands:** "Party Mode" to execute a sequence of commands in one click.

## 🚀 Problem Statement
You are building a backend for a programmable remote. The remote should not know the internal mechanics of each device (e.g., whether a light uses `on()` or a stereo uses `setVolume()`). Instead, it should interact solely with `Command` objects.

## 🧠 Thinking Process & Approach
Triggering actions directly couples the invoker to the receiver. The approach is to wrap every request in a Command object. This allows us to queue, log, and undo operations simply by managing a list of these objects.

### Key Observations:
- Encapsulation of requests as objects.
- Support for Undo/Redo through command stacks.

### Technical Constraints
- **Receivers (Devices):** Implement `Light`, `Stereo`, and `TV` with unique method names to simulate heterogeneous hardware.
- **Invoker (Remote):** Must hold 4 programmable slots and a reference to the last command for undoing.
- **Decoupling:** Adding a new device should require a new `Command` class, not modifications to the `Remote` class.

## 🛠️ Requirements
1. Command Interface (execute/undo).
2. Concrete Commands.
3. Receiver objects.
4. Invoker triggers.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/command/smart_home_hub/smart_home_hub.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
