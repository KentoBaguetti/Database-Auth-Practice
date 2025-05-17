from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users_test"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)
    