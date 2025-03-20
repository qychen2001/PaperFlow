from pydantic import BaseModel, ConfigDict


class ResearchFieldModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    short_name: str
    name: str
    description: str | None
    parent_id: int | None
    level: int
    children: list["ResearchFieldModel"] = []  # 使用前向引用
