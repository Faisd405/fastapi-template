from typing import Optional

from pydantic import BaseModel


# Shared properties
class ExampleBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on example creation
class ExampleCreate(ExampleBase):
    owner_id: int


# Properties to receive on example update
class ExampleUpdate(ExampleBase):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class ExampleInDBBase(ExampleBase):
    id: int
    title: str
    owner_id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Example(ExampleInDBBase):
    pass


# Properties properties stored in DB
class ExampleInDB(ExampleInDBBase):
    pass
