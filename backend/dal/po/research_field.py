from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from dal.database import Base


class ResearchField(Base):
    __tablename__ = "research_field"

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_name = Column(String(50), nullable=False)
    name = Column(String(100), nullable=True)
    description = Column(String(5000), nullable=True)
    parent_id = Column(Integer, ForeignKey("research_field.id"), nullable=True)
    level = Column(Integer, nullable=False)  # 1: 一级领域, 2: 二级领域

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # 自引用关系
    parent = relationship("ResearchField", remote_side=[id], backref="children")
