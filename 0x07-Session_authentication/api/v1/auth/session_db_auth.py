#!/usr/bin/env python3
'''This module contains the SessionAuth class'''
from api.v1.auth.auth import Auth
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    '''This class stores information about the session in a database'''

    def create_session(self, user_id=None):
        '''Overload create session to store the session in db'''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(session_id=session_id, user_id=user_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''retrieves a user id from a session id'''
        if session_id is None:
            return None
        # can't load with get since I don't have the object Id
        UserSession.load_from_file()
        # Search the list for anything with a session id
        user_sessions = UserSession.search({"session_id": session_id})
        # replicate the other class behavoir
        if self.session_duration >= 0:
            user_sessions[0].user_id
        # iterate over list and find match
        for user_session in user_sessions:
            created_at = user_session.created_at
            exp = created_at + timedelta(seconds=self.session_duration)
            if user_session.session_id == session_id:
                if exp < datetime.now():
                    return None
                return user_session.user_id
        return None

        def destroy_session(self, request=None):
            '''Deletes session and logs user out'''
            if request is None:
                return None
            cookie = self.session_cookie(request)
            if cookie is None:
                return False
            # get user sessionlist out of db as above
            logout_list = UserSession.search({"session_id": session_id})
            # loop through list to find logout and remove it from db
            for logout in logout_list:
                if logout.session_id == session_id:
                    logout.remove()
            return True
