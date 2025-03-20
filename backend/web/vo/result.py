from typing import ClassVar, Optional

from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Result(BaseModel):
    code: int
    message: str
    data: Optional[dict] = None

    SUCCESS_CODE: ClassVar[int] = 0
    SUCCESS_MESSAGE: ClassVar[str] = "成功"

    @classmethod
    def success(cls, data: Optional = None) -> JSONResponse:
        if hasattr(data, "dict") and callable(data.dict):
            data = data.dict()
        return JSONResponse(
            status_code=200,
            content=Result(
                code=Result.SUCCESS_CODE, message=Result.SUCCESS_MESSAGE, data=data
            ).dict(),
        )
