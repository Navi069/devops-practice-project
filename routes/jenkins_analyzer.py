from fastapi import APIRouter
from backend.services.ai_service import ask_ai

router = APIRouter()

@router.post("/analyze-jenkins")
def analyze_jenkins(log: str):

    full_prompt = f"""
    You are a senior DevOps and Jenkins expert.

    Analyze the following Jenkins build log.

    Provide:
    1. Root cause
    2. Exact issue explanation
    3. Suggested fix
    4. Prevention recommendations

    Jenkins Log:
    {log}
    """

    response = ask_ai(full_prompt)

    return {
        "analysis": response
    }