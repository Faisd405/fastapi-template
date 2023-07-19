from fastapi import APIRouter
from .routes import auth_router, user_router, example_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(example_router)
