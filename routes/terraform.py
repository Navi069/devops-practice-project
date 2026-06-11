from fastapi import APIRouter
from backend.tools.terraform_generator import generate_terraform

router = APIRouter()

@router.get("/generate-terraform/{resource_type}")
def terraform(resource_type: str):

    result = generate_terraform(resource_type)

    return {
        "resource_type": resource_type,
        "terraform": result
    }