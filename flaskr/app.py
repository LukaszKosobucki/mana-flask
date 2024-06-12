from flask import Flask, request
from flaskr.extensions import db
from postgres.models.student import Student
from postgres.models.degree import Degree
from flaskr.objects.degree import ObjectDegree
from postgres.models.field import Field
from postgres.models.grade import Grade
from postgres.models.subject import Subject
from flaskr.helpers.student import StudentsHelper
from flaskr.helpers.degree import DegreesHelper,DegreeHelper
from flaskr.helpers.field import FieldsHelper
from flaskr.helpers.grade import GradesHelper
from flaskr.helpers.subject import SubjectsHelper

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # change string to the name of your database; add path if necessary
    db_name = "postgres:db-123456@db:5432/university"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' + db_name

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # initialize the app with Flask-SQLAlchemy
    db.init_app(app)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    #this works like restapi almost
    @app.get('/api/v1/students')
    def students():
        try:
            students = db.session.query(Student)
            result = StudentsHelper(students).jsonify()
            return result
        except Exception as e:
            return {"error": str(e)}
    
    @app.get('/api/v1/students/<int:id>')
    def student(id): 
        try:
            student = db.session.query(Student).filter(Student.id == id)
            result = StudentsHelper(student).jsonify()
            if len(result) == 0:
                return {"error": "not found"}
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.delete("/api/v1/students/<int:id>")
    def delete_student(id):
        try:
            db.session.query(Student).filter(Student.id == id).delete()
            db.session.commit()
            return {"status_code": 200, "description": f"successfully deleted student" }
        except Exception as e:
            return {"error": str(e)}
        
    @app.post("/api/v1/students")
    def post_student():
        try: 
            json = request.get_json()
            student_name = json.get('name')
            student_lastname = json.get('lastname')
            student_semester = json.get('semester')
            student_field_id = json.get('fieldId')

            if not student_name:
                return {"error": "student name is required"}
            if not student_lastname:
                return {"error": "student lastname is required"}
            if not student_semester:
                return {"error": "student semester is required"}
            if not student_field_id:
                return {"error": "student fieldId is required"}
           
            db.session.add(Student(name=student_name, lastname=student_lastname, semester=student_semester, field_id=student_field_id))
            db.session.commit()
        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "description": f"successfully added a new student {student_name} {student_lastname}"}
        
    @app.get('/api/v1/degrees')
    def degrees():
        try:
            degrees = db.session.query(Degree)
            result = DegreesHelper(degrees).jsonify()

            return result
        except Exception as e:
            return {"error": str(e)}
    
    @app.get('/api/v1/degrees/<int:id>')
    def degree(id): 
        try:
            degree = db.session.query(Degree).filter(Degree.id == id)
            result = DegreesHelper(degree).jsonify()
            if len(result) == 0:
                return {"error": "not found"}
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.post("/api/v1/degrees")
    def post_degree():
        try: 
            json = request.get_json()
            degree_name = json.get('name')

            if not degree_name:
                return {"error": "degree name is required"}
           
            db.session.add(Degree(name=degree_name))
            db.session.commit()
        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "description": f"successfully added a new degree {degree_name}"}
    
    # @app.put("/api/v1/degrees/<int:id>")
    # def put_degrees(id):
    #     try: 
    #         json = request.get_json()
    #         degree_name = json.get('name')
    #         degree = db.session.query(Degree).filter(Degree.id == id)
    #         degree_object = DegreeHelper().deserialize(degree)
    #         degree_object.name = degree_name
    #         degree = DegreeHelper().serialize(degree_object)

    #         db.session.commit()

    #     except Exception as e:
    #         return {"error": e}
    #     return {"status_code": 200, "descritpion": f"successfully udpated degree of id {deg}"}

    @app.delete("/api/v1/degrees/<int:id>")
    def delete_degree(id):
        try:
            db.session.query(Degree).filter(Degree.id == id).delete()
            # if(degree.id != id):
            #     return {"status_code": "400", "description": "degree does not exist in db"}
            db.session.commit()
            return {"status_code": 200, "description": f"successfully deleted degree" }
        except Exception as e:
            return {"error": str(e)}

    @app.get('/api/v1/fields')
    def fields():
        try:
            fields = db.session.query(Field)
            result = FieldsHelper(fields).jsonify()
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.get('/api/v1/fields/<int:id>')
    def field(id): 
        try:
            field = db.session.query(Field).filter(Field.id == id)
            result = FieldsHelper(field).jsonify()
            if len(result) == 0:
                return {"error": "not found"}
            return result
        except Exception as e:
            return {"error": str(e)}

    @app.delete("/api/v1/fields/<int:id>")
    def delete_field(id):
        try:
            db.session.query(Field).filter(Field.id == id).delete()
            db.session.commit()
            return {"status_code": 200, "description": f"successfully deleted Field" }
        except Exception as e:
            return {"error": str(e)}
        
    @app.post("/api/v1/fields")
    def post_field():
        try: 
            json = request.get_json()
            field_name = json.get('name')
            field_degree_id = json.get('degreeId')

            if not field_name:
                return {"error": "field name is required"}
            if not field_degree_id:
                return {"error": "field degreeId is required"}
           
            db.session.add(Field(name=field_name, degree_id=field_degree_id))
            db.session.commit()
        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "description": f"successfully added a new field {field_name}"}
        
    @app.get('/api/v1/grades')
    def grades():
        try:
            grades = db.session.query(Grade)
            result = GradesHelper(grades).jsonify()
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.get('/api/v1/grades/<int:id>')
    def grade(id): 
        try:
            grade = db.session.query(Grade).filter(Grade.id == id)
            result = GradesHelper(grade).jsonify()
            if len(result) == 0:
                return {"error": "not found"}
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.delete("/api/v1/grades/<int:id>")
    def delete_grade(id):
        try:
            db.session.query(Grade).filter(Grade.id == id).delete()
            db.session.commit()
            return {"status_code": 200, "description": f"successfully deleted Grade" }
        except Exception as e:
            return {"error": str(e)}       
        
    @app.post("/api/v1/grades")
    def post_grade():
        try: 
            json = request.get_json()
            grade_grade = json.get('grade')
            grade_student_id = json.get('studentId')
            grade_subject_id = json.get('subjectId')

            if not grade_grade:
                return {"error": "grade is required"}
            if not grade_student_id:
                return {"error": "grade studentId is required"}
            if not grade_subject_id:
                return {"error": "grade subjectId is required"}
           
            db.session.add(Grade(grade=grade_grade, student_id=grade_student_id, subject_id=grade_subject_id))
            db.session.commit()
        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "description": f"successfully added a new grade {grade_grade}"}

    @app.get('/api/v1/subjects')
    def subjects():
        try:
            subjects = db.session.query(Subject)
            result = SubjectsHelper(subjects).jsonify()
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.get('/api/v1/subjects/<int:id>')
    def subject(id): 
        try:
            subject = db.session.query(Subject).filter(Subject.id == id)
            result = SubjectsHelper(subject).jsonify()
            if len(result) == 0:
                return {"error": "not found"}
            return result
        except Exception as e:
            return {"error": str(e)}
        
    @app.delete("/api/v1/subjects/<int:id>")
    def delete_subject(id):
        try:
            db.session.query(Subject).filter(Subject.id == id).delete()
            db.session.commit()
            return {"status_code": 200, "description": f"successfully deleted Subject" }
        except Exception as e:
            return {"error": str(e)}  
        
    @app.post("/api/v1/subjects")
    def post_subject():
        try: 
            json = request.get_json()
            subject_name = json.get('name')
            subject_field_id = json.get('fieldId')

            if not subject_name:
                return {"error": "subject name is required"}
            if not subject_field_id:
                return {"error": "subject fieldId is required"}
           
            db.session.add(Subject(name=subject_name, field_id=subject_field_id))
            db.session.commit()
        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "description": f"successfully added a new Subject {subject_name}"}

    return app
