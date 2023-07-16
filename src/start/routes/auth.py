from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/login')
async def login():
    pass

@router.post('/register')
async def register():
    pass
