import subprocess
from pathlib import Path
import sys

DASHBOARD_FILE = "DOCS_PORTAL.md"

def get_git_last_modified(file_path):
    try:
        # Task 3.3: Use git log to ensure clean YYYY-MM-DD string
        output = subprocess.check_output(
            ["git", "log", "-1", "--format=%as", "--", file_path],
            text=True,
            stderr=subprocess.DEVNULL
        ).strip()
        return output if output else "N/A"
    except Exception:
        return "N/A"

def update_dashboard():
    path = Path(DASHBOARD_FILE)
    if not path.exists():
        print(f"Error: {DASHBOARD_FILE} not found.")
        return

    lines = path.read_text().splitlines()
    new_lines = []
    updated_count = 0

    print(f"Updating {DASHBOARD_FILE}...")

    for line in lines:
        if "|" in line and not line.strip().startswith("|-") and not line.strip().startswith("| Topic"):
            # Task 3.1: Robust Parsing - split by |
            parts = [p.strip() for p in line.split("|")]
            
            if len(parts) >= 6:
                # Table format: | Topic | File Path | Impact | Last Reviewed | Confidence | Next Review |
                # parts[0] is empty (pre-first |)
                # parts[1] is Topic
                # parts[2] is File Path
                # parts[3] is Impact
                # parts[4] is Last Reviewed
                
                raw_path = parts[2].replace("`", "")
                
                # Task 3.4: File Validation
                if raw_path and Path(raw_path).exists():
                    last_modified = get_git_last_modified(raw_path)
                    
                    # Task 3.2: Column Targeting (index 4 for Last Reviewed)
                    if last_modified != "N/A" and last_modified != parts[4]:
                        print(f"Updating {raw_path}: {parts[4]} -> {last_modified}")
                        parts[4] = last_modified
                        updated_count += 1
                
                # Reconstruct line
                line = " | ".join(parts).strip()
                if not line.startswith("|"): line = f"| {line}"
                if not line.endswith("|"): line = f"{line} |"

        new_lines.append(line)

    path.write_text("\n".join(new_lines) + "\n")
    print(f"Dashboard updated successfully. Total files updated: {updated_count}")

if __name__ == "__main__":
    update_dashboard()
