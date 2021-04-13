#!/usr/bin/env python3
'''This module contains the DB class'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from user import Base
from user import User


class DB:
    '''Database class'''
    def __init__(self):
        '''Initialization function'''
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        '''sessionmakeer function'''
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''add ser function'''
        u = User(email=email, hashed_password=hashed_password)
        self._session.add(u)
        self._session.commit()
        return u

    def find_user_by(**kwargs) -> User:
        '''Returns top row of results from pass kwargs'''
        return self._session.query(User).filter_by(**kwargs).one()
