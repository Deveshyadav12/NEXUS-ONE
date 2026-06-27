from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token

repo = UserRepository()


class AuthService:

    async def register(self, data: dict):

        existing = await repo.find_by_email(data["email"])

        if existing:
            return {
                "success": False,
                "message": "Email already exists"
            }

        data["password"] = hash_password(data["password"])

        await repo.create(data)

        return {
            "success": True,
            "message": "Registration Successful"
        }

    async def login(self, data: dict):

        user = await repo.find_by_email(data["email"])

        if not user:
            return {
                "success": False,
                "message": "Invalid Email"
            }

        if not verify_password(
            data["password"],
            user["password"]
        ):
            return {
                "success": False,
                "message": "Invalid Password"
            }

        token = create_access_token(
            {
                "sub": str(user["_id"]),
                "email": user["email"]
            }
        )

        return {
            "success": True,
            "access_token": token,
            "token_type": "bearer"
        }