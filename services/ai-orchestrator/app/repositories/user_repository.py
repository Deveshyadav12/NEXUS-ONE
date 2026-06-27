from app.database.mongodb import db

class UserRepository:

    def __init__(self):
        self.collection = db["users"]

    async def find_by_email(self, email: str):
        return await self.collection.find_one({"email": email})

    async def create(self, user: dict):
        return await self.collection.insert_one(user)