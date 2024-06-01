from postgres.models.student import  Student
from flaskr.objects.student import  ObjectStudent 

class StudentHelper:
    def __init__(self, student):
        self.id = student.id
        self.name = student.name
        self.lastname = student.lastname
        self.semester = student.semester
        self.field_id = student.field_id

    def jsonify(self): #return json object (for get reuqests)
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'semester': self.semester,
            'field_id': self.field_id
        }
    
    def deserialize(self, student: Student) -> ObjectStudent: #return dataclass object
        return ObjectStudent(student)
    
    def serialize(self, student: ObjectStudent) -> Student: #return database object
        return Student(student)

class StudentsHelper:
    def __init__(self, students):
        self.students = students

    def jsonify(self):
        return [StudentHelper(student).jsonify() for student in self.students]