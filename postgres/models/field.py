from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base


class Field(Base): 
    __tablename__ = 'fields'
    id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] 
    degree_id: Mapped[int] = mapped_column(ForeignKey("degrees.id")) 

    