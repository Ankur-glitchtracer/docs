# 📋 Iterator Pattern: Unified Menu Traversal

## 📝 Overview
The **Iterator Pattern** provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation (be it a List, Map, or Tree). This allows for a uniform way to traverse diverse collections.

!!! abstract "Core Concepts"

    - **Standardized Traversal:** Using `next()` and `has_next()` regardless of the data structure.
        - **Encapsulation:** The client doesn't need to know if the items are stored in a linked list or a hash map.

!!! info "Why Use This Pattern?"

    - **Provides a way to access elements sequentially**
    - **Hides the underlying representation of a collection**
    - **Supports multiple simultaneous traversals**


## 🚀 Problem Statement
Two restaurants have merged. One stores its menu in a `List`, the other in a `Dictionary`. The waitress needs to print both menus, but writing separate `for` loops for each data structure is repetitive and brittle.

## 🛠️ Requirements

1. Iterator Interface.
2. Concrete Iterator.
3. Aggregate Interface.
4. Concrete Aggregate.

### Technical Constraints

- **Polymorphism:** The client (Waitress) should work with a common `Iterator` interface.
- **Separation of Concerns:** The menu class should handle storage, while the iterator class handles traversal.

## 🧠 Thinking Process & Approach
Accessing different collection types (List vs Map) usually requires different loops. The approach is to wrap any structure in a standard Iterator interface (`next`, `has_next`), allowing the client to traverse data uniformly.

### Key Observations:

- Standardized traversal protocol.
- Abstraction of underlying data structures.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/iterator/menu_iterator/menu_iterator.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Composite](../../../structural/composite/organisation_chart/PROBLEM.md) — Iterator can be used to traverse Composites.
- [Factory Method](../../../creational/factory/document_factory/PROBLEM.md) — Factory Method can be used to create the appropriate Iterator subclass.
- [Memento](../../memento/text_editor_history/PROBLEM.md) — Memento can be used to capture the state of an iteration.
