from flaskr.extensions import db
from dataclasses import dataclass

@dataclass
class Degree(db.Model):
    __tablename__ = 'degrees'

    id: int
    name: str

    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

