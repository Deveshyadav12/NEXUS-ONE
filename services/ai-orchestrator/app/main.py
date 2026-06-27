from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="NEXUS ONE",
    version="0.0.1"
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])


@app.get("/")
async def home():
    return {
        "project": "NEXUS ONE",
        "status": "Running"
    }