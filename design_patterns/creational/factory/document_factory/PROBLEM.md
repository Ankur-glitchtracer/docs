# 📄 Factory Method: Dynamic Document Creator

## 📝 Overview
The **Factory Method** pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. This implementation focuses on a Document Management System where the specific file format (PDF, Word) is determined at runtime.

!!! abstract "Core Concepts"
    - **Subclass Responsibility:** The base `Application` delegates the instantiation of documents to its specialized subclasses.
    - **Parallel Hierarchies:** Maintaining a clear relationship between the creator hierarchy (`Application`) and the product hierarchy (`Document`).

## 🚀 Problem Statement
You are building a Document Management System that supports multiple formats like PDF and Word. If the main application logic explicitly checks types to create objects (e.g., `if type == "pdf"`), it becomes brittle and difficult to extend with new formats like Excel or Markdown.

### Technical Constraints
- **Loose Coupling:** The client code (Application) should only interact with the abstract `Document` interface.
- **Type Safety:** Ensure each application variant returns the correct document type without casting.

## 🛠️ Requirements
1.  **Abstract Product:** Define a `Document` class with an `open()` method.
2.  **Concrete Products:** Implement `PDFDocument` and `WordDocument`.
3.  **Abstract Creator:** An `Application` class with an abstract `create_document()` factory method.
4.  **Concrete Creators:** `PDFApplication` and `WordApplication` that return their respective document types.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/factory/document_factory/document_factory.py"
```

!!! success "Why this works"
    It removes the need to bind application-specific classes into the code. The code only deals with the `Document` interface; therefore, it can work with any user-defined concrete document classes.
