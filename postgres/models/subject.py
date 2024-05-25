from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Subject(Base): 
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] 
    field_id: Mapped[int] = mapped_column(ForeignKey("fields.id")) 
    