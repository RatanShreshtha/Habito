from typing import Optional

from beanie import Document
from pydantic import BaseModel


class Task(Document):
    title: str
    description: str

    class Settings:
        name = "tasks_collection"

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Ye kaam krna hai",
                "description": "Bhool mt jana",
            }
        }