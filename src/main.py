from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.start.api_router import router as api_router

app = FastAPI()

app.mount('/public', StaticFiles(directory='public'), name='public')
app.include_router(api_router, prefix='/api')