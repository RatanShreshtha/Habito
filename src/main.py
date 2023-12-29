from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.config import settings
from src.datastore.mongo import db
from src.datastore.redis import cache
from src.routes.health import health_router
from src.routes.task import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.db = await db.initialize_db()
    app.cache = await cache.initialize_cache()

    yield
    app.db.close()
    await app.cache.aclose()


def get_app() -> FastAPI:
    app_settings = settings.app_settings.model_dump()

    app = FastAPI(**app_settings, lifespan=lifespan)

    app.include_router(health_router, tags=["Root"])
    app.include_router(task_router, prefix="/tasks", tags=["Task"])

    return app


app = get_app()
