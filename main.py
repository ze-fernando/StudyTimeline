from fastapi import FastAPI
from src.config.settings import settings
from src.routes.api import route

app = FastAPI(title=settings.APP_NAME)


app.include_router(route)
