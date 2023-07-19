from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from src.databases.database import get_database_session
from src.start.api_router import router as api_router
from src.app.middleware import middleware_api_router

app = FastAPI()


# Static/Public Files
app.mount('/public', StaticFiles(directory='public'), name='public')


@app.get('/hello')
async def hello():
    return {'hello': 'world'}

# Middleware
app = middleware_api_router(app)

# Routers
app.include_router(
    api_router,
    prefix='/api',
    dependencies=[Depends(get_database_session)]
)
