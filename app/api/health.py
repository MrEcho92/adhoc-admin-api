from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def health_check() -> Response:
    return JSONResponse(content={"status": "OK"})
