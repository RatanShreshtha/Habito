import logging
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, Field, RedisDsn, UrlConstraints
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated
from datetime import timedelta

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

    salt: bytes = b"a pinch od salt"
    secret_key: str = "Some very very secret key"
    access_token_expiry: timedelta = Field(timedelta(minutes=45))
    refresh_token_expiry: timedelta = Field(timedelta(days=7))


    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env")


settings = Settings()
