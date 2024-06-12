from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from postgres.models.base import Base
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as pgEnum


# class Degree(str, Enum):
#     Bachelor = "Bachelor"
#     Engineer = "Engineer"
#     Master = "Master"
#     Doctorate = "Doctorate"
#     Habilitate = "Habilitate"

# DegreeType: pgEnum = pgEnum(
#     Degree,
#     name="campaignstatus",
#     create_constraint=True,
#     metadata=Base.metadata,
#     validate_strings=True,
# )

# nie potrafie tego zrobić żeby działało z enumem, TODO: spytać Ani

class Degree(Base): 
    __tablename__ = 'degrees'

    id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False) 
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    