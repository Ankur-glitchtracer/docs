"""
Configuration and templates for the clear_solutions script.
"""

# Mapping of file extensions to their respective "empty" implementations and comment styles
LANGUAGE_CONFIG = {
    ".py": {"clear_to": "    pass\n", "comment": "#"},
    ".java": {"clear_to": "        // TODO: Implement\n        throw new UnsupportedOperationException();\n", "comment": "//"},
    ".cpp": {"clear_to": "    // TODO: Implement\n    throw std::runtime_error(\"Not implemented\");\n", "comment": "//"},
    ".c": {"clear_to": "    // TODO: Implement\n    throw std::runtime_error(\"Not implemented\");\n", "comment": "//"},
    ".cc": {"clear_to": "    // TODO: Implement\n    throw std::runtime_error(\"Not implemented\");\n", "comment": "//"},
    ".js": {"clear_to": "    // TODO: Implement\n    throw new Error(\"Not implemented\");\n", "comment": "//"},
    ".ts": {"clear_to": "    // TODO: Implement\n    throw new Error(\"Not implemented\");\n", "comment": "//"},
    ".go": {"clear_to": "\t// TODO: Implement\n\tpanic(\"not implemented\")\n", "comment": "//"},
}

DASHBOARD_TEMPLATES = {
    "design_patterns.md": """# 🧩 Dashboard: Design Patterns

Track your understanding of core design patterns.

---

## 📊 Summary

| Metric | Value |
|------|------|
| Total Topics | 0 |
| Strong (4–5) | 0 |
| Medium (3) | 0 |
| Weak (≤2) | 0 |

---

## ⏰ Needs Review

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## ✅ Active Topics

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## 📈 Confidence Legend

- **5/5** → Production-ready  
- **4/5** → Strong  
- **3/5** → Comfortable  
- **2/5** → Needs revision  
- **1/5** → Learning  
""",
    "dsa.md": """# 🧩 Dashboard: DSA

Track your understanding of algorithms and data structures.

---

## 📊 Summary

| Metric | Value |
|------|------|
| Total Topics | 0 |
| Strong (4–5) | 0 |
| Medium (3) | 0 |
| Weak (≤2) | 0 |

---

## ⏰ Needs Review

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## ✅ Active Topics

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## 📈 Confidence Legend

- **5/5** → Production-ready  
- **4/5** → Strong  
- **3/5** → Comfortable  
- **2/5** → Needs revision  
- **1/5** → Learning  
""",
    "infrastructure_challenges.md": """# ⚙️ Dashboard: Infrastructure Challenges

Track your expertise in system-level challenges.

---

## 📊 Summary

| Metric | Value |
|------|------|
| Total Topics | 0 |
| Strong (4–5) | 0 |
| Medium (3) | 0 |
| Weak (≤2) | 0 |

---

## ⏰ Needs Review

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## ✅ Active Topics

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## 📈 Confidence Legend

- **5/5** → Production-ready  
- **4/5** → Strong  
- **3/5** → Comfortable  
- **2/5** → Needs revision  
- **1/5** → Learning  
""",
    "machine_coding.md": """# 🏗 Dashboard: Machine Coding

Track your progress in Low-Level Design (LLD).

---

## 📊 Summary

| Metric | Value |
|------|------|
| Total Topics | 0 |
| Strong (4–5) | 0 |
| Medium (3) | 0 |
| Weak (≤2) | 0 |

---

## ⏰ Needs Review

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## ✅ Active Topics

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |

---

## 📈 Confidence Legend

- **5/5** → Production-ready  
- **4/5** → Strong  
- **3/5** → Comfortable  
- **2/5** → Needs revision  
- **1/5** → Learning  
""",
    "engineering_metrics.md": """# 📊 Engineering Mastery Dashboard

This dashboard tracks technical mastery using spaced repetition, confidence scoring, and automated review cycles.

---

## 🔥 Today’s Focus
_(Auto-generated via script: `--today`)_

Run:
```bash
python scripts/update_dashboard.py --today
```

---

## 📂 Category Dashboards

* [DSA](./categories/dsa.md)
* [Design Patterns](./categories/design_patterns.md)
* [Machine Coding](./categories/machine_coding.md)
* [Infrastructure](./categories/infrastructure_challenges.md)

---

## ✅ Active Topics

<!-- ACTIVE_TABLE_START -->
| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!-- ACTIVE_TABLE_END -->

---

## ⏰ Needs Review

*(Auto-managed — do not edit manually)*

<!-- REVIEW_TABLE_START -->
| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!-- REVIEW_TABLE_END -->

---

## 📈 Stats

*(Auto-generated — charts + distribution)*

<!-- STATS_START -->
* Active Topics: 0
* Needs Review: 0
* Weak Areas (≤2): 0
<!-- STATS_END -->

---

## 🧠 How it Works

* **Confidence (1–5)** → Your mastery level
* **Next Review** → Auto-scheduled using spaced repetition
* **Decay** → Confidence decreases if review is missed
* **Impact** → Pulled from `PROBLEM.md` frontmatter
* **NR flag** → Controlled via frontmatter (`nr: true`)

---

## ⚙️ Commands

```bash
# Update dashboard
python scripts/update_dashboard.py

# Preview changes safely
python scripts/update_dashboard.py --dry-run

# Get today's study plan
python scripts/update_dashboard.py --today
```

---

*Confidence Scale: 1 (Learning) → 5 (Production Ready)*
*Use frontmatter (`nr: true`) in PROBLEM.md to disable reminders.*
"""
}
