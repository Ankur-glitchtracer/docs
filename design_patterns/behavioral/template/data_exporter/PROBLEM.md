# 🏗️ Template Method: Universal Data Exporter

## 📝 Overview
The **Template Method** pattern defines the skeleton of an algorithm in a base class but lets subclasses override specific steps without changing the overall structure. It’s the "recipe" approach to software design.

!!! abstract "Core Concepts"
    - **Invariant vs. Variant Steps:** Keeping common logic (e.g., reading from DB) in the base class and deferring custom logic (e.g., formatting) to subclasses.
    - **Hollywood Principle:** "Don't call us, we'll call you"—the base class controls the execution flow.

## 🚀 Problem Statement
You are building a tool to export data into multiple formats (CSV, PDF, JSON). While the formatting and file writing steps differ for each, the initial data fetching from the database is always the same. Copy-pasting the fetching logic into every exporter class leads to massive code duplication.

## 🧠 Thinking Process & Approach
When multiple algorithms share a high-level sequence but differ in details, we use a template method. The base class defines the mandatory 'skeleton', while subclasses fill in the specific primitive operations.

### Key Observations:
- Invariant steps in base class.
- Variant hooks in subclasses.

### Technical Constraints
- **Algorithm Enforcement:** All exporters must strictly follow the sequence: `Read -> Format -> Write`.
- **Hook Methods:** Provide optional "hooks" (like sending a notification) that subclasses can choose to implement or ignore.

