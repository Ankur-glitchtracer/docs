# 🎨 Abstract Factory: Cross-Platform UI Kit

## 📝 Overview
The **Abstract Factory** provides an interface for creating families of related or dependent objects without specifying their concrete classes. This is essential for maintaining visual consistency across different Operating Systems (e.g., Windows vs. macOS).

!!! abstract "Core Concepts"
    - **Product Families:** Ensuring that all components (Buttons, Sliders) belong to the same theme.
    - **Theme Isolation:** The client code remains agnostic of the specific UI theme being rendered.

## 🚀 Problem Statement
You are building a cross-platform UI toolkit. A major constraint is that you must never mix themes: a macOS button should never appear in a Windows-themed window. Hardcoding theme checks throughout the UI logic leads to a maintenance nightmare.

### Technical Constraints
- **Consistency:** The factory must guarantee that all returned products are compatible with each other.
- **Open/Closed Principle:** Switching the entire app's look and feel should ideally require changing only a single line of code.

## 🛠️ Requirements
1.  **Abstract Products:** Define `Button` and `Checkbox` interfaces with a `render()` method.
2.  **Concrete Products:** Implement `WindowsButton/Checkbox` and `MacButton/Checkbox`.
3.  **Abstract Factory:** A `UIFactory` interface with `create_button()` and `create_checkbox()`.
4.  **Concrete Factories:** `WindowsFactory` and `MacFactory` to return the appropriate themed components.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/abstract_factory/ui_toolkit/ui_toolkit.py"
```

!!! success "Why this works"
    It enforces consistency among products. By using the Abstract Factory, the application can switch between entire "families" of products (themes) seamlessly, ensuring that the UI remains cohesive and platform-accurate.
