from openai import OpenAI
from config import OPENAI_API_KEY
from config import GROQ_API_KEY

# OpenAI
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Groq (FREE)
groq_client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def fallback_ideas(trends):
    ideas = []

    for trend in trends:
        idea = f"""
Trend Focus: {trend}

- Create a simple landing page targeting '{trend}'
- Offer a free checklist or guide related to it
- Monetize with subscription (weekly tips, plans, tools)
- Run ads targeting people searching for '{trend}'
"""
        ideas.append(idea)

    return "\n\n".join(ideas)

def generate_ideas(trends):
    prompt = f"""
You are a growth strategist for a fast-scaling health and wellness company.

Based on the following trending topics, generate:

1. 3 digital product ideas
2. 3 high-converting content hooks
3. 1 subscription-based monetization idea

Trends:
{trends}

Keep it concise, practical, and execution-focused.
""" 
    
    # first try OpenAI
    print("\t-- Trying OpenAI...")
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print("\t-- OpenAI failed!", e)
        print("\t-- Switching to Groq...")

    # try Groq
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    except Exception as e:
        print("\t-- Groq failed!", e)
        print("\t-- Using fallback...")
    
    # Use fallback
    return fallback_ideas(trends)

    