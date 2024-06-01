from postgres.models.degree import  Degree
from flaskr.objects.degree import  ObjectDegree 

class DegreeHelper:
    def __init__(self, degree):
        self.id = degree.id
        self.name = degree.name

    def jsonify(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
    def deserialize(self, degree: Degree) -> ObjectDegree:
        return ObjectDegree(degree)
    
    def serialize(self, degree:ObjectDegree) -> Degree:
        return Degree(degree)
    
    

class DegreesHelper:
    def __init__(self, degrees):
        self.degrees = degrees

    def jsonify(self):
        return [DegreeHelper(degree).jsonify() for degree in self.degrees]