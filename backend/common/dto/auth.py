from typing import Optional

from pydantic import BaseModel


class GetUserInfoDetail(BaseModel):
    id: str
    name: str
    permission: Optional[list[str]]


class GetAccessTokenDetail(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]


class CodeTokenExchangeParam(BaseModel):
    code: str
    state: str
