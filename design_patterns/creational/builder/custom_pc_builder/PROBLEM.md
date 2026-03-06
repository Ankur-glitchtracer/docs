# 🖥️ Builder Pattern: High-End Workstation Configurator

## 📝 Overview
The **Builder Pattern** separates the construction of a complex object from its representation. This allows the same construction process to create different representations, which is perfect for assembling a computer with numerous optional components.

!!! abstract "Core Concepts"
    - **Step-by-Step Construction:** Breaking down a massive `__init__` into manageable, semantic methods.
    - **Fluent Interface:** Chaining methods (e.g., `.add_cpu().add_ram()`) for a more readable, Pythonic API.
    - **Object Integrity:** Ensuring the product is fully validated before it is returned to the client.

## 🚀 Problem Statement
Creating a `Computer` object via a standard constructor is problematic when there are dozens of optional parts like different CPUs, RAM sizes, GPUs, and cooling systems. This "telescoping constructor" anti-pattern makes the code unreadable and error-prone.

## 🧠 Thinking Process & Approach
Complex objects with many optional parameters lead to 'telescoping constructors'. The approach is to use a step-by-step builder that separates the configuration of the parts from the final assembly. Adding a validation step in `build()` ensures the object is always born in a valid state.

### Key Observations:
- Fluent interface for readable configuration.
- Internal validation before final object return.

### Technical Constraints
- **Validation:** Prevent the creation of "impossible" PCs (e.g., missing a CPU or insufficient PSU for a high-end GPU).
- **Immutability:** Once `build()` is called, the resulting `Computer` object should be in a final, valid state.

