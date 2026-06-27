from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    MONGODB_URI: str
    DATABASE_NAME: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()