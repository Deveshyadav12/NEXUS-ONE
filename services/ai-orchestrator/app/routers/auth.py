from fastapi import APIRouter
from app.schemas.user import RegisterRequest, LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

service = AuthService()


@router.post("/register")
async def register(user: RegisterRequest):
    return await service.register(user.model_dump())


@router.post("/login")
async def login(user: LoginRequest):
    return await service.login(user.model_dump())


@router.get("/hello")
async def hello():
    return {
        "message": "Authentication Module Working"
    }