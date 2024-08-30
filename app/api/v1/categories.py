from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.categories_service import CategoryService
from app.db.database import get_db
from app.schema.categories_schema import CategoriesSchema

router = APIRouter()


category_service = CategoryService()


@router.get("/categories", response_model=list[CategoriesSchema])
async def get_categories(db: Session = Depends(get_db)) -> Any:
    try:
        categories = category_service.get_categories(db=db)
        return categories
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error getting categories: {e}")
