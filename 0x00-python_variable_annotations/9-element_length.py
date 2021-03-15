#!/usr/bin/env python3
'''takes float as argument; returns function that multiplies it'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''takes float as argument; returns function that multiplies it'''
    return [(i, len(i)) for i in lst]
