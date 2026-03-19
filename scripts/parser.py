def normalize(name):
    return name.lower().replace(" ", "").replace("_", "")

def format_topic(name):
    return name.replace("_", " ").title()

def extract_frontmatter(file_path):
    data = {
        "impact": "Medium",
        "nr": False
    }

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        if not lines or lines[0].strip() != "---":
            return data

        for line in lines[1:]:
            line = line.strip()
            if line == "---":
                break

            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()

            if key == "impact":
                data["impact"] = value.title()

            elif key == "nr":
                data["nr"] = value.lower() == "true"

    except:
        pass

    return data
