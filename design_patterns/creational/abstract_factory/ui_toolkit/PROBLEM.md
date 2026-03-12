# 🎨 Abstract Factory: Cross-Platform UI Kit

## 📝 Overview
The **Abstract Factory** provides an interface for creating families of related or dependent objects without specifying their concrete classes. This is essential for maintaining visual consistency across different Operating Systems (e.g., Windows vs. macOS).

!!! abstract "Core Concepts"

    - **Product Families:** Ensuring that all components (Buttons, Sliders) belong to the same theme.
        - **Theme Isolation:** The client code remains agnostic of the specific UI theme being rendered.

!!! info "Why Use This Pattern?"

    - **Decouples object creation from business logic**
    - **Simplifies testing by allowing mock object injection**
    - **Follows the Open/Closed Principle for new object types**


## 🏭 The Engineering Story
**The Villain:** "Dependency Chaos." Your client code is riddled with `if os == 'Windows': create_button()` checks. Adding a new theme requires editing 50 files.

**The Hero:** "The Kit Provider." A single interface that dispenses families of related objects without specifying their concrete classes.

**The Plot:**

1. Define an interface for creating all products (Buttons, Windows).
2. Create concrete factories for each variant (MacFactory, WinFactory).
3. Client code asks the factory for a button, never knowing if it's Mac or Windows.

**The Twist (Failure):** If ignored, you get **Inconsistent UI States** where a Mac scrollbar appears on a Windows window.

**Interview Signal:** Demonstrates ability to enforce **Consistency** across product families.

## 🚀 Problem Statement
You are building a cross-platform UI toolkit. A major constraint is that you must never mix themes: a macOS button should never appear in a Windows-themed window. Hardcoding theme checks throughout the UI logic leads to a maintenance nightmare.

## 🛠️ Requirements

1. Product Interfaces: Create Button and Checkbox interfaces.
2. Concrete Products: Implement Windows and Mac variants.
3. Abstract Factory Interface: create_button() and create_checkbox().

### Technical Constraints

- **Consistency:** The factory must guarantee that all returned products are compatible with each other.
- **Open/Closed Principle:** Switching the entire app's look and feel should ideally require changing only a single line of code.

## 🧠 Thinking Process & Approach
When we have families of related products (like Windows vs Mac buttons), we need a way to enforce consistency. The approach is to create a 'Factory of Factories' where each concrete factory is responsible for an entire theme, preventing the mixing of incompatible UI components.

### Key Observations:

- Dependency Injection of the factory into the client.
- Strict interface adherence for all product types.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/abstract_factory/ui_toolkit/ui_toolkit.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Factory Method](../../factory/document_factory/PROBLEM.md) — Abstract Factory often uses Factory Methods for its products.
- [Prototype](../../prototype/PROBLEM.md) — Concrete factories are often Singletons and can use Prototype for object creation.
- [Builder](../../builder/custom_pc_builder/PROBLEM.md) — Abstract Factory returns the product immediately; Builder builds it step by step.
