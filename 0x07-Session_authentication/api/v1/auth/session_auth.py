#!/usr/bin/env python3
'''This module contains the SessionAuth class'''
from .auth import Auth
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