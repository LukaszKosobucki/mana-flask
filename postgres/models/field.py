from sqlalchemy import Integer, ForeignKey,String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Field(Base): 
    __tablename__ = 'fields'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    degree_id: Mapped[int] = mapped_column(Integer, ForeignKey("degrees.id"), nullable=False) 
