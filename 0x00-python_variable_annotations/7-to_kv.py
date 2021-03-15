#!/usr/bin/env python3
'''takes in a mixed of key value pairs and returns it as a tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes in a mixed of key value pairs and returns it as a tuple'''
    v = v**2
    return (k, v)
