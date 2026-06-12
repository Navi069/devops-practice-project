from fastapi import APIRouter
from backend.services.ai_service import ask_ai

router = APIRouter()

@router.get("/ai-pipeline/{prompt}")
def ai_pipeline(prompt: str):

    full_prompt = f"""
    You are a senior DevOps engineer.

    Generate a professional GitHub Actions CI/CD pipeline for:

    {prompt}

    Requirements:
    - Return only YAML
    - Use best practices
    - Include testing steps
    - Include dependency installation
    - Include build steps if required
    """

    response = ask_ai(full_prompt)

    return {
        "pipeline": response
    }