from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import User
from app.schema.user_schema import UserCreate, UserSchema


class UserService:
    def get_user(self, db: Session, email: str) -> UserSchema:
        try:
            user = db.query(User).filter(User.email == email).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def create_user(self, db: Session, user: UserCreate) -> UserSchema:
        try:
            new_user = User(
                username=user.username,
                email=user.email,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def update_user(self, db: Session, email: str, updated_data: UserCreate):
        try:
            user = self.get_user(db, email)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            user.username = updated_data.username
            user.email = updated_data.email

            db.commit()
            db.refresh(user)
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def delete_user(self, db: Session, email: str):
        try:
            user = self.get_user(db, email)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            db.delete(user)
            db.commit()
            return user
        except SQLAlchemyError as e:
            db.rollback()
            raise e
