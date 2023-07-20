from fastapi import APIRouter, Depends
from src.app.controllers.example_controller import get_examples, get_example, create_example, update_example, delete_example
from src.databases.database import get_database_session
from sqlalchemy.orm import Session
from src.app.schemas.example import ExampleCreate, ExampleUpdate

router = APIRouter()


@router.get('/')
async def get_all_examples(db: Session = Depends(get_database_session), current_page: int = 0, limit: int = 100):
    return await get_examples(db, current_page, limit)


@router.get('/{example_id}')
async def get_one_example(example_id: int, db: Session = Depends(get_database_session)):
    return await get_example(db, example_id)


@router.post('/')
async def create_one_example(example: ExampleCreate, db: Session = Depends(get_database_session)):
    return await create_example(db, example)


@router.put('/{example_id}')
async def update_one_example(*, example_id: int, example: ExampleUpdate, db: Session = Depends(get_database_session)):
    return await update_example(db, example_id, example)


@router.delete('/{example_id}')
async def delete_one_example(example_id: int, db: Session = Depends(get_database_session)):
    return await delete_example(db, example_id)
