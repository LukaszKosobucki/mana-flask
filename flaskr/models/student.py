from flaskr.extensions import db
from dataclasses import dataclass

@dataclass
class Student(db.Model):
    __tablename__ = 'students'

    id: int
    name: str
    lastname: str

    id = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    semester = db.Column(db.Integer(), nullable=False)
    field_id = db.Column(db.Integer(), nullable=False, unique=True, foreign_key=True)
