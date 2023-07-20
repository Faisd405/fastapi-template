from src.app.schemas.example import ExampleCreate, ExampleUpdate, Example as ExampleSchema
from src.databases.migrations.models.example import Example as ExampleModel
from sqlalchemy.orm import Session


async def get_examples(db: Session, current_page: int = 1, limit: int = 100):
    offset = ((current_page if current_page > 0 else 1) - 1) * limit

    data = {}
    data['list'] = db.query(ExampleModel).offset(offset).limit(limit).all()
    data['params'] = {
        'current_page': current_page,
        'offset': offset,
        'limit': limit,
        'total': db.query(ExampleModel).count(),
    }
    return data


async def get_example(db: Session, example_id: int):
    example = db.query(ExampleModel).filter(
        ExampleModel.id == example_id).first()
    return example


async def create_example(db: Session, example: ExampleCreate):
    db_example = ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example


async def update_example(db: Session, example_id: int, example_data: ExampleUpdate):
    # Fetch the example record from the database
    example = db.query(ExampleModel).filter(
        ExampleModel.id == example_id).first()

    if example:
        # Update the example object with data from ExampleUpdate
        for key, value in example_data.dict(exclude_unset=True).items():
            setattr(example, key, value)

        # Commit the changes to the database
        db.commit()
        db.refresh(example)

    return example


async def delete_example(db: Session, example_id: int):
    example = db.query(ExampleModel).filter(
        ExampleModel.id == example_id).first()
    db.delete(example)
    db.commit()
    return example
