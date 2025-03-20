from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from biz.research_field import ResearchFieldService
from common.dto.research_field import ResearchFieldModel
from dal.database import get_db

router = APIRouter(prefix="/api/field", tags=["research_filed"])


@router.get("/", response_model=ResearchFieldModel)
async def get_research_field_by_id(
    field_id: int,
    db: Session = Depends(get_db),
):
    return ResearchFieldService.get_research_field(db, field_id)


@router.get("/children", response_model=list[ResearchFieldModel])
async def get_research_fields_with_parent_id(
    parent_id: int,
    db: Session = Depends(get_db),
):
    return ResearchFieldService.get_research_field_children(db, parent_id)


@router.get("/all", response_model=list[ResearchFieldModel])
async def get_research_fields(
    db: Session = Depends(get_db),
):
    return ResearchFieldService.get_hierarchical_research_fields(db)
