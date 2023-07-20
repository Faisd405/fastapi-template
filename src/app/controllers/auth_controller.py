
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from src.app.schemas.user import UserCreate, UserUpdate, UserLogin, User as UserSchema
from src.databases.migrations.models.user import User as UserModel
from src.app.helpers.auth import create_access_token


async def login(db: Session, login_data: UserLogin):
    db_user = db.query(UserModel).filter(
        (UserModel.username == login_data.username) | (
            UserModel.email == login_data.username)
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )

    if not bcrypt.verify(login_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect password'
        )

    access_token = create_access_token(data={'sub': db_user.username})

    return {'access_token': access_token, 'token_type': 'bearer'}


async def register(db: Session, user_data: UserCreate):
    if user_data.password != user_data.confirmed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Password and confirmed password do not match'
        )

    check_user = db.query(UserModel).filter(
        (UserModel.email == user_data.email) | (
            UserModel.username == user_data.username)
    ).first()

    if check_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username or Email already registered'
        )

    user_data.password = bcrypt.hash(user_data.password)

    db_user = UserModel(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


async def get_users(db: Session, current_user: UserSchema):
    if current_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return current_user


async def update_users(db: Session, current_user: UserSchema, user_data: UserUpdate):
    if current_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    if user_data.password is not None:
        if user_data.password != user_data.confirmed_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Password and confirmed password do not match'
            )

        user_data.password = bcrypt.hash(user_data.password)

    db_user = db.query(UserModel).filter(
        UserModel.username == current_user.username).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user
