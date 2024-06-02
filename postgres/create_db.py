from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import sys
sys.path.append("")
from postgres.models.student import Student
from postgres.models.degree import Degree
from postgres.models.field import Field
from postgres.models.grade import Grade
from postgres.models.subject import Subject
from postgres.models.base import Base


def create_table():
    engine = create_engine(
        "postgresql+psycopg2://postgres:db-123456@db:5432/university", echo=True)

    Session = sessionmaker(bind=engine) 
    session = Session() 

    Field.children = relationship('Degree', order_by=Degree.id)
    Student.children = relationship('Field', order_by=Field.id)
    Subject.children = relationship('Field', order_by=Field.id)
    Grade.children = relationship('Student', order_by=Student.id)
    Grade.children = relationship('Subject', order_by=Subject.id)


    Base.metadata.create_all(engine) 

    degrees_len = session.query(Degree).all()
    if len(degrees_len) == 0:
        degrees = [
            {'name': 'Bachelor'},
            {'name': 'Engineer'},
            {'name': 'Master'},
            {'name': 'Doctorate'},
        ]
        session.bulk_insert_mappings(Degree, degrees)
        session.commit()

    fields_len = session.query(Field).all()
    if len(fields_len) == 0:
        fields = [
            {'name': 'Enterpreneurship', "degree_id": 1},
            {'name': 'Management', "degree_id": 1},
            {'name': 'Computer Science', "degree_id": 2},
            {'name': 'Mechanics and Termodynamics', "degree_id": 2},
        ]
        session.bulk_insert_mappings(Field, fields)
        session.commit()


    students_len = session.query(Student).all()
    if len(students_len) == 0:
        students = [
            {'name': 'Rajiv', 'lastname': 'Khanna', 'semester': 1, 'field_id': 1},
            {'name': 'Komal', 'lastname': 'Bhandari', 'semester': 5, 'field_id': 2},
            {'name': 'Abdul', 'lastname': 'Sattar', 'semester': 1, 'field_id': 3},
            {'name': 'Priya', 'lastname': 'Rajhans', 'semester': 2, 'field_id': 4},
        ]
        session.bulk_insert_mappings(Student, students)
        session.commit()

    subjects_len = session.query(Subject).all()
    if len(subjects_len) == 0:
        subjects = [
            {'name': 'Enterpreneurship in Company', 'field_id': 1},
            {'name': 'Management in Company', 'field_id': 2},
            {'name': 'Algorithms', 'field_id': 3},
            {'name': 'Termodynamics', 'field_id': 4},
        ]
        session.bulk_insert_mappings(Subject, subjects)
        session.commit()

    grades_len = session.query(Grade).all()
    if len(grades_len) == 0:
        grades = [
            {'grade': '2', 'student_id': 1, 'subject_id': 1},
            {'grade': '3', 'student_id': 2, 'subject_id': 2},
            {'grade': '4', 'student_id': 3, 'subject_id': 3},
            {'grade': '5', 'student_id': 4, 'subject_id': 4},
        ]
        session.bulk_insert_mappings(Grade, grades)
        session.commit()

    session.close()
    


if __name__ == "__main__":
    create_table()