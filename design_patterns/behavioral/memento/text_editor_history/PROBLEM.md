# ⏪ Memento Pattern: Pro-Pixel Undo History

## 📝 Overview
The **Memento Pattern** is the "Ctrl+Z" of software design. It allows an object (the Originator) to produce a snapshot of its state (the Memento) which can be stored by a manager (the Caretaker) and used later for restoration.

!!! abstract "Core Concepts"

    - **Encapsulation Shield:** The internal state of the editor (cursor, selection) remains private.
        - **Caretaker Role:** A `History` class that manages a stack of snapshots without interfering with their data.

!!! info "Why Use This Pattern?"

    - **Captures and restores an object's internal state**
    - **Does not violate encapsulation**
    - **Simplifies undo/redo functionality**


## 🚀 Problem Statement
You are building a professional text editor where users frequently need to undo mistakes. The editor has multiple private fields: `content`, `cursor_position`, and `selection_range`. You need a way to save these fields without allowing other classes to touch the editor's private state directly.

## 🛠️ Requirements

1. Originator: Snapshot creator.
2. Memento: Immutable state store.
3. Caretaker: History manager.

### Technical Constraints

- **Memory Management:** Snapshots should only be triggered on significant actions (e.g., after a word or a line) to avoid exhausting memory.
- **Identity:** The `History` should treat mementos as opaque objects.

## 🧠 Thinking Process & Approach
Implementing Undo requires saving state without exposing private data. The approach uses an opaque Memento object that stores a snapshot. The Editor (Originator) creates it, and the History (Caretaker) manages the stack, ensuring 'time-travel' is possible.

### Key Observations:

- Encapsulation preservation (Caretaker can't read Memento).
- Deep copying state to prevent side effects.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/memento/text_editor_history/text_editor_history.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Command](../../command/smart_home_hub/PROBLEM.md) — Memento can keep the state required for undoing a Command.
- [Iterator](../../iterator/menu_iterator/PROBLEM.md) — Mementos can be used to store the state of an iteration.
