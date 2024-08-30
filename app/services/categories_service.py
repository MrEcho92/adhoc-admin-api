from sqlalchemy.orm import Session
from app.models.models import Category
from app.schema.categories_schema import CategoriesSchema


class CategoryService:
    def __init__(self) -> None:
        pass

    def get_categories(self, db: Session) -> list[CategoriesSchema]:
        try:
            categories = db.query(Category).all()
            return categories
        except Exception:
            raise

    def create_category(self):
        pass
