#!/usr/bin/env python3
'''takes in a mixed list of floats and ints sums them'''
from typing import Mapping


def sum_mixed_list(mxd_lst: Mapping[int, float]) -> float:
    '''takes in a mixed list of floats and ints returns sums'''
    return sum(mxd_lst)
