from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate, UserSchema
from app.services.user_service import UserService
from app.db.database import get_db

router = APIRouter()

user_service = UserService()


@router.get("/users", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user(email: str, db: Session = Depends(get_db)) -> Any:
    try:
        return user_service.get_user(db, email)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user: {e}")


@router.post("/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> Any:
    try:
        return user_service.create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {e}")


@router.put("/users", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def update_user(
    email: str, user: UserCreate, db: Session = Depends(get_db)
) -> Any:
    try:
        return user_service.update_user(db, email, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user: {e}")


@router.delete("/users", status_code=status.HTTP_200_OK)
async def delete_user(email: str, db: Session = Depends(get_db)) -> Any:
    try:
        return user_service.delete_user(db, email)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting user: {e}")
