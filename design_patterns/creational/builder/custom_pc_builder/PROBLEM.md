# 🖥️ Builder Pattern: High-End Workstation Configurator

## 📝 Overview
The **Builder Pattern** separates the construction of a complex object from its representation. This allows the same construction process to create different representations, which is perfect for assembling a computer with numerous optional components.

!!! abstract "Core Concepts"

    - **Step-by-Step Construction:** Breaking down a massive `__init__` into manageable, semantic methods.
        - **Fluent Interface:** Chaining methods (e.g., `.add_cpu().add_ram()`) for a more readable, Pythonic API.
        - **Object Integrity:** Ensuring the product is fully validated before it is returned to the client.

!!! info "Why Use This Pattern?"

    - **Simplifies complex object creation step-by-step**
    - **Allows different representations of the same product**
    - **Separates construction from representation**


## 🚀 Problem Statement
Creating a `Computer` object via a standard constructor is problematic when there are dozens of optional parts like different CPUs, RAM sizes, GPUs, and cooling systems. This "telescoping constructor" anti-pattern makes the code unreadable and error-prone.

## 🛠️ Requirements

1. Product: A complex Computer object.
2. Builder Interface: Defines steps to build the computer.
3. Validation: Ensure the computer is in a valid state before build returns.

### Technical Constraints

- **Validation:** Prevent the creation of "impossible" PCs (e.g., missing a CPU or insufficient PSU for a high-end GPU).
- **Immutability:** Once `build()` is called, the resulting `Computer` object should be in a final, valid state.

## 🧠 Thinking Process & Approach
Complex objects with many optional parameters lead to 'telescoping constructors'. The approach is to use a step-by-step builder that separates the configuration of the parts from the final assembly. Adding a validation step in `build()` ensures the object is always born in a valid state.

### Key Observations:

- Fluent interface for readable configuration.
- Internal validation before final object return.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/builder/custom_pc_builder/custom_pc_builder.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Abstract Factory](../../abstract_factory/ui_toolkit/PROBLEM.md) — Abstract Factory returns the product immediately; Builder builds it step by step.
- [Composite](../../../structural/composite/organisation_chart/PROBLEM.md) — Builder is often used to build complex Composite trees.
- [Singleton](../../singleton/singleton_pattern/PROBLEM.md) — Builders can be Singletons.
