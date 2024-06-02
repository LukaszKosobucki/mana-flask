from postgres.models.grade import  Grade
from flaskr.objects.grade import  ObjectGrade

class SubjectHelper:
    def __init__(self, grade):
        self.id = grade.id
        self.grade = grade.grade
        self.student_id = grade.student_id
        self.subject_id = grade.subject_id

    def jsonify(self):
        return {
            'id': self.id,
            'grade': self.grade,
            'student_id': self.student_id,
            'subject_id': self.subject_id,
        }
    
    def deserialize(self, grade: Grade) -> ObjectGrade:
        return ObjectGrade(grade)
    
    def serialize(self, grade:ObjectGrade) -> Grade:
        return Grade(grade)
    
class GradesHelper:
    def __init__(self, grades):
        self.grades = grades

    def jsonify(self):
        return [SubjectHelper(grade).jsonify() for grade in self.grades]