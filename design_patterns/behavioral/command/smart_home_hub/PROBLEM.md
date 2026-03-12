# 🕹️ Command Pattern: Programmable Smart Home Hub

## 📝 Overview
The **Command Pattern** encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations. This implementation focuses on a **Universal Smart Home Remote** that must control diverse devices (Lights, TVs, Thermostats) with a uniform interface.

!!! abstract "Core Concepts"

    - **Uniform Interface:** Slots for buttons that can be assigned any device action.
        - **Undo Functionality:** A single button to reverse the last executed command.
        - **Macro Commands:** "Party Mode" to execute a sequence of commands in one click.

!!! info "Why Use This Pattern?"

    - **Encapsulates a request as an object**
    - **Supports undo/redo and logging**
    - **Decouples the invoker from the receiver**


## 🚀 Problem Statement
You are building a backend for a programmable remote. The remote should not know the internal mechanics of each device (e.g., whether a light uses `on()` or a stereo uses `setVolume()`). Instead, it should interact solely with `Command` objects.

## 🛠️ Requirements

1. **Command Interface:** Define standard `execute()` and `undo()` methods.
2. **Concrete Commands:** Implement commands for various device actions.
3. **Receiver Objects:** Implement `Light`, `Stereo`, and `TV`.
4. **Invoker:** A `RemoteControl` with programmable slots.

### Technical Constraints

- **Receivers (Devices):** Implement `Light`, `Stereo`, and `TV` with unique method names to simulate heterogeneous hardware.
- **Invoker (Remote):** Must hold 4 programmable slots and a reference to the last command for undoing.
- **Decoupling:** Adding a new device should require a new `Command` class, not modifications to the `Remote` class.

## 🧠 Thinking Process & Approach
**The Villain:** "Hardwired Requests." A UI button directly calls business logic. You can't undo, queue, or log the action.

**The Hero:** "The Request Object." Encapsulates a request as an object.

**The Plot:**

1. Turn a method call (`light.turnOn()`) into an object (`TurnOnCommand(light)`).
2. The Invoker (Button) just calls `execute()`.
3. You can now store these objects in a list for **Undo/Redo**.

**The Twist (Failure):** **Loss of History**. You cannot replay actions to recover from a crash or audit user activity.

**Interview Signal:** Key for implementing **Undo/Redo**, **Command Queuing**, and **Replay Systems**.

Triggering actions directly couples the invoker to the receiver. The approach is to wrap every request in a Command object. This allows us to queue, log, and undo operations simply by managing a list of these objects.

### Key Observations:

- Encapsulation of requests as objects.
- Support for Undo/Redo through command stacks.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/command/smart_home_hub/smart_home_hub.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Memento](../../memento/text_editor_history/PROBLEM.md) — Memento can keep the state required for undoing a Command.
- [Prototype](../../../creational/prototype/PROBLEM.md) — Prototype can be used to clone Commands before putting them on a history list.
- [Observer](../../observer/basic_observer/PROBLEM.md) — Command can be used as an action triggered by an Observer.
