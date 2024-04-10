from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


def create_table():
    engine = create_engine(
        "postgresql+psycopg2://postgres:db-123456@db:5432/test", echo=True)
    meta = MetaData()

    students = Table(
        'students', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('lastname', String),
    )

    meta.create_all(engine)

    # ins = students.insert().values(name='daniel', lastname='kowalski')

    connection = engine.connect()
    # result = connection.execute(ins)

    result = connection.execute(students.insert(), [
        {'name': 'Rajiv', 'lastname': 'Khanna'},
        {'name': 'Komal', 'lastname': 'Bhandari'},
        {'name': 'Abdul', 'lastname': 'Sattar'},
        {'name': 'Priya', 'lastname': 'Rajhans'},
    ])

    print(result.rowcount)
    connection.commit()
    connection.close()
    print("works")


create_table()
