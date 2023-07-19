from src.app.schemas.example import ExampleCreate, ExampleUpdate, Example as ExampleSchema
from src.databases.migrations.models.example import Example as ExampleModel
from sqlalchemy.orm import Session


async def get_examples(db: Session, skip: int = 0, limit: int = 100):
    examples = db.query(ExampleModel).offset(skip).limit(limit).all()
    return examples


async def get_example(db: Session, example_id: int):
    example = db.query(ExampleModel).filter(
        ExampleModel.id == example_id).first()
    return example


async def create_example(db: Session, example: ExampleCreate):
    example = ExampleModel()
    db.add(example)
    db.commit()
    db.refresh(example)
    return example


async def update_example(db: Session, example_id: int, example_data: ExampleUpdate):
    # Fetch the example record from the database
    example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    
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
