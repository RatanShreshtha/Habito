"""FastAPI JWT configuration."""

from datetime import timedelta

from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials, JwtRefreshBearer

from src.core.config import settings
from src.models.user import User

ACCESS_EXPIRES = settings.access_token_expiry
REFRESH_EXPIRES = settings.refresh_token_expiry

access_security = JwtAccessBearer(
    settings.access_token_secret_key,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)

refresh_security = JwtRefreshBearer(
    settings.refresh_token_secret_key,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)


async def user_from_credentials(auth: JwtAuthorizationCredentials) -> User | None:
    """Return the user associated with auth credentials."""
    return await User.by_email(auth.subject["username"])


async def user_from_token(token: str) -> User | None:
    """Return the user associated with a token value."""
    payload = access_security._decode(token)
    return await User.by_email(payload["subject"]["username"])
