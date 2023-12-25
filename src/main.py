from fastapi import FastAPI

from src.core.config import settings
from src.datastore.mongo import db
from src.routes.main import router


def get_app() -> FastAPI:
    app_settings = settings.app_settings.model_dump()

    app = FastAPI(**app_settings)

    app.add_event_handler("startup", db.initialize_db)
    app.include_router(router)

    return app


app = get_app()
