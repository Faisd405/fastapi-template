from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from src.databases.database import SessionLocal, get_database_session
from src.config.settings import settings
from fastapi import Depends, HTTPException
from src.databases.migrations.models.user import User as UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

invalid_credentials_exception = HTTPException(
    status_code=401,
    detail='Invalid authentication credentials',
    headers={'WWW-Authenticate': 'Bearer'}
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY_JWT, algorithm=settings.ALGORITHM_JWT)
    return encoded_jwt


def decode_access_token(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_database_session)):
    try:
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY_JWT,
            algorithms=[settings.ALGORITHM_JWT]
        )

        if decoded_token.get('sub') is None:
            raise invalid_credentials_exception

        if decoded_token.get('exp') is None:
            raise invalid_credentials_exception

        if datetime.fromtimestamp(decoded_token.get('exp')) < datetime.utcnow():
            raise invalid_credentials_exception
        
        user = db.query(UserModel).filter(UserModel.username == decoded_token.get('sub')).first()
        if user is None:
            raise invalid_credentials_exception

        return user
    except JWTError:
        return None
