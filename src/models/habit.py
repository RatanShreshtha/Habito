from datetime import datetime
from typing import List

from beanie import Document, PydanticObjectId


class Habit(Document):
    name: str = Document.field(required=True)
    description: str = Document.field(default="")
    category: str = Document.field(default="")
    target: str = Document.field(required=True)  # e.g., "daily", "weekly", "monthly"
    tracking_method: str = Document.field(required=True)  # e.g., "binary", "numerical", "duration"
    reminder_time: str = Document.field(default="")
    start_date: datetime = Document.field(default=datetime.utcnow)
    current_streak: int = Document.field(default=0)
    longest_streak: int = Document.field(default=0)
    notes: str = Document.field(default="")
    user_id: PydanticObjectId = Document.field(required=True)

    # Relationship with schedules
    schedules: List["Schedule"] = Document.field(link_to="Schedule", default=[])

    class Settings:
        name = "habits"


class Schedule(Document):
    habit_id: PydanticObjectId = Document.field(required=True)
    days_of_week: List[str] = Document.field(default=[])
    time_of_day: str = Document.field(required=True)

    class Settings:
        name = "schedules"
