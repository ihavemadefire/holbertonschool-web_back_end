#!/usr/bin/env python3
'''This module contains the SessionExpAuth class'''
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    '''This class defines how session auth expires'''
    def __init__(self):
        '''Overloading init function'''
        session_duration = getenv("SESSION_DURATION")
        if session_duration:
            self.session_duration = int(session_duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        '''This overloads the create session to add a session dict'''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {}
        session_dict["user_id"] = user_id
        session_dict["created_at"] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''This overloads the useridforsessionid function'''
        if session_id is None:
            return None
        if self.user_id_by_session_id[session_id] is None:
            return None
        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict['user_id']
        if session_dict["created_at"] is None:
            return None
        created_at = session_dict["created_at"]
        if created_at is None:
            return None
        expires = created_at + timedelta(seconds=self.session_duration)
        if expires < datetime.now():
            return None
        return session_dict['user_id']
