from fastapi import FastAPI

from src.core.config import settings
from src.core.logger import setup_rich_logger

setup_rich_logger()
app_settings = settings.app_settings.model_dump()
app = FastAPI(**app_settings)


@app.get("/")
async def read_root():
    return {"msg": "Hello, World!"}
