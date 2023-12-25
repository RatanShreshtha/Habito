from fastapi import FastAPI

from src.core.config import settings
from src.datastore.mongo import db
from src.routes.main import router
from src.routes.task import task_router


def get_app() -> FastAPI:
    app_settings = settings.app_settings.model_dump()

    app = FastAPI(**app_settings)

    app.add_event_handler("startup", db.initialize_db)
    app.include_router(router, tags=["Root"])
    app.include_router(task_router, prefix="/tasks", tags=["Task"])

    return app


app = get_app()
