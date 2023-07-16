from fastapi import APIRouter
from src.app.controllers.question_controller import get_questions, get_question, create_question, update_question, delete_question

router = APIRouter(
    prefix='/questions',
    tags=['questions'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/')
async def get_questions():
    pass


@router.get('/{question_id}')
async def get_question(question_id: int):
    pass


@router.post('/')
async def create_question():
    pass


@router.put('/{question_id}')
async def update_question(question_id: int):
    pass


@router.delete('/{question_id}')
async def delete_question(question_id: int):
    pass
