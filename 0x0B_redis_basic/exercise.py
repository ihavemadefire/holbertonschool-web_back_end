#!/usr/bin/env python3
'''This module contains the REDIS exercise'''
from uuid import uuid4
from typing import Any
import redis


class Cache:
    '''This is the cache class'''
    def __init__(self):
        '''Initialization function'''
        self._redis = redis.Redis()
        self._redis.flushdb
    
    def store(self, data: Any) -> str:
        '''This stores data'''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
