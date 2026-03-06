# 🧱 Null Object Pattern: Resilient Discount Engine

## 📝 Overview
The **Null Object Pattern** uses an object to represent the absence of a value or behavior instead of relying on `null` or `None`. This simplifies client code by removing repetitive null-checks and providing a safe "do-nothing" fallback.

!!! abstract "Core Concepts"
    - **Safe Defaults:** Providing a predictable object that implements the interface but performs no action.
    - **Null-Check Elimination:** Clean up your business logic by removing `if obj is not None:` blocks.

## 🚀 Problem Statement
In an e-commerce checkout system, users can enter coupon codes. If a code is invalid, the lookup usually returns `None`. This forces every part of the system to check for `None` before applying the discount, leading to brittle and cluttered code.

### Technical Constraints
- **Interface Adherence:** The `NoDiscount` object must implement the same `apply_discount` method as real coupons.
- **Zero Impact:** Applying a `NoDiscount` coupon must return the original price without any side effects.

## 🛠️ Requirements
1.  **Abstract Interface:** Define the `Coupon` contract for all discount types.
2.  **Real Coupons:** Implement `PercentageDiscount` and `FlatDiscount` classes.
3.  **Null Object:** Create a `NoDiscount` class that returns the price unchanged.
4.  **Smart Factory:** Implement a `get_coupon(code)` method that returns either a real coupon or the `NoDiscount` object.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/null_object/discount_system/discount_system.py"
```

!!! success "Why this works"
    It moves the "missing value" logic from the business flow into the object structure. The checkout logic becomes a clean, one-line call, making the system more robust and easier to maintain.
