# 🌿 Composite Pattern: Unified Organization Chart

## 📝 Overview
The **Composite Pattern** allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly, simplifying code that deals with complex recursive structures.

!!! abstract "Core Concepts"
    - **Recursive Composition:** Containers can hold both leaf nodes and other containers.
    - **Uniform Interface:** Both `Employee` and `Department` implement the same methods, allowing for transparent interaction.

## 🚀 Problem Statement
You need to build a system to calculate the total salary of an entire company. The company is structured into departments, sub-departments, and individual employees. The challenge is calculating the sum without the client needing to know whether they are dealing with a single person or a whole division.

### Technical Constraints
- **Hierarchy Transparency:** A `Department` should be able to contain any `Entity`, whether it's a `Developer` (leaf) or another `Department` (composite).
- **Recursive Summation:** Calling `get_salary()` on the root node should automatically trigger a recursive traversal of the entire tree.

## 🛠️ Requirements
1.  **Component Interface:** An abstract `Entity` with a `get_salary()` method.
2.  **Leaf Node:** An `Employee` class representing a single person with a fixed salary.
3.  **Composite Node:** A `Department` class that holds a list of `Entity` objects and sums their salaries.
4.  **Management Methods:** The `Department` must support `add()` and `remove()` operations.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/composite/organisation_chart/organisation_chart.py"
```

!!! success "Why this works"
    It simplifies the client code significantly. The client doesn't need to write `if instance of Department: ... else: ...`. They simply call `get_salary()` on the top-level entity, and the pattern's recursive nature handles the rest, regardless of how deep or complex the tree is.
