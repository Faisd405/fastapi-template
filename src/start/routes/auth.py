from fastapi import APIRouter, Form, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.databases.database import get_database_session
from src.app.schemas.user import UserCreate, UserUpdate, UserLogin, User as UserSchema
from src.app.controllers import auth_controller
from src.app.helpers.auth import decode_access_token

router = APIRouter()


@router.post('/login')
async def login(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_database_session)):
    return await auth_controller.login(db, login_data)


@router.post('/register')
async def register(user_data: UserCreate, db: Session = Depends(get_database_session)):
    return await auth_controller.register(db, user_data)


@router.get('/me')
async def get_users(db: Session = Depends(get_database_session), current_user: str = Depends(decode_access_token)):
    return await auth_controller.get_users(db, current_user)


@router.get('/update')
async def get_users(user_data: UserUpdate, db: Session = Depends(get_database_session), current_user: str = Depends(decode_access_token)):
    return await auth_controller.update_users(db, current_user, user_data)
