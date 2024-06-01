from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as pgEnum


class Degree(str, Enum):
    Bachelor = "Bachelor"
    Engineer = "Engineer"
    Master = "Master"
    Doctorate = "Doctorate"

DegreeType: pgEnum = pgEnum(
    Degree,
    name="campaignstatus",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)

class Degree(Base): 
    __tablename__ = 'degrees'

    id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False) 
    name = mapped_column(DegreeType, nullable=False)

    