from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

if str(settings.DB_CONNECTION) == "mysql":
    SQLALCHEMY_DATABASE_URL = f"{settings.DB_CONNECTION}+pymysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"
elif settings.DB_CONNECTION == "sqlite":
    SQLALCHEMY_DATABASE_URL = f"{settings.DB_CONNECTION}:///{settings.DB_DATABASE}"
else:
    SQLALCHEMY_DATABASE_URL = f"{settings.DB_CONNECTION}://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_database_session():
    db = SessionLocal()
    try:
        yield db
        # Check if session is still active
    finally:
        db.close()

Base = declarative_base()
