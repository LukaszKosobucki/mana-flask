from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Grade(Base): 
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"), nullable=False) 
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"), nullable=False) 

    