#!/usr/bin/env python3
""" This module contains the  get page function """
from typing import Callable
import requests
import redis
from functools import wraps


red = redis.Redis()


def count_calls(method: Callable) -> Callable:
    '''This counts the number of times a function has been called'''
    @wraps(method)
    def wrapper(*args, **kwds):
        '''The wrapper function'''
        key = "count:{}".format(args[0])
        red.incr(key, 1)
        red.setex("Count", 10, red.get(key))
        return method(*args, **kwds)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    '''Basic request function'''
    result = requests.get(url)
    return result.text
