from datetime import datetime, timedelta
from typing import Annotated, Any, Union

from jose import JWTError, jwt

from src.core.config import settings


def create_access_token(subject: Union[str, Any]) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=settings.access_token_expiry)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.access_token_secret_key, settings.algorithm)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any]) -> str:
    expires_delta = datetime.utcnow() + timedelta(minutes=settings.refresh_token_expiry)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.refresh_token_secret_key, settings.algorithm)
    return encoded_jwt
