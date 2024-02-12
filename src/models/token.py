from datetime import timedelta

from pydantic import BaseModel

from src.core.config import settings


class AccessToken(BaseModel):
    """Access token details."""

    access_token: str
    access_token_expires: timedelta = settings.access_token_expiry


class RefreshToken(AccessToken):
    """Access and refresh token details."""

    refresh_token: str
    refresh_token_expires: timedelta = settings.refresh_token_expiry
