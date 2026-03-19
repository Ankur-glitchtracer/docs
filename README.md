# [Software Engineering Mastery: Systems, Design & Algorithms](https://ankur-glitchtracer.github.io/docs/)

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/release/python-3140/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated, professional-grade repository showcasing core software engineering competencies: **Low-Level Design (LLD)**, **High-Level Design (HLD)**, **Distributed Systems**, and **Data Structures & Algorithms (DSA)**.

This repository is built as an interactive engineering handbook, demonstrating a commitment to architectural excellence, clean code, and automated tooling.

---

## 🏗️ Architectural Pillars

* **[Design Patterns](./design_patterns/)**: Production-ready implementations of Creational, Structural, and Behavioral patterns using modern Python `Protocols` and type safety.
* **[Machine Coding & LLD](./machine_coding/)**: End-to-end system implementations (Snake & Ladder, Parking Lot, Elevator) focusing on SOLID principles and extensibility.
* **[Distributed Systems](./infrastructure_challenges/)**: Hands-on challenges covering Rate Limiters, Job Schedulers, and real-time Socket communication.
* **[High-Level Design](./system_design_hld/)**: Comprehensive analysis of industry-scale architectures (Netflix, Uber, S3) and core HLD pillars.
* **[DSA Lab](./dsa/)**: A systematic approach to 150+ algorithms, complete with "Thinking Process" breakdowns and complexity analysis.

---

# 🚀 Deploy to GitHub Pages

This project is set up to automatically build and publish a documentation site using **MkDocs** and GitHub Pages.
You can deploy your site in just a few clicks.

---

## ⚡ Quick Start (Recommended)

### 1. 🍴 Fork the Repository

Click the **Fork** button to create your own copy of this repository.

---

### 2. ⚙️ Enable GitHub Pages

Go to **Settings → Pages** and select **GitHub Actions** as the source.

---

### 3. ▶️ Run the Deployment

Go to the **Actions** tab:

* Select **Deploy to GitHub Pages**
* Click **Run workflow**

---

### 4. ⏳ Wait for Deployment

* The workflow will build and deploy your site
* Usually takes 1–2 minutes

---

### 5. 🌐 View Your Website

```bash
https://<your-username>.github.io/<repository-name>/
```

---

## 🔁 Automatic Deployment

Every time you push changes to the `main` branch, your site will automatically update.

---

## 📁 Project Structure

```bash
mkdocs.yml
docs/
```

Example:

```bash
docs/
  index.md
  interview_playbook.md
mkdocs.yml
```

---

## 🧠 How It Works

```text
Your content (docs/)
        │
        ▼
MkDocs builds static site
        │
        ▼
GitHub Actions deploys it
        │
        ▼
Live website on GitHub Pages 🌍
```

---

## ⚠️ Troubleshooting

```text
❌ Site not showing up
- Wait a minute and refresh
- Double-check: Settings → Pages → Source = GitHub Actions

❌ Deployment failed
- Go to Actions tab and click failed workflow
- Common causes:
    * Missing mkdocs.yml
    * Missing docs/ folder
    * YAML formatting issues

❌ Workflow not running
- Ensure GitHub Actions are enabled
- Try running workflow manually from Actions tab
```

---

## 💡 Tips

```text
- No local installs needed
- No branches need to be created manually
- Just edit, commit, and your site updates automatically
```

---

## 🎉 You're Done!

Your documentation site is now live and will update automatically with every change.
Happy building! 🚀

---

## 📊 Engineering Dashboard System

This repository includes an automated system that tracks your learning progress and maintains a structured **engineering dashboard**, updated automatically via GitHub Actions.

---

## 🧠 What This System Does

```text
- Tracks all topics from PROBLEM.md files
- Monitors last update for each topic
- Assigns and updates confidence levels (0–5)
- Schedules next review dates
- Detects overdue topics
- Generates a prioritized "What to Study Today" plan
- Updates category dashboards
- Optionally creates GitHub Issues for review topics
```

---

## 📁 Where Things Live

```text
- Topics source: TARGET_DIRS folders
- Per-topic file: PROBLEM.md
- Main dashboard: docs/dashboard/engineering_metrics.md
- Category dashboards: docs/dashboard/categories/*.md
```

---

## ⚙️ How It Works

```text
1. Scans all topic folders
2. Extracts metadata (impact, review flags, etc.)
3. Updates:
    - Last modified date
    - Confidence score
    - Next review date
4. Moves topics into:
    - ✅ Active
    - 🔁 Review (if overdue)
5. Writes updated dashboards
6. Optionally:
    - 📊 Generates charts
    - 📝 Creates GitHub Issues
```

---

## ⏰ When It Runs

This workflow runs automatically via GitHub Actions:

```text
- On every push to main
- Daily at 03:00 UTC (scheduled)
```

---

## 🔥 “What to Study Today”

```bash
python scripts/update_dashboard.py --today
```

---

## 🧪 Run Locally (Optional)

```bash
python scripts/update_dashboard.py --dry-run
```

Options:

```text
--no-issues → skip GitHub issue creation
--no-chart → skip chart generation
```

---

## 📝 Topic Format (Important)

```text
<topic-name>/
  PROBLEM.md
```

Frontmatter example:

```yaml
impact: high
nr: false
```

---

## 🔁 Review Logic

```text
- Topics scheduled based on confidence and impact
- Overdue topics:
    - Confidence decays
    - Moved to Review section
    - May trigger GitHub Issue
```

---

## ⚠️ Important Notes

```text
- Do not manually edit generated files:
    - docs/dashboard/engineering_metrics.md
    - docs/dashboard/categories/*.md
- Files are automatically overwritten
```

---

## 🛠 Troubleshooting

```text
❌ Dashboard not updating
- Check Actions tab
- Ensure scripts/update_dashboard.py exists
- Ensure all modules (config, parser, etc.) are present

❌ No new topics detected
- Ensure each topic has a PROBLEM.md file
- Proper naming and folder structure

❌ GitHub Issues not created
- Check workflow permissions: issues: write
```

---

## 🎯 Summary

```text
- Tracks your learning progress
- Identifies what you’re forgetting
- Tells you what to study next
- Fully automated
```

---

## 🛠️ Engineering Toolkit

### 1. Interactive Documentation Portal

```bash
make serve  # Launches the portal at http://127.0.0.1:8000
```

### 2. Multi-Language Practice Automation

A custom utility script (`scripts/clear_solutions.py`) that uses AST-based logic to strip implementations while preserving structure—enabling active-recall practice across **Python, Java, Go, C++, and JS/TS**.

You can trigger this automatically from the GitHub **Actions** tab by running the **Clear Solutions and Reset Dashboards** workflow, or run it locally:

```bash
uv run python scripts/clear_solutions.py
```

---

## 🚀 Getting Started

### Prerequisites

```text
- Python 3.14+
- uv: Python package installer
```

### Installation & Quality Checks

```bash
git clone https://github.com/Ankur-glitchtracer/docs.git
cd docs && uv sync
make lint  # Runs Ruff & MyPy
make test  # Runs Pytest
```

---

## 📈 Engineering Dashboard

Tracks technical growth via the [Engineering Mastery Dashboard](./docs/dashboard/engineering_metrics.md).

---

## 🔗 Quick Navigation

```text
- Full Repository Index: ./REPO_INDEX.md
- Learning Path & Roadmap: ./LEARNING_PATH.md
- System Design Insights: ./system_design_hld/INSIGHTS.md
```

---

*Crafted with 🧠 and 🐍 by [Ankur Kumar](https://github.com/Ankur-glitchtracer)*
