from enum import Enum


class ErrorCode(Enum):
    """错误码枚举类，用于统一管理系统中的错误码和错误消息"""

    def __init__(self, code: int, message: str):
        self.code: int = code
        self.message: str = message

    # 通用错误 (1000-1999)
    SUCCESS = (1000, "操作成功：{detail}")
    FAILED = (1001, "操作失败：{detail}")
    UNKNOWN_ERROR = (1002, "未知错误：{detail}")
    SERVICE_UNAVAILABLE = (1003, "服务不可用：{detail}")
    OPERATION_TIMEOUT = (1004, "操作超时：{detail}")

    # 认证与授权错误 (2000-2099)
    UNAUTHORIZED = (2000, "未授权，请先登录：{detail}")
    LOGIN_FAILED = (2001, "登录失败，用户名或密码错误：{detail}")
    TOKEN_ERROR = (2002, "令牌无效或已过期：{detail}")
    PERMISSION_DENIED = (2003, "权限不足，无法访问：{detail}")
    ACCOUNT_ERROR = (2004, "账号状态异常：{detail}")

    # 资源错误 (3000-3099)
    RESOURCE_NOT_FOUND = (3000, "请求的资源不存在：{detail}")
    RESOURCE_ALREADY_EXISTS = (3001, "资源已存在：{detail}")
    RESOURCE_STATUS_ERROR = (3002, "资源状态异常：{detail}")

    # 参数错误 (4000-4099)
    PARAMETER_ERROR = (4000, "参数错误：{detail}")
    MISSING_PARAMETER = (4001, "缺少必要参数：{detail}")
    INVALID_FORMAT = (4002, "格式无效：{detail}")

    # 业务逻辑错误 (5000-5099)
    BUSINESS_ERROR = (5000, "业务处理失败：{detail}")
    OPERATION_NOT_ALLOWED = (5001, "操作不允许：{detail}")
    OPERATION_CONFLICT = (5002, "操作冲突：{detail}")

    # 系统错误 (6000-6099)
    SYSTEM_ERROR = (6000, "系统错误：{detail}")
    INTERNAL_ERROR = (6001, "内部错误：{detail}")
    CONFIG_ERROR = (6002, "配置错误：{detail}")

    # 网络和连接错误 (7000-7099)
    NETWORK_ERROR = (7000, "网络错误：{detail}")
    CONNECTION_ERROR = (7001, "连接错误：{detail}")

    # 数据错误 (8000-8099)
    DATABASE_ERROR = (8000, "数据库错误：{detail}")
    DATA_INTEGRITY_ERROR = (8001, "数据完整性错误：{detail}")

    # 文件错误 (9000-9099)
    FILE_ERROR = (9000, "文件操作错误：{detail}")
    FILE_NOT_FOUND = (9001, "文件不存在：{detail}")
    FILE_FORMAT_ERROR = (9002, "文件格式错误：{detail}")

    # 第三方服务错误 (10000-10099)
    THIRD_PARTY_ERROR = (10000, "第三方服务错误：{detail}")
    API_ERROR = (10001, "API调用失败：{detail}")
    EXTERNAL_SERVICE_ERROR = (10002, "外部服务错误：{detail}")
