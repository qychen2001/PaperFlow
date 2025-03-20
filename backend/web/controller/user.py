from fastapi import APIRouter, Depends

from common.dto.user import AccessToken, CodeExchange, UserInfo
from common.enums.error_code import ErrorCode
from common.exception.auth import AuthException
from common.util.casdoor import casdoor
from common.util.middleware import get_current_user
from web.vo.result import Result

router = APIRouter(prefix="/api/user", tags=["user"])


@router.post("/exchange_code")
async def exchange_code(request: CodeExchange):
    try:
        token = casdoor.get_oauth_token(code=request.code)
        access_token = token.get("access_token", None)
        token_type = token.get("token_type", None)
        return Result.success(
            data=AccessToken(access_token=access_token, token_type=token_type)
        )
    except Exception:
        raise AuthException(ErrorCode.OTHER_AUTH_ERROR, detail="获取access_token失败")


@router.get("/userinfo", response_model=UserInfo)
async def get_userinfo(current_user: UserInfo = Depends(get_current_user)):
    return Result.success(data=current_user)
