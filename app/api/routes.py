from fastapi import APIRouter
from app.api.v1 import addresses
from app.api import health

api_router = APIRouter()
api_router.include_router(addresses.router, tags=["addresses"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
