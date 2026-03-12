# 🔌 Adapter Pattern: Universal Data Translator

## 📝 Overview
The **Adapter Pattern** acts as a bridge between two incompatible interfaces. It allows classes to work together that couldn't otherwise because of differing method signatures or data formats, much like a power adapter converts different plug types.

!!! abstract "Core Concepts"

    - **Interface Wrapping:** Creating a middleman that implements the target interface while delegating to the adaptee.
        - **Non-Invasive Integration:** Connecting legacy or third-party code without modifying its original source.

!!! info "Why Use This Pattern?"

    - **Allows incompatible interfaces to work together**
    - **Promotes reuse of existing classes**
    - **Decouples the client from the implementation of the target**


## 🚀 Problem Statement
Your application expects data in JSON format via a `JsonParser` interface. However, you need to integrate a powerful third-party analytics tool, `XmlAnalytics`, which only provides data in XML. You cannot modify the third-party tool or your existing JSON-based architecture.

## 🛠️ Requirements

1. Target Interface: Interface client expects.
2. Adaptee: Incompatible existing class.
3. Adapter: Translator class.

### Technical Constraints

- **Decoupling:** The client code should remain unaware that it is actually communicating with an XML source.
- **Format Conversion:** The adapter must handle the logic of translating XML structures into JSON strings on the fly.

## 🧠 Thinking Process & Approach
Legacy or 3rd party code often has incompatible interfaces. The approach is to create a translator (Adapter) that wraps the incompatible object and exposes the interface the rest of our application expects.

### Key Observations:

- Interface translation without source modification.
- Seamless integration of third-party libraries.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/adapter/format_translator/format_translator.py"
```

!!! success "Why this works"
    The Adapter provides a bridge between incompatible interfaces, allowing them to work together without modifying their source code. This preserves the Open/Closed Principle.

## 🎤 Interview Follow-ups

- **Scalability Probe:** How would this design hold up under high load?
- **Design Trade-off:** What are the pros/cons of this approach compared to alternatives?

## 🔗 Related Patterns

- [Bridge](../../bridge/remote_control/PROBLEM.md) — Adapter makes things work after they're designed; Bridge makes them work before they are.
- [Decorator](../../decorator/pizza_builder_decorator/PROBLEM.md) — Adapter changes the interface; Decorator adds responsibilities without changing the interface.
- [Proxy](../../proxy/lazy_loading_proxy/PROBLEM.md) — Adapter provides a different interface; Proxy provides the same interface.
- [Facade](../../facade/smart_home_facade/PROBLEM.md) — Adapter wraps one object; Facade wraps many.
