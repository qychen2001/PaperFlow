from pydantic import BaseModel


class CodeExchange(BaseModel):
    code: str
    state: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class UserInfo(BaseModel):
    id: str
    name: str
    permission: list[str]
