# 🍕 Decorator: Dynamic Pizza Customizer

## 📝 Overview
The **Decorator Pattern** allows you to dynamically attach new behaviors to an object at runtime without affecting other objects of the same class. It provides a flexible alternative to subclassing for extending functionality.

!!! abstract "Core Concepts"

    - **Wrapper Principle:** Each decorator "wraps" the previous object, adding its own logic before or after delegating to the inner object.
        - **Recursive Decoration:** You can stack an infinite number of decorators (e.g., double cheese, triple olives).

!!! info "Why Use This Pattern?"

    - **Simplifies complex object creation step-by-step**
    - **Allows different representations of the same product**
    - **Separates construction from representation**


## 🚀 Problem Statement
You are building a POS system for a pizza parlor. Customers can add any combination of toppings to a base pizza. Using inheritance to create classes like `CheesePepperoniMushroomPizza` is impossible due to the sheer number of combinations and the possibility of "double" toppings.

## 🛠️ Requirements

1.  **Component Interface:** Define the `Pizza` abstract base class.
2.  **Concrete Component:** Implement `PlainPizza`.
3.  **Base Decorator:** Create `ToppingDecorator` to maintain a reference to a `Pizza` object.
4.  **Concrete Decorators:** Implement `Cheese`, `Pepperoni`, `Mushroom`, `Olive`, and `DiscountDecorator`.

### Technical Constraints

- **Identity:** The decorated object must still be recognized as a `Pizza` by the system.
- **Cumulative Behavior:** Both `get_cost()` and `get_description()` must correctly aggregate values from all layers of the "onion."

## 🧠 Thinking Process & Approach
When you have a base object that can be extended in numerous combinations, inheritance leads to a 'class explosion'. The approach is to create a decorator class that implements the same interface as the object it wraps. This allows for dynamic, runtime composition of features.

### Key Observations:

- Avoids rigid inheritance hierarchies.
- Enables the Open/Closed Principle: classes are open for extension but closed for modification.
- Each layer is independent and only cares about its specific addition.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/decorator/pizza_builder_decorator/pizza_builder_decorator.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns. It allows for infinite combinations of toppings without creating a complex class hierarchy.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Adapter](../../adapter/format_translator/PROBLEM.md) — Adapter changes the interface; Decorator adds responsibilities without changing the interface.
- [Proxy](../../proxy/lazy_loading_proxy/PROBLEM.md) — Proxy controls access; Decorator adds functionality.
- [Composite](../../composite/organisation_chart/PROBLEM.md) — Both use recursion to organize objects.
