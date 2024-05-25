from flaskr.extensions import db
from dataclasses import dataclass

@dataclass
class Student(db.Model):
    id: int
    name: str
    lastname: str

    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
