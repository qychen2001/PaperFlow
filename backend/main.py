import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import settings

app = FastAPI(title="PaperFlow API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=True)
