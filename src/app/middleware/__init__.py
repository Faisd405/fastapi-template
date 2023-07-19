import fastapi
from .cors import corsSettings


def middleware_api_router(app: fastapi):
    app.add_middleware(**corsSettings)
    
    return app
