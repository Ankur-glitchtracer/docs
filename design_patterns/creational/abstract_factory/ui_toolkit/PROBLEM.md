# 🎨 Abstract Factory: Cross-Platform UI Kit

## 📝 Overview
The **Abstract Factory** provides an interface for creating families of related or dependent objects without specifying their concrete classes. This is essential for maintaining visual consistency across different Operating Systems (e.g., Windows vs. macOS).

!!! abstract "Core Concepts"
    - **Product Families:** Ensuring that all components (Buttons, Sliders) belong to the same theme.
    - **Theme Isolation:** The client code remains agnostic of the specific UI theme being rendered.

## 🚀 Problem Statement
You are building a cross-platform UI toolkit. A major constraint is that you must never mix themes: a macOS button should never appear in a Windows-themed window. Hardcoding theme checks throughout the UI logic leads to a maintenance nightmare.

## 🧠 Thinking Process & Approach
When we have families of related products (like Windows vs Mac buttons), we need a way to enforce consistency. The approach is to create a 'Factory of Factories' where each concrete factory is responsible for an entire theme, preventing the mixing of incompatible UI components.

### Key Observations:
- Dependency Injection of the factory into the client.
- Strict interface adherence for all product types.

### Technical Constraints
- **Consistency:** The factory must guarantee that all returned products are compatible with each other.
- **Open/Closed Principle:** Switching the entire app's look and feel should ideally require changing only a single line of code.

