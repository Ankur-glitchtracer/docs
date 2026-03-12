# Python System Design & Interview Preparation

A comprehensive collection of Low-Level Design (LLD) patterns, Machine Coding solutions, Data Structures and Algorithms (DSA), and Distributed System challenges.

This repository is designed to help engineers master software engineering fundamentals through hands-on practice.

## 🚀 Getting Started

### Prerequisites
- **Python 3.14+** (Recommended)
- **[uv](https://github.com/astral-sh/uv)**: A fast Python package installer and resolver.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/python-examples.git
    cd python-examples
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    ```

## 🛠️ How to Use

### 1. Fork for Personal Practice
Fork this repository to your own account to track your progress and customize the solutions.

### 2. Clear Solutions for Practice
If you want to solve the problems yourself without seeing the implementations, use our multi-language utility script:
```bash
uv run python scripts/clear_solutions.py
```
This script recursively processes `dsa/`, `design_patterns/`, and `machine_coding/` to remove implementation logic while preserving structure (functions, classes, and method signatures).

**Supported Languages:**
- **Python**: Replaces bodies with `pass`.
- **Java / C++ / JS / TS**: Replaces bodies with an exception/error throw.
- **Go**: Replaces bodies with a `panic`.

*Tip: You can use `# <solution>` and `# </solution>` markers (or the equivalent comment style for your language) for precise control over what gets cleared.*

### 3. Running the Documentation Portal
We use MkDocs for a beautiful documentation portal.
```bash
make serve
# OR
uv run mkdocs serve
```
Open `http://127.0.0.1:8000` in your browser to explore the roadmap and problem details.

## 🌐 Publishing Your Own Portal
This repository uses the `mkdocs gh-deploy` tool to automatically build and push your documentation to the `gh-pages` branch.

1.  **Go to Repository Settings** > **Pages**.
2.  Set **Build and deployment** > **Source** to "Deploy from a branch".
3.  Under **Branch**, select `gh-pages` and `/ (root)`.
4.  Click **Save**.

On every push to the `main` branch, the GitHub Action will update your `gh-pages` branch, and your portal will be live at `https://<your-username>.github.io/<repo-name>/`.

## 📁 Repository Structure
- `design_patterns/`: Implementation of Creational, Structural, and Behavioral patterns.
- `dsa/`: Curated list of Data Structures and Algorithms problems.
- `machine_coding/`: Real-world system design and implementation (Snake & Ladder, Parking Lot, etc.).
- `infrastructure_challenges/`: Dockerized jobs, Rate Limiters, etc.
- `system_design_hld/`: High-Level Design pillars and architectures.

## ✅ Quality Standards
Ensure your code follows the project's quality standards:
```bash
make lint  # Runs Ruff and MyPy
make test  # Runs Pytest
```

---
Happy Coding! 🚀
