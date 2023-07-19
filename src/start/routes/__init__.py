from .auth import router as auth_router
from .examples import router as example_router
from .users import router as user_router

__all__ = [
    'auth_router',
    'example_router',
    'user_router'
]
