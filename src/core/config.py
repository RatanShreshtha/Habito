import logging
from datetime import timedelta
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, Field, RedisDsn, UrlConstraints, validator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated

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
    mongo_dsn: Union[
        Annotated[MultiHostUrl, UrlConstraints(allowed_schemes=["mongodb"], default_port=27017)],
        Annotated[MultiHostUrl, UrlConstraints(allowed_schemes=["mongodb+srv"])],
    ] = Field("mongodb://127.0.0.1:27017")

    redis_dsn: RedisDsn = Field("redis://localhost:6379")
    redis_socket_timeout: float = Field(2)

    algorithm: str = "HS256"
    access_token_secret_key: str = "A very very secret string"
    refresh_token_secret_key: str = "Another very very secret string"
    access_token_expiry: int = 30
    refresh_token_expiry: int = 7 * 24 * 60

    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env")


settings = Settings()
