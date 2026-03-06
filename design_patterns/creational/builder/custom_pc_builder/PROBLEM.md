# 🖥️ Builder Pattern: High-End Workstation Configurator

## 📝 Overview
The **Builder Pattern** separates the construction of a complex object from its representation. This allows the same construction process to create different representations, which is perfect for assembling a computer with numerous optional components.

!!! abstract "Core Concepts"
    - **Step-by-Step Construction:** Breaking down a massive `__init__` into manageable, semantic methods.
    - **Fluent Interface:** Chaining methods (e.g., `.add_cpu().add_ram()`) for a more readable, Pythonic API.
    - **Object Integrity:** Ensuring the product is fully validated before it is returned to the client.

## 🚀 Problem Statement
Creating a `Computer` object via a standard constructor is problematic when there are dozens of optional parts like different CPUs, RAM sizes, GPUs, and cooling systems. This "telescoping constructor" anti-pattern makes the code unreadable and error-prone.

### Technical Constraints
- **Validation:** Prevent the creation of "impossible" PCs (e.g., missing a CPU or insufficient PSU for a high-end GPU).
- **Immutability:** Once `build()` is called, the resulting `Computer` object should be in a final, valid state.

## 🛠️ Requirements
1.  **Complex Product:** A `Computer` class with multiple optional attributes.
2.  **Builder Interface:** An abstract base class defining steps like `add_memory()` and `add_gpu()`.
3.  **Director or Fluent API:** Implement a mechanism to execute a specific "recipe" (e.g., Gaming PC vs. Office PC).
4.  **Build Validation:** Perform integrity checks within the `build()` method.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/creational/builder/custom_pc_builder/custom_pc_builder.py"
```

!!! success "Why this works"
    It provides fine-grained control over the construction process. By isolating the complex assembly logic, the `Computer` class remains simple, while the `Builder` ensures that only valid, "healthy" objects are ever instantiated.
