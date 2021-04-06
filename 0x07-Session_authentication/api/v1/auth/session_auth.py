#!/usr/bin/env python3
'''This module contains the SessionAuth class'''
from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    '''The session authorization class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''This is the create session function'''
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        self.id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''This function returns the value of the '''
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''Returns the current user'''
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        '''Logoing function'''
        if request is None:
            return False
        if self.session_cookie(request) is None:
            return False
        if self.user_id_for_session_id(session_id) is none:
            return False
        del self.user_id_by_session_id[session_id]
        return True
