from fastapi import HTTPException, status

from common.enums.error_code import ErrorCode


class AuthException(HTTPException):
    """认证异常类"""

    def __init__(self, error_code: ErrorCode, detail: str = ""):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.error_code = error_code.value[0]
        self.detail = error_code.value[1].format(detail=detail)
        super().__init__(status_code=self.status_code, detail=self.detail)
