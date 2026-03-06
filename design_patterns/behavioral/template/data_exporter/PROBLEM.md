# 🏗️ Template Method: Universal Data Exporter

## 📝 Overview
The **Template Method** pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps without changing the overall structure. It’s the "recipe" approach to software design.

!!! abstract "Core Concepts"
    - **Invariant vs. Variant Steps:** Keeping common logic (e.g., reading from DB) in the base class and deferring custom logic (e.g., formatting) to subclasses.
    - **Hollywood Principle:** "Don't call us, we'll call you"—the base class controls the execution flow.

## 🚀 Problem Statement
You are building a tool to export data into multiple formats (CSV, PDF, JSON). While the formatting and file writing steps differ for each, the initial data fetching from the database is always the same. Copy-pasting the fetching logic into every exporter class leads to massive code duplication.

### Technical Constraints
- **Algorithm Enforcement:** All exporters must strictly follow the sequence: `Read -> Format -> Write`.
- **Hook Methods:** Provide optional "hooks" (like sending a notification) that subclasses can choose to implement or ignore.

## 🛠️ Requirements
1.  **Abstract Base:** Implement `DataExporter` with the `export()` template method.
2.  **Concrete Primatives:** Subclasses must implement `_format_data()` and `_write_file()`.
3.  **Shared Logic:** The `_read_data()` step should be implemented only once in the base class.
4.  **Concrete Exporters:** Implement `CSVExporter` and `PDFExporter`.

## 💻 Solution Implementation

```python
--8<-- "design_patterns/behavioral/template/data_exporter/data_exporter.py"
```

!!! success "Why this works"
    It maximizes code reuse. By centralizing the invariant parts of the algorithm, you eliminate duplication and ensure that all subclasses follow the same mandatory workflow, making the system predictable and easy to extend.
