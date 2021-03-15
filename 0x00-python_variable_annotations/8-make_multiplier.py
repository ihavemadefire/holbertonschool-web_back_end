#!/usr/bin/env python3
'''takes float as argument; returns function that multiplies it'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''takes float as argument; returns function that multiplies it'''
    def multiball(x: float) -> float:
        return multiplier * x
    return multiball
