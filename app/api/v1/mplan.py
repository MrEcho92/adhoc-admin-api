from typing import Any
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schema.mplan_schema import MplanSchema, MplanSchemaCreate, MplanDetailSchema
from app.services.mplan_service import MplanService
from app.db.database import get_db

router = APIRouter()

mplan_service = MplanService()


@router.get("/mplans", response_model=list[MplanSchema], status_code=status.HTTP_200_OK)
async def get_mplans_by_user_id(user_id: UUID, db: Session = Depends(get_db)) -> Any:
    try:
        return mplan_service.get_mplan_by_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user mplans: {e}")


@router.get(
    "/mplans/detail", response_model=MplanDetailSchema, status_code=status.HTTP_200_OK
)
async def get_mplan_details(
    mplan_id: UUID,
    user_id: UUID,
    county: str,
    district: str,
    country: str,
    town_or_city: str,
    db: Session = Depends(get_db),
) -> Any:
    address_info = {
        "county": county,
        "district": district,
        "country": country,
        "town_or_city": town_or_city,
    }
    try:
        return mplan_service.get_mplan_details(db, mplan_id, user_id, address_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting mplan detail: {e}")


@router.post(
    "/mplan/create", response_model=MplanSchema, status_code=status.HTTP_201_CREATED
)
async def create_mplan(mplan: MplanSchemaCreate, db: Session = Depends(get_db)) -> Any:
    try:
        created_mplan = mplan_service.create_mplan(db, mplan)
        return created_mplan
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating mplan: {e}")


@router.put("/mplans", response_model=MplanSchema, status_code=status.HTTP_200_OK)
async def update_mplan(
    mplan_id: UUID,
    user_id: UUID,
    mplan_update: MplanSchemaCreate,
    db: Session = Depends(get_db),
) -> Any:
    try:
        return mplan_service.update_mplan(db, mplan_id, user_id, mplan_update)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating mplan: {e}")


@router.delete("/mplans", status_code=status.HTTP_200_OK)
async def delete_mplan(
    mplan_id: UUID, user_id: UUID, db: Session = Depends(get_db)
) -> Any:
    try:
        mplan_service.delete_mplan(db, mplan_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting mplan: {e}")
