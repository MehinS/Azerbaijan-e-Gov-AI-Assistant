from services.knowledge_base import retrieve_info
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def format_context(results):
    context_text = ""
    for item in results:
        context_text += f"Topic: {item["topic"]}\n"
        context_text += f"Content: {item["content"]}\n\n"
    return context_text.strip()

def handle_legal_question(user_input: str):
    try:
        # Step 1: retrieve context
        results = retrieve_info(user_input)

        if not results:
            return {
                "service": "legal_info",
                "message": "Bu mövzu üzrə dəqiq məlumat tapilmadi. Zəhmət olmasa rəsmi mənbələrə müraciət edin.",
                "source": "no_data"
            }
        
        context = format_context(results)

        # Step 2: build prompt
        prompt = f"""
You are a legal assistant for Azerbaijani government services. 

Answer the question ONLY using the provided context. 
If the answer is not explicitly stated in the context, say you do not know.

Context:
{context}

Question:
{user_input}

Answer in Azerbaijani language.
Add a disclaimer advising the user to verify information from official government sources. 
"""

        # Step 3: call OpenAI
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
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
            "message": "Sorğunuz yaradilarkən xəta baş verdi.",
            "source": "error"
        }