from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_intent(user_input):
    try:
        prompt = f"""
Classify the user request into one of:
- diploma
- legal_question
- marriage
- unknown

Request: {user_input}

Answer only the category.No extra words.
"""
    
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user", "content": prompt}]
        )

        intent = response.choices[0].message.content.strip().lower()
        intent = intent.rstrip(".,;!?")
    
        allowed_intents = ["diploma", "legal_question", "marriage", "unknown"]

        if intent not in allowed_intents:
            intent = "unknown"

        return intent

    except Exception as e:
        print("Error in detect_intent:",e)
        return "unknown"
        