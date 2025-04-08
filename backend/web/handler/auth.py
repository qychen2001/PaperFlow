from typing import cast

from fastapi import Request
from fastapi.responses import JSONResponse

from common.exception.auth import AuthException


async def auth_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    exc = cast(AuthException, exc)
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.error_code, "message": exc.detail, "data": None},
    )
