from sqlalchemy import (Column, Date, ForeignKey, Integer, Numeric, String, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True) #добавить валидацию на имаил
    password_hash = Column(String)