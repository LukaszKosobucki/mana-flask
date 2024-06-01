from dataclasses import dataclass


@dataclass(frozen=True)
class ObjectStudent:
    def __init__(self, student):
        self.id: int = student.id
        self.name: str = student.name
        self.email: str = student.lastname
        self.semester: int = student.semester
        self.field_id: int = student.field_id

