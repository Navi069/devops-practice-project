from fastapi import APIRouter
from backend.tools.github_actions import generate_pipeline

router = APIRouter()

@router.get("/generate-pipeline/{language}")
def pipeline(language: str):

    result = generate_pipeline(language)

    return {
        "language": language,
        "pipeline": result
    }