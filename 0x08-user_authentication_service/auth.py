#!/usr/bin/env python3
'''This module contains the Auth class and related functions'''
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    '''This function Returns a hashed user password'''
    if password and isinstance(password, str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(str.encode(password), salt)
    return None


def _generate_uuid() -> str:
    '''This function returns a string of uuid'''
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        '''Initalize the auth object'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''This functions registers user'''
        try:
            if self._db.find_user_by(email=email):
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        '''This function validates user login'''
        try:
            if self._db.find_user_by(email=email):
                hashed = self._db.find_user_by(email=email).hashed_password
                if bcrypt.checkpw(password.encode(), hashed):
                    return True
                else:
                    return False
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        '''This creates a login session'''
        try:
            u = self._db.find_user_by(email=email)
            s_id = _generate_uuid()
            setattr(u, "session_id", s_id)
            return s_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: int) -> Union[User, None]:
        '''Gets user from session ID'''
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''This function destroys a user session'''
        try:
            u = self._db.find_user_by(id=user_id)
            self._db.update_user(u.id, {"session_id": None})
            return None
        except NoResultFound:
            return None
