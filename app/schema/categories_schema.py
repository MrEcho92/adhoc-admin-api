from pydantic import BaseModel


class CategoryBaseSchema(BaseModel):
    name: str
    label: str


class CategoriesSchema(CategoryBaseSchema):
    id: int


class CreateCategorySchema(CategoryBaseSchema):
    pass
