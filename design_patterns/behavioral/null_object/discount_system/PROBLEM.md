# 🧱 Null Object Pattern: Resilient Discount Engine

## 📝 Overview
The **Null Object Pattern** uses an object to represent the absence of a value or behavior instead of relying on `null` or `None`. This simplifies client code by removing repetitive null-checks and providing a safe "do-nothing" fallback.

!!! abstract "Core Concepts"
    - **Safe Defaults:** Providing a predictable object that implements the interface but performs no action.
    - **Null-Check Elimination:** Clean up your business logic by removing `if obj is not None:` blocks.

## 🚀 Problem Statement
In an e-commerce checkout system, users can enter coupon codes. If a code is invalid, the lookup usually returns `None`. This forces every part of the system to check for `None` before applying the discount, leading to brittle and cluttered code.

## 🧠 Thinking Process & Approach
Repeating 'if obj is not None' clutters code. The approach is to create a 'do-nothing' instance of the same interface. This ensures the business logic can always call methods safely, treating the 'missing' case as just another valid state.

### Key Observations:
- Safe default behavior.
- Total elimination of null-pointer exceptions.

### Technical Constraints
- **Interface Adherence:** The `NoDiscount` object must implement the same `apply_discount` method as real coupons.
- **Zero Impact:** Applying a `NoDiscount` coupon must return the original price without any side effects.

