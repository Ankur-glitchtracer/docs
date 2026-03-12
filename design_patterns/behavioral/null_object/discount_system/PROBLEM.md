# 🧱 Null Object: Resilient Discount Engine

## 📝 Overview
The **Null Object Pattern** uses an object to represent the absence of a value or behavior instead of relying on `null` or `None`. This simplifies client code by removing repetitive null-checks and providing a safe "do-nothing" fallback.

!!! abstract "Core Concepts"

    - **Safe Defaults:** Providing a predictable object that implements the interface but performs no action.
        - **Null-Check Elimination:** Clean up your business logic by removing `if obj is not None:` blocks.

!!! info "Why Use This Pattern?"

    - **Avoids null checks in client code**
    - **Provides a default behavior for empty cases**
    - **Simplifies code by treating null as a valid object**


## 🚀 Problem Statement
In an e-commerce checkout system, users can enter coupon codes. If a code is invalid, the lookup usually returns `None`. This forces every part of the system to check for `None` before applying the discount, leading to brittle and cluttered code.

## 🛠️ Requirements

1.  **Abstract Interface:** Define the contract for discount application.
2.  **Real Implementation:** Concrete classes for different discount types.
3.  **Null Object:** A "do-nothing" class that implements the interface safely.

### Technical Constraints

- **Interface Adherence:** The `NoDiscount` object must implement the same `apply_discount` method as real coupons.
- **Zero Impact:** Applying a `NoDiscount` coupon must return the original price without any side effects.

## 🧠 Thinking Process & Approach
Repeating 'if obj is not None' clutters code. The approach is to create a 'do-nothing' instance of the same interface. This ensures the business logic can always call methods safely, treating the 'missing' case as just another valid state.

### Key Observations:

- Safe default behavior.
- Total elimination of null-pointer exceptions.
- Consistent API usage for both valid and "empty" cases.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/null_object/discount_system/discount_system.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns. It eliminates the "NullPointerException Minefield" and leads to much cleaner business logic.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Strategy](../../strategy/sprinkler_system/PROBLEM.md) — Null Object can be used as a default Strategy.
- [Singleton](../../../creational/singleton/singleton_pattern/PROBLEM.md) — A Null Object is often a Singleton.
