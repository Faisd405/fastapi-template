from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt

from src.databases.migrations.migration_class import BaseMigrationClass

if TYPE_CHECKING:
    from .example import Example  # noqa: F401

# Main SQLAlchemy model


class User(BaseMigrationClass):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(191), index=True)
    username = Column(String(191), unique=True, index=True, nullable=False)
    email = Column(String(191), unique=True, index=True, nullable=False)
    password = Column(String(191), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    example = relationship("Example", back_populates="owner")

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.example)
