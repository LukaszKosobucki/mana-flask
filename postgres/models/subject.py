from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Subject(Base): 
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    name: Mapped[str] = mapped_column(String(45), nullable=False)
    field_id: Mapped[int] = mapped_column(Integer, ForeignKey("fields.id"), nullable=False) 
    