from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Student(Base): 
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] 
    lastname: Mapped[str] 
    semester: Mapped[int]
    field_id: Mapped[int] = mapped_column(ForeignKey("fields.id"))