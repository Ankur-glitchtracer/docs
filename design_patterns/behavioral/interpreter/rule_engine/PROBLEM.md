# 🔠 Interpreter Pattern: Smart Home Rule Engine

## 📝 Overview
The **Interpreter Pattern** defines a representation for a grammar along with an evaluator to process sentences in a simple language. It’s perfect for building custom logic engines where users define rules at runtime.

!!! abstract "Core Concepts"
    - **Expression Tree:** Parsing a string into a tree of "Terminal" (values) and "Non-Terminal" (operators) objects.
    - **Recursive Evaluation:** Each node in the tree knows how to interpret itself and its children.

## 🚀 Problem Statement
You are building a Smart Home Hub where users can write their own automation rules, such as `"TEMP > 30 AND HUMIDITY > 70"`. You need a way to parse these strings and evaluate them against real-time sensor data.

### Technical Constraints
- **Recursive Grammar:** Support nested logic (e.g., `(A AND B) OR C`).
- **Extensibility:** Adding a new operator (like `NOT` or `!=`) should only require adding a new class, not changing the parser or existing expressions.

## 🛠️ Requirements
1.  **Expression Interface:** An abstract `Expression` with an `interpret(context)` method.
2.  **Terminal Expressions:** Implement `Variable` and `Constant` classes.
3.  **Non-Terminal Expressions:** Implement `AndExpression`, `OrExpression`, and `GreaterThanExpression`.
4.  **Context:** A dictionary-like object to hold current sensor values.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/interpreter/rule_engine/rule_engine.py"
```

!!! success "Why this works"
    It turns a complex string-parsing problem into a clean, object-oriented structure. By representing the grammar as classes, you can build incredibly flexible and powerful logic engines that are easy to debug and extend.
