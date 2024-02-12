"""Authentication auth_router."""

from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from src.models.token import AccessToken, RefreshToken
from src.models.user import User, UserSignIn, UserSignUp
from src.utils.auth import get_hashed_password, verify_password
from src.utils.jwt import access_security, refresh_security

auth_router = APIRouter()


@auth_router.post("/signup", response_model=User)
async def signup(user_signup: UserSignUp):
    """Create a new user."""
    user = await User.by_email(user_signup.email)
    if user is not None:
        raise HTTPException(409, "User with that email already exists")

    hashed_password = get_hashed_password(user_signup.password)
    user = User(
        full_name=user_signup.full_name, username=user_signup.email, email=user_signup.email, password=hashed_password
    )
    await user.create()
    return user


@auth_router.post("/signin")
async def signin(user_signin: UserSignIn) -> RefreshToken:
    """Authenticate and returns the user's JWT."""
    user = await User.by_email(user_signin.email)

    if user is None or not verify_password(user_signin.password, user.password):
        raise HTTPException(status_code=401, detail="Bad email or password")

    if not user.verified:
        raise HTTPException(status_code=400, detail="Email is not yet verified")

    access_token = access_security.create_access_token(user.jwt_subject)
    refresh_token = refresh_security.create_refresh_token(user.jwt_subject)
    return RefreshToken(access_token=access_token, refresh_token=refresh_token)


@auth_router.post("/refresh")
async def refresh(auth: JwtAuthorizationCredentials = Security(refresh_security)) -> AccessToken:
    """Return a new access token from a refresh token."""
    access_token = access_security.create_access_token(subject=auth.subject)
    return AccessToken(access_token=access_token)
