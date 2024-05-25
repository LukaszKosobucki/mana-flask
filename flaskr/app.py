from flask import Flask, jsonify
from flaskr.extensions import db
from flaskr.models.student import Student

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # change string to the name of your database; add path if necessary
    db_name = "postgres:db-123456@db:5432/students"

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
    @app.route('/test')
    def test():
        try:
            # students = db.session.query(Students).all()
            students = Student.query.all()
            return jsonify(students)
        except Exception as e:
        # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text
    


    return app
