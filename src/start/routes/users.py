from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/me')
async def get_users():
    pass

@router.get('/update')
async def get_users():
    pass
