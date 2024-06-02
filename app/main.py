from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import settings


def create_application():
    app = FastAPI()

    app.include_router(api_router)

    origins = (
        ["*"] if settings.ENV == "dev" else settings.BACKEND_CORS_ORIGINS
    )  # add only FE url in production

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    return app


app = create_application()
