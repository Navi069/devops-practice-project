from fastapi import APIRouter
from backend.services.ai_service import ask_ai

router = APIRouter()

@router.get("/ai-terraform/{prompt}")
def ai_terraform(prompt: str):

    full_prompt = f"""
    You are a senior DevOps engineer.

    Generate production-ready Terraform code for:
    {prompt}

    Return only Terraform code.
    """

    response = ask_ai(full_prompt)

    return {
        "terraform": response
    }