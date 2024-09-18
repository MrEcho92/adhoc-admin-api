from pydantic import BaseModel
from uuid import UUID


class UserBaseSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema):
    id: UUID
