#!/usr/bin/env python3
'''This module contains the book of amun ra'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    '''Returns a hashed user password'''
    if password and isinstance(password, str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(str.encode(password), salt)
    return None


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        '''Initalize the auth object'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Registers user'''
        try:
            if self._db.find_user_by(email=email):
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))
