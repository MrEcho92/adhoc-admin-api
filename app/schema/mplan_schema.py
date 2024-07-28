from pydantic import BaseModel
from datetime import date, datetime


class Category(BaseModel):
    label: str
    is_completed: bool = False


class MplanSchema(BaseModel):
    id: str
    moving_date: date
    old_address: str
    new_address: str
    selected_categories: list[Category] = []
    created_at: datetime = None
    modified_at: datetime = None
    user_id: str


class CreateMplanSchema(BaseModel):
    user_id: str
    moving_date: date
    old_address: str
    new_address: str
    selected_categories: list[Category] = []
