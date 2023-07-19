from src.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware

corsSettings = {
    "middleware_class": CORSMiddleware,
    "allow_origins": [settings.FRONTEND_URL],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
