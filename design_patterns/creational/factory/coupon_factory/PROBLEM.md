# 🎟️ Factory Pattern: Smart Coupon System

## 📝 Overview
The **Factory Pattern** provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In this e-commerce context, it centralizes the logic for generating various discount types from raw data.

!!! abstract "Core Concepts"

    - **Creation Decoupling:** The `DiscountEngine` shouldn't know how to instantiate specific coupon types.
        - **No-Discount Fallback:** Gracefully handling invalid or missing coupons using a `NoDiscountCoupon`.

!!! info "Why Use This Pattern?"

    - **Decouples object creation from business logic**
    - **Simplifies testing by allowing mock object injection**
    - **Follows the Open/Closed Principle for new object types**


## 🏭 The Engineering Story
**The Villain:** "The Hardcoded Switch." Your `DiscountEngine` has a 100-line `if-elif` block to create different coupon objects. Adding a "Holiday" coupon requires touching the core engine, risking a production crash.

**The Hero:** "The Specialized Creator." A factory that handles the "How" of object creation, leaving the client to focus on the "What."

**The Plot:**

1. Define a common interface for all products (Coupons).
2. Create a Factory class with a `create_coupon(type)` method.
3. The client calls the factory instead of `new Coupon()`.

**The Twist (Failure):** **The Concrete Leak**. If the factory returns a concrete class instead of an interface, the client becomes tightly coupled anyway.

**Interview Signal:** Shows mastery of **Object Creation Decoupling** and the Open/Closed Principle.

## 🚀 Problem Statement
An e-commerce system receives coupon data from external sources like JSON or databases. The `DiscountEngine` is currently responsible for both calculating discounts and deciding which coupon object to create, leading to tight coupling and maintenance headaches when new coupon types are added.

## 🛠️ Requirements

1. Coupon Interface: ABC with applyDiscount.
2. Concrete Coupons: Percentage, Flat, NoDiscount.
3. Coupon Factory: Decoupled creation logic.

### Technical Constraints

- **Extensibility:** Adding a new coupon type (e.g., "Buy One Get One") should not require changes to the `DiscountEngine`.
- **Interface Consistency:** All coupon objects must adhere to a common `apply_discount` contract.

## 🧠 Thinking Process & Approach
Decoupling object creation from business logic is key. The approach uses a central Factory class that parses raw data (like JSON or DB records) and decides which class to instantiate, keeping the main engine focused purely on processing.

### Key Observations:

- Centralized mapping of types to classes.
- Business logic works only with interfaces, never concrete types.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/factory/coupon_factory/coupon_factory.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Abstract Factory](../../abstract_factory/ui_toolkit/PROBLEM.md) — Both are used for object creation, but Abstract Factory creates families of related objects.
- [Prototype](../../prototype/PROBLEM.md) — Factory Method often uses Prototype to clone objects instead of instantiating them.
- [Template Method](../../../behavioral/template/data_exporter/PROBLEM.md) — Factory Methods are often called within Template Methods.
