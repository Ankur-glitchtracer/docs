# 💾 Memento Pattern: Advanced Undo/Redo System

## 📝 Overview
The **Memento Pattern** captures and externalizes an object's internal state without violating encapsulation, so that the object can be restored to this state later. This is the foundation of modern "Undo/Redo" functionality.

!!! abstract "Core Concepts"
    - **Opaque Snapshots:** The `Memento` object is a "black box" that only the `Originator` can read.
    - **History Management:** The `Caretaker` maintains a stack of snapshots without knowing their contents.

## 🚀 Problem Statement
You need to expand a basic text editor to handle complex state saving, including text content, cursor position, and formatting styles. The challenge is implementing an Undo/Redo stack that doesn't expose the editor's private fields to the history manager.

### Technical Constraints
- **Immutability:** Once a `Memento` is created, its state must never change.
- **Deep Copying:** Ensure that saving a state captures the actual values, not just references that might change later.

## 🛠️ Requirements
1.  **Complex Originator:** A `TextEditor` with multiple attributes (text, cursor, formatting).
2.  **Undo/Redo Stack:** Implement a `History` class that supports moving both backwards and forwards.
3.  **State Capture:** Methods to `save()` and `restore()` from `Memento` objects.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/memento/advanced_text_editor/advanced_text_editor.py"
```

!!! success "Why this works"
    It preserves encapsulation. The `History` object (Caretaker) manages the snapshots but never "looks inside" them. Only the `TextEditor` knows how to translate a `Memento` back into an active state, keeping the internal logic secure and clean.
