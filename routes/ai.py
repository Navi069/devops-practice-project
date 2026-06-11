from fastapi import APIRouter
from backend.services.ai_service import ask_ai

router = APIRouter()

@router.get("/ask-ai/{prompt}")
def ai(prompt: str):

    response = ask_ai(prompt)

    return {
        "prompt": prompt,
        "response": response
    }