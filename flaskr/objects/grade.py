from dataclasses import dataclass

@dataclass(frozen=True)
class ObjectGrade:
    def __init__(self, grade):
        self.id: int = grade.id
        self.grade: int = grade.grade
        self.student_id: int = grade.student_id
        self.subject_id: int = grade.subject_id


