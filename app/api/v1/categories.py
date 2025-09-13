from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.categories_service import CategoryService
from app.db.database import get_db
from app.schema.categories_schema import CategoriesSchema, CreateCategorySchema

router = APIRouter()


category_service = CategoryService()


@router.get(
    "/categories", response_model=list[CategoriesSchema], status_code=status.HTTP_200_OK
)
async def get_categories(db: Session = Depends(get_db)) -> Any:
    try:
        categories = category_service.get_categories(db)
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting categories: {e}")


@router.post(
    "/categories", response_model=CategoriesSchema, status_code=status.HTTP_201_CREATED
)
async def create_category(
    category: CreateCategorySchema, db: Session = Depends(get_db)
) -> Any:
    try:
        output = category_service.create_category(db, category)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating category: {e}")


@router.put("/categories/{category_id}")
async def update_category(
    category_id: int, category: CreateCategorySchema, db: Session = Depends(get_db)
) -> Any:
    try:
        category_update = category_service.update_category(
            db, int(category_id), category
        )
        return category_update
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating category: {e}")


@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_service.delete_category(db, int(category_id))
    return HTTPException(status_code=200, detail="Category deleted successfully")
