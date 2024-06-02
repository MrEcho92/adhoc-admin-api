from fastapi import APIRouter

router = APIRouter()


@router.get("/addresses/")
async def get_addresses(postcode: str):
    return [{"postcode": postcode}]
