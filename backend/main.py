import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from common.exception.auth import AuthException
from common.util.middleware import TokenValidatorMiddleware
from settings import settings
from web.controller.user import router as user_router
from web.handler.auth import auth_exception_handler

app = FastAPI(title="PaperFlow API", version="1.0.0")

app.add_middleware(TokenValidatorMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(AuthException, auth_exception_handler)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=True)
