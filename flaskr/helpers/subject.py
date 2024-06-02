from postgres.models.subject import  Subject
from flaskr.objects.subject import  ObjectSubject

class SubjectHelper:
    def __init__(self, subject):
        self.id = subject.id
        self.name = subject.name
        self.field_id = subject.field_id

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'field_id': self.field_id,
        }
    
    def deserialize(self, subject: Subject) -> ObjectSubject:
        return ObjectSubject(subject)
    
    def serialize(self, subject:ObjectSubject) -> Subject:
        return Subject(subject)
    
    

class SubjectsHelper:
    def __init__(self, subjects):
        self.subjects = subjects

    def jsonify(self):
        return [SubjectHelper(subject).jsonify() for subject in self.subjects]