# [Software Engineering Mastery: Systems, Design & Algorithms](https://ankur-glitchtracer.github.io/docs/)

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/release/python-3140/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/badge.svg)](http://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated, professional-grade repository showcasing core software engineering competencies: **Low-Level Design (LLD)**, **High-Level Design (HLD)**, **Distributed Systems**, and **Data Structures & Algorithms (DSA)**.

This repository is built as an interactive engineering handbook, demonstrating a commitment to architectural excellence, clean code, and automated tooling.

---

## 🏗️ Architectural Pillars

- **[Design Patterns](./design_patterns/)**: Production-ready implementations of Creational, Structural, and Behavioral patterns using modern Python `Protocols` and type safety.
- **[Machine Coding & LLD](./machine_coding/)**: End-to-end system implementations (Snake & Ladder, Parking Lot, Elevator) focusing on SOLID principles and extensibility.
- **[Distributed Systems](./infrastructure_challenges/)**: Hands-on challenges covering Rate Limiters, Job Schedulers, and real-time Socket communication.
- **[High-Level Design](./system_design_hld/)**: Comprehensive analysis of industry-scale architectures (Netflix, Uber, S3) and core HLD pillars.
- **[DSA Lab](./dsa/)**: A systematic approach to 150+ algorithms, complete with "Thinking Process" breakdowns and complexity analysis.

---

## 🛠️ Engineering Toolkit

Beyond code implementations, this repository features custom engineering tools to facilitate continuous learning:

### 1. **Interactive Documentation Portal**
Explore the entire repository through a beautifully rendered, searchable documentation portal built with **MkDocs**.
```bash
make serve  # Launches the portal at http://127.0.0.1:8000
```

### 2. **Multi-Language Practice Automation**
A custom utility script (`scripts/clear_solutions.py`) that uses AST-based logic to strip implementations while preserving structure—enabling active-recall practice across **Python, Java, Go, C++, and JS/TS**.
```bash
uv run python scripts/clear_solutions.py
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.14+**
- **[uv](https://github.com/astral-sh/uv)**: A lightning-fast Python package installer and resolver.

### Installation & Quality Checks
1.  **Clone & Sync:**
    ```bash
    git clone https://github.com/Ankur-glitchtracer/docs.git
    cd docs && uv sync
    ```
2.  **Verify Integrity:**
    ```bash
    make lint  # Runs Ruff (Linter) & MyPy (Static Type Checker)
    make test  # Runs Pytest (Unit Testing)
    ```

---

## 📈 Engineering Dashboard
We track technical growth and mastery levels through our [Engineering Mastery Dashboard](./engineering_metrics.md), which logs confidence scores and review schedules for key patterns and systems.

---

## 🔗 Quick Navigation
- [Full Repository Index](./repo_index.md)
- [Learning Path & Roadmap](./index.md)
- [System Design Insights](./system_design_hld/INSIGHTS.md)

---
*Crafted with 🧠 and 🐍 by [Ankur Kumar](https://github.com/Ankur-glitchtracer)*
