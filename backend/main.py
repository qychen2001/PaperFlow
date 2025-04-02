import uvicorn
from fastapi import FastAPI

from settings import settings

app = FastAPI(title="PaperFlow API", version="0.0.0")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
