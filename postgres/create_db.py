from sqlalchemy import create_engine,text
import sqlalchemy

engine = create_engine("postgresql+psycopg2://test:1234@localhost:5432/test",echo=True)
engine.connect()


print("works")

