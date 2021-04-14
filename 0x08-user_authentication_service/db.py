#!/usr/bin/env python3
'''This module contains the DB class'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User


class DB:
    '''This is the Database class'''
    def __init__(self):
        '''Initialization function'''
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        '''This is the sessionmakeer function'''
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

    def find_user_by(self, **kwargs) -> User:
        '''Returns top row of results from pass kwargs'''
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        '''
        This function gets the object via ID then loops through kwargs
        to update values
        '''
        u = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if hasattr(User, k):
                setattr(u, k, v)
            else:
                raise ValueError
        self._session.commit()
        return None
