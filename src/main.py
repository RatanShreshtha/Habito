from fastapi import FastAPI

from src.core.config import settings

app_settings = settings.app_settings.model_dump()
app = FastAPI(**app_settings)


@app.get("/")
async def read_root():
    return {"msg": "Hello, World!"}
