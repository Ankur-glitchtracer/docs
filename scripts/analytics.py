import matplotlib.pyplot as plt
from pathlib import Path

def generate_chart(stats):
    labels = list(stats.keys())
    values = list(stats.values())

    # Skip if no data or all zeros to prevent ValueError in matplotlib.pyplot.pie
    if not values or all(v == 0 for v in values):
        print("[INFO] No data to plot, skipping chart generation.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Topic Distribution")

    # Save to docs/dashboard/
    output_path = Path("docs/dashboard/dashboard_stats.png")
    output_path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
    plt.savefig(output_path)
    plt.close()


def weekly_report(updated, added, review_count, focus_topics, category_focus):
    lines = []
    lines.append("## 🗓 Weekly Review Report\n")

    lines.append(f"- Topics Updated: {updated}")
    lines.append(f"- New Topics Added: {added}")
    lines.append(f"- Needs Review: {review_count}\n")

    lines.append("### 🎯 Focus Areas")
    for cat, count in sorted(category_focus.items(), key=lambda x: -x[1]):
        lines.append(f"- {cat}: {count} weak topics")

    lines.append("\n### 🔥 Priority Topics")
    for t in focus_topics[:10]:
        lines.append(f"- {t}")

    return lines
