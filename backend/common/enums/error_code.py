from enum import Enum


class ErrorCode(Enum):
    # 用户校验相关异常（401）
    USER_NOT_FOUND = (401001, "用户未找到：{detail}")
    INVALID_TOKEN = (401002, "非法Token：{detail}")
    OTHER_AUTH_ERROR = (401003, "其他认证错误：{detail}")

    # 资源相关异常（404）
    RESOURCE_NOT_FOUND = (404001, "资源未找到：{detail}")
    PAGE_NOT_FOUND = (404002, "页面未找到：{detail}")

    # 服务器相关异常（500）
    INTERNAL_SERVER_ERROR = (500001, "服务器内部错误：{detail}")
    DATABASE_ERROR = (500002, "数据库错误：{detail}")
    EXTERNAL_SERVICE_ERROR = (500003, "外部服务错误：{detail}")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
