from typing import Any
from fastapi import APIRouter
from app.schema.mplan_schema import MplanSchema, CreateMplanSchema
from app.services.mplan_service import MplanService

router = APIRouter()

mplan_service = MplanService()


@router.get("/mplan/{id}", response_model=MplanSchema)
async def get_mplan(id: str) -> Any:
    item = await mplan_service.get_mplan_by_id(id)
    return item


@router.get("/mplans", response_model=list[MplanSchema])
async def get_mplans(user_id: str) -> Any:
    items = mplan_service.get_mplans(user_id)
    return items


@router.post("/mplan/create", status_code=201)
async def create_mplan(mplan: CreateMplanSchema) -> Any:
    created_item = mplan_service.create_mplan(mplan)
    return created_item


@router.put("/mplan")
async def update_mplan() -> Any:
    pass


@router.delete("/mplan/{id}")
async def delete_mplan() -> Any:
    pass
