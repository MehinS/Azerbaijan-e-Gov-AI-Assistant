from fastapi import FastAPI
from pydantic import BaseModel

from orchestrator import detect_intent
from agents.diploma_recognition_agent import handle_diploma_recognition
from agents.marriage_agent import handle_marriage
from agents.legal_question_agent import handle_legal_question
from services.privacy_filter import filter_sensitive_data

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str

@app.get('/')
def home():
    return {"message": "Azerbaijan AI Assistant running"}

@app.get("/proactive")
def proactive():
    return {
        "alert": "Passportunuzun vaxtinin bitmeyine 6 ay qalib. Dəyişməyi nəzərdə tutun."
    }

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        user_input = request.user_input

        # privacy filtering
        safe_input = filter_sensitive_data(user_input)

        # intent detection
        intent = detect_intent(safe_input)

        if intent == "diploma":
            return handle_diploma_recognition(safe_input)
        elif intent == "marriage":
            return handle_marriage(safe_input)
        elif intent == "legal_question":
            return handle_legal_question(safe_input)
        else:
            return {
                "service" : "unknown",
                "message" : "Sorry, I don't understand your request yet. "
                }
        
    except Exception as e:
        print("Error in /chat:", e)
        return {"error": "Something went wrong"}