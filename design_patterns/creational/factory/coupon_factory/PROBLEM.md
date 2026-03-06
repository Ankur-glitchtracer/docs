# 🎟️ Factory Pattern: Smart Coupon System

## 📝 Overview
The **Factory Pattern** provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In this e-commerce context, it centralizes the logic for generating various discount types from raw data.

!!! abstract "Core Concepts"
    - **Creation Decoupling:** The `DiscountEngine` shouldn't know how to instantiate specific coupon types.
    - **No-Discount Fallback:** Gracefully handling invalid or missing coupons using a `NoDiscountCoupon`.

## 🚀 Problem Statement
An e-commerce system receives coupon data from external sources like JSON or databases. The `DiscountEngine` is currently responsible for both calculating discounts and deciding which coupon object to create, leading to tight coupling and maintenance headaches when new coupon types are added.

## 🧠 Thinking Process & Approach
Decoupling object creation from business logic is key. The approach uses a central Factory class that parses raw data (like JSON or DB records) and decides which class to instantiate, keeping the main engine focused purely on processing.

### Key Observations:
- Centralized mapping of types to classes.
- Business logic works only with interfaces, never concrete types.

### Technical Constraints
- **Extensibility:** Adding a new coupon type (e.g., "Buy One Get One") should not require changes to the `DiscountEngine`.
- **Interface Consistency:** All coupon objects must adhere to a common `apply_discount` contract.

