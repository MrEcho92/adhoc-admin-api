import os
from typing import Literal, List
from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'dev')}",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    DOMAIN: str = "localhost"
    ENV: Literal["dev", "prod"] = "dev"
    DEBUG: bool = True

    BACKEND_CORS_ORIGINS: List[AnyUrl] = []

    PROJECT_NAME: str = ""
    POSTGRES_SERVER: str = ""
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    @property
    def SQLALCHEMY_DATABASE_URL(self):
        return os.getenv("DATABASE_URL")


settings = Settings()
