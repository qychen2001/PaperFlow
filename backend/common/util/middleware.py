from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from common.dto.user import UserInfo
from common.enums.error_code import ErrorCode
from common.exception.auth import AuthException
from common.util.casdoor import casdoor


class TokenValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        whitelist = ["/api/user/exchange_code"]
        if request.url.path in whitelist:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise AuthException(
                error_code=ErrorCode.INVALID_TOKEN,
                detail="请求头中未包含 Authorization 字段",
            )
        if not auth_header.startswith("Bearer "):
            raise AuthException(
                error_code=ErrorCode.INVALID_TOKEN, detail="Authorization 字段格式错误"
            )
        token = auth_header[7:]
        try:
            user_info = casdoor.parse_jwt_token(token)
            if not all(k in user_info for k in ["name", "id", "email"]):
                raise AuthException(ErrorCode.USER_NOT_FOUND, detail="用户信息不完整")
            request.state.user = user_info
        except Exception as e:
            raise AuthException(ErrorCode.USER_NOT_FOUND, detail=e)

        response = await call_next(request)
        return response


def get_current_user(request: Request) -> UserInfo:
    user = getattr(request.state, "user", None)
    if not user:
        raise AuthException(ErrorCode.USER_NOT_FOUND, detail="当前用户不存在")
    return UserInfo(
        id=user.get("id"),
        name=user.get("name"),
        permission=user.get("permissions", []),
    )
