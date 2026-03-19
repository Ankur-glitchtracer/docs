import argparse
import re
from pathlib import Path
from datetime import datetime

from config import DASHBOARD_FILE, CATEGORY_FILES, TARGET_DIRS
from git_utils import get_last_modified
from parser import normalize, format_topic, extract_frontmatter
from scheduler import extract_confidence, next_review, decay
try:
    from analytics import generate_chart, weekly_report
except ImportError:
    generate_chart = None
    weekly_report = None

try:
    from github_utils import create_issue
except ImportError:
    create_issue = None


# ==============================
# HELPERS
# ==============================

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None


def build_topic_map(root):
    topic_map = {}
    for d in TARGET_DIRS:
        base = root / d
        if not base.exists():
            continue

        # Map directory name to display category
        category = d.replace("_", " ").title()
        if d == "dsa":
            category = "DSA"
        elif d == "infrastructure_challenges":
            category = "Infra"
        elif d == "design_patterns":
            category = "Design Pattern"
        elif d == "machine_coding":
            category = "LLD System"

        for f in base.rglob("PROBLEM.md"):
            topic = format_topic(f.parent.name)
            topic_map[topic] = {"path": f, "category": category}
    return topic_map


# ==============================
# TODAY ENGINE 🔥
# ==============================

def get_today_plan(all_rows, limit=4):
    today = datetime.now()
    scored = []

    for parts in all_rows:
        if not isinstance(parts, list) or len(parts) < 7:
            continue

        topic = parts[1]
        category = parts[2]
        impact = parts[3]
        conf = extract_confidence(parts[5])
        next_rev = parse_date(parts[6])

        score = 0

        # 1. Overdue (highest priority)
        if next_rev and next_rev < today:
            score += 50

        # 2. Low confidence
        score += (5 - conf) * 10

        # 3. Impact
        if impact.lower() == "high":
            score += 15
        elif impact.lower() == "medium":
            score += 5

        # 4. New topics
        if conf == 0:
            score += 20

        scored.append((score, topic, category, impact, conf))

    scored.sort(reverse=True)

    return scored[:limit]


def print_today_plan(plan):
    print("\n🔥 WHAT TO STUDY TODAY\n")
    for i, (_, topic, category, impact, conf) in enumerate(plan, 1):
        print(f"{i}. {topic} ({category}) | Impact: {impact} | Confidence: {conf}/5")
    print()


# ==============================
# CATEGORY WRITER
# ==============================

def write_category_files(active_rows, review_rows, dry_run=False):
    categories = {}

    for row in active_rows + review_rows:
        if not isinstance(row, list) or len(row) < 3:
            continue
        cat = row[2]
        categories.setdefault(cat, []).append(row)

    for cat, rows in categories.items():
        path = Path(CATEGORY_FILES.get(cat, f"dashboard/categories/{cat.lower()}.md"))

        lines = [f"# {cat} Dashboard\n"]
        lines.append("## ✅ Active Topics\n")
        lines.append("| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

        for r in rows:
            cleaned = [cell.strip() for cell in r if cell.strip() != ""]
            lines.append("| " + " | ".join(cleaned) + " |")

        content = "\n".join(lines) + "\n"

        if dry_run:
            print(f"[DRY-RUN] Would write {len(rows)} rows to {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"[WRITE] {len(rows)} rows to {path}")


def update_section(content, marker_base, new_table):
    """Updates a section between <!-- MARKER_START --> and <!-- MARKER_END -->"""
    start_marker = f"<!-- {marker_base}_START -->"
    end_marker = f"<!-- {marker_base}_END -->"
    
    pattern = re.compile(f"{re.escape(start_marker)}[\\s\\S]*?{re.escape(end_marker)}")
    replacement = f"{start_marker}\n{new_table.strip()}\n{end_marker}"
    return pattern.sub(replacement, content)

def combine_dashboard_files(active_rows, review_rows, dry_run=False):
    """
    Updates the main DASHBOARD_FILE (engineering_metrics.md) using it as a template.
    """
    out_path = Path(DASHBOARD_FILE)
    if not out_path.exists():
        # Fallback to creating a basic one if it doesn't exist
        print(f"[WARN] {DASHBOARD_FILE} not found. Using basic concatenation.")
        combined = ["# 📊 Engineering Mastery Dashboard\n"]
        for cat_file in CATEGORY_FILES.values():
            p = Path(cat_file)
            if p.exists():
                combined += ["\n"] + p.read_text().splitlines()
        content = "\n".join(combined) + "\n"
        if not dry_run:
            out_path.write_text(content)
        return

    content = out_path.read_text(encoding='utf-8')
    
    # Generate tables for main dashboard (limit active topics to top 15 by impact/confidence)
    # Header for tables
    header = "| Topic | Category | Impact | Last Reviewed | Confidence | Next Review |"
    separator = "| :--- | :--- | :--- | :--- | :--- | :--- |"
    
    # For active, let's sort by impact (High first) then confidence (Low first) to show what needs work
    impact_map = {"High": 3, "Medium": 2, "Low": 1, "Unknown": 0}
    sorted_active = sorted(active_rows, key=lambda x: (impact_map.get(x[3], 0), 5 - int(x[5].split('/')[0]) if '/' in x[5] else 5), reverse=True)
    
    active_table = [header, separator]
    for row in sorted_active[:15]: # Show top 15
        active_table.append(f"| {' | '.join(row[1:7])} |")
    
    review_table = [header, separator]
    for row in review_rows[:15]: # Show top 15
        review_table.append(f"| {' | '.join(row[1:7])} |")
        
    # Stats
    weak_areas = len([r for r in active_rows if '/' in r[5] and int(r[5].split('/')[0]) <= 2])
    stats_content = [
        f"* Active Topics: {len(active_rows)}",
        f"* Needs Review: {len(review_rows)}",
        f"* Weak Areas (≤2): {weak_areas}"
    ]
    
    # Update sections
    content = update_section(content, "ACTIVE_TABLE", "\n".join(active_table))
    content = update_section(content, "REVIEW_TABLE", "\n".join(review_table))
    content = update_section(content, "STATS", "\n".join(stats_content))
    
    if dry_run:
        print(f"[DRY-RUN] Would update {DASHBOARD_FILE} sections (Active: {len(active_rows)}, Review: {len(review_rows)})")
    else:
        out_path.write_text(content, encoding='utf-8')
        print(f"[UPDATE] {DASHBOARD_FILE} updated successfully.")
        print(f"[WRITE] Combined dashboard")


# ==============================
# MAIN ENGINE
# ==============================

def update_dashboard(dry_run=False, no_issues=False, no_chart=False, show_today=False, auto_add=False):
    root = Path(__file__).parent.parent
    topic_map = build_topic_map(root)
    today = datetime.now()

    active, review = [], []
    existing = set()

    focus_topics = []
    category_focus = {}

    updated = added = 0
    review_topics = []

    # Read category files
    for cat_file in CATEGORY_FILES.values():
        path = Path(cat_file)
        if not path.exists():
            continue

        lines = path.read_text().splitlines()

        for line in lines:
            if "|" not in line or line.startswith("#") or line.strip().startswith("|-"):
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 7:
                continue

            topic = parts[1]
            norm = normalize(topic)
            existing.add(norm)

            for repo_topic, topic_info in topic_map.items():
                if normalize(repo_topic) != norm:
                    continue

                path_md = topic_info["path"]
                meta = extract_frontmatter(path_md)
                impact = meta["impact"]
                nr = meta["nr"]

                parts[3] = impact

                last_mod = get_last_modified(path_md)
                if last_mod != parts[4]:
                    print(f"[UPDATE] {topic}: {parts[4]} → {last_mod}")
                    parts[4] = last_mod
                    updated += 1

                conf = extract_confidence(parts[5])

                if conf <= 2:
                    focus_topics.append(topic)
                    category_focus[parts[2]] = category_focus.get(parts[2], 0) + 1

                next_rev = parse_date(parts[6])
                if not next_rev:
                    next_rev = next_review(conf, impact)
                    parts[6] = next_rev.strftime("%Y-%m-%d")

                if next_rev < today and not nr:
                    print(f"[REVIEW] {topic}")
                    conf = decay(conf)
                    parts[5] = f"{conf}/5"
                    review.append(parts)
                    review_topics.append(topic)
                else:
                    active.append(parts)

                break

    # Add new topics (Opt-in only)
    if auto_add:
        for topic, topic_info in topic_map.items():
            if normalize(topic) not in existing:
                path_md = topic_info["path"]
                category = topic_info["category"]
                meta = extract_frontmatter(path_md)
                impact = meta["impact"]

                print(f"[NEW] {topic}")
                row = ["", topic, category, impact, "N/A", "0/5", "TBD", ""]
                active.append(row)
                added += 1
    else:
        print("[INFO] Topic auto-discovery skipped. Use --auto-add to enable.")

    # TODAY PLAN 🔥
    if show_today:
        plan = get_today_plan(active + review)
        print_today_plan(plan)
        return

    stats = {"Active": len(active), "Review": len(review)}

    if dry_run:
        print("[DRY-RUN] Skipping side effects")
    else:
        if not no_chart and generate_chart:
            generate_chart(stats)
        elif not generate_chart:
            print("[WARN] Chart generation skipped (matplotlib missing)")

        if not no_issues and create_issue:
            create_issue(review_topics)
        elif not create_issue:
            print("[WARN] GitHub issues skipped (github_utils missing)")

    write_category_files(active, review, dry_run=dry_run)
    combine_dashboard_files(active, review, dry_run=dry_run)

    if weekly_report:
        report = weekly_report(updated, added, len(review), focus_topics, category_focus)
        print("\n".join(report))
    else:
        print("\n[WARN] Weekly report skipped (analytics missing)")


# ==============================
# CLI
# ==============================

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-issues", action="store_true")
    parser.add_argument("--no-chart", action="store_true")
    parser.add_argument("--auto-add", action="store_true", help="Automatically add new topics to dashboard")
    parser.add_argument("--today", action="store_true", help="Show today's study plan")

    args = parser.parse_args()

    update_dashboard(
        dry_run=args.dry_run,
        no_issues=args.no_issues,
        no_chart=args.no_chart,
        show_today=args.today,
        auto_add=args.auto_add
    )
