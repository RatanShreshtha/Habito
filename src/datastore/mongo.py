from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from src.models.task import Task


class MongoDBConnector:
    """Load mongodb settings and build valid URI"""

    async def initialize_db(self) -> None:
        """start mongo db client with Beanie and load models"""

        mongo_dsn = settings.mongo_dsn.unicode_string()

        client = AsyncIOMotorClient(mongo_dsn)
        models = [Task]

        try:
            await init_beanie(database=client[settings.mongo_db], document_models=models)
            print(f"Connected to {settings.mongo_db}")
        except Exception:
            raise ConnectionError


db = MongoDBConnector()
