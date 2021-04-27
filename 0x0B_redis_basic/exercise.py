#!/usr/bin/env python3
'''This module contains the REDIS exercise'''
from uuid import uuid4
from typing import Union, Callable, Optional
import redis


class Cache:
    '''This is the cache class'''
    def __init__(self):
        '''Initialization function'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''This stores data'''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        '''This returns a value in its stored form'''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
