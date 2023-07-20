from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from src.databases.migrations.migration_class import BaseMigrationClass

if TYPE_CHECKING:
    from .user import User  # noqa: F401

# Main SQLAlchemy model


class Example(BaseMigrationClass):
    __tablename__ = "examples"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(191), index=True)
    description = Column(String(191), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    owner = relationship("User", back_populates="example")
