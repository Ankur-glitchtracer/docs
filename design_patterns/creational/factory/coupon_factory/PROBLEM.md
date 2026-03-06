# 🎟️ Factory Pattern: Smart Coupon System

## 📝 Overview
The **Factory Pattern** provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In this e-commerce context, it centralizes the logic for generating various discount types from raw data.

!!! abstract "Core Concepts"
    - **Creation Decoupling:** The `DiscountEngine` shouldn't know how to instantiate specific coupon types.
    - **No-Discount Fallback:** Gracefully handling invalid or missing coupons using a `NoDiscountCoupon`.

## 🚀 Problem Statement
An e-commerce system receives coupon data from external sources like JSON or databases. The `DiscountEngine` is currently responsible for both calculating discounts and deciding which coupon object to create, leading to tight coupling and maintenance headaches when new coupon types are added.

### Technical Constraints
- **Extensibility:** Adding a new coupon type (e.g., "Buy One Get One") should not require changes to the `DiscountEngine`.
- **Interface Consistency:** All coupon objects must adhere to a common `apply_discount` contract.

## 🛠️ Requirements
1.  **Coupon Interface:** An abstract base class with an `apply_discount(price)` method.
2.  **Concrete Coupons:** Implement `PercentageCoupon`, `FlatCoupon`, and `NoDiscountCoupon`.
3.  **Coupon Factory:** A central `get_coupon(code, type, value)` method to return the correct object.
4.  **Engine Refactor:** Update the `DiscountEngine` to use the factory for all coupon generation.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/factory/coupon_factory/coupon_factory.py"
```

!!! success "Why this works"
    By separating **Creation Logic** from **Business Logic**, the system becomes modular. The engine remains "closed for modification" while the factory stays "open for extension," allowing for easy addition of new discount strategies.
