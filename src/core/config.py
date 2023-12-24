import logging
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, MongoDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).parent.parent.parent


class AppSettings(BaseModel):
    """FastAPI specific configuration."""

    title: str = "Habito"
    description: str = "A simple portal to track your habits and todos."
    version: str = "0.1.0"
    docs_url: str = "/docs"


class Settings(BaseSettings):
    app_settings: AppSettings = AppSettings()

    debug: Optional[bool] = False

    log_level: int = logging.INFO
    log_file: Path | None = "app.log"
    log_format: str = "%(asctime)s | %(message)s"
    log_date_format: str | None = "%d %b %Y | %H:%M:%S"

    mongo_db: Optional[str] = None
    mongo_dsn: MongoDsn = Field("mongodb://127.0.0.1:27017")

    redis_dsn: RedisDsn = Field("redis://localhost:6379")

    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env")


settings = Settings()
