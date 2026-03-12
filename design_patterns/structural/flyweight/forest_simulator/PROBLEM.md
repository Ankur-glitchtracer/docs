# 🌳 Flyweight Pattern: High-Performance Forest Simulator

## 📝 Overview
The **Flyweight Pattern** is a structural optimization technique used to support large numbers of fine-grained objects efficiently by sharing as much data as possible. It is particularly useful when an application is running out of RAM due to millions of similar objects.

!!! abstract "Core Concepts"

    - **Intrinsic State:** Constant data shared across many objects (e.g., tree texture/color).
        - **Extrinsic State:** Unique data specific to each instance (e.g., X, Y coordinates).
        - **Flyweight Factory:** A manager that ensures identical flyweights are reused rather than recreated.

!!! info "Why Use This Pattern?"

    - **Minimizes memory usage by sharing state**
    - **Efficiently supports large numbers of small objects**
    - **Separates intrinsic and extrinsic state**


## 🚀 Problem Statement
Imagine building a game like Minecraft where you need to render 1,000,000 trees. Creating a full object for each tree, including heavy sprite and texture data, would quickly exhaust the system's memory.

## 🛠️ Requirements

1. Flyweight (shared state).
2. Context (unique state).
3. Flyweight Factory.

### Technical Constraints

- **Memory Efficiency:** Identical tree types (e.g., "Oak", "Pine") must share the same memory address.
- **Data Separation:** Extrinsic state (coordinates) must be passed to the flyweight at drawing time, not stored within it.

## 🧠 Thinking Process & Approach
Creating millions of identical objects exhausts RAM. The approach is to split state into Intrinsic (shared) and Extrinsic (unique). The shared part is cached in a factory, so we only ever store one instance of each type.

### Key Observations:

- Shared memory for constant state.
- Extrinsic state passed in at runtime.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/flyweight/forest_simulator/forest_simulator.py"
```

!!! success "Why this works"
    This design ensures memory efficiency by caching shared state and only storing unique coordinates externally. It adheres to the Flyweight principle by separating intrinsic and extrinsic data.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Composite](../../composite/organisation_chart/PROBLEM.md) — Composite can use Flyweight to share leaf nodes.
- [State](../../../behavioral/state/document_workflow/PROBLEM.md) — State objects are often shared as Flyweights.
- [Strategy](../../../behavioral/strategy/sprinkler_system/PROBLEM.md) — Strategy objects can be shared as Flyweights.
