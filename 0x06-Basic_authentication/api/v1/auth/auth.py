#!/usr/bin/env python3
'''This module contains the auth class'''
from flask import request
from typing import List, TypeVar


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''This funtion requires auth for endpoints'''
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        '''This function requires auth for enpoints'''
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''This function returns the current user'''
        return None
