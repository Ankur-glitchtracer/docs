# 📊 Engineering Mastery Dashboard

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

