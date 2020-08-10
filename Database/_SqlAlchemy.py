#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'

from sqlalchemy import Column, String, create_engine, Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from json import dumps
from random import randint
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    score = Column(Integer)
    books = relationship('Books')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(50), nullable=False)
    user_id = Column(String(20), ForeignKey('user.id'), nullable=False)


engine = create_engine(
    'mysql+mysqlconnector://root:123456@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()
#new_user = User(id='A-004',name='Angela',score = randint(0,100))
# session.add(new_user)
# session.commit()

user = session.query(User).filter(User.id=='A-001').one()
s = dumps(user,default = lambda obj: obj.as_dict())
print(s)