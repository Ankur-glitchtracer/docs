import subprocess

def create_issue(topics):
    if not topics:
        return

    body = "\n".join([f"- {t}" for t in topics])

    subprocess.run([
        "gh", "issue", "create",
        "--title", "📌 Topics Need Review",
        "--body", body
    ])
