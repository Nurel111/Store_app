from fastapi import APIRouter, Depends, HTTPException
from store_app.database.models import UserProfile
from store_app.database.schema import UserProfileOutSchema
from store_app.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

users_router = APIRouter(prefix='/users', tags=['UserProfile'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@users_router.get('/', response_model=List[UserProfileOutSchema])
async def list_user(db: Session = Depends(get_db)):
    return db.query(UserProfile).all()

@users_router.get('/{user_id}/', response_model=UserProfileOutSchema)
async def detail_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.id==user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail='Мындай id жок')
    return user