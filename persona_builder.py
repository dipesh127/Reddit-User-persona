# persona_builder.py
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_persona(username, data):
    content_blocks = []

    for i, c in enumerate(data["comments"], 1):
        content_blocks.append(f"Comment {i}: {c['body']}\nLink: {c['permalink']}")

    for i, p in enumerate(data["posts"], 1):
        body = p['body'] if p['body'] else ""
        content_blocks.append(f"Post {i}: {p['title']}\n{body}\nLink: {p['permalink']}")

    context = "\n\n".join(content_blocks[:50])  # Limit content size

    prompt = f"""
You are an AI tasked with building a detailed Reddit User Persona based on the user's activity.

Use the following format:
Reddit User Persona for u/{username}


👤 BASIC INFORMATION
- Age:
- Occupation:
- Status:
- Location:
- Tier:
- Archetype:

🔖 TRAITS
- Practical | Adaptable | Spontaneous | Active

💬 Quote:
"A quote that represents this user's personality or goals."

📈 MOTIVATIONS(For each motivation, show the level on a scale of 10. Also display the numeric rating as (x/10).)
- Convenience: 
- Wellness: 
- Speed:   
- Preferences: 
- Comfort:
- Dietary Needs: 

🧠 PERSONALITY(For each personality trait pair, show the level on a scale of 10 . Also display the numeric rating as (x/10).)
Introvert  - Extrovert 
Intuition  - Sensing 
Feeling    - Thinking  
Perceiving - Judging  

📌 BEHAVIOUR & HABITS
• Bullet list of habits or online behaviors derived from their posts/comments.  
• Include citations like: (Comment: <permalink>) or (Post: <permalink>)

💢 FRUSTRATIONS
• What frustrates or bothers this user?  
• Include citations from specific Reddit content.

🎯 GOALS & NEEDS
• What are the user's goals, wants, or needs based on their online behavior?  
• Use citations where possible.

---
Reddit Content:
{context}
"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # Groq's best free model
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Failed to generate persona due to error: {e}"
