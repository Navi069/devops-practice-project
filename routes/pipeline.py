from fastapi import APIRouter
from backend.tools.github_actions import generate_python_pipeline

router = APIRouter()

@router.get("/generate-pipeline")
def generate_pipeline():

    pipeline = generate_python_pipeline()

    return {
        "pipeline": pipeline
    }