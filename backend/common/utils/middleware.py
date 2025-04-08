from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware

from common.dto.auth import GetUserInfoDetail
from common.enums.error_code import ErrorCode
from common.exception.auth import AuthException
from common.utils.casdoor import casdoor
from web.vo.result import Result


class TokenValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        whitelist = ["/api/auth/exchange_code"]
        if request.url.path in whitelist:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return Result.error(
                status_code=status.HTTP_401_UNAUTHORIZED,
                code=ErrorCode.TOKEN_ERROR,
                detail="请求头中未包含 Authorization 字段",
            )
        if not auth_header.startswith("Bearer "):
            return Result.error(
                status_code=status.HTTP_401_UNAUTHORIZED,
                code=ErrorCode.TOKEN_ERROR,
                detail="Authorization 字段格式错误",
            )
        token = auth_header[7:]
        try:
            user_info = casdoor.parse_jwt_token(token)
            if not all(k in user_info for k in ["name", "id", "email"]):
                return Result.error(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    code=ErrorCode.ACCOUNT_ERROR,
                    detail="用户信息不完整",
                )
            request.state.user = user_info
        except Exception as e:
            return Result.error(
                status_code=status.HTTP_401_UNAUTHORIZED,
                code=ErrorCode.LOGIN_FAILED,
                detail=str(e),
            )

        response = await call_next(request)
        return response


def get_current_user(request: Request) -> GetUserInfoDetail:
    user = getattr(request.state, "user", None)
    if not user:
        raise AuthException(ErrorCode.LOGIN_FAILED, detail="当前用户不存在")
    return GetUserInfoDetail(
        id=user.get("id"),
        name=user.get("name"),
        permission=user.get("permissions", []),
    )
