#!/usr/bin/env python3
'''Learning TypeVar'''
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    '''Learning TypeVar'''
    if key in dct:
        return dct[key]
    else:
        return default
