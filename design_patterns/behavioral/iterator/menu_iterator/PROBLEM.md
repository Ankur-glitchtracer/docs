# 📋 Iterator Pattern: Unified Menu Traversal

## 📝 Overview
The **Iterator Pattern** provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation (be it a List, Map, or Tree). This allows for a uniform way to traverse diverse collections.

!!! abstract "Core Concepts"
    - **Standardized Traversal:** Using `next()` and `has_next()` regardless of the data structure.
    - **Encapsulation:** The client doesn't need to know if the items are stored in a linked list or a hash map.

## 🚀 Problem Statement
Two restaurants have merged. One stores its menu in a `List`, the other in a `Dictionary`. The waitress needs to print both menus, but writing separate `for` loops for each data structure is repetitive and brittle.

### Technical Constraints
- **Polymorphism:** The client (Waitress) should work with a common `Iterator` interface.
- **Separation of Concerns:** The menu class should handle storage, while the iterator class handles traversal.

## 🛠️ Requirements
1.  **Iterator Interface:** Methods like `next()` and `has_next()`.
2.  **Concrete Iterators:** Traversal logic for `List` and `Dictionary` storage.
3.  **Aggregate Interface:** A `create_iterator()` method for menus.
4.  **Client Refactor:** The `Waitress` should use the iterators to print items in a single, clean loop.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/iterator/menu_iterator/menu_iterator.py"
```

!!! success "Why this works"
    It decouples the traversal algorithm from the collection's structure. If the restaurant decides to switch to a more complex data structure (like a binary tree), the waitress's printing code remains completely unchanged.
