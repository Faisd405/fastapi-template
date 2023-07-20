from fastapi import APIRouter
from .routes import auth_router, example_router

router = APIRouter()

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth'],
    responses={404: {'description': 'Not found'}}
)
router.include_router(
    example_router,
    prefix='/examples',
    tags=['examples'],
    responses={404: {'description': 'Not found'}},
)
