from fastapi import HTTPException

from common.enums.error_code import ErrorCode


class ServerException(HTTPException):
    def __init__(self, error_code: ErrorCode, detail: str = None):
        self.status_code = 500
        self.error_code = error_code.value[0]
        self.detail = error_code.value[1].format(detail=detail)
        super().__init__(status_code=self.status_code, detail=self.detail)
