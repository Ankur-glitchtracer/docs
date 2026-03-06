# 📋 Iterator Pattern: Unified Menu Traversal

## 📝 Overview
The **Iterator Pattern** provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation (be it a List, Map, or Tree). This allows for a uniform way to traverse diverse collections.

!!! abstract "Core Concepts"
    - **Standardized Traversal:** Using `next()` and `has_next()` regardless of the data structure.
    - **Encapsulation:** The client doesn't need to know if the items are stored in a linked list or a hash map.

## 🚀 Problem Statement
Two restaurants have merged. One stores its menu in a `List`, the other in a `Dictionary`. The waitress needs to print both menus, but writing separate `for` loops for each data structure is repetitive and brittle.

## 🧠 Thinking Process & Approach
Accessing different collection types (List vs Map) usually requires different loops. The approach is to wrap any structure in a standard Iterator interface (`next`, `has_next`), allowing the client to traverse data uniformly.

### Key Observations:
- Standardized traversal protocol.
- Abstraction of underlying data structures.

### Technical Constraints
- **Polymorphism:** The client (Waitress) should work with a common `Iterator` interface.
- **Separation of Concerns:** The menu class should handle storage, while the iterator class handles traversal.

