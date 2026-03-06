# 📄 Factory Method: Dynamic Document Creator

## 📝 Overview
The **Factory Method** pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. This implementation focuses on a Document Management System where the specific file format (PDF, Word) is determined at runtime.

!!! abstract "Core Concepts"
    - **Subclass Responsibility:** The base `Application` delegates the instantiation of documents to its specialized subclasses.
    - **Parallel Hierarchies:** Maintaining a clear relationship between the creator hierarchy (`Application`) and the product hierarchy (`Document`).

## 🚀 Problem Statement
You are building a Document Management System that supports multiple formats like PDF and Word. If the main application logic explicitly checks types to create objects (e.g., `if type == "pdf"`), it becomes brittle and difficult to extend with new formats like Excel or Markdown.

## 🧠 Thinking Process & Approach
Decoupling object creation from business logic is key. The approach uses a central Factory class that parses raw data (like JSON or DB records) and decides which class to instantiate, keeping the main engine focused purely on processing.

### Key Observations:
- Centralized mapping of types to classes.
- Business logic works only with interfaces, never concrete types.

### Technical Constraints
- **Loose Coupling:** The client code (Application) should only interact with the abstract `Document` interface.
- **Type Safety:** Ensure each application variant returns the correct document type without casting.

## 🛠️ Requirements
1. Coupon Interface: ABC with applyDiscount.
2. Concrete Coupons: Percentage, Flat, NoDiscount.
3. Coupon Factory: Decoupled creation logic.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/factory/document_factory/document_factory.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
