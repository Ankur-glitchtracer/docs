# 📄 Factory Method: Dynamic Document Creator

## 📝 Overview
The **Factory Method** pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. This implementation focuses on a Document Management System where the specific file format (PDF, Word) is determined at runtime.

!!! abstract "Core Concepts"

    - **Subclass Responsibility:** The base `Application` delegates the instantiation of documents to its specialized subclasses.
        - **Parallel Hierarchies:** Maintaining a clear relationship between the creator hierarchy (`Application`) and the product hierarchy (`Document`).

!!! info "Why Use This Pattern?"

    - **Decouples object creation from business logic**
    - **Simplifies testing by allowing mock object injection**
    - **Follows the Open/Closed Principle for new object types**


## 🏭 The Engineering Story
**The Villain:** "The Rigid Creator." You have a `DocumentEditor` that only knows how to create `TXT` files. When the business asks for `PDF` and `DOCX`, you have to rewrite the entire `Editor` class.

**The Hero:** "The Deferred Method." Defines a method for creating an object, but lets subclasses decide which class to instantiate.

**The Plot:**

1. Define a base class with an abstract `create_document()` method.
2. Create specialized creators (e.g., `PDFApplication`, `WordApplication`).
3. The base class uses the product, but doesn't know its concrete type.

**The Twist (Failure):** **Parallel Hierarchy Bloat**. For every new document type, you must create *both* a new Document class and a new Application class.

**Interview Signal:** Demonstrates understanding of **Inversion of Control** and subclass-driven instantiation.

## 🚀 Problem Statement
You are building a Document Management System that supports multiple formats like PDF and Word. If the main application logic explicitly checks types to create objects (e.g., `if type == "pdf"`), it becomes brittle and difficult to extend with new formats like Excel or Markdown.

## 🛠️ Requirements

1. Coupon Interface: ABC with applyDiscount.
2. Concrete Coupons: Percentage, Flat, NoDiscount.
3. Coupon Factory: Decoupled creation logic.

### Technical Constraints

- **Loose Coupling:** The client code (Application) should only interact with the abstract `Document` interface.
- **Type Safety:** Ensure each application variant returns the correct document type without casting.

## 🧠 Thinking Process & Approach
Decoupling object creation from business logic is key. The approach uses a central Factory class that parses raw data (like JSON or DB records) and decides which class to instantiate, keeping the main engine focused purely on processing.

### Key Observations:

- Centralized mapping of types to classes.
- Business logic works only with interfaces, never concrete types.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/factory/document_factory/document_factory.py"
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
