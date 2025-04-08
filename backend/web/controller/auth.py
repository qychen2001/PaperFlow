from fastapi import APIRouter, Depends

from common.dto.auth import (
    CodeTokenExchangeParam,
    GetAccessTokenDetail,
    GetUserInfoDetail,
)
from common.enums.error_code import ErrorCode
from common.exception.auth import AuthException
from common.utils.casdoor import casdoor
from common.utils.middleware import get_current_user
from web.vo.result import Result

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/exchange_code")
async def exchange_code(request: CodeTokenExchangeParam):
    try:
        token = casdoor.get_oauth_token(code=request.code)
        access_token = token.get("access_token", None)
        token_type = token.get("token_type", None)
        if not access_token or not token_type:
            raise AuthException(ErrorCode.TOKEN_ERROR, detail="获取Access Token失败")
        return Result.success(
            data=GetAccessTokenDetail(access_token=access_token, token_type=token_type)
        )
    except Exception:
        raise AuthException(ErrorCode.TOKEN_ERROR, detail="获取Access Token失败")


@router.get("/userinfo")
async def get_userinfo(current_user: GetUserInfoDetail = Depends(get_current_user)):
    return Result.success(data=current_user)
