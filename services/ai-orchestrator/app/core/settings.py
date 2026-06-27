from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "NEXUS ONE"
    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "nexus_ai"
    JWT_SECRET: str = "change-this-secret"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()