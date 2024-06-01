from postgres.models.field import  Field
from flaskr.objects.field import  ObjectField 

class FieldHelper:
    def __init__(self, field):
        self.id = field.id
        self.name = field.name
        self.degree_id = field.degree_id

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
            'degree_id': self.degree_id,
        }
    
    def deserialize(self, degree: Field) -> ObjectField:
        return ObjectField(degree)
    
    def serialize(self, degree:ObjectField) -> Field:
        return Field(degree)
    
    

class FieldsHelper:
    def __init__(self, fields):
        self.fields = fields

    def jsonify(self):
        return [FieldHelper(field).jsonify() for field in self.fields]