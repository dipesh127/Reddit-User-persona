# main.py
import sys
import os
from reddit_scraper import get_user_data
from persona_builder import generate_persona
from textFileTojson import parse_persona_file
import json
from jinja2 import Template

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_username>")
        return
    if sys.argv[1].startswith("https://www.reddit.com/user/"):
        username=(sys.argv[1]).split("/")[4]
    else:
        username = sys.argv[1]
    print(f"Fetching data for u/{username}...")

    data = get_user_data(username)

    print("Generating persona using AI...")
    persona_text = generate_persona(username, data)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)
        
    persona_json=parse_persona_file(f"{output_dir}/{username}_persona.txt")
    # Save as JSON
    with open(f"jsonData/{username}.json", "w", encoding="utf-8") as f:
        json.dump(persona_json, f, indent=2, ensure_ascii=False)

    with open(f"jsonData/{username}.json") as f:
        json_data = json.load(f)
    
    
    # Render the persona template for the reddit user
    with open("./template/persona_template.html") as f:
        template = Template(f.read())

    rendered = template.render(**json_data)

    with open(f"HtmlOutput/{username}.html", "w") as f:
        f.write(rendered)

    print(f"Persona saved to {output_dir}/{username}_persona.txt")
    print(f"Persona Html format saved to {output_dir}/{username}.html")
if __name__ == "__main__":
    main()
