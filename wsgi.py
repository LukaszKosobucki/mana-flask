from flaskr.app import create_app
from postgres.create_db import create_table

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8000, debug=True)
