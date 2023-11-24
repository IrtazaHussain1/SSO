from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = False
    MONGODB_URI: str
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str
    JWT_SECRET_KEY: str
    JWT_HASH_ALGO: str
    APP_TITLE: Optional[str]

    class Config:
        env_file = ".env"


    @lru_cache
    @staticmethod
    def get_settings():
        return Settings()