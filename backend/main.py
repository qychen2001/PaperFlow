import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from common.exception.auth import AuthException
from common.utils.middleware import TokenValidateMiddleware
from settings import settings
from web.controller import auth_router
from web.handler import auth_exception_handler

app = FastAPI(title="PaperFlow API", version="0.0.0")

app.add_middleware(TokenValidateMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(AuthException, auth_exception_handler)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
