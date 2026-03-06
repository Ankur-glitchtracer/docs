# 🍕 Decorator Pattern: Dynamic Pizza Customizer

## 📝 Overview
The **Decorator Pattern** allows you to dynamically attach new behaviors to an object at runtime without affecting other objects of the same class. It provides a flexible alternative to subclassing for extending functionality.

!!! abstract "Core Concepts"
    - **Wrapper Principle:** Each decorator "wraps" the previous object, adding its own logic before or after delegating to the inner object.
    - **Recursive Decoration:** You can stack an infinite number of decorators (e.g., double cheese, triple olives).

## 🚀 Problem Statement
You are building a POS system for a pizza parlor. Customers can add any combination of toppings to a base pizza. Using inheritance to create classes like `CheesePepperoniMushroomPizza` is impossible due to the sheer number of combinations and the possibility of "double" toppings.

### Technical Constraints
- **Identity:** The decorated object must still be recognized as a `Pizza` by the system.
- **Cumulative Behavior:** Both `get_cost()` and `get_description()` must correctly aggregate values from all layers of the "onion."

## 🛠️ Requirements
1.  **Component Interface:** A `Pizza` interface with `get_cost()` and `get_description()`.
2.  **Base Component:** `PlainPizza` representing the starting point.
3.  **Abstract Decorator:** `ToppingDecorator` that implements `Pizza` and stores a reference to a `Pizza`.
4.  **Concrete Decorators:** Implement `Cheese`, `Pepperoni`, and `Mushroom`.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/decorator/pizza_builder_decorator/pizza_builder_decorator.py"
```

!!! success "Why this works"
    It follows the Single Responsibility Principle by allowing each topping to be its own class. You can add, remove, or reorder toppings at runtime, providing maximum flexibility without the maintenance nightmare of a massive class hierarchy.
