import re
from pathlib import Path

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

def clear_solution_content(file_path):
    """
    Clears implementation details while keeping structure.
    Uses markers if available, otherwise attempts language-specific block clearing.
    """
    ext = file_path.suffix.lower()
    if ext not in LANGUAGE_CONFIG:
        return

    config = LANGUAGE_CONFIG[ext]
    clear_to = config["clear_to"]
    comment = config["comment"]

    with open(file_path, 'r') as f:
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
                        # Simple check: if it has common keywords or looks like a method
                        if any(k in line for k in ["func", "public", "private", "class", "function", "void", "int", "string"]):
                            # We found the start of a block we want to clear
                            # But we want to keep the signature, so we just append the 'clear_to' after this line
                            # and skip lines until the matching closing brace.
                            new_lines.append(clear_to)
                            in_solution = True
                            brace_count = 1
                else:
                    brace_count += line.count("{")
                    brace_count -= line.count("}")
                    if brace_count <= 0:
                        in_solution = False
                        new_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(new_lines)

def main():
    target_dirs = ['dsa', 'design_patterns', 'machine_coding', 'infrastructure_challenges']
    root_dir = Path(__file__).parent.parent
    
    extensions = tuple(LANGUAGE_CONFIG.keys())
    
    for dir_name in target_dirs:
        dir_path = root_dir / dir_name
        if not dir_path.exists():
            continue
            
        print(f"Processing directory: {dir_name}")
        for ext in extensions:
            for file_path in dir_path.rglob(f'*{ext}'):
                if file_path.name.startswith('test_') or file_path.name.endswith('_test.py'):
                    continue
                print(f"  Clearing solutions in: {file_path.relative_to(root_dir)}")
                clear_solution_content(file_path)

if __name__ == "__main__":
    main()
