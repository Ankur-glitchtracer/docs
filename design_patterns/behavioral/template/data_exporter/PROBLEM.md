# 🏗️ Template Method: Universal Data Exporter

## 📝 Overview
The **Template Method** pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps without changing the overall structure. It’s the "recipe" approach to software design.

!!! abstract "Core Concepts"

    - **Invariant vs. Variant Steps:** Keeping common logic (e.g., reading from DB) in the base class and deferring custom logic (e.g., formatting) to subclasses.
        - **Hollywood Principle:** "Don't call us, we'll call you"—the base class controls the execution flow.

!!! info "Why Use This Pattern?"

    - **Defines the skeleton of an algorithm in a base class**
    - **Lets subclasses redefine specific steps**
    - **Promotes code reuse in the base class**


## 🚀 Problem Statement
You are building a tool to export data into multiple formats (CSV, PDF, JSON). While the formatting and file writing steps differ for each, the initial data fetching from the database is always the same. Copy-pasting the fetching logic into every exporter class leads to massive code duplication.

## 🛠️ Requirements

1. Abstract Class: Template method skeleton.
2. Concrete Classes: Primitive implementations.

### Technical Constraints

- **Algorithm Enforcement:** All exporters must strictly follow the sequence: `Read -> Format -> Write`.
- **Hook Methods:** Provide optional "hooks" (like sending a notification) that subclasses can choose to implement or ignore.

## 🧠 Thinking Process & Approach
When multiple algorithms share a high-level sequence but differ in details, we use a template method. The base class defines the mandatory 'skeleton', while subclasses fill in the specific primitive operations.

### Key Observations:

- Invariant steps in base class.
- Variant hooks in subclasses.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/template/data_exporter/data_exporter.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Factory Method](../../../creational/factory/document_factory/PROBLEM.md) — Factory Methods are often called within Template Methods.
- [Strategy](../../strategy/sprinkler_system/PROBLEM.md) — Template Method uses inheritance to vary parts of an algorithm; Strategy uses composition.
