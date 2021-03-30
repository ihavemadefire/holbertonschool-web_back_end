#!/usr/bin/env python3
'''This module encrypts passwords'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Accepts a password as argument, hashes it and returns it as bytes'''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Checks input against a stored and hashed password '''
    return bcrypt.checkpw(password.encode(), hashed_password)
