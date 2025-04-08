from typing import ClassVar, Optional

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from common.enums.error_code import ErrorCode


class Result(BaseModel):
    code: int
    message: str
    data: Optional[dict] = None

    SUCCESS_CODE: ClassVar[int] = 0
    SUCCESS_MESSAGE: ClassVar[str] = "成功"

    @classmethod
    def success(cls, data: Optional[BaseModel | dict] = None) -> JSONResponse:
        dict_data = data.model_dump() if isinstance(data, BaseModel) else data
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "code": cls.SUCCESS_CODE,
                "message": cls.SUCCESS_MESSAGE,
                "data": dict_data,
            },
        )

    @classmethod
    def error(cls, status_code: int, code: ErrorCode, detail: str) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "code": code.value[0],
                "message": code.value[1].format(detail=detail),
                "data": None,
            },
        )
