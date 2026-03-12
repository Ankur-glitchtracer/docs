# 🌿 Composite Pattern: Unified Organization Chart

## 📝 Overview
The **Composite Pattern** allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly, simplifying code that deals with complex recursive structures.

!!! abstract "Core Concepts"

    - **Recursive Composition:** Containers can hold both leaf nodes and other containers.
        - **Uniform Interface:** Both `Employee` and `Department` implement the same methods, allowing for transparent interaction.

!!! info "Why Use This Pattern?"

    - **Treats individual objects and compositions uniformly**
    - **Simplifies client code by hiding structure complexity**
    - **Easily adds new types of components**


## 🚀 Problem Statement
You need to build a system to calculate the total salary of an entire company. The company is structured into departments, sub-departments, and individual employees. The challenge is calculating the sum without the client needing to know whether they are dealing with a single person or a whole division.

## 🛠️ Requirements

1. Component Interface.
2. Leaf: Individual objects.
3. Composite: Recursive containers.

### Technical Constraints

- **Hierarchy Transparency:** A `Department` should be able to contain any `Entity`, whether it's a `Developer` (leaf) or another `Department` (composite).
- **Recursive Summation:** Calling `get_salary()` on the root node should automatically trigger a recursive traversal of the entire tree.

## 🧠 Thinking Process & Approach
Managing part-whole hierarchies (like Org Charts) usually requires different logic for individuals vs groups. The approach is to treat both as the same interface, allowing recursive operations like 'get_salary' to work transparently.

### Key Observations:

- Uniform treatment of leaf and composite nodes.
- Recursive data structure traversal.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/composite/organisation_chart/organisation_chart.py"
```

!!! success "Why this works"
    By using a common interface, the client code can interact with individual objects and compositions identically. This removes the need for type checking and simplifies recursive operations.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Decorator](../../decorator/pizza_builder_decorator/PROBLEM.md) — Both have similar recursive structures, but Decorator has only one child.
- [Visitor](../../../behavioral/visitor/PROBLEM.md) — Visitor can be used to apply an operation over a Composite tree.
- [Chain of Responsibility](../../../behavioral/chain_of_responsibility/PROBLEM.md) — Chain of Responsibility can be implemented using Composite.
