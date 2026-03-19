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

| Topic             | Category       | Impact | Last Reviewed | Confidence | Next Review |
| :---------------- | :------------- | :----- | :------------ | :--------- | :---------- |
| Singleton         | Design Pattern | High   | 2026-03-07    | 5/5        | 2026-05-07  |
| Abstract Factory  | Design Pattern | High   | 2026-03-07    | 4/5        | 2026-04-07  |
| Builder           | Design Pattern | High   | 2026-03-07    | 4/5        | 2026-04-07  |
| Object Pool       | Design Pattern | High   | 2026-03-07    | 4/5        | 2026-04-07  |
| Observer          | Design Pattern | High   | 2026-03-07    | 5/5        | 2026-05-07  |
| Strategy          | Design Pattern | High   | 2026-03-07    | 4/5        | 2026-04-07  |
| Elevator System   | LLD System     | High   | 2026-03-07    | 3/5        | 2026-03-21  |
| Parking Lot       | LLD System     | High   | 2026-03-07    | 4/5        | 2026-03-21  |
| Job Scheduler     | Distributed    | High   | 2026-03-07    | 3/5        | 2026-03-21  |
| Two Sum           | DSA            | High   | 2026-03-07    | 5/5        | 2026-06-07  |
| Trapping Water    | DSA            | High   | 2026-03-07    | 3/5        | 2026-03-21  |
| Number Of Islands | DSA            | High   | 2026-03-07    | 4/5        | 2026-03-21  |
| Lcs Dp            | DSA            | High   | 2026-03-07    | 3/5        | 2026-03-21  |
| Binary Search     | DSA            | High   | 2026-03-07    | 5/5        | 2026-06-07  |
| Kv Store          | HLD            | High   | 2026-03-07    | 4/5        | 2026-04-07  |
| Redis Rate Limit  | Infra          | High   | 2026-03-07    | 3/5        | 2026-03-21  |

---

## ⏰ Needs Review

*(Auto-managed — do not edit manually)*

| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
| :---- | :------- | :----- | :------------ | :--------- | :---------- |

---

## 📈 Stats

*(Auto-generated — charts + distribution)*

Example:

* Active Topics: X
* Needs Review: Y
* Weak Areas (≤2): Z

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

