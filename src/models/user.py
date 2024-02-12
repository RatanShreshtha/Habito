from datetime import datetime
from typing import Annotated, Any, Optional

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr, Field

from src.utils.auth import verify_password


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


class UserSignUp(BaseModel):
    full_name: str | None = None
    username: str
    email: EmailStr
    password: str


class User(Document):
    full_name: str | None = None
    username: str
    email: EmailStr
    password: str
    bio: str | None = None
    verified: bool = False

    def verify_password(self, password) -> datetime | None:
        """Match provided password with sored salted hash."""
        return verify_password(password, self.password)

    @property
    def created_at(self) -> datetime | None:
        """Datetime user was created from ID."""
        return self.id.generation_time if self.id else None

    @property
    def jwt_subject(self) -> dict[str, Any]:
        """JWT subject fields."""
        return {"email": self.email}

    @classmethod
    async def by_email(self, email: str) -> Optional["User"]:
        """Get a user by email."""
        return await self.find_one(self.email == email)

    class Settings:
        name = "users"
