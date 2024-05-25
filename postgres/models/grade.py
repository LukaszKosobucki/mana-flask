from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Grade(Base): 
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    grade: Mapped[int] 
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id")) 
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id")) 

    