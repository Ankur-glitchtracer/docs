# 💾 Memento Pattern: Advanced Undo/Redo System

## 📝 Overview
The **Memento Pattern** captures and externalizes an object's internal state without violating encapsulation, so that the object can be restored to this state later. This is the foundation of modern "Undo/Redo" functionality.

!!! abstract "Core Concepts"
    - **Opaque Snapshots:** The `Memento` object is a "black box" that only the `Originator` can read.
    - **History Management:** The `Caretaker` maintains a stack of snapshots without knowing their contents.

## 🚀 Problem Statement
You need to expand a basic text editor to handle complex state saving, including text content, cursor position, and formatting styles. The challenge is implementing an Undo/Redo stack that doesn't expose the editor's private fields to the history manager.

## 🧠 Thinking Process & Approach
Implementing Undo requires saving state without exposing private data. The approach uses an opaque Memento object that stores a snapshot. The Editor (Originator) creates it, and the History (Caretaker) manages the stack, ensuring 'time-travel' is possible.

### Key Observations:
- Encapsulation preservation (Caretaker can't read Memento).
- Deep copying state to prevent side effects.

### Technical Constraints
- **Immutability:** Once a `Memento` is created, its state must never change.
- **Deep Copying:** Ensure that saving a state captures the actual values, not just references that might change later.

