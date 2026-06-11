from fastapi import FastAPI
from backend.routes.pipeline import router as pipeline_router
from backend.routes.terraform import router as terraform_router
from backend.routes.ai import router as ai_router
from backend.routes.ai_terraform import router as ai_terraform_router

app = FastAPI(
    title="DevOps AI Copilot",
    description="AI-powered DevOps Assistant",
    version="1.0.0"
)

# Register routes
app.include_router(pipeline_router)
app.include_router(terraform_router)
app.include_router(ai_router)
app.include_router(ai_terraform_router)

# Home route
@app.get("/")
def home():
    return {
        "message": "DevOps AI Copilot Running"
    }
