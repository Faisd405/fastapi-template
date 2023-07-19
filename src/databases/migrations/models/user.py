from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.databases.migrations.migration_class import BaseMigrationClass

if TYPE_CHECKING:
    from .example import Example  # noqa: F401

# Main SQLAlchemy model


class User(BaseMigrationClass):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(191), index=True)
    email = Column(String(191), unique=True, index=True, nullable=False)
    password = Column(String(191), nullable=False)
    
    example = relationship("Example", back_populates="owner")
