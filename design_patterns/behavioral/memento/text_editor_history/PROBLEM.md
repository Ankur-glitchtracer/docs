# ⏪ Memento Pattern: Pro-Pixel Undo History

## 📝 Overview
The **Memento Pattern** is the "Ctrl+Z" of software design. It allows an object (the Originator) to produce a snapshot of its state (the Memento) which can be stored by a manager (the Caretaker) and used later for restoration.

!!! abstract "Core Concepts"
    - **Encapsulation Shield:** The internal state of the editor (cursor, selection) remains private.
    - **Caretaker Role:** A `History` class that manages a stack of snapshots without interfering with their data.

## 🚀 Problem Statement
You are building a professional text editor where users frequently need to undo mistakes. The editor has multiple private fields: `content`, `cursor_position`, and `selection_range`. You need a way to save these fields without allowing other classes to touch the editor's private state directly.

### Technical Constraints
- **Memory Management:** Snapshots should only be triggered on significant actions (e.g., after a word or a line) to avoid exhausting memory.
- **Identity:** The `History` should treat mementos as opaque objects.

## 🛠️ Requirements
1.  **Originator:** The `TextEditor` class with private state and snapshot methods.
2.  **Memento:** An immutable object storing `content`, `cursor`, and `selection`.
3.  **Caretaker:** A `History` class that pushes and pops mementos from a stack.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/memento/text_editor_history/text_editor_history.py"
```

!!! success "Why this works"
    It provides a clean "time-travel" mechanism for objects. By isolating the state-saving logic into a Memento, you ensure that the Originator's internal details don't leak into the rest of the application, keeping the design robust and maintainable.
