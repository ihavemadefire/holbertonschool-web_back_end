#!/usr/bin/env python3
'''This module contains the basic_auth class'''
from .auth import Auth
from models.user import User
from models.base import DATA
import base64
from typing import TypeVar


class BasicAuth(Auth):
    '''Inherits from auth class for basic auth'''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''returns base64 header'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        '''decodes base64 header'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_decoded = base64.b64encode(base64.b64decode(
                base64_authorization_header))
            if encoded_decoded == base64_authorization_header:
                pass
        except Exception:
            return None
        decoded = base64.b64decode(base64_authorization_header)
        return decoded.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        '''Extracts user data'''
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        a = decoded_base64_authorization_header.split(":")[0]
        b = decoded_base64_authorization_header.split(":")[1]
        return (a, b)

    def user_object_from_credentials(self,
                                     user_email:
                                     str, user_pwd:
                                     str) -> TypeVar('User'):
        '''finds and returns user object'''
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        if User.count() == 0 or not User.search({"email": user_email}):
            return None
        user = User.search({"email": user_email})[0]
        if user.is_valid_password(user_pwd):
            return user
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Overloads the auth and retrieves the user'''
        auth_header = self.authorization_header(request)
        b64_extracted_auth_header = self.extract_base64_authorization_header(
            auth_header)
        b64_decoded_auth_header = self.decode_base64_authorization_header(
            b64_extracted_auth_header)
        user_credentials = self.extract_user_credentials(
            b64_decoded_auth_header)
        current_user = self.user_object_from_credentials(
            user_credentials[0], user_credentials[1])
        return current_user
