from fastapi import APIRouter
from app.api.v1 import addresses, mplan, categories, users
from app.api import health

api_router = APIRouter()
api_router.include_router(addresses.router, tags=["addresses"])
api_router.include_router(mplan.router, tags=["mplan"])
api_router.include_router(categories.router, tags=["categories"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
