# AI-Assisted Government Service Prototype (Bürokratt-inspired)

## Overview
This project is a prototype of an AI-assisted government service system inspired by Estonia's Bürokratt initiative

It demonstrates how AI can be used to:

- understand user requests
- route them to appropriate services
- retrieve relevant legal information
- support modular and scalable government AI architecture

---

## Key features

- LLM-based intent detection (OpenAI)
- Modular agent architecture (diploma recognition, marriage registration, legal question)
- Retrieveal-Augemented Generation (RAG) for legal queries
- Basic privacy filtering
- Proactive notification simulation
- FastAPI backend

---

## Architecture

User -> FastAPI -> Orchestrator -> Agents -> (RAG / Knowledge base)

### Components

- **Orchestrator**: detects user intent using LLM
- **Agents**:
    - Diploma Recognition Agent
    - Marriage Agent
    - Legal Question Agent
- **Knowledge Base**:
    - keyword-based retrieval simulating legal sources (e.g. e-qanun)
- **Privacy Filter**:
    - removes sensitive data before processing

---

## Example Queries

- "I lost my passport, do I have to pay fine?"
- "I want to get my foreign diploma recognized"
- "How do I register a marriage?"

---

## Tech Stack

- Python
- FastAPI
- OpenAI API (LLM)
- Simple RAG implementation

---

## How to Run

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
pip install -r requirements.txt

4. Create '.env' file:
OPENAI_API_KEY=your_api_key_here

5. Run the app:
python -m uvicorn main:app --reload

6. Open in browser:
http://127.0.0.1:8000/docs

---

## Limitations

- Uses simplified keyword-based retrieval instead of full legal database
- No real API integration with government systems
- Proactive features are simulated
- Not production-ready (demonstration purpose only)

---

## Future Improvements

- Integration with real APIs (e.g. digital.bridge)
- Advanced RAG with vector databases
- User authentication and personlization
- Real-time notifications

---

## Purpose

This project is developed as part of portfolio to explore:

- AI system architecture for government services 
- LLM-based orchestration
- data privacy considerations in AI systems
#
