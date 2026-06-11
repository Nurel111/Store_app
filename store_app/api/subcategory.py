from fastapi import APIRouter, HTTPException, Depends
from store_app.database.models import SubCategory
from store_app.database.schema import SubCategoryOutSchema,SubCategoryInputSchema
from store_app.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

subcategory_router = APIRouter(prefix='/subcategory',tags=['Subcategory'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@subcategory_router.post('/',response_model=SubCategoryOutSchema)
async def create_subcategory(subcategory:SubCategoryInputSchema,db: Session = Depends(get_db)):
    subcategory_db = SubCategory(**subcategory.dict())
    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db


@subcategory_router.get('/',response_model=List[SubCategoryOutSchema])
async def list_subcategory(db: Session = Depends(get_db)):
     return db.query(SubCategory).all()

@subcategory_router.get('/{subcategory.id}/',response_model=SubCategoryOutSchema)
async def detail_subcategory(subcategory_id: int,db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей',status_code=400)

    return subcategory_db



@subcategory_router.put('/{subcategory.id}/',response_model=dict)
async def update_subcategory(subcategory_id: int, subcategory: SubCategoryInputSchema ,
                          db: Session = Depends(get_db)):
    subcategory_db =  db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    for  subcategory_key, subcategory_value in  subcategory.dict().items():
        setattr( subcategory_db, subcategory_key, subcategory_value)

        db.commit()
        db.refresh(subcategory_db)
        return {'message': 'Кате    гори озгорулду'}


@ subcategory_router.delete('/{subcategory.id}/',response_model=dict)
async def delete_subcategory(subcategory_id: int,db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id ==subcategory_id).first()
    if not  subcategory_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    db.delete(subcategory_db)
    db.commit()
    return {'massage': 'категории удален'}