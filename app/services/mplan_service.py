from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, or_
from typing import Any
from uuid import UUID
from datetime import datetime, timezone
from app.schema.mplan_schema import MplanSchema, MplanSchemaCreate, MplanDetailSchema
from app.models import models
from app.utils.date_format import date_format


class MplanService:
    def create_mplan(self, db: Session, mplan: MplanSchemaCreate) -> MplanSchema:
        try:
            moving_date = date_format(mplan.moving_date)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid date format (Expected format: YYYY-MM-DD): {e}.",
            )

        try:
            new_mplan = models.Mplan(
                moving_date=moving_date,
                old_address=mplan.old_address,
                new_address=mplan.new_address,
                user_id=mplan.user_id,
            )
            categories = [
                models.MplanCategory(label=category.label)
                for category in mplan.selected_categories
            ]
            new_mplan.selected_categories.extend(categories)
            db.add(new_mplan)
            db.commit()
            db.refresh(new_mplan)
            return new_mplan
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def get_mplan_details(
        self, db: Session, mplan_id: UUID, user_id: UUID, address_info: Any
    ) -> MplanDetailSchema:
        try:
            mplan = self.get_mplan(db, mplan_id, user_id)
            if not mplan:
                raise HTTPException(status_code=404, detail="MPlan not found")

            councils = (
                db.query(models.Council)
                .filter(
                    func.lower(func.replace(models.Council.slug, "-", " "))
                    == func.lower(address_info.get("district"))
                )
                .all()
            )
            nhs = {
                nhs_type.lower(): db.query(models.NHSOrganisation)
                .filter(
                    models.NHSOrganisation.organisation_type == nhs_type,
                    or_(
                        func.lower(models.NHSOrganisation.city)
                        == func.lower(address_info.get("town_or_city")),
                        func.lower(models.NHSOrganisation.county)
                        == func.lower(address_info.get("county")),
                    ),
                )
                .all()
                for nhs_type in ["GpBranch", "Pharmacy", "Hospital", "Dentist"]
            }
            gp = (
                db.query(models.GPPracticeByConstituency)
                .filter(
                    or_(
                        func.lower(models.GPPracticeByConstituency.address4).like(
                            f"%{func.lower(address_info.get('town_or_city'))}%"
                        ),
                        func.lower(models.GPPracticeByConstituency.address4).like(
                            f"%{func.lower(address_info.get('county'))}%"
                        ),
                    )
                )
                .all()
            )
            water = (
                db.query(models.WaterSupply)
                .filter(
                    func.lower(
                        func.replace(models.WaterSupply.constituency_name, "-", " ")
                    ).like(f"%{func.lower(address_info.get('town_or_city'))}%")
                )
                .all()
            )
            sewages = (
                db.query(models.Sewerage)
                .filter(
                    func.lower(
                        func.replace(models.Sewerage.constituency_name, "-", " ")
                    ).like(f"%{func.lower(address_info.get('town_or_city'))}%")
                )
                .all()
            )
            schools = (
                db.query(models.School)
                .filter(
                    func.lower(models.School.laname)
                    == func.lower(address_info.get("county")),
                    func.lower(models.School.locality)
                    == func.lower(address_info.get("town_or_city")),
                )
                .all()
            )

            response = {
                "mplan": mplan,
                "councils": councils,
                "gp": gp,
                "water": water,
                "sewages": sewages,
                "schools": schools,
            }
            response.update(nhs)
            return response
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def get_mplan_by_user_id(self, db: Session, user_id: UUID) -> list[MplanSchema]:
        try:
            return db.query(models.Mplan).filter(models.Mplan.user_id == user_id).all()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def update_mplan(
        self,
        db: Session,
        mplan_id: UUID,
        user_id: UUID,
        mplan_update: MplanSchemaCreate,
    ) -> MplanSchema:
        try:
            moving_date_update = date_format(mplan_update.moving_date)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid date format (Expected format: YYYY-MM-DD): {e}.",
            )

        try:
            mplan = (
                db.query(models.Mplan)
                .filter(models.Mplan.id == mplan_id, models.Mplan.user_id == user_id)
                .first()
            )
            if not mplan:
                raise HTTPException(
                    status_code=404,
                    detail="Mplan not found or does not belon to the user",
                )

            mplan.moving_address = moving_date_update
            mplan.old_address = mplan_update.old_address
            mplan.new_address = mplan_update.new_address

            mplan.selected_categories = [
                models.MplanCategory(label=cat.label, is_completed=cat.is_completed)
                for cat in mplan_update.selected_categories
            ]
            mplan.modified_at = datetime.now(timezone.utc)
            db.commit()
            db.refresh(mplan)
            return mplan
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def delete_mplan(self, db: Session, mplan_id: UUID, user_id: UUID) -> MplanSchema:
        try:
            mplan = self.get_mplan(db, mplan_id, user_id)
            if not mplan:
                raise HTTPException(status_code=404, detail="MPlan not found")
            db.delete(mplan)
            db.commit()
            return mplan
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    def get_mplan(self, db: Session, mplan_id: UUID, user_id: UUID) -> MplanSchema:
        return (
            db.query(models.Mplan)
            .filter(models.Mplan.id == mplan_id, models.Mplan.user_id == user_id)
            .first()
        )
