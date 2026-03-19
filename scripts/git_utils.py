import subprocess

def get_last_modified(file_path):
    try:
        output = subprocess.check_output(
            ["git", "log", "-1", "--format=%as", "--", str(file_path)],
            text=True
        ).strip()
        return output or "N/A"
    except:
        return "N/A"
