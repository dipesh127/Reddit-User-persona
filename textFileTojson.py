import json
import re

def parse_persona_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    data = {
        "username": None,
        "basic_information": {},
        "traits": [],
        "quote": {},
        "motivations": {},
        "personality": {},
        "behaviour_and_habits": [],
        "frustrations": [],
        "goals_and_needs": []
    }

    section = None

    motivation_numeric_pattern = re.compile(r"^- (.*?): (\d+)/10 \((.*?)\)")
    personality_numeric_pattern = re.compile(r"^- (.*?)-(.*?): (\d+)/10 \((.*?)\)")
    quote_comment_pattern = re.compile(r"\(Comment (\d+)\)")

    for line in lines:
        line = line.strip()

        if line.startswith("Reddit User Persona for u/"):
            data["username"] = line.split("u/")[-1].strip()

        elif line.startswith("👤 BASIC INFORMATION"):
            section = "basic_information"
        elif line.startswith("🔖 TRAITS"):
            section = "traits"
        elif line.startswith("💬 Quote"):
            section = "quote"
        elif line.startswith("📈 MOTIVATIONS"):
            section = "motivations"
        elif line.startswith("🧠 PERSONALITY"):
            section = "personality"
        elif line.startswith("📌 BEHAVIOUR & HABITS"):
            section = "behaviour_and_habits"
        elif line.startswith("💢 FRUSTRATIONS"):
            section = "frustrations"
        elif line.startswith("🎯 GOALS & NEEDS"):
            section = "goals_and_needs"
        elif not line:
            continue
        else:
            if section == "basic_information":
                if line.startswith("- "):
                    key, value = line[2:].split(":", 1)
                    data[section][key.strip().lower().replace(" ", "_")] = value.strip()

            elif section == "traits":
                if line.startswith("- "):
                    data[section].append(line[2:].strip())

            elif section == "quote":
                if line.startswith("\""):
                    data[section]["text"] = line
                    match = quote_comment_pattern.search(line)
                    if match:
                        data[section]["Comment"] = int(match.group(1))
                else:
                    data[section]["description"] = line

            elif section == "motivations":
                match = motivation_numeric_pattern.match(line)
                if match:
                    key = match.group(1).strip().lower().replace(" ", "_")
                    score = int(match.group(2))
                    description = match.group(3).strip()
                    if score >= 8:
                        level = "high"
                    elif score >= 5:
                        level = "medium"
                    else:
                        level = "low"
                    data[section][key] = {
                        "level": level,
                        "score": score,
                        "description": description
                    }

            elif section == "personality":
                match = personality_numeric_pattern.match(line)
                if match:
                    left = match.group(1).strip()
                    right = match.group(2).strip()
                    score = int(match.group(3))
                    description = match.group(4).strip()

                    trait_key = f"{left.lower()}_{right.lower()}".replace(" ", "_")
                    if score < 4:
                        leaning = left
                    elif score > 6:
                        leaning = right
                    else:
                        leaning = "balanced"

                    data[section][trait_key] = {
                        "leaning": leaning,
                        "score": score,
                        "description": description
                    }

            elif section == "behaviour_and_habits":
                if line.startswith("•"):
                    data[section].append(line[1:].strip())

            elif section == "frustrations":
                if line.startswith("•"):
                    data[section].append(line[1:].strip())

            elif section == "goals_and_needs":
                if line.startswith("•"):
                    data[section].append(line[1:].strip())


    return data

