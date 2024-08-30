from pydantic import BaseModel


class CategoriesSchema(BaseModel):
    id: int
    name: str
    label: str
