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
    def post_degrees():
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
    
    @app.put("/api/v1/degrees/<int:id>")
    def put_degrees(id):
        try: 
            json = request.get_json()
            degree_name = json.get('name')
            degree = db.session.query(Degree).filter(Degree.id == id)
            degree_object = DegreeHelper().deserialize(degree)
            degree_object.name = degree_name
            degree = DegreeHelper().serialize(degree_object)

            db.session.commit()

        except Exception as e:
            return {"error": e}
        return {"status_code": 200, "descritpion": f"successfully udpated degree of id {deg}"}

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

    return app
