from services.knowledge_base import retrieve_info
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_legal_question(user_input: str):
    try:
        # Step 1: retrieve context
        context = retrieve_info(user_input)

        # Step 2: build prompt
        prompt = f"""
You are a legal assistant.

Use the context below to answer the question clearly and simply.

Context:
{context}

Question:
{user_input}

Add a disclaimer to check official sources.
"""

        # Step 3: call OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        # Step 4: return structured response
        return {
            "service": "legal_info",
            "message": response.choices[0].message.content,
            "source": "RAG"
        }

    except Exception as e:
        print("Error in legal agent:", e)
        return {
            "service": "legal_info",
            "message": "Sorry, I couldn't process your request right now.",
            "source": "error"
        }