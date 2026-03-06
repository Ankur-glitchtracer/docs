# 🍕 Decorator Pattern: Dynamic Pizza Customizer

## 📝 Overview
The **Decorator Pattern** allows you to dynamically attach new behaviors to an object at runtime without affecting other objects of the same class. It provides a flexible alternative to subclassing for extending functionality.

!!! abstract "Core Concepts"
    - **Wrapper Principle:** Each decorator "wraps" the previous object, adding its own logic before or after delegating to the inner object.
    - **Recursive Decoration:** You can stack an infinite number of decorators (e.g., double cheese, triple olives).

## 🚀 Problem Statement
You are building a POS system for a pizza parlor. Customers can add any combination of toppings to a base pizza. Using inheritance to create classes like `CheesePepperoniMushroomPizza` is impossible due to the sheer number of combinations and the possibility of "double" toppings.

## 🧠 Thinking Process & Approach
Complex objects with many optional parameters lead to 'telescoping constructors'. The approach is to use a step-by-step builder that separates the configuration of the parts from the final assembly. Adding a validation step in `build()` ensures the object is always born in a valid state.

### Key Observations:
- Fluent interface for readable configuration.
- Internal validation before final object return.

### Technical Constraints
- **Identity:** The decorated object must still be recognized as a `Pizza` by the system.
- **Cumulative Behavior:** Both `get_cost()` and `get_description()` must correctly aggregate values from all layers of the "onion."

## 🛠️ Requirements
1. Product: A complex Computer object.
2. Builder Interface: Defines steps to build the computer.
3. Validation: Ensure the computer is in a valid state before build returns.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/decorator/pizza_builder_decorator/pizza_builder_decorator.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
