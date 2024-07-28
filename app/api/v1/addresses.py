from typing import Any
from fastapi import APIRouter
from app.services.addresses_service import AddressesService

router = APIRouter()

address_service = AddressesService()


@router.get("/addresses/{post_code}")
async def get_addresses(post_code: str) -> Any:
    addresses = address_service.get_addresses(post_code)
    return addresses
