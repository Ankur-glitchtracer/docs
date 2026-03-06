# 🌳 Flyweight Pattern: High-Performance Forest Simulator

## 📝 Overview
The **Flyweight Pattern** is a structural optimization technique used to support large numbers of fine-grained objects efficiently by sharing as much data as possible. It is particularly useful when an application is running out of RAM due to millions of similar objects.

!!! abstract "Core Concepts"
    - **Intrinsic State:** Constant data shared across many objects (e.g., tree texture/color).
    - **Extrinsic State:** Unique data specific to each instance (e.g., X, Y coordinates).
    - **Flyweight Factory:** A manager that ensures identical flyweights are reused rather than recreated.

## 🚀 Problem Statement
Imagine building a game like Minecraft where you need to render 1,000,000 trees. Creating a full object for each tree, including heavy sprite and texture data, would quickly exhaust the system's memory.

### Technical Constraints
- **Memory Efficiency:** Identical tree types (e.g., "Oak", "Pine") must share the same memory address.
- **Data Separation:** Extrinsic state (coordinates) must be passed to the flyweight at drawing time, not stored within it.

## 🛠️ Requirements
1.  **Flyweight (TreeType):** Stores shared data like name, color, and texture.
2.  **Flyweight Factory:** Manages a cache of `TreeType` objects.
3.  **Context (Tree):** A lightweight object storing only unique coordinates and a reference to a `TreeType`.
4.  **Forest Client:** Coordinates the planting and drawing of millions of trees.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/flyweight/forest_simulator/forest_simulator.py"
```

!!! success "Why this works"
    By stripping away the "heavy" shared data and keeping only the unique "lightweight" coordinates, we reduce the memory footprint from gigabytes to megabytes. The factory ensures that no matter how many Oak trees we plant, we only ever store the Oak texture once.
