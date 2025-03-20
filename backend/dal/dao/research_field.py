from sqlalchemy.orm import Session

from dal.po.research_field import ResearchField


class ResearchFieldDAO:
    @staticmethod
    def get_by_id(db: Session, field_id: int) -> ResearchField:
        return db.query(ResearchField).filter(ResearchField.id == field_id).first()

    @staticmethod
    def get_children(db: Session, parent_id: int) -> list[ResearchField]:
        return (
            db.query(ResearchField).filter(ResearchField.parent_id == parent_id).all()
        )

    @staticmethod
    def get_hierarchical_fields(db: Session) -> list[ResearchField]:
        # 获取顶层领域（没有父领域的研究领域）
        # SQLAlchemy的relationship会自动加载children关系
        # 由于已经定义了parent-children关系，不需要手动构建层级
        return db.query(ResearchField).filter(ResearchField.parent_id.is_(None)).all()
