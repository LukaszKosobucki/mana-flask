from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base() 

class Student(Base): 
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True) 
    name = Column(String) 
    lastname = Column(String) 