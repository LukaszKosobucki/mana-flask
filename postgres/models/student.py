from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base
from dataclasses import dataclass


class Student(Base): 
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] = mapped_column(String(30),nullable=False)
    lastname: Mapped[str] = mapped_column(String(30), nullable=False)
    semester: Mapped[int] = mapped_column(Integer, nullable=False)
    field_id: Mapped[int] = mapped_column(Integer, ForeignKey("fields.id"), nullable=False)

