from flask import Flask, jsonify
from flaskr.extensions import db
from postgres.models.student import Student
from postgres.models.degree import Degree
from postgres.models.field import Field
from postgres.models.grade import Grade
from postgres.models.subject import Subject
from flaskr.helpers.student import StudentsHelper
from flaskr.helpers.degree import DegreesHelper
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
        
    @app.get('/api/v1/degrees')
    def degrees():
        try:
            degrees = db.session.query(Degree)
            result = DegreesHelper(degrees).jsonify()
            return result
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
        
    @app.get('/api/v1/grades')
    def grades():
        try:
            grades = db.session.query(Grade)
            result = GradesHelper(grades).jsonify()
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

    return app
