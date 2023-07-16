from .auth import router as auth_router
from .questions import router as question_router
from .users import router as user_router

__all__ = [
    'auth_router',
    'question_router',
    'user_router'
]
