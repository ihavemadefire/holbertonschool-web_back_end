#!/usr/bin/env python3
'''This module contains the REDIS exercise'''
from uuid import uuid4
from typing import Union, Callable, Optional
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''This counts the number of times a function has been called'''
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''The wrapper function'''
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''This creates an i/o log'''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''The wrapper function'''
        #pushes input to list stack
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    '''Displays call history'''
    redis_inst = redis.Redis()
    qname = method.__qualname__
    i = redis_inst.get(qname).decode('utf-8')
    input = redis_inst.lrange(qname + ':inputs', 0, -1)
    output = redis_inst.lrange(qname + ':outputs', 0, -1)
    print('{} was called {} times:'.format(qname, i))
    for k, v in zip(input, output):
        print('{}(*{}) -> {}'.format(qname, k.decode('utf-8'),
                                     v.decode('utf-8')))


class Cache():
    '''This is the cache class'''
    def __init__(self):
        '''Initialization function'''
        self._redis = redis.Redis()
        self._redis.flushdb

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''This stores data'''
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        '''This returns a value in its stored form'''
        if fn:
            return fn(self.redis.get(key))
        return self._redis.get(key)
