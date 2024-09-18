from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import Category
from app.schema.categories_schema import CategoriesSchema


class CategoryService:
    def get_categories(self, db: Session) -> list[CategoriesSchema]:
        try:
            categories = db.query(Category).all()
            return categories
        except Exception:
            raise

    def create_category(self, db: Session, category: Category) -> CategoriesSchema:
        try:
            new_category = Category(**category.dict())
            db.add(new_category)
            db.commit()
            db.refresh(new_category)
            return new_category
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def update_category(
        self, db: Session, id: int, category: Category
    ) -> CategoriesSchema:
        try:
            updated_category = db.query(Category).filter_by(id=id).first()
            if not updated_category:
                raise HTTPException(status_code=404, detail="Category not found")
            updated_category.label = category.label
            updated_category.name = category.name
            db.refresh(category)
            db.commit()
            return updated_category
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def delete_category(self, db: Session, id: int):
        try:
            category = db.query(Category).filter_by(id=id).first()
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            db.delete(category)
            db.commit()
            return category
        except SQLAlchemyError as e:
            db.rollback()
            raise e
