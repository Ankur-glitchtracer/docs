# 🛒 Visitor Pattern: Extensible Tax Engine

## 📝 Overview
The **Visitor Pattern** allows you to add new operations to an existing object structure without modifying the objects themselves. This is achieved by separating the data (Items) from the algorithms (Tax Rules) that operate on them.

!!! abstract "Core Concepts"

    - **Double Dispatch:** Directing the operation based on both the Visitor type and the Element type.
        - **Behavioral Extension:** Add new features (like a new tax law) without touching stable data classes.

!!! info "Why Use This Pattern?"

    - **Adds new operations to existing object structures**
    - **Separates an algorithm from an object structure**
    - **Follows the Open/Closed Principle for new operations**


## 🚀 Problem Statement
You have a shopping cart with various item types like `Electronics`, `Food`, and `Luxury`. You need to apply different tax rules (GST, VAT, Import Tax). If you add tax methods to each item class, you'll violate the Single Responsibility Principle and face a maintenance nightmare.

## 🛠️ Requirements

1.  **Item Interface:** Define an `accept(visitor)` method for all item types.
2.  **Concrete Items:** Implement `Electronics`, `Food`, and `Luxury`.
3.  **Visitor Interface:** Define `visit_electronics()`, `visit_food()`, etc.
4.  **Concrete Visitors:** Implement `GSTVisitor`, `VATVisitor`, and `ImportTaxVisitor`.

### Technical Constraints

- **No Structural Changes:** New tax visitors must be added without modifying the `Item` classes.
- **Type Sensitivity:** Tax calculation must differ based on whether the item is `Electronics` or `Food`.

## 🧠 Thinking Process & Approach
(To be detailed...)

## 💻 Solution Implementation

```python
# (To be detailed...)
```

!!! success "Why this works"
    It provides a clean way to follow the Open/Closed Principle for operations. The data structures remain thin and stable, while the "behaviors" are encapsulated into separate Visitor objects that can be added or removed independently.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Composite](../../structural/composite/organisation_chart/PROBLEM.md) — Visitor can be used to apply an operation over a Composite tree.
- [Interpreter](../interpreter/rule_engine/PROBLEM.md) — Visitor can be used to implement the interpretation.
