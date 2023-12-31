
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    DB_CONNECTION: str = "sqlite"
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str = "database.db"
    DB_USERNAME: str
    DB_PASSWORD: str
    
    FRONTEND_URL: str = "http://localhost:3000"
    
    SECRET_KEY_JWT: str
    ALGORITHM_JWT: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()