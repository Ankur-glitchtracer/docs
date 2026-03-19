import argparse
import logging
import re
from pathlib import Path

from config import DASHBOARD_FILE
from config.cleanup_templates import LANGUAGE_CONFIG, DASHBOARD_TEMPLATES

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def clear_solution_content(file_path, dry_run=False):
    """
    Clears implementation details while keeping structure.
    Uses markers if available, otherwise attempts language-specific block clearing.
    """
    ext = file_path.suffix.lower()
    if ext not in LANGUAGE_CONFIG:
        return False

    config = LANGUAGE_CONFIG[ext]
    clear_to = config["clear_to"]
    comment = config["comment"]

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_solution = False
    
    content = "".join(lines)
    # Check for markers: <solution> and </solution>
    start_marker = f"{comment} <solution>"
    end_marker = f"{comment} </solution>"
    has_markers = start_marker in content and end_marker in content

    if has_markers:
        for line in lines:
            if start_marker in line:
                new_lines.append(line)
                new_lines.append(clear_to)
                in_solution = True
            elif end_marker in line:
                new_lines.append(line)
                in_solution = False
            elif not in_solution:
                new_lines.append(line)
    else:
        # Language-specific heuristics for clearing bodies without markers
        if ext == ".py":
            for line in lines:
                if re.match(r'^\s*(def|class)\s+\w+.*:', line):
                    new_lines.append(line)
                    new_lines.append(clear_to)
                    in_solution = True
                elif in_solution:
                    if line.strip() and not line.startswith((" ", "\t", "#")):
                        in_solution = False
                        new_lines.append(line)
                else:
                    new_lines.append(line)
        else:
            # For brace-based languages (Java, C++, JS, TS, Go)
            brace_count = 0
            for line in lines:
                if not in_solution:
                    new_lines.append(line)
                    # Heuristic: Find a line that looks like a function/method signature and starts a block
                    if "{" in line and not line.strip().startswith(comment):
                        # Enhanced keywords for TS/JS as well as others
                        if any(k in line for k in ["func", "public", "private", "class", "function", "void", "int", "string", "const", "let", "export"]):
                            new_lines.append(clear_to)
                            in_solution = True
                            brace_count = line.count("{") - line.count("}")
                            if brace_count <= 0:
                                in_solution = False
                            else:
                                brace_count = 1
                else:
                    brace_count += line.count("{")
                    brace_count -= line.count("}")
                    if brace_count <= 0:
                        in_solution = False
                        new_lines.append(line)

    if content != "".join(new_lines):
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
        return True
    return False

def clear_problem_md_content(file_path, dry_run=False):
    """
    Clears code implementation blocks in PROBLEM.md files.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the Solution Implementation section, optional existing HTML comment, and the code block
    pattern = re.compile(r"(##\s*💻\s*Solution Implementation\s*\n+)(?:<!-- Solution path: (.*?) -->\n)?(```[a-zA-Z0-9+#]*\n)([\s\S]*?)(\n```)", re.IGNORECASE)
    
    def replacer(match):
        header = match.group(1)
        existing_path = match.group(2)
        code_tag = match.group(3)
        inner_content = match.group(4)
        end_tag = match.group(5)
        
        # Try to find a snippet path in the inner content if not already stored
        snippet_match = re.search(r'--8<--\s+"([^"]+)"', inner_content)
        path = existing_path
        if snippet_match:
            path = snippet_match.group(1)
            
        replacement_inner = "(Implementation details need to be added...)"
        
        if path:
            return f"{header}<!-- Solution path: {path} -->\n{code_tag}{replacement_inner}{end_tag}"
        else:
            return f"{header}{code_tag}{replacement_inner}{end_tag}"

    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        return True
    return False

def reset_dashboards(root_dir, dry_run=False):
    dashboard_dir = root_dir / 'docs' / 'dashboard' / 'categories'
    
    reset_count = 0
    
    # 1. Reset category dashboards
    for name, content in DASHBOARD_TEMPLATES.items():
        if name == "engineering_metrics.md":
            continue
        file_path = dashboard_dir / name
        if not dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding='utf-8')
        logger.debug(f"Reset {name} to default.")
        reset_count += 1
        
    # 2. Reset main dashboard
    main_dashboard = root_dir / DASHBOARD_FILE
    if "engineering_metrics.md" in DASHBOARD_TEMPLATES:
        content = DASHBOARD_TEMPLATES["engineering_metrics.md"]
        if not dry_run:
            main_dashboard.parent.mkdir(parents=True, exist_ok=True)
            main_dashboard.write_text(content, encoding='utf-8')
        logger.debug(f"Reset {DASHBOARD_FILE} to default.")
        reset_count += 1
        
    return reset_count

def main():
    parser = argparse.ArgumentParser(description="Reset repository to a learning state by clearing solutions and dashboards.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without modifying files.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    parser.add_argument("--target", type=str, help="Specific directory or file to process (optional).")
    
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.dry_run:
        logger.info("[DRY RUN] No files will be modified.")

    root_dir = Path(__file__).parent.parent
    
    if args.target:
        target_path = root_dir / args.target
        target_dirs = [target_path.name] if target_path.is_dir() else []
        if target_path.is_file():
            # Process single file
            if target_path.name == 'PROBLEM.md':
                if clear_problem_md_content(target_path, args.dry_run):
                    logger.info(f"Cleared documentation in: {target_path.relative_to(root_dir)}")
            else:
                if clear_solution_content(target_path, args.dry_run):
                    logger.info(f"Cleared code in: {target_path.relative_to(root_dir)}")
            return
    else:
        target_dirs = ['dsa', 'design_patterns', 'machine_coding', 'infrastructure_challenges']

    # Reset dashboards
    dashboard_count = reset_dashboards(root_dir, args.dry_run)
    logger.info(f"Reset {dashboard_count} dashboards.")
    
    extensions = tuple(LANGUAGE_CONFIG.keys())
    
    docs_cleared = 0
    code_cleared = 0

    for dir_name in target_dirs:
        dir_path = root_dir / dir_name
        if not dir_path.exists() or not dir_path.is_dir():
            continue
            
        logger.debug(f"Processing directory: {dir_name}")
        
        # Process PROBLEM.md files in all target directories
        for file_path in dir_path.rglob('PROBLEM.md'):
            if clear_problem_md_content(file_path, args.dry_run):
                logger.info(f"Cleared solution doc in: {file_path.relative_to(root_dir)}")
                docs_cleared += 1

        # Process source code files
        for ext in extensions:
            for file_path in dir_path.rglob(f'*{ext}'):
                if file_path.name.startswith('test_') or file_path.name.endswith('_test.py') or file_path.parent.name == 'config':
                    continue
                if clear_solution_content(file_path, args.dry_run):
                    logger.info(f"Cleared code in: {file_path.relative_to(root_dir)}")
                    code_cleared += 1

    logger.info(f"Summary: Cleared {code_cleared} source files, {docs_cleared} documentation files, and reset {dashboard_count} dashboards.")

if __name__ == "__main__":
    main()
