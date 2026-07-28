from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")

    database_host: str = "localhost"
    database_name: str = "fastapi"
    database_user: str = "postgres"
    database_password: str = "123456"
    database_url: str = ""

    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 120

   

settings = Settings()
