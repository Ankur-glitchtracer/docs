# import subprocess
# from pathlib import Path

# DASHBOARD_FILE = "ENGINEERING_METRICS.md"


# # ==============================
# # GIT HELPERS
# # ==============================

# def get_git_last_modified(file_path):
#     try:
#         output = subprocess.check_output(
#             ["git", "log", "-1", "--format=%as", "--", str(file_path)],
#             text=True,
#             stderr=subprocess.DEVNULL
#         ).strip()
#         return output if output else "N/A"
#     except Exception:
#         return "N/A"


# def get_changed_files():
#     try:
#         output = subprocess.check_output(
#             ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
#             text=True
#         )
#         return set(line.strip() for line in output.splitlines() if line.strip())
#     except Exception:
#         return None


# # ==============================
# # BUILD TOPIC → FILE MAP
# # ==============================

# TARGET_DIRS = [
#     "dsa",
#     "design_patterns",
#     "machine_coding",
#     "infrastructure_challenges"
# ]


# def build_topic_map(root_dir):
#     topic_map = {}

#     for dir_name in TARGET_DIRS:
#         base_path = root_dir / dir_name
#         if not base_path.exists():
#             continue

#         for problem_file in base_path.rglob("PROBLEM.md"):
#             topic = problem_file.parent.name.replace("_", " ").title()
#             topic_map[topic] = problem_file

#     return topic_map


# # ==============================
# # CORE LOGIC
# # ==============================

# def update_dashboard():
#     root_dir = Path(__file__).parent.parent
#     dashboard_path = root_dir / DASHBOARD_FILE

#     if not dashboard_path.exists():
#         print(f"Error: {DASHBOARD_FILE} not found.")
#         return

#     topic_map = build_topic_map(root_dir)
#     changed_files = get_changed_files()

#     lines = dashboard_path.read_text().splitlines()
#     new_lines = []
#     updated_count = 0

#     print("Updating dashboard...")

#     for line in lines:
#         stripped = line.strip()

#         if (
#             "|" in line and
#             not stripped.startswith("|-") and
#             not stripped.startswith("| Topic")
#         ):
#             parts = [p.strip() for p in line.split("|")]

#             # | Topic | Category | Impact | Last Reviewed | Confidence | Next Review |
#             if len(parts) >= 6:
#                 topic_name = parts[1]

#                 if topic_name in topic_map:
#                     file_path = topic_map[topic_name]

#                     # Skip if not changed (optimization)
#                     rel_path = str(file_path.relative_to(root_dir))
#                     if changed_files and rel_path not in changed_files:
#                         new_lines.append(line)
#                         continue

#                     last_modified = get_git_last_modified(file_path)

#                     if last_modified != "N/A" and last_modified != parts[4]:
#                         print(f"{topic_name}: {parts[4]} → {last_modified}")
#                         parts[4] = last_modified
#                         updated_count += 1

#                 # Rebuild row
#                 line = " | ".join(parts).strip()
#                 if not line.startswith("|"):
#                     line = f"| {line}"
#                 if not line.endswith("|"):
#                     line = f"{line} |"

#         new_lines.append(line)

#     new_content = "\n".join(new_lines) + "\n"
#     old_content = dashboard_path.read_text()

#     if new_content != old_content:
#         dashboard_path.write_text(new_content)
#         print(f"Updated {updated_count} entries.")
#     else:
#         print("No updates needed.")


# # ==============================
# # ENTRY
# # ==============================

# if __name__ == "__main__":
#     update_dashboard()
# =================================================================================================


# import argparse
# from pathlib import Path
# from datetime import datetime

# from config import DASHBOARD_FILE, TARGET_DIRS
# from git_utils import get_last_modified
# from parser import normalize, format_topic, extract_frontmatter_impact
# from scheduler import extract_confidence, next_review, decay
# from analytics import generate_chart, weekly_report
# from github_utils import create_issue


# def parse_date(date_str):
#     try:
#         return datetime.strptime(date_str, "%Y-%m-%d")
#     except:
#         return None


# def build_topic_map(root):
#     topic_map = {}
#     for d in TARGET_DIRS:
#         base = root / d
#         if not base.exists():
#             continue

#         for f in base.rglob("PROBLEM.md"):
#             topic = format_topic(f.parent.name)
#             topic_map[topic] = f
#     return topic_map


# def update_dashboard(dry_run=False, no_issues=False, no_chart=False):
#     root = Path(__file__).parent.parent
#     dashboard = root / DASHBOARD_FILE

#     topic_map = build_topic_map(root)
#     today = datetime.now()

#     lines = dashboard.read_text().splitlines()

#     active, review = [], []
#     existing = set()

#     focus_topics = []
#     category_focus = {}

#     updated = added = 0
#     review_topics = []

#     for line in lines:
#         if "|" not in line or line.strip().startswith("|-") or line.startswith("| Topic"):
#             active.append(line)
#             continue

#         parts = [p.strip() for p in line.split("|")]
#         if len(parts) < 6:
#             active.append(line)
#             continue

#         topic = parts[1]
#         norm = normalize(topic)
#         existing.add(norm)

#         for repo_topic, path in topic_map.items():
#             if normalize(repo_topic) != norm:
#                 continue

#             # Extract impact from frontmatter
#             impact = extract_frontmatter_impact(path)
#             parts[3] = impact

#             # Update last reviewed
#             last_mod = get_last_modified(path)
#             if last_mod != parts[4]:
#                 print(f"[UPDATE] {topic}: {parts[4]} → {last_mod}")
#                 parts[4] = last_mod
#                 updated += 1

#             # Confidence
#             conf = extract_confidence(parts[5])
#             nr = "[NR]" in topic

#             # Track weak topics
#             if conf <= 2:
#                 focus_topics.append(topic)
#                 cat = parts[2]
#                 category_focus[cat] = category_focus.get(cat, 0) + 1

#             # Next review
#             next_rev = parse_date(parts[6])
#             if not next_rev:
#                 next_rev = next_review(conf, impact)
#                 parts[6] = next_rev.strftime("%Y-%m-%d")

#             if next_rev < today and not nr:
#                 print(f"[REVIEW] {topic} moved to Needs Review")
#                 conf = decay(conf)
#                 parts[5] = f"{conf}/5"
#                 review.append(parts)
#                 review_topics.append(topic)
#             else:
#                 active.append(parts)

#             break

#     # Add new topics
#     for topic, path in topic_map.items():
#         if normalize(topic) not in existing:
#             impact = extract_frontmatter_impact(path)
#             print(f"[NEW] Adding topic: {topic}")
#             row = ["", topic, "Unknown", impact, "N/A", "0/5", "TBD", ""]
#             active.append(row)
#             added += 1

#     stats = {"Active": len(active), "Review": len(review)}

#     if dry_run:
#         print("\n[DRY-RUN] Skipping chart + GitHub issue creation")
#     else:
#         if not no_chart:
#             generate_chart(stats)
#         else:
#             print("[SKIP] Chart generation disabled")

#         if not no_issues:
#             create_issue(review_topics)
#         else:
#             print("[SKIP] GitHub issues disabled")

#     output = ["# 📊 Engineering Mastery Dashboard\n"]
#     output += ["## ✅ Active Topics\n"]
#     output += [" | ".join(r) if isinstance(r, list) else r for r in active]

#     output += ["\n## ⏰ Needs Review\n"]
#     output += [" | ".join(r) for r in review]

#     output += ["\n## 📈 Stats\n"]
#     output += [f"- Active: {len(active)}", f"- Review: {len(review)}"]
#     output += ["\n![Stats](dashboard_stats.png)"]

#     output += ["\n"]
#     output += weekly_report(updated, added, len(review), focus_topics, category_focus)

#     new_content = "\n".join(output) + "\n"

#     if dry_run:
#         print("\n========== DRY RUN OUTPUT ==========\n")
#         print(new_content[:1000])  # preview first 1000 chars
#         print("\n===================================\n")
#         print(f"[SUMMARY] Updated={updated}, Added={added}, Review={len(review)}")
#         return

#     old_content = dashboard.read_text()
#     if new_content != old_content:
#         dashboard.write_text(new_content)
#         print(f"[DONE] Updated={updated}, Added={added}, Review={len(review)}")
#     else:
#         print("[DONE] No changes")


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--dry-run", action="store_true", help="Run without making changes")
#     parser.add_argument("--no-issues", action="store_true", help="Skip GitHub issue creation")
#     parser.add_argument("--no-chart", action="store_true", help="Skip chart generation")

#     args = parser.parse_args()

#     update_dashboard(
#         dry_run=args.dry_run,
#         no_issues=args.no_issues,
#         no_chart=args.no_chart
#     )

import argparse
from pathlib import Path
from datetime import datetime

from config import DASHBOARD_FILE, CATEGORY_FILES, TARGET_DIRS
from git_utils import get_last_modified
from parser import normalize, format_topic, extract_frontmatter
from scheduler import extract_confidence, next_review, decay
from analytics import generate_chart, weekly_report
from github_utils import create_issue


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

        for f in base.rglob("PROBLEM.md"):
            topic = format_topic(f.parent.name)
            topic_map[topic] = f
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
            lines.append(" | ".join(r))

        content = "\n".join(lines) + "\n"

        if dry_run:
            print(f"[DRY-RUN] Would write {len(rows)} rows to {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"[WRITE] {len(rows)} rows to {path}")


def combine_dashboard_files(dry_run=False):
    combined = ["# 📊 Engineering Mastery Dashboard\n"]

    for cat_file in CATEGORY_FILES.values():
        p = Path(cat_file)
        if p.exists():
            combined += ["\n"] + p.read_text().splitlines()

    content = "\n".join(combined) + "\n"
    out = Path(DASHBOARD_FILE)

    if dry_run:
        print(f"[DRY-RUN] Would write combined dashboard")
    else:
        out.write_text(content)
        print(f"[WRITE] Combined dashboard")


# ==============================
# MAIN ENGINE
# ==============================

def update_dashboard(dry_run=False, no_issues=False, no_chart=False, show_today=False):
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

            for repo_topic, path_md in topic_map.items():
                if normalize(repo_topic) != norm:
                    continue

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

    # Add new topics
    for topic, path_md in topic_map.items():
        if normalize(topic) not in existing:
            meta = extract_frontmatter(path_md)
            impact = meta["impact"]

            print(f"[NEW] {topic}")
            row = ["", topic, "Unknown", impact, "N/A", "0/5", "TBD", ""]
            active.append(row)
            added += 1

    # TODAY PLAN 🔥
    if show_today:
        plan = get_today_plan(active + review)
        print_today_plan(plan)
        return

    stats = {"Active": len(active), "Review": len(review)}

    if dry_run:
        print("[DRY-RUN] Skipping side effects")
    else:
        if not no_chart:
            generate_chart(stats)

        if not no_issues:
            create_issue(review_topics)

    write_category_files(active, review, dry_run=dry_run)
    combine_dashboard_files(dry_run=dry_run)

    report = weekly_report(updated, added, len(review), focus_topics, category_focus)
    print("\n".join(report))


# ==============================
# CLI
# ==============================

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-issues", action="store_true")
    parser.add_argument("--no-chart", action="store_true")
    parser.add_argument("--today", action="store_true", help="Show today's study plan")

    args = parser.parse_args()

    update_dashboard(
        dry_run=args.dry_run,
        no_issues=args.no_issues,
        no_chart=args.no_chart,
        show_today=args.today
    )
