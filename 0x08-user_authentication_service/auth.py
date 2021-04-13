#!/usr/bin/env python3
'''This module contains the book of amun ra'''
from typing import ByteString
import bcrypt


def _hash_password(password: str) -> ByteString:
    '''Returns a hashed user password'''
    if password and isinstance(password, str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(str.encode(password), salt)
    return None
