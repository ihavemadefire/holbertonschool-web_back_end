#!/usr/bin/env python3
'''This module contains the DB class'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
fromt typing import TypeVar

from user import Base
from user import User


class DB:

    def __init__(self):
        '''Initialization function'''
        self._engine = create_engine("sqlite:///a.db", echo=True)
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

    def add_user(self, email: str, hashed_password: str) -> TypeVar(User):
        '''add ser function'''
        u = User()
        u.email = email
        u.hashed_password = hashed_password
        self._session.add(u)
        self._session.commit()
        return u

        