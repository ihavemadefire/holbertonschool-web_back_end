#!/usr/bin/env python3
'''Learn to use mypy'''
from typing import Tuple, List, Iterator


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Learn to use mypy'''
    zoomed_in: Iterator = (
        item for item in lst
        for i in range(factor)
    )
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
