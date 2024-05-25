from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import sys
sys.path.append("")
from postgres.models.student import Student, Base

def create_table():
    engine = create_engine(
        "postgresql+psycopg2://postgres:db-123456@db:5432/students", echo=True)

    Session = sessionmaker(bind=engine) 
    session = Session() 
    # meta = MetaData()

    # students = Table(
    #     'students', meta,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String),
    #     Column('lastname', String),
    # )

    # meta.create_all(engine)

    Base.metadata.create_all(engine) 
    
    # ins = students.insert().values(name='daniel', lastname='kowalski')

    # connection = engine.connect()

#  

    students_len = session.query(Student).all()
    print("sdfasdfasdf", len(students_len))
    if len(students_len) == 0:
        print("asdfaskdjfhjasdhfjkashfjklhas", len(students_len))
        students = [
            {'name': 'Rajiv', 'lastname': 'Khanna'},
            {'name': 'Komal', 'lastname': 'Bhandari'},
            {'name': 'Abdul', 'lastname': 'Sattar'},
            {'name': 'Priya', 'lastname': 'Rajhans'},
        ]
        session.bulk_insert_mappings(Student, students)
        session.commit()
    session.commit()
    session.close()
    
    # result = connection.execute(ins)

    # result = connection.execute(students.insert(), [
    #     {'name': 'Rajiv', 'lastname': 'Khanna'},
    #     {'name': 'Komal', 'lastname': 'Bhandari'},
    #     {'name': 'Abdul', 'lastname': 'Sattar'},
    #     {'name': 'Priya', 'lastname': 'Rajhans'},
    # ])

    # print(result.rowcount)
    # connection.commit()
    # connection.close()



if __name__ == "__main__":
    create_table()