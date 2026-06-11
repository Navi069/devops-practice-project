from fastapi import FastAPI
from backend.routes.pipeline import router

app = FastAPI(
    title="DevOps AI Copilot",
    description="AI-powered DevOps Assistant",
    version="1.0.0"
)

# Register routes
app.include_router(router)

# Home route
@app.get("/")
def home():
    return {
        "message": "DevOps AI Copilot Running"
    }
