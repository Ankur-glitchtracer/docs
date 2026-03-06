# 🔠 Interpreter Pattern: Smart Home Rule Engine

## 📝 Overview
The **Interpreter Pattern** defines a representation for a grammar along with an evaluator to process sentences in a simple language. It’s perfect for building custom logic engines where users define rules at runtime.

!!! abstract "Core Concepts"
    - **Expression Tree:** Parsing a string into a tree of "Terminal" (values) and "Non-Terminal" (operators) objects.
    - **Recursive Evaluation:** Each node in the tree knows how to interpret itself and its children.

## 🚀 Problem Statement
You are building a Smart Home Hub where users can write their own automation rules, such as `"TEMP > 30 AND HUMIDITY > 70"`. You need a way to parse these strings and evaluate them against real-time sensor data.

## 🧠 Thinking Process & Approach
Complex boolean logic entered as strings requires a grammar. The approach is to break the string into tokens and build a recursive tree where each node (Expression) knows how to evaluate itself against a given context.

### Key Observations:
- Recursive tree evaluation.
- Separation of parsing logic from execution logic.

### Technical Constraints
- **Recursive Grammar:** Support nested logic (e.g., `(A AND B) OR C`).
- **Extensibility:** Adding a new operator (like `NOT` or `!=`) should only require adding a new class, not changing the parser or existing expressions.

## 🛠️ Requirements
1. Abstract Expression.
2. Terminal Expressions.
3. Non-terminal Expressions.
4. Context object.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/interpreter/rule_engine/rule_engine.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
