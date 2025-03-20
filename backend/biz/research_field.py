from typing import List

from sqlalchemy.orm import Session

from common.dto.research_field import ResearchFieldModel
from dal.dao.research_field import ResearchFieldDAO


class ResearchFieldService:
    @staticmethod
    def get_research_field(db: Session, field_id: int) -> ResearchFieldModel:
        field = ResearchFieldDAO.get_by_id(db, field_id)
        return ResearchFieldModel.model_validate(field)

    @staticmethod
    def get_research_field_children(
        db: Session, parent_id: int
    ) -> List[ResearchFieldModel]:
        fields = ResearchFieldDAO.get_children(db, parent_id)
        return [ResearchFieldModel.model_validate(field) for field in fields]

    @staticmethod
    def get_hierarchical_research_fields(db: Session) -> List[ResearchFieldModel]:
        fields = ResearchFieldDAO.get_hierarchical_fields(db)
        return [ResearchFieldModel.model_validate(field) for field in fields]
