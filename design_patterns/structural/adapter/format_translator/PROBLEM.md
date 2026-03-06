# 🔌 Adapter Pattern: Universal Data Translator

## 📝 Overview
The **Adapter Pattern** acts as a bridge between two incompatible interfaces. It allows classes to work together that couldn't otherwise because of differing method signatures or data formats, much like a power adapter converts different plug types.

!!! abstract "Core Concepts"
    - **Interface Wrapping:** Creating a middleman that implements the target interface while delegating to the adaptee.
    - **Non-Invasive Integration:** Connecting legacy or third-party code without modifying its original source.

## 🚀 Problem Statement
Your application expects data in JSON format via a `JsonParser` interface. However, you need to integrate a powerful third-party analytics tool, `XmlAnalytics`, which only provides data in XML. You cannot modify the third-party tool or your existing JSON-based architecture.

## 🧠 Thinking Process & Approach
Legacy or 3rd party code often has incompatible interfaces. The approach is to create a translator (Adapter) that wraps the incompatible object and exposes the interface the rest of our application expects.

### Key Observations:
- Interface translation without source modification.
- Seamless integration of third-party libraries.

### Technical Constraints
- **Decoupling:** The client code should remain unaware that it is actually communicating with an XML source.
- **Format Conversion:** The adapter must handle the logic of translating XML structures into JSON strings on the fly.

## 🛠️ Requirements
1. Target Interface: Interface client expects.
2. Adaptee: Incompatible existing class.
3. Adapter: Translator class.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/structural/adapter/format_translator/format_translator.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.
