from pathlib import Path
from typing import Annotated, Any, Union
from pydantic import (
    PostgresDsn,
    BeforeValidator,
    computed_field,
    Field
)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Project & Security
    PROJECT_NAME: str = "Alempie"
    BASE_DIR: Path = Path(__file__).resolve().parent
    TEMPLATE_DIR: str = str(BASE_DIR / "templates")
    STATIC_DIR: str = str(BASE_DIR / "static")

    # Database
    POSTGRES_USER: str = 'alempie'
    POSTGRES_PASSWORD: str = 'alempie123'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'alempie'

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """Stelt de URI samen: postgresql://user:pass@server:port/db"""
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                host=self.POSTGRES_SERVER,
                port=self.POSTGRES_PORT,
                path=self.POSTGRES_DB,
            )
        )
settings = Settings()